<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="mb-6 animate-in fade-in slide-in-from-bottom-4 duration-700 ease-out">
        <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Order Logs</h1>
        <p class="text-gray-500 mt-1 font-medium">Review your past orders and customer history.</p>
      </div>

      <nav class="flex items-center gap-6 mb-10 border-b border-gray-200">
        <button 
          @click="router.push('/dashboard')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors"
        >
          Overview
        </button>
        <button class="pb-3 border-b-2 border-primary text-primary font-bold text-sm tracking-wide flex items-center gap-1.5">
          <FileTextIcon class="w-4 h-4" />
          Order Logs
        </button>
        <button 
          @click="router.push('/vendor-payments')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors flex items-center gap-1.5"
        >
          <CreditCardIcon class="w-4 h-4" />
          Payments
        </button>
      </nav>

      <div class="flex gap-3 mb-6">
        <button 
          v-for="filter in ['All', 'Accepted', 'Declined']" 
          :key="filter"
          @click="activeFilter = filter"
          class="px-5 py-2 rounded-full text-sm font-bold transition-all duration-300"
          :class="activeFilter === filter ? 'bg-gray-900 text-white' : 'bg-white border border-gray-200 text-gray-500 hover:border-gray-300 hover:text-gray-900'"
        >
          {{ filter }}
        </button>
      </div>

      <div class="bg-white rounded-4xl border border-gray-100 shadow-sm overflow-hidden">
        <div class="p-6 md:p-8 space-y-4">
          
          <div v-if="filteredOrders.length === 0" class="text-center py-12 text-gray-400">
            <p class="font-medium">No orders found in this category.</p>
          </div>

          <div 
            v-for="order in filteredOrders" 
            :key="order.id"
            class="flex flex-col md:flex-row md:items-center justify-between p-5 bg-gray-50 rounded-3xl border border-transparent hover:bg-white hover:border-gray-200 hover:shadow-md transition-all duration-300 group gap-4"
          >
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 bg-white rounded-2xl shadow-sm flex items-center justify-center text-2xl shrink-0 group-hover:scale-105 transition-transform">
                {{ order.emoji }}
              </div>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <h4 class="font-bold text-gray-900 text-lg">{{ order.itemName }}</h4>
                  <span class="text-xs font-bold text-gray-400 bg-gray-200/50 px-2 py-0.5 rounded-md">#{{ order.id }}</span>
                </div>
                <p class="text-sm font-medium text-gray-500 flex items-center gap-1.5">
                  <UserIcon class="w-3.5 h-3.5" /> {{ order.customerName }} 
                  <span class="mx-1">•</span> 
                  <ClockIcon class="w-3.5 h-3.5" /> {{ order.date }}
                </p>
              </div>
            </div>

            <div class="flex items-center justify-between md:justify-end gap-6 w-full md:w-auto border-t md:border-t-0 border-gray-200/50 pt-4 md:pt-0">
              <span class="font-bold text-gray-900 text-lg">₹{{ order.total }}</span>
              
              <div 
                class="flex items-center gap-1.5 px-3 py-1.5 rounded-full text-sm font-bold"
                :class="order.status === 'Accepted' ? 'bg-primary/10 text-primary' : 'bg-red-50 text-red-600'"
              >
                <CheckCircleIcon v-if="order.status === 'Accepted'" class="w-4 h-4" />
                <XCircleIcon v-else class="w-4 h-4" />
                {{ order.status }}
              </div>
            </div>
          </div>

        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import { FileTextIcon, CreditCardIcon, UserIcon, ClockIcon, CheckCircleIcon, XCircleIcon } from 'lucide-vue-next'

const router = useRouter()
const activeFilter = ref('All')

// Dummy Data (You will replace this with an axios call to fetch completed orders)
const pastOrders = ref([
  { id: 'ORD-892', customerName: 'alwinemmanuel424', itemName: 'Mixture', emoji: '📦', total: '45', date: 'Today, 2:30 PM', status: 'Accepted' },
  { id: 'ORD-891', customerName: 'johndoe99', itemName: 'Fresh Milk', emoji: '🥛', total: '32', date: 'Today, 11:15 AM', status: 'Accepted' },
  { id: 'ORD-890', customerName: 'sarah_smith', itemName: 'Lays Chips', emoji: '🥔', total: '20', date: 'Yesterday, 6:45 PM', status: 'Declined' },
  { id: 'ORD-889', customerName: 'mike_k', itemName: 'Kurukure', emoji: '🌶️', total: '20', date: 'Yesterday, 4:20 PM', status: 'Accepted' },
])

const filteredOrders = computed(() => {
  if (activeFilter.value === 'All') return pastOrders.value;
  return pastOrders.value.filter(order => order.status === activeFilter.value);
})
</script>