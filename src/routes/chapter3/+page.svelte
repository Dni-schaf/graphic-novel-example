<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSets} from '$lib/data/chapter3_images.js';
  import { imageTexts } from '$lib/data/chapter3_texts.js';
</script>


<ComicSection chapterName="chapter3" imageNames={imageSets} {imageTexts}/>
