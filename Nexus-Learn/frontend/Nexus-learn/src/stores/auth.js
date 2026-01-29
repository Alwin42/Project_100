import { defineStore } from 'pinia'
import api from '../services/api'
import router from '../router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    // Check if token exists in localStorage on load
    accessToken: localStorage.getItem('access_token') || null,
    refreshToken: localStorage.getItem('refresh_token') || null,
    user: JSON.parse(localStorage.getItem('user_data')) || null,
    error: null,
    loading: false
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },

  actions: {
    // 1. LOGIN ACTION
    async login(username, password) {
      this.loading = true
      this.error = null
      
      try {
        const response = await api.post('login/', { username, password })
        
        // Save tokens to LocalStorage (so you stay logged in after refresh)
        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        
        localStorage.setItem('access_token', this.accessToken)
        localStorage.setItem('refresh_token', this.refreshToken)

        // Ideally, fetch user details here (optional for now)
        // this.user = { username: username } 
        
        // Redirect to Dashboard
        router.push('/dashboard') 
        
      } catch (err) {
        console.error("Login failed:", err)
        this.error = "Invalid username or password"
        throw err
      } finally {
        this.loading = false
      }
    },

    // 2. REGISTER ACTION
    async register(userData) {
      this.loading = true
      this.error = null
      try {
        await api.post('register/', userData)
        // Auto-login after register, or redirect to login page
        router.push('/login')
      } catch (err) {
        this.error = "Registration failed. Try a different username."
        throw err
      } finally {
        this.loading = false
      }
    },

    // 3. LOGOUT ACTION
    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user_data')
      
      router.push('/login')
    }
  }
})