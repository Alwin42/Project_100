import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Add an interceptor to automatically attach the token to EVERY request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const login = (credentials) => axios.post('http://localhost:8000/api/auth/login', credentials)
export const register = (userData) => axios.post('http://localhost:8000/api/auth/register', userData)

//  NEW: Fetch current user profile
export const getCurrentUser = () => api.get('/users/me')