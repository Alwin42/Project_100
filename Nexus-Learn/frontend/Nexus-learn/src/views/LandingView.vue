<script setup>
import { Button } from '@/components/ui/button'
import Navbar from '@/components/Navbar.vue' 
import { ArrowRightIcon, ArrowTopRightIcon } from '@radix-icons/vue'
import HeroGraphic from '@/components/HeroGraphic.vue'
</script>

<template>
  <div class="min-h-screen bg-[#09090b] text-white overflow-hidden relative selection:bg-nexus-accent selection:text-black">
    
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-nexus-accent/20 blur-[120px] rounded-full pointer-events-none opacity-40"></div>
    <div class="absolute bottom-0 right-0 w-[600px] h-[600px] bg-blue-600/10 blur-[120px] rounded-full pointer-events-none"></div>

    <Navbar />

    <main class="container mx-auto px-6 pt-20 lg:pt-32 pb-20 grid lg:grid-cols-2 gap-16 items-center relative z-10">
      
      <div class="space-y-8"
           v-motion
           :initial="{ opacity: 0, x: -50, filter: 'blur(10px)' }"
           :enter="{ opacity: 1, x: 0, filter: 'blur(0px)', transition: { duration: 800, type: 'spring' } }"
      >
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 backdrop-blur-md mb-2">
          <span class="w-2 h-2 rounded-full bg-nexus-accent animate-pulse"></span>
          <span class="text-xs font-medium text-gray-300 tracking-wide uppercase">Developed by Alwin</span>
        </div>
        
        <h1 class="text-6xl lg:text-8xl font-black tracking-tighter leading-[0.9]">
          NEXUS 
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent via-emerald-200 to-white">
            LEARN
          </span>
        </h1>
        <h1 class="text-6xl lg:text-8xl font-black tracking-tighter leading-[0.9]">
          Your <br />
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent via-emerald-200 to-white">
            Academic Hub
          </span>
        </h1>

        <p class="text-xl text-gray-400 max-w-lg leading-relaxed font-light border-l-2 border-nexus-accent/30 pl-6">
          Tasks, attendance, and projects—simplified for students. The ultimate operating system for your education.
        </p>

        <div class="flex flex-col sm:flex-row gap-4 pt-4">
          <router-link to="/register">
            <Button class="h-14 px-8 text-lg bg-nexus-accent text-black font-bold rounded-full hover:bg-emerald-400 hover:shadow-[0_0_30px_rgba(34,197,94,0.4)] transition-all duration-300">
              Get Started
              <ArrowRightIcon class="ml-2 h-5 w-5" />
            </Button>
          </router-link>
          <router-link to="/login">
            <Button variant="outline" class="h-14 px-8 text-lg border-white/10 bg-white/5 text-white hover:bg-white/10 rounded-full backdrop-blur-md">
              Login
            </Button>
          </router-link>
        </div>
      </div>

      <div class="relative flex justify-center lg:justify-end"
           v-motion
           :initial="{ opacity: 0, scale: 0.8, rotate: -5 }"
           :enter="{ opacity: 1, scale: 1, rotate: 0, transition: { duration: 1000, delay: 200, type: 'spring' } }"
      >
        <div class="relative z-10 p-2 bg-gradient-to-br from-white/10 to-transparent rounded-3xl backdrop-blur-xl border border-white/10 shadow-2xl">
            <HeroGraphic />
        </div>
        
        <div class="absolute -z-10 top-10 right-10 w-full h-full border border-dashed border-white/20 rounded-3xl animate-pulse"></div>
      </div>

    </main>

    <section class="border-t border-white/5 bg-black/20 backdrop-blur-sm py-24 relative overflow-hidden">
      <div class="container mx-auto px-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          
          <div v-motion-slide-visible-once-bottom class="group p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:border-nexus-accent/30 hover:bg-white/[0.05] transition-all duration-500 relative overflow-hidden">
            <div class="absolute top-0 right-0 p-3 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowTopRightIcon class="w-5 h-5 text-nexus-accent" />
            </div>
            <div class="h-12 w-12 bg-blue-500/10 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">📝</div>
            <h3 class="text-2xl font-bold text-white mb-2">Smart Tasks</h3>
            <p class="text-gray-400 leading-relaxed">Prioritize assignments with our automated Kanban board system.</p>
          </div>

          <div v-motion-slide-visible-once-bottom :delay="100" class="group p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:border-nexus-accent/30 hover:bg-white/[0.05] transition-all duration-500 relative overflow-hidden">
             <div class="absolute top-0 right-0 p-3 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowTopRightIcon class="w-5 h-5 text-nexus-accent" />
            </div>
            <div class="h-12 w-12 bg-purple-500/10 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">📅</div>
            <h3 class="text-2xl font-bold text-white mb-2">Auto Timetable</h3>
            <p class="text-gray-400 leading-relaxed">Syncs with your college schedule automatically. Never miss a class.</p>
          </div>

          <div v-motion-slide-visible-once-bottom :delay="200" class="group p-8 rounded-3xl bg-white/[0.03] border border-white/5 hover:border-nexus-accent/30 hover:bg-white/[0.05] transition-all duration-500 relative overflow-hidden">
             <div class="absolute top-0 right-0 p-3 opacity-0 group-hover:opacity-100 transition-opacity">
                <ArrowTopRightIcon class="w-5 h-5 text-nexus-accent" />
            </div>
            <div class="h-12 w-12 bg-nexus-accent/10 rounded-2xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">☁️</div>
            <h3 class="text-2xl font-bold text-white mb-2">Secure Cloud</h3>
            <p class="text-gray-400 leading-relaxed">Store notes, syllabus copies, and projects securely in the cloud.</p>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>