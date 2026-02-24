<template>
  <section class="carousel-section">
    <div class="my-container">
      <div class="carousel-section__row">
        <div
          v-for="(slide, i) in slides"
          :key="i"
          class="carousel-section__item"
        >
          <template v-if="typeof slide === 'string'">
            <img
              :src="slide"
              alt=""
              class="carousel-section__img"
              @click="lightboxSrc = slide"
            />
          </template>
          <div v-else class="carousel-section__img carousel-section__img--placeholder" />
        </div>
      </div>
    </div>
    <Teleport to="body">
      <Transition name="lightbox">
        <div
          v-if="lightboxSrc"
          class="carousel-section__lightbox"
          @click.self="lightboxSrc = null"
        >
          <img :src="lightboxSrc" alt="" class="carousel-section__lightbox-img" />
        </div>
      </Transition>
    </Teleport>
  </section>
</template>

<script setup lang="ts">
defineProps<{
  title?: string
  slides: (string | object)[]
}>()

const lightboxSrc = ref<string | null>(null)

function onKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape') lightboxSrc.value = null
}
onMounted(() => window.addEventListener('keydown', onKeydown))
onUnmounted(() => window.removeEventListener('keydown', onKeydown))
</script>

<style lang="scss" scoped>
.carousel-section {
  padding: 3rem 0;
}

.carousel-section__title {
  @include headingBaseStyle(h2);
  color: $color-olive;
  margin: 0 0 1.5rem;
}

.carousel-section__row {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 0.75rem;
}

@media (max-width: 900px) {
  .carousel-section__row {
    grid-template-columns: repeat(8, minmax(120px, 1fr));
    overflow-x: auto;
    padding-bottom: 0.25rem;
  }
}

.carousel-section__item {
  min-width: 0;
}

.carousel-section__img {
  width: 100%;
  aspect-ratio: 170 / 250;
  object-fit: cover;
  border-radius: 12px;
  cursor: pointer;

  &--placeholder {
    background: linear-gradient(135deg, $color-accent 0%, $color-pistachio 100%);
  }
}

.carousel-section__lightbox {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: rgba(0, 0, 0, 0.85);
  cursor: pointer;
}

.carousel-section__lightbox-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  pointer-events: none;
}

.lightbox-enter-active,
.lightbox-leave-active {
  transition: opacity 0.2s ease;
}
.lightbox-enter-from,
.lightbox-leave-to {
  opacity: 0;
}
</style>
