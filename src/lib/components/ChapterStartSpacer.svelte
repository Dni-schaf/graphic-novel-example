<script>
  import { page } from '$app/state';
  import { goto } from '$app/navigation';
  import { languageState } from '$lib/state/language.svelte.js';
  import { getCurrentChapterNumber, getPrevChapterNumber, getPrevChapterUrl } from '$lib/utils/chapterNav.js';
  import { onMount } from 'svelte';
    import { smoothScrollTo } from '$lib/utils/smoothScroll.js';


  const currentChapter = getCurrentChapterNumber(page.url.pathname);
  const prevChapter = getPrevChapterNumber(currentChapter);


  const texts = {
    de: (n) => `Zurück zu Kapitel ${n}`,
    en: (n) => `Back to chapter ${n}`,
    no: (n) => `Tilbake til kapittel ${n}`
  };

  onMount(() => {
    requestAnimationFrame(() => {
      smoothScrollTo(window.innerHeight * 1.2);
    });
  });

</script>

<div class="chapter-start-spacer">
  {#if prevChapter !== null}
    <p><span class="arrow-up">&#9001;</span></p>
    <a style="position: absolute; top:0 " href={getPrevChapterUrl(languageState.current, currentChapter)}> 
      <span class="chapter-transition-hint">
      {texts[languageState.current]?.(prevChapter) || texts.de(prevChapter)}
    </span>
    </a>
  {/if}
</div>

<style>
.arrow-up {
  display: inline-block;
  transform: rotate(90deg);
  color: white;
}

  .chapter-start-spacer {
    position: relative;
    height: 100vh;
    display: flex;
    justify-content: center;
    padding-bottom: 10vh;
  }
  .chapter-transition-hint {
    font-size: 1rem;
    width: 16vw;
    transform: translateX(-50%) translateY(100%);
    text-align: center;
    position: absolute;
    background: #6F8193;
    color:  white;
    padding: 0.5rem 1rem;
    border-color: white;
    border-style: solid;
    border-width: 2px;
    font-family: "chapter";
    border-bottom-left-radius: 17px 255px;
    border-bottom-right-radius: 15px 20px;
    border-top-left-radius: 15px 15px;
    border-top-right-radius: 20px 225px;
  }

</style>