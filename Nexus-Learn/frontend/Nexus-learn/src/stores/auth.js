import { defineStore } from 'pinia';
import api from '../services/api';
import router from '../router';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('access_token') || null,
    user: null,
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    // LOGIN ACTION
    async login(username, password) {
      try {
        const response = await api.post('login/', { username, password });
        
        // Save tokens to Local Storage
        this.token = response.data.access;
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);
        
        // Redirect to Dashboard
        router.push('/dashboard');
      } catch (error) {
        console.error("Login failed:", error);
        throw error; // Let the component handle the error message
      }
    },

    // LOGOUT ACTION
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      router.push('/login');
    }
  }
});