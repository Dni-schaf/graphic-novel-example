<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import MapSection from '$lib/components/MapSection.svelte';
  import Map from '$lib/components/Map.svelte';
  import { imageSetA, imageSetB } from '$lib/data/chapter1_images.js';
  import { imageTexts } from '$lib/data/chapter1_texts.js';
  import { mapState } from '$lib/state/mapState.svelte.js';
</script>

<Map scale={150} rotate={[-70, 0]} chapterName="chapter1" />

<ComicSection chapterName="chapter1" imageNames={imageSetA} {imageTexts}/>
<MapSection dateStart="02.06.1910" dateEnd="14.06.1910" />

<ComicSection chapterName="chapter1" imageNames={imageSetB} {imageTexts}/>
<MapSection dateStart="15.06.1910" dateEnd="09.08.1910" />


<div style="position: fixed; top: 50px; left: 10px; background: white; z-index: 100; padding: 5px;">
  mapState progress: {mapState.progress.toFixed(2)}
</div>

<!--
const datestart_1A = "02.06.1910";
const dateend_1A = "14.06.1910";

const datestart_1B = "02.06.1910";
const dateend_1B = "14.06.1910";

const datestart_2 = "02.06.1910";
const dateend_2 = "14.06.1910";

const datestart_3 = "02.06.1910";
const dateend_3 = "14.06.1910";

const datestart_4A = "02.06.1910";
const dateend_4A = "14.06.1910";

const datestart_4B = "02.06.1910";
const dateend_4B = "14.06.1910";

const datestart_4C = "02.06.1910";
const dateend_4C = "14.06.1910";

const datestart_4D = "02.06.1910";
const dateend_4D = "14.06.1910";

const datestart_5 = "02.06.1910";
const dateend_5 = "14.06.1910";

const datestart_6 = "02.06.1910";
const dateend_6 = "14.06.1910";
-->