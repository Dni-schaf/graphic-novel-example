<script>
  import { switchLanguage } from '$lib/utils/language.js';
  import { languageState } from '$lib/state/language.svelte.js';
  import { uiTexts } from '$lib/data/uiTexts.js';
  import { legalTexts } from '$lib/data/legalTexts.js';
  import { menuState } from '$lib/state/menu.svelte.js';
  import MenuLink from '$lib/components/MenuLink.svelte';
  import { chapterTitles } from '$lib/data/chapterTitles.js';
  import { page } from '$app/state';
  import { goto } from '$app/navigation';

  function handleLanguageSwitch(lang) {
  console.log('vorher:', menuState.isOpen);
  switchLanguage(lang);
  menuState.isOpen = false;
  console.log('nachher:', menuState.isOpen);
  }
</script>


<div id="menu_overlay_bg">
  <div id="menu_overlay">
    <section id="settings">
      <button onclick={() => menuState.isOpen = false} 
      id="close_button" 
      aria-label={uiTexts.closeMenu[languageState.current]}
      >
        x
      </button>
      <div id="language_buttons_container">
        <button onclick={() => handleLanguageSwitch('de')} class="language_button">DE</button>
        <button onclick={() => handleLanguageSwitch('en')} class="language_button">EN</button>
        <button onclick={() => handleLanguageSwitch('no')} class="language_button">NO</button>
      </div>
    </section>

    <div class="table_of_content">
      <div id="menu_chapter">
        {#each chapterTitles as entry}
          <MenuLink textData={entry} />
        {/each}
      </div>
    </div> 
    <div id="footnode">
      <h3 class="menu_footnote_title">{legalTexts.sourcesTitle[languageState.current]} </h3>
      <p class="menu_footnote">{legalTexts.sourceContent[languageState.current]} </p>

      <h3 class="menu_footnote_title">{legalTexts.LegalnoticeTitle[languageState.current]} </h3>
      <p class="menu_footnote">{legalTexts.LegalnoticeContent[languageState.current]} </p>

      <h3 class="menu_footnote_title">{legalTexts.PolicyTitle[languageState.current]} </h3>
      <p class="menu_footnote">{legalTexts.PolicyContent1[languageState.current]} </p>
      <p class="menu_footnote">{legalTexts.PolicyContent2[languageState.current]} </p>
      <p class="menu_footnote">{legalTexts.PolicyContent3[languageState.current]} </p>
      <p class="menu_footnote">{legalTexts.PolicyContent4[languageState.current]} </p>
      <p class="menu_footnote">{legalTexts.PolicyContent5[languageState.current]} </p>
    </div>




  </div>
</div>
  