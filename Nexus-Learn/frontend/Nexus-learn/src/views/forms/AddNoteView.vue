<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router' // Import useRoute
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { FileText, Upload, BookOpen, ChevronDown } from 'lucide-vue-next'

const router = useRouter()
const route = useRoute() // Get current route to check for pre-selected subject
const subjects = ref([])
const loading = ref(false)

const form = ref({
  subject: '',
  title: '',
  file: null
})

onMounted(async () => {
  try {
    const res = await api.get('subjects/')
    subjects.value = res.data

    // AUTO-SELECT: If URL has ?subject=5, auto-select it
    if (route.query.subject) {
      form.value.subject = Number(route.query.subject)
    }
  } catch (e) {
    console.error("Failed to load subjects", e)
  }
})

const handleFileChange = (e) => {
  form.value.file = e.target.files[0]
}

const submit = async () => {
  if (!form.value.file || !form.value.subject) {
    alert("Please select a subject and a file.")
    return
  }

  loading.value = true
  try {
    const formData = new FormData()
    formData.append('subject', form.value.subject)
    formData.append('title', form.value.title)
    formData.append('file', form.value.file)

    await api.post('notes/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    
    // Redirect to the subject details page
    router.push(`/dashboard/subjects/${form.value.subject}`)
  } catch (e) {
    console.error("Failed to upload note", e)
    alert("Upload failed. Please try again.")
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex items-center justify-center min-h-[60vh] p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white relative overflow-hidden z-10">
      
      <div class="absolute top-0 left-0 w-32 h-32 bg-nexus-accent/20 rounded-full blur-[80px] pointer-events-none"></div>

      <CardHeader>
        <CardTitle class="text-2xl flex items-center gap-2 relative z-10">
          <Upload class="w-6 h-6 text-nexus-accent" />
          Upload Note
        </CardTitle>
      </CardHeader>
      
      <CardContent class="relative z-10">
        <form @submit.prevent="submit" class="space-y-6">
          
          <div class="space-y-2">
            <Label>Select Subject</Label>
            <div class="relative">
              <BookOpen class="absolute left-3 top-2.5 w-4 h-4 text-gray-500 pointer-events-none" />
              
              <select 
                v-model="form.subject"
                class="w-full pl-10 pr-10 h-10 rounded-md bg-white/5 border border-white/10 text-white focus:border-nexus-accent outline-none appearance-none cursor-pointer"
                required
              >
                <option value="" disabled class="bg-gray-900 text-gray-400">Choose a subject...</option>
                <option 
                  v-for="sub in subjects" 
                  :key="sub.id" 
                  :value="sub.id" 
                  class="bg-gray-900 text-white"
                >
                  {{ sub.name }}
                </option>
              </select>

              <ChevronDown class="absolute right-3 top-3 w-4 h-4 text-gray-400 pointer-events-none" />
            </div>
            <p v-if="subjects.length === 0" class="text-xs text-red-400 mt-1">
              No subjects found. Please add a subject first.
            </p>
          </div>

          <div class="space-y-2">
            <Label>Note Title</Label>
            <div class="relative">
              <FileText class="absolute left-3 top-2.5 w-4 h-4 text-gray-500 pointer-events-none" />
              <Input 
                v-model="form.title" 
                placeholder="e.g. Chapter 1 Summary" 
                class="pl-10 bg-white/5 border-white/10 text-white focus:border-nexus-accent" 
                required
              />
            </div>
          </div>

          <div class="space-y-2">
            <Label>PDF / Document</Label>
            <Input 
              type="file" 
              @change="handleFileChange" 
              class="bg-white/5 border-white/10 text-white file:text-nexus-accent file:bg-white/10 file:border-0 file:rounded-md file:mr-4 file:px-2 cursor-pointer" 
              required
            />
          </div>

          <div class="flex gap-4 pt-2">
            <Button type="button" variant="ghost" class="w-full text-white hover:bg-white/10" @click="router.back()">
              Cancel
            </Button>
            <Button type="submit" class="w-full bg-nexus-accent text-black font-bold hover:bg-nexus-accent/90" :disabled="loading">
              {{ loading ? 'Uploading...' : 'Upload Note' }}
            </Button>
          </div>

        </form>
      </CardContent>
    </Card>
  </div>
</template>