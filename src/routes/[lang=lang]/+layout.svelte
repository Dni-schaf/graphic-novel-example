<script>
  import { languageState } from '$lib/state/language.svelte.js';

  let { data, children } = $props();

  // Sobald sich der URL-Parameter ändert, synchronisieren wir den globalen State
  $effect(() => {
    languageState.current = data.lang;
  });
</script>

{@render children()}