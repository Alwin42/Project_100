<template>
  <div class="min-h-screen bg-gray-50 flex flex-col font-sans selection:bg-secondary/40">
    
    <Navbar />

    <main class="grow flex items-center justify-center px-6 pt-28 pb-16">
      <div class="bg-white w-full max-w-md rounded-4xl shadow-xl border border-gray-100 p-8 sm:p-10 relative overflow-hidden">
        
        <div class="absolute top-0 right-0 -mr-8 -mt-8 w-32 h-32 bg-secondary/20 rounded-full blur-2xl pointer-events-none"></div>

        <div class="text-center mb-8 relative z-10">
          <div class="mx-auto w-14 h-14 bg-secondary/30 rounded-2xl flex items-center justify-center mb-5">
            <StoreIcon class="w-7 h-7 text-primary" /> 
          </div>
          <h2 class="text-3xl font-bold text-gray-900 tracking-tight">Vendor Portal</h2>
          <p class="text-gray-500 mt-2 font-medium">Manage your shop, live stock, and orders.</p>
        </div>

        <form @submit.prevent="handleVendorLogin" class="space-y-5 relative z-10">
          
          <div>
            <label class="block text-sm font-bold text-gray-700 mb-2">Business Email</label>
            <input 
              v-model="loginForm.email" 
              type="email" 
              placeholder="shop@example.com"
              class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
              required
            />
          </div>

          <div>
            <div class="flex justify-between items-center mb-2">
              <label class="block text-sm font-bold text-gray-700">Password</label>
              <a href="#" class="text-xs font-bold text-primary hover:underline">Forgot?</a>
            </div>
            <input 
              v-model="loginForm.password" 
              type="password" 
              placeholder="••••••••"
              class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
              required
            />
          </div>

          <button 
            type="submit"
            :disabled="isLoading"
            class="w-full mt-2 bg-primary text-white font-bold text-lg py-4 rounded-2xl hover:opacity-90 active:scale-[0.98] transition-all shadow-md shadow-primary/20 flex justify-center items-center gap-2 disabled:opacity-70"
          >
            <Loader2Icon v-if="isLoading" class="w-6 h-6 animate-spin" />
            <span v-else>Login to Dashboard</span>
          </button>

        </form>

        <p class="text-center text-sm text-gray-600 mt-8 font-medium">
          Want to list your shop? 
          <router-link to="/vendor-register" class="text-primary font-bold hover:underline ml-1">
            Register here
          </router-link>
        </p>

      </div>
    </main>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import { StoreIcon, Loader2Icon } from 'lucide-vue-next'

const router = useRouter()
const isLoading = ref(false)

const loginForm = ref({
  email: '',
  password: ''
})

const handleVendorLogin = async () => {
  try {
    isLoading.value = true;
    
    // 1. Send the email and password to your Node.js server!
    const response = await axios.post('http://localhost:3000/api/auth/vendor/login', loginForm.value);
    
    // 2. Save the secure token so the app remembers who is logged in
    localStorage.setItem('token', response.data.token);
    localStorage.setItem('userEmail', loginForm.value.email);
    
    // 3. Send them straight to the new Vendor Dashboard!
    router.push('/dashboard'); 
    
  } catch (error) {
    console.error("Login Error:", error);
    // This will pop up an alert if they type the wrong password
    alert(error.response?.data?.error || "Login failed. Please check your connection.");
  } finally {
    isLoading.value = false;
  }
}
</script>