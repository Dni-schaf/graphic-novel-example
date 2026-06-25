<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { imageSets} from '$lib/data/chapter5_images.js';
  import { imageTexts } from '$lib/data/chapter5_texts.js';
</script>


<ComicSection chapterName="chapter5" imageNames={imageSets} {imageTexts}/>
