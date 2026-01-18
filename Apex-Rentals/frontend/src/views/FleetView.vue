<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cars = ref([])
// CORRECT URL: No extra slash at the end
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/api/cars/`)
    cars.value = response.data
  } catch (err) { console.error(err) }
})
// Add this helper function to define colors
const getTagStyle = (tag) => {
  if (!tag) return 'bg-gray-500/10 text-gray-400 border-gray-500/20' // Fallback
  
  const t = tag.toLowerCase()
  
  if (t === 'economy') return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30 shadow-[0_0_10px_-3px_rgba(52,211,153,0.3)]'
  if (t === 'premium') return 'bg-amber-500/10 text-amber-300 border-amber-500/30 shadow-[0_0_15px_-3px_rgba(245,158,11,0.3)]'
  if (t === 'sports') return 'bg-rose-600/10 text-rose-500 border-rose-500/30 shadow-[0_0_15px_-3px_rgba(225,29,72,0.4)]'
  if (t === 'classic') return 'bg-slate-400/10 text-slate-300 border-slate-400/30 shadow-[0_0_10px_-3px_rgba(148,163,184,0.3)]'
  if (t === 'vintage') return 'bg-orange-900/20 text-[#DEB887] border-[#DEB887]/30 shadow-[0_0_10px_-3px_rgba(222,184,135,0.3)]'
  
  return 'bg-[#5F9598]/10 text-[#5F9598] border-[#5F9598]/30' // Default Teal
}

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400?text=No+Image"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div class="bg-[#061E29] min-h-screen pt-32 pb-24 px-6 relative overflow-hidden">
    
    <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-[#1D546D]/20 blur-[120px] rounded-full pointer-events-none"></div>

    <div class="max-w-[1920px] mx-auto relative z-10">
      
      <div class="text-center mb-20 animate-fade-in-up">
        <h1 class="text-5xl md:text-7xl font-bold text-white mb-4 tracking-tighter">
          THE <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#5F9598] to-white">COLLECTION</span>
        </h1>
        <p class="text-gray-400 uppercase tracking-[0.3em] text-sm">
          Choose your weapon
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        
        <div 
          v-for="(car, index) in cars" 
          :key="car.id" 
          class="group relative bg-[#0B2B38]/60 backdrop-blur-md border border-white/5 rounded-2xl overflow-hidden hover:-translate-y-2 transition-all duration-500 hover:shadow-[0_20px_50px_-12px_rgba(95,149,152,0.2)]"
          :style="{ animation: `fadeInUp 0.8s ease-out ${index * 0.1}s backwards` }"
        >
          <div class="absolute inset-0 border-2 border-transparent group-hover:border-[#5F9598]/30 rounded-2xl transition-colors duration-500 pointer-events-none z-20"></div>

          <div class="h-64 overflow-hidden relative">
            <div class="absolute inset-0 bg-black/40 group-hover:bg-transparent transition-all duration-500 z-10"></div>
            
            <img 
              :src="getImageUrl(car.image)" 
              :alt="car.model" 
              class="w-full h-full object-cover transform group-hover:scale-110 transition duration-700 ease-in-out"
            />
            
            <div class="absolute bottom-4 right-4 z-20 bg-black/70 backdrop-blur-md px-4 py-2 rounded-lg border border-white/10">
              <span class="text-[#5F9598] font-bold">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
              <span class="text-xs text-gray-400"> / day</span>
            </div>
          </div>

          <div class="p-6">
            <div class="flex justify-between items-start mb-4">
              <div>
                <p class="text-[#5F9598] text-[10px] font-bold tracking-[0.2em] uppercase mb-1">{{ car.manufacturer }}</p>
                <h3 class="text-2xl font-bold text-white leading-tight group-hover:text-[#5F9598] transition-colors">{{ car.model }}</h3>
              </div>
              
              <div 
                v-if="car.tag"
                class="px-3 py-1 rounded-full text-[10px] font-bold uppercase tracking-wider border backdrop-blur-sm transition-all duration-300 group-hover:scale-105"
                :class="getTagStyle(car.tag)"
              >
                {{ car.tag }}
              </div>
            </div>

            <div class="flex gap-4 mb-6 border-t border-white/5 pt-4 text-gray-400 text-sm">
              <div class="flex items-center gap-1"><ion-icon name="hardware-chip-outline" class="text-[#5F9598]"></ion-icon> {{ car.transmission }}</div>
              <div class="flex items-center gap-1"><ion-icon name="water-outline" class="text-[#5F9598]"></ion-icon> {{ car.fuel_type }}</div>
              
            </div>

            <router-link 
              :to="{ name: 'details', params: { id: car.id } }"
              class="block w-full text-center py-3 bg-white/5 hover:bg-[#5F9598] hover:text-[#061E29] text-white text-sm font-bold uppercase tracking-widest rounded-lg transition-all duration-300"
            >
              Reserve Now
            </router-link>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
/* Only applying this specific keyframe here to avoid conflicts */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>