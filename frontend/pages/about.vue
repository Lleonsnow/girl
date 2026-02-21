<template>
  <div class="my-container page">
    <h1 class="page__title">{{ t('pages.aboutTitle') }}</h1>
    <p class="page__text">{{ t('pages.devText') }}</p>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
</script>

<style lang="scss" scoped>
.page {
  padding: 4rem 0;
}

.page__title {
  @include headingBaseStyle(h1);
  color: $color-olive;
  margin: 0 0 1rem;
}

.page__text {
  @include headingBaseStyle(article);
  color: $color-text;
}
</style>
