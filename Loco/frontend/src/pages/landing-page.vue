<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'

// 1. Import the specific icons you need from lucide-vue-next
import { 
  Wrench, SprayCan, Zap, GraduationCap, Paintbrush, Hammer, 
  Search, CalendarCheck, CheckCircle2 
} from 'lucide-vue-next'

const serviceQuery = ref('')
const locationQuery = ref('')

// 2. Use the imported icon components in the data arrays
const categories = [
  { name: 'Plumbing', icon: Wrench, color: 'bg-primary/10 text-primary' },
  { name: 'Cleaning', icon: SprayCan, color: 'bg-highlight/10 text-secondary' },
  { name: 'Electrical', icon: Zap, color: 'bg-accent/20 text-secondary' },
  { name: 'Tutoring', icon: GraduationCap, color: 'bg-primary/10 text-primary' },
  { name: 'Painting', icon: Paintbrush, color: 'bg-highlight/10 text-secondary' },
  { name: 'Carpentry', icon: Hammer, color: 'bg-accent/20 text-secondary' },
]

const steps = [
  { title: 'Search', desc: 'Find the perfect local professional for your needs.', icon: Search },
  { title: 'Book', desc: 'Choose a time that works for you and book instantly.', icon: CalendarCheck },
  { title: 'Relax', desc: 'Sit back while our verified experts get the job done.', icon: CheckCircle2 },
]
</script>

<template>
  <div class="min-h-screen bg-white font-sans text-gray-800">
    
    <Navbar />

    <!-- Hero Section -->
    <section class="relative overflow-hidden bg-gradient-to-br from-primary via-secondary to-accent text-white">
      <div class="absolute top-0 right-0 w-96 h-96 bg-highlight/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
      <div class="absolute bottom-0 left-0 w-96 h-96 bg-accent/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
      
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 md:py-32 text-center">
        <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-6">
          Find Trusted Local <br class="hidden md:block" />
          <span class="text-highlight">Service Providers</span>
        </h1>
        <p class="text-lg md:text-xl text-blue-100 max-w-2xl mx-auto mb-10">
          Connect with verified professionals in your neighborhood. From plumbing to tutoring, get the job done right, every time.
        </p>

        <!-- Search Bar -->
        <div class="max-w-3xl mx-auto bg-white rounded-2xl p-2 shadow-2xl shadow-black/20 flex flex-col md:flex-row gap-2">
          <div class="flex-1 flex items-center gap-3 px-4 py-3 bg-gray-50 rounded-xl">
            <!-- Using Search icon directly here -->
            <Search class="w-5 h-5 text-gray-400" />
            <input v-model="serviceQuery" type="text" placeholder="What service do you need?" class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-400" />
          </div>
          <div class="flex-1 flex items-center gap-3 px-4 py-3 bg-gray-50 rounded-xl">
            <!-- Location pin icon -->
            <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            <input v-model="locationQuery" type="text" placeholder="Your location" class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-400" />
          </div>
          <button class="px-8 py-3 bg-highlight text-white font-bold rounded-xl hover:opacity-90 transition shadow-lg shadow-highlight/30 whitespace-nowrap">
            Search
          </button>
        </div>
      </div>
    </section>

    <!-- Popular Categories -->
    <section id="categories" class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Popular Services</h2>
          <p class="text-gray-600 text-lg">Browse our most requested local services</p>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
          <div v-for="cat in categories" :key="cat.name" 
               class="bg-white p-6 rounded-2xl text-center hover:shadow-xl transition-all duration-300 hover:-translate-y-1 cursor-pointer border border-gray-100">
            <!-- 3. Render the dynamic icon component -->
            <div class="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center" :class="cat.color">
              <component :is="cat.icon" class="w-8 h-8" />
            </div>
            <h3 class="font-semibold text-gray-800">{{ cat.name }}</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- How it Works -->
    <section id="how-it-works" class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">How Loco Works</h2>
          <p class="text-gray-600 text-lg">Getting help has never been easier</p>
        </div>

        <div class="grid md:grid-cols-3 gap-12">
          <div v-for="(step, index) in steps" :key="step.title" class="text-center relative">
            <div v-if="index < steps.length - 1" class="hidden md:block absolute top-12 left-[60%] w-[80%] h-0.5 bg-gradient-to-r from-primary to-highlight"></div>
            
            <div class="relative z-10 w-24 h-24 mx-auto mb-6 bg-gradient-to-br from-primary to-secondary text-white rounded-full flex items-center justify-center shadow-lg shadow-primary/20">
              <!-- Render the step icon, sized larger for this section -->
              <component :is="step.icon" class="w-12 h-12" />
            </div>
            <h3 class="text-xl font-bold text-primary mb-2">{{ step.title }}</h3>
            <p class="text-gray-600">{{ step.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Become a Provider CTA -->
    <section id="provider-cta" class="py-20 bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">Are You a Local Professional?</h2>
        <p class="text-blue-100 text-lg mb-8 max-w-2xl mx-auto">
          Join thousands of service providers on Loco. Grow your business, manage bookings easily, and reach more customers in your area.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <button class="px-8 py-4 bg-highlight text-white font-bold rounded-xl hover:opacity-90 transition shadow-lg shadow-black/20 text-lg">
            Start Providing Today
          </button>
          <button class="px-8 py-4 bg-white/10 backdrop-blur-sm border border-white/30 text-white font-bold rounded-xl hover:bg-white/20 transition text-lg">
            Learn More
          </button>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid md:grid-cols-4 gap-8 mb-8">
          <div>
            <div class="flex items-center gap-2 mb-4">
              
              <span class="text-2xl font-bold text-white">Loco</span>
            </div>
            <p class="text-sm">Connecting you with trusted local professionals for all your everyday needs.</p>
          </div>
          <div>
            <h4 class="text-white font-semibold mb-4">For Customers</h4>
            <ul class="space-y-2 text-sm">
              <li><a href="#" class="hover:text-highlight transition">Browse Services</a></li>
              <li><a href="#" class="hover:text-highlight transition">How it Works</a></li>
              <li><a href="#" class="hover:text-highlight transition">Pricing</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-white font-semibold mb-4">For Providers</h4>
            <ul class="space-y-2 text-sm">
              <li><a href="#" class="hover:text-highlight transition">Become a Pro</a></li>
              <li><a href="#" class="hover:text-highlight transition">Provider App</a></li>
              <li><a href="#" class="hover:text-highlight transition">Success Stories</a></li>
            </ul>
          </div>
          <div>
            <h4 class="text-white font-semibold mb-4">Company</h4>
            <ul class="space-y-2 text-sm">
              <li><a href="#" class="hover:text-highlight transition">About Us</a></li>
              <li><a href="#" class="hover:text-highlight transition">Contact</a></li>
              <li><a href="#" class="hover:text-highlight transition">Privacy Policy</a></li>
            </ul>
          </div>
        </div>
        <div class="border-t border-gray-800 pt-8 text-center text-sm">
          <p>&copy; {{ new Date().getFullYear() }} Loco. All rights reserved.</p>
        </div>
      </div>
    </footer>

  </div>
</template>