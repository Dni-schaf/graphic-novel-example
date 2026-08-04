<script>
  import { languageState } from '$lib/state/language.svelte.js';

  let { textData } = $props();

  let scrollY = $state(0);
  let bubbleElement;
  let offset = $state(0);

  $effect(() => {
    const y = scrollY; // Abhängigkeit, damit der Effect bei jedem Scroll neu läuft
    if (bubbleElement) {
      const rect = bubbleElement.getBoundingClientRect();
      const viewportCenter = window.innerHeight / 2;
      const distanceFromCenter = rect.top + rect.height / 2 - viewportCenter;
      offset = -distanceFromCenter * (textData.parallaxSpeed ?? 0);
    }
  });

</script>

<svelte:window bind:scrollY />

<div
  class="text-container {textData.kind}"
  style="top: {textData.top}; left: {textData.left}; width: {textData.width}; text-align: {textData.textAlign}; transform: translateY({offset}px);"
  bind:this={bubbleElement}
>
  <p class={textData.color}>
    {textData[`text_${languageState.current}`] || textData.text_de}
  </p>
</div>