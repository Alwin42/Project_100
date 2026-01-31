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
  AlertCircle,
  Layers
} from 'lucide-vue-next'

const route = useRoute()
const router = useRouter()
const subject = ref(null)
const notes = ref([]) 
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

onMounted(async () => {
  try {
    const id = route.params.id
    
    // 1. Get Subject Details
    const res = await api.get(`subjects/${id}/`)
    subject.value = res.data

    // 2. Get Notes filtered by this Subject
    const notesRes = await api.get('notes/')
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

const deleteNote = async (noteId) => {
  if (!confirm("Are you sure you want to delete this note?")) return

  try {
    await api.delete(`notes/${noteId}/`)
    // Remove from local list
    notes.value = notes.value.filter(n => n.id !== noteId)
  } catch (e) {
    console.error("Failed to delete note", e)
    alert("Failed to delete note.")
  }
}

const getFileUrl = (path) => {
  if (!path) return '#'
  return path.startsWith('http') ? path : `http://127.0.0.1:8000${path}`
}
</script>

<template>
  <div class="max-w-6xl mx-auto space-y-8 animate-in fade-in duration-700 p-4 md:p-8">
    
    <Button 
      variant="ghost" 
      class="text-gray-400 hover:text-white pl-0 gap-2 transition-colors hover:bg-white/5"
      @click="router.back()"
    >
      <ArrowLeft class="w-4 h-4" /> Back to Subjects
    </Button>

    <div v-if="loading" class="text-center py-20 text-gray-400 flex flex-col items-center">
      <div class="animate-spin w-10 h-10 border-4 border-nexus-accent border-t-transparent rounded-full mb-4"></div>
      <p class="animate-pulse">Loading subject details...</p>
    </div>

    <div v-else-if="error" class="bg-red-500/10 border border-red-500/50 rounded-xl p-8 text-center text-red-200 backdrop-blur-sm">
      <AlertCircle class="w-12 h-12 mx-auto mb-3 text-red-400" />
      <p class="text-lg font-medium">{{ error }}</p>
      <Button class="mt-6 bg-white/10 hover:bg-white/20 text-white" @click="router.push('/dashboard/subjects')">
        Return to List
      </Button>
    </div>

    <div v-else class="space-y-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <Card class="bg-black/40 backdrop-blur-3xl border-white/10 text-white relative overflow-hidden shadow-2xl rounded-3xl group h-full">
          <div class="absolute top-0 right-0 w-64 h-64 bg-nexus-accent/10 rounded-full blur-[80px] -translate-y-1/2 translate-x-1/2 pointer-events-none group-hover:bg-nexus-accent/20 transition-all duration-1000"></div>
          
          <CardHeader class="relative z-10 p-8 h-full flex flex-col justify-between">
            <div class="flex justify-between items-start gap-4">
               <div class="space-y-4">
                  <div class="flex items-center gap-3">
                    <Badge class="px-3 py-1 text-sm font-medium backdrop-blur-md shadow-sm" :class="getDifficultyColor(subject.difficulty)">
                      {{ getDifficultyLabel(subject.difficulty) }}
                    </Badge>
                    
                  </div>
                  <h1 class="text-4xl font-extrabold tracking-tight text-white leading-tight">
                    {{ subject.name }}
                  </h1>
               </div>

               <Button 
                variant="destructive" 
                size="icon" 
                class="bg-red-500/10 text-red-400 hover:bg-red-600 hover:text-white border border-red-500/20 transition-all duration-300 shadow-lg shrink-0"
                @click="deleteSubject"
                title="Delete Subject"
              >
                <Trash2 class="w-5 h-5" />
              </Button>
            </div>
          </CardHeader>
        </Card>

        <Card class="bg-black/40 backdrop-blur-xl border-white/10 text-white shadow-lg hover:border-nexus-accent/30 transition-colors h-full">
          <CardHeader class="pb-2 pt-6 px-6">
            <CardTitle class="text-lg flex items-center gap-2 text-gray-200">
              <div class="p-2 bg-nexus-accent/10 rounded-lg text-nexus-accent">
                  <User class="w-5 h-5" />
              </div>
              Instructor
            </CardTitle>
          </CardHeader>
          <CardContent class="p-6">
            <div class="p-5 bg-gradient-to-br from-white/5 to-transparent rounded-2xl border border-white/5 flex items-center gap-4 hover:bg-white/10 transition-colors cursor-default h-full">
              <div class="w-16 h-16 rounded-full bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center text-2xl font-bold shadow-inner text-white shrink-0">
                {{ subject.teacher_name ? subject.teacher_name.charAt(0) : '?' }}
              </div>
              <div>
                <p class="font-bold text-xl text-white">{{ subject.teacher_name || 'Not Assigned' }}</p>
                <p class="text-sm text-nexus-accent/80 font-medium uppercase tracking-wide mt-1">Course Lead</p>
              </div>
            </div>
          </CardContent>
        </Card>

      </div>

      <Card class="bg-black/40 backdrop-blur-xl border-white/10 text-white shadow-lg hover:border-blue-500/30 transition-colors overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/10 rounded-full blur-[60px] -translate-y-10 translate-x-10 pointer-events-none"></div>
        
        <CardHeader class="flex flex-row items-center justify-between pb-6 border-b border-white/5 px-8 pt-8">
          <CardTitle class="text-xl flex items-center gap-2 text-gray-200">
            <div class="p-2 bg-blue-500/10 rounded-lg text-blue-400">
                <Layers class="w-5 h-5" />
            </div>
            Course Materials
          </CardTitle>
          <Button 
            size="sm" 
            class="bg-nexus-accent/10 hover:bg-nexus-accent text-nexus-accent hover:text-black border border-nexus-accent/20 transition-all shadow-sm h-9 px-4 font-medium" 
            @click="router.push({ path: '/dashboard/add-note', query: { subject: subject.id } })"
          >
            <Plus class="w-4 h-4 mr-2" /> Add Note
          </Button>
        </CardHeader>

        <CardContent class="space-y-8 pt-8 px-8 pb-8">
          
          <div v-if="subject.youtube_link || subject.wiki_link">
            <h3 class="text-sm font-bold text-gray-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <BookOpen class="w-4 h-4" /> External Resources
            </h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <a 
                v-if="subject.youtube_link" 
                :href="subject.youtube_link" 
                target="_blank"
                class="flex items-center gap-4 p-4 bg-white/5 rounded-xl border border-white/5 hover:border-red-500/50 hover:bg-white/10 transition-all group cursor-pointer"
              >
                <div class="p-2.5 bg-red-500/10 rounded-full text-red-500 group-hover:bg-red-500 group-hover:text-white transition-colors shadow-sm">
                  <Youtube class="w-5 h-5" />
                </div>
                <div>
                  <span class="text-sm font-semibold block text-gray-200 group-hover:text-white transition-colors">YouTube Playlist</span>
                  <span class="text-xs text-gray-500 group-hover:text-gray-400">Watch Tutorials</span>
                </div>
              </a>

              <a 
                v-if="subject.wiki_link" 
                :href="subject.wiki_link" 
                target="_blank"
                class="flex items-center gap-4 p-4 bg-white/5 rounded-xl border border-white/5 hover:border-blue-500/50 hover:bg-white/10 transition-all group cursor-pointer"
              >
                <div class="p-2.5 bg-blue-500/10 rounded-full text-blue-500 group-hover:bg-blue-500 group-hover:text-white transition-colors shadow-sm">
                  <LinkIcon class="w-5 h-5" />
                </div>
                <div>
                  <span class="text-sm font-semibold block text-gray-200 group-hover:text-white transition-colors">Documentation</span>
                  <span class="text-xs text-gray-500 group-hover:text-gray-400">Read Wiki</span>
                </div>
              </a>
            </div>
          </div>

          <div>
            <h3 class="text-sm font-bold text-gray-400 uppercase tracking-wider mb-4 flex items-center gap-2">
              <FileText class="w-4 h-4" /> Uploaded Notes
            </h3>

            <div v-if="notes.length > 0" class="space-y-3">
              <div 
                v-for="note in notes" 
                :key="note.id" 
                class="flex items-center justify-between p-4 bg-white/5 rounded-xl border border-white/5 hover:bg-white/10 hover:border-nexus-accent/20 transition-all group"
              >
                <div class="flex items-center gap-4">
                  <div class="p-3 bg-gray-800 rounded-lg text-gray-400 group-hover:text-nexus-accent group-hover:bg-nexus-accent/10 transition-colors">
                      <FileText class="w-6 h-6" />
                  </div>
                  <div>
                    <p class="text-base font-semibold text-white group-hover:text-nexus-accent transition-colors">{{ note.title }}</p>
                    <p class="text-xs text-gray-500 mt-0.5 flex items-center gap-1">
                      {{ new Date(note.created_at).toLocaleDateString() }}
                    </p>
                  </div>
                </div>
                
                <div class="flex items-center gap-2">
                  <a 
                    :href="getFileUrl(note.file)" 
                    target="_blank" 
                    class="p-2.5 bg-white/5 text-gray-400 rounded-lg hover:bg-nexus-accent hover:text-black transition-all shadow-sm hover:shadow-nexus-accent/20"
                    title="Download Note"
                  >
                    <Download class="w-5 h-5" />
                  </a>

                  <button 
                    @click="deleteNote(note.id)"
                    class="p-2.5 bg-white/5 text-gray-400 rounded-lg hover:bg-red-500 hover:text-white transition-all shadow-sm hover:shadow-red-500/20"
                    title="Delete Note"
                  >
                    <Trash2 class="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
            
            <div v-else class="flex flex-col items-center py-8 text-center border-2 border-dashed border-white/5 rounded-xl bg-white/[0.02]">
              <p class="text-gray-500 font-medium text-sm">No notes uploaded yet.</p>
              <Button 
                variant="link" 
                class="text-nexus-accent h-auto p-0 text-xs mt-1" 
                @click="router.push({ path: '/dashboard/add-note', query: { subject: subject.id } })"
              >
                Upload First Note
              </Button>
            </div>
          </div>

        </CardContent>
      </Card>

    </div>
  </div>
</template>