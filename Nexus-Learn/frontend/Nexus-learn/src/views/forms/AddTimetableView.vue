<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { CalendarClock, BookOpen, Calendar, Clock, ChevronDown } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const subjects = ref([])
const form = ref({ subject: '', day: 'Mon', start_time: '', end_time: '', room_number: '' })

onMounted(async () => { const res = await api.get('subjects/'); subjects.value = res.data })
const submit = async () => { await api.post('timetable/', form.value); router.push('/dashboard') }
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-cyan-500 flex items-center justify-center shadow-lg shadow-cyan-500/20"><CalendarClock class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Add <span class="text-cyan-500">Class</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Subject</Label><div class="relative"><BookOpen class="absolute left-4 top-3.5 h-5 w-5 text-gray-500" /><select v-model="form.subject" class="w-full pl-12 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-cyan-500 outline-none appearance-none cursor-pointer"><option v-for="s in subjects" :key="s.id" :value="s.id" class="bg-gray-900">{{ s.name }}</option></select><ChevronDown class="absolute right-4 top-4 w-4 h-4 text-gray-400 pointer-events-none" /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Day</Label><div class="relative"><Calendar class="absolute left-4 top-3.5 h-5 w-5 text-gray-500" /><select v-model="form.day" class="w-full pl-12 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-cyan-500 outline-none appearance-none cursor-pointer"><option value="Mon" class="bg-gray-900">Monday</option><option value="Tue" class="bg-gray-900">Tuesday</option><option value="Wed" class="bg-gray-900">Wednesday</option><option value="Thu" class="bg-gray-900">Thursday</option><option value="Fri" class="bg-gray-900">Friday</option></select><ChevronDown class="absolute right-4 top-4 w-4 h-4 text-gray-400 pointer-events-none" /></div></div>
          
          <div class="grid grid-cols-2 gap-4">
             <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Start</Label><div class="relative group"><Clock class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-cyan-500 transition-colors" /><Input type="time" v-model="form.start_time" class="pl-12 h-12 bg-white/5 border-white/10 text-white [color-scheme:dark] rounded-2xl focus:border-cyan-500" /></div></div>
             <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">End</Label><div class="relative group"><Clock class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-cyan-500 transition-colors" /><Input type="time" v-model="form.end_time" class="pl-12 h-12 bg-white/5 border-white/10 text-white [color-scheme:dark] rounded-2xl focus:border-cyan-500" /></div></div>
          </div>

          <Button type="submit" class="w-full h-12 text-lg bg-cyan-500 hover:bg-cyan-400 text-black font-bold shadow-lg shadow-cyan-500/20 rounded-2xl mt-4">Save Class</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>