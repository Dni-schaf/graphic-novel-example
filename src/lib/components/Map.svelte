<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import * as topojson from 'topojson-client';

  import { Amundsen } from '$lib/data/AmundsenData.js';
  import { Scott } from '$lib/data/ScottData.js';
  import { cityLabels } from '$lib/data/cityLabels.js';
  import { languageState } from '$lib/state/language.svelte.js';
  import { mapState } from '$lib/state/mapState.svelte.js';

  let { scale, rotate, chapterName} = $props();

  let scottLengths = { lengths: [], times: [] };
  let amundsenLengths = { lengths: [], times: [] };

  function drawLabels(labels, svglabel, projection, chapterName) {
  labels.forEach((label) => {
    if (!label.visibleInChapters.includes(chapterName)) return;

    const coords = projection([label.lng, label.lat]);

    svglabel.append("circle")
      .attr("cx", coords[0])
      .attr("cy", coords[1])
      .attr("r", 3)
      .attr("class", "city-circle" + " " + label.text_de);

    svglabel.append("text")
      .attr("x", coords[0])
      .attr("y", coords[1])
      .attr("dx", "8px")
      .attr("dy", "0.35em") 
      .attr("class", label.kind)
      .text(label[`text_${languageState.current}`] || label.text_de);
  });
  }

  function drawPath(dataset, svgpath, projection) {
          const datecount = dataset.length;
    
  //es wir je eine linie zwischen 2 tagen gezeichnet
  for (let i = 0; i < datecount - 1; i++){
    const start = projection([dataset[i].lng, dataset[i].lat]);
    const end = projection([dataset[i+1].lng, dataset[i+1].lat]);
    
      const lines = svgpath
        .append("line")
        .style("stroke-width", 2)
        // first point: first date
        .attr("x1", function (index) { 
          let longitude = projection([dataset[i].lng,dataset[i].lat]);
          return longitude[0];
        })
        .attr("y1", function (index) { 
          let latitude = projection([dataset[i].lng,dataset[i].lat]);
          return latitude[1];
        })
        // second point: second date
        .attr("x2", function (index) { 
          let longitude = projection([dataset[i+1].lng,dataset[i+1].lat]);
          return longitude[0];
        })
        .attr("y2", function (index) { 
          let latitude = projection([dataset[i+1].lng,dataset[i+1].lat]);
          return latitude[1];
        })
        .attr("id", function (index) {
          let setID = dataset[i+1].team + i
          return setID;
        })
        .attr("class", dataset[i].team);
    }
  };

  function fillLength(dataset, team) {
    const lengths = [];
    const times = [];
  
    for (let i = 0; i < dataset.length - 1; i++) {
      const lineElement = document.getElementById(team + i);
      if (lineElement) {
        lengths.push(lineElement.getTotalLength());
        times.push(dataset[i+1].timestamp - dataset[i].timestamp);
      }
    }
    return { lengths, times };
  }



  function hidelines(lengths, team) {
    lengths.forEach((length, i) => {
      d3.select("#" + team + i)
        .attr("stroke-dasharray", length)
        .attr("stroke-dashoffset", length);
    });
  }

  function updatePath(dataset, team, lengths, times) {
    const currentTime = mapState.dateStart + mapState.progress * (mapState.dateEnd - mapState.dateStart);

    for (let i = 0; i < dataset.length - 1; i++) {
          if (lengths[i] === 0) continue; // ← Null-Längen überspringen

      const lineTimestamp = dataset[i].timestamp;
      const nextTimestamp = dataset[i + 1].timestamp;

      if (currentTime / 1000 >= nextTimestamp) {
        // Linie komplett sichtbar
        d3.select("#" + team + i).attr("stroke-dashoffset", 0);
      } else if (currentTime / 1000 <= lineTimestamp) {
        // Linie komplett versteckt
        d3.select("#" + team + i).attr("stroke-dashoffset", lengths[i]);
      } else {
        // Linie gerade im Aufzeichnen
        const segmentProgress = (currentTime / 1000 - lineTimestamp) / times[i];
        const dashoffset = lengths[i] * (1 - segmentProgress);
        d3.select("#" + team + i).attr("stroke-dashoffset", dashoffset);
      }
    }
  }

  function drawEverything() {
    // Bestehenden Inhalt zuerst löschen, damit nicht doppelt gezeichnet wird
    d3.select("#map").select("svg").remove();
    d3.select("#ice").select("svg").remove();
    d3.select("#grid").select("svg").remove();
    d3.select("#path").select("svg").remove();
    d3.select("#label").select("svg").remove();

    const breite = window.innerWidth;
    const hoehe = window.innerHeight;
    const halbbreit = breite / 2;
    const halbhoehe = hoehe / 2;

    const svgmap = d3.select("#map").append("svg")
      .attr("width", breite)
      .attr("height", hoehe);

    const svgice = d3.select("#ice").append("svg")
      .attr("width", breite)
      .attr("height", hoehe);

    const svggrid = d3.select("#grid").append("svg")
      .attr("width", breite)
      .attr("height", hoehe);

    const projection = d3.geoAzimuthalEqualArea()
      .rotate(rotate)
      .scale(scale)
      .translate([halbbreit, halbhoehe]);

    const path = d3.geoPath().projection(projection);

    const graticule = d3.geoGraticule().step([20, 15]);

    const svgpath = d3.select("#path").append("svg")
      .attr("width", breite)
      .attr("height", hoehe);

    const svglabel = d3.select("#label").append("svg")
      .attr("width", breite)
      .attr("height", hoehe);

    // Eis laden und zeichnen
    d3.json("https://gist.githubusercontent.com/ScharffenBerg/5fb9342bb4abe86bec09230d90275197/raw/4bfb48ab30681e6ec441b0d8a2d7a5da6583900a/Shelf_Ice_Data.json").then((ice) => {
      svgice.append("g")
        .attr("class", "iceshelf")
        .selectAll("path")
        .data(ice.features)
        .enter().append("path")
        .attr('d', path)
        .attr("class", "ice");
    });

    // Welt laden und zeichnen
    d3.json("https://unpkg.com/world-atlas@1.1.4/world/110m.json").then((world) => {
      svgmap.append("path")
        .datum(graticule.outline)
        .attr("class", "foreground")
        .attr("d", path);

      svgmap.append("g")
        .selectAll("path")
        .data(topojson.feature(world, world.objects.countries).features)
        .enter().append("path")
        .attr("d", path)
        .attr("class", "map");

      svggrid.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);
    });

    drawPath(Scott, svgpath, projection);
    drawPath(Amundsen, svgpath, projection);

    scottLengths = fillLength(Scott, "Scott");
console.log("Erste 3 Längen:", scottLengths.lengths.slice(0, 3));
console.log("Hat NaN?", scottLengths.lengths.some(l => isNaN(l)));
console.log("Hat Null?", scottLengths.lengths.some(l => l === 0));
    amundsenLengths = fillLength(Amundsen, "Amundsen");
    
    
    hidelines(scottLengths.lengths, "Scott");
    hidelines(amundsenLengths.lengths, "Amundsen");

    drawLabels(cityLabels, svglabel, projection, chapterName)
    // Längen berechnen und Linien verstecken

  };


let isReady = $state(false); // ← NEU: Flag, ob Karte gezeichnet ist

onMount(() => {
    drawEverything();
    isReady = true; // ← NEU: erst jetzt ist alles bereit


    let resizeTimeout;
    window.addEventListener("resize", () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
          drawEverything();
          // nach Resize auch neu verstecken
          hidelines(scottLengths.lengths, "Scott");
          hidelines(amundsenLengths.lengths, "Amundsen");
        }, 150);
    });
});

$effect(() => {
    // ← NEU: nur ausführen wenn Karte bereit ist
    if (isReady && mapState.progress > 0 && scottLengths.lengths.length > 0) {
        updatePath(Scott, "Scott", scottLengths.lengths, scottLengths.times);
        updatePath(Amundsen, "Amundsen", amundsenLengths.lengths, amundsenLengths.times);
    }
});

</script>

<div id="map"></div>
<div id="ice"></div>
<div id="grid"></div>
<div id="path"></div>
<div id="label"></div>