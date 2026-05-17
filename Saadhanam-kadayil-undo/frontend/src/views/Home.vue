<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <nav class="flex justify-center gap-8 pt-8 mt-17 mb-12 text-lg font-medium text-gray-600">
      <a href="#" class="pb-2 border-b-[3px] border-black text-black font-semibold hover:-translate-y-0.5 transition-transform">Orders</a>
      <router-link to="/history" class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">History</router-link>
      <a href="#" class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">Payments</a>
    </nav> 

    <main class="max-w-6xl mx-auto px-6 w-full">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-12 gap-6">
        <h1 class="text-3xl md:text-5xl font-extrabold text-gray-900 tracking-tight leading-tight">
          Find what you <br class="hidden md:block"/>need right now!
        </h1>

        <div class="w-full md:w-112.5">
          <div class="flex items-center bg-white rounded-full h-14 shadow-sm border border-gray-200 focus-within:border-primary focus-within:ring-4 focus-within:ring-primary/10 transition-all duration-300 group relative overflow-hidden">
            
            <input 
              v-model="searchQuery"
              type="text" 
              placeholder="Search for 'Milk', 'Bread'..." 
              class="bg-transparent grow pl-6 pr-2 text-gray-800 placeholder-gray-400 focus:outline-none font-medium w-full text-lg"
            >
            
            <button 
              v-if="searchQuery" 
              @click="searchQuery = ''"
              class="p-2 text-gray-400 hover:text-gray-600 transition-colors active:scale-95"
            >
              <XIcon class="w-5 h-5" />
            </button>

            <button class="bg-primary h-full px-6 flex items-center justify-center hover:bg-primary/90 transition-colors duration-300 ml-2">
              <SearchIcon class="w-5 h-5 text-white group-focus-within:scale-110 transition-transform duration-300" />
            </button>
          </div>

          <div class="flex gap-2 mt-3 overflow-x-auto pb-2 scrollbar-hide">
            <span class="text-xs font-bold text-gray-400 py-1.5 pr-1">Popular:</span>
            <button 
              v-for="chip in ['Vegetables', 'Dairy & Eggs', 'Snacks', 'Beverages']" 
              :key="chip" 
              @click="searchQuery = chip" 
              class="text-xs font-bold px-3 py-1.5 rounded-full border border-gray-200 text-gray-500 hover:text-primary hover:border-primary/50 transition-colors whitespace-nowrap active:scale-95"
            >
              {{ chip }}
            </button>
          </div>
        </div>
      </div>

      <section class="mb-16 animate-in fade-in duration-500" v-if="!searchQuery && topSearches.length > 0">
        <h2 class="text-2xl font-bold text-gray-900 mb-6">Top Searches</h2>
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

      <section class="mb-16 animate-in fade-in duration-500" v-if="!searchQuery">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Nearby Vendors</h2>
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
            <h2 class="text-2xl font-bold text-gray-900 tracking-tight">
              {{ searchQuery ? 'Search Results' : 'Browse by Category' }}
            </h2>
            <p class="text-gray-500 text-sm mt-1 font-medium">
              {{ searchQuery ? `Showing results for "${searchQuery}"` : "Discover what's in stock across local stores." }}
            </p>
          </div>
        </div>

        <div v-if="allItems.length === 0" class="text-center py-12 text-gray-400">
          <Loader2Icon class="w-8 h-8 animate-spin mx-auto mb-3 text-secondary" />
          <p class="font-medium">Finding the freshest items...</p>
        </div>

        <div v-else-if="Object.keys(groupedItems).length === 0 && searchQuery" class="text-center py-16 bg-gray-50 rounded-4xl border border-gray-100 shadow-inner">
          <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-4 shadow-sm border border-gray-100">
            <SearchIcon class="w-6 h-6 text-gray-300" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">No items found</h3>
          <p class="text-gray-500 font-medium">We couldn't find any items matching "<span class="text-gray-900 font-bold">{{ searchQuery }}</span>".</p>
          <button @click="searchQuery = ''" class="mt-4 text-primary font-bold hover:underline">Clear Search</button>
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
                  index > 1 && !searchQuery ? 'hidden md:flex' : 'flex',
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
import { ref, computed, onMounted } from 'vue' 
import axios from 'axios' 
import Navbar from '../components/Navbar.vue'
import { SearchIcon, MapPinIcon, StarIcon, StoreIcon, Loader2Icon, PlusIcon, XIcon } from 'lucide-vue-next'

const searchQuery = ref('')
const isModalOpen = ref(false)
const allItems = ref([])

const topSearches = ref([]) 
const nearbyVendors = ref([])

const groupedItems = computed(() => {
  const groups = {};
  const query = searchQuery.value.toLowerCase().trim();
  
  const filteredItems = allItems.value.filter(item => {
    if (!query) return true; 
    
    const itemName = item.name ? item.name.toLowerCase() : '';
    const categoryName = item.category ? item.category.toLowerCase() : '';
    
    return itemName.includes(query) || categoryName.includes(query);
  });

  filteredItems.forEach(item => {
    const cat = item.category || 'Other';
    if (!groups[cat]) {
      groups[cat] = [];
    }
    groups[cat].push(item);
  });
  
  return groups;
})

onMounted(async () => {
  try {
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
      alert("🎉 " + response.data.message);
    }
  } catch (error) {
    alert(error.response?.data?.error || "Failed to reserve item.");
  }
}
</script>