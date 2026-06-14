import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../views/Landing-page.vue'
import HomeView from '../views/Home.vue' 
import VendorLogin from '../views/Vendor-login.vue'
import VendorReg from '../views/Vendor-reg.vue'
import Dashboard from '../views/Dashboard.vue'
import Inventory from '../views/Inventory.vue'
import Stores from '../views/Stores.vue'
import CustomerDashboard from '../views/CustomerDashboard.vue'
import VendorOrders from '../views/VendorOrders.vue'
import VendorPayments from '../views/VendorPayments.vue'
import CustomerHistory from '../views/CustomerHistory.vue'
import VendorHelp from '../views/Vendor-help.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'landing', component: LandingPage, },
    { path: '/home', name: 'home', component: HomeView, },
    { path: '/vendor-login', name: 'vendorLogin', component: VendorLogin, },
    { path: '/vendor-register', name: 'vendorRegister', component: VendorReg, },
    { path: '/dashboard', name: 'dashboard', component: Dashboard, },
    { path: '/inventory', name: 'inventory', component: Inventory,},
    { path: '/stores', name: 'stores', component: Stores },
    { path: '/customer-dashboard', name: 'customerDashboard', component: CustomerDashboard },
    { path: '/vendor-orders', name: 'vendorOrders', component: VendorOrders },
    { path: '/vendor-payments', name: 'vendorPayments', component: VendorPayments },
    { path: '/history', name: 'customerHistory', component: CustomerHistory },
    { path: '/vendor-help', name: 'VendorHelp', component: VendorHelp },
  ],
})

export default router
