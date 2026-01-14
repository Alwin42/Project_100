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

const scrollToFleet = () => {
  document.getElementById('fleet').scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <div>
    <div class="relative h-screen w-full overflow-hidden">
      
      <div 
        class="absolute inset-0 bg-cover bg-center bg-no-repeat"
        style="background-image: url('/hero-bg.jpg');"
      >
        <div class="absolute inset-0 bg-black/40"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-[#061E29] via-transparent to-transparent"></div>
      </div>

      <div class="absolute inset-0 flex flex-col items-center justify-center text-center px-4 pt-20">
        <h1 class="text-5xl md:text-8xl font-bold text-white mb-8 tracking-tighter opacity-0 animate-fade-in-up" style="animation-fill-mode: forwards;">
          DEFY <span class="text-[#5F9598]">ORDINARY</span>
        </h1>
        
        <p class="text-gray-200 text-lg md:text-xl max-w-xl mb-12 font-light tracking-wide opacity-0 animate-fade-in-up" style="animation-delay: 0.3s; animation-fill-mode: forwards;">
          Experience the thrill of the extraordinary.
        </p>

        <button 
          @click="scrollToFleet"
          class="group relative px-10 py-4 bg-transparent border border-white/30 text-white font-medium tracking-[0.2em] uppercase overflow-hidden hover:border-[#5F9598] transition-all duration-500 opacity-0 animate-fade-in-up"
          style="animation-delay: 0.6s; animation-fill-mode: forwards;"
        >
          <span class="absolute inset-0 w-full h-full bg-[#5F9598]/20 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-500 ease-out"></span>
          <span class="relative">Explore Fleet</span>
        </button>
      </div>
    </div>

    
  </div>
</template>

<style>
/* Custom Keyframes for this file only */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in-up {
  animation: fadeInUp 1s ease-out;
}
</style>