<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSetA, imageSetB } from '$lib/data/chapter1_images.js';
  import { imageTexts } from '$lib/data/chapter1_texts.js';
</script>


<ComicSection chapterName="chapter1" imageNames={imageSetA} {imageTexts}/>
<ComicSection chapterName="chapter1" imageNames={imageSetB} {imageTexts}/>