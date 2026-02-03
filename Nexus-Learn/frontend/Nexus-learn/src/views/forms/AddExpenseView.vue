<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { TriangleAlert, Wallet, DollarSign, Calendar } from 'lucide-vue-next'
import BackgroundShapes from '@/components/BackgroundShapes.vue'
const router = useRouter()
const isLoading = ref(false)
const errorMessage = ref('')
const form = ref({ category: '', amount: '', date: new Date().toISOString().split('T')[0] })

const submit = async () => {
  isLoading.value = true; errorMessage.value = ''
  try { await api.post('expenses/', form.value); router.push('/dashboard') } 
  catch (error) { errorMessage.value = "Failed to save expense." } finally { isLoading.value = false }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center  px-4 py-12 pt-24 text-white relative overflow-hidden">
    <BackgroundShapes />
    <Card class="w-full max-w-lg bg-black/60 backdrop-blur-3xl border-white/10 text-white shadow-2xl relative z-10 rounded-[2.5rem] animate-in fade-in zoom-in duration-500">
      <CardHeader class="text-center pb-2">
        <div class="flex justify-center mb-4"><div class="h-12 w-12 rounded-xl bg-green-500 flex items-center justify-center shadow-lg shadow-green-500/20"><Wallet class="h-6 w-6 text-black" /></div></div>
        <CardTitle class="text-3xl font-black tracking-tight">Add <span class="text-green-500">Expense</span></CardTitle>
      </CardHeader>
      <CardContent class="p-8 pt-4">
        <form @submit.prevent="submit" class="space-y-5">
          <Alert v-if="errorMessage" variant="destructive" class="bg-red-500/10 border-red-500/20 text-red-200 rounded-xl"><TriangleAlert class="h-4 w-4" /><AlertTitle>Error</AlertTitle><AlertDescription>{{ errorMessage }}</AlertDescription></Alert>

          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Category</Label><div class="relative group"><Wallet class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-green-500 transition-colors" /><Input v-model="form.category" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-green-500 rounded-2xl" placeholder="e.g. Food" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Amount</Label><div class="relative group"><DollarSign class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-green-500 transition-colors" /><Input type="number" step="0.01" v-model="form.amount" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-green-500 rounded-2xl" placeholder="0.00" required /></div></div>
          <div class="space-y-2"><Label class="text-xs uppercase font-bold text-gray-500 ml-1">Date</Label><div class="relative group"><Calendar class="absolute left-4 top-3.5 h-5 w-5 text-gray-500 group-focus-within:text-green-500 transition-colors" /><Input type="date" v-model="form.date" class="pl-12 h-12 bg-white/5 border-white/10 text-white focus:border-green-500 rounded-2xl [color-scheme:dark]" required /></div></div>

          <Button type="submit" class="w-full h-12 text-lg bg-green-500 hover:bg-green-400 text-black font-bold shadow-lg shadow-green-500/20 rounded-2xl mt-4" :disabled="isLoading">{{ isLoading ? 'Saving...' : 'Save Expense' }}</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>