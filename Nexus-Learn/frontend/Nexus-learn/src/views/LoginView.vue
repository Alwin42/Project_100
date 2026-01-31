<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardContent } from '@/components/ui/card'
import { ExclamationTriangleIcon, PersonIcon, LockClosedIcon } from '@radix-icons/vue' 
import ShufflingGrid from '@/components/ShufflingGrid.vue' 

const authStore = useAuthStore()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  isLoading.value = true
  errorMessage.value = ''
  try {
    await authStore.login(username.value, password.value)
  } catch (error) {
    errorMessage.value = 'Invalid credentials'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-[#09090b] text-white p-4 relative overflow-hidden">
    
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,_rgba(34,197,94,0.1),_transparent_50%)]"></div>
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_bottom_left,_rgba(59,130,246,0.1),_transparent_50%)]"></div>

    <Card 
      class="w-full max-w-4xl bg-black/40 backdrop-blur-2xl border-white/10 shadow-2xl overflow-hidden grid grid-cols-1 md:grid-cols-2 relative z-10"
      v-motion
      :initial="{ opacity: 0, scale: 0.98 }"
      :enter="{ opacity: 1, scale: 1, transition: { duration: 0.5 } }"
    >
      
      <div class="p-8 md:p-12 flex flex-col justify-center space-y-8">
        <div class="space-y-2">
          <h2 class="text-3xl font-bold tracking-tight text-white">Welcome Back</h2>
          <p class="text-gray-400">Enter your credentials to access the terminal.</p>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-6">
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-400">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-4">
            <div class="space-y-2">
              <Label class="text-xs uppercase tracking-wider text-gray-500 font-bold">Username</Label>
              <div class="relative group">
                <PersonIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                <Input v-model="username" class="pl-10 bg-white/5 border-white/10 focus:border-nexus-accent h-11" placeholder="Enter username" />
              </div>
            </div>

            <div class="space-y-2">
              <Label class="text-xs uppercase tracking-wider text-gray-500 font-bold">Password</Label>
              <div class="relative group">
                <LockClosedIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
                <Input v-model="password" type="password" class="pl-10 bg-white/5 border-white/10 focus:border-nexus-accent h-11" placeholder="••••••••" />
              </div>
            </div>
          </div>

          <Button type="submit" class="w-full h-11 bg-nexus-accent text-black font-bold hover:bg-emerald-400 transition-all shadow-[0_0_20px_rgba(34,197,94,0.3)]" :disabled="isLoading">
            {{ isLoading ? 'Authenticating...' : 'Sign In' }}
          </Button>

          <p class="text-center text-sm text-gray-500">
            Don't have an account? <a href="/register" class="text-nexus-accent hover:underline">Register</a>
          </p>
        </form>
      </div>

      <div class="hidden md:flex flex-col items-center justify-center bg-white/[0.02] border-l border-white/5 relative p-12">
        <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 mix-blend-overlay"></div>
        
        <div class="scale-100 mb-8">
            <ShufflingGrid />
        </div>

        <div class="mt-9 text-center space-y-2 max-w-xs relative z-10">
          <h3 class="text-xl font-bold text-white">Nexus Learn System</h3>
          <p class="text-sm text-gray-400">Secure, cloud-based academic management for the modern student.</p>
        </div>
      </div>

    </Card>
  </div>
</template>