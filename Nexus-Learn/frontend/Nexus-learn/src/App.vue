<script setup>
import { onMounted, onUnmounted } from 'vue'
import Navbar from './components/Navbar.vue'
import Lenis from 'lenis'

let lenis

onMounted(() => {
  lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    smoothWheel: true,
  })

  function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
  }
  requestAnimationFrame(raf)
})

onUnmounted(() => {
  if (lenis) lenis.destroy()
})
</script>

<template>
  <div class="min-h-screen font-sans bg-[#09090b] text-white antialiased selection:bg-nexus-accent selection:text-black">
    <Navbar v-if="$route.name !== 'landing'" />
    <main>
      <router-view />
    </main>
  </div>
</template>

<style>
html, body {
  width: 100%;
  overflow-x: hidden; 
  background-color: #09090b;
  margin: 0;
  padding: 0;
}

::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: #09090b;
}

::-webkit-scrollbar-thumb {
  background-color: #333;
  border-radius: 5px;
  border: 2px solid #09090b;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #22c55e;
}

html {
  scrollbar-width: thin;
  scrollbar-color: #333 #09090b;
}
</style>