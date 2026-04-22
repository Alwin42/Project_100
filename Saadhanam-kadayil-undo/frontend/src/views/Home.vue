<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <nav class="flex justify-center gap-8 pt-8 mt-9 mb-16 text-lg font-medium text-gray-600">
      <a href="#" class="pb-2 border-b-[3px] border-black text-black font-semibold">Orders</a>
      <a href="#" class="pb-2 hover:text-black transition-colors">History</a>
      <a href="#" class="pb-2 hover:text-black transition-colors">Payments</a>
    </nav>

    <main class="max-w-6xl mx-auto px-6 w-full">
      
      <div class="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
        <h1 class="text-3xl md:text-4xl font-bold text-primary">
          Find what you need now!
        </h1>

        <div class="flex items-center bg-secondary rounded-full w-full md:w-112.5 h-12 shadow-sm relative overflow-hidden">
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search your grocery item" 
            class="bg-transparent grow px-6 text-gray-800 placeholder-gray-600/70 focus:outline-none font-medium w-full"
          >
          <button class="bg-accent-1 h-full px-5 flex items-center justify-center hover:brightness-95 transition-all">
            <SearchIcon class="w-5 h-5 text-accent-2" />
          </button>
        </div>
      </div>

      <section class="mb-16">
        <h2 class="text-2xl font-bold text-primary mb-6">Top Searches</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          <div 
            v-for="item in topSearches" 
            :key="item.id"
            class="bg-primary rounded-4xl p-4 flex flex-col shadow-lg transition-transform hover:-translate-y-1"
          >
            <div class="bg-white rounded-3xl h-36 mb-4 overflow-hidden flex items-center justify-center p-2 relative">
               <span class="text-6xl">{{ item.emoji }}</span>
            </div>
            
            <div class="flex justify-between items-center mb-2 px-1">
              <h3 class="text-white font-bold text-lg">{{ item.name }}</h3>
              <span class="text-white text-xs font-medium">{{ item.status }}</span>
            </div>
            
            <div class="flex justify-between items-end mb-6 px-1">
              <div class="flex items-center gap-1.5">
                <MapPinIcon class="w-3.5 h-3.5 text-accent-2 fill-accent-2" />
                <span class="text-white text-xs font-medium">{{ item.location }}</span>
              </div>
              <span class="text-white font-bold text-lg leading-none">{{ item.price }}</span>
            </div>
            
            <button class="bg-accent-1 text-primary font-bold text-sm tracking-wide rounded-full py-2.5 mx-2 hover:brightness-105 active:scale-95 transition-all">
              RESERVE
            </button>
          </div>

        </div>
      </section>

      <section>
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-primary">Nearby Vendors</h2>
          <button class="text-sm font-bold text-primary hover:text-primary/80 transition-colors">View Map &rarr;</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="vendor in nearbyVendors" 
            :key="vendor.id"
            class="bg-white border-2 border-gray-100 rounded-4xl p-5 shadow-sm hover:shadow-lg hover:border-secondary/50 transition-all flex flex-col"
          >
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 bg-secondary/20 rounded-2xl flex items-center justify-center shrink-0">
                <span class="text-3xl">{{ vendor.emoji }}</span>
              </div>
              
              <div class="grow">
                <h3 class="text-lg font-bold text-gray-900 leading-tight">{{ vendor.name }}</h3>
                <div class="flex items-center gap-1 mt-1">
                  <StarIcon class="w-3.5 h-3.5 text-accent-2 fill-accent-2" />
                  <span class="text-sm font-bold text-gray-700">{{ vendor.rating }}</span>
                </div>
                <div class="flex items-center gap-1 mt-1 text-gray-500">
                  <MapPinIcon class="w-3.5 h-3.5" />
                  <span class="text-sm">{{ vendor.distance }} away</span>
                </div>
              </div>
            </div>

            <div class="mt-auto flex items-center justify-between">
              <span class="text-xs font-bold px-3 py-1.5 rounded-full" :class="vendor.isOpen ? 'bg-secondary/20 text-primary' : 'bg-gray-100 text-gray-500'">
                {{ vendor.isOpen ? 'Open Now' : 'Closed' }}
              </span>
              <button class="text-primary font-bold text-sm hover:underline flex items-center gap-1">
                <StoreIcon class="w-4 h-4" />
                Visit Shop
              </button>
            </div>
          </div>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { SearchIcon, MapPinIcon, StarIcon, StoreIcon } from 'lucide-vue-next'

const searchQuery = ref('')

// Dummy Data for Top Searches
const topSearches = ref([
  { 
    id: 1, 
    name: 'Tomato', 
    emoji: '🍅', 
    status: 'In Stock', 
    location: 'Location of shop', 
    price: '20/kg' 
  },
  { 
    id: 2, 
    name: 'Curd', 
    emoji: '🥣', 
    status: 'In Stock', 
    location: 'Location of shop', 
    price: '35' 
  },
  { 
    id: 3, 
    name: 'Egg', 
    emoji: '🥚', 
    status: 'In Stock', 
    location: 'Location of shop', 
    price: '6/nos' 
  }
])

// Dummy Data for Nearby Vendors
const nearbyVendors = ref([
  { 
    id: 1, 
    name: 'Kerala Traders', 
    distance: '0.8 km', 
    rating: '4.8', 
    isOpen: true, 
    emoji: '🏪' 
  },
  { 
    id: 2, 
    name: 'FreshMart Supermarket', 
    distance: '1.2 km', 
    rating: '4.5', 
    isOpen: true, 
    emoji: '🛒' 
  },
  { 
    id: 3, 
    name: 'Mini SupplyCo', 
    distance: '2.5 km', 
    rating: '4.2', 
    isOpen: false, 
    emoji: '🏬' 
  }
])
</script>