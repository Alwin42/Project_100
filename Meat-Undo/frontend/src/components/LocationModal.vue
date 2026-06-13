<template>
  <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-xs">
    <div class="bg-white w-full max-w-md rounded-3xl p-6 shadow-xl border border-gray-100 mx-4">
      
      <div class="flex justify-between items-center mb-6">
        <h3 class="text-xl font-bold text-gray-900">Select Delivery Location</h3>
        <button @click="$emit('close')" class="text-gray-400 hover:text-gray-600 font-bold text-lg">✕</button>
      </div>

      <button 
        @click="getCurrentLocation" 
        :disabled="isLocating"
        class="w-full mb-4 py-3 px-4 bg-primary/5 hover:bg-primary/10 text-primary font-bold rounded-2xl flex items-center justify-center gap-2 transition-all text-sm disabled:opacity-50"
      >
        <span>📍</span>
        {{ isLocating ? 'Detecting location...' : 'Use Current Location' }}
      </button>

      <div class="relative flex py-2 items-center text-gray-400 text-xs my-2">
        <div class="grow border-t border-gray-200"></div>
        <span class="mx-3 font-semibold">OR SELECT REGION</span>
        <div class="grow border-t border-gray-200"></div>
      </div>

      <div class="space-y-2 max-h-48 overflow-y-auto mb-6 pr-1">
        <button 
          v-for="loc in popularLocations" 
          :key="loc"
          @click="selectLocation(loc)"
          class="w-full text-left py-3 px-4 hover:bg-gray-50 rounded-xl font-medium text-gray-700 transition-colors text-sm border border-gray-100 flex items-center gap-2"
        >
          <span>🏢</span> {{ loc }}
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close', 'location-selected'])
const isLocating = ref(false)

// Customize these based on your local customer hubs
const popularLocations = ref([
  'Kochi City',
  'Kakkanad',
  'Edappally',
  'Aluva',
  'Tripunithura'
])

const selectLocation = (locationName) => {
  emit('location-selected', locationName)
  emit('close')
}

// Optional: Use browser Geolocation API
const getCurrentLocation = () => {
  if (!navigator.geolocation) {
    alert('Geolocation is not supported by your browser')
    return
  }

  isLocating.value = true
  navigator.geolocation.getCurrentPosition(
    (position) => {
      isLocating.value = false
      // In production, you'd reverse-geocode these lat/long coordinates using a map API.
      // For now, we save a placeholder indicating a coordinates match.
      const coordString = `Detected Location (${position.coords.latitude.toFixed(2)}, ${position.coords.longitude.toFixed(2)})`
      selectLocation(coordString)
    },
    (error) => {
      isLocating.value = false
      console.error(error)
      alert('Unable to retrieve your location. Please pick a region manually.')
    }
  )
}
</script>