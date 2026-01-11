<template>
  <div class="min-h-screen w-full bg-black font-sans text-white overflow-x-hidden">
    
    <nav class="bg-[#061E29] text-[#F3F4F4] shadow-md sticky top-0 z-50 w-full">
      <div class="w-full px-4 sm:px-6 lg:px-12">
        <div class="flex justify-between items-center h-20">
          
          <router-link to="/" class="flex items-center gap-2 group">
              <span class="text-2xl font-bold tracking-tight">
              Apex<span class="text-[#5F9598]">Rentals</span>
            </span>
          </router-link>
          
          <div class="hidden md:flex space-x-8 items-center text-sm font-medium tracking-wide">
            <router-link to="/" class="hover:text-[#5F9598] transition duration-300">HOME</router-link>
            <a href="#" class="hover:text-[#5F9598] transition duration-300">FLEET</a>
            <a href="#" class="hover:text-[#5F9598] transition duration-300">ABOUT</a>
            
            <a href="#" class="bg-[#1D546D] rounded-xl hover:bg-white hover:text-[#061E29] px-6 py-2.5 rounded-none transition duration-300 font-bold border border-transparent hover:border-white">
              LOGIN
            </a>
          </div>

          <div class="md:hidden text-white">
            <button class="focus:outline-none">
              <svg class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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