<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button';
import { Menu, X } from 'lucide-vue-next'; // Import icons

const auth = useAuthStore();
const router = useRouter();
const isMobileMenuOpen = ref(false);

const toggleMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
};

const closeMenu = () => {
  isMobileMenuOpen.value = false;
};

const handleLogout = () => {
  closeMenu();
  auth.logout();
  router.push('/login');
};
</script>

<template>
  <header class="sticky top-0 z-50 w-full border-b border-gray-800 bg-nexus-card/90 backdrop-blur-md shadow-sm">
    <div class="container mx-auto flex h-16 items-center justify-between px-4">
      
      <router-link to="/" class="flex items-center gap-2 group" @click="closeMenu">
        <div class="h-8 w-8 rounded-lg bg-nexus-accent flex items-center justify-center transition-transform group-hover:scale-105">
          <span class="text-black font-bold text-lg">N</span>
        </div>
        <span class="text-lg font-bold tracking-tight text-white group-hover:text-nexus-accent transition-colors">
          Nexus Learn
        </span>
      </router-link>

      <nav class="hidden md:flex items-center gap-6 text-sm font-medium">
        <router-link to="/home" class="text-gray-300 hover:text-nexus-accent transition-colors">
          Home
        </router-link>
        
        <template v-if="auth.isAuthenticated">
          <router-link to="/dashboard" class="text-gray-300 hover:text-nexus-accent transition-colors">
            Dashboard
          </router-link>
          <router-link to="/dashboard/subjects" class="text-gray-300 hover:text-nexus-accent transition-colors">
            Subjects
          </router-link>
          <router-link to="/dashboard/cloud" class="text-gray-300 hover:text-nexus-accent transition-colors">
            Cloud
          </router-link>
        </template>
      </nav>

      <div class="hidden md:flex items-center gap-4">
        <div v-if="auth.isAuthenticated" class="flex items-center gap-4">
          <span class="text-sm text-white">
            Welcome, {{ auth.user?.username || 'Student' }}
          </span>
          <Button class="text-white hover:bg-red-500/20 hover:text-red-400" variant="ghost" size="sm" @click="handleLogout">
            Logout
          </Button>
        </div>
        <div v-else>
          <router-link to="/login">
            <Button class="bg-nexus-accent text-black hover:bg-nexus-dark font-bold" size="sm">
              Login
            </Button>
          </router-link>
        </div>
      </div>

      <button @click="toggleMenu" class="md:hidden text-gray-300 hover:text-white focus:outline-none">
        <component :is="isMobileMenuOpen ? X : Menu" class="w-6 h-6" />
      </button>

    </div>

    <transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="transform -translate-y-2 opacity-0"
      enter-to-class="transform translate-y-0 opacity-100"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="transform translate-y-0 opacity-100"
      leave-to-class="transform -translate-y-2 opacity-0"
    >
      <div v-if="isMobileMenuOpen" class="md:hidden border-t border-gray-800 bg-black/95 backdrop-blur-xl absolute w-full left-0 top-16 shadow-2xl">
        <nav class="flex flex-col p-4 space-y-4">
          
          <router-link to="/home" class="text-gray-300 hover:text-nexus-accent hover:bg-white/5 p-3 rounded-lg transition-all" @click="closeMenu">
            Home
          </router-link>
          
          <template v-if="auth.isAuthenticated">
            <router-link to="/dashboard" class="text-gray-300 hover:text-nexus-accent hover:bg-white/5 p-3 rounded-lg transition-all" @click="closeMenu">
              Dashboard
            </router-link>
            <router-link to="/dashboard/subjects" class="text-gray-300 hover:text-nexus-accent hover:bg-white/5 p-3 rounded-lg transition-all" @click="closeMenu">
              Subjects
            </router-link>
            <router-link to="/dashboard/cloud" class="text-gray-300 hover:text-nexus-accent hover:bg-white/5 p-3 rounded-lg transition-all" @click="closeMenu">
              Cloud
            </router-link>
            
            <div class="border-t border-gray-800 pt-4 mt-2">
              <div class="flex items-center justify-between px-2 mb-4">
                <span class="text-sm text-gray-400">User: {{ auth.user?.username }}</span>
              </div>
              <Button class="w-full bg-red-500/10 text-red-400 hover:bg-red-500/20" @click="handleLogout">
                Logout
              </Button>
            </div>
          </template>

          <template v-else>
            <router-link to="/login" @click="closeMenu">
              <Button class="w-full bg-nexus-accent text-black font-bold">
                Login
              </Button>
            </router-link>
          </template>

        </nav>
      </div>
    </transition>
  </header>
</template>

<style scoped>
.router-link-active {
  color: #1DCD9F;
  font-weight: 600;
}
</style>