<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Reactive state to track login status
const isLoggedIn = ref(false)

// Function to check if user is logged in
const checkLoginStatus = () => {
  const token = localStorage.getItem('token')
  const userId = localStorage.getItem('user_id')
  // Returns true if both exist, otherwise false
  isLoggedIn.value = !!(token && userId)
}

// 1. Check on initial load
onMounted(() => {
  checkLoginStatus()
})

// 2. Watch the route to re-check login status on navigation
watch(() => route.path, () => {
  checkLoginStatus()
})

// Logout Logic
const handleLogout = () => {
  localStorage.clear()
  isLoggedIn.value = false
  router.push('/login')
}
</script>

<template>
  <div class="min-h-screen w-full bg-[#061E29] text-[#F3F4F4] font-sans selection:bg-[#5F9598] selection:text-[#061E29]">
    
    <nav class="absolute top-0 left-0 w-full z-50 py-8 px-6 lg:px-16">
      <div class="max-w-[1920px] mx-auto flex justify-between items-center">
        
        <router-link to="/" class="text-3xl font-bold tracking-tight hover:text-[#5F9598] transition-colors duration-300">
          Apex-Rentals
        </router-link>
        
        <div class="hidden md:flex items-center gap-12 text-base font-medium">
          <router-link to="/" class="hover:text-[#5F9598] transition-colors duration-300">Home</router-link>
          <router-link to="/about" class="hover:text-[#5F9598] transition-colors duration-300">About</router-link>
          <router-link to="/fleet" class="hover:text-[#5F9598] transition-colors duration-300">Fleet</router-link>
          <router-link to="/dashboard" class="hover:text-[#5F9598] transition-colors duration-300">Dashboard</router-link>
          
          <router-link 
            v-if="!isLoggedIn" 
            to="/login" 
            class="border-b border-transparent hover:border-white pb-1 transition-all duration-300"
          >
            Login
          </router-link>

          <button 
            v-else 
            @click="handleLogout" 
            class="border-b border-transparent hover:border-red-600 text-red-400 hover:text-red-500 pb-1 transition-all duration-300 cursor-pointer"
          >
            log-out
          </button>
        </div>

        <div class="md:hidden">
          <button class="text-white hover:text-[#5F9598] transition">
            <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

      </div>
    </nav>

    <router-view></router-view> 
  </div>
</template>