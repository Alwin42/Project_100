import { createRouter, createWebHistory } from 'vue-router'
import authpage from '../pages/authpage.vue'
import LandingPage from '../pages/landing-page.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LandingPage, 
    },
    {
      path: '/auth',
      name: 'auth',
      component: authpage,
    },
  ],
})

export default router