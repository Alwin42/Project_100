<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { TriangleAlert, Bell, CheckCircle2, AlignLeft, ChevronDown } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')
const form = ref({ title: '', priority: 'Medium', description: '' })

const submit = async () => {
  isLoading.value = true; errorMessage.value = ''
  try { await api.post('tasks/', form.value); router.push('/dashboard') } 
  catch (error) { errorMessage.value = "Failed to add reminder." } finally { isLoading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-pink-500 flex items-center justify-center shadow-lg shadow-pink-500/20"><Bell class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Set <span class="text-pink-500">Reminder</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl"><TriangleAlert class="h-4 w-4" /><AlertTitle>Error</AlertTitle><AlertDescription>{{ errorMessage }}</AlertDescription></Alert>

          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Task</Label><div class="relative group"><CheckCircle2 class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-pink-500 transition-colors" /><Input v-model="form.title" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-pink-500 rounded-2xl" placeholder="e.g. Assignment" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Priority</Label><div class="relative"><select v-model="form.priority" class="w-full pl-4 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-pink-500 outline-none appearance-none cursor-pointer"><option class="bg-gray-900">Low</option><option class="bg-gray-900">Medium</option><option class="bg-gray-900">High</option></select><ChevronDown class="absolute right-4 top-4 w-4 h-4 text-gray-400 pointer-events-none" /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Description</Label><div class="relative group"><AlignLeft class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-pink-500 transition-colors" /><Input v-model="form.description" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-pink-500 rounded-2xl" placeholder="Details..." /></div></div>

          <Button type="submit" class="w-full h-12 text-lg bg-pink-500 hover:bg-pink-400 text-black font-bold shadow-lg shadow-pink-500/20 rounded-2xl mt-4" :disabled="isLoading">{{ isLoading ? 'Saving...' : 'Create Reminder' }}</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>