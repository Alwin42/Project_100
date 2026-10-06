<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}
</script>

<template>
  <nav class="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">
        
        <!-- Logo -->
        <a href="/" class="flex items-center gap-2 group">
          
          <span class="text-2xl font-bold text-primary">Loco</span>
        </a>
        
        <!-- Desktop Links -->
        <div class="hidden md:flex items-center gap-8">
          <a href="#categories" class="text-gray-600 hover:text-primary transition font-medium">Services</a>
          <a href="#how-it-works" class="text-gray-600 hover:text-primary transition font-medium">How it Works</a>
          <a href="/dashboard" class="text-gray-600 hover:text-primary transition font-medium">Dashboard</a>

        </div>

        <!-- Desktop Auth Buttons -->
        <div class="hidden md:flex items-center gap-3">
          <router-link to="/auth" class="px-4 py-2 text-primary font-semibold hover:bg-primary/5 rounded-lg transition">Log In</router-link>
          <router-link to="/auth" class="px-5 py-2 bg-highlight text-white font-semibold rounded-lg hover:opacity-90 transition shadow-lg shadow-highlight/20">Sign Up</router-link>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="toggleMobileMenu" class="p-2 text-gray-600 hover:text-primary hover:bg-gray-100 rounded-lg transition">
            <!-- Hamburger Icon -->
            <svg v-if="!isMobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
            <!-- Close Icon -->
            <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu Dropdown -->
    <div v-if="isMobileMenuOpen" class="md:hidden bg-white border-t border-gray-100 shadow-lg">
      <div class="px-4 py-4 space-y-3">
        <a href="#categories" @click="isMobileMenuOpen = false" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium">Services</a>
        <a href="#how-it-works" @click="isMobileMenuOpen = false" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium">How it Works</a>
        <a href="#provider-cta" @click="isMobileMenuOpen = false" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium">Become a Pro</a>
        
        <div class="pt-3 border-t border-gray-100 flex flex-col gap-3">
          <button class="w-full px-4 py-2 text-primary font-semibold border border-primary/20 rounded-lg hover:bg-primary/5 transition">Log In</button>
          <button class="w-full px-4 py-2 bg-highlight text-white font-semibold rounded-lg hover:opacity-90 transition shadow-md">Sign Up</button>
        </div>
      </div>
    </div>
  </nav>
</template>