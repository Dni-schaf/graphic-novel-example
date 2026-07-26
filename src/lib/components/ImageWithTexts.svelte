<script>
  import TextBubble from '$lib/components/TextBubble.svelte';

  let { imageName, chapterName, imageTexts } = $props();

  let imagePath = $derived(`/images/${chapterName}/${imageName}.webp`);
  let textEntries = $derived(imageTexts[imageName]);
</script>

<div class="image-container">
  <img src={imagePath} alt={imageName} />

  {#if textEntries}
    {#each textEntries as entry}
      <TextBubble textData={entry} />
    {/each}
  {/if}
</div>