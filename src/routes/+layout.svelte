<script>
  import '../app.css';
  import { menuState } from '$lib/state/menu.svelte.js';

  let { children } = $props();
</script>

<button onclick={() => menuState.isOpen = !menuState.isOpen}>
  Menü
</button>

{#if menuState.isOpen}
  <div style="background: red; padding: 2rem; color: white;">
    Hier kommt später das Menü hin
  </div>
{/if}

{@render children()}