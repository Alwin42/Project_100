<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { 
  Plus, 
  Calendar, 
  CheckCircle2, 
  Clock,
  Sparkles,
  Check, 
  Trash2,
  MapPin
} from 'lucide-vue-next'

// Import the new Animation Component
import GeometricBackground from '@/components/GeometricBackground.vue'

const user = ref({ username: 'Student' })
const todayClasses = ref([])
const pendingTasks = ref([])

// --- HELPERS ---

// Get current day abbreviation (Mon, Tue, Wed...)
const getCurrentDay = () => {
  const days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
  return days[new Date().getDay()]
}

// --- ACTIONS ---

const markDone = async (id) => {
  try {
    await api.patch(`tasks/${id}/`, { is_done: true })
    pendingTasks.value = pendingTasks.value.filter(t => t.id !== id)
  } catch (e) {
    console.error("Failed to update task", e)
  }
}

const deleteTask = async (id) => {
  if(!confirm("Are you sure you want to delete this task?")) return

  try {
    await api.delete(`tasks/${id}/`)
    pendingTasks.value = pendingTasks.value.filter(t => t.id !== id)
  } catch (e) {
    console.error("Failed to delete task", e)
  }
}

// --- LOAD DATA ---

onMounted(async () => {
  try {
    // 1. Get User Profile
    const userRes = await api.get('user/')
    user.value = userRes.data

    // 2. Get Pending Tasks
    const taskRes = await api.get('tasks/')
    pendingTasks.value = taskRes.data.filter(t => !t.is_done).slice(0, 5) 

    // 3. Get Timetable & Filter for TODAY
    const timeRes = await api.get('timetable/')
    const today = getCurrentDay()
    
    // Filter: Show only classes for today, sorted by start time
    todayClasses.value = timeRes.data
      .filter(item => item.day === today)
      .sort((a, b) => a.start_time.localeCompare(b.start_time))

  } catch (e) {
    console.error("Dashboard load failed", e)
  }
})
</script>

<template>
  <div class="space-y-10">
    
    <div class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-nexus-accent/10 to-transparent p-8 border border-white/5 shadow-2xl backdrop-blur-3xl min-h-[250px] flex flex-col justify-end">
      
      <GeometricBackground />

      <div class="relative z-10 flex flex-col md:flex-row justify-between items-end gap-4">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <Sparkles class="w-5 h-5 text-yellow-300" />
            <span class="text-sm font-medium text-yellow-300/80 tracking-wider uppercase">Student Dashboard</span>
          </div>
          <h1 class="text-4xl md:text-5xl font-extrabold text-white tracking-tight">
            Hello, <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-white">{{ user.username }}</span>
          </h1>
          <p class="text-gray-300 mt-2 text-lg">Your academic focus is looking sharp today.</p>
        </div>
        
        <div class="text-right hidden md:block bg-black/40 px-6 py-3 rounded-2xl border border-white/10 backdrop-blur-md shadow-xl">
          <p class="text-3xl font-mono text-white font-bold tracking-widest">
            {{ new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) }}
          </p>
          <p class="text-sm text-nexus-accent/80 font-medium uppercase tracking-wide">
            {{ new Date().toLocaleDateString(undefined, { weekday: 'long', month: 'short', day: 'numeric' }) }}
          </p>
        </div>
      </div>
    </div>

    <div>
      <h3 class="text-xl font-bold text-white mb-4 flex items-center gap-2">
        <div class="w-1 h-6 bg-nexus-accent rounded-full"></div>
        Quick Actions
      </h3>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        
        <RouterLink to="/dashboard/add-note" class="group">
          <Button variant="ghost" class="h-auto py-6 w-full flex flex-col gap-3 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-nexus-accent/50 hover:shadow-[0_0_20px_rgba(34,197,94,0.2)] transition-all duration-300 rounded-2xl backdrop-blur-md group-hover:-translate-y-1">
            <div class="p-3 bg-gradient-to-br from-nexus-accent/20 to-transparent rounded-xl group-hover:scale-110 transition-transform">
              <Plus class="w-6 h-6 text-nexus-accent" />
            </div>
            <span class="text-white font-medium group-hover:text-nexus-accent transition-colors">Add Note</span>
          </Button>
        </RouterLink>

        <RouterLink to="/dashboard/add-activity" class="group">
          <Button variant="ghost" class="h-auto py-6 w-full flex flex-col gap-3 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-blue-400/50 hover:shadow-[0_0_20px_rgba(96,165,250,0.2)] transition-all duration-300 rounded-2xl backdrop-blur-md group-hover:-translate-y-1">
            <div class="p-3 bg-gradient-to-br from-blue-500/20 to-transparent rounded-xl group-hover:scale-110 transition-transform">
              <Plus class="w-6 h-6 text-blue-400" />
            </div>
            <span class="text-white font-medium group-hover:text-blue-400 transition-colors">Log Activity</span>
          </Button>
        </RouterLink>

        <RouterLink to="/dashboard/add-expense" class="group">
          <Button variant="ghost" class="h-auto py-6 w-full flex flex-col gap-3 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-green-400/50 hover:shadow-[0_0_20px_rgba(74,222,128,0.2)] transition-all duration-300 rounded-2xl backdrop-blur-md group-hover:-translate-y-1">
            <div class="p-3 bg-gradient-to-br from-green-500/20 to-transparent rounded-xl group-hover:scale-110 transition-transform">
              <Plus class="w-6 h-6 text-green-400" />
            </div>
            <span class="text-white font-medium group-hover:text-green-400 transition-colors">Add Expense</span>
          </Button>
        </RouterLink>
        
        <RouterLink to="/dashboard/add-subject" class="group">
          <Button variant="ghost" class="h-auto py-6 w-full flex flex-col gap-3 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-purple-400/50 hover:shadow-[0_0_20px_rgba(192,132,252,0.2)] transition-all duration-300 rounded-2xl backdrop-blur-md group-hover:-translate-y-1">
            <div class="p-3 bg-gradient-to-br from-purple-500/20 to-transparent rounded-xl group-hover:scale-110 transition-transform">
              <Plus class="w-6 h-6 text-purple-400" />
            </div>
            <span class="text-white font-medium group-hover:text-purple-400 transition-colors">Add Subject</span>
          </Button>
        </RouterLink>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      
      <Card class="bg-black/30 backdrop-blur-xl border border-white/10 rounded-3xl shadow-2xl overflow-hidden min-h-[300px]">
        <CardHeader class="border-b border-white/5 pb-4 bg-white/5">
          <CardTitle class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <CheckCircle2 class="w-5 h-5 text-nexus-accent" /> 
              <span class="text-white">Pending Tasks</span>
            </div>
            <Button variant="ghost" size="sm" class="h-8 text-xs text-gray-400 hover:text-white hover:bg-white/10">View All</Button>
          </CardTitle>
        </CardHeader>
        
        <CardContent class="p-6 space-y-3">
          <div v-if="pendingTasks.length === 0" class="flex flex-col items-center justify-center py-8 text-center">
            <div class="w-12 h-12 bg-nexus-accent/10 rounded-full flex items-center justify-center mb-3">
              <CheckCircle2 class="w-6 h-6 text-nexus-accent" />
            </div>
            <p class="text-gray-400">All caught up! No pending tasks.</p>
          </div>
          
          <div 
            v-for="task in pendingTasks" 
            :key="task.id" 
            class="group relative p-4 rounded-xl bg-white/5 border border-white/5 hover:bg-white/10 hover:border-nexus-accent/30 transition-all flex justify-between items-center overflow-hidden"
          >
            <div class="flex items-center gap-3 z-10">
              <div 
                class="w-2 h-2 rounded-full"
                :class="task.priority === 'High' ? 'bg-red-500' : 'bg-nexus-accent'"
              ></div>
              <span class="text-gray-200 group-hover:text-white transition-colors font-medium">
                {{ task.title }}
              </span>
            </div>

            <span 
              class="text-xs font-bold px-3 py-1 rounded-full border group-hover:opacity-0 transition-opacity duration-200"
              :class="task.priority === 'High' ? 'bg-red-500/10 text-red-400 border-red-500/20' : 'bg-blue-500/10 text-blue-400 border-blue-500/20'"
            >
              {{ task.priority || 'Normal' }}
            </span>

            <div class="absolute right-2 top-1/2 -translate-y-1/2 flex gap-2 translate-x-full group-hover:translate-x-0 transition-transform duration-300 ease-out z-20">
              <button 
                @click.stop="markDone(task.id)"
                class="p-2 rounded-lg bg-nexus-accent/20 text-nexus-accent hover:bg-nexus-accent hover:text-black transition-colors"
                title="Mark as Done"
              >
                <Check class="w-4 h-4" />
              </button>

              <button 
                @click.stop="deleteTask(task.id)"
                class="p-2 rounded-lg bg-red-500/20 text-red-400 hover:bg-red-500 hover:text-white transition-colors"
                title="Delete Task"
              >
                <Trash2 class="w-4 h-4" />
              </button>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card class="bg-black/30 backdrop-blur-xl border border-white/10 rounded-3xl shadow-2xl overflow-hidden min-h-[300px]">
        <CardHeader class="border-b border-white/5 pb-4 bg-white/5">
          <CardTitle class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <Clock class="w-5 h-5 text-blue-400" /> 
              <span class="text-white">Today's Schedule</span>
            </div>
            <RouterLink to="/dashboard/timetable">
              <Button variant="ghost" size="sm" class="h-8 text-xs text-gray-400 hover:text-white hover:bg-white/10">Full Schedule</Button>
            </RouterLink>
          </CardTitle>
        </CardHeader>
        
        <CardContent class="p-0">
          <div v-if="todayClasses.length === 0" class="flex flex-col items-center justify-center py-10 text-center opacity-60">
            <div class="w-12 h-12 bg-blue-500/10 rounded-full flex items-center justify-center mb-3">
              <Calendar class="w-6 h-6 text-blue-400" />
            </div>
            <p class="text-white font-medium">No classes today</p>
            <p class="text-sm text-gray-500">Enjoy your free time!</p>
          </div>

          <div v-else class="flex flex-col">
            <div 
              v-for="cls in todayClasses" 
              :key="cls.id"
              class="flex items-center gap-4 p-4 border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors"
            >
              <div class="flex flex-col items-center min-w-[60px]">
                <span class="text-white font-bold text-sm">{{ cls.start_time.slice(0, 5) }}</span>
                <span class="text-xs text-gray-500">{{ cls.end_time.slice(0, 5) }}</span>
              </div>

              <div class="w-1 h-8 bg-blue-500/20 rounded-full"></div>

              <div class="flex-1">
                <h4 class="text-white font-medium truncate">{{ cls.subject_name || 'Unknown Subject' }}</h4>
                <div class="flex items-center gap-2 text-xs text-gray-400 mt-0.5">
                  <span v-if="cls.room_number" class="flex items-center gap-1 bg-white/10 px-1.5 py-0.5 rounded text-gray-300">
                    <MapPin class="w-3 h-3" /> {{ cls.room_number }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

    </div>
  </div>
</template>