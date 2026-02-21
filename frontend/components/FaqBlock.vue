<template>
  <section class="faq-section">
    <div class="my-container">
      <div class="faq">
        <button
          v-for="(item, i) in items"
          :key="item.id"
          type="button"
          class="faq__item"
          :class="{ 'faq__item--open': openSet.has(i) }"
          @click="toggle(i)"
        >
          <span class="faq__question">{{ item.question }}</span>
          <span class="faq__icon" aria-hidden="true">{{ openSet.has(i) ? '−' : '+' }}</span>
          <div class="faq__answer-wrap">
            <p class="faq__answer">{{ item.answer }}</p>
          </div>
        </button>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface FaqItem {
  id: string
  question: string
  answer: string
}

defineProps<{
  title?: string
  items: FaqItem[]
}>()

const openSet = ref<Set<number>>(new Set())
function toggle(i: number) {
  const next = new Set(openSet.value)
  if (next.has(i)) next.delete(i)
  else next.add(i)
  openSet.value = next
}
</script>

<style lang="scss" scoped>
.faq-section {
  padding: 3rem 0;
  background: rgba($color-pistachio, 0.08);
}

.faq-section__title {
  @include headingBaseStyle(h2);
  color: $color-olive;
  margin: 0 0 1.5rem;
}

.faq {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.faq__item {
  display: block;
  width: 100%;
  text-align: left;
  padding: 1rem 1.25rem;
  background: $color-bg;
  border: 1px solid $color-accent;
  border-radius: 12px;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
  position: relative;
  padding-right: 3rem;

  &:hover {
    border-color: $color-main;
  }

  &--open {
    border-color: $color-main;
    background: rgba($color-main, 0.06);
  }
}

.faq__question {
  @include headingBaseStyle(text);
  color: $color-olive;
  display: block;
  padding-right: 1rem;
}

.faq__icon {
  position: absolute;
  right: 1.25rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.25rem;
  color: $color-main;
  line-height: 1;
}

.faq__answer-wrap {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 0.75s ease;
}

.faq__item--open .faq__answer-wrap {
  grid-template-rows: 1fr;
}

.faq__answer {
  min-height: 0;
  overflow: hidden;
  @include headingBaseStyle(article);
  color: $color-text;
  margin: 1rem 0 0;
  padding-top: 0.75rem;
  border-top: 1px solid $color-accent;
}
</style>
