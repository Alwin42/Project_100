<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const car = ref(null)
const loading = ref(true)
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  const carId = route.params.id
  // Add a small delay for the animation to feel smooth
  setTimeout(async () => {
    try {
      const response = await axios.get(`${API_URL}/api/cars/${carId}/`)
      car.value = response.data
    } catch (err) { 
      console.error(err) 
    } finally {
      loading.value = false
    }
  }, 300)
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/800x600"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div class="min-h-screen w-full bg-[#061E29] pt-32 pb-20 px-4 sm:px-6 lg:px-12 relative overflow-hidden">
    
    <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-[#1D546D]/20 blur-[150px] rounded-full pointer-events-none animate-pulse-slow"></div>
    <div class="absolute bottom-0 left-0 w-[400px] h-[400px] bg-[#5F9598]/10 blur-[150px] rounded-full pointer-events-none"></div>

    <div v-if="loading" class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12 items-center animate-pulse">
      <div class="h-[400px] bg-[#0B2B38]/50 rounded-xl"></div>
      <div class="space-y-4">
        <div class="h-10 w-1/2 bg-[#0B2B38]/50 rounded"></div>
        <div class="h-40 w-full bg-[#0B2B38]/50 rounded"></div>
      </div>
    </div>

    <div v-else-if="car" class="relative z-10 max-w-7xl mx-auto animate-fade-in-up">
      
      <router-link to="/fleet" class="inline-flex items-center text-[#5F9598] hover:text-white mb-8 font-bold tracking-widest uppercase text-xs transition-colors duration-300">
        <span class="mr-2">←</span> Back to Collection
      </router-link>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
        
        <div class="relative group perspective-1000">
          <div class="absolute -inset-1 bg-gradient-to-r from-[#5F9598] to-[#1D546D] rounded-xl opacity-30 group-hover:opacity-60 blur-lg transition duration-700"></div>
          
          <div class="relative rounded-xl overflow-hidden border border-white/10 shadow-2xl">
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform transition duration-700 group-hover:scale-105" 
            />
            
            <div class="absolute top-6 left-6 bg-[#061E29]/90 backdrop-blur border border-[#5F9598]/30 px-4 py-2 rounded-lg">
              <span class="text-[#5F9598] font-bold tracking-widest text-xs uppercase">{{ car.make }} Series</span>
            </div>
          </div>
        </div>

        <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 md:p-12 shadow-2xl border border-white/5 relative overflow-hidden">
          
          <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#5F9598] to-transparent"></div>

          <span class="text-[#5F9598] font-bold tracking-[0.3em] text-xs uppercase mb-2 block">
            The {{ car.make }} Collection
          </span>
          
          <h1 class="text-4xl md:text-5xl font-extrabold text-white mb-6 leading-tight">
            {{ car.model }}
          </h1>
          
          <div class="border-l-2 border-[#5F9598] pl-6 mb-8">
            <p class="text-gray-300 italic text-lg leading-relaxed">
              "The {{ car.year }} {{ car.model }} combines engineering excellence with daily practicality. 
              Perfect for the roads of Kerala."
            </p>
          </div>

          <div class="flex items-baseline mb-10 pb-8 border-b border-white/10">
            <span class="text-5xl font-bold text-white">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
            <span class="text-gray-400 ml-3 text-lg font-light">/ per day</span>
          </div>

          <button 
            :disabled="!car.is_available"
            class="w-full py-5 text-[#061E29] font-bold text-lg uppercase tracking-[0.2em] rounded-xl transition-all duration-300 transform hover:-translate-y-1 hover:shadow-[0_10px_40px_-10px_rgba(95,149,152,0.5)] relative overflow-hidden group/btn"
            :class="car.is_available 
              ? 'bg-[#5F9598] hover:bg-white' 
              : 'bg-gray-700 text-gray-500 cursor-not-allowed'"
          >
            <span class="relative z-10">{{ car.is_available ? 'Confirm Reservation' : 'Currently Unavailable' }}</span>
          </button>

          <div class="grid grid-cols-2 gap-6 mt-10">
            <div class="flex items-center gap-3 text-gray-300 text-sm font-medium">
              <div class="w-8 h-8 rounded-full bg-[#061E29] flex items-center justify-center text-[#5F9598]">✓</div>
              Instant Confirmation
            </div>
            <div class="flex items-center gap-3 text-gray-300 text-sm font-medium">
              <div class="w-8 h-8 rounded-full bg-[#061E29] flex items-center justify-center text-[#5F9598]">✓</div>
              Full Insurance
            </div>
            <div class="flex items-center gap-3 text-gray-300 text-sm font-medium">
              <div class="w-8 h-8 rounded-full bg-[#061E29] flex items-center justify-center text-[#5F9598]">✓</div>
              GPS Navigation
            </div>
            <div class="flex items-center gap-3 text-gray-300 text-sm font-medium">
              <div class="w-8 h-8 rounded-full bg-[#061E29] flex items-center justify-center text-[#5F9598]">✓</div>
              24/7 Roadside Support
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes pulse-slow {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 0.6; transform: scale(1.1); }
}
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-pulse-slow { animation: pulse-slow 8s infinite ease-in-out; }
.animate-fade-in-up { animation: fade-in-up 0.8s ease-out forwards; }
</style>