import Link from 'next/link'

export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col items-center
                     justify-center bg-white px-6">
      <h1 className="text-5xl font-bold text-gray-900 mb-4">
        TripMind
      </h1>
      <p className="text-xl text-gray-500 mb-10">
        Track travel expenses together
      </p>
      <div className="flex gap-4">
        <Link
          href="/(auth)/login"
          className="px-6 py-3 bg-blue-500 text-white
                     rounded-lg font-medium hover:bg-blue-600"
        >
          Log In
        </Link>
        <Link
          href="/(auth)/register"
          className="px-6 py-3 border border-gray-300 text-gray-700
                     rounded-lg font-medium hover:bg-gray-50"
        >
          Sign Up
        </Link>
      </div>
    </main>
  )
}