import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import SubjectsView from '../views/SubjectsView.vue' 
import LandingView from '../views/LandingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',  
      name: 'register',
      component: RegisterView
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: SubjectsView
    },
    {
      path: '/dashboard', // Moved HomeView here
      name: 'dashboard',
      component: HomeView,
      // Optional: Add a meta field to check auth later
      meta: { requiresAuth: true }
    },
  ]
})

export default router