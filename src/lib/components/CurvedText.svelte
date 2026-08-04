<script>
  import { languageState } from '$lib/state/language.svelte.js';

  let { entry } = $props();
</script>

<svg class="curved-text-overlay" viewBox={entry.viewBox} preserveAspectRatio="none">
  <path id={entry.id} d={entry.pathD} fill="none" stroke="none" />
  <text fill={entry.color} font-size={entry.fontSize}>
    <textPath href="#{entry.id}" startOffset={entry.startOffset || '0%'}>
      {entry[`text_${languageState.current}`] || entry.text_de}
    </textPath>
  </text>
</svg>

<style>
  .curved-text-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
  }
</style>