<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
// Importing icons for a premium feel
import { 
  ExclamationTriangleIcon, 
  PersonIcon, 
  CalendarIcon, 
  BackpackIcon, 
  LaptopIcon, 
  EnvelopeClosedIcon, 
  LockClosedIcon,
  IdCardIcon 
} from '@radix-icons/vue'

const authStore = useAuthStore()
const router = useRouter()

const formData = ref({
  username: '', password: '', email: '', first_name: '',
  age: '', dob: '', college: '', course: ''
})

const isLoading = ref(false)
const errorMessage = ref('')

const handleRegister = async () => {
  isLoading.value = true
  errorMessage.value = ''
  try {
    const payload = {
      username: formData.value.username,
      password: formData.value.password,
      email: formData.value.email,
      first_name: formData.value.first_name,
      profile: {
        age: formData.value.age,
        dob: formData.value.dob,
        college: formData.value.college,
        course: formData.value.course
      }
    }
    await authStore.register(payload)
    router.push('/login')
  } catch (error) {
    errorMessage.value = "Registration failed. Username might be taken."
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-nexus-main bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-gray-900 via-nexus-main to-nexus-main py-12 px-4 relative overflow-hidden">
    
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px]  rounded-full  pointer-events-none"></div>

    <Card 
      class="w-full max-w-xl bg-black/60 backdrop-blur-xl border-white/10 text-white shadow-2xl relative z-10"
      v-motion
      :initial="{ opacity: 0, y: 20 }"
      :enter="{ opacity: 1, y: 0, transition: { duration: 600 } }"
    >
      <CardHeader class="space-y-2">
        <div class="flex justify-center mb-2">
          <div class="h-10 w-10 rounded-lg bg-nexus-accent flex items-center justify-center shadow-[0_0_15px_rgba(29,205,159,0.4)]">
            <span class="text-black font-bold text-xl">N</span>
          </div>
        </div>
        <CardTitle class="text-3xl font-bold text-center tracking-tight">
          Join <span class="text-nexus-accent">Nexus Learn</span>
        </CardTitle>
        <CardDescription class="text-center text-gray-400 text-base">
          Initialize your student workspace profile
        </CardDescription>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="handleRegister" class="space-y-5">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/40 border-red-900/50 text-red-200">
            <ExclamationTriangleIcon class="h-4 w-4 text-red-400" />
            <AlertTitle class="text-red-400">Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="space-y-2">
              <Label class="text-gray-300 text-xs uppercase tracking-wider font-semibold">First Name</Label>
              <div class="relative">
                <PersonIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.first_name" placeholder="John" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
            </div>
            <div class="space-y-2">
              <Label class="text-gray-300 text-xs uppercase tracking-wider font-semibold">Age</Label>
              <div class="relative">
                <CalendarIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.age" type="number" placeholder="20" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
            </div>
          </div>

          <div class="space-y-2">
             <Label class="text-gray-300 text-xs uppercase tracking-wider font-semibold">Date of Birth</Label>
             <div class="relative">
               <Input 
                 v-model="formData.dob" 
                 type="date" 
                 class="bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20 [color-scheme:dark]" 
                 required 
                />
             </div>
          </div>

          <div class="space-y-2">
            <Label class="text-gray-300 text-xs uppercase tracking-wider font-semibold">Academic Details</Label>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="relative">
                <BackpackIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.college" placeholder="College Name" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
              <div class="relative">
                <LaptopIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.course" placeholder="Course / Major" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
            </div>
          </div>

          <div class="space-y-4 pt-2">
            <div class="relative flex py-2 items-center">
              <div class="flex-grow border-t border-white/10"></div>
              <span class="flex-shrink-0 mx-4 text-gray-500 text-xs uppercase">Account Credentials</span>
              <div class="flex-grow border-t border-white/10"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="relative">
                <IdCardIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.username" placeholder="Username" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
              <div class="relative">
                <EnvelopeClosedIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
                <Input v-model="formData.email" type="email" placeholder="Email Address" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
              </div>
            </div>

            <div class="relative">
              <LockClosedIcon class="absolute left-3 top-2.5 h-4 w-4 text-gray-500" />
              <Input v-model="formData.password" type="password" placeholder="Create Password" class="pl-9 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20" required />
            </div>
          </div>

          <Button 
            type="submit" 
            class="w-full h-11 text-base bg-nexus-accent hover:bg-nexus-dark text-black font-bold shadow-[0_0_20px_rgba(29,205,159,0.2)] hover:shadow-[0_0_30px_rgba(29,205,159,0.4)] transition-all duration-300 mt-6" 
            :disabled="isLoading"
          >
            {{ isLoading ? 'Initializing Profile...' : 'Complete Registration' }}
          </Button>

        </form>
      </CardContent>
      <CardFooter class="justify-center pb-8">
        <p class="text-sm text-gray-500">
          Already part of the system? <a href="/login" class="text-nexus-accent hover:text-white transition-colors hover:underline underline-offset-4">Login </a>
        </p>
      </CardFooter>
    </Card>
  </div>
</template>