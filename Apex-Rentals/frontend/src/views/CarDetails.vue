<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const API_URL = "http://127.0.0.1:8000"

// --- STATE ---
const car = ref(null)
const loading = ref(true)
const isVerified = ref(false)
const hasUploadedID = ref(false)
const userId = localStorage.getItem('user_id')

// --- MODAL STATE ---
const showModal = ref(false)
const modalConfig = ref({ 
  title: '', 
  message: '', 
  type: 'info', 
  action: null 
})

// Helper to Open Modal
const openModal = (title, message, type = 'info', action = null) => {
  modalConfig.value = { title, message, type, action }
  showModal.value = true
}

// 1. Fetch Data
onMounted(async () => {
  const carId = route.params.id

  // A. Fetch Car (Public)
  try {
    const carRes = await axios.get(`${API_URL}/api/cars/${carId}/`)
    car.value = carRes.data
  } catch (err) {
    console.error("Failed to load car", err)
  }

  // B. Check Status (Private)
  if (userId) {
    try {
      const token = localStorage.getItem('token')
      const statusRes = await axios.get(`${API_URL}/api/user/status/`, {
        headers: { 'Authorization': `Token ${token}` }
      })
      isVerified.value = statusRes.data.is_verified
      hasUploadedID.value = statusRes.data.has_uploaded_id
    } catch (e) {
      console.warn("User status check failed", e)
    }
  }

  setTimeout(() => loading.value = false, 300)
})

// 2. Handle Rent Logic
const handleRentClick = () => {
  if (!userId) {
    openModal("Login Required", "You must be logged in to reserve a vehicle.", "confirm", () => router.push('/login'))
    return
  }
  if (!hasUploadedID) {
    openModal("ID Proof Missing", "You must upload your ID proof in the Dashboard before renting.", "error", () => router.push('/dashboard'))
    return
  }
  if (!isVerified.value) {
    openModal("Verification Pending", "Your ID is currently under review by our Admin team.", "info")
    return
  }

  openModal(
    "Confirm Reservation", 
    `Are you sure you want to proceed with booking the ${car.value.model} for ₹${car.value.price_per_day}/day?`, 
    "confirm",
    () => {
      router.push({ name: 'payment', params: { id: car.value.id } })
    }
  )
}

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400?text=No+Image"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div class="min-h-screen bg-[#061E29] pt-32 pb-20 relative overflow-hidden">
    
    <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-[#1D546D]/20 blur-[120px] rounded-full pointer-events-none"></div>

    <div v-if="loading" class="flex justify-center items-center h-[60vh]">
      <div class="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-[#5F9598]"></div>
    </div>

    <div v-else-if="car" class="max-w-7xl mx-auto px-6 relative z-10">
      
      <button @click="router.back()" class="flex items-center gap-2 text-gray-400 hover:text-white mb-8 transition-colors group">
        <ion-icon name="arrow-back" class="group-hover:-translate-x-1 transition-transform"></ion-icon>
        Back to Fleet
      </button>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
        
        <div class="lg:col-span-2 relative group rounded-2xl overflow-hidden border border-white/10 shadow-2xl h-[500px] lg:h-[600px]">
          <div class="absolute inset-0 bg-gradient-to-t from-[#061E29] via-transparent to-transparent opacity-60 z-10"></div>
          
          <img 
            :src="getImageUrl(car.image)" 
            :alt="car.model" 
            class="w-full h-full object-cover transform group-hover:scale-105 transition duration-700"
          >
          
          <div class="absolute bottom-6 left-6 z-20">
            <div class="inline-block px-4 py-1 bg-[#5F9598] text-[#061E29] font-bold text-xs uppercase tracking-widest rounded-full mb-2">
              {{ car.tag || 'Premium' }}
            </div>
            <h1 class="text-4xl md:text-5xl font-bold text-white">{{ car.model }}</h1>
          </div>
        </div>

        <div class="bg-[#0B2B38]/60 backdrop-blur-md p-8 rounded-2xl border border-white/5 shadow-xl h-full">
          
          <div class="flex justify-between items-end border-b border-white/10 pb-6 mb-8">
            <div>
              <p class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-1">{{ car.manufacturer }}</p>
              <h2 class="text-2xl font-bold text-white">Overview</h2>
            </div>
            <div class="text-right">
              <p class="text-2xl font-bold text-[#5F9598]">₹{{ Number(car.price_per_day).toLocaleString() }}</p>
              <p class="text-gray-400 text-sm">per day</p>
            </div>
          </div>

          <div class="grid grid-cols-3 gap-4 mb-10">
            
            <div class="bg-[#061E29] p-2 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="speedometer-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Transmission</p>
              <p class="text-white font-bold text-sm">{{ car.transmission }}</p>
            </div>
            
            <div class="bg-[#061E29] p-4 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="water-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Fuel</p>
              <p class="text-white font-bold text-sm">{{ car.fuel_type }}</p>
            </div>

            <div class="bg-[#061E29] p-4 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="calendar-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Year</p>
              <p class="text-white font-bold text-sm">{{ car.year || '2024' }}</p>
            </div>

            <div class="bg-[#061E29] p-4 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="color-palette-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Color</p>
              <p class="text-white font-bold text-sm">{{ car.color || 'Black' }}</p>
            </div>

             <div class="bg-[#061E29] p-4 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="person-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Owner</p>
              <p class="text-white font-bold text-sm">{{ car.owner_name || 'Apex' }}</p>
            </div>

            <div class="bg-[#061E29] p-4 rounded-xl border border-white/5 flex flex-col items-center text-center">
              <ion-icon name="call-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Contact</p>
              <p class="text-white font-bold text-sm">{{ car.owner_phone || 'N/A' }}</p>
            </div>

            <div class="bg-[#061E29] p-6 rounded-xl border border-white/5 flex flex-col items-center text-center col-span-2">
              <ion-icon name="location-outline" class="text-2xl text-[#5F9598] mb-2"></ion-icon>
              <p class="text-gray-400 text-xs uppercase">Location</p>
              <p class="text-white font-bold text-sm">{{ car.location || 'Kochi, Kerala' }}</p>
            </div>

          </div>

          <button 
            @click="handleRentClick"
            :disabled="!car.is_available"
            class="w-full py-4 font-bold text-sm uppercase tracking-[0.2em] rounded-xl transition-all duration-300 transform hover:-translate-y-1 relative overflow-hidden group/btn mb-6"
            :class="[
               !car.is_available 
                 ? 'bg-gray-700 text-gray-500 cursor-not-allowed' 
                 : isVerified 
                    ? 'bg-[#5F9598] hover:bg-white text-[#061E29] shadow-[0_10px_40px_-10px_rgba(95,149,152,0.5)]' 
                    : 'bg-amber-600/10 text-amber-500 border border-amber-600/30 hover:bg-amber-600/20'
            ]"
          >
            <span class="relative z-10">
              {{ !car.is_available ? 'Currently Unavailable' : (isVerified ? 'Confirm Reservation' : 'Verify ID to Rent') }}
            </span>
          </button>
          
          <p v-if="!isVerified && userId" class="text-center text-xs text-amber-500/80">
            * Complete ID verification in Dashboard to unlock booking.
          </p>

        </div>
      </div>
    </div>

    <div v-else class="text-center pt-20">
      <h2 class="text-2xl text-white">Car not found</h2>
      <button @click="router.push('/fleet')" class="text-[#5F9598] mt-4 hover:underline">Go back to fleet</button>
    </div>

    <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-black/80 backdrop-blur-sm transition-opacity" @click="showModal = false"></div>
      
      <div class="relative bg-[#0B2B38] border border-white/10 p-8 rounded-2xl max-w-md w-full shadow-2xl animate-fade-in-up">
        
        <div class="mb-4 text-4xl">
           <ion-icon v-if="modalConfig.type === 'error'" name="warning" class="text-red-400"></ion-icon>
           <ion-icon v-if="modalConfig.type === 'info'" name="information-circle" class="text-amber-400"></ion-icon>
           <ion-icon v-if="modalConfig.type === 'confirm'" name="calendar" class="text-[#5F9598]"></ion-icon>
        </div>

        <h3 class="text-2xl font-bold text-white mb-2">{{ modalConfig.title }}</h3>
        <p class="text-gray-400 mb-8">{{ modalConfig.message }}</p>

        <div class="flex gap-4">
          <button @click="showModal = false" class="flex-1 py-3 rounded-lg font-bold border border-white/10 text-gray-400 hover:bg-white/5 transition">Cancel</button>
          
          <button v-if="modalConfig.action" @click="modalConfig.action" class="flex-1 py-3 rounded-lg font-bold bg-[#5F9598] text-[#061E29] hover:bg-white transition">
            {{ modalConfig.type === 'confirm' ? 'Continue' : 'Proceed' }}
          </button>
          
          <button v-else @click="showModal = false" class="flex-1 py-3 rounded-lg font-bold bg-[#5F9598] text-[#061E29] hover:bg-white transition">Okay</button>
        </div>

      </div>
    </div>

  </div>
</template>

<style scoped>
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.animate-fade-in-up { animation: fadeInUp 0.3s ease-out forwards; }
</style>