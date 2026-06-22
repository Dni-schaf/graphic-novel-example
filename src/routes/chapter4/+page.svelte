<script>
  import ComicSection from '$lib/components/ComicSection.svelte';
  import { languageState } from '$lib/state/language.svelte.js';
  import { imageSetA, imageSetB, imageSetC, imageSetD } from '$lib/data/chapter4_images.js';
  import { imageTexts } from '$lib/data/chapter4_texts.js';
</script>

<button onclick={() => languageState.current = 'de'}>DE</button>
<button onclick={() => languageState.current = 'en'}>EN</button>
<button onclick={() => languageState.current = 'no'}>NO</button>

<ComicSection chapterName="chapter4" imageNames={imageSetA} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetB} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetC} {imageTexts}/>
<ComicSection chapterName="chapter4" imageNames={imageSetD} {imageTexts}/>