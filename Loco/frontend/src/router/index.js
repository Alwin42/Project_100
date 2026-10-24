import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../pages/landing-page.vue'
import AuthPage from '../pages/authpage.vue'
import HomePage from '../pages/HomePage.vue'
import UserDashboard from '../pages/UserDashboard.vue' // 👈 Import Dashboard

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'landing', component: LandingPage },
    { path: '/auth', name: 'auth', component: AuthPage },
    { path: '/home', name: 'home', component: HomePage },
    { 
      path: '/dashboard', 
      name: 'dashboard', 
      component: UserDashboard 
    },
  ],
})

export default router