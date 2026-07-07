<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import * as topojson from 'topojson-client';

  import { Amundsen } from '$lib/data/AmundsenData.js';
  import { Scott } from '$lib/data/ScottData.js';

  let { scale, rotate } = $props();

  let isReady = $state(false);
  let scrollY = $state(0);
  let scottLengths = { lengths: [], times: [] };
  let amundsenLengths = { lengths: [], times: [] };

  // Scroll-Fortschritt: 0 = oben, 1 = unten
  let progress = $derived.by(() => {
    if (typeof document === 'undefined') return 0;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    return scrollHeight > 0 ? Math.max(0, Math.min(1, scrollY / scrollHeight)) : 0;
  });

  function drawPath(dataset, svgpath, projection) {
    const datecount = dataset.length;
    for (let i = 0; i < datecount - 1; i++) {
      const start = projection([dataset[i].lng, dataset[i].lat]);
      const end = projection([dataset[i+1].lng, dataset[i+1].lat]);
      svgpath.append("line")
        .style("stroke-width", 2)
        .attr("x1", start[0])
        .attr("y1", start[1])
        .attr("x2", end[0])
        .attr("y2", end[1])
        .attr("id", dataset[i+1].team + i)
        .attr("class", dataset[i].team);
    }
  }

  function fillLength(dataset, team) {
    const lengths = [];
    const times = [];
    for (let i = 0; i < dataset.length - 1; i++) {
      const el = document.getElementById(team + i);
      if (el) {
        lengths.push(el.getTotalLength());
        times.push(dataset[i+1].timestamp - dataset[i].timestamp);
      }
    }
    return { lengths, times };
  }

  function hidelines(lengths, team) {
    lengths.forEach((length, i) => {
      if (length === 0) return;
      d3.select("#" + team + i)
        .attr("stroke-dasharray", length)
        .attr("stroke-dashoffset", length);
    });
  }

  function updatePath(dataset, team, lengths, times) {
    const startTimestamp = dataset[0].timestamp;
    const endTimestamp = dataset[dataset.length - 1].timestamp;
    const currentTime = startTimestamp + progress * (endTimestamp - startTimestamp);

    for (let i = 0; i < dataset.length - 1; i++) {
      if (lengths[i] === 0) continue;
      const lineTimestamp = dataset[i].timestamp;
      const nextTimestamp = dataset[i+1].timestamp;

      if (currentTime >= nextTimestamp) {
        d3.select("#" + team + i).attr("stroke-dashoffset", 0);
      } else if (currentTime <= lineTimestamp) {
        d3.select("#" + team + i).attr("stroke-dashoffset", lengths[i]);
      } else {
        const segmentProgress = (currentTime - lineTimestamp) / times[i];
        const dashoffset = lengths[i] * (1 - segmentProgress);
        d3.select("#" + team + i).attr("stroke-dashoffset", dashoffset);
      }
    }
  }

  function drawEverything() {
    d3.select("#map").select("svg").remove();
    d3.select("#ice").select("svg").remove();
    d3.select("#grid").select("svg").remove();
    d3.select("#path").select("svg").remove();

    const breite = window.innerWidth;
    const hoehe = window.innerHeight;

    const svgmap = d3.select("#map").append("svg").attr("width", breite).attr("height", hoehe);
    const svgice = d3.select("#ice").append("svg").attr("width", breite).attr("height", hoehe);
    const svggrid = d3.select("#grid").append("svg").attr("width", breite).attr("height", hoehe);
    const svgpath = d3.select("#path").append("svg").attr("width", breite).attr("height", hoehe);

    const projection = d3.geoAzimuthalEqualArea()
      .rotate(rotate)
      .scale(scale)
      .translate([breite / 2, hoehe / 2]);

    const path = d3.geoPath().projection(projection);
    const graticule = d3.geoGraticule().step([20, 15]);

    Promise.all([
      d3.json("https://gist.githubusercontent.com/ScharffenBerg/5fb9342bb4abe86bec09230d90275197/raw/4bfb48ab30681e6ec441b0d8a2d7a5da6583900a/Shelf_Ice_Data.json"),
      d3.json("https://unpkg.com/world-atlas@1.1.4/world/110m.json")
    ]).then(([ice, world]) => {
      svgice.append("g")
        .attr("class", "iceshelf")
        .selectAll("path")
        .data(ice.features)
        .enter().append("path")
        .attr('d', path)
        .attr("class", "ice");

      svgmap.append("path").datum(graticule.outline).attr("class", "foreground").attr("d", path);
      svgmap.append("g")
        .selectAll("path")
        .data(topojson.feature(world, world.objects.countries).features)
        .enter().append("path")
        .attr("d", path)
        .attr("class", "map");
      svggrid.append("path").datum(graticule).attr("class", "graticule").attr("d", path);

      drawPath(Scott, svgpath, projection);
      drawPath(Amundsen, svgpath, projection);

      scottLengths = fillLength(Scott, "Scott");
      amundsenLengths = fillLength(Amundsen, "Amundsen");

      hidelines(scottLengths.lengths, "Scott");
      hidelines(amundsenLengths.lengths, "Amundsen");

      isReady = true;
    });
  }

  $effect(() => {
    if (isReady && scottLengths.lengths.length > 0) {
      updatePath(Scott, "Scott", scottLengths.lengths, scottLengths.times);
      updatePath(Amundsen, "Amundsen", amundsenLengths.lengths, amundsenLengths.times);
    }
  });

  onMount(() => {
    drawEverything();

    let resizeTimeout;
    window.addEventListener("resize", () => {
      clearTimeout(resizeTimeout);
      resizeTimeout = setTimeout(drawEverything, 150);
    });
  });
</script>

<svelte:window bind:scrollY />

<div id="map"></div>
<div id="ice"></div>
<div id="grid"></div>
<div id="path"></div>