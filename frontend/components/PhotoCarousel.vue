<template>
  <section class="carousel-section">
    <div class="my-container">
      <div class="carousel-section__row">
        <div
          v-for="(slide, i) in slides"
          :key="i"
          class="carousel-section__item"
          :class="{ 'carousel-section__item--loaded': loadedIndices.has(i) }"
          :style="{ '--i': i }"
        >
          <template v-if="typeof slide === 'string'">
            <img
              :src="slide"
              alt=""
              class="carousel-section__img"
              @load="onImageLoad(i)"
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
const loadedIndices = ref<Set<number>>(new Set())

function onImageLoad(i: number) {
  loadedIndices.value = new Set([...loadedIndices.value, i])
}

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
  align-items: center;
}

@media (max-width: 900px) {
  .carousel-section__row {
    grid-template-columns: repeat(8, minmax(120px, 1fr));
    overflow-x: auto;
    padding-bottom: 0.25rem;
  }
}

.carousel-section__item {
  --i: 0;
  position: relative;
  min-width: 0;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 14px;
  padding: 4px;
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 255, 255, 0.5) 100%);
  box-shadow:
    0 2px 8px rgba(0, 0, 0, 0.04),
    0 8px 24px rgba(0, 0, 0, 0.06),
    inset 0 1px 0 rgba(255, 255, 255, 0.85);

  &::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 10px;
    background: linear-gradient(
      160deg,
      rgba(255, 255, 255, 0.97) 0%,
      rgba(255, 255, 255, 0.6) 40%,
      transparent 70%,
      rgba(255, 255, 255, 0.2) 100%
    );
    pointer-events: none;
    opacity: 1;
    transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    transition-delay: calc(var(--i) * 45ms + 100ms);
  }

  &--loaded::after {
    opacity: 0;
  }
}

.carousel-section__img {
  width: 100%;
  aspect-ratio: 170 / 250;
  object-fit: cover;
  border-radius: 10px;
  cursor: pointer;
  transform: scale(1.1);
  opacity: 0;
  transition:
    opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1),
    transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  transition-delay: calc(var(--i) * 45ms);

  .carousel-section__item--loaded & {
    opacity: 1;
    transform: scale(1.1);
  }

  &--placeholder {
    opacity: 1;
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
