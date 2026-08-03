<script>
  import { page } from '$app/state';
  import { goto } from '$app/navigation';
  import { languageState } from '$lib/state/language.svelte.js';
  import { getCurrentChapterNumber, getPrevChapterNumber, getPrevChapterUrl } from '$lib/utils/chapterNav.js';
  import { onMount } from 'svelte';

  const currentChapter = getCurrentChapterNumber(page.url.pathname);
  const prevChapter = getPrevChapterNumber(currentChapter);

  let sentinelElement;
  let hasTriggered = false;

  const texts = {
    de: (n) => `Weiter scrollen bringt dich zu Kapitel ${n}`,
    en: (n) => `Keep scrolling to continue to chapter ${n}`,
    no: (n) => `Fortsett å scrolle for å komme til kapittel ${n}`
  };

  function triggerNext() {
    if (hasTriggered || prevChapter === null) return;
    hasTriggered = true;
    console.log('WÜRDE JETZT SPRINGEN zu Kapitel ' + prevChapter, 'color: red; font-size: 16px; font-weight: bold;');
    console.log('scrollY:', window.scrollY, '| Dokumenthöhe:', document.documentElement.scrollHeight);
    goto(getPrevChapterUrl(languageState.current, currentChapter));
    hasTriggered = false;
  }

onMount(() => {
  if (prevChapter === null) return;

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

<div class="chapter-start-spacer">
  {#if prevChapter !== null}
    <p class="chapter-transition-hint">
      {texts[languageState.current]?.(prevChapter) || texts.de(prevChapter)}
    </p>
    <a style="position: absolute; top:0 " href={getPrevChapterUrl(languageState.current, currentChapter)}> 
      prev
    </a>
  {/if}
  <div class="sentinel" bind:this={sentinelElement}></div>
</div>

<style>
  .chapter-start-spacer {
    position: relative;
    height: 100vh;
    display: flex;
    justify-content: center;
    padding-bottom: 10vh;
  }
  .chapter-transition-hint {
    font-size: 1rem;
    opacity: 0.6;
    text-align: center;
    position: absolute;
    bottom: 0;
  }
  .sentinel {
    position: absolute;
    top: 0;
    height: 10px;
    width: 100%;
  }
</style>