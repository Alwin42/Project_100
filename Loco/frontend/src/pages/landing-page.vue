<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'

import { 
  Wrench, SprayCan, Zap, GraduationCap, Paintbrush, Hammer, 
  Search, MapPin, ArrowRight
} from 'lucide-vue-next'

const serviceQuery = ref('')
const locationQuery = ref('')

const categories = [
  { name: 'Plumbing', icon: Wrench },
  { name: 'Cleaning', icon: SprayCan },
  { name: 'Electrical', icon: Zap },
  { name: 'Tutoring', icon: GraduationCap },
  { name: 'Painting', icon: Paintbrush },
  { name: 'Carpentry', icon: Hammer },
]

const steps = [
  { num: '01', title: 'Search', desc: 'Browse verified local professionals for your specific needs.' },
  { num: '02', title: 'Book', desc: 'Select a time that works for you and confirm instantly.' },
  { num: '03', title: 'Relax', desc: 'Sit back while our trusted experts get the job done right.' },
]
</script>

<template>
  <div class="min-h-screen bg-white font-sans text-gray-900 antialiased">
    <Navbar />

    <!-- Hero Section -->
    <section class="relative pt-20 pb-24 md:pt-32 md:pb-32">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-6xl font-bold tracking-tight text-primary mb-6">
          Local services, <br class="hidden md:block" />
          <span class="text-gray-900">simplified.</span>
        </h1>
        <p class="text-lg md:text-xl text-gray-500 max-w-2xl mx-auto mb-12 font-medium">
          Connect with trusted professionals in your neighborhood. Quality help, right around the corner.
        </p>

        <!-- Search Bar -->
        <div class="max-w-2xl mx-auto bg-white border border-gray-200 rounded-2xl p-2 flex flex-col sm:flex-row gap-2 shadow-sm">
          <div class="flex-1 flex items-center gap-3 px-4 py-2">
            <Search class="w-5 h-5 text-gray-400 flex-shrink-0" />
            <input v-model="serviceQuery" type="text" placeholder="What service do you need?" class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-400" />
          </div>
          <div class="flex-1 flex items-center gap-3 px-4 py-2 border-t sm:border-t-0 sm:border-l border-gray-100">
            <MapPin class="w-5 h-5 text-gray-400 flex-shrink-0" />
            <input v-model="locationQuery" type="text" placeholder="Your location" class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-400" />
          </div>
          <button class="px-6 py-3 bg-primary text-white font-semibold rounded-xl hover:bg-primary/90 transition flex items-center justify-center gap-2">
            Search
            <ArrowRight class="w-4 h-4" />
          </button>
        </div>
      </div>
    </section>

    <!-- Popular Categories -->
    <section id="categories" class="py-20 border-t border-gray-100">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Popular Services</h2>
          <p class="text-gray-500 text-lg">Browse our most requested local professionals</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div v-for="cat in categories" :key="cat.name" 
               class="group p-6 rounded-2xl text-center border border-gray-100 hover:border-primary/20 hover:bg-primary/5 transition-all duration-300 cursor-pointer">
            <div class="w-12 h-12 mx-auto mb-4 rounded-xl bg-gray-50 group-hover:bg-primary/10 flex items-center justify-center transition-colors">
              <component :is="cat.icon" class="w-6 h-6 text-gray-600 group-hover:text-primary transition-colors" />
            </div>
            <h3 class="font-medium text-gray-800 group-hover:text-primary transition-colors">{{ cat.name }}</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- How it Works -->
    <section id="how-it-works" class="py-20 border-t border-gray-100 bg-gray-50/50">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">How it works</h2>
          <p class="text-gray-500 text-lg">Three simple steps to get things done</p>
        </div>

        <div class="grid md:grid-cols-3 gap-12">
          <div v-for="step in steps" :key="step.num" class="text-center md:text-left">
            <!-- Minimalist large faint numbers instead of heavy gradient circles -->
            <div class="text-5xl font-bold text-primary/10 mb-4">{{ step.num }}</div>
            <h3 class="text-xl font-bold text-gray-900 mb-2">{{ step.title }}</h3>
            <p class="text-gray-500 leading-relaxed">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Become a Provider CTA -->
    <section id="provider-cta" class="py-20 border-t border-gray-100">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <!-- Subtle tinted box instead of a heavy gradient -->
        <div class="bg-primary/5 border border-primary/10 rounded-3xl p-10 md:p-16 text-center">
          <h2 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">Grow your local business</h2>
          <p class="text-gray-600 text-lg mb-8 max-w-xl mx-auto">
            Join thousands of service providers on Loco. Manage bookings, reach more customers, and simplify your workflow.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <!-- Highlight color used sparingly for the main CTA -->
            <button class="px-8 py-3 bg-highlight text-white font-semibold rounded-xl hover:opacity-90 transition shadow-sm">
              Start Providing Today
            </button>
            <button class="px-8 py-3 bg-white border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition">
              Learn More
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-gray-100 py-12">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-4 gap-8 mb-12">
          <div>
            <div class="flex items-center gap-2 mb-4">
              <span class="text-2xl font-bold text-primary">Loco</span>
            </div>
            <p class="text-sm text-gray-500">Connecting you with trusted local professionals for all your everyday needs.</p>
          </div>
          <div>
            <h4 class="text-gray-900 font-semibold mb-4 text-sm uppercase tracking-wider">Customers</h4>
            <ul class="space-y-3 text-sm">
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Browse Services</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">How it Works</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Pricing</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-gray-900 font-semibold mb-4 text-sm uppercase tracking-wider">Providers</h4>
            <ul class="space-y-3 text-sm">
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Become a Pro</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Provider App</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Success Stories</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-gray-900 font-semibold mb-4 text-sm uppercase tracking-wider">Company</h4>
            <ul class="space-y-3 text-sm">
              <li><a href="#" class="text-gray-500 hover:text-primary transition">About Us</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Contact</a></li>
              <li><a href="#" class="text-gray-500 hover:text-primary transition">Privacy Policy</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-100 pt-8 text-center text-sm text-gray-400">
          <p>&copy; {{ new Date().getFullYear() }} Loco. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>