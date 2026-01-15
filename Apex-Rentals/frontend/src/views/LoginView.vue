<script setup>
import { ref } from 'vue'

const username = ref('')
const password = ref('')

const handleLogin = () => {
  console.log("Logging in with:", username.value, password.value)
  // Add actual login logic here later
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

    <div class="relative z-10 w-full max-w-md bg-[#0B2B38]/90 p-8 md:p-12 border border-white/10 shadow-2xl backdrop-blur-md animate-fade-in-up">
      
      <div class="text-center mb-10">
        <h1 class="text-3xl font-bold text-white mb-2 tracking-tight">Welcome Back</h1>
        <p class="text-gray-400 text-sm">Access your premium dashboard</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        
        <div class="group">
          <label class="block text-[#5F9598] text-xs font-bold uppercase tracking-widest mb-2">Username</label>
          <input 
            v-model="username" 
            type="text" 
            class="w-full bg-[#061E29] border border-white/10 text-white px-4 py-3 focus:outline-none focus:border-[#5F9598] transition-colors duration-300 placeholder-gray-600"
            placeholder="Enter your username"
          >
        </div>

        <div class="group">
          <label class="block text-[#5F9598] text-xs font-bold uppercase tracking-widest mb-2">Password</label>
          <input 
            v-model="password" 
            type="password" 
            class="w-full bg-[#061E29] border border-white/10 text-white px-4 py-3 focus:outline-none focus:border-[#5F9598] transition-colors duration-300 placeholder-gray-600"
            placeholder="••••••••"
          >
        </div>

        <button 
          type="submit"
          class="w-full bg-[#5F9598] text-[#061E29] font-bold py-4 uppercase tracking-widest hover:bg-white transition-colors duration-300 mt-4"
        >
          Sign In
        </button>

      </form>

      <div class="mt-8 text-center border-t border-white/10 pt-6">
        <p class="text-gray-400 text-sm">
          New to Apex Rentals? 
          <router-link to="/register" class="text-[#5F9598] hover:text-white font-bold ml-1 transition-colors">
            Create Account
          </router-link>
        </p>
      </div>

    </div>
  </div>
</template>