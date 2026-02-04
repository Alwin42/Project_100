<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '@/services/api'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Wallet, TrendingDown, Calendar, PieChart, BarChart3, ArrowUpRight } from 'lucide-vue-next'

const expenses = ref([])
const loading = ref(true)

// --- DATA FETCHING ---
onMounted(async () => {
  try {
    const res = await api.get('expenses/')
    // Sort by date descending (newest first)
    expenses.value = res.data.sort((a, b) => new Date(b.date) - new Date(a.date))
  } catch (e) {
    console.error("Failed to load expenses", e)
  } finally {
    loading.value = false
  }
})

// --- COMPUTED ANALYTICS ---

// 1. Total Lifetime Spend
const totalSpent = computed(() => {
  return expenses.value.reduce((sum, item) => sum + parseFloat(item.amount || 0), 0)
})

// 2. Group Expenses by Month/Year
const monthlyBreakdown = computed(() => {
  const groups = {}
  
  expenses.value.forEach(exp => {
    // Use exp.date first, fallback to created_at
    const d = new Date(exp.date || exp.created_at)
    if (isNaN(d.getTime())) return

    const key = d.toLocaleString('default', { month: 'long', year: 'numeric' })
    
    if (!groups[key]) {
      groups[key] = { total: 0, count: 0, month: d.getMonth(), year: d.getFullYear() }
    }
    groups[key].total += parseFloat(exp.amount || 0)
    groups[key].count += 1
  })

  return Object.entries(groups)
    .map(([name, data]) => ({ name, ...data }))
    .sort((a, b) => b.year - a.year || b.month - a.month)
})

// 3. Yearly Statistics (Current Year)
const yearlyStats = computed(() => {
  const currentYear = new Date().getFullYear()
  const currentMonthIndex = new Date().getMonth() + 1 

  const thisYearExpenses = expenses.value.filter(e => {
    const d = new Date(e.date || e.created_at)
    return d.getFullYear() === currentYear
  })

  const totalThisYear = thisYearExpenses.reduce((sum, e) => sum + parseFloat(e.amount || 0), 0)
  const averagePerMonth = currentMonthIndex > 0 ? (totalThisYear / currentMonthIndex) : 0

  return { year: currentYear, total: totalThisYear, average: averagePerMonth }
})
</script>

<template>
  <div class="min-h-screen  text-white p-6 space-y-8 pb-20">
    
    <div class="flex flex-col md:flex-row justify-between items-end gap-4 border-b border-white/10 pb-6">
      <div>
        <h1 class="text-3xl font-black tracking-tight flex items-center gap-3">
          <div class="p-2 bg-green-500/10 rounded-xl border border-green-500/20">
             <Wallet class="w-6 h-6 text-green-500" />
          </div>
          Expense <span class="text-green-500">Tracker</span>
        </h1>
        <p class="text-gray-400 mt-2 font-medium">Track your spending and manage your budget.</p>
      </div>
      
      <div class="text-right bg-white/5 px-8 py-4 rounded-2xl border border-white/10 hover:bg-white/10 hover:-translate-y-1 transition-all duration-300 cursor-default shadow-lg hover:shadow-green-500/10">
        <p class="text-xs text-gray-400 uppercase tracking-widest font-bold mb-1">Lifetime Total</p>
        <p class="text-4xl font-mono font-bold text-green-400 tracking-tighter">₹{{ totalSpent.toLocaleString() }}</p>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <Card class="bg-black/40 backdrop-blur-xl border border-white/10 text-white shadow-xl hover:border-white/20 transition-all duration-300 group">
        <CardHeader class="pb-2">
          <CardTitle class="flex items-center gap-2 text-lg text-nexus-accent group-hover:text-white transition-colors">
            <PieChart class="w-5 h-5" /> {{ yearlyStats.year }} Overview
          </CardTitle>
        </CardHeader>
        <CardContent class="grid grid-cols-2 gap-4 pt-4">
          <div class="p-4 rounded-xl bg-green-500/5 border border-green-500/10 hover:bg-green-500/10 hover:border-green-500/30 transition-all duration-300">
            <p class="text-xs text-green-400 uppercase font-bold">Spent This Year</p>
            <p class="text-2xl font-bold text-white mt-1">₹{{ yearlyStats.total.toLocaleString() }}</p>
          </div>
          <div class="p-4 rounded-xl bg-blue-500/5 border border-blue-500/10 hover:bg-blue-500/10 hover:border-blue-500/30 transition-all duration-300">
            <p class="text-xs text-blue-400 uppercase font-bold">Avg / Month</p>
            <p class="text-2xl font-bold text-white mt-1">₹{{ yearlyStats.average.toFixed(0) }}</p>
          </div>
        </CardContent>
      </Card>

      <Card class="bg-black/40 backdrop-blur-xl border border-white/10 text-white shadow-xl hover:border-white/20 transition-all duration-300">
        <CardHeader class="pb-2">
          <CardTitle class="flex items-center gap-2 text-lg text-orange-400">
            <BarChart3 class="w-5 h-5" /> Monthly Breakdown
          </CardTitle>
        </CardHeader>
        <CardContent class="h-[140px] overflow-y-auto pr-2 custom-scrollbar space-y-2">
          <div 
            v-for="month in monthlyBreakdown" 
            :key="month.name" 
            class="flex justify-between items-center p-3 rounded-lg bg-white/5 border border-white/5 hover:bg-white/10 hover:translate-x-1 hover:border-white/10 transition-all duration-300 cursor-default group"
          >
            <span class="font-medium text-gray-400 group-hover:text-white transition-colors">{{ month.name }}</span>
            <span class="font-mono font-bold text-white group-hover:text-nexus-accent transition-colors">₹{{ month.total.toLocaleString() }}</span>
          </div>
          <div v-if="monthlyBreakdown.length === 0" class="text-center text-gray-500 text-sm py-4">
            No data available yet.
          </div>
        </CardContent>
      </Card>
    </div>

    <div>
      <h2 class="text-xl font-bold text-white mb-6 flex items-center gap-2">
        <TrendingDown class="w-5 h-5 text-red-400" /> Recent Transactions
      </h2>
      
      <div v-if="loading" class="text-center py-12 text-gray-500 animate-pulse">Loading expenses...</div>
      
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card 
          v-for="exp in expenses" 
          :key="exp.id" 
          class="bg-black/40 border border-white/10 text-white transition-all duration-300 group relative overflow-hidden
                 hover:-translate-y-1 hover:scale-[1.02] hover:bg-white/5 hover:border-green-500/40 hover:shadow-[0_10px_40px_-10px_rgba(34,197,94,0.1)]"
        >
          <div class="absolute inset-0 bg-gradient-to-br from-green-500/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>

          <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2 relative z-10">
            <CardTitle class="text-sm font-bold text-gray-400 truncate group-hover:text-white transition-colors duration-300">
              {{ exp.category }}
            </CardTitle>
            <div class="p-1.5 bg-red-500/10 rounded-md group-hover:bg-red-500/20 transition-colors">
              <TrendingDown class="h-4 w-4 text-red-400 group-hover:scale-110 transition-transform duration-300" />
            </div>
          </CardHeader>
          
          <CardContent class="relative z-10">
            <div class="flex items-end justify-between">
                <div class="text-2xl font-black text-white tracking-tight">₹{{ parseFloat(exp.amount).toFixed(2) }}</div>
                <ArrowUpRight class="w-4 h-4 text-gray-600 opacity-0 group-hover:opacity-100 group-hover:text-green-400 group-hover:translate-x-1 group-hover:-translate-y-1 transition-all duration-300" />
            </div>
            
            <div class="flex items-center gap-2 mt-3 pt-3 border-t border-white/5 group-hover:border-white/10 transition-colors">
              <Calendar class="w-3 h-3 text-gray-600 group-hover:text-green-400 transition-colors" />
              <p class="text-xs text-gray-500 font-mono group-hover:text-gray-300 transition-colors">
                {{ new Date(exp.date || exp.created_at).toLocaleDateString(undefined, { dateStyle: 'medium' }) }}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>

  </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.02);
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.2);
}
</style>