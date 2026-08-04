<script>
  import ChapterStartSpacer from '$lib/components/ChapterStartSpacer.svelte';
  import ChapterEndSpacer from '$lib/components/ChapterEndSpacer.svelte';
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import PureMap from '$lib/components/pureMap.svelte'; // Großbuchstabe für Komponenten-Konvention
  import { imageSets } from '$lib/data/chapter6_images.js';
  import { imageTexts } from '$lib/data/chapter6_texts.js';
  import { speaker } from '$lib/data/chapter6_speaker.js';

    // Eine geordnete Liste aller Sections mit Typ und Höhe
  let sections = $state([
    { type: 'comic', height: 0 },  
    { type: 'map',   height: 0, dateStart: "02.11.1910", dateEnd: "25.11.1910"},  // MapSection 1a
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

<PureMap scale={150} rotate={[-70, 0]} chapterName="chapter6" {totalMapHeight}
  {comicHeights} {sections}/>

<ChapterStartSpacer />
<ComicSection id="srt" chapterName="chapter6" imageNames={imageSets} {imageTexts} onHeightChange={(h) => updateHeight(0, h)}/>
<MapSection dateStart="02.11.1910" dateEnd="25.11.1910" sectionId="6a" speakerTexts={speaker} onHeightChange={(h) => updateHeight(1, h)}/>
<ChapterEndSpacer />



