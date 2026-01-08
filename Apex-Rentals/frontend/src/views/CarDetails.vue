<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const car = ref(null)
const API_URL = "http://127.0.0.1:8000"

onMounted(async () => {
  // Get the ID from the URL (e.g., /cars/1 -> id is 1)
  const carId = route.params.id
  try {
    const response = await axios.get(`${API_URL}/api/cars/${carId}/`)
    car.value = response.data
  } catch (err) {
    console.error("Error fetching car:", err)
  }
})

const getImageUrl = (imagePath) => {
  if (!imagePath) return "https://via.placeholder.com/600x400"
  if (imagePath.startsWith("http")) return imagePath
  return `${API_URL}${imagePath}`
}
</script>

<template>
  <div v-if="car" class="details-container">
    <div class="image-section">
      <img :src="getImageUrl(car.image)" :alt="car.model" />
    </div>
    
    <div class="info-section">
      <h1>{{ car.year }} {{ car.make }} {{ car.model }}</h1>
      <p class="price">₹{{ car.price_per_day }} <span>/ day</span></p>
      
      <div class="specs">
        <p><strong>Status:</strong> {{ car.is_available ? 'Available' : 'Booked' }}</p>
      </div>

      <button class="book-btn">Confirm Booking</button>
      <router-link to="/" class="back-link">← Back to Fleet</router-link>
    </div>
  </div>

  <div v-else class="loading">Loading details...</div>
</template>

<style scoped>
.details-container {
  display: flex;
  gap: 40px;
  max-width: 1000px;
  margin: 40px auto;
  padding: 20px;
}
.image-section img {
  width: 100%;
  max-width: 500px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.info-section h1 { font-size: 2.5rem; margin-bottom: 10px; }
.price { font-size: 1.8rem; color: #007bff; font-weight: bold; }
.price span { font-size: 1rem; color: #666; font-weight: normal; }
.book-btn {
  background: #28a745;
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.1rem;
  border-radius: 8px;
  cursor: pointer;
  margin-top: 20px;
  width: 100%;
}
.back-link { display: block; margin-top: 20px; text-decoration: none; color: #666; }
</style>