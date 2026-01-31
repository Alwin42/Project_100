<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { 
  FileText, 
  Download, 
  BookOpen, 
  Plus, 
  Calendar,
  AlertCircle
} from 'lucide-vue-next'
import { RouterLink } from 'vue-router'

const notes = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await api.get('notes/')
    notes.value = res.data
  } catch (e) {
    console.error("Failed to load notes", e)
  } finally {
    loading.value = false
  }
})

const getFileUrl = (path) => {
  if (!path) return '#'
  return path.startsWith('http') ? path : `http://127.0.0.1:8000${path}`
}
</script>

<template>
  <div class="space-y-8 animate-in fade-in duration-500">
    
    <div class="flex flex-col md:flex-row justify-between md:items-center gap-4">
      <div>
        <h1 class="text-3xl font-bold text-white flex items-center gap-3">
          <BookOpen class="w-8 h-8 text-nexus-accent" />
          My Notes Library
        </h1>
        <p class="text-gray-400 mt-1">Access all your uploaded study materials.</p>
      </div>
      
      <RouterLink to="/dashboard/add-note">
        <Button class="bg-nexus-accent text-black hover:bg-nexus-accent/90 font-bold w-full md:w-auto">
          <Plus class="w-5 h-5 mr-2" /> Upload New Note
        </Button>
      </RouterLink>
    </div>

    <div v-if="loading" class="text-center py-20 text-gray-400">Loading notes...</div>

    <div v-else-if="notes.length === 0" class="text-center py-20 bg-white/5 rounded-3xl border border-white/10">
      <FileText class="w-16 h-16 text-gray-600 mx-auto mb-4" />
      <h3 class="text-xl text-white font-bold">No notes found</h3>
      <p class="text-gray-400 mt-2">Upload notes to see them here.</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card v-for="note in notes" :key="note.id" class="bg-black/40 border-white/10 text-white hover:border-nexus-accent/50 transition-all group">
        <CardHeader class="pb-2">
          <div class="flex justify-between items-start">
            <div class="p-3 bg-white/5 rounded-xl text-nexus-accent border border-white/5">
              <FileText class="w-6 h-6" />
            </div>
            <a :href="getFileUrl(note.file)" target="_blank">
              <Button size="icon" variant="ghost" class="hover:bg-nexus-accent hover:text-black">
                <Download class="w-4 h-4" />
              </Button>
            </a>
          </div>
        </CardHeader>
        
        <CardContent class="space-y-3">
          <div>
            <h3 class="text-lg font-bold text-white truncate group-hover:text-nexus-accent transition-colors">
              {{ note.title }}
            </h3>
            <p class="text-sm text-gray-400 mt-1 flex items-center gap-2">
              <BookOpen class="w-3 h-3" />
              {{ note.subject_name || 'Subject ' + note.subject }}
            </p>
          </div>
          
          <div class="pt-3 border-t border-white/5 flex items-center gap-2 text-xs text-gray-500">
            <Calendar class="w-3 h-3" />
            {{ new Date(note.created_at).toLocaleDateString() }}
          </div>
        </CardContent>
      </Card>
    </div>

  </div>
</template>