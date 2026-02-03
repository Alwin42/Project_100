<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { TriangleAlert, BookOpen, User, MonitorPlay, FileText, ChevronDown } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')
const form = ref({ name: '', difficulty: 2, teacher_name: '', youtube_link: '', wiki_link: '' })

const submit = async () => {
  isLoading.value = true; errorMessage.value = ''
  try { await api.post('subjects/', form.value); router.push('/dashboard') } 
  catch (error) { errorMessage.value = "Failed to add subject." } finally { isLoading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-indigo-500 flex items-center justify-center shadow-lg shadow-indigo-500/20"><BookOpen class="h-6 w-6 text-white" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">New <span class="text-indigo-500">Subject</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl"><TriangleAlert class="h-4 w-4" /><AlertTitle>Error</AlertTitle><AlertDescription>{{ errorMessage }}</AlertDescription></Alert>

          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Subject Name</Label><div class="relative group"><BookOpen class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" /><Input v-model="form.name" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-indigo-500 rounded-2xl" placeholder="e.g. Math" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Teacher</Label><div class="relative group"><User class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" /><Input v-model="form.teacher_name" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-indigo-500 rounded-2xl" placeholder="e.g. Dr. Stone" /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Difficulty</Label><div class="relative"><select v-model="form.difficulty" class="w-full pl-4 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-indigo-500 outline-none appearance-none cursor-pointer"><option :value="1" class="bg-gray-900">Easy</option><option :value="2" class="bg-gray-900">Medium</option><option :value="3" class="bg-gray-900">Hard</option></select><ChevronDown class="absolute right-4 top-4 w-4 h-4 text-gray-400 pointer-events-none" /></div></div>
          
          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">YouTube</Label><div class="relative group"><MonitorPlay class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" /><Input v-model="form.youtube_link" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-indigo-500 rounded-2xl" placeholder="URL..." /></div></div>
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Wiki</Label><div class="relative group"><FileText class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-indigo-500 transition-colors" /><Input v-model="form.wiki_link" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-indigo-500 rounded-2xl" placeholder="URL..." /></div></div>
          </div>

          <Button type="submit" class="w-full h-12 text-lg bg-indigo-500 hover:bg-indigo-400 text-white font-bold shadow-lg shadow-indigo-500/20 rounded-2xl mt-4" :disabled="isLoading">{{ isLoading ? 'Saving...' : 'Save Subject' }}</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>