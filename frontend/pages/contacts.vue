<template>
  <div class="my-container page">
    <h1 class="page__title">{{ t('pages.contactsTitle') }}</h1>
    <p class="page__intro">{{ t('contacts.intro') }}</p>
    <form class="contacts-form" @submit.prevent="onSubmit">
      <div class="contacts-form__field">
        <label for="contacts-name" class="contacts-form__label">{{ t('contacts.name') }} *</label>
        <input
          id="contacts-name"
          v-model="form.name"
          type="text"
          class="contacts-form__input"
          required
        />
      </div>
      <div class="contacts-form__field">
        <label for="contacts-email" class="contacts-form__label">{{ t('contacts.email') }} *</label>
        <input
          id="contacts-email"
          v-model="form.email"
          type="email"
          class="contacts-form__input"
          required
        />
      </div>
      <div class="contacts-form__field">
        <label for="contacts-phone" class="contacts-form__label">{{ t('contacts.phone') }} *</label>
        <input
          id="contacts-phone"
          v-model="form.phone"
          type="tel"
          class="contacts-form__input"
          required
        />
      </div>
      <div class="contacts-form__field">
        <label for="contacts-comment" class="contacts-form__label">{{ t('contacts.comment') }} *</label>
        <textarea
          id="contacts-comment"
          v-model="form.comment"
          class="contacts-form__input contacts-form__input--area"
          rows="4"
          required
        />
      </div>
      <label class="contacts-form__checkbox">
        <input v-model="form.privacyConsent" type="checkbox" required />
        <span class="contacts-form__checkbox-text">
          {{ t('contacts.privacyConsentPrefix') }}
          <NuxtLink :to="localePath('/privacy')" target="_blank" rel="noopener noreferrer" class="contacts-form__link">{{ t('contacts.privacyConsentLink') }}</NuxtLink>.
        </span>
      </label>
      <button type="submit" class="contacts-form__btn">{{ t('contacts.submit') }}</button>
      <p class="contacts-form__disclaimer">
        {{ t('contacts.disclaimerPrefix') }}
        <NuxtLink :to="localePath('/privacy')" target="_blank" rel="noopener noreferrer" class="contacts-form__link">{{ t('contacts.disclaimerLink1') }}</NuxtLink>{{ t('contacts.disclaimerAnd') }}
        <NuxtLink :to="localePath('/terms')" target="_blank" rel="noopener noreferrer" class="contacts-form__link">{{ t('contacts.disclaimerLink2') }}</NuxtLink>{{ t('contacts.disclaimerSuffix') }}
      </p>
    </form>
  </div>
</template>

<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
const form = reactive({
  name: '',
  email: '',
  phone: '',
  comment: '',
  privacyConsent: false,
})

function onSubmit() {
  // TODO: send to backend
}
</script>

<style lang="scss" scoped>
.page {
  padding: 4rem 0;
  max-width: 560px;
}

.page__title {
  @include headingBaseStyle(h1);
  color: $color-olive;
  margin: 0 0 1rem;
}

.page__intro {
  @include headingBaseStyle(article);
  color: $color-text;
  margin: 0 0 2rem;
  line-height: 1.5;
}

.contacts-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.contacts-form__field {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.contacts-form__label {
  @include headingBaseStyle(text-small);
  color: $color-olive;
  font-weight: 600;
}

.contacts-form__input {
  padding: 0.6rem 0.75rem;
  font: inherit;
  font-size: 1rem;
  border: 1px solid $color-accent;
  border-radius: 8px;
  background: $color-bg;
  color: $color-text;
  transition: border-color 0.2s;

  &:focus {
    outline: none;
    border-color: $color-main;
  }

  &--area {
    resize: vertical;
    min-height: 100px;
  }
}

.contacts-form__btn {
  align-self: flex-start;
  margin-top: 0.5rem;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  font-weight: 600;
  border: none;
  border-radius: 6px;
  background: $color-olive;
  color: $color-white;
  cursor: pointer;
  transition: background 0.2s;

  &:hover {
    background: $color-main-dark;
  }
}

.contacts-form__checkbox {
  display: flex;
  align-items: flex-start;
  gap: 0.5rem;
  cursor: pointer;
  @include headingBaseStyle(text-small);
  color: $color-text;
}

.contacts-form__checkbox input {
  margin-top: 0.25rem;
  flex-shrink: 0;
}

.contacts-form__checkbox-text {
  line-height: 1.4;
}

.contacts-form__link {
  color: $color-main;
  text-decoration: underline;
}

.contacts-form__disclaimer {
  margin: 0.5rem 0 0;
  @include headingBaseStyle(text-super-small);
  color: $color-text-muted;
  line-height: 1.4;
}
</style>
