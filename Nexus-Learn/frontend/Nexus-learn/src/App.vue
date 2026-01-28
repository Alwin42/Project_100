<template>
  <div class="min-h-screen bg-slate-50 font-sans antialiased">
    
    <Navbar />

    <main class="container mx-auto py-6 px-4">
      <router-view />
    </main>
    
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue';
</script>

<style>

</style>