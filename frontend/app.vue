<template>
  <div>
    <div
      id="nuxt-loading-cover"
      class="loading-cover"
      style="position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;background:#2d3328"
      aria-hidden="true"
    >
      <div class="loading-cover__inner">
        <h1 class="loading-cover__title">{{ footerSiteName }}</h1>
        <div class="loading-cover__line"><span class="loading-cover__line-fill" /></div>
      </div>
    </div>
    <ClientOnly>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
      <TheFooter v-if="cookieStore.accepted" :site-name="footerSiteName" :links="footerLinks" />
      <template v-if="!cookieStore.accepted">
        <div class="cookie-overlay" aria-hidden="true" />
        <CookieBanner />
      </template>
      <template #fallback>
        <div class="cookie-gate" />
        <CookieBanner />
      </template>
    </ClientOnly>
  </div>
</template>

<script setup lang="ts">
const router = useRouter()
const { t } = useI18n()
const localePath = useLocalePath()
const cookieStore = useCookieConsentStore()
const siteConfig = useSiteConfigStore()
const footerSiteName = computed(() => siteConfig.authorPseudonym || t('siteName', { author: siteConfig.authorPseudonym }))
const footerLinks = computed(() => [
  { to: localePath('/privacy'), label: t('home.footerPrivacy') },
  { to: localePath('/terms'), label: t('home.footerAgreement') },
])
const MIN_VISIBLE_MS = 1800
const FADE_DURATION_MS = 700

function removeLoadingCover() {
  const el = document.getElementById('nuxt-loading-cover')
  if (!el) return
  el.classList.add('fade-out')
  setTimeout(() => el.remove(), FADE_DURATION_MS)
}

onMounted(() => {
  useCookieConsentStore().syncFromStorage()
  useSiteConfigStore().fetchConfig()
  const started = Date.now()
  Promise.all([
    router.isReady(),
    new Promise((r) => setTimeout(r, MIN_VISIBLE_MS)),
  ]).then(() => {
    const elapsed = Date.now() - started
    const remaining = Math.max(0, MIN_VISIBLE_MS - elapsed)
    setTimeout(removeLoadingCover, remaining)
  })
})
</script>

<style lang="scss" scoped>
.app-fallback {
  min-height: 100vh;
  width: 100%;
  display: flex;
}

.app-fallback__sidebar {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 56px;
  background: $color-bg-dark;
  flex-shrink: 0;
}

.app-fallback__main {
  flex: 1;
  min-width: 0;
  margin-left: 56px;
  min-height: 100vh;
}

.cookie-gate {
  position: fixed;
  inset: 0;
  background: $color-bg-dark;
  z-index: 99989;
}

.cookie-overlay {
  position: fixed;
  inset: 0;
  background: rgba($color-bg-dark, 0.4);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  z-index: 99989;
  pointer-events: auto;
}
</style>

<style lang="scss">
.loading-cover {
  background: linear-gradient(160deg, #2d3328 0%, #4a5d3e 50%, #2d3328 100%) !important;
  background-size: 200% 200%;
  animation: loading-cover-bg 3s ease-in-out infinite;
  transition: opacity 0.7s ease;
}
.loading-cover.fade-out { opacity: 0; pointer-events: none; }
.loading-cover__inner { text-align: center; }
.loading-cover__title {
  margin: 0 0 1.5rem;
  font-size: clamp(2rem, 8vw, 3.5rem);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: linear-gradient(135deg, #b5c4a8 0%, #9db892 50%, #f5f7f2 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  animation: loading-cover-shine 2s ease-in-out infinite;
}
.loading-cover__line {
  width: 120px;
  height: 3px;
  margin: 0 auto;
  background: rgba(181, 196, 168, 0.2);
  border-radius: 3px;
  overflow: hidden;
}
.loading-cover__line-fill {
  display: block;
  height: 100%;
  width: 40%;
  background: linear-gradient(90deg, #9db892, #b5c4a8);
  border-radius: 3px;
  animation: loading-cover-line 1.2s ease-in-out infinite;
}
@keyframes loading-cover-bg {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
@keyframes loading-cover-shine {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}
@keyframes loading-cover-line {
  0% { transform: translateX(-100%); }
  50% { transform: translateX(250%); }
  100% { transform: translateX(-100%); }
}
</style>
