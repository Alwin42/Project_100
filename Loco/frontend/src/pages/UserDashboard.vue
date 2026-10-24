<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { useRouter } from 'vue-router'
import { 
  Calendar, CheckCircle, DollarSign, Heart, Clock, MapPin, 
  Star, MoreHorizontal, Plus, ArrowRight
} from 'lucide-vue-next'

// Import dummy data
import dashboardData from '../data/dashboard.json'

const router = useRouter()

// Map icon names from JSON to actual Lucide components
const iconMap = {
  Calendar,
  CheckCircle,
  DollarSign,
  Heart
}

// Dummy user name
const userName = 'Alwin'

// Helper to get status badge styles
const getStatusStyle = (status) => {
  switch (status) {
    case 'Confirmed': return 'bg-highlight/10 text-secondary'
    case 'Pending': return 'bg-yellow-50 text-yellow-600'
    case 'Completed': return 'bg-gray-100 text-gray-600'
    default: return 'bg-gray-100 text-gray-600'
  }
}
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- Header -->
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-10 gap-4">
        <div>
          <h1 class="text-3xl md:text-4xl font-bold text-gray-900">
            Welcome back, <span class="text-primary">{{ userName }}</span>
          </h1>
          <p class="text-gray-500 mt-2 text-lg">Here's what's happening with your bookings today.</p>
        </div>
        <button 
          @click="router.push('/home')"
          class="flex items-center gap-2 px-5 py-2.5 bg-primary text-white font-semibold rounded-xl hover:bg-primary/90 transition shadow-sm"
        >
          <Plus class="w-5 h-5" />
          Book New Service
        </button>
      </div>

      <!-- Stats Overview -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-10">
        <div 
          v-for="stat in dashboardData.stats" 
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
        
        <!-- Left Column: Upcoming Bookings (Takes 2/3 width) -->
        <div class="lg:col-span-2">
          <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden">
            <div class="px-6 py-5 border-b border-gray-100 flex items-center justify-between">
              <h2 class="text-lg font-bold text-gray-900">Upcoming Bookings</h2>
              <router-link to="/home" class="text-sm font-medium text-primary hover:underline flex items-center gap-1">
                View All <ArrowRight class="w-4 h-4" />
              </router-link>
            </div>
            
            <div class="divide-y divide-gray-50">
              <div 
                v-for="booking in dashboardData.upcomingBookings" 
                :key="booking.id"
                class="p-6 hover:bg-gray-50/50 transition"
              >
                <div class="flex items-start justify-between gap-4">
                  <div class="flex items-start gap-4">
                    <!-- Avatar -->
                    <div class="w-12 h-12 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white font-bold text-sm shadow-sm flex-shrink-0">
                      {{ booking.initials }}
                    </div>
                    <div>
                      <h3 class="font-semibold text-gray-900">{{ booking.service }}</h3>
                      <p class="text-sm text-gray-500 mt-0.5">by {{ booking.provider }}</p>
                      
                      <div class="flex items-center gap-4 mt-3 text-xs text-gray-500">
                        <span class="flex items-center gap-1">
                          <Calendar class="w-3.5 h-3.5" /> {{ booking.date }}
                        </span>
                        <span class="font-semibold text-gray-900">${{ booking.price }}</span>
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

        <!-- Right Column: Recent History (Takes 1/3 width) -->
        <div class="lg:col-span-1">
          <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden h-full">
            <div class="px-6 py-5 border-b border-gray-100">
              <h2 class="text-lg font-bold text-gray-900">Recent History</h2>
            </div>
            
            <div class="divide-y divide-gray-50">
              <div 
                v-for="item in dashboardData.recentHistory" 
                :key="item.id"
                class="p-5 hover:bg-gray-50/50 transition"
              >
                <div class="flex items-center gap-3 mb-3">
                  <div class="w-9 h-9 rounded-full bg-gray-100 flex items-center justify-center text-gray-600 font-bold text-xs flex-shrink-0">
                    {{ item.initials }}
                  </div>
                  <div class="flex-1 min-w-0">
                    <h4 class="text-sm font-semibold text-gray-900 truncate">{{ item.service }}</h4>
                    <p class="text-xs text-gray-500">{{ item.date }}</p>
                  </div>
                </div>
                
                <div class="flex items-center justify-between pl-12">
                  <div class="flex items-center gap-0.5">
                    <Star v-for="n in item.rating" :key="n" class="w-3.5 h-3.5 text-yellow-500 fill-yellow-500" />
                    <Star v-for="n in (5 - item.rating)" :key="'e'+n" class="w-3.5 h-3.5 text-gray-200" />
                  </div>
                  <span class="text-xs font-medium text-gray-500">${{ item.price }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </main>
  </div>
</template>