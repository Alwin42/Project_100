import { defineStore } from 'pinia'
import api from '../services/api' // Ensure this path matches your api.js location

export const useDashboardStore = defineStore('dashboard', {
  state: () => ({
    timetable: [],
    reminders: [],
    loading: false,
    error: null
  }),

  getters: {
    // Filter the full timetable to return only today's classes
    todaysClasses: (state) => {
      const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
      const todayShort = days[new Date().getDay()] // e.g., "Wed" or "Mon"
      
      return state.timetable.filter(cls => cls.day === todayShort)
    }
  },

  actions: {
    async fetchTimetable() {
      this.loading = true
      try {
        const response = await api.get('timetable/')
        this.timetable = response.data
      } catch (err) {
        console.error("Failed to fetch timetable", err)
        this.error = "Could not load timetable"
      } finally {
        this.loading = false
      }
    },

    async fetchReminders() {
      try {
        const response = await api.get('reminders/')
        this.reminders = response.data
      } catch (err) {
        console.error("Failed to fetch reminders", err)
      }
    }
  }
})