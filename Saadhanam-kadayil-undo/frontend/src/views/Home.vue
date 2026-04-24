<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <nav class="flex justify-center gap-8 pt-8 mt-17 mb-16 text-lg font-medium text-gray-600">
      <a href="#" class="pb-2 border-b-[3px] border-black text-black font-semibold hover:-translate-y-0.5 transition-transform">Orders</a>
      <a href="#" class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">History</a>
      <a href="#" class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">Payments</a>
    </nav>

    <main class="max-w-6xl mx-auto px-6 w-full">
      
      <div class="flex flex-col md:flex-row justify-between items-center mb-12 gap-6">
        <h1 class="text-3xl md:text-4xl font-bold text-primary">
          Find what you need now!
        </h1>

        <div class="flex items-center bg-secondary rounded-full w-full md:w-112.5 h-12 shadow-sm relative overflow-hidden focus-within:ring-4 focus-within:ring-secondary/40 focus-within:shadow-lg transition-all duration-300 group">
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search your grocery item" 
            class="bg-transparent grow px-6 text-gray-800 placeholder-gray-600/70 focus:outline-none font-medium w-full"
          >
          <button class="bg-accent-1 h-full px-5 flex items-center justify-center hover:bg-accent-1/90 transition-colors duration-300">
            <SearchIcon class="w-5 h-5 text-accent-2 group-focus-within:scale-110 transition-transform duration-300" />
          </button>
        </div>
      </div>

      <section class="mb-16">
        <h2 class="text-2xl font-bold text-primary mb-6">Top Searches</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          <div 
            v-for="item in topSearches" 
            :key="item.id"
            class="bg-primary rounded-4xl p-4 flex flex-col shadow-lg hover:shadow-xl hover:shadow-primary/30 transition-all duration-300 hover:-translate-y-2 group cursor-pointer"
          >
            <div class="bg-white rounded-3xl h-36 mb-4 overflow-hidden flex items-center justify-center p-2 relative group-hover:scale-[0.98] transition-transform duration-300">
               <span class="text-6xl group-hover:scale-110 transition-transform duration-500">{{ item.emoji }}</span>
            </div>
            
            <div class="flex justify-between items-center mb-2 px-1">
              <h3 class="text-white font-bold text-lg">{{ item.name }}</h3>
              <span class="text-white text-xs font-medium bg-white/20 px-2 py-0.5 rounded-full">{{ item.status }}</span>
            </div>
            
            <div class="flex justify-between items-end mb-6 px-1">
              <div class="flex items-center gap-1.5">
                <MapPinIcon class="w-3.5 h-3.5 text-accent-2 fill-accent-2" />
                <span class="text-white/90 text-xs font-medium">{{ item.location }}</span>
              </div>
              <span class="text-white font-bold text-lg leading-none">₹{{ item.price }}</span>
            </div>
            
            <button class="bg-accent-1 text-primary font-bold text-sm tracking-wide rounded-full py-2.5 mx-2 hover:bg-white hover:shadow-md active:scale-95 transition-all duration-300">
              RESERVE
            </button>
          </div>

        </div>
      </section>

      <section>
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-primary">Nearby Vendors</h2>
          <button class="text-sm font-bold text-primary hover:text-primary/80 hover:translate-x-1 transition-all duration-300">View Map &rarr;</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="vendor in nearbyVendors" 
            :key="vendor.id"
            class="bg-white border-2 border-gray-100 rounded-4xl p-5 shadow-sm hover:shadow-xl hover:shadow-secondary/10 hover:border-secondary/50 transition-all duration-300 hover:-translate-y-1 flex flex-col group cursor-pointer"
          >
            <div class="flex items-start gap-4 mb-4">
              <div class="w-16 h-16 bg-secondary/10 group-hover:bg-secondary/20 rounded-2xl flex items-center justify-center shrink-0 transition-colors duration-300">
                <span class="text-3xl group-hover:scale-110 transition-transform duration-300">{{ vendor.emoji }}</span>
              </div>
              
              <div class="grow">
                <h3 class="text-lg font-bold text-gray-900 leading-tight group-hover:text-primary transition-colors duration-300">{{ vendor.name }}</h3>
                <div class="flex items-center gap-1 mt-1">
                  <StarIcon class="w-3.5 h-3.5 text-accent-2 fill-accent-2" />
                  <span class="text-sm font-bold text-gray-700">{{ vendor.rating }}</span>
                </div>
                
                <a 
                  v-if="vendor.mapUrl"
                  :href="vendor.mapUrl" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="inline-flex items-center gap-1 mt-1.5 text-gray-500 hover:text-primary transition-colors hover:bg-secondary/10 px-2 -ml-2 py-0.5 rounded-lg group/map"
                >
                  <MapPinIcon class="w-3.5 h-3.5 group-hover/map:animate-bounce group-hover/map:text-primary" />
                  <span class="text-sm font-medium underline-offset-2 group-hover/map:underline">Directions ({{ vendor.distance }})</span>
                </a>
                <div v-else class="flex items-center gap-1 mt-1.5 text-gray-500">
                  <MapPinIcon class="w-3.5 h-3.5" />
                  <span class="text-sm">{{ vendor.distance }} away</span>
                </div>

              </div>
            </div>

            <div class="mt-auto flex items-center justify-between pt-3 border-t border-gray-50">
              <span class="text-xs font-bold px-3 py-1.5 rounded-full transition-colors duration-300" :class="vendor.isOpen ? 'bg-secondary/20 text-primary' : 'bg-gray-100 text-gray-500'">
                {{ vendor.isOpen ? 'Open Now' : 'Closed' }}
              </span>
              <button class="text-primary font-bold text-sm hover:underline flex items-center gap-1 hover:translate-x-1 transition-transform duration-300">
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
const isModalOpen = ref(false)

const topSearches = ref([
  { id: 1, name: 'Tomato', emoji: '🍅', status: 'In Stock', location: 'Kerala Traders', price: '20/kg' },
  { id: 2, name: 'Curd', emoji: '🥣', status: 'In Stock', location: 'FreshMart', price: '35/pkt' },
  { id: 3, name: 'Egg', emoji: '🥚', status: 'In Stock', location: 'Daily Needs', price: '6/nos' }
])

const nearbyVendors = ref([
  { id: 1, name: 'Kerala Traders', distance: '0.8 km', rating: '4.8', isOpen: true, emoji: '🏪', mapUrl: 'http://google.com/maps' },
  { id: 2, name: 'FreshMart Supermarket', distance: '1.2 km', rating: '4.5', isOpen: true, emoji: '🛒', mapUrl: 'http://google.com/maps' },
  { id: 3, name: 'Mini SupplyCo', distance: '2.5 km', rating: '4.2', isOpen: false, emoji: '🏬', mapUrl: 'http://google.com/maps' }
])
</script>