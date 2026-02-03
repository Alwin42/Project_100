<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { Motion } from 'motion-v'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { CalendarClock, Wallet, BookOpen, Trophy, Cloud, ArrowRight, Bell } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const widgets = ref([])
const loading = ref(true)
const user = ref({ username: 'Student' })

const cardVariants = {
  offscreen: { y: 100, opacity: 0, scale: 0.9 },
  onscreen: {
    y: 0, opacity: 1, scale: 1,
    transition: { type: "spring", bounce: 0.4, duration: 0.8 }
  }
}

onMounted(async () => {
  try {
    try { const u = await api.get('user/'); user.value = u.data } catch(e) {}

    const [time, exp, note, act, file, task] = await Promise.allSettled([
      api.get('timetable/'), api.get('expenses/'), api.get('notes/'), 
      api.get('activities/'), api.get('files/'), api.get('tasks/')
    ])

    const w = []
    
    // 0. Reminders (Pink)
    if (task.status === 'fulfilled' && task.value.data.length) {
      const pending = task.value.data.filter(t => !t.is_done).slice(0, 3)
      if(pending.length) w.push({ id: 'reminders', title: 'Reminders', icon: Bell, color: '#ec4899', items: pending.map(t => ({ main: t.title, sub: `${t.priority} Priority` })), link: '/dashboard' })
    }
    // 1. Timetable (Blue)
    if (time.status === 'fulfilled' && time.value.data.length) w.push({ id: 'time', title: 'Timetable', icon: CalendarClock, color: '#3b82f6', items: time.value.data.slice(0,3).map(c => ({main: c.subject_name, sub: `${c.day} • ${c.start_time.slice(0,5)}`})), link: '/dashboard/timetable' })
    // 2. Expenses (Green)
    if (exp.status === 'fulfilled' && exp.value.data.length) {
      const total = exp.value.data.reduce((s, i) => s + parseFloat(i.amount||0), 0)
      w.push({ id: 'exp', title: 'Expenses', icon: Wallet, color: '#22c55e', stat: `₹${total.toFixed(0)}`, statLabel: 'Total', items: exp.value.data.slice(0,3).map(e => ({main: e.category, sub: `₹${e.amount}`})), link: '/dashboard/expenses' })
    }
    // 3. Notes (Purple)
    if (note.status === 'fulfilled' && note.value.data.length) w.push({ id: 'note', title: 'Notes', icon: BookOpen, color: '#a855f7', items: note.value.data.slice(0,3).map(n => ({main: n.title, sub: n.subject_name})), link: '/dashboard/notes' })
    // 4. Cloud (Cyan)
    if (file.status === 'fulfilled' && file.value.data.length) w.push({ id: 'cloud', title: 'Cloud', icon: Cloud, color: '#06b6d4', items: file.value.data.slice(0,3).map(f => ({main: f.title, sub: 'File'})), link: '/dashboard/cloud' })

    widgets.value = w
  } catch (e) { console.error(e) } finally { loading.value = false }
})
</script>

<template>
  <div class="min-h-screen bg-[#09090b] text-white overflow-x-hidden relative selection:bg-nexus-accent selection:text-black">
    <BackgroundShapes />
    <div class="container mx-auto px-6 py-20 pb-40 relative z-10">
      
      <div class="text-center mb-24 space-y-4">
        <h1 class="text-5xl md:text-8xl font-black tracking-tighter">
          Hello, <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-blue-500 animate-gradient">{{ user.username }}</span>
        </h1>
        <p class="text-xl text-gray-400 font-light">Your entire academic life, <span class="text-white font-semibold">stacked.</span></p>
      </div>

      <div class="flex flex-col items-center w-full relative gap-12">
        <div v-if="loading" class="text-gray-500 animate-pulse text-lg">Loading widgets...</div>

        <Motion 
          v-else v-for="(widget, index) in widgets" :key="widget.id"
          class="sticky-card w-full max-w-[450px] group"
          :initial="cardVariants.offscreen"
          :whileInView="cardVariants.onscreen"
          :viewport="{ amount: 0.2 }"
          :style="{ position: 'sticky', top: `${110 + (index * 25)}px`, zIndex: index + 1 }"
        >
          <div class="relative overflow-hidden rounded-[2.5rem] bg-black/40 backdrop-blur-3xl border border-white/10 shadow-2xl transition-all duration-500 h-[500px] flex flex-col group-hover:scale-[1.02] group-hover:border-white/20">
            <div class="absolute inset-0 opacity-0 group-hover:opacity-20 transition-opacity duration-700" :style="{ background: `radial-gradient(circle at top right, ${widget.color}, transparent 70%)` }"></div>
            
            <div class="relative z-10 p-8 flex flex-col h-full">
              <div class="flex items-center gap-4 mb-8">
                <div class="p-3.5 rounded-2xl bg-white/5 border border-white/5 text-white group-hover:bg-white/10 transition-colors">
                  <component :is="widget.icon" class="w-7 h-7" :style="{ color: widget.color }" />
                </div>
                <h2 class="text-3xl font-bold text-white tracking-tight">{{ widget.title }}</h2>
              </div>

              <div v-if="widget.stat" class="mb-6 pb-6 border-b border-white/5">
                 <span class="text-xs font-bold text-gray-500 uppercase tracking-widest pl-1">{{ widget.statLabel }}</span>
                 <div class="text-5xl font-black text-white mt-1 tracking-tight" :style="{ textShadow: `0 0 30px ${widget.color}40` }">{{ widget.stat }}</div>
              </div>

              <div class="space-y-3 flex-1">
                 <div v-for="(item, i) in widget.items" :key="i" class="flex items-center justify-between p-4 rounded-xl bg-white/[0.03] border border-white/5 hover:bg-white/[0.08] transition-all duration-300">
                    <span class="font-semibold text-gray-200 truncate">{{ item.main }}</span>
                    <span class="text-xs font-mono text-gray-500">{{ item.sub }}</span>
                 </div>
              </div>

              <div class="mt-8 pt-6 border-t border-white/5">
                 <RouterLink :to="widget.link">
                    <Button class="w-full h-14 rounded-2xl bg-white/5 hover:bg-white text-white hover:text-black font-bold border border-white/10 transition-all text-lg shadow-lg">
                      Open {{ widget.title }} <ArrowRight class="ml-2 w-5 h-5"/>
                    </Button>
                 </RouterLink>
              </div>
            </div>
          </div>
        </Motion>
        <div class="h-[30vh]"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sticky-card { filter: drop-shadow(0 -20px 30px rgba(0,0,0,0.5)); }
</style>