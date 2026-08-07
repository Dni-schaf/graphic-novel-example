<script>
  import ChapterEndSpacer from '$lib/components/ChapterEndSpacer.svelte';
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import PureMap from '$lib/components/pureMap.svelte'; // Großbuchstabe für Komponenten-Konvention
  import { imageSetA, imageSetB } from '$lib/data/chapter1_images.js';
  import { imageTexts } from '$lib/data/chapter1_texts.js';
  import { speaker } from '$lib/data/chapter1_speaker.js';
  import { curvedTexts } from '$lib/data/chapter1_curvedTexts.js';
  import { parallaxLayers } from '$lib/data/chapter1_parallax.js';



    // Eine geordnete Liste aller Sections mit Typ und Höhe
  let sections = $state([
    { type: 'comic', height: 0 },  // ComicSection A
    { type: 'map',   height: 0, dateStart: "02.06.1910", dateEnd: "14.06.1910", mapScale: 600, mapRotate: [0, -50]},  // MapSection 1a
    { type: 'comic', height: 0 },  // ComicSection B
    { type: 'map',   height: 0, dateStart: "15.06.1910", dateEnd: "09.08.1910" },  // MapSection 1b
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

<PureMap scale={150} rotate={[-70, 0]} chapterName="chapter1" {totalMapHeight}
  {comicHeights} {sections}/>

<ComicSection id="srt" chapterName="chapter1" imageNames={imageSetA} {imageTexts} {curvedTexts} {parallaxLayers} onHeightChange={(h) => updateHeight(0, h)}/>
<MapSection dateStart="02.06.1910" dateEnd="14.06.1910" sectionId="1a" speakerTexts={speaker} onHeightChange={(h) => updateHeight(1, h)} />

<ComicSection chapterName="chapter1" imageNames={imageSetB} {imageTexts} {curvedTexts} {parallaxLayers} onHeightChange={(h) => updateHeight(2, h)}/>
<MapSection dateStart="15.06.1910" dateEnd="09.08.1910" sectionId="1b" speakerTexts={speaker} onHeightChange={(h) => updateHeight(3, h)}/>
<ChapterEndSpacer />

<!--
<div style="position: fixed; bottom: 10px; right: 10px; background: yellow; z-index: 999;">
  {#each sections as s, i}
    <p>{i}: {s.type} — {s.height.toFixed(0)}px</p>
  {/each}
</div>

-->