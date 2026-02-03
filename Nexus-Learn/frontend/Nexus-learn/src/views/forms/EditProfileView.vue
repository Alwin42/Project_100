<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { UserCircle, GraduationCap, BookOpen, CalendarDays, Save, CheckCircle2, X } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'

const router = useRouter()
const isLoading = ref(false)
const isSaving = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const form = ref({ age: '', dob: '', college: '', course: '' })
const username = ref('')

onMounted(async () => {
  isLoading.value = true
  try { const res = await api.get('user/'); username.value = res.data.username; if(res.data.profile) form.value = { ...res.data.profile } } 
  catch (e) { errorMessage.value = "Failed to load profile." } finally { isLoading.value = false }
})

const submit = async () => {
  isSaving.value = true; successMessage.value = ''; errorMessage.value = ''
  try { await api.patch('user/', { profile: form.value }); successMessage.value = "Profile updated!"; setTimeout(() => { router.push('/dashboard') }, 1500) } 
  catch (e) { errorMessage.value = "Update failed." } finally { isSaving.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <div class="fixed inset-0  pointer-events-none mix-blend-overlay"></div>

    <Card class="w-full max-w-2xl bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="border-b border-white/10 pb-6">
        <div class="flex items-center gap-4">
          <div class="w-16 h-16 rounded-2xl bg-gradient-to-br from-nexus-accent to-blue-600 flex items-center justify-center shadow-lg"><UserCircle class="w-10 h-10 text-black/80" /></div>
          <div><CardTitle class="text-2xl font-bold text-white">Edit Profile</CardTitle><p class="text-gray-400 text-sm">Update details for {{ username }}</p></div>
        </div>
      </CardHeader>

      <CardContent class="pt-6 space-y-6">
        <Alert v-if="successMessage" class="bg-green-500/10 border-green-500/50 text-green-400 rounded-2xl"><CheckCircle2 class="w-4 h-4" /><AlertDescription>{{ successMessage }}</AlertDescription></Alert>
        <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/50 text-red-400 rounded-2xl"><X class="w-4 h-4" /><AlertDescription>{{ errorMessage }}</AlertDescription></Alert>

        <form @submit.prevent="submit" class="space-y-6">
          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">College</Label><div class="relative group"><GraduationCap class="absolute left-4 top-3.5 w-4 h-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><Input v-model="form.college" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent rounded-2xl" /></div></div>
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Course</Label><div class="relative group"><BookOpen class="absolute left-4 top-3.5 w-4 h-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><Input v-model="form.course" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent rounded-2xl" /></div></div>
          </div>
          <div class="grid gap-6 grid-cols-2">
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Age</Label><div class="relative group"><UserCircle class="absolute left-4 top-3.5 w-4 h-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><Input type="number" v-model="form.age" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent rounded-2xl" /></div></div>
            <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Date of Birth</Label><div class="relative group"><CalendarDays class="absolute left-4 top-3.5 w-4 h-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" /><Input type="date" v-model="form.dob" class="pl-12 h-12 bg-white/5 border-white/10 text-white [color-scheme:dark] focus:border-nexus-accent rounded-2xl" /></div></div>
          </div>
          <div class="flex gap-4 pt-4">
            <Button type="button" variant="ghost" class="w-full text-white hover:bg-white/10 rounded-2xl" @click="router.back()">Cancel</Button>
            <Button type="submit" class="w-full bg-nexus-accent text-black font-bold hover:bg-emerald-400 rounded-2xl shadow-lg shadow-emerald-500/20" :disabled="isSaving"><Save v-if="!isSaving" class="w-4 h-4 mr-2" />{{ isSaving ? 'Saving...' : 'Save Changes' }}</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  </div>
</template>