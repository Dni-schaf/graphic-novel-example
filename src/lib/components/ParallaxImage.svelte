<script>
  let { chapterName, layer } = $props();

  let imagePath = $derived(`/images/${chapterName}/${layer.image}.webp`);

  let scrollY = $state(0);
  let elementRef;
  let offset = $state(0);

  $effect(() => {
    const y = scrollY;
    if (elementRef) {
      const rect = elementRef.getBoundingClientRect();
      const viewportCenter = window.innerHeight / 2;
      const distanceFromCenter = rect.top + rect.height / 2 - viewportCenter;
      offset = -distanceFromCenter * layer.speed;
    }
  });
</script>

<svelte:window bind:scrollY />

<img
  src={imagePath}
  alt=""
  loading="lazy"
  class="parallax-layer"
  style="top: {layer.top}; left: {layer.left}; width: {layer.width}; transform: translateY({offset}px);"
  bind:this={elementRef}
/>

<style>
  .parallax-layer {
    position: absolute;
    pointer-events: none;
  }
</style>