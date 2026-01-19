<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const API_URL = "http://127.0.0.1:8000"

const car = ref(null)
const loading = ref(true)
const processing = ref(false)
const success = ref(false)

// Mock Payment Details
const cardName = ref('')
const cardNumber = ref('')
const expiry = ref('')
const cvv = ref('')

onMounted(async () => {
  try {
    const carRes = await axios.get(`${API_URL}/api/cars/${route.params.id}/`)
    car.value = carRes.data
  } catch (err) {
    console.error("Error loading car", err)
  } finally {
    loading.value = false
  }
})

const handlePayment = () => {
  processing.value = true
  
  // Simulate API delay
  setTimeout(() => {
    processing.value = false
    success.value = true
    
    // Redirect to Dashboard after 2 seconds
    setTimeout(() => {
      router.push('/dashboard')
    }, 2000)
  }, 2000)
}
</script>

<template>
  <div class="min-h-screen bg-[#061E29] flex items-center justify-center p-4 relative overflow-hidden">
    <div class="absolute top-0 left-0 w-[500px] h-[500px] bg-[#5F9598]/10 blur-[120px] rounded-full pointer-events-none"></div>

    <div v-if="success" class="bg-[#0B2B38] p-10 rounded-2xl border border-green-500/30 text-center animate-bounce-in shadow-2xl z-10">
      <div class="w-20 h-20 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-4 text-green-400 text-4xl">
        <ion-icon name="checkmark"></ion-icon>
      </div>
      <h2 class="text-2xl font-bold text-white mb-2">Payment Successful!</h2>
      <p class="text-gray-400">Your ride is reserved. Redirecting...</p>
    </div>

    <div v-else-if="car" class="max-w-4xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 z-10">
      
      <div class="bg-[#0B2B38]/60 backdrop-blur-md p-8 rounded-2xl border border-white/5 h-fit">
        <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Order Summary</h2>
        <img :src="car.image" class="w-full h-48 object-cover rounded-lg mb-6 border border-white/10" />
        <h3 class="text-2xl font-bold text-white">{{ car.model }}</h3>
        <p class="text-gray-400 text-sm mb-6">{{ car.manufacturer }} Series</p>
        
        <div class="flex justify-between items-center border-t border-white/10 pt-4">
          <span class="text-gray-300">Total to pay</span>
          <span class="text-2xl font-bold text-[#5F9598]">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
        </div>
      </div>

      <div class="bg-[#0B2B38] p-8 rounded-2xl border border-white/5 shadow-2xl">
        <h2 class="text-white font-bold text-xl mb-6 flex items-center gap-2">
          <ion-icon name="card-outline"></ion-icon> Secure Payment
        </h2>

        <form @submit.prevent="handlePayment" class="space-y-4">
          <div>
            <label class="block text-xs text-gray-400 uppercase tracking-wider mb-2">Cardholder Name</label>
            <input v-model="cardName" required type="text" class="w-full bg-[#061E29] border border-white/10 rounded-lg p-3 text-white focus:border-[#5F9598] outline-none transition" placeholder="John Doe">
          </div>
          
          <div>
            <label class="block text-xs text-gray-400 uppercase tracking-wider mb-2">Card Number</label>
            <input v-model="cardNumber" required type="text" maxlength="16" class="w-full bg-[#061E29] border border-white/10 rounded-lg p-3 text-white focus:border-[#5F9598] outline-none transition" placeholder="0000 0000 0000 0000">
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-xs text-gray-400 uppercase tracking-wider mb-2">Expiry</label>
              <input v-model="expiry" required type="text" placeholder="MM/YY" class="w-full bg-[#061E29] border border-white/10 rounded-lg p-3 text-white focus:border-[#5F9598] outline-none transition">
            </div>
            <div>
              <label class="block text-xs text-gray-400 uppercase tracking-wider mb-2">CVV</label>
              <input v-model="cvv" required type="password" maxlength="3" placeholder="123" class="w-full bg-[#061E29] border border-white/10 rounded-lg p-3 text-white focus:border-[#5F9598] outline-none transition">
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="processing"
            class="w-full bg-[#5F9598] hover:bg-white text-[#061E29] font-bold py-4 rounded-xl mt-4 transition-all duration-300 flex items-center justify-center gap-2"
          >
            <span v-if="processing" class="animate-spin h-5 w-5 border-2 border-[#061E29] border-t-transparent rounded-full"></span>
            {{ processing ? 'Processing...' : 'Pay Now' }}
          </button>
        </form>
      </div>

    </div>
  </div>
</template>