<template>
  <div class="home-container">
    <h1>Available Cars</h1>
    
    <div class="car-grid">
      <div class="car-card" v-for="n in 3" :key="n">
        <div class="car-image">🚗</div> <h3>Toyota Camry</h3>
        <p class="price">$50 / day</p>
        <button>Rent Now</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container { padding: 20px; }
.car-grid { display: flex; gap: 20px; flex-wrap: wrap; }
.car-card { 
  border: 1px solid #ccc; 
  padding: 15px; 
  border-radius: 8px; 
  width: 200px; 
  text-align: center;
}
.car-image { font-size: 50px; background: #f0f0f0; margin-bottom: 10px; }
button { background: #007bff; color: white; border: none; padding: 10px; cursor: pointer; }
</style>