import { createRouter, createWebHistory } from 'vue-router'
// 1. Import the HomeView component you just created
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // 2. Add the route configuration to the empty array
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    }
  ],
})

export default router