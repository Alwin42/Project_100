<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Upload, FileText, Cloud } from 'lucide-vue-next'

const router = useRouter()
const loading = ref(false)
const form = ref({
  title: '',
  file: null
})

const handleFileChange = (e) => {
  form.value.file = e.target.files[0]
}

const submit = async () => {
  if (!form.value.file || !form.value.title) {
    alert("Please select a file and enter a title.")
    return
  }

  loading.value = true
  try {
    const formData = new FormData()
    formData.append('title', form.value.title)
    formData.append('file', form.value.file)

    // Note: 'files/' matches the URL we registered in Step 3
    await api.post('files/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    
    router.push('/dashboard/cloud')
  } catch (e) {
    console.error("Upload failed", e)
    alert("Failed to upload file.")
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex items-center justify-center min-h-[60vh] p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white relative overflow-hidden">
      <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/20 rounded-full blur-[80px]"></div>

      <CardHeader>
        <CardTitle class="text-2xl flex items-center gap-2">
          <Cloud class="w-6 h-6 text-blue-400" />
          Upload to Cloud
        </CardTitle>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="submit" class="space-y-6">
          <div class="space-y-2">
            <Label>File Title</Label>
            <Input v-model="form.title" placeholder="e.g. Project Proposal" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Select File</Label>
            <div class="border-2 border-dashed border-white/10 rounded-xl p-8 text-center hover:bg-white/5 transition-colors cursor-pointer relative">
                <input type="file" @change="handleFileChange" class="absolute inset-0 opacity-0 cursor-pointer" required />
                <Upload class="w-8 h-8 text-gray-400 mx-auto mb-2" />
                <p class="text-sm text-gray-400" v-if="!form.file">Click to browse or drag file here</p>
                <p class="text-sm text-nexus-accent font-bold" v-else>{{ form.file.name }}</p>
            </div>
          </div>

          <div class="flex gap-4 pt-2">
            <Button type="button" variant="ghost" class="w-full text-gray-400 hover:text-white" @click="router.back()">Cancel</Button>
            <Button type="submit" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold" :disabled="loading">
              {{ loading ? 'Uploading...' : 'Upload File' }}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>