<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Textarea } from '@/components/ui/textarea'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { ExclamationTriangleIcon } from '@radix-icons/vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')

const form = ref({ 
  name: '', 
  activity_type: '', 
  description: '' 
})
const selectedImage = ref(null)

const handleFile = (e) => { 
  selectedImage.value = e.target.files[0] 
}

const submit = async () => {
  isLoading.value = true
  errorMessage.value = ''

  const fd = new FormData()
  fd.append('name', form.value.name)
  fd.append('activity_type', form.value.activity_type)
  fd.append('description', form.value.description)
  
  if (selectedImage.value) {
    fd.append('image', selectedImage.value)
  }

  try {
    // Explicitly set header for file upload
    await api.post('activities/', fd, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    router.push('/dashboard')
  } catch (error) {
    console.error(error)
    if (error.response && error.response.data) {
      // Show the specific error from Django (e.g., "Image too large" or "This field is required")
      // This converts the error object into a readable string
      const serverErrors = Object.values(error.response.data).flat().join(', ')
      errorMessage.value = serverErrors || "Server rejected the data."
    } else {
      errorMessage.value = "Failed to save activity."
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader>
        <CardTitle class="text-nexus-accent">Log Activity</CardTitle>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/50 border-red-900 text-white mb-4">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label>Name</Label>
            <Input v-model="form.name" placeholder="e.g. Hackathon" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Type</Label>
            <Input v-model="form.activity_type" placeholder="e.g. Technical" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Description</Label>
            <Textarea v-model="form.description" placeholder="Details..." class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Image (Optional)</Label>
            <Input type="file" @change="handleFile" accept="image/*" class="bg-white/5 border-white/10 text-white file:text-nexus-accent file:font-bold" />
          </div>

          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold" :disabled="isLoading">
            {{ isLoading ? 'Saving...' : 'Save' }}
          </Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>