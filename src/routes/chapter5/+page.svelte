<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { languageState } from '$lib/state/language.svelte.js';
  import { imageSets} from '$lib/data/chapter5_images.js';
  import { imageTexts } from '$lib/data/chapter5_texts.js';
</script>

<button onclick={() => languageState.current = 'de'}>DE</button>
<button onclick={() => languageState.current = 'en'}>EN</button>
<button onclick={() => languageState.current = 'no'}>NO</button>

<ComicSection chapterName="chapter5" imageNames={imageSets} {imageTexts}/>
