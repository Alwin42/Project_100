<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card } from '@/components/ui/card'
import { PersonIcon, CalendarIcon, BackpackIcon, LaptopIcon, EnvelopeClosedIcon, LockClosedIcon, IdCardIcon, ExclamationTriangleIcon } from '@radix-icons/vue'
import ShufflingGrid from '@/components/ShufflingGrid.vue' // Import Animation

const authStore = useAuthStore()
const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')

const formData = ref({
  username: '', password: '', email: '', first_name: '',
  age: '', dob: '', college: '', course: ''
})

const handleRegister = async () => {
  isLoading.value = true
  errorMessage.value = ''
  try {
    // Construct payload (omitted for brevity, same as your code)
    const payload = {
        username: formData.value.username, password: formData.value.password, email: formData.value.email, first_name: formData.value.first_name,
        profile: { age: formData.value.age, dob: formData.value.dob, college: formData.value.college, course: formData.value.course }
    }
    await authStore.register(payload)
    router.push('/login')
  } catch (error) {
    errorMessage.value = "Registration failed."
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-[#09090b] text-white p-4 relative overflow-hidden">
    
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_bottom_right,_rgba(168,85,247,0.1),_transparent_50%)]"></div>

    <Card 
      class="w-full max-w-6xl bg-black/40 backdrop-blur-2xl border-white/10 shadow-2xl overflow-hidden grid grid-cols-1 lg:grid-cols-12 relative z-10"
      v-motion
      :initial="{ opacity: 0, y: 20 }"
      :enter="{ opacity: 1, y: 0, transition: { duration: 0.6 } }"
    >
      
      <div class="hidden lg:flex col-span-5 flex-col items-center justify-center bg-white/[0.02] border-r border-white/5 relative p-12">
        <div class="absolute inset-0 bg-gradient-to-b from-transparent to-black/50"></div>
        
        <div class="scale-125 mb-10">
            <ShufflingGrid />
        </div>

        <div class="text-center space-y-4 max-w-xs relative z-10">
          <h3 class="text-2xl font-bold text-white">Join the Network</h3>
          <p class="text-gray-400 leading-relaxed">Create your student profile to access cloud storage, timetable tracking, and academic analytics.</p>
        </div>
      </div>

      <div class="col-span-12 lg:col-span-7 p-8 md:p-12">
        <div class="mb-8">
          <h2 class="text-2xl font-bold text-white">Create Account</h2>
          <p class="text-gray-400 text-sm">Initialize your student workspace profile</p>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-5">
           <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-400">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
             <div class="space-y-2">
                <Label class="text-xs text-gray-500 font-bold uppercase">First Name</Label>
                <div class="relative"><PersonIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.first_name" class="pl-9 bg-white/5 border-white/10" placeholder="John" /></div>
             </div>
             <div class="space-y-2">
                <Label class="text-xs text-gray-500 font-bold uppercase">Age</Label>
                <div class="relative"><CalendarIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.age" type="number" class="pl-9 bg-white/5 border-white/10" placeholder="20" /></div>
             </div>
          </div>

          <div class="space-y-2">
             <Label class="text-xs text-gray-500 font-bold uppercase">College & Course</Label>
             <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
               <div class="relative"><BackpackIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.college" class="pl-9 bg-white/5 border-white/10" placeholder="College Name" /></div>
               <div class="relative"><LaptopIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.course" class="pl-9 bg-white/5 border-white/10" placeholder="Course" /></div>
             </div>
          </div>

           <div class="space-y-4 pt-4 border-t border-white/10">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="relative"><IdCardIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.username" class="pl-9 bg-white/5 border-white/10" placeholder="Username" /></div>
                <div class="relative"><EnvelopeClosedIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.email" type="email" class="pl-9 bg-white/5 border-white/10" placeholder="Email" /></div>
              </div>
              <div class="relative"><LockClosedIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500" /><Input v-model="formData.password" type="password" class="pl-9 bg-white/5 border-white/10" placeholder="Password" /></div>
           </div>

           <Button type="submit" class="w-full h-11 bg-white text-black font-bold hover:bg-gray-200 mt-4" :disabled="isLoading">
            {{ isLoading ? 'Creating Profile...' : 'Complete Registration' }}
          </Button>
          
           <p class="text-center text-sm text-gray-500 mt-4">
            Already have an account? <a href="/login" class="text-nexus-accent hover:underline">Login</a>
          </p>
        </form>
      </div>
    </Card>
  </div>
</template>