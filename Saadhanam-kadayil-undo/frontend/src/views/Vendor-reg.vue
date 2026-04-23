<template>
  <div class="min-h-screen bg-gray-50 flex flex-col font-sans selection:bg-secondary/40">
    
    <Navbar />

    <main class="grow flex items-center justify-center px-6 pt-28 pb-16">
      <div class="bg-white w-full max-w-3xl rounded-4xl shadow-xl border border-gray-100 p-8 sm:p-10 relative overflow-hidden">
        
        <div class="text-center mb-10">
          <h2 class="text-3xl font-bold text-primary tracking-tight">Partner with StockUndo</h2>
          <p class="text-gray-500 mt-2 font-medium">Get your local shop in front of thousands of nearby customers.</p>
        </div>

        <form @submit.prevent="handleVendorRegister" class="space-y-6">
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Shop/Business Name</label>
              <input 
                v-model="regForm.shopName" 
                type="text" 
                placeholder="e.g. Kerala Traders"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Owner's Full Name</label>
              <input 
                v-model="regForm.ownerName" 
                type="text" 
                placeholder="Your Name"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Business Email</label>
              <input 
                v-model="regForm.email" 
                type="email" 
                placeholder="shop@example.com"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Phone Number</label>
              <input 
                v-model="regForm.phone" 
                type="tel" 
                placeholder="+91"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>

          </div>

          <div class="space-y-6">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Shop Location / Address</label>
              <input 
                v-model="regForm.address" 
                type="text" 
                placeholder="Full street address"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Google Maps Link <span class="text-gray-400 font-normal">(Optional)</span></label>
              <input 
                v-model="regForm.mapUrl" 
                type="url" 
                placeholder="https://goo.gl/maps/..."
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
              />
              <p class="text-xs text-gray-500 mt-1.5">Paste the "Share" link from Google Maps so customers can find you easily.</p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Create Password</label>
              <input 
                v-model="regForm.password" 
                type="password" 
                placeholder="••••••••"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Confirm Password</label>
              <input 
                v-model="regForm.confirmPassword" 
                type="password" 
                placeholder="••••••••"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                required
              />
            </div>
          </div>

         <button 
            type="submit"
            :disabled="isLoading"
            class="w-full mt-6 bg-accent-1 text-primary font-bold text-lg py-4 rounded-2xl hover:brightness-95 active:scale-[0.98] transition-all shadow-sm flex justify-center items-center gap-2 disabled:opacity-70"
          >
            <Loader2Icon v-if="isLoading" class="w-6 h-6 animate-spin" />
            <span v-else>Register My Shop</span>
          </button>

        </form>

        <p class="text-center text-sm text-gray-600 mt-8 font-medium">
          Already a partner? 
          <router-link to="/vendor-login" class="text-primary font-bold hover:underline ml-1">
            Login here
          </router-link>
        </p>

      </div>
    </main>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import { Loader2Icon } from 'lucide-vue-next' 

const router = useRouter()
const isLoading = ref(false)

const regForm = ref({
  shopName: '',
  ownerName: '',
  email: '',
  phone: '',
  address: '',
  mapUrl: '',
  password: '',
  confirmPassword: ''
})

const handleVendorRegister = async () => {
  // 1. Double-check passwords match
  if(regForm.value.password !== regForm.value.confirmPassword) {
    alert("Passwords do not match!")
    return
  }
  
  try {
    isLoading.value = true;
    
    // 2. Send the data to your Node.js backend!
    const response = await axios.post('http://localhost:3000/api/auth/vendor/register', regForm.value);
    
    // 3. Save the secure token so they are instantly logged in
    localStorage.setItem('token', response.data.token);
    localStorage.setItem('userEmail', regForm.value.email);
    
    // 4. Send them straight to their new dashboard
    alert("Shop Registered Successfully!");
    router.push('/dashboard'); 
    
  } catch (error) {
    console.error("Registration Error:", error);
    // Show the exact error message from the backend (e.g., "Email already registered")
    alert(error.response?.data?.error || "Failed to register. Is your server running?");
  } finally {
    isLoading.value = false;
  }
}
</script>