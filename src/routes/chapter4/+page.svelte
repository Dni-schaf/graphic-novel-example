<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSetA, imageSetB, imageSetC, imageSetD } from '$lib/data/chapter4_images.js';
  import { imageTexts } from '$lib/data/chapter4_texts.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter4"/>

<ComicSection chapterName="chapter4" imageNames={imageSetA} {imageTexts}/>
<MapSection dateStart="10.09.1910" dateEnd="15.09.1910" />

<ComicSection chapterName="chapter4" imageNames={imageSetB} {imageTexts}/>
<MapSection dateStart="15.09.1910" dateEnd="25.09.1910" />

<ComicSection chapterName="chapter4" imageNames={imageSetC} {imageTexts}/>
<MapSection dateStart="25.09.1910" dateEnd="01.10.1910" />

<ComicSection chapterName="chapter4" imageNames={imageSetD} {imageTexts}/>
<MapSection dateStart="01.10.1910" dateEnd="11.10.1910" />
