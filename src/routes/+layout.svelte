<script>
  import '../app.css';
  import { menuState } from '$lib/state/menu.svelte.js';
  import { languageState } from '$lib/state/language.svelte.js';
  import { uiTexts } from '$lib/data/uiTexts.js';
  import MenuContent from '$lib/components/MenuContent.svelte';

  let { children } = $props();
</script>

<button 
  onclick={() => menuState.isOpen = !menuState.isOpen} 
  id="menu_button" 
  aria-label={uiTexts.openMenu[languageState.current]}
>
  ☰
</button>

{#if menuState.isOpen}
  <MenuContent />
{/if}

{@render children()}