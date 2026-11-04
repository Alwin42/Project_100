<script setup>
import { ref, computed } from 'vue'
import Navbar from '../components/Navbar.vue'
import { useRouter } from 'vue-router'
import { 
  Search, SlidersHorizontal, Star, MapPin, Briefcase, Clock,
  Wrench, SprayCan, Zap, GraduationCap, Paintbrush, Hammer, Home,
  Filter, ChevronDown, Heart, Share2
} from 'lucide-vue-next'

// Import dummy data
import servicesData from '../data/services.json'

const router = useRouter()

// State
const searchQuery = ref('')
const selectedCategory = ref('All')
const sortBy = ref('rating')
const priceRange = ref('all')
const selectedService = ref(null)

// Categories configuration
const categories = [
  { name: 'All', icon: Home },
  { name: 'Plumbing', icon: Wrench },
  { name: 'Cleaning', icon: SprayCan },
  { name: 'Electrical', icon: Zap },
  { name: 'Tutoring', icon: GraduationCap },
  { name: 'Painting', icon: Paintbrush },
  { name: 'Construction', icon: Hammer },
]

// Filter and sort services
const filteredServices = computed(() => {
  let results = [...servicesData]

  // Filter by Category
  if (selectedCategory.value !== 'All') {
    results = results.filter(service => service.category === selectedCategory.value)
  }

  // Filter by Search Query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    results = results.filter(service => 
      service.serviceTitle.toLowerCase().includes(query) ||
      service.providerName.toLowerCase().includes(query) ||
      service.location.toLowerCase().includes(query)
    )
  }

  // Filter by Price Range
  if (priceRange.value === 'low') {
    results = results.filter(service => service.price < 100)
  } else if (priceRange.value === 'mid') {
    results = results.filter(service => service.price >= 100 && service.price < 300)
  } else if (priceRange.value === 'high') {
    results = results.filter(service => service.price >= 300)
  }

  // Sort
  if (sortBy.value === 'price-low') {
    results.sort((a, b) => a.price - b.price)
  } else if (sortBy.value === 'price-high') {
    results.sort((a, b) => b.price - a.price)
  } else if (sortBy.value === 'rating') {
    results.sort((a, b) => b.rating - a.rating)
  } else if (sortBy.value === 'jobs') {
    results.sort((a, b) => b.completedJobs - a.completedJobs)
  }

  return results
})

const selectService = (service) => {
  selectedService.value = service
}

const bookService = () => {
  if (selectedService.value) {
    router.push('/dashboard')
  }
}

const closeServiceDetail = () => {
  selectedService.value = null
}
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- Page Header -->
      <div class="mb-8">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-900">Browse Services</h1>
        <p class="text-gray-500 mt-2 text-lg">Find and book trusted local professionals</p>
      </div>

      <!-- Categories -->
      <div class="mb-6">
        <div class="flex gap-3 overflow-x-auto pb-2 scrollbar-hide">
          <button
            v-for="cat in categories"
            :key="cat.name"
            @click="selectedCategory = cat.name"
            :class="[
              'flex items-center gap-2 px-5 py-2.5 rounded-full text-sm font-medium whitespace-nowrap transition-all border',
              selectedCategory === cat.name 
                ? 'bg-primary text-white border-primary shadow-sm shadow-primary/20' 
                : 'bg-white text-gray-600 border-gray-200 hover:border-primary/30 hover:text-primary'
            ]"
          >
            <component :is="cat.icon" class="w-4 h-4" />
            {{ cat.name }}
          </button>
        </div>
      </div>

      <!-- Search, Filter & Sort Bar -->
      <div class="bg-white border border-gray-200 rounded-2xl p-3 mb-8 flex flex-col md:flex-row gap-3 shadow-sm">
        <!-- Search Input -->
        <div class="flex-1 flex items-center gap-3 px-4 py-2 bg-gray-50 rounded-xl">
          <Search class="w-5 h-5 text-gray-400 flex-shrink-0" />
          <input 
            v-model="searchQuery" 
            type="text" 
            placeholder="Search services, providers, or locations..." 
            class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-400 text-sm"
          />
        </div>
        
        <!-- Price Filter -->
        <div class="flex items-center gap-2 px-4 py-2 bg-gray-50 rounded-xl md:w-48">
          <Filter class="w-5 h-5 text-gray-400 flex-shrink-0" />
          <select 
            v-model="priceRange" 
            class="w-full bg-transparent outline-none text-gray-700 text-sm font-medium cursor-pointer"
          >
            <option value="all">All Prices</option>
            <option value="low">Under $100</option>
            <option value="mid">$100 - $300</option>
            <option value="high">$300+</option>
          </select>
        </div>

        <!-- Sort Dropdown -->
        <div class="flex items-center gap-2 px-4 py-2 bg-gray-50 rounded-xl md:w-56">
          <SlidersHorizontal class="w-5 h-5 text-gray-400 flex-shrink-0" />
          <select 
            v-model="sortBy" 
            class="w-full bg-transparent outline-none text-gray-700 text-sm font-medium cursor-pointer"
          >
            <option value="rating">Top Rated</option>
            <option value="jobs">Most Experienced</option>
            <option value="price-low">Price: Low to High</option>
            <option value="price-high">Price: High to Low</option>
          </select>
        </div>
      </div>

      <!-- Results Count -->
      <div class="flex items-center justify-between mb-6">
        <h2 class="text-xl font-bold text-gray-900">
          {{ selectedCategory === 'All' ? 'All Services' : selectedCategory }} 
          <span class="text-gray-400 font-normal text-base ml-2">({{ filteredServices.length }} found)</span>
        </h2>
      </div>

      <!-- Services Grid -->
      <div v-if="filteredServices.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="service in filteredServices" 
          :key="service.id"
          @click="selectService(service)"
          class="bg-white border border-gray-100 rounded-2xl p-6 hover:border-primary/20 hover:shadow-lg hover:shadow-primary/5 transition-all duration-300 group cursor-pointer"
        >
          <!-- Header: Avatar & Info -->
          <div class="flex items-start justify-between mb-4">
            <div class="flex items-center gap-3">
              <!-- Profile Avatar -->
              <div class="w-12 h-12 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white font-bold text-sm shadow-sm">
                {{ service.initials }}
              </div>
              <div>
                <h3 class="font-bold text-gray-900 group-hover:text-primary transition-colors">{{ service.providerName }}</h3>
                <p class="text-xs text-gray-500 flex items-center gap-1 mt-0.5">
                  <MapPin class="w-3 h-3" /> {{ service.location }}
                </p>
              </div>
            </div>
            <!-- Category Tag -->
            <span class="px-2.5 py-1 bg-gray-100 text-gray-600 text-xs font-medium rounded-full">
              {{ service.category }}
            </span>
          </div>

          <!-- Service Title -->
          <h4 class="text-lg font-semibold text-gray-800 mb-4">{{ service.serviceTitle }}</h4>

          <!-- Stats Row -->
          <div class="flex items-center justify-between pt-4 border-t border-gray-100">
            <div class="flex items-center gap-4 text-sm text-gray-500">
              <span class="flex items-center gap-1 font-medium text-gray-700">
                <Star class="w-4 h-4 text-yellow-500 fill-yellow-500" /> {{ service.rating }}
              </span>
              <span class="flex items-center gap-1">
                <Briefcase class="w-4 h-4" /> {{ service.completedJobs }} jobs
              </span>
            </div>
            <div class="text-right">
              <span class="text-lg font-bold text-primary">${{ service.price }}</span>
              <span class="text-xs text-gray-400 block">starting</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-20 bg-white rounded-2xl border border-gray-100">
        <Search class="w-12 h-12 text-gray-300 mx-auto mb-4" />
        <h3 class="text-xl font-semibold text-gray-800 mb-2">No services found</h3>
        <p class="text-gray-500">Try adjusting your search or filters to find what you're looking for.</p>
        <button @click="searchQuery = ''; selectedCategory = 'All'; priceRange = 'all'" class="mt-4 px-4 py-2 text-primary font-medium hover:bg-primary/5 rounded-lg transition">
          Clear Filters
        </button>
      </div>

    </main>

    <!-- Service Detail Modal -->
    <div v-if="selectedService" class="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4" @click="closeServiceDetail">
      <div class="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto" @click.stop>
        
        <!-- Modal Header -->
        <div class="sticky top-0 bg-white border-b border-gray-100 px-6 py-4 flex items-center justify-between">
          <h2 class="text-xl font-bold text-gray-900">Service Details</h2>
          <button @click="closeServiceDetail" class="p-2 hover:bg-gray-100 rounded-lg transition">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Modal Content -->
        <div class="p-6">
          <!-- Provider Info -->
          <div class="flex items-start gap-4 mb-6">
            <div class="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-secondary flex items-center justify-center text-white font-bold text-xl shadow-sm">
              {{ selectedService.initials }}
            </div>
            <div class="flex-1">
              <h3 class="text-xl font-bold text-gray-900">{{ selectedService.providerName }}</h3>
              <p class="text-sm text-gray-500 flex items-center gap-1 mt-1">
                <MapPin class="w-4 h-4" /> {{ selectedService.location }}
              </p>
              <div class="flex items-center gap-4 mt-2">
                <span class="flex items-center gap-1 text-sm font-medium text-gray-700">
                  <Star class="w-4 h-4 text-yellow-500 fill-yellow-500" /> {{ selectedService.rating }} rating
                </span>
                <span class="flex items-center gap-1 text-sm text-gray-500">
                  <Briefcase class="w-4 h-4" /> {{ selectedService.completedJobs }} jobs completed
                </span>
              </div>
            </div>
          </div>

          <!-- Service Details -->
          <div class="bg-gray-50 rounded-xl p-5 mb-6">
            <h4 class="text-lg font-semibold text-gray-900 mb-2">{{ selectedService.serviceTitle }}</h4>
            <span class="inline-block px-3 py-1 bg-primary/10 text-primary text-sm font-medium rounded-full mb-4">
              {{ selectedService.category }}
            </span>
            <p class="text-gray-600 text-sm leading-relaxed">
              Professional {{ selectedService.category.toLowerCase() }} services with years of experience. 
              Quality workmanship guaranteed with customer satisfaction as top priority.
            </p>
          </div>

          <!-- What's Included -->
          <div class="mb-6">
            <h4 class="text-lg font-semibold text-gray-900 mb-3">What's Included</h4>
            <ul class="space-y-2">
              <li class="flex items-start gap-2 text-sm text-gray-600">
                <svg class="w-5 h-5 text-highlight flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                Professional service with certified expertise
              </li>
              <li class="flex items-start gap-2 text-sm text-gray-600">
                <svg class="w-5 h-5 text-highlight flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                Quality materials and equipment included
              </li>
              <li class="flex items-start gap-2 text-sm text-gray-600">
                <svg class="w-5 h-5 text-highlight flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                Satisfaction guarantee and follow-up support
              </li>
            </ul>
          </div>

          <!-- Pricing -->
          <div class="bg-primary/5 border border-primary/10 rounded-xl p-5 mb-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm text-gray-600 mb-1">Starting Price</p>
                <p class="text-3xl font-bold text-primary">${{ selectedService.price }}</p>
              </div>
              <div class="text-right">
                <p class="text-sm text-gray-600 mb-1">Estimated Time</p>
                <p class="text-lg font-semibold text-gray-900 flex items-center gap-1">
                  <Clock class="w-4 h-4" /> 2-4 hours
                </p>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="flex gap-3">
            <button 
              @click="bookService"
              class="flex-1 px-6 py-3 bg-highlight text-white font-semibold rounded-xl hover:opacity-90 transition shadow-sm flex items-center justify-center gap-2"
            >
              Book Now
            </button>
            <button class="px-4 py-3 border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition">
              <Heart class="w-5 h-5" />
            </button>
            <button class="px-4 py-3 border border-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-50 transition">
              <Share2 class="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
.scrollbar-hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>