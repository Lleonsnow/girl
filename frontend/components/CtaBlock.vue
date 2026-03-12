<template>
  <section class="cta-block">
    <div class="my-container cta-block__inner">
      <div class="cta-block__thumb-wrap">
        <img v-if="thumbSrc" :src="thumbSrc" alt="" class="cta-block__thumb" />
        <div v-else class="cta-block__thumb cta-block__thumb--placeholder" />
      </div>
      <div class="cta-block__content">
        <p class="cta-block__text">{{ text }}</p>
        <button v-if="openPopup" type="button" class="cta-block__btn" @click="$emit('cta-click')">{{ buttonLabel }}</button>
        <NuxtLink v-else-if="chatLink" :to="chatLink" class="cta-block__btn">{{ buttonLabel }}</NuxtLink>
        <a v-else-if="chatHref" :href="chatHref" target="_blank" rel="noopener noreferrer" class="cta-block__btn">{{ buttonLabel }}</a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    text: string
    buttonLabel?: string
    thumbSrc?: string
    chatLink?: string
    chatHref?: string
    openPopup?: boolean
  }>(),
  { buttonLabel: 'Начать чат', openPopup: false }
)
defineEmits<{ (e: 'cta-click'): void }>()
</script>

<style lang="scss" scoped>
@use "sass:color";
.cta-block {
  padding: 1.5rem 0;
  background: color.mix($color-pistachio, $color-bg, 18%);
  border-radius: 8px;
}

.cta-block__inner {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: nowrap;
  justify-content: space-around;
  padding: 0 100px;
}

.cta-block__thumb-wrap {
  flex-shrink: 0;
  width: 85px;
  height: 85px;
  border-radius: 8px;
  overflow: hidden;
  aspect-ratio: 1;
  background: $color-accent;
}

.cta-block__thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;

  &--placeholder {
    background: linear-gradient(135deg, $color-main 0%, $color-olive 100%);
  }
}

.cta-block__content {
  flex: 1;
  min-width: 0;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: nowrap;
  justify-content: space-around;
}

.cta-block__text {
  @include headingBaseStyle(article);
  color: $color-text;
  margin: 0;
  font-size: 1.25rem;
  line-height: 1.35;
}

.cta-block__btn {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 500px;
  height: 70px;
  padding: 0 1.25rem;
  border: none;
  border-radius: 8px;
  background: $color-olive;
  color: $color-white;
  @include headingBaseStyle(text-small);
  font-size: 1.125rem;
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s;
  cursor: pointer;
  font-family: inherit;

  &:hover {
    background: $color-main-dark;
  }

  &:focus {
    outline: none;
  }
}
</style>
