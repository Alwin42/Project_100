<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center font-sans selection:bg-secondary/40 relative">
    
    <Navbar @open-login="isModalOpen = true" />

    <main class="mt-32 mb-16 px-6 max-w-7xl w-full grow grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      
      <div class="flex flex-col items-start text-left">
        
        <div class="  text-primary text-xs md:text-sm font-bold px-4 py-1.5 rounded-full mb-8 shadow-sm border">
          Fresh catch & premium cuts, without the wait.
        </div>

        <h2 class="text-4xl md:text-6xl font-extrabold text-gray-900 mb-6 leading-tight tracking-tight">
          Meat     
          <span class="text-transparent bg-clip-text bg-linear-to-r from-primary to-secondary">
          undo?
          </span>
        </h2>
        
        <p class="text-lg md:text-xl text-gray-600 mb-10 max-w-xl leading-relaxed">
          Skip the messy waiting areas. Check live stock, request your exact cut (curry, fillet, skinless), and reserve premium meat, fish, and farm-fresh eggs from your trusted local butchers before they sell out.
        </p>

        <div class="flex flex-wrap gap-4">
          <button 
            v-if="!isLoggedIn"
            @click="isModalOpen = true"
            class="group relative overflow-hidden rounded-full bg-primary px-8 py-3.5 text-lg font-bold text-white shadow-[0_4px_14px_0_rgba(70,132,50,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(70,132,50,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
          >
            <span class="absolute inset-0 bg-white/20 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
            <span>Login to Reserve</span>
            <ArrowRightIcon class="w-5 h-5 transition-all duration-300 group-hover:translate-x-1 group-hover:text-accent-2" />
          </button>
          
          <button 
            v-if="!isLoggedIn"
            @click="goToVendorLogin"
            class="group relative overflow-hidden rounded-full px-8 py-3.5 text-lg font-bold text-green-800 shadow-[0_4px_14px_0_rgba(70,132,50,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(70,132,50,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
          >
            <span class="absolute inset-0  opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
            <span>Login as Vendor</span>
            <ArrowRightIcon class="w-5 h-5 transition-all duration-300 group-hover:translate-x-1 group-hover:text-accent-2" />
          </button>

          <button 
            v-else
            @click="goToShop"
            class="group relative overflow-hidden rounded-full bg-primary px-8 py-3.5 text-lg font-bold text-white shadow-[0_4px_14px_0_rgba(70,132,50,0.39)] transition-all hover:shadow-[0_6px_20px_rgba(70,132,50,0.23)] hover:-translate-y-1 active:translate-y-0 active:shadow-md flex items-center gap-2"
          >
            <span class="absolute inset-0 bg-white/20 opacity-0 transition-opacity duration-300 group-hover:opacity-100"></span>
            <span>Browse Fresh Cuts</span>
            <ArrowRightIcon class="w-5 h-5 transition-all duration-300 group-hover:translate-x-1 group-hover:text-accent-2" />
          </button>
        </div>

      </div>

      <div class="w-full relative group">
         <div class="w-full h-64 md:h-96 bg-white rounded-3xl shadow-xl border border-gray-100 overflow-hidden relative">
            <img 
               src="/images/fresh-meat-fish.jpg" 
               alt="Saadhanam Kadayil undo - Fresh Meat and Fish" 
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

onMounted(() => {
  const token = localStorage.getItem('token')
  if (token) {
    isLoggedIn.value = true
  }
})

const goToShop = () => {
  router.push('/home')
}

const goToVendorLogin = () => {
  router.push('/vendor-login')
}
</script>