<script>
  import MenuContent from '$lib/components/MenuContent.svelte';
  import { languageState } from '$lib/state/language.svelte.js';

  import MapSection from '$lib/components/MapSection.svelte';
  import PureMap from '$lib/components/pureMap.svelte'; // Großbuchstabe für Komponenten-Konvention
</script>

<PureMap scale={150} rotate={[-70, 0]} chapterName="Kapitel1" />

<div style="width: 100%; height: 500vh">

</div>