<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import { 
  Calendar, CheckCircle, DollarSign, Heart, Clock, MapPin, 
  Star, MoreHorizontal, Plus, ArrowRight, Loader2
} from 'lucide-vue-next'
import { getDashboardData } from '../api/auth'

const router = useRouter()
const isLoading = ref(true)
const error = ref(null)

// Real data from backend
const dashboardData = ref({
  stats: {
    upcoming_bookings: 0,
    completed_bookings: 0,
    total_spent: 0,
    saved_providers: 0
  },
  upcoming_bookings: [],
  recent_history: []
})

// Map backend stats to frontend format
const stats = ref([
  { label: 'Upcoming', value: '0', icon: 'Calendar', color: 'bg-primary/10 text-primary' },
  { label: 'Completed', value: '0', icon: 'CheckCircle', color: 'bg-highlight/10 text-secondary' },
  { label: 'Total Spent', value: '$0', icon: 'DollarSign', color: 'bg-accent/20 text-secondary' },
  { label: 'Saved Pros', value: '0', icon: 'Heart', color: 'bg-red-50 text-red-500' }
])

// Map icon names to components
const iconMap = {
  Calendar,
  CheckCircle,
  DollarSign,
  Heart
}

// Format date for display
const formatDate = (dateString) => {
  if (!dateString) return 'Not scheduled'
  const date = new Date(dateString)
  const today = new Date()
  const tomorrow = new Date(today)
  tomorrow.setDate(tomorrow.getDate() + 1)
  
  if (date.toDateString() === today.toDateString()) {
    return `Today, ${date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}`
  } else if (date.toDateString() === tomorrow.toDateString()) {
    return `Tomorrow, ${date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}`
  }
  return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
}

// Get status badge style
const getStatusStyle = (status) => {
  switch (status.toLowerCase()) {
    case 'confirmed': return 'bg-highlight/10 text-secondary'
    case 'pending': return 'bg-yellow-50 text-yellow-600'
    case 'completed': return 'bg-gray-100 text-gray-600'
    case 'cancelled': return 'bg-red-50 text-red-600'
    default: return 'bg-gray-100 text-gray-600'
  }
}

// Fetch dashboard data
const fetchDashboardData = async () => {
  try {
    isLoading.value = true
    error.value = null
    
    const response = await getDashboardData()
    const data = response.data
    
    // Update stats
    stats.value = [
      { 
        label: 'Upcoming', 
        value: data.stats.upcoming_bookings.toString(), 
        icon: 'Calendar', 
        color: 'bg-primary/10 text-primary' 
      },
      { 
        label: 'Completed', 
        value: data.stats.completed_bookings.toString(), 
        icon: 'CheckCircle', 
        color: 'bg-highlight/10 text-secondary' 
      },
      { 
        label: 'Total Spent', 
        value: `$${data.stats.total_spent.toFixed(2)}`, 
        icon: 'DollarSign', 
        color: 'bg-accent/20 text-secondary' 
      },
      { 
        label: 'Saved Pros', 
        value: data.stats.saved_providers.toString(), 
        icon: 'Heart', 
        color: 'bg-red-50 text-red-500' 
      }
    ]
    
    // Update bookings
    dashboardData.value = {
      stats: data.stats,
      upcoming_bookings: data.upcoming_bookings.map(booking => ({
        ...booking,
        date: formatDate(booking.booking_date),
        formattedAmount: `$${booking.amount.toFixed(2)}`
      })),
      recent_history: data.recent_history.map(booking => ({
        ...booking,
        date: formatDate(booking.booking_date),
        formattedAmount: `$${booking.amount.toFixed(2)}`
      }))
    }
    
  } catch (err) {
    console.error('Failed to fetch dashboard data:', err)
    error.value = 'Failed to load dashboard data. Please try again.'
    
    if (err.response?.status === 401) {
      localStorage.removeItem('token')
      router.push('/auth')
    }
  } finally {
    isLoading.value = false
  }
}

// Fetch data on mount
onMounted(() => {
  fetchDashboardData()
})
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- Loading State -->
      <div v-if="isLoading" class="flex items-center justify-center min-h-[60vh]">
        <div class="text-center">
          <Loader2 class="w-12 h-12 animate-spin text-primary mx-auto mb-4" />
          <p class="text-gray-600">Loading your dashboard...</p>
        </div>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="text-center py-12">
        <div class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-xl mb-4">
          {{ error }}
        </div>
        <button 
          @click="fetchDashboardData"
          class="px-6 py-2 bg-primary text-white rounded-lg hover:bg-primary/90 transition"
        >
          Retry
        </button>
      </div>

      <!-- Dashboard Content -->
      <div v-else>
        <!-- Header -->
        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-10 gap-4">
          <div>
            <h1 class="text-3xl md:text-4xl font-bold text-gray-900">
              Welcome back
            </h1>
            <p class="text-gray-500 mt-2 text-lg">Here's what's happening with your bookings today.</p>
          </div>
          <button 
            @click="router.push('/services')"
            class="flex items-center gap-2 px-5 py-2.5 bg-primary text-white font-semibold rounded-xl hover:bg-primary/90 transition shadow-sm"
          >
            <Plus class="w-5 h-5" />
            Book New Service
          </button>
        </div>

        <!-- Stats Overview -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-10">
          <div 
            v-for="stat in stats" 
            :key="stat.label"
            class="bg-white border border-gray-100 rounded-2xl p-5 hover:border-primary/10 transition"
          >
            <div class="flex items-center justify-between mb-4">
              <div class="w-10 h-10 rounded-xl flex items-center justify-center" :class="stat.color">
                <component :is="iconMap[stat.icon]" class="w-5 h-5" />
              </div>
              <MoreHorizontal class="w-5 h-5 text-gray-300" />
            </div>
            <p class="text-2xl font-bold text-gray-900">{{ stat.value }}</p>
            <p class="text-sm text-gray-500 mt-1">{{ stat.label }}</p>
          </div>
        </div>

        <!-- Main Content Grid -->
        <div class="grid lg:grid-cols-3 gap-6 md:gap-8">
          
          <!-- Left Column: Upcoming Bookings -->
          <div class="lg:col-span-2">
            <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
              <div class="px-6 py-5 border-b border-gray-100 flex items-center justify-between">
                <h2 class="text-lg font-bold text-gray-900">Upcoming Bookings</h2>
                <router-link to="/services" class="text-sm font-medium text-primary hover:underline flex items-center gap-1">
                  View All <ArrowRight class="w-4 h-4" />
                </router-link>
              </div>
              
              <div v-if="dashboardData.upcoming_bookings.length === 0" class="p-12 text-center text-gray-500">
                <Calendar class="w-12 h-12 mx-auto mb-3 text-gray-300" />
                <p>No upcoming bookings</p>
                <button 
                  @click="router.push('/services')"
                  class="mt-4 text-primary font-medium hover:underline"
                >
                  Browse Services
                </button>
              </div>
              
              <div v-else class="divide-y divide-gray-50">
                <div 
                  v-for="booking in dashboardData.upcoming_bookings" 
                  :key="booking.bid"
                  class="p-6 hover:bg-gray-50/50 transition"
                >
                  <div class="flex items-start justify-between gap-4">
                    <div class="flex items-start gap-4">
                      <!-- Avatar -->
                      <div class="w-12 h-12 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white font-bold text-sm shadow-sm flex-shrink-0">
                        {{ booking.provider_initials }}
                      </div>
                      <div>
                        <h3 class="font-semibold text-gray-900">{{ booking.service_title }}</h3>
                        <p class="text-sm text-gray-500 mt-0.5">by {{ booking.provider_name }}</p>
                        
                        <div class="flex items-center gap-4 mt-3 text-xs text-gray-500">
                          <span class="flex items-center gap-1">
                            <Calendar class="w-3.5 h-3.5" /> {{ booking.date }}
                          </span>
                          <span class="font-semibold text-gray-900">{{ booking.formattedAmount }}</span>
                        </div>
                      </div>
                    </div>
                    
                    <!-- Status Badge -->
                    <span class="px-3 py-1 text-xs font-semibold rounded-full whitespace-nowrap" :class="getStatusStyle(booking.status)">
                      {{ booking.status }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Column: Recent History -->
          <div class="lg:col-span-1">
            <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden h-full">
              <div class="px-6 py-5 border-b border-gray-100">
                <h2 class="text-lg font-bold text-gray-900">Recent History</h2>
              </div>
              
              <div v-if="dashboardData.recent_history.length === 0" class="p-8 text-center text-gray-500">
                <CheckCircle class="w-10 h-10 mx-auto mb-2 text-gray-300" />
                <p class="text-sm">No completed bookings yet</p>
              </div>
              
              <div v-else class="divide-y divide-gray-50">
                <div 
                  v-for="item in dashboardData.recent_history" 
                  :key="item.bid"
                  class="p-5 hover:bg-gray-50/50 transition"
                >
                  <div class="flex items-center gap-3 mb-3">
                    <div class="w-9 h-9 rounded-full bg-gray-100 flex items-center justify-center text-gray-600 font-bold text-xs flex-shrink-0">
                      {{ item.provider_initials }}
                    </div>
                    <div class="flex-1 min-w-0">
                      <h4 class="text-sm font-semibold text-gray-900 truncate">{{ item.service_title }}</h4>
                      <p class="text-xs text-gray-500">{{ item.date }}</p>
                    </div>
                  </div>
                  
                  <div class="flex items-center justify-between pl-12">
                    <span class="text-xs text-gray-500">{{ item.formattedAmount }}</span>
                    <span class="px-2 py-1 text-xs font-medium rounded-full bg-gray-100 text-gray-600">
                      {{ item.status }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </main>
  </div>
</template>