<template>
  <div class="fixed inset-0 pointer-events-none z-0 overflow-hidden">
    
    <div class="absolute top-[-50px] left-[-50px] w-64 h-64 rounded-full border-4 border-nexus-accent/40 opacity-60 animate-float"></div>

    <div class="absolute top-20 right-[10%] w-32 h-32 bg-blue-400/20 border border-blue-400/40 rounded-xl animate-float-delayed" style="animation-duration: 8s;"></div>

    <div class="absolute top-[40%] left-[5%] animate-pulse-slow">
      <div class="w-0 h-0 border-l-[40px] border-l-transparent border-b-[70px] border-b-purple-400/40 border-r-[40px] border-r-transparent"></div>
    </div>

    <div class="absolute bottom-40 right-10 w-48 h-48 border-[6px] border-pink-400/30 rounded-full animate-float"></div>

    <div class="absolute bottom-[10%] left-[15%] w-20 h-20 bg-cyan-400/30 rounded-md rotate-45 animate-float-delayed"></div>

    <div class="absolute top-[15%] left-[45%] text-white/10 text-9xl font-black rotate-12 animate-float">
      +
    </div>

    <div class="absolute top-[60%] right-[20%] w-80 h-80 border-2 border-dashed border-yellow-300/30 rounded-full animate-spin-slow"></div>

    <div class="absolute bottom-10 left-[50%] w-16 h-16 border-2 border-emerald-400/50 rotate-45 animate-float-delayed"></div>

  </div>
</template>

<style scoped>
@keyframes float {
  0% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes float-delayed {
  0% { transform: translateY(0px) rotate(45deg); }
  50% { transform: translateY(-15px) rotate(55deg); }
  100% { transform: translateY(0px) rotate(45deg); }
}

@keyframes pulse-slow {
  0%, 100% { opacity: 0.4; transform: scale(1); }
  50% { opacity: 0.7; transform: scale(1.05); }
}

@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-float { animation: float 6s ease-in-out infinite; }
.animate-float-delayed { animation: float-delayed 8s ease-in-out infinite; }
.animate-pulse-slow { animation: pulse-slow 5s ease-in-out infinite; }
.animate-spin-slow { animation: spin-slow 20s linear infinite; }
</style>