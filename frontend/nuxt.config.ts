export default defineNuxtConfig({
  compatibilityDate: '2025-02-16',
  css: ['~/assets/scss/main.scss'],
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
