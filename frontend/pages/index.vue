<template>
  <div class="home">
    <ClientOnly>
      <IdlePopup :image-src="heroImage" />
      <template #fallback><span /></template>
    </ClientOnly>
    <HomeHero :src="heroImage" :url-overrides="socialUrlOverrides" />
    <CtaBlock
      :text="t('home.ctaText')"
      :button-label="t('home.ctaButton')"
      thumb-src="/main/miniature.jpg"
      :chat-link="localePath('/contacts')"
    />
    <SocialGrid :items="socialGridItems" />
    <PhotoCarousel :title="t('home.photosTitle')" :slides="carouselSlides" />
    <FaqBlock :title="t('home.faqTitle')" :items="faqItems" />
  </div>
</template>

<script setup lang="ts">
import { getSocialLinks } from '~/utils/socials'

const { t } = useI18n()
const localePath = useLocalePath()

const socialUrlOverrides = {
  telegram: '#',
  instagram: '#',
  tiktok: '#',
  twitch: '#',
  youtube: '#',
  discord: '#',
  boosty: '#',
}

const socialGridItems = computed(() =>
  getSocialLinks(socialUrlOverrides).map((s, i) => ({
    id: String(i + 1),
    name: s.name,
    url: s.url,
  }))
)

const heroImage = '/main/main.jpg'
const carouselSlides = Array.from({ length: 11 }, (_, i) => `/carousel/${i + 1}.jpg`)

const faqItems = computed(() => [
  { id: '1', question: t('home.faq1q'), answer: t('home.faq1a') },
  { id: '2', question: t('home.faq2q'), answer: t('home.faq2a') },
  { id: '3', question: t('home.faq3q'), answer: t('home.faq3a') },
])
</script>

<style lang="scss" scoped>
.home {
  background: $color-bg;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
