<script setup>
import { ref } from 'vue'
import { Menu, X } from 'lucide-vue-next'

const isMobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
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
          <router-link to="/home" class="text-sm font-medium text-gray-600 hover:text-primary transition">Services</router-link>
          <router-link to="/dashboard" class="text-sm font-medium text-gray-600 hover:text-primary transition">Dashboard</router-link>
          <router-link to="/profile" class="text-sm font-medium text-gray-600 hover:text-primary transition">Profile</router-link>
        </div>

        <!-- Desktop Auth Buttons -->
        <div class="hidden md:flex items-center gap-3">
          <router-link to="/auth" class="px-4 py-2 text-sm font-semibold text-primary hover:bg-primary/5 rounded-lg transition">
            Log In
          </router-link>
          <router-link to="/auth" class="px-5 py-2 text-sm font-semibold text-white bg-highlight rounded-lg hover:opacity-90 transition shadow-sm shadow-highlight/20">
            Sign Up
          </router-link>
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
        <router-link to="/home" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Services</router-link>
        <router-link to="/dashboard" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Dashboard</router-link>
        <router-link to="/profile" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Profile</router-link>
        
        <div class="pt-4 mt-4 border-t border-gray-100 flex flex-col gap-3">
          <router-link to="/auth" @click="closeMobileMenu" class="w-full text-center px-4 py-2.5 text-primary font-semibold border border-gray-200 rounded-lg hover:bg-gray-50 transition">
            Log In
          </router-link>
          <router-link to="/auth" @click="closeMobileMenu" class="w-full text-center px-4 py-2.5 bg-highlight text-white font-semibold rounded-lg hover:opacity-90 transition shadow-sm">
            Sign Up
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>