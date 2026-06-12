<template>
  <div class="min-h-screen bg-gray-50 font-sans pb-20">
    
    <Navbar />

    <main class="max-w-4xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="mb-10 animate-in fade-in slide-in-from-bottom-4 duration-700">
        <router-link to="/home" class="text-primary hover:text-primary/80 font-medium "> &larr; Back to Home</router-link>
        <h1 class="text-3xl md:text-4xl font-bold text-gray-900 tracking-tight mt-6">Order History</h1>
        <p class="text-gray-500 font-medium mt-1">Track your recent reservations and past purchases.</p>
      </div>

      <div v-if="isLoading" class="text-center py-20 text-gray-400">
        <Loader2Icon class="w-10 h-10 animate-spin mx-auto mb-4 text-primary" />
        <p class="font-bold text-lg">Loading your history...</p>
      </div>

      <div v-else-if="orders.length === 0" class="bg-white rounded-4xl border border-gray-100 p-16 text-center shadow-sm">
        <div class="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mx-auto mb-4">
          <ShoppingBagIcon class="w-8 h-8 text-gray-400" />
        </div>
        <h3 class="text-2xl font-bold text-gray-900 mb-2">No orders yet</h3>
        <p class="text-gray-500 font-medium mb-6">Looks like you haven't reserved anything from local stores yet.</p>
        <button @click="router.push('/home')" class="bg-primary text-white font-bold px-8 py-3 rounded-full hover:bg-primary/90 transition-colors">
          Start Shopping
        </button>
      </div>

      <div v-else class="space-y-4">
        
        <div 
          v-for="order in orders" 
          :key="order._id"
          class="bg-white rounded-3xl p-5 md:p-6 border border-gray-100 shadow-sm hover:shadow-md hover:border-primary/20 transition-all duration-300 group"
        >
          <div class="flex justify-between items-start mb-4 border-b border-gray-50 pb-4">
            <div class="flex items-center gap-2">
              <StoreIcon class="w-5 h-5 text-gray-400 group-hover:text-primary transition-colors" />
              <h3 class="font-bold text-gray-900 text-lg">
                {{ order.vendorId ? order.vendorId.shopName : 'Local Store' }}
              </h3>
            </div>
            
            <span 
              class="px-3 py-1 text-xs font-bold rounded-full flex items-center gap-1.5"
              :class="{
                'bg-yellow-50 text-yellow-600 border border-yellow-100': order.status === 'Pending',
                'bg-primary/10 text-primary border border-primary/20': order.status === 'Accepted',
                'bg-red-50 text-red-600 border border-red-100': order.status === 'Declined'
              }"
            >
              <ClockIcon v-if="order.status === 'Pending'" class="w-3.5 h-3.5" />
              <CheckCircleIcon v-else-if="order.status === 'Accepted'" class="w-3.5 h-3.5" />
              <XCircleIcon v-else class="w-3.5 h-3.5" />
              {{ order.status }}
            </span>
          </div>

          <div class="flex items-center gap-4 mb-5">
            <div class="w-16 h-16 bg-gray-50 rounded-2xl flex items-center justify-center text-3xl shrink-0 group-hover:scale-105 transition-transform">
              {{ order.item.emoji || '📦' }}
            </div>
            <div class="grow">
              <h4 class="font-bold text-gray-900 text-xl">{{ order.item.name }}</h4>
              <p class="text-sm font-medium text-gray-500 mt-0.5">Order ID: <span class="text-gray-400">#{{ order._id.slice(-6).toUpperCase() }}</span></p>
            </div>
            <div class="text-right">
              <span class="font-bold text-gray-900 text-xl">₹{{ order.item.price }}</span>
            </div>
          </div>

          <div class="flex flex-wrap items-center gap-4 bg-gray-50 rounded-2xl p-3 border border-gray-100">
            <div class="flex items-center gap-1.5 text-sm font-bold text-gray-600">
              <CalendarIcon class="w-4 h-4 text-primary" />
              {{ formatDate(order.createdAt) }}
            </div>
            <div class="w-1.5 h-1.5 rounded-full bg-gray-300 hidden md:block"></div>
            <div class="flex items-center gap-1.5 text-sm font-bold text-gray-600">
              <ClockIcon class="w-4 h-4 text-secondary" />
              {{ formatTime(order.createdAt) }}
            </div>
          </div>

        </div>

      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import { 
  Loader2Icon, StoreIcon, ClockIcon, CheckCircleIcon, 
  XCircleIcon, CalendarIcon, ShoppingBagIcon 
} from 'lucide-vue-next'

const router = useRouter()
const orders = ref([])
const isLoading = ref(true)

// Fetch History on Page Load
onMounted(async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    alert("Please login to view your history.")
    router.push('/home')
    return
  }

  try {
    const response = await axios.get('http://localhost:3000/api/orders/history', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    if (response.data.success) {
      orders.value = response.data.history
    }
  } catch (error) {
    console.error("Failed to load history:", error)
  } finally {
    isLoading.value = false
  }
})

// Helper function to format the Date (e.g., "May 17, 2026")
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' }
  return new Date(dateString).toLocaleDateString('en-US', options)
}

// Helper function to format the Time (e.g., "2:30 PM")
const formatTime = (dateString) => {
  const options = { hour: 'numeric', minute: '2-digit', hour12: true }
  return new Date(dateString).toLocaleTimeString('en-US', options)
}
</script>