<template>
  <div class="layout">
    <header class="header">
      <div class="my-container header__inner">
        <NuxtLink to="/" class="header__logo">Luxury</NuxtLink>
        <nav class="header__nav">
          <NuxtLink to="/" class="header__link">Главная</NuxtLink>
          <NuxtLink to="/about" class="header__link">Обо мне</NuxtLink>
          <NuxtLink to="/contacts" class="header__link">Контакты</NuxtLink>
        </nav>
      </div>
    </header>
    <main class="main">
      <slot />
    </main>
    <footer class="footer">
      <div class="my-container footer__inner">
        <p class="footer__copy">© {{ new Date().getFullYear() }}</p>
      </div>
    </footer>
  </div>
</template>

<style lang="scss" scoped>
.layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: $color-bg;
  border-bottom: 1px solid $color-accent;
}

.header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.header__logo {
  @include headingBaseStyle(h3);
  color: $color-olive;
}

.header__nav {
  display: flex;
  gap: 1.5rem;
}

.header__link {
  color: $color-text;
  transition: color 0.2s;
  &:hover {
    color: $color-main;
  }
}

.main {
  flex: 1;
}

.footer {
  background: $color-bg-dark;
  color: $color-accent;
  padding: 1.5rem 0;
}

.footer__copy {
  margin: 0;
  @include headingBaseStyle(text-small-thin);
  opacity: 0.9;
}
</style>
