import type { SocialId } from '~/utils/socials'

export interface SiteConfigSocial {
  telegram: string
  instagram: string
  tiktok: string
  twitch: string
  youtube: string
  discord: string
  boosty: string
}

export interface SiteConfigState {
  authorName: string
  authorPseudonym: string
  authorEmail: string
  siteUrl: string
  siteOwnerName: string
  siteOwnerNameEn: string
  siteContactEmail: string
  social: SiteConfigSocial
}

const defaultSocial: SiteConfigSocial = {
  telegram: '',
  instagram: '',
  tiktok: '',
  twitch: '',
  youtube: '',
  discord: '',
  boosty: '',
}

function defaultState(): SiteConfigState {
  return {
    authorName: '',
    authorPseudonym: '',
    authorEmail: '',
    siteUrl: '',
    siteOwnerName: '',
    siteOwnerNameEn: '',
    siteContactEmail: '',
    social: { ...defaultSocial },
  }
}

export const useSiteConfigStore = defineStore('siteConfig', () => {
  const config = useRuntimeConfig()
  const apiBase = (config.public.apiBase as string)?.replace(/\/$/, '') || ''

  const state = ref<SiteConfigState>(defaultState())

  const authorName = computed(() => state.value.authorName)
  const authorPseudonym = computed(() => state.value.authorPseudonym)
  const authorEmail = computed(() => state.value.authorEmail)
  const siteUrl = computed(() => state.value.siteUrl)
  const siteOwnerName = computed(() => state.value.siteOwnerName)
  const siteOwnerNameEn = computed(() => state.value.siteOwnerNameEn)
  const { locale } = useI18n()
  const siteOwnerNameLocalized = computed(() =>
    locale.value === 'en' ? (state.value.siteOwnerNameEn || state.value.siteOwnerName) : state.value.siteOwnerName
  )
  const siteContactEmail = computed(() => state.value.siteContactEmail)
  const social = computed(() => state.value.social)

  const socialOverrides = computed((): Partial<Record<SocialId, string>> => {
    const s = state.value.social
    const out: Partial<Record<SocialId, string>> = {}
    if (s.telegram) out.telegram = s.telegram
    if (s.instagram) out.instagram = s.instagram
    if (s.tiktok) out.tiktok = s.tiktok
    if (s.twitch) out.twitch = s.twitch
    if (s.youtube) out.youtube = s.youtube
    if (s.discord) out.discord = s.discord
    if (s.boosty) out.boosty = s.boosty
    return out
  })

  const boostyUrl = computed(() => state.value.social.boosty || 'https://boosty.to')

  async function fetchConfig() {
    if (!import.meta.client || !apiBase) return
    try {
      const res = await $fetch<SiteConfigState>(`${apiBase}/api/site-config/`, { credentials: 'omit' })
      const def = defaultState()
      state.value = {
        authorName: res.authorName ?? '',
        authorPseudonym: res.authorPseudonym ?? def.authorPseudonym,
        authorEmail: res.authorEmail ?? '',
        siteUrl: res.siteUrl ?? def.siteUrl,
        siteOwnerName: res.siteOwnerName ?? def.siteOwnerName,
        siteOwnerNameEn: (res as SiteConfigState).siteOwnerNameEn ?? def.siteOwnerNameEn,
        siteContactEmail: res.siteContactEmail ?? def.siteContactEmail,
        social: { ...defaultSocial, ...res.social },
      }
    } catch (_) {}
  }

  return {
    state,
    authorName,
    authorPseudonym,
    authorEmail,
    siteUrl,
    siteOwnerName,
    siteOwnerNameEn,
    siteOwnerNameLocalized,
    siteContactEmail,
    social,
    socialOverrides,
    boostyUrl,
    fetchConfig,
  }
})
