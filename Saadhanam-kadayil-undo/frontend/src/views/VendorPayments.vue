<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="mb-6 animate-in fade-in slide-in-from-bottom-4 duration-700 ease-out">
        <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Payments & Settlements</h1>
        <p class="text-gray-500 mt-1 font-medium">Manage your earnings, payouts, and bank details.</p>
      </div>

      <nav class="flex items-center gap-6 mb-10 border-b border-gray-200">
        <button 
          @click="router.push('/dashboard')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors"
        >
          Overview
        </button>
        <button 
          @click="router.push('/vendor-orders')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors flex items-center gap-1.5"
        >
          <FileTextIcon class="w-4 h-4" />
          Order Logs
        </button>
        <button class="pb-3 border-b-2 border-primary text-primary font-bold text-sm tracking-wide flex items-center gap-1.5">
          <CreditCardIcon class="w-4 h-4" />
          Payments
        </button>
      </nav>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        
        <div class="md:col-span-2 bg-gray-900 rounded-4xl p-8 text-white shadow-xl relative overflow-hidden group">
          <div class="absolute right-0 top-0 w-64 h-64 bg-primary/20 rounded-full blur-3xl -mr-10 -mt-10 pointer-events-none group-hover:bg-primary/30 transition-colors duration-700"></div>
          
          <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <p class="text-gray-400 font-medium mb-2 flex items-center gap-2">
                <WalletIcon class="w-5 h-5 text-accent-1" /> Available to Withdraw
              </p>
              <h2 class="text-5xl font-extrabold tracking-tight mb-2">₹1,240<span class="text-2xl text-gray-500">.00</span></h2>
              <p class="text-sm text-gray-400 font-medium">Next auto-settlement: <span class="text-white">Friday, May 15</span></p>
            </div>
            <button class="bg-primary text-white font-bold px-8 py-4 rounded-2xl hover:bg-primary/90 hover:shadow-lg hover:-translate-y-1 transition-all duration-300 active:scale-95 shrink-0 w-full md:w-auto text-center">
              Withdraw Funds
            </button>
          </div>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm flex flex-col justify-between hover:shadow-md transition-shadow">
          <div class="p-3 bg-secondary/20 rounded-2xl w-fit mb-4">
            <TrendingUpIcon class="w-6 h-6 text-primary" />
          </div>
          <div>
            <p class="text-gray-500 font-medium mb-1">Total Lifetime Earnings</p>
            <h3 class="text-3xl font-bold text-gray-900">₹14,850</h3>
            <p class="text-xs font-bold text-primary mt-2 flex items-center gap-1 bg-secondary/10 w-fit px-2 py-1 rounded-md">
              <ArrowUpRightIcon class="w-3 h-3" /> +12% this month
            </p>
          </div>
        </div>

      </div>

      <div class="bg-white rounded-4xl border border-gray-100 shadow-sm overflow-hidden p-6 md:p-8">
        <h2 class="text-xl font-bold text-gray-900 mb-6">Recent Settlements</h2>
        
        <div class="space-y-4">
          <div 
            v-for="transaction in transactions" 
            :key="transaction.id"
            class="flex items-center justify-between p-4 bg-gray-50 rounded-2xl hover:bg-white hover:border-gray-200 border border-transparent transition-colors group"
          >
            <div class="flex items-center gap-4">
              <div class="w-12 h-12 rounded-xl flex items-center justify-center shrink-0" :class="transaction.type === 'Payout' ? 'bg-primary/10 text-primary' : 'bg-white shadow-sm text-gray-900'">
                <DownloadIcon v-if="transaction.type === 'Payout'" class="w-5 h-5" />
                <ShoppingBagIcon v-else class="w-5 h-5" />
              </div>
              <div>
                <h4 class="font-bold text-gray-900">{{ transaction.title }}</h4>
                <p class="text-xs font-medium text-gray-500">{{ transaction.date }} • {{ transaction.id }}</p>
              </div>
            </div>
            
            <div class="text-right">
              <p class="font-bold text-lg" :class="transaction.type === 'Payout' ? 'text-gray-900' : 'text-primary'">
                {{ transaction.type === 'Payout' ? '-' : '+' }}₹{{ transaction.amount }}
              </p>
              <span class="text-xs font-bold text-gray-400">{{ transaction.status }}</span>
            </div>
          </div>
        </div>
        
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import { FileTextIcon, CreditCardIcon, WalletIcon, TrendingUpIcon, ArrowUpRightIcon, DownloadIcon, ShoppingBagIcon } from 'lucide-vue-next'

const router = useRouter()

// Dummy Data
const transactions = ref([
  { id: 'TXN-004', title: 'Daily Order Revenue', type: 'Income', amount: '240', date: 'Today, 4:00 PM', status: 'Completed' },
  { id: 'TXN-003', title: 'Daily Order Revenue', type: 'Income', amount: '1,000', date: 'Yesterday, 8:00 PM', status: 'Completed' },
  { id: 'TXN-002', title: 'Bank Transfer (HDFC ending in 1234)', type: 'Payout', amount: '3,500', date: 'May 08, 9:00 AM', status: 'Settled' },
  { id: 'TXN-001', title: 'Daily Order Revenue', type: 'Income', amount: '3,500', date: 'May 07, 8:00 PM', status: 'Completed' },
])
</script>