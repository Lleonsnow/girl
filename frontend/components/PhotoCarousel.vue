<template>
  <section class="carousel-section">
    <div class="my-container">
      <div class="carousel" ref="emblaRef">
        <div class="carousel__container">
          <div
            v-for="(slide, i) in slides"
            :key="i"
            class="carousel__slide"
          >
            <img v-if="typeof slide === 'string'" :src="slide" alt="" class="carousel__img" />
            <div v-else class="carousel__img carousel__img--placeholder" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import useEmblaCarousel from 'embla-carousel-vue'

const [emblaRef] = useEmblaCarousel({ loop: true, align: 'start' })

defineProps<{
  title?: string
  slides: (string | object)[]
}>()
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

.carousel {
  overflow: hidden;
  position: relative;
}

.carousel__container {
  display: flex;
  touch-action: pan-y;
  gap: 0.75rem;
}

.carousel__slide {
  flex: 0 0 170px;
  min-width: 0;

  &:first-child {
    margin-left: 0.75rem;
  }

  &:last-child {
    margin-right: 0.75rem;
  }
}

.carousel__img {
  width: 170px;
  height: 250px;
  object-fit: cover;
  border-radius: 12px;

  &--placeholder {
    width: 170px;
    height: 250px;
    background: linear-gradient(135deg, $color-accent 0%, $color-pistachio 100%);
  }
}
</style>
