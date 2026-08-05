<script>
  import { overlayState } from '$lib/state/overlayState.svelte.js';
</script>

{#if overlayState.visible}
  <div class="chapter-loading-overlay">
    <svg class="compass-rose" viewBox="0 0 100 100">
      <!-- Platzhalter - hier später eure echte Kompassrosen-Illustration einsetzen -->
      <circle cx="50" cy="50" r="40" fill="none" stroke="#333" stroke-width="1"/>
      <polygon points="50,15 56,50 50,85 44,50" fill="#333" class="compass-needle"/>
    </svg>
  </div>
{/if}

<style>
  .chapter-loading-overlay {
    position: fixed;
    inset: 0;
    background: white;
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .compass-needle {
    transform-origin: 50px 50px;
    animation: spin-settle 1.4s ease-in-out infinite;
  }
  @keyframes spin-settle {
    0%   { transform: rotate(0deg); }
    50%  { transform: rotate(370deg); }
    100% { transform: rotate(360deg); }
  }
</style>