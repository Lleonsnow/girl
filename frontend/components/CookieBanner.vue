<template>
  <div class="cookie-banner" role="dialog" aria-label="Cookie consent">
    <p class="cookie-banner__text">{{ t('cookie.text') }}</p>
    <div class="cookie-banner__actions">
      <button type="button" class="cookie-banner__btn cookie-banner__btn--secondary" @click="accept('essential')">
        {{ t('cookie.essentialOnly') }}
      </button>
      <button type="button" class="cookie-banner__btn cookie-banner__btn--primary" @click="accept('full')">
        {{ t('cookie.acceptAll') }}
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
const cookieStore = useCookieConsentStore()
const { accept } = cookieStore
</script>

<style lang="scss" scoped>
.cookie-banner {
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 70%;
  max-width: 1200px;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
  background: $color-bg;
  border: 1px solid $color-accent;
  border-bottom: none;
  border-radius: 12px 12px 0 0;
  box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.2);
  z-index: 99990;
}

.cookie-banner__text {
  margin: 0;
  flex: 1;
  min-width: 200px;
  @include headingBaseStyle(article);
  color: $color-text;
  line-height: 1.5;
}

.cookie-banner__actions {
  display: flex;
  gap: 0.75rem;
  flex-shrink: 0;
}

.cookie-banner__btn {
  padding: 0.5rem 1rem;
  font: inherit;
  font-size: 0.95rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: opacity 0.2s;

  &:hover {
    opacity: 0.9;
  }

  &--primary {
    border: none;
    background: $color-olive;
    color: $color-white;
  }

  &--secondary {
    border: 1px solid $color-accent;
    background: transparent;
    color: $color-text;
  }
}
</style>
