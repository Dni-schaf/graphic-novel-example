<script>
  import MenuLink from '$lib/components/MenuLink.svelte';
  import { chapterTitles } from '$lib/data/chapterTitles.js';
</script>

<div class="table_of_Content">
    {#each chapterTitles as entry}
      <MenuLink textData={entry} />
    {/each}
</div> 