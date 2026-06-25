<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSetA, imageSetB, imageSetC, imageSetD } from '$lib/data/chapter4_images.js';
  import { imageTexts } from '$lib/data/chapter4_texts.js';
</script>

<ComicSection chapterName="chapter4" imageNames={imageSetA} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetB} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetC} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetD} {imageTexts}/>