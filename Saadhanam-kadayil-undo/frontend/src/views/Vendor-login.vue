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
            class="w-full mt-2 bg-primary text-white font-bold text-lg py-4 rounded-2xl hover:opacity-90 active:scale-[0.98] transition-all shadow-md shadow-primary/20"
          >
            Login to Dashboard
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
import Navbar from '../components/Navbar.vue'
import { StoreIcon } from 'lucide-vue-next'

const loginForm = ref({
  email: '',
  password: ''
})

const handleVendorLogin = () => {
  console.log("Vendor Login Data Ready for Backend:", loginForm.value)
  // Backend logic will go here
}
</script>