import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CarDetails from './views/CarDetails.vue'
import AboutView from './views/AboutView.vue' 

const routes = [
  { path: '/', component: HomeView, name: 'home' },
  { path: '/cars/:id', component: CarDetails, name: 'details' },
  { path: '/about', component: AboutView, name: 'about' } 
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router