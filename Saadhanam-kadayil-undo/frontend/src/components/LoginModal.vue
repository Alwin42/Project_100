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
        <p class="text-gray-500 mt-2 text-sm">Log in instantly with a secure code.</p>
      </div>

      <div v-if="step === 1">
        <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
        <input 
          v-model="email" 
          type="email" 
          placeholder="you@example.com"
          class="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none transition-all"
          @keyup.enter="isValidEmail ? requestOTP() : null"
        />

        <button 
          @click="requestOTP"
          :disabled="!isValidEmail || isLoading"
          class="w-full mt-6 bg-green-600 text-white font-bold py-3.5 rounded-xl hover:bg-green-700 disabled:bg-green-300 transition-colors flex justify-center items-center gap-2"
        >
          <Loader2Icon v-if="isLoading" class="w-5 h-5 animate-spin" />
          <span v-else>Get Code</span>
        </button>
      </div>

      <div v-if="step === 2">
        <p class="text-sm text-center text-gray-600 mb-6">
          We sent a 4-digit code to <br/><strong>{{ email }}</strong>. 
          <button @click="step = 1" class="text-green-600 font-medium hover:underline ml-1">Edit</button>
        </p>

        <label class="block text-sm font-medium text-gray-700 mb-2">Enter Code</label>
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
import { XIcon, MailIcon, Loader2Icon } from 'lucide-vue-next' 

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

const step = ref(1)
const email = ref('')
const otp = ref('')
const isLoading = ref(false)

// Validates email before allowing the button click
const isValidEmail = computed(() => email.value.includes('@') && email.value.includes('.'))

// Connects directly to your local Node.js server!
const API_BASE = 'http://localhost:3000/api/auth'

const requestOTP = async () => {
  try {
    isLoading.value = true;
    // 1. Send the email to Node.js
    await axios.post(`${API_BASE}/send-otp`, { email: email.value });
    step.value = 2; // Move to next screen
  } catch (error) {
    console.error(error);
    alert("Failed to send code. Is your Node.js server running?");
  } finally {
    isLoading.value = false;
  }
}

const verifyOTP = async () => {
  try {
    isLoading.value = true;
    // 2. Send the OTP and Email to Node.js for verification
    const response = await axios.post(`${API_BASE}/verify-otp`, { 
      email: email.value, 
      otp: otp.value 
    });
    
    // 3. Save the secure JWT token so the user stays logged in!
    localStorage.setItem('token', response.data.token);
    localStorage.setItem('userEmail', email.value);
    
    // 4. Close the modal and optionally reload or redirect
    emit('close');
    alert("Login Successful! Check your console.");
    
    // Quick refresh to update the UI (you can replace this with Vue Router navigation later)
    window.location.reload(); 
    
  } catch (error) {
    console.error(error);
    alert("Incorrect code. Please check your email and try again.");
  } finally {
    isLoading.value = false;
  }
}
</script>