<template>
  <header class="w-full bg-white/80 backdrop-blur-md border-b border-gray-100 py-3 px-6 fixed top-0 flex justify-center z-50 transition-all duration-300">
    
    <div class="max-w-6xl w-full flex justify-between items-center">
      
      <div class="flex items-center gap-2.5 cursor-pointer group">
        <div class="p-1.5 bg-green-50 rounded-xl group-hover:bg-green-100 transition-colors duration-300">
          <ShoppingBasketIcon class="w-5 h-5 text-green-600" />
        </div>
        <h1 class="text-xl font-bold text-gray-900 tracking-tight">StockUndo</h1>
      </div>

      <button class="text-sm font-semibold text-gray-600 hover:text-green-700 bg-gray-50/50 hover:bg-green-50 border border-transparent hover:border-green-100 px-5 py-2 rounded-full transition-all duration-300">
        Vendor Portal
      </button>
      
    </div>
  </header>
</template>

<script setup>
import { ShoppingBasketIcon } from 'lucide-vue-next'
</script>