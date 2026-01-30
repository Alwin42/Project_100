<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Wallet, TrendingDown } from 'lucide-vue-next'

const expenses = ref([])
const loading = ref(true)

// Calculate Total Spent
const totalSpent = computed(() => {
  return expenses.value.reduce((sum, item) => sum + parseFloat(item.amount || 0), 0)
})

onMounted(async () => {
  try {
    const res = await api.get('expenses/')
    expenses.value = res.data
  } catch (e) { console.error(e) } finally { loading.value = false }
})
</script>

<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-3xl font-bold text-white">Expenses</h1>
      <div class="text-right">
        <p class="text-gray-400 text-sm">Total Spent</p>
        <p class="text-2xl font-mono text-nexus-accent">₹{{ totalSpent.toFixed(2) }}</p>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      <Card v-for="exp in expenses" :key="exp.id" class="bg-black/40 border-white/10 text-white hover:bg-white/5 transition-all">
        <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle class="text-sm font-medium text-gray-300">
            {{ exp.category }}
          </CardTitle>
          <TrendingDown class="h-5 w-5 text-red-400" />
        </CardHeader>
        <CardContent>
          <div class="text-2xl font-bold">₹{{ parseFloat(exp.amount).toFixed(2) }}</div>
          <p class="text-xs text-gray-500 mt-1">
            {{ new Date(exp.created_at).toLocaleDateString() }}
          </p>
        </CardContent>
      </Card>
    </div>
  </div>
</template>