<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSets} from '$lib/data/chapter6_images.js';
  import { imageTexts } from '$lib/data/chapter6_texts.js';
</script>

<ComicSection chapterName="chapter6" imageNames={imageSets} {imageTexts}/>
