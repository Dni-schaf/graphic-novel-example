<script>
  import ImageWithTexts from '$lib/components/ImageWithTexts.svelte';
  let { chapterName, imageNames, imageTexts, curvedTexts, onHeightChange, id = undefined } = $props();

  let sectionElement;

  import { onMount } from 'svelte';

let lastHeight = 0;

onMount(() => {
  const observer = new ResizeObserver(entries => {
    const height = entries[0].contentRect.height;
    if (height !== lastHeight) {
      lastHeight = height;
      if (onHeightChange) onHeightChange(height);
    }
  });
  observer.observe(sectionElement);
  return () => observer.disconnect();
});
  
</script>

<div class="comic-section" {id} bind:this={sectionElement}>
  {#each imageNames as imageName}
    <ImageWithTexts {imageName} {chapterName} {imageTexts} {curvedTexts} />
  {/each}
</div>