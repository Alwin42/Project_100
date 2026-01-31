<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent, CardFooter } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { 
  BookOpen, 
  User, 
  Plus, 
  ArrowRight, 
  GraduationCap, 
  AlertCircle 
} from 'lucide-vue-next'

const subjects = ref([])
const loading = ref(true)
const error = ref(null)

// Helper for difficulty colors
const getDifficultyColor = (level) => {
  switch (Number(level)) {
    case 1: return 'bg-green-500/20 text-green-400 border-green-500/50' // Easy
    case 2: return 'bg-blue-500/20 text-blue-400 border-blue-500/50'   // Medium
    case 3: return 'bg-yellow-500/20 text-yellow-400 border-yellow-500/50' // Hard
    case 4: return 'bg-red-500/20 text-red-400 border-red-500/50'     // Very Hard
    default: return 'bg-gray-500/20 text-gray-400'
  }
}

const getDifficultyLabel = (level) => {
  const map = { 1: 'Easy', 2: 'Medium', 3: 'Hard', 4: 'Very Hard' }
  return map[level] || 'Unknown'
}

onMounted(async () => {
  try {
    const res = await api.get('subjects/')
    subjects.value = res.data
  } catch (e) {
    console.error(e)
    if (e.response && e.response.status === 401) {
      error.value = "Session expired. Please login again."
    } else {
      error.value = "Failed to load subjects."
    }
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="space-y-8 animate-in fade-in duration-500">
    
    <div class="flex flex-col md:flex-row justify-between md:items-center gap-4">
      <div>
        <h1 class="text-3xl font-bold text-white flex items-center gap-3">
          <GraduationCap class="w-8 h-8 text-nexus-accent" />
          My Subjects
        </h1>
        <p class="text-gray-400 mt-1">Manage your courses and learning materials.</p>
      </div>
      
      <RouterLink to="/dashboard/add-subject">
        <Button class="bg-nexus-accent text-black hover:bg-nexus-accent/90 font-bold w-full md:w-auto shadow-[0_0_20px_rgba(34,197,94,0.2)]">
          <Plus class="w-5 h-5 mr-2" />
          Add Subject
        </Button>
      </RouterLink>
    </div>

    <div v-if="loading" class="text-center py-20 text-gray-400">
      <div class="animate-spin w-8 h-8 border-4 border-nexus-accent border-t-transparent rounded-full mx-auto mb-4"></div>
      Loading library...
    </div>

    <div v-else-if="error" class="bg-red-500/10 border border-red-500/50 rounded-xl p-6 text-center text-red-200">
      <AlertCircle class="w-10 h-10 mx-auto mb-2 text-red-400" />
      <p>{{ error }}</p>
    </div>

    <div v-else-if="subjects.length === 0" class="text-center py-20 bg-white/5 rounded-3xl border border-white/10 backdrop-blur-sm">
      <BookOpen class="w-16 h-16 text-gray-600 mx-auto mb-4" />
      <h3 class="text-xl text-white font-bold">No subjects added</h3>
      <p class="text-gray-400 mt-2">Click "Add Subject" to start tracking your courses.</p>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
      
      <RouterLink 
        v-for="sub in subjects" 
        :key="sub.id" 
        :to="`/dashboard/subjects/${sub.id}`"
        class="block group"
      >
        <Card class="h-full bg-black/40 backdrop-blur-xl border-white/10 text-white hover:border-nexus-accent/50 hover:bg-white/5 transition-all duration-300 relative overflow-hidden group-hover:-translate-y-1 group-hover:shadow-2xl">
          
          <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-br from-nexus-accent/10 to-transparent rounded-full blur-2xl -translate-y-10 translate-x-10 group-hover:from-nexus-accent/20 transition-all"></div>

          <CardHeader>
            <div class="flex justify-between items-start gap-2">
              <div class="p-3 bg-white/5 rounded-xl border border-white/5 group-hover:border-nexus-accent/30 transition-colors">
                <BookOpen class="w-6 h-6 text-nexus-accent" />
              </div>
              <span 
                class="text-xs font-bold px-2 py-1 rounded border capitalize"
                :class="getDifficultyColor(sub.difficulty)"
              >
                {{ getDifficultyLabel(sub.difficulty) }}
              </span>
            </div>
            
            <CardTitle class="text-2xl mt-4 group-hover:text-nexus-accent transition-colors">
              {{ sub.name }}
            </CardTitle>
          </CardHeader>

          <CardContent class="space-y-4">
            <div class="flex items-center gap-2 text-gray-400 text-sm">
              <User class="w-4 h-4" />
              <span>{{ sub.teacher_name || 'No teacher assigned' }}</span>
            </div>
          </CardContent>

          <CardFooter class="border-t border-white/5 pt-4 mt-auto">
            <div class="flex items-center text-sm text-gray-400 group-hover:text-white transition-colors w-full justify-between">
              <span>View Details</span>
              <ArrowRight class="w-4 h-4 group-hover:translate-x-1 transition-transform text-nexus-accent" />
            </div>
          </CardFooter>

        </Card>
      </RouterLink>

    </div>
  </div>
</template>