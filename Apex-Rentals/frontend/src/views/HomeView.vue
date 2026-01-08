<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 1. Create a variable to hold our list of cars
const cars = ref([])
const error = ref(null)

// 2. Define the Base URL for your Backend
// (This handles the issue where the image path is just "/media/..." without the domain)
const API_URL = "http://127.0.0.1:8000"

// 3. When the component loads, go get the data
onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/api/cars/`)
    cars.value = response.data
    console.log("Data loaded:", cars.value)
  } catch (err) {
    error.value = "Failed to load cars. Is the backend running?"
    console.error(err)
  }
})

// 4. Helper function to fix image URLs
// Django sends "/media/img.png", but we need "http://localhost:8000/media/img.png"
const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/300x200?text=No+Image"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div class="home-container">
    <h1>Available Cars</h1>

    <div v-if="error" class="error-msg">{{ error }}</div>

    <div v-else-if="cars.length === 0">Loading cars...</div>

    <div v-else class="car-grid">
      <div class="car-card" v-for="car in cars" :key="car.id">
        
        <img 
          :src="getImageUrl(car.image)" 
          :alt="car.model" 
          class="car-image"
        />

        <h3>{{ car.year }} {{ car.make }} {{ car.model }}</h3>
        <p class="price">₹{{ car.price_per_day }} / day</p>
        
        <span 
          class="status" 
          :class="{ available: car.is_available, booked: !car.is_available }"
        >
          {{ car.is_available ? 'Available' : 'Booked' }}
        </span>

        <router-link :to="{ name: 'details', params: { id: car.id } }">
            <button :disabled="!car.is_available">
              {{ car.is_available ? 'Rent Now' : 'Unavailable' }}
            </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container { padding: 20px; }
.error-msg { color: red; font-weight: bold; }
.car-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); 
  gap: 20px; 
}
.car-card { 
  border: 1px solid #ddd; 
  border-radius: 8px; 
  overflow: hidden;
  transition: transform 0.2s;
  background: white;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.car-card:hover { transform: translateY(-5px); }
.car-image { 
  width: 100%; 
  height: 180px; 
  object-fit: cover; 
}
h3 { margin: 10px; font-size: 1.2rem; }
.price { color: #2c3e50; font-weight: bold; margin: 0 10px 10px; }
button { 
  width: 100%; 
  padding: 12px; 
  border: none; 
  background: #007bff; 
  color: white; 
  font-weight: bold; 
  cursor: pointer;
}
button:disabled { background: #ccc; cursor: not-allowed; }
.status {
  display: inline-block;
  margin: 0 10px 10px;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
}
.available { background: #e6fffa; color: #00b894; }
.booked { background: #ffe6e6; color: #d63031; }
</style>