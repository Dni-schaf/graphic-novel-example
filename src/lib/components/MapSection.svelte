<script>
  import { onMount } from 'svelte';
  import { mapState } from '$lib/state/mapState.svelte.js';
  import SpeakerBubble from '$lib/components/SpeakerBubble.svelte';
  
  let { dateStart, dateEnd, onHeightChange, sectionId, speakerTexts } = $props();
  let entries = $derived(speakerTexts?.[sectionId] || []);

  function convertToDate(dateString) {
    const [day, month, year] = dateString.split('.');
    return new Date(`${year}-${month}-${day}`).getTime();
  }

  let windowHeight = $state(0);
  let scrollPosition = $state(0);
  let sectionElement;
  let sectionTop = $state(0);

  let startDate = $derived(convertToDate(dateStart));
  let endDate = $derived(convertToDate(dateEnd));
  let daysDiff = $derived((endDate - startDate) / (1000 * 60 * 60 * 24));
  let divHeight = $derived(daysDiff * 30 + windowHeight);

  let progress = $derived(
    Math.max(0, Math.min(1,
      (scrollPosition - (sectionTop - windowHeight)) / divHeight
    ))
  );

  $effect(() => {
  if (progress > 0 && progress < 1) {
    mapState.progress = progress;
    mapState.dateStart = dateStart;
    mapState.dateEnd = dateEnd;
  }
});

  onMount(() => {
    // sectionTop erst nach vollständigem Laden setzen
    function updateTop() {
      if (sectionElement) {
        sectionTop = sectionElement.getBoundingClientRect().top + window.scrollY;
      }
    }
    
    
    if (document.readyState === 'complete') {
      // Seite schon fertig geladen → direkt aufrufen
      updateTop();
    } else {
      // Seite noch nicht fertig → warten
      window.addEventListener('load', updateTop);
    }
    
    window.addEventListener('resize', updateTop);
    
    return () => {
      window.removeEventListener('load', updateTop);
      window.removeEventListener('resize', updateTop);
    };
  });


let lastReportedHeight = 0;

$effect(() => {
  if (onHeightChange && divHeight !== lastReportedHeight) {
    lastReportedHeight = divHeight;
    onHeightChange(divHeight);
  }
});
</script>

<svelte:window
  bind:innerHeight={windowHeight}
  bind:scrollY={scrollPosition}
/>


<div class="map-section" style="height: {divHeight}px;" bind:this={sectionElement}>
  {#each entries as entry}
    <SpeakerBubble textData={entry} />
  {/each}
</div>
