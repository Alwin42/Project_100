<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge' 
import { Button } from '@/components/ui/button'
import { 
  Trophy, 
  Image as ImageIcon, 
  Calendar, 
  Plus, 
  AlertCircle,
  Trash2 
} from 'lucide-vue-next'
import { RouterLink } from 'vue-router'

const activities = ref([])
const loading = ref(true)
const error = ref(null)

const getImageUrl = (path) => {
  if (!path) return null
  return path.startsWith('http') ? path : `http://127.0.0.1:8000${path}`
}

// --- DELETE FUNCTION ---
const deleteActivity = async (id) => {
  if (!confirm("Are you sure you want to delete this activity?")) return

  try {
    // 1. Delete from backend
    await api.delete(`activities/${id}/`)
    
    // 2. Remove from local list immediately
    activities.value = activities.value.filter(act => act.id !== id)
  } catch (e) {
    console.error("Failed to delete activity", e)
    alert("Failed to delete. Please try again.")
  }
}

// --- LOAD DATA ---
onMounted(async () => {
  try {
    const res = await api.get('activities/')
    activities.value = res.data
  } catch (e) {
    console.error(e)
    if (e.response && e.response.status === 401) {
      error.value = "Session expired. Please logout and login again."
    } else {
      error.value = "Failed to load activities."
    }
  } finally { 
    loading.value = false 
  }
})
</script>

<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-3xl font-bold text-white">Activity Log</h1>
      <RouterLink to="/dashboard/add-activity">
        <Button class="bg-nexus-accent text-black font-bold">
          <Plus class="w-4 h-4 mr-2" /> Log Activity
        </Button>
      </RouterLink>
    </div>
    
    <div v-if="loading" class="text-center py-20 text-gray-400">
      <div class="animate-spin w-8 h-8 border-4 border-nexus-accent border-t-transparent rounded-full mx-auto mb-4"></div>
      Loading activities...
    </div>

    <div v-else-if="error" class="bg-red-500/10 border border-red-500/50 rounded-xl p-6 text-center text-red-200">
      <AlertCircle class="w-10 h-10 mx-auto mb-2 text-red-400" />
      <p>{{ error }}</p>
    </div>

    <div v-else-if="activities.length === 0" class="text-center py-20 bg-white/5 rounded-3xl border border-white/10">
      <Trophy class="w-16 h-16 text-gray-600 mx-auto mb-4" />
      <h3 class="text-xl text-white font-bold">No activities yet</h3>
      <p class="text-gray-400 mt-2">Log your hackathons, workshops, and achievements here.</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      
      <Card v-for="act in activities" :key="act.id" class="bg-black/40 border-white/10 text-white overflow-hidden hover:border-nexus-accent/50 transition-all flex flex-col group">
        
        <div class="h-48 bg-white/5 flex items-center justify-center overflow-hidden relative">
          <img v-if="act.image" :src="getImageUrl(act.image)" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
          <ImageIcon v-else class="w-12 h-12 text-gray-700" />
          
          <button 
            @click.stop="deleteActivity(act.id)"
            class="absolute top-2 right-2 p-2 bg-red-600/90 text-white rounded-lg opacity-0 group-hover:opacity-100 transition-opacity hover:bg-red-700 shadow-lg"
            title="Delete Activity"
          >
            <Trash2 class="w-4 h-4" />
          </button>

          <div v-if="act.date" class="absolute bottom-2 left-2 bg-black/60 backdrop-blur-md text-white text-xs px-2 py-1 rounded flex items-center gap-1">
            <Calendar class="w-3 h-3" /> {{ act.date }}
          </div>
        </div>

        <CardHeader class="pb-2">
          <div class="flex justify-between items-start gap-2">
            <CardTitle class="text-lg leading-tight">{{ act.name }}</CardTitle>
            <Badge class="bg-nexus-accent text-black hover:bg-nexus-accent whitespace-nowrap">{{ act.activity_type }}</Badge>
          </div>
        </CardHeader>
        
        <CardContent class="flex-1">
          <p class="text-gray-400 text-sm line-clamp-3">{{ act.description }}</p>
        </CardContent>
      </Card>

    </div>
  </div>
</template>