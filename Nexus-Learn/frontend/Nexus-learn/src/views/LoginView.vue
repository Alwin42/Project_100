<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert' 
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
import { ExclamationTriangleIcon } from '@radix-icons/vue' // Standard Shadcn Icon

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
  <div class="min-h-screen flex items-center justify-center bg-nexus-main px-4 text-white">
    
    <Card class="w-full max-w-md bg-nexus-card border-gray-800 text-white shadow-2xl">
      
      <CardHeader class="space-y-1">
        <CardTitle class="text-3xl font-bold text-center text-nexus-accent">Nexus Login</CardTitle>
        <CardDescription class="text-center text-gray-400">
          Enter your credentials to access the system
        </CardDescription>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="handleLogin" class="space-y-6">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/50 border-red-900 text-white">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label for="username" class="text-gray-300">Username</Label>
            <Input 
              id="username" 
              v-model="username" 
              type="text" 
              placeholder="Enter your username" 
              class="bg-nexus-main border-gray-700 text-white focus:border-nexus-accent placeholder:text-gray-600"
              required
            />
          </div>

          <div class="space-y-2">
            <Label for="password" class="text-gray-300">Password</Label>
            <Input 
              id="password" 
              v-model="password" 
              type="password" 
              placeholder="••••••••" 
              class="bg-nexus-main border-gray-700 text-white focus:border-nexus-accent placeholder:text-gray-600"
              required
            />
          </div>

          <Button 
            type="submit" 
            class="w-full bg-nexus-accent hover:bg-nexus-dark text-black font-bold transition-colors" 
            :disabled="isLoading"
          >
            {{ isLoading ? 'Accessing System...' : 'Initialize Session' }}
          </Button>

        </form>
      </CardContent>
      
      <CardFooter class="justify-center">
        <p class="text-sm text-gray-500">
          New User? <a href="/register" class="text-nexus-accent hover:underline">Create Account</a>
        </p>
      </CardFooter>

    </Card>
  </div>
</template>