<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center font-sans selection:bg-secondary/40 relative">
    
    <Navbar @open-login="isModalOpen = true" />

    <main class="mt-32 mb-16 px-6 max-w-7xl w-full grow grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      
      <div class="flex flex-col items-start text-left">
        
        <div class=" bg-accent-1 text-primary text-xs md:text-sm font-bold px-4 py-1.5 rounded-full mb-8 shadow-sm border border-accent-1/50">
          ✨ Find what you need, right now.
        </div>

        <h2 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6 leading-tight tracking-tight">
          Saadhanam <br/>         
          <span class="text-transparent bg-clip-text bg-linear-to-r from-primary to-secondary">
            kadayil undo?
          </span>
        </h2>
        
        <p class="text-lg md:text-xl text-gray-600 mb-10 max-w-xl leading-relaxed">
          Check live stock, reserve items, and order directly from local vendors. Stop guessing if it's in stock before you walk.
        </p>

        <div>
          <button 
            v-if="!isLoggedIn"
            @click="isModalOpen = true"
            class="group relative overflow-hidden rounded-full bg-primary px-8 py-3.5 text-lg font-bold text-white shadow-[0_4px_14px_0_rgba(70,132,50,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(70,132,50,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
          >
            <span class="absolute inset-0 bg-white/20 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
            <span>Login to Start Shopping</span>
            <ArrowRightIcon class="w-5 h-5 transition-all duration-300 group-hover:translate-x-1 group-hover:text-accent-2" />
          </button>

          <button 
            v-else
            @click="goToShop"
            class="group relative overflow-hidden rounded-full bg-primary px-8 py-3.5 text-lg font-bold text-white shadow-[0_4px_14px_0_rgba(70,132,50,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(70,132,50,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
          >
            <span class="absolute inset-0 bg-white/20 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
            <span>Start Shopping</span>
            <ArrowRightIcon class="w-5 h-5 transition-all duration-300 group-hover:translate-x-1 group-hover:text-accent-2" />
          </button>
        </div>

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
import { ref, onMounted } from 'vue' 
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import LoginModal from '../components/LoginModal.vue' 
import { ArrowRightIcon } from 'lucide-vue-next'

const isModalOpen = ref(false)
const isLoggedIn = ref(false)
const router = useRouter()

// Check if the user is logged in when the landing page loads
onMounted(() => {
  const token = localStorage.getItem('token')
  if (token) {
    isLoggedIn.value = true
  }
})

// Function to route logged-in users directly to the store
const goToShop = () => {
  router.push('/home') // Make sure this matches the path in your router configuration
}
</script>