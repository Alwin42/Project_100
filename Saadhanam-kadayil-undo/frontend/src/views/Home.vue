<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <div class="  border-b border-gray-100 py-2 mt-26 flex justify-center items-center gap-1.5 text-xs font-bold text-gray-500">
      <MapPinIcon class="w-3.5 h-3.5 text-primary" />
      Delivering to: <span class="text-gray-900 underline decoration-gray-300 underline-offset-2 cursor-pointer hover:text-primary">Select Location</span>
    </div>

    <nav class="flex justify-center gap-8 pt-6 mb-10 text-lg font-medium text-gray-600">
      <a href="#" class="pb-2 border-b-[3px] border-black text-black font-semibold hover:-translate-y-0.5 transition-transform">Fresh Stock</a>
      <router-link to="/history" class="pb-2 hover:text-black hover:-translate-y-0.5 transition-all duration-300">History</router-link>
    </nav> 

    <main class="max-w-6xl mx-auto px-6 w-full">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-12 gap-6">
        <h1 class="text-3xl md:text-5xl font-extrabold text-gray-900 tracking-tight leading-tight">
          Fresh catch & <br class="hidden md:block"/>premium cuts
        </h1>

        <div class="w-full md:w-112.5">
          <div class="flex items-center bg-white rounded-full h-14 shadow-sm border border-gray-200 focus-within:border-primary focus-within:ring-4 focus-within:ring-primary/10 transition-all duration-300 group relative overflow-hidden">
            
            <input 
              v-model="searchQuery"
              type="text" 
              placeholder="Search 'Seer Fish', 'Curry Cut'..." 
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
            <button 
              v-for="chip in ['All', 'Fish', 'Chicken', 'Mutton', 'Beef', 'Duck & Poultry', 'Farm Eggs']" 
              :key="chip" 
              @click="searchQuery = chip === 'All' ? '' : chip" 
              class="text-xs font-bold px-4 py-2 rounded-full border transition-all whitespace-nowrap active:scale-95"
              :class="(searchQuery === chip || (chip === 'All' && !searchQuery)) ? 'bg-primary text-white border-primary shadow-md' : 'bg-white border-gray-200 text-gray-600 hover:border-primary/50 hover:text-primary'"
            >
              {{ chip }}
            </button>
          </div>
        </div>
      </div>

      <section class="mb-16">
        
        <div v-if="allItems.length === 0" class="text-center py-12 text-gray-400">
          <Loader2Icon class="w-8 h-8 animate-spin mx-auto mb-3 text-secondary" />
          <p class="font-medium">Finding the freshest cuts...</p>
        </div>

        <div v-else-if="Object.keys(groupedItems).length === 0 && searchQuery" class="text-center py-16 bg-gray-50 rounded-4xl border border-gray-100 shadow-inner">
          <div class="w-16 h-16 bg-white rounded-full flex items-center justify-center mx-auto mb-4 shadow-sm border border-gray-100">
            <SearchIcon class="w-6 h-6 text-gray-300" />
          </div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">No items found</h3>
          <p class="text-gray-500 font-medium">We couldn't find any fresh stock matching "<span class="text-gray-900 font-bold">{{ searchQuery }}</span>".</p>
          <button @click="searchQuery = ''" class="mt-4 text-primary font-bold hover:underline">Clear Search</button>
        </div>

        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div 
            v-for="(items, categoryName) in groupedItems" 
            :key="categoryName" 
            class="flex flex-col bg-white border border-gray-100 rounded-4xl p-6 shadow-[0_4px_20px_-4px_rgba(0,0,0,0.05)]"
          >
            <div class="flex justify-between items-center mb-5 border-b border-gray-50 pb-4">
              <h3 class="text-2xl font-bold text-gray-900">{{ categoryName }}</h3>
              <span class="text-xs font-bold text-gray-400 bg-gray-100 px-3 py-1 rounded-full">{{ items.length }} items</span>
            </div>

            <div class="flex flex-col gap-4">
              <div 
                v-for="item in items.slice(0, 6)" 
                :key="item._id" 
                class="flex flex-col sm:flex-row sm:items-center justify-between p-4 rounded-3xl border transition-all duration-300 group gap-4"
                :class="item.inStock ? 'bg-gray-50/50 hover:bg-white hover:shadow-lg hover:border-primary/30 border-gray-100' : 'bg-gray-50/30 border-gray-100 opacity-75 grayscale-[0.2]'"
              >
                
                <div class="flex items-center gap-4 overflow-hidden">
                  <div class="w-16 h-16 bg-white shadow-sm rounded-2xl flex items-center justify-center text-3xl shrink-0 group-hover:scale-105 group-hover:shadow transition-all duration-300">
                    {{ item.emoji || '🥩' }}
                  </div>
                  <div class="truncate">
                    <div class="flex items-center gap-2 mb-0.5">
                      <h4 class="font-bold text-lg truncate" :class="item.inStock ? 'text-gray-900 group-hover:text-primary transition-colors' : 'text-gray-500'">
                        {{ item.name }}
                      </h4>
                      <span v-if="!item.inStock" class="text-[9px] uppercase tracking-wider font-extrabold bg-red-50 text-red-500 px-2 py-0.5 rounded-md border border-red-100 shrink-0">Sold Out</span>
                      <span v-else-if="item.category === 'Fish & Seafood'" class="text-[9px] uppercase tracking-wider font-extrabold bg-blue-50 text-blue-500 px-2 py-0.5 rounded-md border border-blue-100 shrink-0 hidden sm:inline-block">Fresh Catch</span>
                    </div>
                    
                    <p class="text-sm text-gray-500 flex items-center gap-1.5 truncate mb-1">
                      <StoreIcon class="w-3.5 h-3.5 shrink-0" />
                      {{ item.vendorId ? item.vendorId.shopName : 'Local Butcher' }}
                    </p>
                    <p class="text-base font-extrabold" :class="item.inStock ? 'text-primary' : 'text-gray-400'">
                      Est. ₹{{ item.price }} <span class="text-xs font-medium text-gray-400">/ {{ item.unit }}</span>
                    </p>
                  </div>
                </div>

                <button 
                  @click="item.inStock ? reserveItem(item) : null"
                  :disabled="!item.inStock"
                  class="w-full sm:w-auto px-6 py-3 rounded-2xl font-bold text-sm transition-all duration-300 shrink-0 flex items-center justify-center gap-2 shadow-sm"
                  :class="item.inStock ? ' text-primary hover:bg-primary hover:text-white hover:shadow-md active:scale-95' : 'bg-gray-100 text-gray-400 cursor-not-allowed'"
                >
                  Order Now
                </button>

              </div>
            </div>
            
            <button v-if="items.length > 6" class="w-full mt-4 py-3 text-sm font-bold text-primary hover:bg-secondary/10 rounded-xl transition-colors">
              View All {{ categoryName }} &rarr;
            </button>

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
import { SearchIcon, MapPinIcon, StoreIcon, Loader2Icon, XIcon } from 'lucide-vue-next'

const searchQuery = ref('')
const isModalOpen = ref(false)
const allItems = ref([])

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
      alert(response.data.message);
    }
  } catch (error) {
    alert(error.response?.data?.error || "Failed to reserve item.");
  }
}
</script>