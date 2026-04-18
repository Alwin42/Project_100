<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center font-sans selection:bg-green-200 relative">
    
    <Navbar />

    <main class="mt-32 mb-16 px-6 max-w-7xl w-full grow grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      
      <div class="flex flex-col items-start text-left">
        
        <div class="animate-pulse bg-green-100 text-green-800 text-xs md:text-sm font-semibold px-4 py-1.5 rounded-full mb-8 shadow-sm border border-green-200">
          ✨ Find what you need, right now.
        </div>

        <h2 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6 leading-tight tracking-tight">
          Saadhanam <br/>         
          <span class="text-transparent bg-clip-text bg-linear-to-r from-green-600 to-emerald-400">
            kadayil undo?
          </span>
        </h2>
        
        <p class="text-lg md:text-xl text-gray-600 mb-10 max-w-xl leading-relaxed">
          Check live stock, reserve items, and order directly from local vendors. Stop guessing if it's in stock before you walk.
        </p>

        <button 
          @click="isModalOpen = true"
          class="group relative overflow-hidden rounded-full bg-green-600 px-8 py-3.5 text-lg font-bold text-white shadow-[0_4px_14px_0_rgba(22,163,74,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(22,163,74,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
        >
          <span class="absolute inset-0 bg-white/20 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
          <span>Login to Start Shopping</span>
          <ArrowRightIcon class="w-5 h-5 transition-transform duration-300 group-hover:translate-x-1" />
        </button>

      </div>

      <div class="w-full relative group">
         <div class="w-full h-64 md:h-96 bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden relative">
            <img 
               src="/images/grocery-img.jpg" 
               alt="Saadhanam Kadayil undo - App Preview" 
               class="w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
            />
            <div class="absolute inset-0 bg-linear-to-t from-black/20 to-transparent pointer-events-none"></div>
         </div>
      </div>
      
    </main>

    <LoginModal :isOpen="isModalOpen" @close="isModalOpen = false" />

  </div>
</template>

<script setup>
// ADDED: Import ref for state management
import { ref } from 'vue' 
import Navbar from '../components/Navbar.vue'
// ADDED: Import the LoginModal component
import LoginModal from '../components/LoginModal.vue' 
import { ArrowRightIcon } from 'lucide-vue-next'

// ADDED: State to track if the modal is open or closed
const isModalOpen = ref(false)
</script>