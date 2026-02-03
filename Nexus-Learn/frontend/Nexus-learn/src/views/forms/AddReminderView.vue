<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { TriangleAlert, Bell, CheckCircle2, AlignLeft } from 'lucide-vue-next'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')
const form = ref({ title: '', priority: 'Medium', description: '' })

const submit = async () => {
  isLoading.value = true
  errorMessage.value = ''
  try {
    // Assuming 'tasks/' is the endpoint for reminders/tasks in your dashboard
    await api.post('tasks/', form.value)
    router.push('/dashboard')
  } catch (error) { 
    errorMessage.value = "Failed to add reminder. Please check your network." 
  } finally { 
    isLoading.value = false 
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-[#09090b] bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-gray-900 via-[#09090b] to-[#09090b] px-4 py-12 pt-24 text-white relative overflow-hidden">
    
    <div class="fixed inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 pointer-events-none mix-blend-overlay"></div>

    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2rem] animate-in fade-in zoom-in duration-500">
      
      <CardHeader class="pb-2 space-y-1 text-center">
        <div class="flex justify-center mb-4">
          <div class="h-12 w-12 rounded-xl bg-pink-500 flex items-center justify-center shadow-lg shadow-pink-500/20">
            <Bell class="h-6 w-6 text-black" />
          </div>
        </div>
        <CardTitle class="text-3xl font-black tracking-tight">
          Set <span class="text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-rose-400">Reminder</span>
        </CardTitle>
      </CardHeader>

      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl">
            <TriangleAlert class="h-4 w-4" /><AlertTitle>Error</AlertTitle><AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label class="text-xs uppercase tracking-widest text-gray-500 font-bold ml-1">Task / Reminder</Label>
            <div class="relative group">
              <CheckCircle2 class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-pink-500 transition-colors" />
              <Input 
                v-model="form.title" 
                class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-pink-500 focus:bg-white/10 focus:ring-0 rounded-2xl transition-all placeholder:text-gray-600" 
                placeholder="e.g. Submit Assignment"
                required 
              />
            </div>
          </div>

          <div class="space-y-2">
            <Label class="text-xs uppercase tracking-widest text-gray-500 font-bold ml-1">Priority</Label>
            <div class="relative">
              <select 
                v-model="form.priority" 
                class="w-full pl-4 pr-10 h-12 bg-white/5 border border-white/10 text-white rounded-2xl focus:border-pink-500 focus:bg-white/10 outline-none appearance-none cursor-pointer transition-all"
              >
                <option value="Low" class="bg-gray-900 text-gray-300">Low</option>
                <option value="Medium" class="bg-gray-900 text-gray-300">Medium</option>
                <option value="High" class="bg-gray-900 text-gray-300">High</option>
              </select>
              <div class="absolute right-4 top-4 pointer-events-none opacity-50">
                 <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
              </div>
            </div>
          </div>

          <div class="space-y-2">
            <Label class="text-xs uppercase tracking-widest text-gray-500 font-bold ml-1">Description (Optional)</Label>
            <div class="relative group">
              <AlignLeft class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-pink-500 transition-colors" />
              <Input 
                v-model="form.description" 
                class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-pink-500 focus:bg-white/10 focus:ring-0 rounded-2xl transition-all placeholder:text-gray-600" 
                placeholder="Details..."
              />
            </div>
          </div>

          <Button 
            type="submit" 
            class="w-full h-12 text-lg bg-pink-500 hover:bg-pink-400 text-black font-bold shadow-lg shadow-pink-500/20 transition-all duration-300 rounded-2xl mt-4" 
            :disabled="isLoading"
          >
            {{ isLoading ? 'Saving...' : 'Create Reminder' }}
          </Button>

        </form>
      </CardContent>
    </Card>
  </div>
</template>