<script>
  import { languageState } from '$lib/state/language.svelte.js';

  let { textData } = $props();
</script>

<div
  class="text-container {textData.kind}"
  style="bottom: {textData.bottom}; left: {textData.left}; width: {textData.width}; text-align: {textData.textAlign};"
>
  <p class={textData.color} style="font-size: {textData.fontSize};">
    <span class="highlight {textData.backgroundColor}">
      {textData[`text_${languageState.current}`] || textData.text_de}
    </span>
  </p>
</div>