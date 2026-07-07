<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSets} from '$lib/data/chapter3_images.js';
  import { imageTexts } from '$lib/data/chapter3_texts.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter3"/>

<ComicSection chapterName="chapter3" imageNames={imageSets} {imageTexts}/>
<MapSection dateStart="09.09.1910" dateEnd="10.09.1910" />
