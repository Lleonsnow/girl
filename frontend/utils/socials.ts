export const SOCIAL_IDS = [
  'instagram',
  'telegram',
  'tiktok',
  'twitch',
  'youtube',
  'discord',
  'boosty',
] as const

export type SocialId = (typeof SOCIAL_IDS)[number]

export interface SocialLink {
  id: SocialId
  name: string
  url: string
}

const LABELS: Record<SocialId, string> = {
  instagram: 'Instagram',
  telegram: 'Telegram',
  tiktok: 'TikTok',
  twitch: 'Twitch',
  youtube: 'YouTube',
  discord: 'Discord',
  boosty: 'Boosty',
}

export function getSocialLinks(urlOverrides?: Partial<Record<SocialId, string>>): SocialLink[] {
  return SOCIAL_IDS.map((id) => ({
    id,
    name: LABELS[id],
    url: urlOverrides?.[id] ?? '#',
  }))
}
