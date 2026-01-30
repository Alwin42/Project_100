<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { ExclamationTriangleIcon } from '@radix-icons/vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')

const form = ref({ 
  name: '', 
  difficulty: 2, // Default to Medium
  teacher_name: '', 
  youtube_link: '',
  wiki_link: '' 
})

const submit = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    // Make the API request
    await api.post('subjects/', form.value)
    
    // If successful, go to dashboard
    router.push('/dashboard')
    
  } catch (error) {
    console.error(error)
    // Show error on screen
    errorMessage.value = "Failed to add subject. Please check your inputs."
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader>
        <CardTitle class="text-nexus-accent">Add New Subject</CardTitle>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/50 border-red-900 text-white">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label>Subject Name</Label>
            <Input v-model="form.name" placeholder="e.g. Mathematics" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Teacher Name</Label>
            <Input v-model="form.teacher_name" placeholder="e.g. Dr. Smith" class="bg-white/5 border-white/10 text-white" />
          </div>

          <div class="space-y-2">
            <Label>Difficulty</Label>
            <select v-model="form.difficulty" class="w-full p-2 rounded bg-white/5 border border-white/10 text-white focus:outline-none focus:border-nexus-accent">
              <option :value="1">Easy</option>
              <option :value="2">Medium</option>
              <option :value="3">Hard</option>
              <option :value="4">Very Hard</option>
            </select>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-2">
              <Label>YouTube Link</Label>
              <Input v-model="form.youtube_link" placeholder="https://..." class="bg-white/5 border-white/10 text-white" />
            </div>
            <div class="space-y-2">
              <Label>Wiki/Docs Link</Label>
              <Input v-model="form.wiki_link" placeholder="https://..." class="bg-white/5 border-white/10 text-white" />
            </div>
          </div>

          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold" :disabled="isLoading">
            {{ isLoading ? 'Saving...' : 'Save Subject' }}
          </Button>

        </form>
      </CardContent>
    </Card>
  </div>
</template>