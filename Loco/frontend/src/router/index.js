import { createRouter, createWebHistory } from 'vue-router'
import AuthPage from '../pages/authpage.vue'
import HomePage from '../pages/HomePage.vue'
import UserDashboard from '../pages/UserDashboard.vue'
import ProfilePage from '../pages/ProfilePage.vue'
import ServicesPage from '../pages/ServicesPage.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'landing', component: HomePage },
    { path: '/auth', name: 'auth', component: AuthPage },
    { 
      path: '/dashboard', 
      name: 'dashboard', 
      component: UserDashboard 
    },
    { path: '/profile', name: 'profile', component: ProfilePage },
    { path: '/services', name: 'services', component: ServicesPage },
  ],
})

export default router