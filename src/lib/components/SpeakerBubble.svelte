<script>
  import { languageState } from '$lib/state/language.svelte.js';

  let { textData } = $props();
</script>

<div
  class="text-container {textData.kind}"
  style="top: {textData.top}; left: {textData.left}; width: {textData.width}; text-align: {textData.textAlign};"
>
  <p class={textData.color}>
      {textData[`text_${languageState.current}`] || textData.text_de}
  </p>
</div>