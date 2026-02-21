<template>
  <aside class="side-menu">
    <nav class="side-menu__nav">
      <NuxtLink :to="localePath('/')" class="side-menu__section" activeClass="side-menu__section--active">
        <span class="side-menu__icon-wrap"><IconHome class="side-menu__icon" /></span>
        <div class="side-menu__body">
          <span class="side-menu__title">{{ t('menu.mainTitle') }}</span>
          <span class="side-menu__sub">{{ t('menu.mainSub') }}</span>
        </div>
      </NuxtLink>

      <div class="side-menu__section side-menu__section--group">
        <NuxtLink :to="localePath('/about')" class="side-menu__icon-wrap" activeClass="side-menu__icon-wrap--active"><IconAbout class="side-menu__icon" /></NuxtLink>
        <div class="side-menu__body">
          <span class="side-menu__title">{{ t('menu.aboutTitle') }}</span>
          <div class="side-menu__sublinks">
            <NuxtLink :to="localePath('/about')" class="side-menu__sublink" activeClass="side-menu__sublink--active">{{ t('menu.aboutSub1') }}</NuxtLink>
            <NuxtLink :to="localePath('/photos')" class="side-menu__sublink" activeClass="side-menu__sublink--active">{{ t('menu.aboutSub2') }}</NuxtLink>
          </div>
        </div>
      </div>

      <div class="side-menu__section side-menu__section--group">
        <NuxtLink :to="localePath('/')" class="side-menu__icon-wrap" activeClass="side-menu__icon-wrap--active"><IconSocials class="side-menu__icon" /></NuxtLink>
        <div class="side-menu__body">
          <span class="side-menu__title">{{ t('menu.socialsTitle') }}</span>
          <div class="side-menu__sublinks">
            <a v-for="s in socialLinks" :key="s.id" :href="s.url" target="_blank" rel="noopener noreferrer" class="side-menu__sublink">{{ s.name }}</a>
          </div>
        </div>
      </div>

      <NuxtLink :to="localePath('/contacts')" class="side-menu__section" activeClass="side-menu__section--active">
        <span class="side-menu__icon-wrap"><IconContacts class="side-menu__icon" /></span>
        <div class="side-menu__body">
          <span class="side-menu__title">{{ t('menu.contactsTitle') }}</span>
          <span class="side-menu__sub">{{ t('menu.contactsSub') }}</span>
        </div>
      </NuxtLink>

      <div class="side-menu__section side-menu__section--group">
        <span class="side-menu__icon-wrap"><IconLang class="side-menu__icon" /></span>
        <div class="side-menu__body">
          <span class="side-menu__title">{{ t('menu.langTitle') }}</span>
          <LangSwitcher class="side-menu__lang" />
        </div>
      </div>
    </nav>
    <div class="side-menu__footer">
      <NuxtLink :to="localePath('/privacy')" class="side-menu__section side-menu__section--footer" activeClass="side-menu__section--active">
        <span class="side-menu__icon-wrap"><IconTerms class="side-menu__icon" /></span>
        <span class="side-menu__label">{{ t('menu.privacy') }}</span>
      </NuxtLink>
      <NuxtLink :to="localePath('/terms')" class="side-menu__section side-menu__section--footer" activeClass="side-menu__section--active">
        <span class="side-menu__icon-wrap"><IconTerms class="side-menu__icon" /></span>
        <span class="side-menu__label">{{ t('menu.agreement') }}</span>
      </NuxtLink>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { getSocialLinks } from '~/utils/socials'

const { t } = useI18n()
const localePath = useLocalePath()
const socialLinks = getSocialLinks()

const IconHome = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
  h('path', { d: 'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z' }),
  h('polyline', { points: '9 22 9 12 15 12 15 22' }),
])
const IconAbout = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' }, [
  h('circle', { cx: '12', cy: '8', r: '4' }),
  h('path', { d: 'M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2' }),
])
const IconSocials = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('circle', { cx: '18', cy: '5', r: '3' }),
  h('circle', { cx: '6', cy: '12', r: '3' }),
  h('circle', { cx: '18', cy: '19', r: '3' }),
  h('line', { x1: '8.59', y1: '13.51', x2: '15.42', y2: '17.49' }),
  h('line', { x1: '15.41', y1: '6.51', x2: '8.59', y2: '10.49' }),
])
const IconContacts = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('path', { d: 'M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z' }),
  h('polyline', { points: '22,6 12,13 2,6' }),
])
const IconLang = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('circle', { cx: '12', cy: '12', r: '10' }),
  h('line', { x1: '2', y1: '12', x2: '22', y2: '12' }),
  h('path', { d: 'M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z' }),
])
const IconTerms = () => h('svg', { class: 'side-menu__svg', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', 'stroke-width': '2' }, [
  h('path', { d: 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z' }),
  h('polyline', { points: '14 2 14 8 20 8' }),
  h('line', { x1: '16', y1: '13', x2: '8', y2: '13' }),
  h('line', { x1: '16', y1: '17', x2: '8', y2: '17' }),
])
</script>

<style lang="scss" scoped>
.side-menu {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 56px;
  background: $color-bg-dark;
  color: $color-accent;
  z-index: 200;
  transition: width 0.25s ease;
  overflow: hidden;
  display: flex;
  flex-direction: column;

  &:hover {
    width: 240px;
    box-shadow: 4px 0 20px rgba(0, 0, 0, 0.15);
  }
}

.side-menu__nav {
  flex: 1;
  padding: 0.5rem 0;
  display: flex;
  flex-direction: column;
  gap: 0;
  overflow-y: auto;
}

.side-menu__footer {
  padding: 0.75rem 0;
  border-top: 1px solid rgba($color-accent, 0.2);
}

.side-menu__section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0 0.75rem;
  height: 44px;
  min-height: 44px;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.2s, color 0.2s, height 0.25s ease, min-height 0.25s ease, padding 0.25s ease;
  box-sizing: border-box;
  overflow: hidden;

  &:hover {
    background: rgba($color-accent, 0.1);
    color: $color-white;
  }

  &--active {
    background: rgba($color-main, 0.25);
    color: $color-pistachio;
  }

  &--group {
    cursor: default;
  }

  &--group:hover {
    background: transparent;
    color: inherit;
  }

  &--footer {
    height: 44px;
    min-height: 44px;
  }

  &--footer .side-menu__label {
    @include headingBaseStyle(text-super-small);
  }
}

.side-menu:hover .side-menu__section {
  height: auto;
  min-height: 44px;
  padding: 0.5rem 0.75rem;
  align-items: flex-start;
}

.side-menu:hover .side-menu__section--footer {
  height: 44px;
  min-height: 44px;
  padding: 0 0.75rem;
  align-items: center;
}

.side-menu__section--group .side-menu__icon-wrap {
  cursor: pointer;
}

.side-menu__icon-wrap {
  flex-shrink: 0;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: inherit;
  text-decoration: none;

  &:hover {
    color: $color-white;
  }

  &--active {
    color: $color-pistachio;
  }
}

.side-menu__svg {
  width: 20px;
  height: 20px;
}

.side-menu__body {
  flex: 1;
  min-width: 0;
  opacity: 0;
  transform: translateX(-6px);
  transition: opacity 0.2s, transform 0.2s;
}

.side-menu:hover .side-menu__body,
.side-menu:hover .side-menu__label {
  opacity: 1;
  transform: translateX(0);
}

.side-menu__title {
  display: block;
  @include headingBaseStyle(text-small);
  font-weight: 600;
  margin-bottom: 0.125rem;
}

.side-menu__sub {
  display: block;
  @include headingBaseStyle(text-super-small);
  opacity: 0.85;
}

.side-menu__sublinks {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
  margin-top: 0.25rem;
}

.side-menu__sublink {
  @include headingBaseStyle(text-super-small);
  color: inherit;
  text-decoration: none;
  opacity: 0.9;
  padding: 0.125rem 0;
  pointer-events: auto;
  cursor: pointer;
  transition: opacity 0.2s;

  &:hover {
    opacity: 1;
    color: $color-pistachio;
  }

  &--active {
    color: $color-pistachio;
  }
}

.side-menu__label {
  @include headingBaseStyle(text-small);
  opacity: 0;
  transform: translateX(-6px);
  transition: opacity 0.2s, transform 0.2s;
  align-self: center;
}

.side-menu__lang {
  margin-top: 0.5rem;
}
</style>
