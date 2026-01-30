<script setup>
import { Button } from '@/components/ui/button'
import Navbar from '@/components/Navbar.vue' 
import { ArrowRightIcon, CheckIcon } from '@radix-icons/vue'
import HeroGraphic from '@/components/HeroGraphic.vue'
</script>

<template>
  <div class="min-h-screen bg-nexus-main text-white overflow-hidden">
    
    <Navbar />

    <main class="container mx-auto px-6 pt-10 lg:pt-20 grid lg:grid-cols-2 gap-12 items-center">
      
      <div class="space-y-8"
           v-motion
           :initial="{ opacity: 0, x: -100 }"
           :enter="{ opacity: 1, x: 0, transition: { duration: 800, delay: 200 } }"
      >
        <h1 class="text-5xl lg:text-7xl font-extrabold tracking-tight leading-tight">
          Boost Your <br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-blue-500 animate-gradient">
            Academic Life
          </span>
        </h1>

        <p class="text-xl text-gray-400 max-w-lg leading-relaxed">
          The all-in-one digital workspace for students. Organize tasks, track attendance, and manage projects with a hacker-style interface.
        </p>

        <div class="flex flex-col sm:flex-row gap-4">
          <router-link to="/register">
            <Button class="h-12 px-8 text-lg bg-nexus-accent text-black font-bold hover:scale-105 transition-transform duration-200">
              Register Now
              <ArrowRightIcon class="ml-2 h-5 w-5" />
            </Button>
          </router-link>
          
        </div>

        <div class="pt-8 flex items-center gap-6 text-gray-500 text-sm">
          <div class="flex items-center gap-2">
            <CheckIcon class="text-nexus-accent" /> Secure
          </div>
          <div class="flex items-center gap-2">
            <CheckIcon class="text-nexus-accent" /> Reliable 
          </div>
        </div>
      </div>

      <div class="relative flex justify-center lg:justify-end"
           v-motion
           :initial="{ opacity: 0, scale: 0.8 }"
           :enter="{ opacity: 1, scale: 1, transition: { duration: 800, delay: 400 } }"
      >
       
        
        <div class="relative flex justify-center lg:justify-end">
        <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[400px] h-[400px]  rounded-full  pointer-events-none"></div>
        
        <HeroGraphic />
      </div>
      </div>

    </main>

    <section class="backdrop-blur-sm py-12">
      <div class="container mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 px-6 text-center">
        
        <div v-motion-slide-visible-once-bottom class="space-y-3 p-4 rounded-xl hover:bg-white/5 transition-colors cursor-default">
          <div class="mx-auto h-12 w-12 bg-gray-800 rounded-lg flex items-center justify-center text-2xl">📝</div>
          <h3 class="text-xl font-bold text-white">Smart Tasks</h3>
          <p class="text-gray-400">Prioritize assignments with our drag-and-drop Kanban board.</p>
        </div>

        <div v-motion-slide-visible-once-bottom :delay="200" class="space-y-3 p-4 rounded-xl hover:bg-white/5 transition-colors cursor-default">
          <div class="mx-auto h-12 w-12 bg-gray-800 rounded-lg flex items-center justify-center text-2xl">📅</div>
          <h3 class="text-xl font-bold text-white">Auto Timetable</h3>
          <p class="text-gray-400">Never miss a class. Syncs with your college schedule automatically.</p>
        </div>

        <div v-motion-slide-visible-once-bottom :delay="400" class="space-y-3 p-4 rounded-xl hover:bg-white/5 transition-colors cursor-default">
          <div class="mx-auto h-12 w-12 bg-gray-800 rounded-lg flex items-center justify-center text-2xl">☁️</div>
          <h3 class="text-xl font-bold text-white">Secure Cloud</h3>
          <p class="text-gray-400">Store notes and syllabus copies safely. Accessible anywhere.</p>
        </div>

      </div>
    </section>
  </div>
</template>

<style scoped>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
  100% { transform: translateY(0px); }
}

.animate-float {
  animation: float 6s ease-in-out infinite;
}
</style>