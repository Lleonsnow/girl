const COOKIE_CONSENT_KEY = 'cookie_consent'
const COOKIE_CONSENT_ID_KEY = 'cookie_consent_id'
const COOKIE_CONSENT_ID_MAX_AGE = 365 * 24 * 60 * 60

function readStored(): boolean {
  if (import.meta.client) {
    try {
      const stored = localStorage.getItem(COOKIE_CONSENT_KEY)
      return stored === 'full' || stored === 'essential'
    } catch (_) {}
  }
  return false
}

function getConsentIdFromCookie(): string | null {
  if (!import.meta.client) return null
  const match = document.cookie.match(new RegExp(`(?:^|; )${COOKIE_CONSENT_ID_KEY}=([^;]*)`))
  return match ? decodeURIComponent(match[1]) : null
}

function setConsentIdCookie(id: string) {
  if (!import.meta.client) return
  document.cookie = `${COOKIE_CONSENT_ID_KEY}=${encodeURIComponent(id)}; path=/; max-age=${COOKIE_CONSENT_ID_MAX_AGE}; SameSite=Lax`
}

export const useCookieConsentStore = defineStore('cookieConsent', () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase as string

  const accepted = ref(false)

  if (import.meta.client) accepted.value = readStored()

  async function syncFromStorage() {
    if (!import.meta.client) return
    const consentId = getConsentIdFromCookie()
    if (consentId && apiBase) {
      try {
        const res = await $fetch<{ accepted: boolean; consent_type?: string }>(
          `${apiBase.replace(/\/$/, '')}/api/consent/check/`,
          { query: { id: consentId }, credentials: 'omit' }
        )
        if (res.accepted && res.consent_type) {
          accepted.value = true
          try {
            localStorage.setItem(COOKIE_CONSENT_KEY, res.consent_type)
          } catch (_) {}
          return
        }
      } catch (_) {}
    }
    accepted.value = readStored()
  }

  async function accept(value: 'full' | 'essential') {
    if (import.meta.client) {
      try {
        localStorage.setItem(COOKIE_CONSENT_KEY, value)
      } catch (_) {}
      if (apiBase) {
        try {
          const res = await $fetch<{ consent_id: string }>(
            `${apiBase.replace(/\/$/, '')}/api/consent/`,
            {
              method: 'POST',
              body: { consent_type: value },
              credentials: 'omit',
              headers: { 'Content-Type': 'application/json' },
            }
          )
          if (res.consent_id) setConsentIdCookie(res.consent_id)
        } catch (_) {}
      }
    }
    accepted.value = true
  }

  return { accepted, accept, syncFromStorage }
})
