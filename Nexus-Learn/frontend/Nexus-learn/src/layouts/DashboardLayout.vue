<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterView, RouterLink, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { 
  LayoutDashboard, 
  CalendarDays, 
  StickyNote, 
  Wallet, 
  UserCircle, 
  LogOut,
  Activity,
  Menu,    // <--- The Hamburger Icon is back
  X,       // Close Icon
  PanelLeftClose 
} from 'lucide-vue-next'

const route = useRoute()
const auth = useAuthStore()

// --- STATE ---
// Default to FALSE (Closed) to be safe for mobile. 
// We open it automatically on Desktop in onMounted.
const isSidebarOpen = ref(false)

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

// Auto-close on mobile when clicking a link
const handleLinkClick = () => {
  if (window.innerWidth < 768) {
    isSidebarOpen.value = false
  }
}

// Check screen size on load
onMounted(() => {
  if (window.innerWidth >= 768) {
    isSidebarOpen.value = true // Open by default on Desktop
  }
})

const links = [
  { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard },
  { name: 'Activities', path: '/dashboard/activities', icon: Activity },
  { name: 'My Notes', path: '/dashboard/notes', icon: StickyNote },
  { name: 'Expenses', path: '/dashboard/expenses', icon: Wallet },
  { name: 'Timetable', path: '/dashboard/timetable', icon: CalendarDays },
  { name: 'Edit Profile', path: '/dashboard/profile', icon: UserCircle },
]
</script>

<template>
  <div class="flex min-h-screen bg-nexus-main text-white font-sans relative overflow-x-hidden">
    
    <div 
      v-if="isSidebarOpen" 
      @click="isSidebarOpen = false"
      class="fixed inset-0 bg-black/80 z-40 md:hidden backdrop-blur-sm"
    ></div>

    <aside 
      class="fixed inset-y-0 left-0 z-40 w-44 bg-black backdrop-blur-xl border-r border-white/10 flex flex-col p-4 transition-transform duration-400 ease-in-out"
      :class="isSidebarOpen ? 'translate-x-0' : '-translate-x-full'"
    >
      <div class="mb-8 flex items-center justify-between px-2">
        <div class="flex items-center gap-2">
          
          <span class="text-xl font-bold tracking-wider text-white">Menu </span>
        </div>
        
        <button @click="toggleSidebar" class="text-gray-400 hover:text-white">
          <PanelLeftClose class="w-6 h-6" />
        </button>
      </div>

      <nav class="space-y-2 flex-1">
        <RouterLink 
          v-for="link in links" 
          :key="link.path" 
          :to="link.path"
          @click="handleLinkClick"
        >
          <Button 
            variant="ghost" 
            class="w-full justify-start gap-3 text-gray-400 hover:text-white hover:bg-white/10 mb-1"
            :class="{ 'bg-nexus-accent/10 text-nexus-accent hover:text-nexus-accent hover:bg-nexus-accent/20': route.path === link.path }"
          >
            <component :is="link.icon" class="w-5 h-5" />
            {{ link.name }}
          </Button>
        </RouterLink>
      </nav>

      <div class="mt-auto pt-4 border-t border-white/10">
        <Button variant="ghost" class="w-full justify-start gap-3 text-red-400 hover:text-red-300 hover:bg-red-900/20" @click="auth.logout">
          <LogOut class="w-5 h-5" />
          Logout
        </Button>
      </div>
    </aside>

    <main 
      class="flex-1 transition-all duration-300 ease-in-out p-4 md:p-8 overflow-y-auto"
      :class="isSidebarOpen ? 'md:ml-64' : 'ml-0'"
    >
      
      <div class="mb-6 flex items-center gap-4">
        
        <Button 
          v-if="!isSidebarOpen" 
          variant="ghost" 
          size="icon" 
          @click="toggleSidebar" 
          class="text-white hover:bg-white/10"
        >
          <Menu class="w-6 h-6" />
        </Button>
        
        <span v-if="!isSidebarOpen" class="font-bold text-lg text-gray-400">Menu</span>
      </div>

      <RouterView />
    </main>

  </div>
</template>