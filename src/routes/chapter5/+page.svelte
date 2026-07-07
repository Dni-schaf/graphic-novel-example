<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSets} from '$lib/data/chapter5_images.js';
  import { imageTexts } from '$lib/data/chapter5_texts.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter5" />

<ComicSection chapterName="chapter5" imageNames={imageSets} {imageTexts}/>
<MapSection dateStart="12.10.1910" dateEnd="01.11.1910" />

