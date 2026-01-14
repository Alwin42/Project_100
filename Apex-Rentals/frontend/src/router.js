import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CarDetails from './views/CarDetails.vue'
import AboutView from './views/AboutView.vue'
import FleetView from './views/FleetView.vue' // <--- 1. Import it

const routes = [
  { path: '/', component: HomeView, name: 'home' },
  { path: '/cars/:id', component: CarDetails, name: 'details' },
  { path: '/about', component: AboutView, name: 'about' },
  { path: '/fleet', component: FleetView, name: 'fleet' } // <--- 2. Add this
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } }
})

export default router