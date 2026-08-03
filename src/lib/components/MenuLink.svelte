<script>
  import { languageState } from '$lib/state/language.svelte.js';
  import { menuState } from '$lib/state/menu.svelte.js';
  let { textData } = $props();
  let imagePath = $derived(`/images/ui/${textData.route}-preview.jpg`);
</script>


<div class="menu_link">
    <a href="/{languageState.current}/{textData.route}" onclick={() => menuState.isOpen = false}>        
        <img src={imagePath} alt={textData[`chapter_${languageState.current}`] || textData.chapter_de} />
        <div class="link_text_container" >
            <p class="menu_chapter">
                {textData[`chapter_${languageState.current}`] || textData.chapter_de} 
            </p>
            <p class="menu_title">
                {textData[`title_${languageState.current}`] || textData.title_de}
            </p>
        </div>
    </a>
</div>