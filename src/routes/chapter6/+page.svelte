<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSets} from '$lib/data/chapter6_images.js';
  import { imageTexts } from '$lib/data/chapter6_texts.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter6"/>

<ComicSection chapterName="chapter6" imageNames={imageSets} {imageTexts}/>
<MapSection dateStart="02.11.1910" dateEnd="25.11.1910" />

