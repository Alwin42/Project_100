<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cars = ref([])
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/api/cars/`)
    cars.value = response.data
  } catch (err) { console.error(err) }
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400?text=No+Image"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div>
    <div class="relative bg-navy py-24 px-6 border-b border-white/5">
      <div class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-full bg-blue/20 blur-[120px] rounded-full pointer-events-none"></div>
      
      <div class="relative z-10 text-center max-w-4xl mx-auto">
        <h1 class="text-5xl md:text-7xl font-bold mb-6 tracking-tight">
          ELEVATE YOUR <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal to-blue">DRIVE</span>
        </h1>
        <p class="text-gray-400 text-lg md:text-xl mb-10 font-light">
          Experience the pinnacle of automotive engineering. 
          Reserved for those who demand excellence.
        </p>
      </div>
    </div>

    <div class="max-w-[1800px] mx-auto px-6 lg:px-12 py-20">
      <div class="flex items-end justify-between mb-12">
        <div>
          <h2 class="text-3xl font-bold">Exclusive Fleet</h2>
          <div class="h-1 w-20 bg-teal mt-4"></div>
        </div>
        <span class="text-gray-500 font-mono">{{ cars.length }} VEHICLES AVAILABLE</span>
      </div>

      <div class="grid grid-cols-1  md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <div 
          v-for="car in cars" 
          :key="car.id" 
          class="group bg-[#5F9598] rounded-xl hover:border-teal/50 transition-all duration-500"
        >
          <div class="relative h-64 overflow-hidden bg-black/50">
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover rounded-xl opacity-80 group-hover:opacity-100 group-hover:scale-105 transition duration-700"
            />
            <div class="absolute top-4 right-4">
              <span v-if="car.is_available" class="bg-teal/90 text-navy text-xs font-bold px-3 py-1 backdrop-blur-sm">
                AVAILABLE
              </span>
              <span v-else class="bg-red-500/90 text-white text-xs font-bold px-3 py-1 backdrop-blur-sm">
                RESERVED
              </span>
            </div>
          </div>

          <div class="p-6">
            <p class="text-teal text-xs font-bold tracking-widest uppercase mb-2">{{ car.make }}</p>
            <h3 class="text-2xl font-bold text-white mb-6">{{ car.model }}</h3>
            
            <div class="flex items-center justify-between border-t border-white/10 pt-6">
              <div>
                <p class="text-2xl font-bold text-white">₹{{ Number(car.price_per_day).toLocaleString() }}</p>
                <p class="text-xs text-gray-500 uppercase">Per Day</p>
              </div>
              <router-link 
                :to="{ name: 'details', params: { id: car.id } }"
                class="bg-[#061E29] hover:bg-[#1D546D] rounded-lg hover:text-navy text-white px-6 py-3 transition-colors duration-300 font-medium"
              >
                View Details
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>