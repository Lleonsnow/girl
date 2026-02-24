<template>
  <Teleport to="body">
    <Transition name="idle-popup">
      <div v-if="visible" class="discount-popup" @click.self="close">
        <div class="discount-popup__card">
          <div class="discount-popup__photo-wrap">
            <img v-if="imageSrc" :src="imageSrc" alt="" class="discount-popup__photo" />
            <div v-else class="discount-popup__photo discount-popup__photo--placeholder" />
          </div>
          <div class="discount-popup__body">
            <h2 class="discount-popup__title">{{ t('idle.title', { author: siteConfig.authorPseudonym }) }}</h2>
            <p class="discount-popup__text">{{ t('idle.text') }}</p>
            <p class="discount-popup__sub">{{ t('idle.sub') }}</p>
            <a
              :href="effectiveBoostyUrl"
              target="_blank"
              rel="noopener noreferrer"
              class="discount-popup__btn"
              @click="close"
            >
              {{ t('idle.btn') }}
            </a>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script setup lang="ts">
const { t } = useI18n()
const props = withDefaults(
  defineProps<{
    visible: boolean
    imageSrc?: string
    boostyUrl?: string
  }>(),
  { boostyUrl: '' }
)
const siteConfig = useSiteConfigStore()
const effectiveBoostyUrl = computed(() => props.boostyUrl || siteConfig.boostyUrl)

const emit = defineEmits<{ (e: 'update:visible', v: boolean): void }>()

function close() {
  emit('update:visible', false)
}
</script>

<style lang="scss" scoped>
.discount-popup {
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

.discount-popup__card {
  width: 560px;
  border-radius: 12px;
  overflow: hidden;
  background: $color-bg;
  box-shadow: 0 24px 48px rgba(0, 0, 0, 0.25);
}

.discount-popup__photo-wrap {
  width: 560px;
  height: 560px;
  background: $color-accent;
}

.discount-popup__photo {
  width: 100%;
  height: 100%;
  object-fit: cover;

  &--placeholder {
    background: linear-gradient(135deg, $color-pistachio 0%, $color-main 100%);
  }
}

.discount-popup__body {
  height: 300px;
  padding: 1.5rem 1.5rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.discount-popup__title {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: $color-olive;
}

.discount-popup__text {
  margin: 0;
  font-size: 1rem;
  line-height: 1.4;
  color: $color-text;
}

.discount-popup__sub {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.35;
  color: $color-text-muted;
}

.discount-popup__btn {
  margin-top: auto;
  padding: 0.9rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  color: $color-white;
  text-decoration: none;
  text-align: center;
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
  .discount-popup__card {
    transition: transform 0.25s ease;
  }
}
.idle-popup-enter-from,
.idle-popup-leave-to {
  opacity: 0;
  .discount-popup__card {
    transform: scale(0.95);
  }
}
</style>
