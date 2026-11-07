<script setup>
import { ArrowRight, Briefcase, Home, Lock, Mail, MapPin, Phone, User } from 'lucide-vue-next'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login, register } from '../api/auth'
import Navbar from '../components/Navbar.vue'

const router = useRouter()
const isLogin = ref(true)
const isLoading = ref(false)
const errorMessage = ref('')

const formData = ref({
  email: '',
  password: '',
  name: '',
  phone: '',
  city_town: '',
  country: '',
  role: '' 
})

const toggleMode = () => {
  isLogin.value = !isLogin.value
  errorMessage.value = ''
}

const handleSubmit = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  try {
    if (isLogin.value) {
      const res = await login({ email: formData.value.email, password: formData.value.password })
      localStorage.setItem('token', res.data.access_token)
      
      // Decode token to get role (simple split for demo, ideally use a JWT decoder)
      const payload = JSON.parse(atob(res.data.access_token.split('.')[1]))
      
      if (payload.role === 'provider') {
        router.push('/dashboard')
      } else {
        router.push('/home')
      }
    } else {
      await register(formData.value)
      // Switch to login mode after successful registration
      isLogin.value = true 
    }
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'An error occurred. Please try again.'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <Navbar/>
  <div class="min-h-screen flex flex-col md:flex-row bg-white">
    <!-- Left Side: Branding / Hero -->
    <div class="hidden md:flex md:w-1/2 bg-gradient-to-br from-primary via-secondary to-accent text-white p-12 flex-col justify-between relative overflow-hidden">
      <!-- Decorative blobs -->
      <div class="absolute top-0 right-0 w-96 h-96 bg-highlight/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-96 h-96 bg-accent/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
      
      <div class="relative z-10">
        <h1 class="text-4xl lg:text-5xl font-extrabold leading-tight mb-4">
          Connect with <br/> Trusted Local <br/> <span class="text-highlight">Professionals</span>
        </h1>
        <p class="text-lg text-blue-100 max-w-md">
          Whether you need a quick fix or a long-term partner, Loco brings the best local talent to your fingertips.
        </p>
      </div>
      
      <div class="relative z-10 text-sm text-blue-200">
        &copy; {{ new Date().getFullYear() }} Loco. All rights reserved.
      </div>
    </div>

    <!-- Right Side: Auth Form -->
    <div class="w-full md:w-1/2 p-6 sm:p-12 flex items-center">
      <div class="w-full max-w-md mx-auto">
        <!-- Mobile Logo -->
        <div class="md:hidden flex items-center gap-2 mb-8 justify-center">
          <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white font-bold text-xl">L</div>
          <span class="text-2xl font-bold text-primary">Loco</span>
        </div>

        <h2 class="text-3xl font-bold text-gray-900 mb-2">
          {{ isLogin ? 'Welcome back' : 'Create your account' }}
        </h2>
        <p class="text-gray-500 mb-8">
          {{ isLogin ? 'Enter your credentials to access your account.' : 'Join Loco today and get started.' }}
        </p>

        <form @submit.prevent="handleSubmit" class="space-y-4">
          <!-- Error Message -->
          <div v-if="errorMessage" class="p-3 bg-red-50 text-red-600 text-sm rounded-lg border border-red-100">
            {{ errorMessage }}
          </div>

          <!-- Full Name -->
          <div class="relative">
            <User class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              v-model="formData.name" 
              type="text" 
              placeholder="Full Name" 
              required 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- Email -->
          <div class="relative">
            <Mail class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              v-model="formData.email" 
              type="email" 
              placeholder="Email Address" 
              required 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- Phone (Signup only) -->
          <div v-if="!isLogin" class="relative">
            <Phone class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              v-model="formData.phone" 
              type="tel" 
              placeholder="Phone Number" 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- City/Town (Signup only) -->
          <div v-if="!isLogin" class="relative">
            <MapPin class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              v-model="formData.city_town" 
              type="text" 
              placeholder="City/Town" 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- Country (Signup only) -->
          <div v-if="!isLogin" class="relative">
            <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <input 
              v-model="formData.country" 
              type="text" 
              placeholder="Country" 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- Password -->
          <div class="relative">
            <Lock class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input 
              v-model="formData.password" 
              type="password" 
              placeholder="Password" 
              required 
              class="w-full pl-10 pr-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
            />
          </div>

          <!-- Role Selector (Signup only) -->
          <div v-if="!isLogin" class="grid grid-cols-2 gap-3">
            <button 
              type="button"
              @click="formData.role = 'user'"
              :class="[
                'p-3 rounded-xl border-2 flex items-center justify-center gap-2 transition font-medium',
                formData.role === 'user' 
                  ? 'border-primary bg-primary/5 text-primary' 
                  : 'border-gray-200 text-gray-500 hover:border-gray-300'
              ]"
            >
              <Home class="w-5 h-5" /> Customer
            </button>
            <button 
              type="button"
              @click="formData.role = 'provider'"
              :class="[
                'p-3 rounded-xl border-2 flex items-center justify-center gap-2 transition font-medium',
                formData.role === 'provider' 
                  ? 'border-highlight bg-highlight/5 text-secondary' 
                  : 'border-gray-200 text-gray-500 hover:border-gray-300'
              ]"
            >
              <Briefcase class="w-5 h-5" /> Provider
            </button>
          </div>

          <!-- Submit Button -->
          <button 
            type="submit" 
            :disabled="isLoading"
            class="w-full py-3 bg-primary text-white font-semibold rounded-xl hover:opacity-90 transition shadow-lg shadow-primary/20 flex items-center justify-center gap-2 disabled:opacity-50 mt-2"
          >
            <span v-if="isLoading">Processing...</span>
            <span v-else>{{ isLogin ? 'Sign In' : 'Create Account' }}</span>
            <ArrowRight v-if="!isLoading" class="w-5 h-5" />
          </button>
        </form>

        <!-- Toggle Login/Signup -->
        <p class="text-center text-gray-500 mt-6">
          {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
          <button @click="toggleMode" class="text-primary font-semibold hover:underline ml-1">
            {{ isLogin ? 'Sign up' : 'Log in' }}
          </button>
        </p>
      </div>
    </div>
  </div>
</template>