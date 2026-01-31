<script setup>
import { RouterLink } from 'vue-router'
import { Button } from '@/components/ui/button'
import Navbar from '@/components/Navbar.vue' // Reuse your Navbar
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { RocketIcon, ClockIcon, FileTextIcon } from '@radix-icons/vue'

// Fake data for the preview widgets
const nextClass = { subject: 'Data Structures', time: '10:00 AM' }
const pendingTasks = 3
</script>

<template>
  <div class="min-h-screen bg-nexus-main text-white">
    <div class="container mx-auto px-6 py-10">
      
      <div class="flex justify-between items-center mb-10">
        <div>
          <h1 class="text-4xl font-bold">Good Morning, Student.</h1>
          <p class="text-gray-400 mt-2">Here is your daily snapshot.</p>
        </div>
        <RouterLink to="/dashboard">
          <Button class="bg-nexus-accent text-black font-bold hover:bg-emerald-400">
            Open Full Dashboard <RocketIcon class="ml-2"/>
          </Button>
        </RouterLink>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <Card class="bg-black/40 border-white/10 backdrop-blur-md">
          <CardHeader>
            <CardTitle class="flex items-center gap-2 text-blue-400">
              <ClockIcon /> Up Next
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div class="text-2xl font-bold text-white">{{ nextClass.subject }}</div>
            <div class="text-gray-400">{{ nextClass.time }}</div>
          </CardContent>
        </Card>

        <Card class="bg-black/40 border-white/10 backdrop-blur-md">
          <CardHeader>
            <CardTitle class="flex items-center gap-2 text-nexus-accent">
              <FileTextIcon /> Pending Tasks
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div class="text-2xl font-bold text-white">{{ pendingTasks }} Tasks</div>
            <div class="text-gray-400">Due today</div>
          </CardContent>
        </Card>
      </div>

    </div>
  </div>
</template>