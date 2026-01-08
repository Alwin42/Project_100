<template>
  <nav class="navbar">
    <div class="logo">Apex Rentals</div>
    <div class="links">
      <router-link to="/">Home</router-link>
      <a href="#">Login</a>
    </div>
  </nav>

  <router-view></router-view> 
</template>

<style>
/* Global simple styles */
body { margin: 0; font-family: sans-serif; }
.navbar {
  background: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo { font-weight: bold; font-size: 1.2rem; }
.links a { color: white; text-decoration: none; margin-left: 15px; }
</style>