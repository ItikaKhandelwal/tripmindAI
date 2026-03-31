import Constants from 'expo-constants'

const API_URL = Constants.expoConfig?.extra?.apiUrl as string

export async function apiFetch(
  path: string,
  options: RequestInit = {}
) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  })

  if (!response.ok) {
    const error = await response.json()
    throw new Error(error.detail || 'API request failed')
  }

  return response.json()
}

// Example usage:
// const trips = await apiFetch('/trips/')
// const health = await apiFetch('/health')