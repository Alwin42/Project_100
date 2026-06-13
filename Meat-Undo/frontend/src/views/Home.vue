<template>
  <div class="min-h-screen bg-white font-sans pb-20">
    
    <Navbar @open-login="isModalOpen = true" />

    <div class="border-b border-gray-100 py-2 mt-26 flex justify-center items-center gap-1.5 text-xs font-bold text-gray-500">
      <MapPinIcon class="w-3.5 h-3.5 text-primary" /> 
      <span>Delivering to:</span>
      <span 
        @click="isLocationModalOpen = true" 
        class="text-gray-900 underline decoration-gray-300 underline-offset-2 cursor-pointer hover:text-primary transition-colors"
      >
        {{ selectedLocation }}
      </span>
    </div>

    <LocationModal 
      :isOpen="isLocationModalOpen" 
      @close="isLocationModalOpen = false" 
      @location-selected="updateLocation" 
    />

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
          <div class="flex items-center bg-white rounded-full h-14 shadow-sm border border-gray-200 focus-within:border-primary focus-within:ring-2 focus-within:ring-primary/10 px-5 transition-all group">
            <span class="text-gray-400 mr-3 text-xl group-focus-within:text-primary transition-colors">🔍</span>
            <input 
              v-model="searchQuery"
              type="text" 
              placeholder="Search items or categories..." 
              class="w-full h-full outline-none bg-transparent font-medium text-gray-800 placeholder-gray-400 text-sm"
            />
          </div>
        </div>
      </div>

      <div v-if="Object.keys(groupedItems).length === 0" class="text-center py-16 border border-dashed border-gray-200 rounded-3xl bg-gray-50">
        <span class="text-4xl block mb-3">📦</span>
        <h3 class="text-base font-bold text-gray-900">No matching items in stock</h3>
        <p class="text-gray-400 text-xs mt-1">Try adjusting your keywords or category filter.</p>
      </div>

      <div v-else class="space-y-12">
        <div v-for="(items, category) in groupedItems" :key="category" class="animate-in fade-in slide-in-from-bottom-3 duration-500">
          <h2 class="text-xs font-black text-gray-400 tracking-widest uppercase mb-6 flex items-center gap-2">
            <span>🔹</span> {{ category }}
          </h2>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div 
              v-for="item in items" 
              :key="item._id"
              class="bg-white border border-gray-100 rounded-3xl p-5 shadow-xs hover:shadow-lg hover:border-gray-200/80 transition-all duration-300 flex flex-col group relative"
            >
              <span 
                class="absolute top-4 right-4 text-[10px] font-black uppercase tracking-wider px-2.5 py-1 rounded-full z-10 shadow-xs"
                :class="item.inStock ? 'bg-green-50 text-green-600 border border-green-100' : 'bg-red-50 text-red-500 border border-red-100'"
              >
                {{ item.inStock ? 'In Stock' : 'Out of Stock' }}
              </span>

              <div class="flex gap-4 items-start grow">
                <div class="w-16 h-16 rounded-2xl bg-gray-50 flex items-center justify-center text-3xl border border-gray-100 shrink-0 shadow-inner group-hover:scale-105 transition-transform duration-300">
                  {{ item.emoji || '🥩' }}
                </div>
                <div class="space-y-1">
                  <h4 class="font-bold text-gray-900 text-base leading-tight group-hover:text-primary transition-colors">
                    {{ item.name }}
                  </h4>
                  <p class="text-xs text-gray-400 font-medium line-clamp-2 leading-relaxed">
                    {{ item.description || 'Fresh quality stock from vendor.' }}
                  </p>
                  <p class="text-xs font-bold text-gray-500 flex items-center gap-1 pt-1">
                    <span>🏪</span> <span class="underline decoration-gray-200">{{ item.shopName || 'Local Vendor' }}</span>
                  </p>
                </div>
              </div>

              <div class="mt-6 pt-4 border-t border-gray-50 flex items-center justify-between gap-4">
                <div>
                  <span class="text-[10px] font-bold text-gray-400 block uppercase tracking-wider">Price / {{ item.unit || 'kg' }}</span>
                  <span class="text-lg font-black text-gray-900">₹{{ item.price }}</span>
                </div>

                <button 
                  @click="reserveItem(item)"
                  :disabled="!item.inStock"
                  class="bg-primary text-white font-bold text-xs px-5 h-10 rounded-full hover:bg-primary/90 hover:shadow-md disabled:bg-gray-100 disabled:text-gray-400 disabled:shadow-none transition-all active:scale-95"
                >
                  Reserve Now
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <LoginModal :isOpen="isModalOpen" @close="isModalOpen = false" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import LoginModal from '../components/LoginModal.vue'
import LocationModal from '../components/LocationModal.vue'
import { MapPinIcon } from 'lucide-vue-next'

// Configuration handling production API URLs dynamically
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3000'

const router = useRouter()
const isModalOpen = ref(false)
const isLocationModalOpen = ref(false)
const selectedLocation = ref('Select Location')
const searchQuery = ref('')
const allItems = ref([])

// Group and filter items dynamically matching query
const groupedItems = computed(() => {
  const groups = {}
  const query = searchQuery.value.toLowerCase().trim()
  
  const filteredItems = allItems.value.filter(item => {
    if (!query) return true
    
    const itemName = item.name ? item.name.toLowerCase() : ''
    const categoryName = item.category ? item.category.toLowerCase() : ''
    
    return itemName.includes(query) || categoryName.includes(query)
  })

  filteredItems.forEach(item => {
    const cat = item.category || 'Other'
    if (!groups[cat]) {
      groups[cat] = []
    }
    groups[cat].push(item)
  })
  
  return groups
})

onMounted(async () => {
  // Sync selected location from local storage cache
  const savedLocation = localStorage.getItem('deliveryLocation')
  if (savedLocation) {
    selectedLocation.value = savedLocation
  }

  // Load production/development inventory list
  try {
    const itemsResponse = await axios.get(`${API_BASE_URL}/api/public/items`)
    if (itemsResponse.data.success) {
      allItems.value = itemsResponse.data.items
    }
  } catch (error) {
    console.error("Failed to load home page data:", error)
  }
})

// Trigger location updates and sync to device memory
const updateLocation = (newLocation) => {
  selectedLocation.value = newLocation
  localStorage.setItem('deliveryLocation', newLocation)
}

// Reserve items with authorization token headers
const reserveItem = async (item) => {
  const token = localStorage.getItem('token')
  
  if (!token) {
    alert("Please log in to reserve items!")
    isModalOpen.value = true
    return
  }

  try {
    const response = await axios.post(`${API_BASE_URL}/api/orders/reserve`, 
      { productId: item._id },
      { headers: { Authorization: `Bearer ${token}` } }
    )
    
    if (response.data.success) {
      alert(`Successfully reserved: ${item.name}! Check your Orders tab for details.`)
    }
  } catch (error) {
    console.error("Reservation request failed:", error)
    alert(error.response?.data?.message || "Something went wrong while booking your item.")
  }
}
</script>