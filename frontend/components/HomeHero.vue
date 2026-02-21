<template>
  <section class="hero">
    <div class="hero__photo-wrap">
      <img v-if="src" :src="src" alt="" class="hero__photo" />
      <div v-else class="hero__photo hero__photo--placeholder" />
      <h1 class="hero__title" :class="{ 'hero__title--visible': showTitle }">{{ brandName }}</h1>
    </div>
    <div class="hero__socials">
      <SocialIcons :url-overrides="urlOverrides" />
    </div>
  </section>
</template>

<script setup lang="ts">
import type { SocialId } from '~/utils/socials'

withDefaults(
  defineProps<{
    src?: string
    brandName?: string
    urlOverrides?: Partial<Record<SocialId, string>>
  }>(),
  { brandName: 'My Anesthesia' }
)

const showTitle = ref(false)
let titleTimer: ReturnType<typeof setTimeout>

function scheduleTitleShow() {
  titleTimer = setTimeout(() => { showTitle.value = true }, 2000)
}

onMounted(() => {
  if (document.readyState === 'complete') scheduleTitleShow()
  else window.addEventListener('load', scheduleTitleShow)
})
onUnmounted(() => {
  clearTimeout(titleTimer)
  window.removeEventListener('load', scheduleTitleShow)
})
</script>

<style lang="scss" scoped>
.hero {
  padding: 0;
  text-align: center;
}

.hero__photo-wrap {
  position: relative;
  width: 100%;
  height: 600px;
  margin: 0 0 1.5rem;
  overflow: hidden;
  background: $color-accent;
}

.hero__title {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  margin: 0;
  padding: 1rem 1rem 1.5rem;
  font-size: clamp(2.5rem, 10vw, 5rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  background: linear-gradient(135deg, $color-bg 0%, $color-accent 35%, $color-pistachio 65%, $color-main 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  opacity: 0;
  transition: opacity 0.8s ease;

  &--visible {
    opacity: 1;
  }
}

.hero__photo {
  width: 100%;
  height: 100%;
  object-fit: cover;

  &--placeholder {
    background: linear-gradient(135deg, $color-pistachio 0%, $color-main 100%);
  }
}

.hero__socials {
  padding: 0 1rem 2rem;
}
</style>
