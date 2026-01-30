<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'

const router = useRouter()
const form = ref({ category: '', amount: '' })
const submit = async () => { await api.post('expenses/', form.value); router.push('/dashboard') }
</script>

<template>
  <div class="min-h-screen bg-nexus-main flex items-center justify-center p-4">
    <Card class="w-full max-w-md bg-black/60 backdrop-blur-xl border-white/10 text-white">
      <CardHeader><CardTitle class="text-nexus-accent">Add Expense</CardTitle></CardHeader>
      <CardContent>
        <form @submit.prevent="submit" class="space-y-4">
          <div class="space-y-2"><Label>Category</Label><Input v-model="form.category" class="bg-white/5 border-white/10 text-white" /></div>
          <div class="space-y-2"><Label>Amount</Label><Input type="number" v-model="form.amount" class="bg-white/5 border-white/10 text-white" /></div>
          <Button type="submit" class="w-full bg-nexus-accent text-black font-bold">Save Expense</Button>
        </form>
      </CardContent>
    </Card>
  </div>
</template>