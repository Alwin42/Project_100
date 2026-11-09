import axios from 'axios'

// Create an axios instance with the base URL
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Add an interceptor to automatically attach the JWT token to EVERY request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// --- Auth Endpoints ---
export const login = (credentials) => axios.post('http://localhost:8000/api/auth/login', credentials)
export const register = (userData) => axios.post('http://localhost:8000/api/auth/register', userData)

// --- User Endpoints ---
export const getCurrentUser = () => api.get('/users/me')

// --- Dashboard Endpoints ---
export const getDashboardData = () => api.get('/dashboard/')
export const getDashboardStats = () => api.get('/dashboard/stats')
export const getUpcomingBookings = () => api.get('/dashboard/bookings/upcoming')
export const getBookingHistory = () => api.get('/dashboard/bookings/history')