import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
// We will create these placeholder views next
import SubjectsView from '../views/SubjectsView.vue' 
// import CloudView from '../views/CloudView.vue' // Uncomment when created

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: SubjectsView
    },
    // {
    //   path: '/cloud',
    //   name: 'cloud',
    //   component: CloudView
    // }
  ]
})

export default router