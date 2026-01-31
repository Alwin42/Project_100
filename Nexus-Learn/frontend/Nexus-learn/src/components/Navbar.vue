<template>
  <header class="sticky top-0 z-40 w-full border-b border-gray-800 bg-nexus-card shadow-sm">
    <div class="container mx-auto flex h-16 items-center justify-between px-4">
      
      <div class="flex items-center gap-2">
        <div class="h-8 w-8 rounded-lg bg-nexus-accent flex items-center justify-center">
          <span class="text-black font-bold text-lg">N</span>
        </div>
        <span class="text-lg font-bold tracking-tight text-white">Nexus Learn</span>
      </div>

      <nav class="hidden md:flex items-center gap-6 text-sm font-medium">
        <router-link to="/" class="text-gray-300 hover:text-nexus-accent transition-colors">
          Home
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/dashboard" class="text-gray-300 hover:text-nexus-accent transition-colors">
          Dashboard
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/dashboard/subjects" class="text-gray-300 hover:text-nexus-accent transition-colors">
          Subjects
        </router-link>
        
        <router-link v-if="auth.isAuthenticated" to="/cloud" class="text-gray-300 hover:text-nexus-accent transition-colors">
          Cloud
        </router-link>
      </nav>

      <div class="flex items-center gap-4">
        <div v-if="auth.isAuthenticated" class="flex items-center gap-4">
          <span class="text-sm text-white hidden sm:inline-block">
            Welcome, {{ auth.user?.username || 'Student' }}
          </span>
          <Button class="text-white"variant="destructive" size="sm" @click="handleLogout">
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

    </div>
  </header>
</template>

<script setup>
import { useAuthStore } from '../stores/auth';
import { useRouter } from 'vue-router';
import { Button } from '@/components/ui/button';

const auth = useAuthStore();
const router = useRouter();

const handleLogout = () => {
  auth.logout();
  router.push('/login');
};
</script>

<style scoped>
/* Router Link Active State 
   This automatically applies to the link of the page you are currently on.
   We set it to the Accent Color (#1DCD9F) so it glows.
*/
.router-link-active {
  color: #1DCD9F; /* nexus-accent */
  font-weight: 600;
}
</style>