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

    <div v-if="loading" class="max-w-[1600px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-center animate-pulse">
      <div class="lg:col-span-7 h-[600px] bg-[#0B2B38]/50 rounded-xl"></div>
      <div class="lg:col-span-5 space-y-4">
        <div class="h-10 w-1/2 bg-[#0B2B38]/50 rounded"></div>
        <div class="h-40 w-full bg-[#0B2B38]/50 rounded"></div>
      </div>
    </div>

    <div v-else-if="car" class="relative z-10 max-w-[1600px] mx-auto animate-fade-in-up">
      
      <router-link to="/fleet" class="inline-flex items-center text-[#5F9598] hover:text-white mb-8 font-bold tracking-widest uppercase text-xs transition-colors duration-300">
        <span class="mr-2">←</span> Back to Collection
      </router-link>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-start">
        
        <div class="lg:col-span-7 relative group perspective-1000">
          <div class="absolute -inset-1 bg-gradient-to-r from-[#5F9598] to-[#1D546D] rounded-xl opacity-30 group-hover:opacity-60 blur-lg transition duration-700"></div>
          
          <div class="relative rounded-xl overflow-hidden border border-white/10 shadow-2xl h-[400px] lg:h-[600px]">
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform transition duration-700 group-hover:scale-105" 
            />
            
            <div class="absolute top-6 left-6 bg-[#061E29]/90 backdrop-blur border border-[#5F9598]/30 px-4 py-2 rounded-lg">
              <span class="text-[#5F9598] font-bold tracking-widest text-xs uppercase">{{ car.model }} Series</span>
            </div>
            
          </div>
        </div>

        <div class="lg:col-span-5 bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 shadow-2xl border border-white/5 relative overflow-hidden">
          
          <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-[#5F9598] to-transparent"></div>

          <span class="text-[#5F9598] font-bold tracking-[0.3em] text-[10px] uppercase mb-1 block">
            The {{ car.manufacturer }} Collection
          </span>
          
          <h1 class="text-3xl md:text-5xl font-extrabold text-white mb-4 leading-tight">
            {{ car.model }}
          </h1>

          <div class="flex items-center gap-2 mb-6">
            <span class="px-3 py-1 bg-white/10 rounded text-xs font-bold text-gray-300 uppercase tracking-wider">{{ car.category }}</span>
            <span class="px-3 py-1 bg-white/10 rounded text-xs font-bold text-gray-300 uppercase tracking-wider">{{ car.year }}</span>
            <span class="px-3 py-1 bg-white/10 rounded text-xs font-bold text-gray-300 uppercase tracking-wider">{{ car.color }} Color</span>
            
          </div>
          
          <div class="grid grid-cols-2 gap-x-4 gap-y-4 mb-6 border-t border-b border-white/10 py-6">
            
            <div class="flex items-center gap-3">
              <div class="p-2 bg-[#061E29] rounded-lg text-[#5F9598] border border-white/5">
                <ion-icon name="water" style="font-size: 20px;"></ion-icon>
              </div>
              <div>
                <p class="text-[10px] text-gray-400 uppercase tracking-widest">Fuel Type</p>
                <p class="text-white font-bold text-sm leading-none">{{ car.fuel_type }}</p>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <div class="p-2 bg-[#061E29] rounded-lg text-[#5F9598] border border-white/5">
                <ion-icon name="hardware-chip" style="font-size: 20px;"></ion-icon>
              </div>
              <div>
                <p class="text-[10px] text-gray-400 uppercase tracking-widest">Transmission</p>
                <p class="text-white font-bold text-sm leading-none">{{ car.transmission }}</p>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <div class="p-2 bg-[#061E29] rounded-lg text-[#5F9598] border border-white/5">
                <ion-icon name="speedometer" style="font-size: 20px;"></ion-icon>
              </div>
              <div>
                <p class="text-[10px] text-gray-400 uppercase tracking-widest">Mileage</p>
                <p class="text-white font-bold text-sm leading-none">{{ car.mileage }} km/L</p>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <div class="p-2 bg-[#061E29] rounded-lg text-[#5F9598] border border-white/5">
                <ion-icon name="location" style="font-size: 20px;"></ion-icon>
              </div>
              <div>
                <p class="text-[10px] text-gray-400 uppercase tracking-widest">Location</p>
                <p class="text-white font-bold text-sm leading-tight  max-w-[140px]">{{ car.location }}</p>
              </div>
            </div>

          </div>

          <div class="flex items-baseline mb-4">
            <span class="text-4xl font-bold text-white">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
            <span class="text-gray-400 ml-2 text-sm font-light">/ day</span>
          </div>

          <button 
            :disabled="!car.is_available"
            class="w-full py-4 text-[#061E29] font-bold text-lg uppercase tracking-[0.2em] rounded-xl transition-all duration-300 transform hover:-translate-y-1 hover:shadow-[0_10px_40px_-10px_rgba(95,149,152,0.5)] relative overflow-hidden group/btn mb-6"
            :class="car.is_available 
              ? 'bg-[#5F9598] hover:bg-white' 
              : 'bg-gray-700 text-gray-500 cursor-not-allowed'"
          >
            <span class="relative z-10">{{ car.is_available ? 'Confirm Reservation' : 'Unavailable' }}</span>
          </button>

          <div class="bg-[#061E29]/30 rounded-lg p-3 flex items-center justify-between border border-white/5">
             <div class="flex items-center gap-3">
               <div class="w-8 h-8 rounded-full bg-gradient-to-br from-[#5F9598] to-[#1D546D] flex items-center justify-center text-white font-bold text-xs">
                 {{ car.owner_name ? car.owner_name.charAt(0) : 'A' }}
               </div>
               <div>
                 <p class="text-[10px] text-gray-400 uppercase">Listed By</p>
                 <p class="text-xs font-bold text-white">{{ car.owner_name }}</p>
               </div>
             </div>
             <a :href="`tel:${car.owner_phone}`" class="text-[#5F9598] hover:text-white transition-colors">
               <ion-icon name="call" style="font-size: 18px;"></ion-icon>
             </a>
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