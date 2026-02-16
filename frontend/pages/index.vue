<template>
  <div class="home">
    <section class="hero">
      <div class="my-container hero__inner">
        <h1 class="hero__title">Girl</h1>
        <p class="hero__subtitle">You, me, let's chat now...</p>
        <p class="hero__status">Online</p>
        <NuxtLink to="/contacts" class="hero__cta">Написать</NuxtLink>
      </div>
    </section>

    <section class="section section--alt">
      <div class="my-container">
        <h2 class="section__title">Обо мне</h2>
        <p class="section__text">
          Добро пожаловать. Здесь ты найдёшь ссылки на соцсети и контакты.
        </p>
      </div>
    </section>

    <section class="section">
      <div class="my-container">
        <h2 class="section__title">Связаться</h2>
        <p class="section__text">
          Хочешь общаться в личных сообщениях и получать эксклюзивный контент?
        </p>
        <NuxtLink to="/contacts" class="cta-button">Написать в личку</NuxtLink>
      </div>
    </section>
  </div>
</template>

<style lang="scss" scoped>
.home {
  background: $color-bg;
}

.hero {
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, $color-bg 0%, $color-accent 50%, $color-pistachio 100%);
  padding: 4rem 0;
}

.hero__inner {
  text-align: center;
}

.hero__title {
  @include headingBaseStyle(h1-error);
  color: $color-olive;
  margin: 0 0 0.5rem;
  letter-spacing: 0.02em;
}

.hero__subtitle {
  @include headingBaseStyle(text);
  color: $color-text;
  margin: 0 0 0.25rem;
}

.hero__status {
  @include headingBaseStyle(text-small);
  color: $color-main-dark;
  margin: 0 0 2rem;
}

.hero__cta {
  display: inline-block;
  padding: 0.75rem 2rem;
  background: $color-olive;
  color: $color-white;
  border-radius: 9999px;
  @include headingBaseStyle(text-small);
  transition: background 0.2s;
  &:hover {
    background: $color-main-dark;
  }
}

.section {
  padding: 4rem 0;
}

.section--alt {
  background: rgba($color-pistachio, 0.15);
}

.section__title {
  @include headingBaseStyle(h2);
  color: $color-olive;
  margin: 0 0 1rem;
}

.section__text {
  @include headingBaseStyle(article);
  color: $color-text;
  margin: 0 0 1.5rem;
  max-width: 40rem;
}

.cta-button {
  display: inline-block;
  padding: 0.75rem 2rem;
  background: $color-main;
  color: $color-white;
  border-radius: 9999px;
  @include headingBaseStyle(text-small);
  transition: background 0.2s;
  &:hover {
    background: $color-main-dark;
  }
}
</style>
