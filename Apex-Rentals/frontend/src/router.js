import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './views/HomeView.vue'
import CarDetails from './views/CarDetails.vue'
import AboutView from './views/AboutView.vue'
import FleetView from './views/FleetView.vue' 
import LoginView from './views/LoginView.vue'       
import DashboardView from './views/DashboardView.vue'
import PaymentView from './views/PaymentView.vue'

const routes = [
  { path: '/', component: HomeView, name: 'home' },
  { path: '/cars/:id', component: CarDetails, name: 'details' },
  { path: '/about', component: AboutView, name: 'about' },
  { path: '/fleet', component: FleetView, name: 'fleet' },
  { path: '/login', component: LoginView, name: 'login' },       
  { path: '/dashboard', name: 'dashboard', component: DashboardView },
  { path: '/payment/:id', name: 'payment', component: PaymentView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() { return { top: 0 } }
})

export default router