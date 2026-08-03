<script>
  import { afterNavigate } from '$app/navigation';
  import { languageState } from '$lib/state/language.svelte.js';

  let { data, children } = $props();

    afterNavigate(({ to }) => {
    if (to?.url.hash) {
      const target = document.getElementById(to.url.hash.slice(1));
      if (target) {
        target.scrollIntoView({ behavior: 'instant', block: 'start' });
      }
    } else {
      window.scrollTo(0, 0);
    }
  });


  // Sobald sich der URL-Parameter ändert, synchronisieren wir den globalen State
  $effect(() => {
    languageState.current = data.lang;
  });
</script>

{@render children()}