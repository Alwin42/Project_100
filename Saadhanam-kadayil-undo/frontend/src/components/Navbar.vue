<template>
  <div class="fixed top-4 inset-x-4 z-50 flex flex-col items-center pointer-events-none">
    
    <header class="w-full max-w-5xl bg-white/90 backdrop-blur-md border border-gray-200 shadow-lg rounded-full py-2.5 px-6 flex justify-between items-center pointer-events-auto transition-all duration-300">
      
      <router-link to="/" class="flex items-center gap-2.5 cursor-pointer group shrink-0">
        <div class="p-1.5 bg-secondary/20 rounded-xl group-hover:bg-secondary/40 transition-colors duration-300">
          <ShoppingBasketIcon class="w-5 h-5 text-primary" />
        </div>
        <h1 class="text-xl font-bold text-gray-900 tracking-tight">StockUndo</h1>
      </router-link>
      
      <div class="hidden md:flex items-center gap-3">
        
        <router-link 
          v-if="userRole !== 'vendor'" 
          to="/vendor-register"
          class="text-sm font-semibold text-gray-600 hover:text-primary bg-gray-50/50 hover:bg-secondary/20 border border-transparent hover:border-secondary/40 px-5 py-2 rounded-full transition-all duration-300"
        >
          Become a Vendor
        </router-link>
        
        <router-link 
          v-if="isLoggedIn && userRole === 'vendor'" 
          to="/dashboard"
          class="text-sm font-bold text-primary bg-secondary/20 hover:bg-secondary/30 px-5 py-2 rounded-full transition-all duration-300"
        >
          Vendor Dashboard 
        </router-link>
        
        <button 
          v-if="!isLoggedIn"
          @click="$emit('open-login')"
          class="text-sm font-bold text-white hover:text-white bg-primary hover:opacity-90 px-6 py-2 rounded-full transition-all duration-300 shadow-sm hover:shadow-md active:scale-95"
        >
          Login
        </button>

        <button 
          v-else
          @click="handleLogout"
          class="text-sm font-semibold text-gray-600 hover:text-red-600 bg-gray-50/50 hover:bg-red-50 border border-transparent hover:border-red-100 px-5 py-2 rounded-full transition-all duration-300 flex items-center gap-2 active:scale-95"
        >
          <LogOutIcon class="w-4 h-4" />
          Logout
        </button>

      </div>

      <button 
        @click="isMobileMenuOpen = !isMobileMenuOpen" 
        class="md:hidden p-2 text-gray-600 hover:text-primary bg-gray-50/50 rounded-full transition-colors active:scale-95"
      >
        <MenuIcon v-if="!isMobileMenuOpen" class="w-6 h-6" />
        <XIcon v-else class="w-6 h-6" />
      </button>

    </header>

    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="transform scale-95 opacity-0 -translate-y-2"
      enter-to-class="transform scale-100 opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="transform scale-100 opacity-100 translate-y-0"
      leave-to-class="transform scale-95 opacity-0 -translate-y-2"
    >
      <div 
        v-if="isMobileMenuOpen"
        class="w-full max-w-sm mt-3 bg-white/95 backdrop-blur-xl border border-gray-200 shadow-2xl rounded-3xl p-5 flex flex-col gap-3 pointer-events-auto md:hidden"
      >
        <router-link 
          v-if="userRole !== 'vendor'" 
          to="/vendor-register"
          @click="isMobileMenuOpen = false"
          class="w-full text-center text-sm font-semibold text-gray-700 hover:text-primary bg-gray-50 hover:bg-secondary/20 py-3 rounded-2xl transition-colors"
        >
          Become a Vendor
        </router-link>

        <router-link 
          v-if="isLoggedIn && userRole === 'vendor'" 
          to="/dashboard"
          @click="isMobileMenuOpen = false"
          class="w-full text-center text-sm font-bold text-primary bg-secondary/20 hover:bg-secondary/30 py-3 rounded-2xl transition-colors"
        >
          Vendor Dashboard
        </router-link>

        <button 
          v-if="!isLoggedIn"
          @click="handleMobileLogin"
          class="w-full text-center text-sm font-bold text-white bg-primary py-3 rounded-2xl transition-colors active:scale-95"
        >
          Login
        </button>

        <button 
          v-else
          @click="handleMobileLogout"
          class="w-full flex items-center justify-center gap-2 text-sm font-semibold text-red-600 bg-red-50 hover:bg-red-100 py-3 rounded-2xl transition-colors active:scale-95"
        >
          <LogOutIcon class="w-4 h-4" />
          Logout
        </button>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ShoppingBasketIcon, LogOutIcon, MenuIcon, XIcon } from 'lucide-vue-next'

const router = useRouter()
const emit = defineEmits(['open-login'])

const isLoggedIn = ref(false)
const userRole = ref('customer') 
const isMobileMenuOpen = ref(false) // State for mobile drawer

const parseJwt = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (e) {
    return null;
  }
}

const checkAuth = () => {
  const token = localStorage.getItem('token');
  if (token) {
    isLoggedIn.value = true;
    const decoded = parseJwt(token);
    if (decoded && decoded.role) {
      userRole.value = decoded.role;
    }
  } else {
    isLoggedIn.value = false;
    userRole.value = 'customer';
  }
}

onMounted(() => {
  checkAuth();
});

// Helper for desktop logout
const handleLogout = () => {
  localStorage.removeItem('token');
  localStorage.removeItem('userEmail');
  isLoggedIn.value = false;
  userRole.value = 'customer';
  router.push('/');
}

// Helpers for mobile interactions (closes the menu simultaneously)
const handleMobileLogin = () => {
  isMobileMenuOpen.value = false;
  emit('open-login');
}

const handleMobileLogout = () => {
  isMobileMenuOpen.value = false;
  handleLogout();
}
</script>