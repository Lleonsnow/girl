<template>
  <Transition name="loading-banner" @after-leave="emit('gone')">
    <div
      v-if="visible"
      class="loading-banner"
      style="position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:#2d3328"
    >
      <div class="loading-banner__inner">
        <h1 class="loading-banner__title">My Anesthesia</h1>
        <div class="loading-banner__line">
          <span class="loading-banner__line-fill" />
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{ loading?: boolean }>(),
  { loading: true }
)

const emit = defineEmits<{ gone: [] }>()

const visible = ref(true)
watch(() => props.loading, (v) => {
  if (!v) visible.value = false
})
</script>

<style lang="scss" scoped>
.loading-banner {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg, $color-bg-dark 0%, $color-olive 50%, $color-bg-dark 100%);
  background-size: 200% 200%;
  animation: loading-banner-bg 3s ease-in-out infinite;
}

.loading-banner__inner {
  text-align: center;
}

.loading-banner__title {
  margin: 0 0 1.5rem;
  font-size: clamp(2rem, 8vw, 3.5rem);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  background: linear-gradient(135deg, $color-accent 0%, $color-pistachio 50%, $color-bg 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  -webkit-text-fill-color: transparent;
  animation: loading-banner-shine 2s ease-in-out infinite;
}

.loading-banner__line {
  width: 120px;
  height: 3px;
  margin: 0 auto;
  background: rgba($color-accent, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.loading-banner__line-fill {
  display: block;
  height: 100%;
  width: 40%;
  background: linear-gradient(90deg, $color-pistachio, $color-accent);
  border-radius: 3px;
  animation: loading-banner-line 1.2s ease-in-out infinite;
}

@keyframes loading-banner-bg {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

@keyframes loading-banner-shine {
  0%, 100% { background-position: 0% center; }
  50% { background-position: 100% center; }
}

@keyframes loading-banner-line {
  0% { transform: translateX(-100%); }
  50% { transform: translateX(250%); }
  100% { transform: translateX(-100%); }
}

.loading-banner-enter-active,
.loading-banner-leave-active {
  transition: opacity 0.6s ease;
}
.loading-banner-leave-to {
  opacity: 0;
}
</style>
