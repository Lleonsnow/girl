export default defineNuxtConfig({
  compatibilityDate: '2025-02-16',
  modules: ['@pinia/nuxt', '@nuxtjs/i18n'],
  css: ['~/assets/scss/main.scss'],
  i18n: {
    locales: [
      { code: 'ru', language: 'ru', file: 'ru.json' },
      { code: 'en', language: 'en', file: 'en.json' },
    ],
    defaultLocale: 'ru',
    strategy: 'prefix_except_default',
    langDir: 'locales',
  },
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000',
    },
  },
  devServer: {
    port: 3000,
  },
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "~/assets/scss/base/variables.scss" as *; @use "~/assets/scss/base/mixins.scss" as *;',
        },
      },
    },
  },
})
