import { defineStore } from 'pinia'
import api from '../services/api'
import router from '../router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    // Initialize state from LocalStorage to handle page refreshes
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
        
        // Update State
        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        this.user = { username: username } // Set user object
        
        // Save to LocalStorage (Persist data)
        localStorage.setItem('access_token', this.accessToken)
        localStorage.setItem('refresh_token', this.refreshToken)
        localStorage.setItem('user_data', JSON.stringify(this.user))

        // Redirect to Dashboard
        router.push('/home') 
        
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
        // Redirect to login page after successful registration
        router.push('/login')
      } catch (err) {
        console.error("Registration failed:", err)
        this.error = "Registration failed. Try a different username."
        throw err
      } finally {
        this.loading = false
      }
    },

    // 3. LOGOUT ACTION
    logout() {
      // Clear State
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      
      // Clear LocalStorage
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user_data')
      
      // Redirect to Login
      router.push('/login')
    }
  }
})