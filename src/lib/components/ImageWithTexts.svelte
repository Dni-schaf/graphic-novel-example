<script>
  import TextBubble from '$lib/components/TextBubble.svelte';
  import CurvedText from '$lib/components/CurvedText.svelte';
  import ParallaxImage from '$lib/components/ParallaxImage.svelte';
  import { bonusModules } from '$lib/data/bonusModules.js';
  import { allImageDimensions } from '$lib/data/imageDimensions.js';
  import { onMount } from 'svelte';

  let { imageName, chapterName, imageTexts, curvedTexts, parallaxLayers } = $props();

  let imagePath = $derived(`/images/${chapterName}/${imageName}.webp`);
  let textEntries = $derived(imageTexts[imageName]);
  let curvedEntries = $derived(curvedTexts?.[imageName]);
  let BonusComponent = $derived(bonusModules[imageName]);
  let dimensions = $derived(allImageDimensions[imageName]);
  let parallaxEntries = $derived(parallaxLayers?.[imageName]);
</script>

<div class="image-container">
  {#if BonusComponent}
    <BonusComponent {imageName} />
  {:else}
    <img
      src={imagePath}
      alt={imageName}
      loading="lazy"
      style={dimensions ? `aspect-ratio: ${dimensions.width} / ${dimensions.height};` : ''}
    />

    {#if parallaxEntries}
      {#each parallaxEntries as layer}
        <ParallaxImage {chapterName} {layer} />
      {/each}
    {/if}

    {#if textEntries}
      {#each textEntries as entry}
        <TextBubble textData={entry} />
      {/each}
    {/if}

    {#if curvedEntries}
      {#each curvedEntries as entry}
        <CurvedText {entry} />
      {/each}
    {/if}
  {/if}
</div>