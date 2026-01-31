<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { 
  ArrowLeft, 
  User, 
  BookOpen, 
  Trash2, 
  Youtube,
  Link as LinkIcon,
  FileText,
  Download,
  Plus,
  AlertCircle
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const subject = ref(null)
const notes = ref([]) // Store notes for this subject
const loading = ref(true)
const error = ref(null)

const getDifficultyColor = (level) => {
  switch (Number(level)) {
    case 1: return 'bg-green-500/20 text-green-400 border-green-500/50'
    case 2: return 'bg-blue-500/20 text-blue-400 border-blue-500/50'
    case 3: return 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50'
    case 4: return 'bg-red-500/20 text-red-400 border-red-500/50'
    default: return 'bg-gray-500/20 text-gray-400'
  }
}

const getDifficultyLabel = (level) => {
  const map = { 1: 'Easy', 2: 'Medium', 3: 'Hard', 4: 'Very Hard' }
  return map[level] || 'Unknown'
}

// Fetch Data
onMounted(async () => {
  try {
    const id = route.params.id
    
    // 1. Get Subject Details
    const res = await api.get(`subjects/${id}/`)
    subject.value = res.data

    // 2. Get Notes filtered by this Subject
    // Assuming backend supports filtering or we filter client-side
    const notesRes = await api.get('notes/')
    // Filter client-side if backend returns all
    notes.value = notesRes.data.filter(n => n.subject === parseInt(id) || n.subject.id === parseInt(id))
    
  } catch (e) {
    console.error("Failed to load details", e)
    error.value = "Subject not found or access denied."
  } finally {
    loading.value = false
  }
})

const deleteSubject = async () => {
  if (!confirm("Are you sure? This will delete the subject and all related data.")) return
  try {
    await api.delete(`subjects/${subject.value.id}/`)
    router.push('/dashboard/subjects')
  } catch (e) {
    alert("Failed to delete subject.")
  }
}

const getFileUrl = (path) => {
  if (!path) return '#'
  return path.startsWith('http') ? path : `http://127.0.0.1:8000${path}`
}
</script>

<template>
  <div class="max-w-4xl mx-auto space-y-6 animate-in fade-in duration-500">
    
    <Button 
      variant="ghost" 
      class="text-gray-400 hover:text-white pl-0 gap-2"
      @click="router.back()"
    >
      <ArrowLeft class="w-4 h-4" /> Back to Subjects
    </Button>

    <div v-if="loading" class="text-center py-20 text-gray-400">
      <div class="animate-spin w-8 h-8 border-4 border-nexus-accent border-t-transparent rounded-full mx-auto mb-4"></div>
      Loading details...
    </div>

    <div v-else-if="error" class="bg-red-500/10 border border-red-500/50 rounded-xl p-6 text-center text-red-200">
      <AlertCircle class="w-10 h-10 mx-auto mb-2 text-red-400" />
      <p>{{ error }}</p>
      <Button class="mt-4 bg-white/10 hover:bg-white/20" @click="router.push('/dashboard/subjects')">
        Return to List
      </Button>
    </div>

    <div v-else class="space-y-6">
      
      <Card class="bg-black/40 backdrop-blur-3xl border-white/10 text-white relative overflow-hidden">
        <div class="absolute top-0 right-0 w-96 h-96 bg-nexus-accent/10 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>

        <CardHeader class="relative z-10 pb-2">
          <div class="flex justify-between items-start">
            <div class="space-y-1">
              <Badge class="mb-2" :class="getDifficultyColor(subject.difficulty)">
                {{ getDifficultyLabel(subject.difficulty) }} Difficulty
              </Badge>
              <h1 class="text-4xl font-extrabold tracking-tight text-white">{{ subject.name }}</h1>
            </div>
            
            <Button 
              variant="destructive" 
              size="icon" 
              class="bg-red-500/10 text-red-400 hover:bg-red-600 hover:text-white border border-red-500/20"
              @click="deleteSubject"
              title="Delete Subject"
            >
              <Trash2 class="w-5 h-5" />
            </Button>
          </div>
        </CardHeader>
      </Card>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <Card class="md:col-span-1 bg-black/40 backdrop-blur-xl border-white/10 text-white h-fit">
          <CardHeader>
            <CardTitle class="text-lg flex items-center gap-2">
              <User class="w-5 h-5 text-nexus-accent" />
              Instructor
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div class="p-4 bg-white/5 rounded-xl border border-white/5 flex items-center gap-4">
              <div class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-lg font-bold">
                {{ subject.teacher_name ? subject.teacher_name.charAt(0) : '?' }}
              </div>
              <div>
                <p class="font-bold text-white">{{ subject.teacher_name || 'Not Assigned' }}</p>
                <p class="text-xs text-gray-400">Course Instructor</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <div class="md:col-span-2 space-y-6">
          
          <Card class="bg-black/40 backdrop-blur-xl border-white/10 text-white">
            <CardHeader>
              <CardTitle class="text-lg flex items-center gap-2">
                <BookOpen class="w-5 h-5 text-blue-400" />
                Learning Resources
              </CardTitle>
            </CardHeader>
            <CardContent class="space-y-3">
              <div v-if="subject.youtube_link" class="flex items-center justify-between p-3 bg-white/5 rounded-lg border border-white/5 hover:border-red-500/50 transition-colors group">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-red-500/10 rounded-full text-red-500 group-hover:bg-red-500 group-hover:text-white transition-colors">
                    <Youtube class="w-5 h-5" />
                  </div>
                  <span class="text-sm font-medium">YouTube Playlist</span>
                </div>
                <a :href="subject.youtube_link" target="_blank" class="text-xs bg-white/10 hover:bg-white/20 px-3 py-1.5 rounded-md transition-colors">
                  Watch Now
                </a>
              </div>

              <div v-if="subject.wiki_link" class="flex items-center justify-between p-3 bg-white/5 rounded-lg border border-white/5 hover:border-blue-500/50 transition-colors group">
                <div class="flex items-center gap-3">
                  <div class="p-2 bg-blue-500/10 rounded-full text-blue-500 group-hover:bg-blue-500 group-hover:text-white transition-colors">
                    <LinkIcon class="w-5 h-5" />
                  </div>
                  <span class="text-sm font-medium">Wiki / Documentation</span>
                </div>
                <a :href="subject.wiki_link" target="_blank" class="text-xs bg-white/10 hover:bg-white/20 px-3 py-1.5 rounded-md transition-colors">
                  Visit Link
                </a>
              </div>

              <div v-if="!subject.youtube_link && !subject.wiki_link" class="text-center py-4 text-gray-500 text-sm">
                No external links added.
              </div>
            </CardContent>
          </Card>

          <Card class="bg-black/40 backdrop-blur-xl border-white/10 text-white">
            <CardHeader class="flex flex-row items-center justify-between">
              <CardTitle class="text-lg flex items-center gap-2">
                <FileText class="w-5 h-5 text-nexus-accent" />
                Study Notes
              </CardTitle>
              <Button size="sm" class="bg-white/10 hover:bg-white/20 text-xs h-8" @click="router.push('/dashboard/add-note')">
                <Plus class="w-3 h-3 mr-1" /> Add Note
              </Button>
            </CardHeader>
            <CardContent>
              <div v-if="notes.length > 0" class="space-y-2">
                <div v-for="note in notes" :key="note.id" class="flex items-center justify-between p-3 bg-white/5 rounded-lg border border-white/5 hover:bg-white/10 transition-colors">
                  <div class="flex items-center gap-3">
                    <FileText class="w-8 h-8 text-gray-400" />
                    <div>
                      <p class="text-sm font-medium text-white">{{ note.title }}</p>
                      <p class="text-xs text-gray-500">{{ new Date(note.created_at).toLocaleDateString() }}</p>
                    </div>
                  </div>
                  <a :href="getFileUrl(note.file)" target="_blank" class="p-2 bg-nexus-accent/10 text-nexus-accent rounded-full hover:bg-nexus-accent hover:text-black transition-colors">
                    <Download class="w-4 h-4" />
                  </a>
                </div>
              </div>
              
              <div v-else class="text-center py-6 text-gray-500 text-sm border border-dashed border-white/10 rounded-lg">
                No notes uploaded yet.
              </div>
            </CardContent>
          </Card>

        </div>
      </div>
    </div>
  </div>
</template>