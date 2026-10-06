import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api/auth',
})

export const login = (credentials) => api.post('/login', credentials)
export const register = (userData) => api.post('/register', userData)