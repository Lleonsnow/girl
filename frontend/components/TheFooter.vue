<template>
  <footer class="footer">
    <div class="my-container footer__inner">
      <p class="footer__copy">© {{ year }} {{ siteName }}</p>
      <nav v-if="links.length" class="footer__links">
        <NuxtLink v-for="link in links" :key="link.to" :to="link.to" class="footer__link">{{ link.label }}</NuxtLink>
      </nav>
    </div>
  </footer>
</template>

<script setup lang="ts">
interface FooterLink {
  to: string
  label: string
}

withDefaults(
  defineProps<{
    siteName?: string
    links?: FooterLink[]
  }>(),
  { siteName: 'My Anesthesia', links: () => [] }
)

const year = new Date().getFullYear()
</script>

<style lang="scss" scoped>
.footer {
  background: $color-bg-dark;
  color: $color-accent;
  padding: 1.5rem 0;
  margin-top: auto;
}

.footer__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer__copy {
  margin: 0;
  @include headingBaseStyle(text-small-thin);
  opacity: 0.9;
}

.footer__links {
  display: flex;
  gap: 1.5rem;
}

.footer__link {
  color: inherit;
  @include headingBaseStyle(text-small-thin);
  text-decoration: none;
  opacity: 0.9;
  transition: opacity 0.2s;

  &:hover {
    opacity: 1;
  }
}
</style>
