<template>
  <div class="my-container page">
    <h1 class="page__title">{{ t('pages.termsTitle') }}</h1>
    <p class="page__meta">{{ t('terms.siteLabel', { siteUrl: siteConfig.siteUrl }) }} {{ t('terms.effectiveDate') }}</p>
    <div class="page__body">
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s1Title') }}</h2>
        <p>{{ t('terms.s1P1', { siteUrl: siteConfig.siteUrl }) }}</p>
        <p>{{ t('terms.s1P2', { siteOwner: siteConfig.siteOwnerNameLocalized }) }}</p>
        <p>{{ t('terms.s1P3') }}</p>
        <p>{{ t('terms.s1P4') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s2Title') }}</h2>
        <p>{{ t('terms.s2P1') }}</p>
        <p>{{ t('terms.s2P2') }}</p>
        <p>{{ t('terms.s2P3') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s3Title') }}</h2>
        <p>{{ t('terms.s3P1') }}</p>
        <p>{{ t('terms.s3P2') }}</p>
        <p>{{ t('terms.s3P3') }}</p>
        <p>{{ t('terms.s3P4') }}</p>
        <p>{{ t('terms.s3P5') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s4Title') }}</h2>
        <p>{{ t('terms.s4P1') }}</p>
        <p>{{ t('terms.s4P2') }}</p>
        <p>{{ t('terms.s4P3') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s5Title') }}</h2>
        <p>{{ t('terms.s5P1') }}</p>
        <ul>
          <li v-for="i in 5" :key="i">{{ t(`terms.s5Li${i}`) }}</li>
        </ul>
        <p>{{ t('terms.s5P2') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s6Title') }}</h2>
        <p>{{ t('terms.s6P1') }}</p>
        <p>{{ t('terms.s6P2') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s7Title') }}</h2>
        <p>{{ t('terms.s7P1') }}</p>
        <ul>
          <li v-for="i in 5" :key="i">{{ t(`terms.s7Li${i}`) }}</li>
        </ul>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s8Title') }}</h2>
        <p>{{ t('terms.s8P1') }}</p>
        <p>{{ t('terms.s8P2') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s9Title') }}</h2>
        <p>{{ t('terms.s9P1') }}</p>
        <p>{{ t('terms.s9P2') }}</p>
      </section>
      <section class="terms-section">
        <h2 class="terms-section__title">{{ t('terms.s10Title') }}</h2>
        <p>{{ t('terms.s10P1') }}</p>
        <p>{{ t('terms.s10P2') }}</p>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
const siteConfig = useSiteConfigStore()
</script>

<style lang="scss" scoped>
.page {
  padding: 4rem 0;
  max-width: 720px;
}

.page__title {
  @include headingBaseStyle(h1);
  color: $color-olive;
  margin: 0 0 0.5rem;
}

.page__meta {
  @include headingBaseStyle(text-small);
  color: $color-text-muted;
  margin: 0 0 1.5rem;
}

.page__body {
  @include headingBaseStyle(article);
  color: $color-text;
  line-height: 1.6;
}

.terms-section {
  margin-bottom: 1.5rem;

  &:last-child {
    margin-bottom: 0;
  }
}

.terms-section__title {
  @include headingBaseStyle(h2);
  color: $color-olive;
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
}

.terms-section p {
  margin: 0 0 0.5rem;
}

.terms-section ul {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.terms-section li {
  margin-bottom: 0.25rem;
}
</style>
