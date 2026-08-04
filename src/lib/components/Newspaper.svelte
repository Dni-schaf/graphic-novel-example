<script>
  import '../styles/newspaper.css';
  import { languageState } from '$lib/state/language.svelte.js';
  import { newspaperContent } from '$lib/data/chapter1_newspaper.js';

  let { imageName } = $props();

  let content = $derived(newspaperContent[imageName]);

  function t(entry) {
    return entry?.[`text_${languageState.current}`] || entry?.text_de || "";
  }
</script>

{#if content}
  <div class="newspaper-wrapper">

    <div class="newsticker">
      <div class="ticker-text">{t(content.tickertext1)}</div>
      <div class="ticker-text">{t(content.tickertext2)}</div>
      <div class="ticker-text">{t(content.tickertext3)}</div>
    </div>

    <div id="titel">{t(content.title)}</div>

    <div class="newspaperdate">
      <div class="date-text number">{t(content.number)}</div>
      <div class="date-text">{t(content.date)}</div>
      <div class="date-text price">{t(content.price)}</div>
    </div>

    <div class="intro">
      <div class="intro-text">
        <p class="intro-paragraph-1">{t(content.p1)}</p>
        <p class="intro-paragraph-2">{t(content.p2)}</p>
        <p class="intro-paragraph-3">{t(content.p3)}</p>
      </div>
      <div class="intro-image"></div>
    </div>

    <div class="newspaper">
      <div class="column-area">
        <div class="flow-text">
          <p class="subheadline">{t(content.p4.subheadline)}</p>
          <p class="content">{t(content.p4.content)}</p>
          <p class="subheadline">{t(content.p6.subheadline)}</p>
          <p class="content">{t(content.p6.content)}</p>
          <p class="subheadline">{t(content.p8.subheadline)}</p>
          <p class="content">{t(content.p8.content)}</p>
          <p class="subheadline">{t(content.p10.subheadline)}</p>
          <p class="content">{t(content.p10.content)}</p>
        </div>
      </div>
    </div>

    <div class="part4">
      <div class="part4-image"></div>
      <div class="part4-text">
        <p class="subheadline">{t(content.part4.subheadline)}</p>
        <p class="content">{t(content.part4.content)}</p>
      </div>
    </div>

    <div class="card-row">
      {#each [['card1', 'card-bg-1'], ['card2', 'card-bg-2'], ['card3', 'card-bg-3']] as [key, bgClass]}
        <div class="card-item {bgClass}">
          <div class="card-headline-wrapper">
            <p class="card-headline">{t(content[key].headline)}</p>
          </div>
          <div class="card-sub-wrapper">
            <p class="card-sub">{t(content[key].sub)}</p>
          </div>
        </div>
      {/each}
    </div>

  </div>
{/if}