<script>
  import { page } from '$app/state';
  import { goto } from '$app/navigation';
  import { languageState } from '$lib/state/language.svelte.js';
  import { getCurrentChapterNumber, getNextChapterNumber, getNextChapterUrl } from '$lib/utils/chapterNav.js';
  import { onMount } from 'svelte';

  const currentChapter = getCurrentChapterNumber(page.url.pathname);
  const nextChapter = getNextChapterNumber(currentChapter);

  const texts = {
    de: (n) => `Weiter zu Kapitel ${n}`,
    en: (n) => `Proceed to chapter ${n}`,
    no: (n) => `Fortsett til kapittel ${n}`
  };
</script>

<div class="chapter-end-spacer" id="end">
  {#if nextChapter !== null}
    <a style="position: absolute; bottom:0% " href={getNextChapterUrl(languageState.current, currentChapter)}> 
      <span class="chapter-transition-hint">
      {texts[languageState.current]?.(nextChapter) || texts.de(nextChapter)}
    </span>
    </a>
    <p><span class="arrow-up">&#9001;</span></p>

  {/if}
</div>

<style>
.arrow-up {
  display: inline-block;
  transform: rotate(-90deg);
  color: white;
  position: absolute;
  bottom: 1vh;
}
  .chapter-end-spacer {
    position: relative;
    height: 200vh;
    display: flex;
    justify-content: center;
    padding-top: 10vh;
  }
    .chapter-transition-hint {
    font-size: 1rem;
    width: 16vw;
    transform: translateX(-50%) translateY(-200%);
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