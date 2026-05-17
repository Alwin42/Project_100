<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <nav class="flex justify-center gap-8 pt-8 mt-17 mb-16 text-lg font-medium text-gray-600">
      <a href="#" class="pb-2 border-b-[3px] border-black text-black font-semibold hover:-translate-y-0.5 transition-transform">Orders</a>
      <router-link to="/history"class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">History</router-link>
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

      <section class="mb-16" v-if="topSearches.length > 0">
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

      <section class="mb-16">
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
                <span class="text-3xl group-hover:scale-110 transition-transform duration-300">{{ vendor.emoji || '🏪' }}</span>
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

      <section class="mb-16">
        <div class="flex justify-between items-end mb-8">
          <div>
            <h2 class="text-2xl font-bold text-primary tracking-tight">Browse by Category</h2>
            <p class="text-gray-500 text-sm mt-1 font-medium">Discover what's in stock across local stores.</p>
          </div>
        </div>

        <div v-if="allItems.length === 0" class="text-center py-12 text-gray-400">
          <Loader2Icon class="w-8 h-8 animate-spin mx-auto mb-3 text-secondary" />
          <p class="font-medium">Finding the freshest items...</p>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          
          <div 
            v-for="(items, categoryName) in groupedItems" 
            :key="categoryName" 
            class="flex flex-col bg-white border border-gray-100 rounded-4xl p-5 shadow-sm"
          >
            <div class="flex justify-between items-center mb-5 pl-2 pr-1 border-b border-gray-50 pb-3">
              <h3 class="text-xl font-bold text-gray-900">{{ categoryName }}</h3>
              <button class="text-sm font-bold text-primary hover:text-primary/80 transition-colors">View All &rarr;</button>
            </div>

            <div class="flex flex-col gap-3">
              <div 
                v-for="(item, index) in items.slice(0, 4)" 
                :key="item._id" 
                class="items-center justify-between p-3 rounded-2xl border transition-all duration-300 group"
                :class="[
                  index > 1 ? 'hidden md:flex' : 'flex',
                  item.inStock ? 'bg-gray-50/50 hover:bg-white hover:shadow-md hover:border-primary/20 border-transparent' : 'bg-gray-50/30 border-gray-100 opacity-75 grayscale-[0.2]'
                ]"
              >
                <div class="flex items-center gap-4 overflow-hidden">
                  <div class="w-12 h-12 bg-white shadow-sm rounded-xl flex items-center justify-center text-2xl shrink-0 group-hover:scale-105 transition-transform duration-300">
                    {{ item.emoji || '📦' }}
                  </div>
                  <div class="truncate">
                    <h4 class="font-bold text-sm truncate flex items-center gap-2" :class="item.inStock ? 'text-gray-900 group-hover:text-primary transition-colors' : 'text-gray-500'">
                      {{ item.name }}
                      <span v-if="!item.inStock" class="text-[9px] uppercase tracking-wider font-extrabold bg-red-50 text-red-500 px-2 py-0.5 rounded-md border border-red-100 shrink-0">
                        Out of Stock
                      </span>
                    </h4>
                    <p class="text-xs text-gray-500 flex items-center gap-1 mt-0.5 truncate">
                      <StoreIcon class="w-3 h-3 shrink-0" />
                      {{ item.vendorId ? item.vendorId.shopName : 'Local Vendor' }}
                    </p>
                    <p class="text-sm font-bold mt-1" :class="item.inStock ? 'text-primary' : 'text-gray-400'">
                      ₹{{ item.price }} <span class="text-xs font-medium text-gray-400">/ {{ item.unit }}</span>
                    </p>
                  </div>
                </div>

                <button 
                  @click="item.inStock ? reserveItem(item) : null"
                  :disabled="!item.inStock"
                  class="p-2.5 rounded-xl shadow-sm border transition-all duration-300 shrink-0 ml-2 flex items-center justify-center"
                  :class="item.inStock ? 'bg-white hover:bg-primary text-gray-400 hover:text-white border-gray-100 active:scale-95' : 'bg-gray-100 text-gray-300 border-gray-100 cursor-not-allowed'"
                  :title="item.inStock ? 'Reserve Item' : 'Currently Unavailable'"
                >
                  <PlusIcon class="w-5 h-5" />
                </button>
              </div>
            </div>
            
          </div>

        </div>
      </section>

    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue' // Added computed!
import axios from 'axios' 
import Navbar from '../components/Navbar.vue'

import { SearchIcon, MapPinIcon, StarIcon, StoreIcon, Loader2Icon, PlusIcon } from 'lucide-vue-next'

const searchQuery = ref('')
const isModalOpen = ref(false)
const allItems = ref([])

const topSearches = ref([]) 
const nearbyVendors = ref([])

// NEW: Computed property to automatically group fetched items by their Category
const groupedItems = computed(() => {
  const groups = {};
  
  allItems.value.forEach(item => {
    // If an item somehow has no category, put it in "Other"
    const cat = item.category || 'Other';
    
    if (!groups[cat]) {
      groups[cat] = [];
    }
    groups[cat].push(item);
  });
  
  return groups;
})

// Fetch real data when the home page loads
onMounted(async () => {
  try {
    // 1. Fetch Nearby Vendors
    const vendorResponse = await axios.get('http://localhost:3000/api/public/vendors');
    if (vendorResponse.data.success) {
      nearbyVendors.value = vendorResponse.data.vendors.map(vendor => ({
        id: vendor._id,
        name: vendor.shopName,
        distance: 'Nearby',
        rating: 'New',
        isOpen: vendor.isOpen ?? true,
        emoji: '🏪', 
        mapUrl: vendor.mapUrl
      }));
    }

    // 2. Fetch All Items
    const itemsResponse = await axios.get('http://localhost:3000/api/public/items');
    if (itemsResponse.data.success) {
      allItems.value = itemsResponse.data.items;
    }
    
  } catch (error) {
    console.error("Failed to load home page data:", error);
  }
})

const reserveItem = async (item) => {
  const token = localStorage.getItem('token');
  
  if (!token) {
    alert("Please log in to reserve items!");
    isModalOpen.value = true;
    return;
  }

  try {
    const response = await axios.post('http://localhost:3000/api/orders/reserve', 
      { productId: item._id },
      { headers: { Authorization: `Bearer ${token}` } }
    );
    
    if (response.data.success) {
      alert("🎉 " + response.data.message); // Fixed broken emoji artifact
    }
  } catch (error) {
    alert(error.response?.data?.error || "Failed to reserve item.");
  }
}
</script>