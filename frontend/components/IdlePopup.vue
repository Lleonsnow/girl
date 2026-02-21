<template>
  <Teleport to="body">
    <Transition name="idle-popup">
      <div v-if="visible" class="idle-popup" @click.self="close">
        <div class="idle-popup__card">
          <div class="idle-popup__photo-wrap">
            <img v-if="imageSrc" :src="imageSrc" alt="" class="idle-popup__photo" />
            <div v-else class="idle-popup__photo idle-popup__photo--placeholder" />
          </div>
          <div class="idle-popup__body">
            <h2 class="idle-popup__title">{{ t('idle.title') }}</h2>
            <p class="idle-popup__text">{{ t('idle.text') }}</p>
            <p class="idle-popup__sub">{{ t('idle.sub') }}</p>
            <button type="button" class="idle-popup__btn" @click="close">
              {{ t('idle.btn') }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
const { t } = useI18n()
const SESSION_KEY = 'idlePopupShown'

const props = withDefaults(
  defineProps<{ imageSrc?: string; idleMs?: number }>(),
  { idleMs: 30000 }
)

const visible = ref(false)
let idleTimer: ReturnType<typeof setTimeout> | null = null

function alreadyShownThisSession(): boolean {
  if (import.meta.server) return true
  return sessionStorage.getItem(SESSION_KEY) === '1'
}

function resetTimer() {
  if (idleTimer) clearTimeout(idleTimer)
  if (alreadyShownThisSession()) return
  idleTimer = setTimeout(() => {
    if (alreadyShownThisSession()) return
    if (import.meta.client) sessionStorage.setItem(SESSION_KEY, '1')
    visible.value = true
  }, props.idleMs)
}

function close() {
  visible.value = false
}

function onActivity() {
  if (!visible.value) resetTimer()
}

onMounted(() => {
  resetTimer()
  window.addEventListener('mousemove', onActivity)
  window.addEventListener('keydown', onActivity)
  window.addEventListener('scroll', onActivity)
  window.addEventListener('click', onActivity)
})

onUnmounted(() => {
  if (idleTimer) clearTimeout(idleTimer)
  window.removeEventListener('mousemove', onActivity)
  window.removeEventListener('keydown', onActivity)
  window.removeEventListener('scroll', onActivity)
  window.removeEventListener('click', onActivity)
})
</script>

<style lang="scss" scoped>
.idle-popup {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  background: rgba($color-bg-dark, 0.7);
  backdrop-filter: blur(4px);
}

.idle-popup__card {
  width: 560px;
  border-radius: 12px;
  overflow: hidden;
  background: $color-bg;
  box-shadow: 0 24px 48px rgba(0, 0, 0, 0.25);
}

.idle-popup__photo-wrap {
  width: 560px;
  height: 560px;
  background: $color-accent;
}

.idle-popup__photo {
  width: 100%;
  height: 100%;
  object-fit: cover;

  &--placeholder {
    background: linear-gradient(135deg, $color-pistachio 0%, $color-main 100%);
  }
}

.idle-popup__body {
  height: 300px;
  padding: 1.5rem 1.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.idle-popup__title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: $color-olive;
}

.idle-popup__text {
  margin: 0;
  font-size: 1rem;
  line-height: 1.4;
  color: $color-text;
}

.idle-popup__sub {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.35;
  color: $color-text-muted;
}

.idle-popup__btn {
  margin-top: auto;
  padding: 0.9rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  color: $color-white;
  background: linear-gradient(
    90deg,
    $color-main 0%,
    $color-pistachio 25%,
    $color-accent 50%,
    $color-pistachio 75%,
    $color-main 100%
  );
  background-size: 200% 100%;
  animation: idle-popup-gradient 4s linear infinite;
  transition: transform 0.2s, box-shadow 0.2s;

  &:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 16px rgba($color-olive, 0.3);
  }
}

@keyframes idle-popup-gradient {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.idle-popup-enter-active,
.idle-popup-leave-active {
  transition: opacity 0.25s ease;
  .idle-popup__card {
    transition: transform 0.25s ease;
  }
}
.idle-popup-enter-from,
.idle-popup-leave-to {
  opacity: 0;
  .idle-popup__card {
    transform: scale(0.95);
  }
}
</style>
