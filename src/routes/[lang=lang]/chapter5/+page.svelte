<script>
  import ChapterStartSpacer from '$lib/components/ChapterStartSpacer.svelte';
  import ChapterEndSpacer from '$lib/components/ChapterEndSpacer.svelte';
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import PureMap from '$lib/components/pureMap.svelte'; // Großbuchstabe für Komponenten-Konvention
  import { imageSets } from '$lib/data/chapter5_images.js';
  import { imageTexts } from '$lib/data/chapter5_texts.js';
  import { speaker } from '$lib/data/chapter5_speaker.js';
  import { parallaxLayers } from '$lib/data/chapter5_parallax.js';

    // Eine geordnete Liste aller Sections mit Typ und Höhe
  let sections = $state([
    { type: 'comic', height: 0 },  
    { type: 'map',   height: 0, dateStart: "12.10.1910", dateEnd: "01.11.1910"},
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

<PureMap scale={150} rotate={[-70, 0]} chapterName="chapter5" {totalMapHeight}
  {comicHeights} {sections}/>

<ChapterStartSpacer />
<ComicSection id="srt" chapterName="chapter5" imageNames={imageSets} {imageTexts} {parallaxLayers}onHeightChange={(h) => updateHeight(0, h)}/>
<MapSection dateStart="12.10.1910" dateEnd="01.11.1910" sectionId="5a" speakerTexts={speaker} onHeightChange={(h) => updateHeight(1, h)}/>
<ChapterEndSpacer />



