import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CarDetails from './views/CarDetails.vue' 

const routes = [
  { path: '/', component: HomeView, name: 'home' },
  { path: '/cars/:id', component: CarDetails, name: 'details' }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router