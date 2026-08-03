<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import PureMap from '$lib/components/pureMap.svelte'; // Großbuchstabe für Komponenten-Konvention
  import { imageSetA, imageSetB, imageSetC, imageSetD } from '$lib/data/chapter4_images.js';
  import { imageTexts } from '$lib/data/chapter4_texts.js';

    // Eine geordnete Liste aller Sections mit Typ und Höhe
  let sections = $state([
    { type: 'comic', height: 0 },  // ComicSection A
    { type: 'map',   height: 0, dateStart: "10.09.1910", dateEnd: "15.09.1910"},
    { type: 'comic', height: 0 },  // ComicSection B
    { type: 'map',   height: 0, dateStart: "15.09.1910", dateEnd: "25.09.1910" },
    { type: 'comic', height: 0 },  // ComicSection C
    { type: 'map',   height: 0, dateStart: "25.09.1910", dateEnd: "01.10.1910" },
    { type: 'comic', height: 0 },  // ComicSection D
    { type: 'map',   height: 0, dateStart: "01.10.1910", dateEnd: "11.10.1910" },
  ]);

  function updateHeight(index, height) {
    sections[index] = { ...sections[index], height };
  }

let totalMapHeight = $derived(
  sections
    .filter(s => s.type === 'map')
    .reduce((sum, s) => sum + s.height, 0)
);

let comicHeights = $derived(
  sections.map(s => s.type === 'comic' ? s.height : 0)
);

</script>

<PureMap scale={150} rotate={[-70, 0]} chapterName="chapter4" {totalMapHeight}
  {comicHeights} {sections}/>

<ComicSection chapterName="chapter4" imageNames={imageSetA} {imageTexts} onHeightChange={(h) => updateHeight(0, h)}/>
<MapSection dateStart="10.09.1910" dateEnd="15.09.1910" onHeightChange={(h) => updateHeight(1, h)}/>

<ComicSection chapterName="chapter4" imageNames={imageSetB} {imageTexts} onHeightChange={(h) => updateHeight(2, h)}/>
<MapSection dateStart="15.09.1910" dateEnd="25.09.1910" onHeightChange={(h) => updateHeight(3, h)}/>

<ComicSection chapterName="chapter4" imageNames={imageSetC} {imageTexts} onHeightChange={(h) => updateHeight(4, h)}/>
<MapSection dateStart="25.09.1910" dateEnd="01.10.1910" onHeightChange={(h) => updateHeight(5, h)}/>

<ComicSection chapterName="chapter4" imageNames={imageSetD} {imageTexts} onHeightChange={(h) => updateHeight(6, h)}/>
<MapSection dateStart="01.10.1910" dateEnd="11.10.1910" onHeightChange={(h) => updateHeight(7, h)}/>
<div class="chapter-end-spacer" style="height: 200vh;"></div>

<!--
<div style="position: fixed; bottom: 10px; right: 10px; background: yellow; z-index: 999;">
  {#each sections as s, i}
    <p>{i}: {s.type} — {s.height.toFixed(0)}px</p>
  {/each}
</div>

-->