<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { FileText, Download } from 'lucide-vue-next'

const notes = ref([])
const loading = ref(true)

// Helper to construct full media URL
const getFileUrl = (path) => {
  if (!path) return '#'
  if (path.startsWith('http')) return path
  return `http://127.0.0.1:8000${path}`
}

onMounted(async () => {
  try {
    const res = await api.get('notes/')
    notes.value = res.data
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-3xl font-bold text-white">My Notes</h1>
      <RouterLink to="/add-note">
        <Button class="bg-nexus-accent text-black font-bold">+ Upload Note</Button>
      </RouterLink>
    </div>

    <div v-if="loading" class="text-white">Loading notes...</div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card v-for="note in notes" :key="note.id" class="bg-black/40 border-white/10 text-white hover:border-nexus-accent/50 transition-all">
        <CardHeader class="flex flex-row items-center gap-4 pb-2">
          <div class="p-3 bg-white/5 rounded-lg">
            <FileText class="w-8 h-8 text-nexus-accent" />
          </div>
          <div>
            <CardTitle class="text-lg">{{ note.title }}</CardTitle>
            <p class="text-sm text-gray-400">{{ note.subject_name || 'General' }}</p>
          </div>
        </CardHeader>
        <CardContent>
          <p class="text-xs text-gray-500">Uploaded on {{ new Date(note.created_at).toLocaleDateString() }}</p>
        </CardContent>
        <CardFooter>
          <a :href="getFileUrl(note.file)" target="_blank" class="w-full">
            <Button variant="outline" class="w-full border-white/10 hover:bg-white/10 text-white gap-2">
              <Download class="w-4 h-4" /> Download PDF
            </Button>
          </a>
        </CardFooter>
      </Card>
    </div>
  </div>
</template>