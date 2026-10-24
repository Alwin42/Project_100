<script setup>
import { ref, computed } from 'vue'
import Navbar from '../components/Navbar.vue'
import { 
  Search, SlidersHorizontal, Star, MapPin, Briefcase, 
  Wrench, SprayCan, Zap, GraduationCap, Paintbrush, Hammer, Home
} from 'lucide-vue-next'

// Import dummy data
import servicesData from '../data/services.json'

// State
const searchQuery = ref('')
const selectedCategory = ref('All')
const sortBy = ref('rating')

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

// Computed property for filtering and sorting
const filteredServices = computed(() => {
  let results = [...servicesData]

  // 1. Filter by Category
  if (selectedCategory.value !== 'All') {
    results = results.filter(service => service.category === selectedCategory.value)
  }

  // 2. Filter by Search Query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    results = results.filter(service => 
      service.serviceTitle.toLowerCase().includes(query) ||
      service.providerName.toLowerCase().includes(query) ||
      service.location.toLowerCase().includes(query)
    )
  }

  // 3. Sort
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

// Dummy user name (In a real app, this comes from your Auth Store/Context)
const userName = 'Alwin' 
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- 1. Welcome Note -->
      <div class="mb-10">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-900">
          Welcome back, <span class="text-primary">{{ userName }}</span>
        </h1>
        <p class="text-gray-500 mt-2 text-lg">Find the best local professionals for your next project.</p>
      </div>

      <!-- 4. Categories (Quick Filters) -->
      <div class="mb-8">
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

      <!-- 2. Search, Filter & Sort Bar -->
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
        
        <!-- Sort Dropdown -->
        <div class="flex items-center gap-2 px-4 py-2 bg-gray-50 rounded-xl md:w-64">
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

      <!-- 3. Profile Cards for Recent Works / Providers -->
      <div v-if="filteredServices.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="service in filteredServices" 
          :key="service.id"
          class="bg-white border border-gray-100 rounded-2xl p-6 hover:border-primary/20 hover:shadow-lg hover:shadow-primary/5 transition-all duration-300 group"
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
        <button @click="searchQuery = ''; selectedCategory = 'All'" class="mt-4 px-4 py-2 text-primary font-medium hover:bg-primary/5 rounded-lg transition">
          Clear Filters
        </button>
      </div>

    </main>
  </div>
</template>

<style scoped>
/* Hide scrollbar for Chrome, Safari and Opera */
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}
/* Hide scrollbar for IE, Edge and Firefox */
.scrollbar-hide {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>