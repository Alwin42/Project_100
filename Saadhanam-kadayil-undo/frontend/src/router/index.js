import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/Landing-page.vue'
import HomeView from '../views/Home.vue' 
import VendorLogin from '../views/Vendor-login.vue'
import VendorReg from '../views/Vendor-reg.vue'
import Dashboard from '../views/Dashboard.vue'
import Inventory from '../views/Inventory.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingPage,
    },
    {
      path: '/home', 
      name: 'home',
      component: HomeView,
    },
    {
      path: '/vendor-login', 
      name: 'vendorLogin',
      component: VendorLogin,
    },
    {
      path: '/vendor-register', 
      name: 'vendorRegister',
      component: VendorReg,
    },
    {
      path: '/dashboard', 
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory,
    }
  ],
})

export default router
