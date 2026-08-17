<script>
  import MenuContent from '$lib/components/MenuContent.svelte';
  import { languageState } from '$lib/state/language.svelte.js';
  import { switchLanguage } from '$lib/utils/language.js';
  import { indexTexts } from '$lib/data/indexTexts.js';
  import { getChapterStartUrl } from '$lib/utils/chapterNav.js';
  import '../../lib/styles/indexstyle.css';
</script>

<div id="nav">
    <div id="language"> 
        <button onclick={() => switchLanguage('de')} class="language_button">DE</button>
        <button onclick={() => switchLanguage('en')} class="language_button">EN</button>
        <button onclick={() => switchLanguage('no')} class="language_button">NO</button>    
    </div>
</div>

<header>
  <img id="logo" src="/images/ui/dna-logo-white.svg" alt="DNA Logo" width="25%">
  <p id="present">{indexTexts.present[languageState.current]}</p>
  <img id="title_index" src={`/images/ui/title_${languageState.current}.svg`} alt="Title" width="100%">
  <!--<h1 id="title">Ein Palast aus Eis </br><span id="subline">am Ende der Welt</span></h1>-->
  <div id="clouds"></div>
        
        
</header>

<div id="iceshelf"></div>

<div id="content">
    <section>
        <h3 id="headline">{indexTexts.headline[languageState.current]}</h3>
        <p class="content_p" id="p1">{indexTexts.p1[languageState.current]}</p>
        <p class="content_p" id="p2">{indexTexts.p2[languageState.current]}</p>
        <p class="content_p" id="p3">{indexTexts.p3[languageState.current]}</p>
        <p class="content_p" id="call_to_action">{indexTexts.call_to_action[languageState.current]}</p>
        <div class="button-wrapper">
          <a href={getChapterStartUrl(languageState.current, 1)}>
            <button id="button_start">
                <span id="button_txt">{indexTexts.button_txt[languageState.current]}</span>
            </button>
          </a>
        </div>
    </section>
    
    <div id="gab"></div>
    
    <!-- <section>
            <h3 id="headline">Danksagung</h3>
            <p class="content_p" id="p4">Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>
    </section>

    <div id="gab"></div>-->
    
    <section id="footer">
        <img src="/images/ui/dna-logo-blue.svg" alt="DNA Logo" width="35%"> 
        <p id="impressum">
          {indexTexts.impressum[languageState.current]}
        </p>
    </section>
</div>
