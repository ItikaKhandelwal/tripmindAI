import { Redirect } from 'expo-router'

export default function Index() {
  // TODO: check if user is logged in
  // For now, always redirect to login
  const isLoggedIn = false

  if (isLoggedIn) {
    return <Redirect href="/(tabs)/" />
  }

  return <Redirect href="/(auth)/login" />
}