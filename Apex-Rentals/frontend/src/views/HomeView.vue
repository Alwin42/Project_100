<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cars = ref([])
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/api/cars/`)
    cars.value = response.data
  } catch (err) {
    console.error(err)
  }
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div>
    <div class="text-white py-12 px-4 text-center">
      <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight mb-4">
        Find Your Perfect Drive
      </h1>
      <p class="text-gray-400 mb-6 max-w-xl mx-auto">
        Premium cars. Instant booking. Zero hassle.
      </p>
      <button class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-2.5 rounded-full font-bold transition">
        Browse Fleet
      </button>
    </div>

    <div class="w-full max-w-[1800px] mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      <h2 class="text-2xl font-bold text-gray-900 mb-6 px-2">Available Vehicles</h2>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        
        <div 
          v-for="car in cars" 
          :key="car.id" 
          class="bg-white rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 border border-gray-200 flex flex-col group"
        >
          <div class="h-52 overflow-hidden relative rounded-t-xl bg-gray-100">
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform group-hover:scale-105 transition duration-500"
            />
            <div v-if="!car.is_available" class="absolute inset-0 bg-black/50 flex items-center justify-center">
              <span class="bg-red-600 text-white text-xs font-bold px-2 py-1 rounded uppercase">Booked</span>
            </div>
          </div>

          <div class="p-4 flex-1 flex flex-col">
            <div class="flex justify-between items-start mb-2">
              <div>
                <p class="text-xs text-blue-600 font-bold uppercase">{{ car.make }}</p>
                <h3 class="text-lg font-bold text-gray-900">{{ car.model }}</h3>
              </div>
              <span class="text-xs font-semibold text-gray-500 border border-gray-300 px-1.5 py-0.5 rounded">
                {{ car.year }}
              </span>
            </div>
            
            <p class="text-gray-500 text-xs mb-4 line-clamp-2">
              Automatic • Petrol • 5 Seats
            </p>

            <div class="mt-auto pt-3 border-t border-gray-100 flex items-center justify-between">
              <p class="text-xl font-bold text-gray-900">₹{{ Number(car.price_per_day).toLocaleString() }}</p>
              
              <router-link 
                :to="{ name: 'details', params: { id: car.id } }"
                class="bg-gray-900 group-hover:bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition"
              >
                Rent
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>