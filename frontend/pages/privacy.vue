<template>
  <div class="my-container page">
    <h1 class="page__title">{{ t('pages.privacyTitle') }}</h1>
    <div class="page__body">
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s1Title') }}</h2>
        <p>{{ t('privacy.s1P1') }}</p>
        <p>{{ t('privacy.s1P2', { siteOwner: siteConfig.siteOwnerNameLocalized }) }}</p>
        <p>{{ t('privacy.s1P3', { siteUrl: siteConfig.siteUrl }) }}</p>
        <p>{{ t('privacy.s1P4') }}</p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s2Title') }}</h2>
        <p>{{ t('privacy.s2P1') }}</p>
        <ul>
          <li v-for="i in 6" :key="i">{{ t(`privacy.s2Li${i}`) }}</li>
        </ul>
        <p>{{ t('privacy.s2P2') }}</p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s3Title') }}</h2>
        <p>{{ t('privacy.s3P1') }}</p>
        <ul>
          <li v-for="i in 4" :key="i">{{ t(`privacy.s3Li${i}`) }}</li>
        </ul>
        <p>{{ t('privacy.s3P2') }}</p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s4Title') }}</h2>
        <p>{{ t('privacy.s4P1') }}</p>
        <ul>
          <li>{{ t('privacy.s4Li1') }}</li>
          <li>{{ t('privacy.s4Li2') }}</li>
        </ul>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s5Title') }}</h2>
        <p>{{ t('privacy.s5P1') }}</p>
        <p>{{ t('privacy.s5P2') }}</p>
        <p>{{ t('privacy.s5P3') }}</p>
        <p>{{ t('privacy.s5P4') }}</p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s6Title') }}</h2>
        <p>{{ t('privacy.s6P1') }}</p>
        <p>{{ t('privacy.s6P2') }}</p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s7Title') }}</h2>
        <p>{{ t('privacy.s7P1') }}</p>
        <ul>
          <li v-for="i in 3" :key="i">{{ t(`privacy.s7Li${i}`) }}</li>
        </ul>
        <p>{{ t('privacy.s7P2') }} <a :href="'mailto:' + siteConfig.siteContactEmail">{{ siteConfig.siteContactEmail }}</a></p>
      </section>
      <section class="policy-section">
        <h2 class="policy-section__title">{{ t('privacy.s8Title') }}</h2>
        <p>{{ t('privacy.s8P1') }}</p>
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
  margin: 0 0 1.5rem;
}

.page__body {
  @include headingBaseStyle(article);
  color: $color-text;
  line-height: 1.6;
}

.policy-section {
  margin-bottom: 1.5rem;

  &:last-child {
    margin-bottom: 0;
  }
}

.policy-section__title {
  @include headingBaseStyle(h2);
  color: $color-olive;
  margin: 0 0 0.75rem;
  font-size: 1.1rem;
}

.policy-section p {
  margin: 0 0 0.5rem;
}

.policy-section ul {
  margin: 0.5rem 0;
  padding-left: 1.5rem;
}

.policy-section li {
  margin-bottom: 0.25rem;
}

.policy-section a {
  color: $color-main;
  text-decoration: underline;
}
</style>
