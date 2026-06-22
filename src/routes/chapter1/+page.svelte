<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { languageState } from '$lib/state/language.svelte.js';
  import { imageSetA, imageSetB } from '$lib/data/chapter1_images.js';
  import { imageTexts } from '$lib/data/chapter1_texts.js';
</script>

<button onclick={() => languageState.current = 'de'}>DE</button>
<button onclick={() => languageState.current = 'en'}>EN</button>
<button onclick={() => languageState.current = 'no'}>NO</button>

<ComicSection chapterName="chapter1" imageNames={imageSetA} {imageTexts}/>
<ComicSection chapterName="chapter1" imageNames={imageSetB} {imageTexts}/>