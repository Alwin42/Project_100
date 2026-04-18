<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-gray-900/40 backdrop-blur-sm px-4">
    
    <div class="bg-white w-full max-w-md rounded-3xl shadow-2xl p-8 relative transform transition-all">
      
      <button @click="$emit('close')" class="absolute top-4 right-4 text-gray-400 hover:text-gray-700">
        <XIcon class="w-6 h-6" />
      </button>

      <div class="text-center mb-8">
        <div class="mx-auto w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mb-4">
          <MailIcon class="w-6 h-6 text-green-600" /> 
        </div>
        <h3 class="text-2xl font-bold text-gray-900">Welcome to StockUndo</h3>
        <p class="text-gray-500 mt-2 text-sm">Log in or create an account instantly.</p>
      </div>

      <div v-if="step === 1">
        <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
        <div class="relative">
          <input 
            v-model="email" 
            type="email" 
            placeholder="you@example.com"
            class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition-all"
            @keyup.enter="isValidEmail ? requestOTP() : null"
          />
        </div>

        <button 
          @click="requestOTP"
          :disabled="!isValidEmail || isLoading"
          class="w-full mt-6 bg-green-600 text-white font-bold py-3.5 rounded-xl hover:bg-green-700 disabled:bg-green-300 transition-colors flex justify-center items-center gap-2"
        >
          <Loader2Icon v-if="isLoading" class="w-5 h-5 animate-spin" />
          <span v-else>Get OTP</span>
        </button>
      </div>

      <div v-if="step === 2">
        <p class="text-sm text-center text-gray-600 mb-6">
          We sent a 4-digit code to <br/><strong>{{ email }}</strong>. 
          <button @click="step = 1" class="text-green-600 font-medium hover:underline ml-1">Edit</button>
        </p>

        <label class="block text-sm font-medium text-gray-700 mb-2">Enter OTP</label>
        <input 
          v-model="otp" 
          type="text" 
          placeholder="••••"
          class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition-all text-center tracking-[0.5em] text-lg font-bold"
          maxlength="4"
          @keyup.enter="otp.length === 4 ? verifyOTP() : null"
        />

        <button 
          @click="verifyOTP"
          :disabled="otp.length !== 4 || isLoading"
          class="w-full mt-6 bg-green-600 text-white font-bold py-3.5 rounded-xl hover:bg-green-700 disabled:bg-green-300 transition-colors flex justify-center items-center gap-2"
        >
          <Loader2Icon v-if="isLoading" class="w-5 h-5 animate-spin" />
          <span v-else>Verify & Login</span>
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
// Swapped SmartphoneIcon out for MailIcon
import { XIcon, MailIcon, Loader2Icon } from 'lucide-vue-next' 

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

const step = ref(1)
const email = ref('') // Changed from phoneNumber
const otp = ref('')
const isLoading = ref(false)

// Simple check to ensure they typed a somewhat valid email before enabling the button
const isValidEmail = computed(() => {
  return email.value.includes('@') && email.value.includes('.')
})

// You will change this to your actual deployed backend URL later
const API_BASE = 'http://localhost:3000/api/auth'

const requestOTP = async () => {
  try {
    isLoading.value = true
    // Make request to your Node.js backend (sending email instead of phoneNumber)
    await axios.post(`${API_BASE}/send-otp`, { email: email.value })
    
    // If successful, move to OTP entry screen
    step.value = 2
  } catch (error) {
    alert("Failed to send OTP. Please try again.")
  } finally {
    isLoading.value = false
  }
}

const verifyOTP = async () => {
  try {
    isLoading.value = true
    // Verify OTP with Node.js backend
    const response = await axios.post(`${API_BASE}/verify-otp`, { 
      email: email.value, 
      otp: otp.value 
    })
    
    // Save the login token (usually in localStorage or Pinia state)
    localStorage.setItem('token', response.data.token)
    
    alert("Login Successful!")
    emit('close')
    
  } catch (error) {
    alert("Incorrect OTP. Please check and try again.")
  } finally {
    isLoading.value = false
  }
}
</script>