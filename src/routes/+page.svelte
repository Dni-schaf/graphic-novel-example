<script>
  import MenuContent from '$lib/components/MenuContent.svelte';
  import { languageState } from '$lib/state/language.svelte.js';
</script>

<button onclick={() => languageState.current = 'de'}>DE</button>
<button onclick={() => languageState.current = 'en'}>EN</button>
<button onclick={() => languageState.current = 'no'}>NO</button>

<MenuContent />
