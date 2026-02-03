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
import { TriangleAlert, Trophy, Type, FileText, Image } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')
const form = ref({ name: '', activity_type: '', description: '' })
const selectedImage = ref(null)

const handleFile = (e) => { selectedImage.value = e.target.files[0] }

const submit = async () => {
  isLoading.value = true; errorMessage.value = ''
  const fd = new FormData()
  fd.append('name', form.value.name); fd.append('activity_type', form.value.activity_type); fd.append('description', form.value.description)
  if (selectedImage.value) fd.append('image', selectedImage.value)

  try {
    await api.post('activities/', fd, { headers: { 'Content-Type': 'multipart/form-data' } })
    router.push('/dashboard')
  } catch (error) { errorMessage.value = "Failed to save activity." } finally { isLoading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    

    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-orange-500 flex items-center justify-center shadow-lg shadow-orange-500/20"><Trophy class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Log <span class="text-orange-500">Activity</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl"><TriangleAlert class="h-4 w-4" /><AlertTitle>Error</AlertTitle><AlertDescription>{{ errorMessage }}</AlertDescription></Alert>

          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Name</Label><div class="relative group"><Trophy class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-orange-500 transition-colors" /><Input v-model="form.name" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-orange-500 rounded-2xl" placeholder="e.g. Hackathon" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Type</Label><div class="relative group"><Type class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-orange-500 transition-colors" /><Input v-model="form.activity_type" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-orange-500 rounded-2xl" placeholder="e.g. Technical" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Description</Label><div class="relative group"><FileText class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-orange-500 transition-colors" /><Textarea v-model="form.description" class="pl-12 pt-3 bg-white/5 border-white/10 text-white focus:border-orange-500 rounded-2xl min-h-[100px]" placeholder="Details..." required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Image</Label><div class="relative group"><Image class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-orange-500 transition-colors" /><Input type="file" @change="handleFile" accept="image/*" class="pl-12 pt-2 h-12 bg-white/5 border-white/10 text-white file:text-orange-500 rounded-2xl cursor-pointer" /></div></div>

          <Button type="submit" class="w-full h-12 text-lg bg-orange-500 hover:bg-orange-400 text-black font-bold shadow-lg shadow-orange-500/20 rounded-2xl mt-4" :disabled="isLoading">{{ isLoading ? 'Saving...' : 'Save Activity' }}</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>