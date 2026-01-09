<template>
  <div class="min-h-screen bg-white font-sans text-gray-900">
    
    <nav class="bg-gray-900 text-white shadow-lg sticky top-0 z-50 w-full">
      
      <div class="max-w-full mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          
          <router-link to="/" class="flex-shrink-0 flex items-center">
            <span class="text-xl sm:text-2xl font-bold tracking-tight">
              Apex<span class="text-blue-500">Rentals</span>
            </span>
          </router-link>
          
          <div class="hidden md:flex space-x-8 items-center text-sm font-medium">
            <router-link to="/" class="hover:text-blue-400 transition">Home</router-link>
            <a href="#" class="hover:text-blue-400 transition">Fleet</a>
            <a href="#" class="hover:text-blue-400 transition">About</a>
            <a href="#" class="bg-blue-600 hover:bg-blue-700 px-5 py-2 rounded-full transition">Login</a>
          </div>

          <div class="md:hidden">
            <button class="text-gray-300 hover:text-white focus:outline-none">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>

    <router-view></router-view> 
  </div>
</template>