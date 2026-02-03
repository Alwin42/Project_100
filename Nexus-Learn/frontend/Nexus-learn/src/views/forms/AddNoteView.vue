<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { FileText, Upload, BookOpen, ChevronDown } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter(); const route = useRoute()
const subjects = ref([]); const loading = ref(false)
const form = ref({ subject: '', title: '', file: null })

onMounted(async () => {
  try { const res = await api.get('subjects/'); subjects.value = res.data; if (route.query.subject) form.value.subject = Number(route.query.subject) } catch (e) {}
})
const handleFileChange = (e) => { form.value.file = e.target.files[0] }
const submit = async () => {
  if (!form.value.file || !form.value.subject) return alert("Select subject and file.")
  loading.value = true
  try {
    const fd = new FormData(); fd.append('subject', form.value.subject); fd.append('title', form.value.title); fd.append('file', form.value.file)
    await api.post('notes/', fd, { headers: { 'Content-Type': 'multipart/form-data' } })
    router.push(`/dashboard/subjects/${form.value.subject}`)
  } catch (e) { alert("Upload failed.") } finally { loading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />

    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-nexus-accent flex items-center justify-center shadow-lg shadow-nexus-accent/20"><Upload class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Upload <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-white">Note</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Subject</Label><div class="relative group"><BookOpen class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><select v-model="form.subject" class="w-full pl-12 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-nexus-accent outline-none appearance-none cursor-pointer"><option value="" disabled class="bg-gray-900">Select...</option><option v-for="s in subjects" :key="s.id" :value="s.id" class="bg-gray-900">{{ s.name }}</option></select><ChevronDown class="absolute right-4 top-4 w-4 h-4 text-gray-400 pointer-events-none" /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Title</Label><div class="relative group"><FileText class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><Input v-model="form.title" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent rounded-2xl" placeholder="e.g. Unit 1" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">File</Label><Input type="file" @change="handleFileChange" class="pt-2 h-12 bg-white/5 border-white/10 text-white file:text-nexus-accent rounded-2xl cursor-pointer" required /></div>

          <div class="flex gap-4 pt-4">
            <Button type="button" variant="ghost" class="w-1/3 text-gray-400 hover:text-white rounded-2xl" @click="router.back()">Cancel</Button>
            <Button type="submit" class="w-2/3 h-12 text-lg bg-nexus-accent hover:bg-nexus-dark text-black font-bold shadow-lg shadow-nexus-accent/20 rounded-2xl" :disabled="loading">{{ loading ? 'Uploading...' : 'Upload' }}</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>