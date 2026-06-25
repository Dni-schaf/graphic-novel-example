<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSets } from '$lib/data/chapter2_images.js';
  import { imageTexts } from '$lib/data/chapter2_texts.js';
</script>

<ComicSection chapterName="chapter2" imageNames={imageSets} {imageTexts}/>
