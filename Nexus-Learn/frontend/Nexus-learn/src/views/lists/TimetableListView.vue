<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { CalendarClock, MapPin, Plus, Clock } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const timetable = ref([])
const loading = ref(true)

// Configuration matching your reference image
const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

const periods = [
  { id: 1, label: '08:00 - 08:45' },
  { id: 2, label: '09:10 - 09:55' },
  { id: 3, label: '10:00 - 10:45' },
  { id: 4, label: '10:50 - 11:35' },
  { id: 5, label: '11:55 - 12:40' },
  { id: 6, label: '12:45 - 01:30' }
]

onMounted(async () => {
  try {
    const res = await api.get('timetable/')
    timetable.value = res.data
  } catch (e) {
    console.error("Failed to load timetable", e)
  } finally {
    loading.value = false
  }
})

//  to find the class for a specific Day and Period Index (1-based)
const getClassForSlot = (dayName, periodIndex) => {
  // Convert "Monday" -> "Mon" to match backend data
  const shortDay = dayName.substring(0, 3) 
  
  // Get all classes for this day, sorted by time
  const dayClasses = timetable.value
    .filter(t => t.day === shortDay)
    .sort((a, b) => a.start_time.localeCompare(b.start_time))
  
  // Return the class corresponding to the column index (0 for Period 1, etc.)
  return dayClasses[periodIndex]
}
</script>

<template>
  <div class="min-h-screen text-white overflow-x-hidden relative p-4 md:p-8">
    
    <BackgroundShapes />
    <div class="fixed inset-0  -z-10"></div>
    
    <div class="container mx-auto relative z-10 max-w-7xl">
      
      <div class="flex flex-col md:flex-row justify-between items-end mb-8 gap-4">
        <div>
          <div class="flex items-center gap-3 mb-2">
            <div class="p-3 rounded-xl bg-blue-500/10 border border-blue-500/20 text-blue-400">
              <CalendarClock class="w-8 h-8" />
            </div>
            <h1 class="text-4xl font-black tracking-tighter text-white">Class <span class="text-blue-500">Timetable</span></h1>
          </div>
          <p class="text-gray-400 font-medium">Regular Class Time Table (2025-2026)</p>
        </div>
        
        <router-link to="/dashboard/add-timetable">
          <Button class="bg-blue-500 hover:bg-blue-400 text-black font-bold h-12 rounded-xl shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all px-6">
            <Plus class="w-5 h-5 mr-2" /> Add Class
          </Button>
        </router-link>
      </div>

      <div class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-black/40 backdrop-blur-sm shadow-3xl">
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse min-w-[1000px]">
            
            <thead>
              <tr class="border-b border-white/10 bg-white/5">
                <th class="p-6 font-bold text-blue-400 text-lg border-r border-white/10 w-40 uppercase tracking-widest bg-black/20">
                  Day / Time
                </th>
                <th v-for="(period, index) in periods" :key="period.id" class="p-4 border-r border-white/10 min-w-[160px] text-center group hover:bg-white/5 transition-colors">
                  <div class="inline-flex items-center justify-center w-8 h-8 rounded-full bg-blue-500/20 text-blue-400 font-bold mb-2 border border-blue-500/30">
                    {{ index + 1 }}
                  </div>
                  <div class="flex items-center justify-center gap-1.5 text-xs font-mono text-gray-400 bg-black/40 py-1 px-2 rounded-lg border border-white/5">
                    <Clock class="w-3 h-3" /> {{ period.label }}
                  </div>
                </th>
              </tr>
            </thead>

            <tbody>
              <tr v-if="loading">
                <td colspan="7" class="p-12 text-center text-gray-500 animate-pulse">Loading schedule data...</td>
              </tr>
              
              <tr v-else v-for="day in days" :key="day" class="border-b border-white/5 hover:bg-white/[0.02] transition-colors group">
                
                <td class="p-6 font-black text-white text-lg border-r border-white/10 bg-white/[0.02] group-hover:bg-blue-500/5 transition-colors uppercase tracking-wider">
                  {{ day }}
                </td>

                <td v-for="(period, index) in periods" :key="period.id" class="p-2 border-r border-white/5 h-32 align-top relative">
                  
                  <template v-if="getClassForSlot(day, index)">
                    <div class="h-full w-full p-4 rounded-2xl bg-blue-500/10 border border-blue-500/20 flex flex-col justify-between hover:bg-blue-500/20 hover:scale-[1.02] transition-all cursor-default shadow-lg group/card">
                      <div>
                        <div class="font-bold text-white text-sm line-clamp-2 leading-tight group-hover/card:text-blue-200">
                          {{ getClassForSlot(day, index).subject_name }}
                        </div>
                        <div class="text-[10px] font-bold text-blue-400 mt-1 uppercase tracking-wider">
                          {{ getClassForSlot(day, index).subject || 'CODE' }}
                        </div>
                      </div>
                      
                      <div v-if="getClassForSlot(day, index).room_number" class="flex items-center gap-1.5 text-xs text-gray-400 bg-black/40 p-1.5 rounded-lg w-fit border border-white/5">
                        <MapPin class="w-3 h-3 text-blue-400" /> 
                        {{ getClassForSlot(day, index).room_number }}
                      </div>
                    </div>
                  </template>

                  <div v-else class="h-full w-full flex items-center justify-center opacity-0 hover:opacity-100 transition-opacity">
                    <div class="w-2 h-2 rounded-full bg-white/10"></div>
                  </div>

                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>