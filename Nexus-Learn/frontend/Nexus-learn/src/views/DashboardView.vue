<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { Motion } from 'motion-v'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { 
  Plus, Calendar, CheckCircle2, Clock, Sparkles, 
  Trash2, MapPin, ArrowRight, Bell 
} from 'lucide-vue-next'
import GeometricBackground from '@/components/GeometricBackground.vue'

const user = ref({ username: 'Student' })
const todayClasses = ref([])
const pendingTasks = ref([])
const isLoading = ref(true)

const getCurrentDay = () => ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][new Date().getDay()]

const markDone = async (id) => {
  try {
    pendingTasks.value = pendingTasks.value.filter(t => t.id !== id)
    await api.patch(`tasks/${id}/`, { is_done: true })
  } catch (e) { console.error("Failed to update task", e) }
}

const deleteTask = async (id) => {
  if(!confirm("Delete this task?")) return
  try {
    pendingTasks.value = pendingTasks.value.filter(t => t.id !== id)
    await api.delete(`tasks/${id}/`)
  } catch (e) { console.error("Failed to delete task", e) }
}

onMounted(async () => {
  try {
    const userRes = await api.get('user/')
    user.value = userRes.data
    const taskRes = await api.get('tasks/')
    pendingTasks.value = taskRes.data.filter(t => !t.is_done).slice(0, 5) 
    const timeRes = await api.get('timetable/')
    todayClasses.value = timeRes.data.filter(i => i.day === getCurrentDay()).sort((a, b) => a.start_time.localeCompare(b.start_time))
  } catch (e) { console.error("Dashboard load failed", e) } finally { isLoading.value = false }
})

const containerVar = { hidden: { opacity: 0 }, show: { opacity: 1, transition: { staggerChildren: 0.1 } } }
const itemVar = { hidden: { opacity: 0, y: 20 }, show: { opacity: 1, y: 0, transition: { type: 'spring', stiffness: 50 } } }
</script>

<template>
  <Motion initial="hidden" animate="show" :variants="containerVar" class="space-y-8 p-1">
    
    <Motion :variants="itemVar" class="relative overflow-hidden rounded-[2.5rem] p-8 md:p-10 border border-white/10 shadow-2xl min-h-[280px] flex flex-col justify-end group">
      <div class="absolute inset-0 bg-gradient-to-br from-gray-900 via-black to-black z-0"></div>
      <div class="absolute inset-0 opacity-40 mix-blend-overlay bg-[url('https://grainy-gradients.vercel.app/noise.svg')] z-0 pointer-events-none"></div>
      <div class="absolute inset-0 z-0 opacity-60"><GeometricBackground /></div>

      <div class="relative z-10 flex flex-col md:flex-row justify-between items-end gap-6">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-yellow-500/10 border border-yellow-500/20 backdrop-blur-md mb-2">
            <Sparkles class="w-4 h-4 text-yellow-300 animate-pulse" />
            <span class="text-xs font-bold text-yellow-300 tracking-widest uppercase">Student Dashboard</span>
          </div>
          <h1 class="text-4xl md:text-6xl font-black text-white tracking-tight drop-shadow-lg">
            Hello, <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent via-green-200 to-white animate-gradient-x">{{ user.username }}</span>
          </h1>
          <p class="text-gray-400 text-lg font-medium max-w-lg">Ready to conquer your academic goals today?</p>
        </div>
        <div class="hidden md:block text-right">
           <div class="bg-white/5 border border-white/10 backdrop-blur-xl px-6 py-4 rounded-2xl shadow-xl hover:bg-white/10 transition-colors cursor-default">
              <p class="text-4xl font-mono text-white font-bold tracking-widest tabular-nums">{{ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) }}</p>
              <p class="text-sm text-nexus-accent font-bold uppercase tracking-widest mt-1">{{ new Date().toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' }) }}</p>
           </div>
        </div>
      </div>
    </Motion>

    <Motion :variants="itemVar">
      <div class="flex items-center gap-3 mb-5 px-1">
        <div class="w-1.5 h-6 bg-nexus-accent rounded-full shadow-[0_0_10px_currentColor]"></div>
        <h3 class="text-xl font-bold text-white tracking-wide">Quick Actions</h3>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
        
        <RouterLink to="/dashboard/add-note" class="group relative">
          <div class="absolute inset-0 bg-nexus-accent/20 blur-xl rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <Button variant="ghost" class="relative h-auto py-6 w-full flex flex-col gap-3 bg-black/40 border border-white/10 hover:border-nexus-accent/50 rounded-3xl backdrop-blur-xl transition-all duration-300 group-hover:-translate-y-2 overflow-hidden">
            <div class="p-3 bg-nexus-accent/10 rounded-2xl group-hover:bg-nexus-accent group-hover:text-black transition-all duration-300">
              <Plus class="w-6 h-6 text-nexus-accent group-hover:text-black" />
            </div>
            <span class="text-gray-300 font-bold text-sm group-hover:text-white">Add Note</span>
          </Button>
        </RouterLink>

        <RouterLink to="/dashboard/add-activity" class="group relative">
           <div class="absolute inset-0 bg-blue-500/20 blur-xl rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
           <Button variant="ghost" class="relative h-auto py-6 w-full flex flex-col gap-3 bg-black/40 border border-white/10 hover:border-blue-400/50 rounded-3xl backdrop-blur-xl transition-all duration-300 group-hover:-translate-y-2">
            <div class="p-3 bg-blue-500/10 rounded-2xl group-hover:bg-blue-500 group-hover:text-black transition-all duration-300">
              <Plus class="w-6 h-6 text-blue-400 group-hover:text-black" />
            </div>
            <span class="text-gray-300 font-bold text-sm group-hover:text-white">Log Activity</span>
          </Button>
        </RouterLink>

        <RouterLink to="/dashboard/add-expense" class="group relative">
           <div class="absolute inset-0 bg-green-500/20 blur-xl rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
           <Button variant="ghost" class="relative h-auto py-6 w-full flex flex-col gap-3 bg-black/40 border border-white/10 hover:border-green-400/50 rounded-3xl backdrop-blur-xl transition-all duration-300 group-hover:-translate-y-2">
            <div class="p-3 bg-green-500/10 rounded-2xl group-hover:bg-green-500 group-hover:text-black transition-all duration-300">
              <Plus class="w-6 h-6 text-green-400 group-hover:text-black" />
            </div>
            <span class="text-gray-300 font-bold text-sm group-hover:text-white">Add Expense</span>
          </Button>
        </RouterLink>
        
        <RouterLink to="/dashboard/add-subject" class="group relative">
           <div class="absolute inset-0 bg-purple-500/20 blur-xl rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
           <Button variant="ghost" class="relative h-auto py-6 w-full flex flex-col gap-3 bg-black/40 border border-white/10 hover:border-purple-400/50 rounded-3xl backdrop-blur-xl transition-all duration-300 group-hover:-translate-y-2">
            <div class="p-3 bg-purple-500/10 rounded-2xl group-hover:bg-purple-500 group-hover:text-black transition-all duration-300">
              <Plus class="w-6 h-6 text-purple-400 group-hover:text-black" />
            </div>
            <span class="text-gray-300 font-bold text-sm group-hover:text-white">Add Subject</span>
          </Button>
        </RouterLink>

        <RouterLink to="/dashboard/add-reminder" class="group relative">
           <div class="absolute inset-0 bg-pink-500/20 blur-xl rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
           <Button variant="ghost" class="relative h-auto py-6 w-full flex flex-col gap-3 bg-black/40 border border-white/10 hover:border-pink-400/50 rounded-3xl backdrop-blur-xl transition-all duration-300 group-hover:-translate-y-2">
            <div class="p-3 bg-pink-500/10 rounded-2xl group-hover:bg-pink-500 group-hover:text-black transition-all duration-300">
              <Plus class="w-6 h-6 text-pink-400 group-hover:text-black" />
            </div>
            <span class="text-gray-300 font-bold text-sm group-hover:text-white">Add Reminder</span>
          </Button>
        </RouterLink>

      </div>
    </Motion>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <Motion :variants="itemVar" class="h-full">
        <Card class="bg-black/20 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-xl overflow-hidden h-full flex flex-col hover:border-white/20 transition-colors">
          <CardHeader class="border-b border-white/5 pb-4 bg-white/[0.02]">
            <CardTitle class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="p-2 bg-nexus-accent/10 rounded-lg"><CheckCircle2 class="w-5 h-5 text-nexus-accent" /></div>
                <span class="text-white font-bold text-lg">Pending Tasks</span>
              </div>
              <div class="text-xs font-mono text-gray-500 bg-white/5 px-2 py-1 rounded-md">{{ pendingTasks.length }} Active</div>
            </CardTitle>
          </CardHeader>
          <CardContent class="p-6 flex-1">
            <div v-if="pendingTasks.length === 0" class="flex flex-col items-center justify-center h-full py-12 text-center">
              <div class="w-16 h-16 bg-nexus-accent/5 border border-nexus-accent/20 rounded-full flex items-center justify-center mb-4 shadow-[0_0_30px_rgba(34,197,94,0.1)]">
                <CheckCircle2 class="w-8 h-8 text-nexus-accent" />
              </div>
              <p class="text-white font-medium text-lg">All tasks completed</p>
            </div>
            <div v-else class="space-y-3">
              <div v-for="task in pendingTasks" :key="task.id" class="group relative p-4 rounded-2xl bg-white/5 border border-white/5 hover:bg-white/10 hover:border-nexus-accent/30 transition-all duration-300 flex justify-between items-center overflow-hidden">
                <div class="absolute left-0 top-0 bottom-0 w-1" :class="task.priority === 'High' ? 'bg-red-500' : 'bg-nexus-accent'"></div>
                <div class="flex items-center gap-4 pl-3 z-10">
                   <button @click.stop="markDone(task.id)" class="w-5 h-5 rounded-full border-2 border-gray-500 group-hover:border-nexus-accent flex items-center justify-center transition-colors">
                      <div class="w-2.5 h-2.5 bg-nexus-accent rounded-full opacity-0 group-hover:opacity-100 transition-opacity"></div>
                   </button>
                   <div>
                      <h4 class="text-gray-200 group-hover:text-white font-medium transition-colors">{{ task.title }}</h4>
                      <p v-if="task.priority === 'High'" class="text-[10px] text-red-400 font-bold uppercase tracking-wider mt-0.5">High Priority</p>
                   </div>
                </div>
                <button @click.stop="deleteTask(task.id)" class="p-2 rounded-xl bg-red-500/10 text-red-400 hover:bg-red-500 hover:text-white transition-all opacity-0 group-hover:opacity-100"><Trash2 class="w-4 h-4" /></button>
              </div>
            </div>
          </CardContent>
        </Card>
      </Motion>

      <Motion :variants="itemVar" class="h-full">
        <Card class="bg-black/20 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-xl overflow-hidden h-full flex flex-col hover:border-white/20 transition-colors">
          <CardHeader class="border-b border-white/5 pb-4 bg-white/[0.02]">
            <CardTitle class="flex items-center justify-between">
              <div class="flex items-center gap-3">
                <div class="p-2 bg-blue-500/10 rounded-lg"><Clock class="w-5 h-5 text-blue-400" /></div>
                <span class="text-white font-bold text-lg">Today's Schedule</span>
              </div>
              <RouterLink to="/dashboard/timetable"><Button variant="ghost" size="sm" class="h-8 text-xs text-blue-400 hover:text-white hover:bg-blue-500/20 rounded-full px-4">Full Schedule</Button></RouterLink>
            </CardTitle>
          </CardHeader>
          <CardContent class="p-0 flex-1">
            <div v-if="todayClasses.length === 0" class="flex flex-col items-center justify-center h-full py-12 text-center opacity-70">
              <div class="w-16 h-16 bg-blue-500/10 rounded-full flex items-center justify-center mb-4"><Calendar class="w-8 h-8 text-blue-400" /></div>
              <p class="text-white font-medium">No classes today</p>
            </div>
            <div v-else class="flex flex-col p-2">
              <div v-for="(cls, index) in todayClasses" :key="cls.id" class="relative flex items-center gap-4 p-4 rounded-xl hover:bg-white/5 transition-colors group">
                <div class="flex flex-col items-end min-w-[60px] z-10">
                  <span class="text-white font-bold text-sm font-mono bg-black/40 px-1.5 py-0.5 rounded border border-white/5">{{ cls.start_time.slice(0, 5) }}</span>
                  <span class="text-[10px] text-gray-500 mt-1">{{ cls.end_time.slice(0, 5) }}</span>
                </div>
                <div class="w-3 h-3 rounded-full border-2 border-black z-10 shadow-[0_0_10px_currentColor]" :class="index === 0 ? 'bg-blue-400 text-blue-400' : 'bg-gray-700 text-gray-700'"></div>
                <div class="flex-1 pl-2">
                  <h4 class="text-gray-200 group-hover:text-blue-300 font-bold transition-colors">{{ cls.subject_name || 'Unknown Subject' }}</h4>
                  <div class="flex items-center gap-3 mt-1">
                    <span v-if="cls.room_number" class="flex items-center gap-1.5 text-xs text-gray-400 bg-white/5 px-2 py-1 rounded-md"><MapPin class="w-3 h-3 text-blue-400" /> {{ cls.room_number }}</span>
                  </div>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </Motion>
    </div>
  </Motion>
</template>