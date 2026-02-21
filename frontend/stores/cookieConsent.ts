const COOKIE_CONSENT_KEY = 'cookie_consent'

function readStored(): boolean {
  if (import.meta.client) {
    try {
      const stored = localStorage.getItem(COOKIE_CONSENT_KEY)
      return stored === 'full' || stored === 'essential'
    } catch (_) {}
  }
  return false
}

export const useCookieConsentStore = defineStore('cookieConsent', () => {
  const accepted = ref(false)

  if (import.meta.client) accepted.value = readStored()

  function syncFromStorage() {
    if (import.meta.client) accepted.value = readStored()
  }

  function accept(value: 'full' | 'essential') {
    if (import.meta.client) {
      try {
        localStorage.setItem(COOKIE_CONSENT_KEY, value)
      } catch (_) {}
    }
    accepted.value = true
  }

  return { accepted, accept, syncFromStorage }
})
