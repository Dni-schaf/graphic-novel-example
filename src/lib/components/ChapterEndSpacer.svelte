<script>
  import { page } from '$app/state';
  import { goto } from '$app/navigation';
  import { languageState } from '$lib/state/language.svelte.js';
  import { getCurrentChapterNumber, getNextChapterNumber, getNextChapterUrl } from '$lib/utils/chapterNav.js';
  import { onMount } from 'svelte';

  const currentChapter = getCurrentChapterNumber(page.url.pathname);
  const nextChapter = getNextChapterNumber(currentChapter);

  let sentinelElement;
  let hasTriggered = false;

  const texts = {
    de: (n) => `Weiter scrollen bringt dich zu Kapitel ${n}`,
    en: (n) => `Keep scrolling to continue to chapter ${n}`,
    no: (n) => `Fortsett å scrolle for å komme til kapittel ${n}`
  };

  function triggerNext() {
    if (hasTriggered || nextChapter === null) return;
    hasTriggered = true;
    console.log('WÜRDE JETZT SPRINGEN zu Kapitel ' + nextChapter, 'color: red; font-size: 16px; font-weight: bold;');
    console.log('scrollY:', window.scrollY, '| Dokumenthöhe:', document.documentElement.scrollHeight);
    goto(getNextChapterUrl(languageState.current, currentChapter));
    hasTriggered = false;
  }

onMount(() => {
  if (nextChapter === null) return;

  let dwellTimer = null;

  const observer = new IntersectionObserver(
    (entries) => {
        console.log('Sentinel sichtbar:', entries[0].isIntersecting, '| Zeit:', new Date().toLocaleTimeString());
      if (entries[0].isIntersecting) {
        // Erst nach 600ms durchgehender Sichtbarkeit triggern
        dwellTimer = setTimeout(triggerNext, 600);
      } else {
        clearTimeout(dwellTimer);
      }
    },
    { threshold: 0.9 }
  );

  observer.observe(sentinelElement);
  return () => {
    clearTimeout(dwellTimer);
    observer.disconnect();
  };
});
</script>

<div class="chapter-end-spacer" id="chapter-end">
  {#if nextChapter !== null}
    <p class="chapter-transition-hint">
      {texts[languageState.current]?.(nextChapter) || texts.de(nextChapter)}
    </p>
    <a style="position: absolute; bottom:0% " href={getNextChapterUrl(languageState.current, currentChapter)}> 
      next
    </a>
  {/if}
  <div class="sentinel" bind:this={sentinelElement}></div>
</div>

<style>
  .chapter-end-spacer {
    position: relative;
    height: 200vh;
    display: flex;
    justify-content: center;
    padding-top: 10vh;
  }
  .chapter-transition-hint {
    font-size: 1rem;
    opacity: 0.6;
    text-align: center;
  }
  .sentinel {
    position: absolute;
    bottom: 0;
    height: 10px;
    width: 100%;
  }
</style>