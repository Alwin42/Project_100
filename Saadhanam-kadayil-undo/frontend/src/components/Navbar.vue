<template>
  <header class="w-full bg-white/80 backdrop-blur-md border-b border-gray-100 py-3 px-6 fixed top-0 flex justify-center z-50 transition-all duration-300">
    
    <div class="max-w-6xl w-full flex justify-between items-center">
      
      <router-link to="/" class="flex items-center gap-2.5 cursor-pointer group">
        <div class="p-1.5 bg-secondary/20 rounded-xl group-hover:bg-secondary/40 transition-colors duration-300">
          <ShoppingBasketIcon class="w-5 h-5 text-primary" />
        </div>
        <h1 class="text-xl font-bold text-gray-900 tracking-tight">StockUndo</h1>
      </router-link>
      
      <div class="flex items-center gap-3">
        
        <button 
          v-if="userRole !== 'vendor'" 
          class="text-sm font-semibold text-gray-600 hover:text-primary bg-gray-50/50 hover:bg-secondary/20 border border-transparent hover:border-secondary/40 px-5 py-2 rounded-full transition-all duration-300"
        >
          Become a Vendor
        </button>
        
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
          class="text-sm font-bold text-white hover:text-white bg-primary hover:opacity-90 px-6 py-2 rounded-full transition-all duration-300 shadow-sm hover:shadow-md"
        >
          Login
        </button>

        <button 
          v-else
          @click="handleLogout"
          class="text-sm font-semibold text-gray-600 hover:text-red-600 bg-gray-50/50 hover:bg-red-50 border border-transparent hover:border-red-100 px-5 py-2 rounded-full transition-all duration-300 flex items-center gap-2"
        >
          <LogOutIcon class="w-4 h-4" />
          Logout
        </button>

      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ShoppingBasketIcon, LogOutIcon } from 'lucide-vue-next'

const router = useRouter()

// Emits an event so the parent page knows to pop open the LoginModal
const emit = defineEmits(['open-login'])

const isLoggedIn = ref(false)
const userRole = ref('customer') // Defaults to customer

// Helper function to decode the JWT and safely read the payload
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

// Check local storage for token and determine role
const checkAuth = () => {
  const token = localStorage.getItem('token');
  if (token) {
    isLoggedIn.value = true;
    const decoded = parseJwt(token);
    
    // If the token has a role attached, update our state
    if (decoded && decoded.role) {
      userRole.value = decoded.role;
    }
  } else {
    isLoggedIn.value = false;
    userRole.value = 'customer';
  }
}

// Run the check when the Navbar loads
onMounted(() => {
  checkAuth();
});

// Logout function
const handleLogout = () => {
  // 1. Wipe the secure data from the browser
  localStorage.removeItem('token');
  localStorage.removeItem('userEmail');
  
  // 2. Reset the state variables
  isLoggedIn.value = false;
  userRole.value = 'customer';
  
  // 3. Kick the user back to the landing page
  router.push('/');
}
</script>