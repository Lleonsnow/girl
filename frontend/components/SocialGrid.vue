<template>
  <section class="social-grid-section">
    <div class="my-container">
      <div class="social-grid">
        <a
          v-for="(item, i) in items"
          :key="item.id"
          :href="item.url"
          target="_blank"
          rel="noopener noreferrer"
          class="social-grid__item"
          :class="{ 'social-grid__item--full': isLastAlone(i) }"
        >
          <div class="social-grid__thumb-wrap">
            <img v-if="item.thumb" :src="item.thumb" alt="" class="social-grid__thumb" />
            <div v-else class="social-grid__thumb social-grid__thumb--placeholder" />
          </div>
          <span class="social-grid__name">{{ item.name }}</span>
        </a>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface GridItem {
  id: string
  name: string
  url: string
  thumb?: string
}

const props = defineProps<{
  items: GridItem[]
}>()

function isLastAlone(index: number) {
  return props.items.length % 2 === 1 && index === props.items.length - 1
}
</script>

<style lang="scss" scoped>
.social-grid-section {
  padding: 3rem 0;
}

.social-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, 560px);
  gap: 1.5rem;
  justify-content: center;
}

.social-grid__item {
  display: block;
  width: 560px;
  border-radius: 12px;
  overflow: hidden;
  background: $color-bg;
  text-decoration: none;
  color: $color-text;
  transition: transform 0.2s, box-shadow 0.2s;

  &--full {
    grid-column: 1 / -1;
    max-width: 100%;
    width: 100%;
  }

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba($color-olive, 0.15);
  }
}

.social-grid__thumb-wrap {
  width: 100%;
  height: 100px;
  background: $color-accent;
}

.social-grid__thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;

  &--placeholder {
    background: linear-gradient(135deg, $color-pistachio 0%, $color-main 100%);
  }
}

.social-grid__name {
  display: block;
  padding: 1rem;
  @include headingBaseStyle(text);
  color: $color-olive;
}
</style>
