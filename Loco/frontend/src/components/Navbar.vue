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
          <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white font-bold text-xl shadow-sm group-hover:shadow-md transition">
            L
          </div>
          <span class="text-2xl font-bold text-primary tracking-tight">Loco</span>
        </router-link>
        
        <!-- Desktop Navigation Links -->
        <div class="hidden md:flex items-center gap-8">
          <a href="#categories" class="text-sm font-medium text-gray-600 hover:text-primary transition">Services</a>
          <a href="#how-it-works" class="text-sm font-medium text-gray-600 hover:text-primary transition">How it Works</a>
          <a href="#provider-cta" class="text-sm font-medium text-gray-600 hover:text-primary transition">Become a Pro</a>
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
        <a href="#categories" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Services</a>
        <a href="#how-it-works" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">How it Works</a>
        <a href="#provider-cta" @click="closeMobileMenu" class="block px-3 py-2 text-gray-600 hover:text-primary hover:bg-gray-50 rounded-lg font-medium transition">Become a Pro</a>
        
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