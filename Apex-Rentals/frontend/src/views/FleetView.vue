<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cars = ref([])
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  try {
    // Now this becomes: http://127.0.0.1:8000/api/cars/
    const response = await axios.get(`${API_URL}/api/cars/`)
    cars.value = response.data
    console.log("Cars loaded:", cars.value) // Debugging: check console to be sure
  } catch (err) { 
    console.error("Error loading cars:", err) 
  }
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400?text=No+Image"
  if (imagePath.startsWith("http")) return imagePath
  // Now this correctly creates: http://127.0.0.1:8000/media/car.jpg
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div id="fleet" class="bg-[#061E29] min-h-screen py-24 px-6 lg:px-16 pt-32">
    <div class="max-w-[1920px] mx-auto">
      
      <div class="flex items-end justify-between mb-16 border-b border-white/10 pb-6">
        <h2 class="text-4xl font-bold text-white">The Collection</h2>
        <span class="text-[#5F9598] font-mono">AVAILABLE MODELS</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10">
        <div 
          v-for="car in cars" 
          :key="car.id" 
          class="group bg-[#0B2B38] border border-white/5 hover:border-[#5F9598]/50 transition-all duration-500 relative"
        >
          <div class="h-72 overflow-hidden relative">
            <div class="absolute inset-0 bg-black/20 group-hover:bg-transparent transition-colors duration-500 z-10"></div>
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform group-hover:scale-110 transition duration-700 ease-in-out"
            />
          </div>

          <div class="p-8">
            <h3 class="text-3xl font-bold text-white mb-2">{{ car.model }}</h3>
            <p class="text-[#5F9598] text-xs font-bold tracking-[0.2em] uppercase mb-8">{{ car.make }}</p>
            
            <div class="flex items-center justify-between border-t border-white/10 pt-6">
              <div>
                <span class="text-2xl font-bold text-white">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
                <span class="text-gray-500 text-sm ml-1">/DAY</span>
              </div>
              
              <router-link 
                :to="{ name: 'details', params: { id: car.id } }"
                class="text-white hover:text-[#5F9598] transition-colors uppercase tracking-wider text-sm font-medium"
              >
                Reserve &rarr;
              </router-link>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>