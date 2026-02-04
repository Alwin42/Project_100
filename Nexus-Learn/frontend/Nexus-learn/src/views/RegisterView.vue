<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card } from '@/components/ui/card'
import { 
  PersonIcon, CalendarIcon, BackpackIcon, LaptopIcon, 
  EnvelopeClosedIcon, LockClosedIcon, IdCardIcon, ExclamationTriangleIcon 
} from '@radix-icons/vue'
// Ensure you have ShufflingGrid or remove this import if not using the animation
import ShufflingGrid from '@/components/ShufflingGrid.vue' 

const authStore = useAuthStore()
const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')

const formData = ref({
  username: '', 
  password: '', 
  email: '', 
  first_name: '',
  age: '', 
  dob: '', 
  college: '', 
  course: ''
})

const handleRegister = async () => {
  isLoading.value = true
  errorMessage.value = ''
  
  try {
    // FIX 1: Send null if dob is empty to prevent backend "Invalid Date" error
    const dobValue = formData.value.dob === '' ? null : formData.value.dob

    const payload = {
        username: formData.value.username, 
        password: formData.value.password, 
        email: formData.value.email, 
        first_name: formData.value.first_name,
        profile: { 
          age: formData.value.age, 
          dob: dobValue, 
          college: formData.value.college, 
          course: formData.value.course 
        }
    }
    
    await authStore.register(payload)
    router.push('/login')
    
  } catch (error) {
    console.error("Registration Error:", error)
    
    // FIX 2: Handle Nested Errors to prevent "[object Object]"
    if (error.response && error.response.data) {
        const data = error.response.data
        let messages = []

        // Recursive function to flatten nested errors (e.g. profile.age errors)
        const extractErrors = (obj) => {
            for (const key in obj) {
                if (Array.isArray(obj[key])) {
                    messages.push(`${key}: ${obj[key].join(' ')}`)
                } else if (typeof obj[key] === 'object' && obj[key] !== null) {
                    extractErrors(obj[key])
                } else {
                    messages.push(String(obj[key]))
                }
            }
        }
        
        extractErrors(data)
        errorMessage.value = messages.join(' | ')
    } else {
        errorMessage.value = "Registration failed. Please check your connection."
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-[#09090b] text-white p-4 relative overflow-hidden">
    
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_bottom_right,_rgba(168,85,247,0.15),_transparent_50%)]"></div>
    <div class="absolute inset-0 opacity-20 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] pointer-events-none mix-blend-overlay"></div>

    <Card 
      class="w-full max-w-6xl bg-black/40 backdrop-blur-3xl border-white/10 shadow-2xl overflow-hidden grid grid-cols-1 lg:grid-cols-12 relative z-10 rounded-[2.5rem]"
      v-motion
      :initial="{ opacity: 0, y: 20 }"
      :enter="{ opacity: 1, y: 0, transition: { duration: 0.6 } }"
    >
      
      <div class="hidden lg:flex col-span-5 flex-col items-center justify-center bg-white/[0.02] border-r border-white/10 relative p-12">
        <div class="absolute inset-0 bg-gradient-to-b from-transparent to-black/60 pointer-events-none"></div>
        
        <div class="scale-125 mb-10">
            <ShufflingGrid />
        </div>

        <div class="text-center space-y-4 max-w-xs relative z-10">
          <h3 class="text-3xl font-black text-white tracking-tight">Join Nexus</h3>
          <p class="text-gray-400 font-medium leading-relaxed">The ultimate academic operating system for modern students.</p>
        </div>
      </div>

      <div class="col-span-12 lg:col-span-7 p-10 md:p-14 relative z-10">
        <div class="mb-8">
          <h2 class="text-3xl font-black text-white tracking-tight">Create Account</h2>
          <p class="text-gray-400 font-medium">Initialize your student workspace profile</p>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-6">
           <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
             <div class="space-y-2">
                <Label class="text-xs text-gray-500 font-bold uppercase ml-1">First Name</Label>
                <div class="relative group">
                    <PersonIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                    <Input v-model="formData.first_name" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="John" />
                </div>
             </div>
             <div class="space-y-2">
                <Label class="text-xs text-gray-500 font-bold uppercase ml-1">Age</Label>
                <div class="relative group">
                    <CalendarIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                    <Input v-model="formData.age" type="number" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="20" />
                </div>
             </div>
          </div>

          <div class="space-y-2">
             <Label class="text-xs text-gray-500 font-bold uppercase ml-1">College & Course</Label>
             <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
               <div class="relative group">
                   <BackpackIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                   <Input v-model="formData.college" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="College Name" />
               </div>
               <div class="relative group">
                   <LaptopIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                   <Input v-model="formData.course" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="Course" />
               </div>
             </div>
          </div>

          <div class="space-y-2">
             <Label class="text-xs text-gray-500 font-bold uppercase ml-1">Date of Birth</Label>
             <Input v-model="formData.dob" type="date" class="h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl px-4 [color-scheme:dark]" />
          </div>

           <div class="space-y-5 pt-6 border-t border-white/10">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                <div class="relative group">
                    <IdCardIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                    <Input v-model="formData.username" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="Username" />
                </div>
                <div class="relative group">
                    <EnvelopeClosedIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                    <Input v-model="formData.email" type="email" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="Email" />
                </div>
              </div>
              <div class="relative group">
                  <LockClosedIcon class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                  <Input v-model="formData.password" type="password" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:bg-white/10 rounded-2xl" placeholder="Password" />
              </div>
           </div>

           <Button type="submit" class="w-full h-12 bg-white text-black font-bold hover:bg-gray-200 mt-6 text-lg rounded-2xl shadow-lg" :disabled="isLoading">
            {{ isLoading ? 'Creating Profile...' : 'Complete Registration' }}
          </Button>
          
           <p class="text-center text-sm text-gray-500 mt-6 font-medium">
            Already have an account? <a href="/login" class="text-nexus-accent hover:text-white transition-colors underline-offset-4 hover:underline">Login</a>
          </p>
        </form>
      </div>
    </Card>
  </div>
</template>