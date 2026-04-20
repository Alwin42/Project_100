<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="pt-28 px-6 max-w-7xl mx-auto w-full">
      
      <div class="mb-12 text-center md:text-left flex flex-col md:flex-row justify-between items-center gap-6">
        <div>
          <h2 class="text-3xl md:text-4xl font-extrabold text-gray-900 tracking-tight">
            What are you looking for today?
          </h2>
          <p class="text-gray-500 mt-2">Search thousands of items across local stores.</p>
        </div>

        <div class="w-full md:w-112.5 relative group">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
            <SearchIcon class="h-5 w-5 text-gray-400 group-focus-within:text-primary transition-colors" />
          </div>
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search for rice, milk, vegetables..." 
            class="w-full pl-11 pr-4 py-3.5 bg-white border border-gray-200 rounded-2xl shadow-sm focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all text-gray-700 font-medium"
          >
          <button class="absolute inset-y-1.5 right-1.5 bg-primary hover:opacity-90 text-white px-4 rounded-xl text-sm font-bold transition-all shadow-sm">
            Search
          </button>
        </div>
      </div>

      <section class="mb-16">
        <div class="flex items-center gap-2 mb-6">
          <div class="p-2 bg-accent-1/30 rounded-lg text-accent-2">
            <TrendingUpIcon class="w-5 h-5" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900">Trending Items</h3>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6">
          <div 
            v-for="item in trendingItems" 
            :key="item.id"
            class="bg-white rounded-2xl p-4 border border-gray-100 shadow-sm hover:shadow-md transition-all hover:-translate-y-1 cursor-pointer group"
          >
            <div class="w-full aspect-square rounded-xl bg-gray-50 mb-4 overflow-hidden relative flex items-center justify-center">
              <span class="text-4xl">{{ item.emoji }}</span>
              <div class="absolute inset-0 bg-linear-to-t from-black/5 to-transparent"></div>
            </div>
            
            <h4 class="font-bold text-gray-800 group-hover:text-primary transition-colors line-clamp-1">
              {{ item.name }}
            </h4>
            
            <div class="mt-2 flex items-center gap-1.5">
              <span class="relative flex h-2.5 w-2.5">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-secondary opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-primary"></span>
              </span>
              <p class="text-xs font-semibold text-primary">In {{ item.shopCount }} nearby shops</p>
            </div>
          </div>
        </div>
      </section>

      <section>
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-2">
            <div class="p-2 bg-secondary/20 rounded-lg text-primary">
              <StoreIcon class="w-5 h-5" />
            </div>
            <h3 class="text-2xl font-bold text-gray-900">Local Vendors Near You</h3>
          </div>
          <button class="text-sm font-semibold text-primary hover:text-primary/80">View Map &rarr;</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div 
            v-for="shop in nearbyShops" 
            :key="shop.id"
            class="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm hover:shadow-lg transition-all flex flex-col"
          >
            <div class="flex justify-between items-start mb-4">
              <div>
                <h4 class="text-lg font-bold text-gray-900">{{ shop.name }}</h4>
                <p class="text-sm text-gray-500 flex items-center gap-1 mt-1">
                  <MapPinIcon class="w-3.5 h-3.5" /> {{ shop.distance }} away
                </p>
              </div>
              <div class="flex items-center gap-1 bg-accent-1/40 text-yellow-700 px-2 py-1 rounded-md text-xs font-bold">
                <StarIcon class="w-3.5 h-3.5 fill-current" />
                {{ shop.rating }}
              </div>
            </div>

            <div class="mt-auto pt-4 border-t border-gray-50 flex gap-2">
              <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-md">Groceries</span>
              <span class="text-xs bg-gray-100 text-gray-600 px-2 py-1 rounded-md" v-if="shop.hasFreshProduce">Fresh Produce</span>
            </div>

            <button class="w-full mt-4 py-2.5 rounded-xl border-2 border-gray-100 font-bold text-gray-700 hover:border-primary hover:text-primary transition-colors">
              Check Stock
            </button>
          </div>
        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { SearchIcon, TrendingUpIcon, StoreIcon, MapPinIcon, StarIcon } from 'lucide-vue-next'

const searchQuery = ref('')

// Dummy Data for Trending Items
const trendingItems = ref([
  { id: 1, name: 'Matta Rice (5kg)', emoji: '🌾', shopCount: 12 },
  { id: 2, name: 'Milma Milk (Blue)', emoji: '🥛', shopCount: 8 },
  { id: 3, name: 'Coconut Oil (1L)', emoji: '🥥', shopCount: 15 },
  { id: 4, name: 'Onions (1kg)', emoji: '🧅', shopCount: 22 },
  { id: 5, name: 'Eggs (Dozen)', emoji: '🥚', shopCount: 19 },
])

// Dummy Data for Nearby Shops
const nearbyShops = ref([
  { id: 1, name: 'Kerala Traders', distance: '0.8 km', rating: 4.8, hasFreshProduce: true },
  { id: 2, name: 'FreshMart Supermarket', distance: '1.2 km', rating: 4.5, hasFreshProduce: true },
  { id: 3, name: 'Mini SupplyCo', distance: '2.5 km', rating: 4.2, hasFreshProduce: false },
  { id: 4, name: 'Green Valley Grocers', distance: '3.0 km', rating: 4.9, hasFreshProduce: true },
  { id: 5, name: 'Daily Needs Store', distance: '3.2 km', rating: 4.0, hasFreshProduce: false },
  { id: 6, name: 'Sunrise Minimart', distance: '4.1 km', rating: 4.6, hasFreshProduce: true },
])
</script>