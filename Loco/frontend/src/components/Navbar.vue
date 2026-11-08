<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { Menu, X, LogOut } from 'lucide-vue-next'

const router = useRouter()
const isMobileMenuOpen = ref(false)

// Check if user is logged in by looking for the token in localStorage
const isLoggedIn = ref(!!localStorage.getItem('token'))

// Ensure it stays updated if the user logs in/out in another tab
onMounted(() => {
  isLoggedIn.value = !!localStorage.getItem('token')
  window.addEventListener('storage', () => {
    isLoggedIn.value = !!localStorage.getItem('token')
  })
})

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

const handleLogout = () => {
  // 1. Remove the token from localStorage
  localStorage.removeItem('token')
  // 2. Update the reactive state
  isLoggedIn.value = false
  // 3. Close mobile menu if open
  closeMobileMenu()
  // 4. Redirect to home page
  router.push('/')
}
</script>

<template>
  <nav class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        
        <!-- Logo -->
        <router-link to="/" class="flex items-center gap-2 group">
          <span class="text-2xl font-bold text-primary tracking-tight">Loco</span>
        </router-link>
        
        <!-- Desktop Navigation Links -->
        <div class="hidden md:flex items-center gap-8">
          <router-link to="/" class="text-sm font-medium text-gray-600 hover:text-primary transition">Home</router-link>
          <router-link to="/services" class="text-sm font-medium text-gray-600 hover:text-primary transition">Services</router-link>
          <router-link to="/dashboard" class="text-sm font-medium text-gray-600 hover:text-primary transition">Dashboard</router-link>
          <router-link to="/profile" class="text-sm font-medium text-gray-600 hover:text-primary transition">Profile</router-link>
        </div>

        <!-- Desktop Auth Buttons -->
        <!-- SHOW IF LOGGED OUT -->
        <div v-if="!isLoggedIn" class="hidden md:flex items-center gap-3">
          <router-link to="/auth" class="px-4 py-2 text-sm font-semibold text-primary hover:bg-primary/5 rounded-lg transition">
            Log In
          </router-link>
          <router-link to="/auth" class="px-5 py-2 text-sm font-semibold text-white bg-highlight rounded-lg hover:opacity-90 transition shadow-sm shadow-highlight/20">
            Sign Up
          </router-link>
        </div>

        <!-- SHOW IF LOGGED IN -->
        <div v-else class="hidden md:flex items-center gap-3">
          <button 
            @click="handleLogout" 
            class="px-4 py-2 text-sm font-semibold text-gray-600 hover:bg-gray-100 hover:text-red-600 rounded-lg transition flex items-center gap-2"
          >
            <LogOut class="w-4 h-4" />
            Log Out
          </button>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button 
            @click="toggleMobileMenu" 
            class="p-2 text-gray-600 hover:text-primary hover:bg-gray-100 rounded-lg transition"
            aria-label="Toggle menu"
          >
            <Menu v-if="!isMobileMenuOpen" class="w-6 h-6" />
            <X v-else class="w-6 h-6" />
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu Dropdown -->
    <div 
      v-if="isMobileMenuOpen" 
      class="md:hidden bg-white border-t border-gray-100 shadow-lg absolute w-full left-0"
    >
      <div class="px-4 py-4 space-y-2">
        <router-link to="/" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Home</router-link>
        <router-link to="/services" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Services</router-link>
        <router-link to="/dashboard" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Dashboard</router-link>
        <router-link to="/profile" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Profile</router-link>
        
        <div class="pt-4 mt-4 border-t border-gray-100 flex flex-col gap-3">
          <!-- Mobile Auth Buttons -->
          <template v-if="!isLoggedIn">
            <router-link to="/auth" @click="closeMobileMenu" class="w-full text-center px-4 py-2.5 text-primary font-semibold border border-gray-200 rounded-lg hover:bg-gray-50 transition">
              Log In
            </router-link>
            <router-link to="/auth" @click="closeMobileMenu" class="w-full text-center px-4 py-2.5 bg-highlight text-white font-semibold rounded-lg hover:opacity-90 transition shadow-sm">
              Sign Up
            </router-link>
          </template>
          
          <template v-else>
            <button 
              @click="handleLogout" 
              class="w-full text-center px-4 py-2.5 text-red-600 font-semibold border border-red-100 bg-red-50 rounded-lg hover:bg-red-100 transition flex items-center justify-center gap-2"
            >
              <LogOut class="w-4 h-4" />
              Log Out
            </button>
          </template>
        </div>
      </div>
    </div>
  </nav>
</template>