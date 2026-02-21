<template>
  <div class="lang-switcher">
    <NuxtLink
      :to="switchLocalePath('ru')"
      class="lang-switcher__btn"
      :class="{ 'lang-switcher__btn--active': locale === 'ru' }"
    >
      RU
    </NuxtLink>
    <NuxtLink
      :to="switchLocalePath('en')"
      class="lang-switcher__btn"
      :class="{ 'lang-switcher__btn--active': locale === 'en' }"
    >
      EN
    </NuxtLink>
  </div>
</template>

<script setup lang="ts">
const { locale } = useI18n()
const switchLocalePath = useSwitchLocalePath()
</script>

<style lang="scss" scoped>
.lang-switcher {
  display: flex;
  gap: 0.25rem;
}

.lang-switcher__btn {
  display: inline-block;
  padding: 0.35rem 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  border: 1px solid rgba($color-accent, 0.4);
  border-radius: 4px;
  background: transparent;
  color: $color-accent;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;

  &:hover {
    background: rgba($color-accent, 0.15);
    color: $color-white;
  }

  &--active {
    background: $color-accent;
    color: $color-bg-dark;
    border-color: $color-accent;
  }
}
</style>
