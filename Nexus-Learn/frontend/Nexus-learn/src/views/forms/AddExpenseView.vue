<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { ExclamationTriangleIcon } from '@radix-icons/vue'

const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')

// FIX 1: Initialize 'date' so it is reactive
const form = ref({ 
  category: '', 
  amount: '',
  date: new Date().toISOString().split('T')[0] // Default to today
})

const submit = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    await api.post('expenses/', form.value)
    router.push('/dashboard')
  } catch (error) {
    console.error(error)
    if (error.response && error.response.status === 401) {
      errorMessage.value = "Session expired. Please Log Out and Log In again."
    } else if (error.response && error.response.data) {
      const serverErrors = Object.values(error.response.data).flat().join(', ')
      errorMessage.value = serverErrors || "Server rejected the data."
    } else {
      errorMessage.value = "Failed to save expense."
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-md bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader>
        <CardTitle class="text-nexus-accent">Add Expense</CardTitle>
      </CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-900/50 border-red-900 text-white">
            <ExclamationTriangleIcon class="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{{ errorMessage }}</AlertDescription>
          </Alert>

          <div class="space-y-2">
            <Label>Category</Label>
            <Input v-model="form.category" placeholder="e.g. Food, Transport" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Amount (₹)</Label>
            <Input type="number" step="0.01" v-model="form.amount" placeholder="0.00" class="bg-white/5 border-white/10 text-white" required />
          </div>

          <div class="space-y-2">
            <Label>Date</Label>
            <Input type="date" v-model="form.date" class="bg-white/5 border-white/10 text-white [color-scheme:dark]" required />
          </div>

          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold" :disabled="isLoading">
            {{ isLoading ? 'Saving...' : 'Save Expense' }}
          </Button>

        </form>
      </CardContent>
    </Card>
  </div>
</template>