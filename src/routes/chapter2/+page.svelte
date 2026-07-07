<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSets } from '$lib/data/chapter2_images.js';
  import { imageTexts } from '$lib/data/chapter2_texts.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter2"/>

<ComicSection chapterName="chapter2" imageNames={imageSets} {imageTexts}/>
<MapSection dateStart="09.08.1910" dateEnd="06.09.1910" />