<script>
  import ImageWithTexts from '$lib/components/ImageWithTexts.svelte';
  let { chapterName, imageNames, imageTexts } = $props();
</script>

<div class="comic-section">
  {#each imageNames as imageName}
    <ImageWithTexts {imageName} {chapterName} {imageTexts} />
  {/each}
</div>