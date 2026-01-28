<template>
  <header class="sticky top-0 z-40 w-full border-b bg-white shadow-sm">
    <div class="container mx-auto flex h-16 items-center justify-between px-4">
      
      <div class="flex items-center gap-2">
        <div class="h-8 w-8 rounded-lg bg-slate-900 flex items-center justify-center">
          <span class="text-white font-bold text-lg">N</span>
        </div>
        <span class="text-lg font-bold tracking-tight text-slate-900">Nexus Learn</span>
      </div>

      <nav class="hidden md:flex items-center gap-6 text-sm font-medium">
        <router-link to="/" class="text-slate-600 hover:text-slate-900 transition-colors">
          Home
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/dashboard" class="text-slate-600 hover:text-slate-900 transition-colors">
          Dashboard
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/subjects" class="text-slate-600 hover:text-slate-900 transition-colors">
          Subjects
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/cloud" class="text-slate-600 hover:text-slate-900 transition-colors">
          Cloud
        </router-link>
      </nav>

      <div class="flex items-center gap-4">
        <div v-if="auth.isAuthenticated" class="flex items-center gap-4">
          <span class="text-sm text-slate-500 hidden sm:inline-block">Welcome, Student</span>
          <Button variant="destructive" size="sm" @click="handleLogout">
            Logout
          </Button>
        </div>

        <div v-else>
          <router-link to="/login">
            <Button variant="default" size="sm">Login</Button>
          </router-link>
        </div>
      </div>

    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button'; // Using Shadcn Button

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/login');
};
</script>

<style scoped>
/* Router Link Active State - making the active link darker */
.router-link-active {
  color: #0f172a; /* Slate-900 */
  font-weight: 600;
}
</style>