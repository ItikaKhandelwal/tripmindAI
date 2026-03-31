export type TripStatus = 'planning' | 'active' | 'completed'
export type MemberRole = 'owner' | 'admin' | 'member'

export interface User {
  id: string
  email: string
  full_name?: string
  avatar_url?: string
  default_currency: string
  created_at: string
}

export interface Trip {
  id: string
  owner_id: string
  name: string
  destination?: string
  start_date?: string
  end_date?: string
  currency: string
  budget: number
  cover_image?: string
  status: TripStatus
  created_at: string
  updated_at: string
}

export interface Expense {
  id: string
  trip_id: string
  paid_by: string
  category_id?: string
  title: string
  amount: number
  currency: string
  date: string
  notes?: string
  receipt_url?: string
  created_at: string
}

export interface Category {
  id: string
  name: string
  icon?: string
  color?: string
  is_default: boolean
  user_id?: string
}

export interface TripMember {
  id: string
  trip_id: string
  user_id: string
  role: MemberRole
  joined_at: string
}