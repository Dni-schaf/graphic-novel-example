<script>
  import { languageState } from '$lib/state/language.svelte.js';
  let { textData } = $props();
  let imagePath = $derived(`/images/ui/${textData[`route`]}-preview.jpg`);
</script>


<div class="menu_link">
    <a href="/{textData[`route`]}">
        <img src={imagePath} alt="Previewimage" />
        <p class="menu_chapter">
            {textData[`chapter_${languageState.current}`] || textData.chapter_de} 
        </p>
        <p class="menu_title">
            {textData[`title_${languageState.current}`] || textData.title_de}
        </p>
    </a>
</div>