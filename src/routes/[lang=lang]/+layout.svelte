<script>
   import { beforeNavigate, afterNavigate } from '$app/navigation';
   import { tick } from 'svelte';
   import { overlayState } from '$lib/state/overlayState.svelte.js';
   import ChapterLoadingOverlay from '$lib/components/ChapterLoadingOverlay.svelte';
   import { languageState } from '$lib/state/language.svelte.js';

  let { data, children } = $props();
  let navigationId = 0;

  beforeNavigate(({ to }) => {
    if (to?.url.hash) {
      overlayState.visible = true;
    }
  });

  afterNavigate(async ({ to }) => {
    const thisNavigation = ++navigationId; // eigene "Ausweisnummer" für diesen Sprung

    if (!to?.url.hash) {
      window.scrollTo(0, 0);
      overlayState.visible = false;
      return;
    }

    await tick();

    function scrollToTarget() {
      const target = document.getElementById(to.url.hash.slice(1));
      if (target) target.scrollIntoView({ behavior: 'instant', block: 'start' });
    }

    scrollToTarget();

let lastWidth = document.documentElement.clientWidth;
let stableCount = 0;
const maxWait = 2500;
const start = performance.now();

function checkStable() {
  if (thisNavigation !== navigationId) return; // eine neuere Navigation hat übernommen -> abbrechen

  const currentWidth = document.documentElement.clientWidth;
  if (currentWidth === lastWidth) {
    stableCount++;
  } else {
    stableCount = 0;
    lastWidth = currentWidth;
    scrollToTarget();
  }

  const elapsed = performance.now() - start;
  if (stableCount >= 2 || elapsed >= maxWait) {
    overlayState.visible = false;
  } else {
    setTimeout(checkStable, 150);
  }
}

setTimeout(checkStable, 150);
  });


  // Sobald sich der URL-Parameter ändert, synchronisieren wir den globalen State
  $effect(() => {
    languageState.current = data.lang;
  });
</script>

{@render children()}