<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const formData = ref({
  username: '',
  password: '',
  email: '',
  first_name: '',
  // Profile specific fields
  age: '',
  dob: '',
  college: '',
  course: ''
})

const isLoading = ref(false)
const errorMessage = ref('')

const handleRegister = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    // We need to structure the data exactly how the Backend expects it
    // The 'profile' data must be nested inside a "profile" object
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
    
    // If successful, redirect to login
    router.push('/login')
    
  } catch (error) {
    console.error(error)
    errorMessage.value = "Registration failed. Username might be taken."
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <Card class="w-full max-w-lg">
      <CardHeader>
        <CardTitle class="text-2xl font-bold text-center">Create Account</CardTitle>
        <CardDescription class="text-center">Join Nexus Learn today</CardDescription>
      </CardHeader>
      
      <CardContent>
        <form @submit.prevent="handleRegister" class="space-y-4">
          
          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-2">
              <Label>First Name</Label>
              <Input v-model="formData.first_name" placeholder="John" required />
            </div>
            <div class="space-y-2">
              <Label>Age</Label>
              <Input v-model="formData.age" type="number" placeholder="20" required />
            </div>
          </div>

          <div class="space-y-2">
             <Label>Date of Birth</Label>
             <Input v-model="formData.dob" type="date" required />
          </div>

          <div class="space-y-2">
            <Label>College Name</Label>
            <Input v-model="formData.college" placeholder="IIT Madras" required />
          </div>

          <div class="space-y-2">
            <Label>Course / Major</Label>
            <Input v-model="formData.course" placeholder="B.Tech Computer Science" required />
          </div>

          <div class="space-y-2">
            <Label>Username</Label>
            <Input v-model="formData.username" placeholder="Pick a username" required />
          </div>

          <div class="space-y-2">
            <Label>Email</Label>
            <Input v-model="formData.email" type="email" placeholder="john@example.com" required />
          </div>

          <div class="space-y-2">
            <Label>Password</Label>
            <Input v-model="formData.password" type="password" placeholder="••••••••" required />
          </div>

          <div v-if="errorMessage" class="text-red-500 text-sm text-center">
            {{ errorMessage }}
          </div>

          <Button type="submit" class="w-full" :disabled="isLoading">
            {{ isLoading ? 'Creating Account...' : 'Sign Up' }}
          </Button>

        </form>
      </CardContent>
      <CardFooter class="justify-center">
        <p class="text-sm text-gray-500">
          Already have an account? 
          <a href="/login" class="text-blue-600 hover:underline">Log in</a>
        </p>
      </CardFooter>
    </Card>
  </div>
</template>