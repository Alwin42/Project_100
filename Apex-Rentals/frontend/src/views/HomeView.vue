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
  if (!imagePath) return "https://via.placeholder.com/600x400"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div>
    <div class="bg-[#1D546D] text-white py-24 px-4 text-center">
      <h1 class="text-4xl md:text-6xl font-bold mb-6 tracking-tight">
        Drive the <span class="text-apex-teal">Extraordinary</span>
      </h1>
      <p class="text-gray-300 mb-10 text-lg max-w-2xl mx-auto font-light">
        Experience premium travel with our exclusive fleet. 
        Unmatched comfort at unbeatable daily rates.
      </p>
      <button class="border-2 border-apex-teal text-apex-teal hover:bg-apex-teal hover:text-white px-10 py-3 rounded-xl font-bold tracking-widest transition duration-300 uppercase text-sm">
        Explore Fleet
      </button>
    </div>

    <div class="w-full max-w-[1800px] mx-auto px-4 sm:px-6 lg:px-12 py-16">
      
      <div class="flex items-center justify-between mb-10 border-b border-gray-300 pb-4">
        <h2 class="text-3xl font-bold text-apex-navy">Available Vehicles</h2>
        <span class="text-apex-blue font-semibold">{{ cars.length }} Cars Ready</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        
        <div 
          v-for="car in cars" 
          :key="car.id" 
          class="bg-white group hover:shadow-2xl transition-all duration-500 border-b-4 border-transparent hover:border-apex-teal flex flex-col"
        >
          <div class="h-64 overflow-hidden relative bg-gray-200">
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform group-hover:scale-110 transition duration-700"
            />
            <div class="absolute top-4 left-4">
              <span v-if="car.is_available" class="bg-apex-teal text-white text-xs font-bold px-3 py-1 uppercase tracking-wider shadow-md">
                Available
              </span>
              <span v-else class="bg-apex-navy text-white text-xs font-bold px-3 py-1 uppercase tracking-wider shadow-md">
                Booked
              </span>
            </div>
          </div>

          <div class="p-6 flex-1 flex flex-col">
            <div class="mb-4">
              <p class="text-xs text-apex-teal font-bold uppercase tracking-widest mb-1">{{ car.make }}</p>
              <h3 class="text-2xl font-bold text-apex-navy">{{ car.model }}</h3>
            </div>
            
            <div class="flex items-center gap-4 text-gray-500 text-sm mb-6">
              <span>{{ car.year }}</span>
              <span>•</span>
              <span>Automatic</span>
              <span>•</span>
              <span>Petrol</span>
            </div>

            <div class="mt-auto flex items-center justify-between pt-4 border-t border-gray-100">
              <div>
                <span class="text-xl font-bold text-apex-navy">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
                <span class="text-xs text-gray-400">/day</span>
              </div>
              
              <router-link 
                :to="{ name: 'details', params: { id: car.id } }"
                class="bg-[#061E29] text-white hover:bg-[#1D546D] rounded-lg px-6 py-2 text-sm font-bold uppercase tracking-wider transition duration-300">
                Rent
              </router-link>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>