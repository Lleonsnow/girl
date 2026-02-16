<template>
  <div class="my-container page">
    <h1 class="page__title">Контакты</h1>
    <p class="page__text">Страница в разработке.</p>
  </div>
</template>

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
