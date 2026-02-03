<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Upload, Cloud, Type } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const loading = ref(false)
const form = ref({ title: '', file: null })

const handleFileChange = (e) => { form.value.file = e.target.files[0] }

const submit = async () => {
  if (!form.value.file || !form.value.title) { alert("Please select a file."); return }
  loading.value = true
  try {
    const formData = new FormData(); formData.append('title', form.value.title); formData.append('file', form.value.file)
    await api.post('files/', formData, { headers: { 'Content-Type': 'multipart/form-data' } })
    router.push('/dashboard/cloud')
  } catch (e) { alert("Failed to upload.") } finally { loading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-blue-500 flex items-center justify-center shadow-lg shadow-blue-500/20"><Cloud class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Upload <span class="text-blue-500">File</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Title</Label><div class="relative group"><Type class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-blue-500 transition-colors" /><Input v-model="form.title" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-blue-500 rounded-2xl" placeholder="e.g. Project Proposal" required /></div></div>
          
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">File</Label>
            <div class="border-2 border-dashed border-white/10 rounded-2xl p-8 text-center hover:bg-white/5 hover:border-blue-500/50 transition-colors cursor-pointer relative group">
                <input type="file" @change="handleFileChange" class="absolute inset-0 opacity-0 cursor-pointer" required />
                <Upload class="w-8 h-8 text-gray-400 group-hover:text-blue-500 transition-colors mx-auto mb-2" />
                <p class="text-sm text-gray-400" v-if="!form.file">Click or drag file here</p>
                <p class="text-sm text-blue-500 font-bold" v-else>{{ form.file.name }}</p>
            </div>
          </div>

          <div class="flex gap-4 pt-4">
            <Button type="button" variant="ghost" class="w-1/3 text-gray-400 hover:text-white rounded-2xl" @click="router.back()">Cancel</Button>
            <Button type="submit" class="w-2/3 h-12 text-lg bg-blue-500 hover:bg-blue-400 text-black font-bold shadow-lg shadow-blue-500/20 rounded-2xl" :disabled="loading">{{ loading ? 'Uploading...' : 'Upload File' }}</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>