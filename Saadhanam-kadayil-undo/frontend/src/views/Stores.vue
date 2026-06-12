<template>
  <div class="min-h-screen bg-gray-50 font-sans pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="text-center mb-10">
        <h1 class="text-3xl md:text-5xl font-bold text-gray-900 tracking-tight mb-4">Find Stores Near You</h1>
        <p class="text-gray-500 font-medium max-w-xl mx-auto">Discover local vendors, fresh groceries, and daily essentials just a few minutes away.</p>
      </div>

      <div class="max-w-2xl mx-auto mb-16 animate-in fade-in slide-in-from-bottom-4 duration-700">
        <div class="relative group">
          <div class="absolute -inset-1 bg-linear-to-r from-primary/20 to-secondary/30 rounded-full blur opacity-0 group-hover:opacity-100 transition duration-500"></div>
          
          <div class="relative flex items-center bg-white rounded-full h-16 shadow-sm border border-gray-200 group-hover:border-primary/50 focus-within:border-primary focus-within:ring-4 focus-within:ring-primary/10 transition-all duration-300 px-6">
            <MapPinIcon class="w-6 h-6 text-gray-400 group-focus-within:text-primary transition-colors duration-300 shrink-0" />
            
            <input 
              v-model="userLocation"
              type="text" 
              placeholder="Enter your street or neighborhood (e.g. Kakkanad)" 
              class="bg-transparent grow pl-4 text-gray-800 placeholder-gray-400 focus:outline-none font-medium text-lg w-full"
            >
            
            <button 
              v-if="userLocation"
              @click="userLocation = ''"
              class="p-2 bg-gray-100 hover:bg-gray-200 text-gray-500 rounded-full transition-colors active:scale-95 shrink-0"
            >
              <XIcon class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      <div v-if="isLoading" class="text-center py-20 text-gray-400">
        <Loader2Icon class="w-10 h-10 animate-spin mx-auto mb-4 text-primary" />
        <p class="font-bold text-lg">Locating nearby stores...</p>
      </div>

      <div v-else>
        
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-bold text-gray-900">
            {{ userLocation ? `Stores around "${userLocation}"` : 'All Available Stores' }}
          </h2>
          <span class="text-sm font-bold text-primary bg-secondary/20 px-3 py-1 rounded-full">
            {{ filteredVendors.length }} found
          </span>
        </div>

        <div v-if="filteredVendors.length === 0" class="bg-white rounded-4xl border border-gray-100 p-16 text-center shadow-sm">
          <div class="w-20 h-20 bg-gray-50 rounded-full flex items-center justify-center mx-auto mb-4">
            <MapPinOffIcon class="w-8 h-8 text-gray-400" />
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-2">No stores found</h3>
          <p class="text-gray-500 font-medium">We couldn't find any vendors matching that location. Try searching a wider area!</p>
          <button @click="userLocation = ''" class="mt-6 text-primary font-bold hover:underline">Clear Search</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="vendor in filteredVendors" 
            :key="vendor._id"
            class="bg-white border border-gray-100 rounded-4xl p-6 shadow-sm hover:shadow-xl hover:shadow-secondary/10 hover:border-primary/30 transition-all duration-300 hover:-translate-y-1.5 flex flex-col group cursor-pointer"
          >
            <div class="flex items-start gap-5 mb-5">
              <div class="w-16 h-16 bg-secondary/10 group-hover:bg-primary rounded-2xl flex items-center justify-center shrink-0 transition-colors duration-500">
                <span class="text-3xl group-hover:scale-110 transition-transform duration-500">{{ vendor.emoji || '🏪' }}</span>
              </div>
              
              <div class="grow">
                <h3 class="text-xl font-bold text-gray-900 leading-tight group-hover:text-primary transition-colors duration-300">{{ vendor.shopName }}</h3>
                <div class="flex items-center gap-1 mt-1.5">
                  <StarIcon class="w-4 h-4 text-accent-2 fill-accent-2" />
                  <span class="text-sm font-bold text-gray-700">New Vendor</span>
                </div>
                
                <p class="text-sm text-gray-500 font-medium mt-2 flex items-start gap-1.5 line-clamp-2">
                  <MapPinIcon class="w-4 h-4 shrink-0 mt-0.5 text-gray-400" />
                  {{  vendor.address.state + ', ' + vendor.address.district + ', ' + vendor.address.area + ', ' + vendor.address.streetOrBuilding  || 'Address not provided' }}
                </p>
                
                <p v-if="vendor.openTime && vendor.closeTime" class="text-sm text-gray-500 font-medium mt-1.5 flex items-center gap-1.5">
                  <ClockIcon class="w-4 h-4 shrink-0 text-secondary" />
                  {{ formatTime(vendor.openTime) }} - {{ formatTime(vendor.closeTime) }}
                </p>
              </div>
            </div>

            <div class="mt-auto flex items-center justify-between pt-4 border-t border-gray-100">
              <span 
                class="text-xs font-bold px-3 py-1.5 rounded-full transition-colors duration-300" 
                :class="(vendor.isOpen ?? true) ? 'bg-secondary/20 text-primary' : 'bg-gray-100 text-gray-500'"
              >
                {{ (vendor.isOpen ?? true) ? 'Open Now' : 'Closed' }}
              </span>
              <a 
                v-if="vendor.mapUrl"
                :href="vendor.mapUrl" 
                target="_blank" 
                class="text-primary font-bold text-sm hover:underline flex items-center gap-1 hover:translate-x-1 transition-transform duration-300"
              >
                <StoreIcon class="w-4 h-4" />
                Visit Shop
              </a>
            </div>
          </div>
        </div>

      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import { MapPinIcon, XIcon, Loader2Icon, StarIcon, StoreIcon, MapPinOffIcon } from 'lucide-vue-next'
import { ClockIcon } from 'lucide-vue-next' 
const vendors = ref([])
const userLocation = ref('')
const isLoading = ref(true)


const formatTime = (time24) => {
  if (!time24) return '';
  const [hour, minute] = time24.split(':');
  const h = parseInt(hour, 10);
  const ampm = h >= 12 ? 'PM' : 'AM';
  const h12 = h % 12 || 12;
  return `${h12}:${minute} ${ampm}`;
}

// Fetch all vendors from the database on page load
onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:3000/api/public/vendors');
    if (response.data.success) {
      vendors.value = response.data.vendors;
    }
  } catch (error) {
    console.error("Failed to load stores:", error);
  } finally {
    isLoading.value = false;
  }
})

// INSTANT SEARCH FILTER: Matches the typed location against the vendor's address
const filteredVendors = computed(() => {
  if (!userLocation.value) return vendors.value;
  
  const query = userLocation.value.toLowerCase().trim();
  
  return vendors.value.filter(vendor => {
    // Safely check if the address exists, then check if it includes the query
    const address = vendor.address ? vendor.address.toLowerCase() : '';
    const name = vendor.shopName ? vendor.shopName.toLowerCase() : '';
    
    return address.includes(query) || name.includes(query);
  });
})
</script>