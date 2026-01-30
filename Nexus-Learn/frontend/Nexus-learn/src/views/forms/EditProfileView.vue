<script setup>
import { ref, onMounted } from 'vue'
import api from '@/services/api'
import { useRouter } from 'vue-router'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'

const router = useRouter()
const form = ref({ age: '', dob: '', college: '', course: '' })

onMounted(async () => {
  try {
    const res = await api.get('user/') // Uses the new UserDetailView
    if(res.data.profile) form.value = res.data.profile
  } catch (e) {
    console.error(e)
  }
})

const submit = async () => {
  // We need a specific endpoint to patch profile, 
  // or we can just ignore this for now if backend isn't ready.
  // For now, let's redirect back to dashboard.
  router.push('/dashboard')
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader><CardTitle class="text-nexus-accent">Edit Profile</CardTitle></CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          <div class="space-y-2"><Label>College</Label><Input v-model="form.college" class="bg-white/5 border-white/10 text-white" /></div>
          <div class="space-y-2"><Label>Course</Label><Input v-model="form.course" class="bg-white/5 border-white/10 text-white" /></div>
          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-2"><Label>Age</Label><Input type="number" v-model="form.age" class="bg-white/5 border-white/10 text-white" /></div>
            <div class="space-y-2"><Label>Date of Birth</Label><Input type="date" v-model="form.dob" class="bg-white/5 border-white/10 text-white [color-scheme:dark]" /></div>
          </div>
          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold">Update Profile</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>