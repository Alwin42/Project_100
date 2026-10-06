import { createRouter, createWebHistory } from 'vue-router'
// Import the new landing page
import LandingPage from '../pages/landing-page.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      // Use the new LandingPage component
      component: LandingPage, 
    },
    // Keep your other routes here if you have them...
  ],
})

export default router