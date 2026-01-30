<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'

const router = useRouter()
const subjects = ref([])
const form = ref({ subject: '', day: 'Mon', start_time: '', end_time: '', room_number: '' })

onMounted(async () => {
  const res = await api.get('subjects/')
  subjects.value = res.data
})
const submit = async () => { await api.post('timetable/', form.value); router.push('/dashboard') }
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader><CardTitle class="text-nexus-accent">Add Class</CardTitle></CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          <div class="space-y-2"><Label>Subject</Label>
            <select v-model="form.subject" class="w-full p-2 bg-white/5 border border-white/10 text-white rounded">
              <option v-for="s in subjects" :key="s.id" :value="s.id">{{ s.name }}</option>
            </select>
          </div>
          <div class="space-y-2"><Label>Day</Label>
            <select v-model="form.day" class="w-full p-2 bg-white/5 border border-white/10 text-white rounded">
              <option value="Mon">Monday</option><option value="Tue">Tuesday</option><option value="Wed">Wednesday</option>
              <option value="Thu">Thursday</option><option value="Fri">Friday</option>
            </select>
          </div>
          <div class="grid grid-cols-2 gap-4">
             <div class="space-y-2"><Label>Start</Label><Input type="time" v-model="form.start_time" class="bg-white/5 border-white/10 text-white [color-scheme:dark]" /></div>
             <div class="space-y-2"><Label>End</Label><Input type="time" v-model="form.end_time" class="bg-white/5 border-white/10 text-white [color-scheme:dark]" /></div>
          </div>
          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold">Save Class</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>