<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { 
  UserCircle, 
  GraduationCap, 
  BookOpen, 
  CalendarDays, 
  Save, 
  X,
  CheckCircle2
} from 'lucide-vue-next'

const router = useRouter()
const isLoading = ref(false)
const isSaving = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

// Form State
const form = ref({ 
  age: '', 
  dob: '', 
  college: '', 
  course: '' 
})
const username = ref('')

// Load User Data
onMounted(async () => {
  isLoading.value = true
  try {
    const res = await api.get('user/')
    username.value = res.data.username
    // If profile exists, populate form
    if(res.data.profile) {
      form.value = { ...res.data.profile }
    }
  } catch (e) {
    console.error("Failed to load profile", e)
    errorMessage.value = "Failed to load profile data."
  } finally {
    isLoading.value = false
  }
})

// Submit Update
const submit = async () => {
  isSaving.value = true
  successMessage.value = ''
  errorMessage.value = ''

  try {
    // NOTE: We send the data wrapped in 'profile' if your serializer expects nested write,
    // or flat if you adjusted your View. Assuming standard nested PATCH:
    const payload = {
      profile: {
        age: form.value.age,
        dob: form.value.dob,
        college: form.value.college,
        course: form.value.course
      }
    }
    
    await api.patch('user/', payload)
    
    successMessage.value = "Profile updated successfully!"
    
    // Optional: Redirect after short delay
    setTimeout(() => {
      router.push('/dashboard')
    }, 1500)

  } catch (e) {
    console.error(e)
    errorMessage.value = "Failed to update profile. Please try again."
  } finally {
    isSaving.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    
    <Card class="w-full max-w-2xl bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative overflow-hidden">
      <div class="absolute top-0 right-0 w-64 h-64 bg-nexus-accent/10 rounded-full blur-[2px] -translate-y-1/2 translate-x-1/2 pointer-events-none"></div>

      <CardHeader class="border-b border-white/10 pb-6">
        <div class="flex items-center gap-4">
          <div class="w-16 h-16 rounded-full bg-gradient-to-br from-nexus-accent to-blue-600 flex items-center justify-center shadow-lg">
            <UserCircle class="w-10 h-10 text-black/80" />
          </div>
          <div>
            <CardTitle class="text-2xl font-bold text-white">Edit Profile</CardTitle>
            <p class="text-gray-400 text-sm">Update your academic details, {{ username }}</p>
          </div>
        </div>
      </CardHeader>

      <CardContent class="pt-6 space-y-6">
        
        <Alert v-if="successMessage" class="bg-green-500/10 border-green-500/50 text-green-400">
          <CheckCircle2 class="w-4 h-4" />
          <AlertDescription>{{ successMessage }}</AlertDescription>
        </Alert>
        
        <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/50 text-red-400">
          <X class="w-4 h-4" />
          <AlertDescription>{{ errorMessage }}</AlertDescription>
        </Alert>

        <form @submit.prevent="submit" class="space-y-6">
          
          <div class="grid gap-6 md:grid-cols-2">
            <div class="space-y-2">
              <Label class="text-gray-300">College / University</Label>
              <div class="relative">
                <GraduationCap class="absolute left-3 top-2.5 w-4 h-4 text-gray-500" />
                <Input 
                  v-model="form.college" 
                  placeholder="e.g. IIT Madras" 
                  class="pl-10 bg-white/5 border-white/10 text-white focus:border-nexus-accent/50 transition-all" 
                />
              </div>
            </div>

            <div class="space-y-2">
              <Label class="text-gray-300">Degree / Course</Label>
              <div class="relative">
                <BookOpen class="absolute left-3 top-2.5 w-4 h-4 text-gray-500" />
                <Input 
                  v-model="form.course" 
                  placeholder="e.g. B.Tech Computer Science" 
                  class="pl-10 bg-white/5 border-white/10 text-white focus:border-nexus-accent/50 transition-all" 
                />
              </div>
            </div>
          </div>

          <div class="grid gap-6 grid-cols-2">
            <div class="space-y-2">
              <Label class="text-gray-300">Age</Label>
              <div class="relative">
                <UserCircle class="absolute left-3 top-2.5 w-4 h-4 text-gray-500" />
                <Input 
                  type="number" 
                  v-model="form.age" 
                  class="pl-10 bg-white/5 border-white/10 text-white focus:border-nexus-accent/50" 
                />
              </div>
            </div>

            <div class="space-y-2">
              <Label class="text-gray-300">Date of Birth</Label>
              <div class="relative">
                <CalendarDays class="absolute left-3 top-2.5 w-4 h-4 text-gray-500" />
                <Input 
                  type="date" 
                  v-model="form.dob" 
                  class="pl-10 bg-white/5 border-white/10 text-white [color-scheme:dark] focus:border-nexus-accent/50" 
                />
              </div>
            </div>
          </div>

          <div class="flex gap-4 pt-4">
            <Button 
              type="button" 
              variant="outline" 
              class="w-full border-white/10 hover:bg-white/10 text-white"
              @click="router.back()"
            >
              Cancel
            </Button>
            
            <Button 
              type="submit" 
              class="w-full bg-nexus-accent text-black font-bold hover:bg-nexus-accent/90 transition-colors"
              :disabled="isSaving"
            >
              <Save v-if="!isSaving" class="w-4 h-4 mr-2" />
              <div v-else class="animate-spin w-4 h-4 border-2 border-black border-t-transparent rounded-full mr-2"></div>
              {{ isSaving ? 'Saving...' : 'Save Changes' }}
            </Button>
          </div>

        </form>
      </CardContent>
    </Card>
  </div>
</template>