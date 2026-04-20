import { createRouter, createWebHistory } from 'vue-router'

// 1. Import both of your views
import LandingPage from '../views/Landing-page.vue'
import HomeView from '../views/Home.vue' // This is the new dashboard we just built

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  
  // 2. Define each route as a separate object in the array
  routes: [
    {
      // This is the first page users see
      path: '/',
      name: 'landing',
      component: LandingPage,
    },
    {
      
      path: '/home', 
      name: 'home',
      component: HomeView,
    }
  ],
})

export default router