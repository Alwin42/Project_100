<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { CalendarClock, MapPin } from 'lucide-vue-next'

const timetable = ref([])
const loading = ref(true)

// Group by Day
const days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
const grouped = ref({})

onMounted(async () => {
  try {
    const res = await api.get('timetable/')
    timetable.value = res.data
    // Initialize groups
    days.forEach(d => grouped.value[d] = [])
    // Sort into days
    res.data.forEach(item => {
      if(grouped.value[item.day]) grouped.value[item.day].push(item)
    })
  } catch (e) { console.error(e) } finally { loading.value = false }
})
</script>

<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold text-white">Weekly Timetable</h1>

    <div class="grid grid-cols-1 lg:grid-cols-5 gap-4">
      <div v-for="day in days" :key="day" class="space-y-4">
        <div class="bg-nexus-accent/10 text-nexus-accent font-bold text-center py-2 rounded border border-nexus-accent/20">
          {{ day }}
        </div>

        <Card v-for="cls in grouped[day]" :key="cls.id" class="bg-black/40 border-white/10 text-white">
          <CardContent class="p-4 space-y-2">
            <h3 class="font-bold text-lg truncate">{{ cls.subject_name }}</h3>
            <div class="flex items-center gap-2 text-sm text-gray-400">
              <CalendarClock class="w-4 h-4" />
              {{ cls.start_time.slice(0,5) }} - {{ cls.end_time.slice(0,5) }}
            </div>
            <div class="flex items-center gap-2 text-xs text-gray-500">
              <MapPin class="w-3 h-3" />
              Room: {{ cls.room_number || 'N/A' }}
            </div>
          </CardContent>
        </Card>
        
        <div v-if="!grouped[day]?.length" class="text-center text-gray-600 text-sm py-4 border border-dashed border-white/10 rounded">
          No classes
        </div>
      </div>
    </div>
  </div>
</template>