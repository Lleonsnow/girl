<template>
  <div class="about-page">
    <div class="my-container page">
      <h1 class="page__title">{{ t('pages.aboutTitle') }}</h1>
      <section class="about-hero">
        <div class="about-hero__text">
          <p class="page__text">{{ t('about.bioIntro') || t('pages.devText') }}</p>
        </div>
        <div class="about-hero__photo-col">
          <img src="/main/main.jpg" alt="" class="about-hero__img" width="480" height="480" />
          <p class="about-hero__credo">{{ t('about.credo') }}</p>
        </div>
      </section>
      <section class="about-rest">
        <p class="page__text">{{ t('about.bioRest') }}</p>
      </section>
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
</template>

<script setup lang="ts">
const { t } = useI18n()
const siteConfig = useSiteConfigStore()
const showDiscountPopup = ref(false)
const heroImage = '/main/main.jpg'
</script>

<style lang="scss" scoped>
.about-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  padding-bottom: 150px;
}

.page {
  padding: 4rem 0;
  flex: 1;
}

.page__title {
  @include headingBaseStyle(h1);
  color: $color-olive;
  margin: 0 0 1.5rem;
}

.about-hero {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  margin-bottom: 2rem;
}

.about-hero__text {
  flex: 1;
  min-width: 0;
}

.about-hero__photo-col {
  flex-shrink: 0;
  width: 480px;
}

.about-hero__img {
  width: 480px;
  height: 480px;
  object-fit: cover;
  border-radius: 8px;
  display: block;
}

.about-hero__credo {
  margin: 0.5rem 0 0;
  font-size: 0.875rem;
  line-height: 1.4;
  color: $color-text;
  opacity: 0.9;
}

.about-rest {
  margin-top: 0;
}

.page__text {
  @include headingBaseStyle(article);
  color: $color-text;
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

@media (max-width: 1020px) {
  .about-hero {
    flex-direction: column;
  }
  .about-hero__photo-col {
    width: 100%;
    max-width: 480px;
  }
  .about-hero__img {
    width: 100%;
    max-width: 480px;
    height: auto;
    aspect-ratio: 1;
  }
}
</style>
