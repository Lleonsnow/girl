<template>
  <div class="photos-page">
    <div class="my-container page">
      <h1 class="page__title">{{ t('pages.photosTitle') }}</h1>
      <div class="page__gallery">
        <img
          v-for="(src, i) in photoSlides"
          :key="i"
          :src="src"
          alt=""
          class="page__img"
          @click="lightboxSrc = src"
        />
      </div>
    </div>
    <div class="cta-sticky">
      <div class="cta-sticky__inner">
        <CtaBlock
      :text="t('home.ctaText')"
      :button-label="t('home.ctaButton')"
      thumb-src="/main/miniature.jpg"
      :open-popup="true"
      @cta-click="showDiscountPopup = true"
        />
      </div>
    </div>
    <DiscountPopup
      v-model:visible="showDiscountPopup"
      :image-src="heroImage"
      :boosty-url="siteConfig.boostyUrl"
    />
  </div>
  <Teleport to="body">
    <Transition name="lightbox">
      <div
        v-if="lightboxSrc"
        class="lightbox"
        @click.self="lightboxSrc = null"
      >
        <img :src="lightboxSrc" alt="" class="lightbox__img" />
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
const { t } = useI18n()
const photoSlides = Array.from({ length: 11 }, (_, i) => `/photos/${i + 1}.jpg`)
const lightboxSrc = ref<string | null>(null)
const siteConfig = useSiteConfigStore()
const showDiscountPopup = ref(false)
const heroImage = '/main/main.jpg'

function onKeydown(e: KeyboardEvent) {
  if (e.key === 'Escape') lightboxSrc.value = null
}
onMounted(() => window.addEventListener('keydown', onKeydown))
onUnmounted(() => window.removeEventListener('keydown', onKeydown))
</script>

<style lang="scss" scoped>
.photos-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.cta-sticky {
  position: fixed;
  bottom: 72px;
  left: 56px;
  right: 0;
  z-index: 10;
  display: flex;
  justify-content: center;
}

.cta-sticky__inner {
  width: 100%;
  max-width: $width-desktop-max;
  border-radius: 8px;
  overflow: hidden;
}

.photos-page {
  padding-bottom: 150px;
}

.page {
  padding: 4rem 0;
  flex: 1;
}

.page__title {
  @include headingBaseStyle(h1);
  color: $color-olive;
  margin: 0 0 1rem;
}

.page__gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-top: 1.5rem;
}

.page__img {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 8px;
  cursor: pointer;
}

.lightbox {
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

.lightbox__img {
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
