import { createRouter, createWebHistory } from 'vue-router'
import authpage from '../pages/authpage.vue'
import LandingPage from '../pages/landing-page.vue'
import HomePage from '../pages/HomePage.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage, 
    },
    {
      path: '/auth',
      name: 'auth',
      component: authpage,
    },
    {
      path: '/home', 
      name: 'home',
      component: HomePage,
      
    },
  ],
})

export default router