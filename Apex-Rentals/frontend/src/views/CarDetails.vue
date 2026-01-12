<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const car = ref(null)
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  const carId = route.params.id
  try {
    const response = await axios.get(`${API_URL}/api/cars/${carId}/`)
    car.value = response.data
  } catch (err) { console.error(err) }
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/800x600"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div v-if="car" class="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-12 py-12">
    
    <router-link to="/" class="inline-flex items-center text-apex-teal hover:text-apex-navy mb-8 font-bold tracking-wide transition">
      ← BACK TO FLEET
    </router-link>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      
      <div class="relative group">
        <div class="absolute -inset-2 bg-gradient-to-r from-apex-teal to-apex-blue rounded-lg opacity-30 group-hover:opacity-50 transition duration-500 blur"></div>
        <img :src="getImageUrl(car.image)" :alt="car.model" class="relative w-full rounded shadow-xl border border-gray-200" />
      </div>

      <div class="bg-gray-600 rounded-xl p-8 md:p-12 shadow-sm border-t-4 ">
        <span class="text-white font-bold tracking-[0.2em] text-sm uppercase">{{ car.make }} COLLECTION</span>
        <h1 class="text-5xl font-extrabold text-white mt-2 mb-6">{{ car.model }}</h1>
        
        <p class="text-white leading-relaxed mb-8 border-l-4 border-gray-200 pl-4 italic">
          "The {{ car.year }} {{ car.model }} combines engineering excellence with daily practicality. 
          Perfect for the roads of Kerala."
        </p>

        <div class="flex items-baseline mb-8">
          <span class="text-4xl font-bold text-gray-200">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
          <span class="text-gray-200 ml-2">per day</span>
        </div>

        <button 
          :disabled="!car.is_available"
          class="w-full py-4 text-white font-bold text-lg uppercase tracking-widest transition transform hover:-translate-y-1"
          :class="car.is_available 
            ? 'bg-[#061E29] rounded-xl hover:bg-[#5F9598] shadow-lg shadow-blue-900/20' 
            : 'bg-gray-300 text-gray-500 cursor-not-allowed'"
        >
          {{ car.is_available ? 'Confirm Booking' : 'Currently Unavailable' }}
        </button>

        <div class="grid rounded-lg grid-cols-2 gap-4 mt-8 text-sm text-gray-200 font-semibold">
          <div class="flex items-center gap-2">✅ Instant Confirmation</div>
          <div class="flex items-center gap-2">✅ Insurance Included</div>
          <div class="flex items-center gap-2">✅ GPS Navigation</div>
          <div class="flex items-center gap-2">✅ 24/7 Support</div>
        </div>
      </div>
    </div>
  </div>
</template>