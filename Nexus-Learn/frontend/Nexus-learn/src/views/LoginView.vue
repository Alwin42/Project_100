<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
// Enhanced Icons
import { ExclamationTriangleIcon, PersonIcon, LockClosedIcon } from '@radix-icons/vue' 

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
    errorMessage.value = 'Invalid username or password'
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-nexus-main bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-gray-900 via-nexus-main to-nexus-main px-4 text-white relative overflow-hidden">
    
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] rounded-full  pointer-events-none"></div>

    <Card 
      class="w-full max-w-md bg-black/60 backdrop-blur-xl border-white/10 text-white shadow-2xl relative z-10"
      v-motion
      :initial="{ opacity: 0, scale: 0.95 }"
      :enter="{ opacity: 1, scale: 1, transition: { duration: 600 } }"
    >
      
      <CardHeader class="space-y-2">
        <div class="flex justify-center mb-4">
          <div class="h-12 w-12 rounded-xl bg-nexus-accent flex items-center justify-center shadow-[0_0_20px_rgba(29,205,159,0.3)]">
            <span class="text-black font-bold text-2xl">N</span>
          </div>
        </div>

        <CardTitle class="text-3xl font-bold text-center tracking-tight">
          Welcome <span class="text-nexus-accent">Back</span>
        </CardTitle>
        <CardDescription class="text-center text-gray-400 text-base">
          Enter your credentials to access the terminal
        </CardDescription>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="handleLogin" class="space-y-6">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/40 border-red-900/50 text-red-200 shadow-[0_0_10px_rgba(220,38,38,0.2)]">
            <ExclamationTriangleIcon class="h-4 w-4 text-red-400" />
            <AlertTitle class="text-red-400">Access Denied</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label for="username" class="text-gray-300 text-xs uppercase tracking-wider font-semibold">Username</Label>
            <div class="relative group">
              <PersonIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
              <Input 
                id="username" 
                v-model="username" 
                type="text" 
                placeholder="Enter your username" 
                class="pl-10 h-11 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20 placeholder:text-gray-600 transition-all"
                required
              />
            </div>
          </div>

          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <Label for="password" class="text-gray-300 text-xs uppercase tracking-wider font-semibold">Password</Label>
              <a href="#" class="text-xs text-nexus-accent hover:text-white transition-colors">Forgot password?</a>
            </div>
            <div class="relative group">
              <LockClosedIcon class="absolute left-3 top-3 h-4 w-4 text-gray-500 group-focus-within:text-nexus-accent transition-colors" />
              <Input 
                id="password" 
                v-model="password" 
                type="password" 
                placeholder="••••••••" 
                class="pl-10 h-11 bg-white/5 border-white/10 text-white focus:border-nexus-accent focus:ring-nexus-accent/20 placeholder:text-gray-600 transition-all"
                required
              />
            </div>
          </div>

          <Button 
            type="submit" 
            class="w-full h-11 text-base bg-nexus-accent hover:bg-nexus-dark text-black font-bold shadow-[0_0_20px_rgba(29,205,159,0.2)] hover:shadow-[0_0_30px_rgba(29,205,159,0.4)] transition-all duration-300" 
            :disabled="isLoading"
          >
            {{ isLoading ? 'Authenticating...' : 'Initialize Session' }}
          </Button>

        </form>
      </CardContent>
      
      <CardFooter class="justify-center pb-8">
        <p class="text-sm text-gray-500">
          New User? <a href="/register" class="text-nexus-accent hover:text-white transition-colors hover:underline underline-offset-4">Create Account</a>
        </p>
      </CardFooter>

    </Card>
  </div>
</template>