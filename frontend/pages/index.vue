<template>
  <div class="home">
    <ClientOnly>
      <IdlePopup :image-src="heroImage" />
      <template #fallback><span /></template>
    </ClientOnly>
    <HomeHero :src="heroImage" :brand-name="siteConfig.authorPseudonym" :url-overrides="siteConfig.socialOverrides" />
    <CtaBlock
      :text="t('home.ctaText')"
      :button-label="t('home.ctaButton')"
      thumb-src="/main/miniature.jpg"
      :open-popup="true"
      @cta-click="showDiscountPopup = true"
    />
    <DiscountPopup
      v-model:visible="showDiscountPopup"
      :image-src="heroImage"
      :boosty-url="siteConfig.boostyUrl"
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
const siteConfig = useSiteConfigStore()

const showDiscountPopup = ref(false)

const socialGridItems = computed(() =>
  getSocialLinks(siteConfig.socialOverrides).map((s, i) => ({
    id: String(i + 1),
    name: s.name,
    url: s.url,
  }))
)

const heroImage = '/main/main.jpg'
const allCarousel = Array.from({ length: 11 }, (_, i) => `/carousel/${i + 1}.jpg`)
const carouselSlides = ref<string[]>([])
onMounted(() => {
  carouselSlides.value = [...allCarousel].sort(() => Math.random() - 0.5).slice(0, 8)
})

const faqItems = computed(() => {
  const a = siteConfig.authorPseudonym
  return [
    { id: '1', question: t('home.faq1q', { author: a }), answer: t('home.faq1a') },
    { id: '2', question: t('home.faq2q', { author: a }), answer: t('home.faq2a') },
    { id: '3', question: t('home.faq3q'), answer: t('home.faq3a') },
    { id: '4', question: t('home.faq4q', { author: a }), answer: t('home.faq4a') },
    { id: '5', question: t('home.faq5q', { author: a }), answer: t('home.faq5a') },
  ]
})
</script>

<style lang="scss" scoped>
.home {
  background: $color-bg;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style>
