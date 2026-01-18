<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const step = ref(1) // 1 = Email, 2 = OTP
const loading = ref(false)
const email = ref('')
const otp = ref('')
const message = ref('')
const error = ref('')

const API_URL = "http://127.0.0.1:8000"

const handleSendOTP = async () => {
  loading.value = true
  error.value = ''
  message.value = ''
  
  try {
    // Send email to backend
    await axios.post(`${API_URL}/api/auth/send-otp/`, { email: email.value })
    message.value = `Code sent to ${email.value}`
    step.value = 2 // Move to next screen
  } catch (err) {
    error.value = err.response?.data?.error || "Failed to send code. Check email."
  } finally {
    loading.value = false
  }
}

const handleVerifyOTP = async () => {
  loading.value = true
  error.value = ''
  
  try {
    // Verify code with backend
    const response = await axios.post(`${API_URL}/api/auth/verify-otp/`, { 
      email: email.value, 
      otp: otp.value 
    })
    
    // Login Success!
    // Store user ID or Token in localStorage if needed
    localStorage.setItem('user_id', response.data.user_id)
    
    router.push('/fleet') // Redirect to the car list
  } catch (err) {
    error.value = "Invalid code. Please try again."
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="relative min-h-screen w-full flex items-center justify-center overflow-hidden">
    
    <div 
      class="absolute inset-0 bg-cover bg-center bg-no-repeat"
      style="background-image: url('/hero-bg.jpg');"
    >
      <div class="absolute inset-0 bg-[#061E29]/80 backdrop-blur-sm"></div>
    </div>

    <div class="relative z-10 w-full max-w-md bg-[#0B2B38]/90 p-8 md:p-12 border border-white/10 shadow-2xl backdrop-blur-md animate-fade-in-up rounded-2xl">
      
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-white mb-2 tracking-tight">
          {{ step === 1 ? 'Welcome Back' : 'Verify Identity' }}
        </h1>
        <p class="text-gray-400 text-sm">
          {{ step === 1 ? 'Enter your email to access your account' : 'Enter the 6-digit code sent to your email' }}
        </p>
      </div>

      <form v-if="step === 1" @submit.prevent="handleSendOTP" class="space-y-6">
        <div class="group">
          <label class="block text-[#5F9598] text-xs font-bold uppercase tracking-widest mb-2">Email Address</label>
          <input 
            v-model="email" 
            type="email" 
            required
            class="w-full bg-[#061E29] border border-white/10 text-white px-4 py-3 rounded focus:outline-none focus:border-[#5F9598] transition-colors duration-300 placeholder-gray-600"
            placeholder="name@example.com"
          >
        </div>
        <button 
          type="submit"
          :disabled="loading"
          class="w-full bg-[#5F9598] text-[#061E29] font-bold py-4 rounded uppercase tracking-widest hover:bg-white transition-colors duration-300 mt-4 disabled:opacity-50"
        >
          {{ loading ? 'Sending Code...' : 'Send Login Code' }}
        </button>
      </form>

      <form v-else @submit.prevent="handleVerifyOTP" class="space-y-6">
        <div class="group">
          <label class="block text-[#5F9598] text-xs font-bold uppercase tracking-widest mb-2">Verification Code</label>
          <input 
            v-model="otp" 
            type="text" 
            maxlength="6"
            class="w-full bg-[#061E29] border border-white/10 text-white px-4 py-3 rounded text-center tracking-[0.5em] text-2xl font-bold focus:outline-none focus:border-[#5F9598] transition-colors duration-300"
            placeholder="••••••"
          >
        </div>
        
        <button 
          type="submit"
          :disabled="loading"
          class="w-full bg-[#5F9598] text-[#061E29] font-bold py-4 rounded uppercase tracking-widest hover:bg-white transition-colors duration-300 mt-4 disabled:opacity-50"
        >
          {{ loading ? 'Verifying...' : 'Login Now' }}
        </button>
        
        <button 
          type="button" 
          @click="step = 1" 
          class="w-full text-gray-400 text-xs hover:text-white mt-4"
        >
          Entered wrong email? Go back
        </button>
      </form>

      <div v-if="message" class="mt-4 p-3 bg-green-500/20 border border-green-500/30 rounded text-green-400 text-xs text-center">
        {{ message }}
      </div>
      <div v-if="error" class="mt-4 p-3 bg-red-500/20 border border-red-500/30 rounded text-red-400 text-xs text-center">
        {{ error }}
      </div>

    </div>
  </div>
</template>