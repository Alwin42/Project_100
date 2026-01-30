<template>
  <div class="min-h-screen font-sans bg-nexus-main antialiased">
    
    <Navbar v-if="$route.name !== 'landing'" />

    <main>
      <router-view />
    </main>
    
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
import { useRoute } from 'vue-router'; 

// No extra logic needed, $route is available in template
</script>