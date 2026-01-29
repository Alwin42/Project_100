<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'

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
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
    <Card class="w-full max-w-md">
      
      <CardHeader class="space-y-1">
        <CardTitle class="text-2xl font-bold text-center">Student Login</CardTitle>
        <CardDescription class="text-center">
          Enter your credentials to access your dashboard
        </CardDescription>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="handleLogin" class="space-y-4">
          
          <div class="space-y-2">
            <Label for="username">Username</Label>
            <Input 
              id="username" 
              v-model="username" 
              type="text" 
              placeholder="Enter your username" 
              required
            />
          </div>

          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <Label for="password">Password</Label>
              </div>
            <Input 
              id="password" 
              v-model="password" 
              type="password" 
              placeholder="••••••••" 
              required
            />
          </div>

          <div v-if="errorMessage" class="text-sm text-red-500 font-medium text-center">
            {{ errorMessage }}
          </div>

          <Button type="submit" class="w-full" :disabled="isLoading">
            {{ isLoading ? 'Signing in...' : 'Sign In' }}
          </Button>

        </form>
      </CardContent>
      
      <CardFooter class="text-center text-sm text-gray-500 justify-center">
        Don't have an account? Contact your administrator.
      </CardFooter>

    </Card>
  </div>
</template>