<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Welcome back, Partner!</h1>
          <p class="text-gray-500 mt-1 font-medium">Here is what is happening at your shop today.</p>
        </div>
        <button class="bg-primary text-white font-bold px-6 py-3 rounded-full hover:opacity-90 active:scale-95 transition-all shadow-md flex items-center gap-2">
          <PlusIcon class="w-5 h-5" />
          Add New Item
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        
        <div class="bg-primary rounded-4xl p-6 text-white shadow-lg relative overflow-hidden">
          <div class="absolute top-0 right-0 -mr-6 -mt-6 w-24 h-24 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
          <div class="flex justify-between items-start mb-4 relative z-10">
            <div class="p-2.5 bg-white/20 rounded-2xl">
              <ShoppingBagIcon class="w-6 h-6 text-white" />
            </div>
            <span class="bg-accent-1 text-primary text-xs font-bold px-3 py-1 rounded-full">+12% today</span>
          </div>
          <h3 class="text-white/80 font-medium mb-1 relative z-10">Total Orders</h3>
          <p class="text-4xl font-bold relative z-10">42</p>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm flex flex-col justify-between">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-secondary/20 rounded-2xl">
              <TrendingUpIcon class="w-6 h-6 text-primary" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Today's Revenue</h3>
            <p class="text-3xl font-bold text-gray-900">₹4,850</p>
          </div>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm flex flex-col justify-between">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-accent-1/40 rounded-2xl">
              <PackageIcon class="w-6 h-6 text-accent-2" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Active Items in Store</h3>
            <p class="text-3xl font-bold text-gray-900">128</p>
          </div>
        </div>

      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-2 bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-primary">Live Inventory</h2>
            <button class="text-sm font-bold text-primary hover:underline">View All</button>
          </div>

          <div class="space-y-4">
            <div 
              v-for="item in inventory" 
              :key="item.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-3xl hover:bg-secondary/10 transition-colors border border-transparent hover:border-secondary/30"
            >
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-3xl shadow-sm shrink-0">
                  {{ item.emoji }}
                </div>
                <div>
                  <h4 class="font-bold text-gray-900">{{ item.name }}</h4>
                  <p class="text-sm font-medium text-gray-500">{{ item.price }}</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <button 
                  @click="item.inStock = !item.inStock"
                  class="relative w-14 h-8 rounded-full transition-colors duration-300"
                  :class="item.inStock ? 'bg-primary' : 'bg-gray-300'"
                >
                  <div 
                    class="absolute top-1 left-1 bg-white w-6 h-6 rounded-full transition-transform duration-300 shadow-sm"
                    :class="item.inStock ? 'translate-x-6' : 'translate-x-0'"
                  ></div>
                </button>
                <span class="text-sm font-bold w-16 text-right" :class="item.inStock ? 'text-primary' : 'text-gray-400'">
                  {{ item.inStock ? 'In Stock' : 'Out' }}
                </span>
                <button class="p-2 text-gray-400 hover:text-primary transition-colors bg-white rounded-xl shadow-sm hover:shadow">
                  <Edit2Icon class="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-primary">Live Orders</h2>
            <span class="bg-red-100 text-red-600 text-xs font-bold px-2.5 py-1 rounded-full">3 Pending</span>
          </div>

          <div class="space-y-5">
            <div 
              v-for="order in activeOrders" 
              :key="order.id"
              class="border border-gray-100 rounded-3xl p-4 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden"
            >
              <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-accent-1"></div>
              
              <div class="flex justify-between items-start mb-2 pl-2">
                <h4 class="font-bold text-gray-900">{{ order.customerName }}</h4>
                <span class="text-xs font-bold text-gray-500">{{ order.time }}</span>
              </div>
              
              <p class="text-sm text-gray-600 font-medium pl-2 mb-4">
                {{ order.itemsCount }} items • <span class="text-primary font-bold">{{ order.total }}</span>
              </p>

              <div class="flex gap-2 pl-2">
                <button class="grow bg-gray-50 hover:bg-gray-100 text-gray-700 font-bold py-2 rounded-xl text-sm transition-colors">
                  Decline
                </button>
                <button class="grow bg-accent-1 text-primary hover:brightness-95 font-bold py-2 rounded-xl text-sm transition-colors shadow-sm">
                  Accept
                </button>
              </div>
            </div>
          </div>
          
        </div>

      </div>

    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { PlusIcon, ShoppingBagIcon, TrendingUpIcon, PackageIcon, Edit2Icon } from 'lucide-vue-next'

// Dummy Data mapped to your established UI patterns
const inventory = ref([
  { id: 1, name: 'Fresh Tomato', emoji: '🍅', price: '₹20/kg', inStock: true },
  { id: 2, name: 'Milma Curd', emoji: '🥣', price: '₹35/pack', inStock: true },
  { id: 3, name: 'Brown Eggs', emoji: '🥚', price: '₹6/nos', inStock: false },
  { id: 4, name: 'Matta Rice', emoji: '🌾', price: '₹45/kg', inStock: true },
])

const activeOrders = ref([
  { id: 101, customerName: 'Rahul K.', itemsCount: 4, total: '₹240', time: '2 mins ago' },
  { id: 102, customerName: 'Sneha P.', itemsCount: 1, total: '₹35', time: '5 mins ago' },
  { id: 103, customerName: 'Ajay V.', itemsCount: 8, total: '₹890', time: '12 mins ago' },
])
</script>