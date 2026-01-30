<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { ExclamationTriangleIcon } from '@radix-icons/vue'

const router = useRouter()
const subjects = ref([])
const form = ref({ title: '', subject: '' })
const file = ref(null)
const isLoading = ref(false)
const errorMessage = ref('')

onMounted(async () => { 
  try {
    const res = await api.get('subjects/') 
    subjects.value = res.data 
  } catch (error) {
    console.error("Failed to load subjects", error)
  }
})

const handleFile = (e) => { 
  file.value = e.target.files[0] 
}

const submit = async () => {
  if (!file.value) {
    errorMessage.value = "Please select a file."
    return
  }
  if (!form.value.subject) {
    errorMessage.value = "Please select a subject."
    return
  }

  isLoading.value = true
  errorMessage.value = ''

  const fd = new FormData()
  fd.append('title', form.value.title)
  fd.append('subject', form.value.subject)
  fd.append('file', file.value)

  try {
    // --- THE FIX ---
    // Explicitly tell api.js to use multipart/form-data for this request
    await api.post('notes/', fd, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    router.push('/dashboard')
  } catch (error) {
    console.error(error)
    if (error.response && error.response.status === 401) {
       errorMessage.value = "Session expired. Please logout and login again."
    } else if (error.response && error.response.data) {
      const serverErrors = Object.values(error.response.data).flat().join(', ')
      errorMessage.value = serverErrors || "Server rejected the data."
    } else {
      errorMessage.value = "Failed to upload note."
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-md bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader>
        <CardTitle class="text-nexus-accent">Upload Note</CardTitle>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/50 border-red-900 text-white mb-4">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label>Title</Label>
            <Input v-model="form.title" placeholder="e.g. Unit 1 Notes" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Subject</Label>
            <select v-model="form.subject" class="w-full p-2 bg-white/5 border border-white/10 text-white rounded focus:outline-none focus:ring-2 focus:ring-nexus-accent/50" required>
              <option value="" disabled selected>Select Subject</option>
              <option v-for="s in subjects" :key="s.id" :value="s.id">{{ s.name }}</option>
            </select>
          </div>

          <div class="space-y-2">
            <Label>File (PDF/DOC)</Label>
            <Input type="file" @change="handleFile" class="bg-white/5 border-white/10 text-white file:text-nexus-accent file:font-bold" required />
          </div>

          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold" :disabled="isLoading">
             {{ isLoading ? 'Uploading...' : 'Upload' }}
          </Button>

        </form>
      </CardContent>
    </Card>
  </div>
</template>