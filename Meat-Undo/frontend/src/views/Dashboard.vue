<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4 animate-in fade-in slide-in-from-bottom-4 duration-700 ease-out">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Welcome back, {{ vendorName }}!</h1>
          <p class="text-gray-500 mt-1 font-medium">Here is what is happening at your shop today.</p>
        </div>
        <button 
          @click="openAddModal"
          class="bg-primary text-white font-bold px-6 py-3 rounded-full hover:bg-primary/90 hover:shadow-lg hover:shadow-primary/30 hover:-translate-y-0.5 active:scale-95 transition-all duration-300 flex items-center gap-2 group"
        >
          <PlusIcon class="w-5 h-5 transition-transform duration-300 group-hover:rotate-90" />
          Add New Item
        </button>
      </div>

      <nav class="flex items-center gap-6 mb-10 border-b border-gray-200">
        <button class="pb-3 border-b-2 border-primary text-primary font-bold text-sm tracking-wide">
          Overview
        </button>
        <button 
          @click="router.push('/vendor-orders')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors flex items-center gap-1.5"
        >
          <FileTextIcon class="w-4 h-4" />
          Order Logs
        </button>
        <button 
          @click="router.push('/vendor-payments')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors flex items-center gap-1.5"
        >
          <CreditCardIcon class="w-4 h-4" />
          Payments
        </button>
        <button 
          @click="router.push('/vendor-help')" 
          class="pb-3 border-b-2 border-transparent text-gray-500 hover:text-gray-900 font-bold text-sm tracking-wide transition-colors flex items-center gap-1.5"
        >
          <LifeBuoyIcon class="w-4 h-4" />
          Help Center
        </button>
      </nav>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        
        <div class="bg-primary rounded-4xl p-6 text-white shadow-lg shadow-primary/20 relative overflow-hidden group hover:-translate-y-1.5 transition-all duration-300 cursor-default">
          <div class="absolute top-0 right-0 -mr-6 -mt-6 w-32 h-32 bg-white/10 rounded-full blur-2xl pointer-events-none group-hover:scale-150 transition-transform duration-700"></div>
          <div class="flex justify-between items-start mb-4 relative z-10">
            <div class="p-2.5 bg-white/20 rounded-2xl group-hover:scale-110 transition-transform duration-300">
              <ShoppingBagIcon class="w-6 h-6 text-white" />
            </div>
            <span class="bg-accent-1 text-primary text-xs font-bold px-3 py-1 rounded-full shadow-sm">Pending</span>
          </div>
          <h3 class="text-white/90 font-medium mb-1 relative z-10">Total Orders</h3>
          <p class="text-4xl font-bold relative z-10">{{ stats.orders }}</p>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:shadow-gray-200/50 hover:border-gray-200 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group cursor-default">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-secondary/20 rounded-2xl group-hover:bg-secondary/30 transition-colors duration-300">
              <TrendingUpIcon class="w-6 h-6 text-primary" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Expected Revenue</h3>
            <p class="text-3xl font-bold text-gray-900 group-hover:text-primary transition-colors duration-300">₹{{ stats.revenue }}</p>
          </div>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:shadow-yellow-200/50 hover:border-yellow-200 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group cursor-default">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-red-50 rounded-2xl group-hover:bg-yellow-100 transition-colors duration-300">
              <ReceiptIcon class="w-6 h-6 text-yellow-500" />
            </div>
             <span class="text-gray-400 text-xs font-bold px-2 py-1 bg-gray-50 rounded-full border border-gray-100">3%</span>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1 flex items-center gap-1.5">Platform Fee</h3>
            <p class="text-3xl font-bold text-yellow-600">₹{{ calculatedFee }}</p>
          </div>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:shadow-gray-200/50 hover:border-gray-200 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group cursor-default">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-accent-1/40 rounded-2xl group-hover:bg-accent-1/60 transition-colors duration-300">
              <PackageIcon class="w-6 h-6 text-accent-2" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Active Items</h3>
            <p class="text-3xl font-bold text-gray-900">{{ stats.activeItems }}</p>
          </div>
        </div>

      </div>

      <div class="bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8 mb-8 hover:shadow-md transition-shadow duration-300">
        <div class="flex items-center justify-between mb-6">
          <h2 class="text-xl font-bold text-gray-900 flex items-center gap-2">
            <StoreIcon class="w-5 h-5 text-primary" /> Shop Operations
          </h2>
          <button @click="saveShopSettings" class="text-sm font-bold bg-gray-50 hover:bg-gray-100 text-gray-700 px-4 py-2 rounded-xl transition-colors active:scale-95">
            Save Changes
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          
          <div class="flex flex-col justify-center items-start bg-gray-50 p-5 rounded-3xl border border-gray-100 h-full">
            <p class="text-sm font-bold text-gray-500 mb-4">Master Switch</p>
            <div class="flex items-center gap-4">
              <button 
                @click="shopSettings.isOpen = !shopSettings.isOpen"
                class="relative w-16 h-9 rounded-full transition-colors duration-300 focus:outline-none shadow-inner"
                :class="shopSettings.isOpen ? 'bg-primary' : 'bg-gray-300'"
              >
                <div 
                  class="absolute top-1 left-1 bg-white w-7 h-7 rounded-full transition-transform duration-300 shadow-sm flex items-center justify-center"
                  :class="shopSettings.isOpen ? 'translate-x-7' : 'translate-x-0'"
                ></div>
              </button>
              <span class="font-bold text-lg transition-colors duration-300" :class="shopSettings.isOpen ? 'text-primary' : 'text-gray-400'">
                {{ shopSettings.isOpen ? "We're Open!" : "Closed" }}
              </span>
            </div>
          </div>

          <div class="flex flex-col justify-center items-start bg-gray-50 p-5 rounded-3xl border border-gray-100 h-full">
            <p class="text-sm font-bold text-gray-500 mb-4 flex items-center gap-1.5"><TruckIcon class="w-4 h-4"/> Home Delivery</p>
            <div class="flex items-center gap-4">
              <button 
                @click="shopSettings.deliveryAvailable = !shopSettings.deliveryAvailable"
                class="relative w-16 h-9 rounded-full transition-colors duration-300 focus:outline-none shadow-inner"
                :class="shopSettings.deliveryAvailable ? 'bg-secondary' : 'bg-gray-300'"
              >
                <div 
                  class="absolute top-1 left-1 bg-white w-7 h-7 rounded-full transition-transform duration-300 shadow-sm flex items-center justify-center"
                  :class="shopSettings.deliveryAvailable ? 'translate-x-7' : 'translate-x-0'"
                ></div>
              </button>
              <span class="font-bold text-sm transition-colors duration-300 leading-tight" :class="shopSettings.deliveryAvailable ? 'text-gray-900' : 'text-gray-400'">
                {{ shopSettings.deliveryAvailable ? "Delivery Enabled" : "Pickup Only" }}
              </span>
            </div>
          </div>

          <div class="md:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-6 bg-gray-50 p-5 rounded-3xl border border-gray-100">
            <div>
              <p class="text-sm font-bold text-gray-500 mb-2 flex items-center gap-1.5"><ClockIcon class="w-4 h-4"/> Opening Time</p>
              <input 
                type="time" 
                v-model="shopSettings.openTime"
                class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 font-bold text-gray-800 focus:ring-2 focus:ring-primary/20 outline-none"
              >
            </div>
            <div>
              <p class="text-sm font-bold text-gray-500 mb-2 flex items-center gap-1.5"><ClockIcon class="w-4 h-4"/> Closing Time</p>
              <input 
                type="time" 
                v-model="shopSettings.closeTime"
                class="w-full bg-white border border-gray-200 rounded-xl px-4 py-2.5 font-bold text-gray-800 focus:ring-2 focus:ring-primary/20 outline-none"
              >
            </div>
            
            <div class="md:col-span-2 pt-3 border-t border-gray-200">
              <p class="text-sm font-bold text-gray-500 mb-3 flex items-center gap-1.5"><CalendarDaysIcon class="w-4 h-4"/> Working Days</p>
              <div class="flex flex-wrap gap-2">
                <button 
                  v-for="day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']" 
                  :key="day"
                  @click="toggleDay(day)"
                  class="px-4 py-1.5 rounded-full text-sm font-bold transition-all duration-200 active:scale-95"
                  :class="shopSettings.days.includes(day) ? 'bg-primary text-white shadow-sm' : 'bg-white border border-gray-200 text-gray-400 hover:border-primary/50 hover:text-primary'"
                >
                  {{ day }}
                </button>
              </div>
            </div>
          </div>

        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-2 bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8 hover:shadow-md transition-shadow duration-300">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-primary flex items-center gap-2">
              Live Inventory
              <span class="relative flex h-2.5 w-2.5">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-secondary opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-primary"></span>
              </span>
            </h2>
            <button @click="router.push('/inventory')" class="text-sm font-bold text-primary hover:underline hover:text-primary/80 transition-colors">View All</button>
          </div>

          <div class="space-y-4">
            <div 
              v-for="item in inventory.slice(0, 5)" 
              :key="item._id || item.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-3xl hover:bg-white hover:shadow-md hover:scale-[1.01] transition-all duration-300 border border-transparent hover:border-secondary/30 group"
            >
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-3xl shadow-sm shrink-0 group-hover:shadow transition-shadow">
                  {{ item.emoji || '🥩' }}
                </div>
                <div>
                  <h4 class="font-bold text-gray-900 group-hover:text-primary transition-colors">{{ item.name }}</h4>
                  <p class="text-sm font-medium text-gray-500">₹{{ item.price }} / {{ item.unit }}</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <button 
                  @click="toggleStock(item)"
                  class="relative w-14 h-8 rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:ring-offset-2"
                  :class="item.inStock ? 'bg-primary' : 'bg-gray-300'"
                >
                  <div 
                    class="absolute top-1 left-1 bg-white w-6 h-6 rounded-full transition-transform duration-300 shadow-sm"
                    :class="item.inStock ? 'translate-x-6' : 'translate-x-0'"
                  ></div>
                </button>
                <span class="text-sm font-bold w-16 text-right transition-colors duration-300" :class="item.inStock ? 'text-primary' : 'text-gray-400'">
                  {{ item.inStock ? 'In Stock' : 'Out' }}
                </span>
                <button class="p-2 text-gray-400 hover:text-primary transition-all duration-300 bg-white rounded-xl shadow-sm hover:shadow hover:-translate-y-0.5 active:translate-y-0">
                  <Edit2Icon class="w-4 h-4" />
                </button>
              </div>
            </div>
            
            <p v-if="inventory.length > 5" class="text-center text-xs font-bold text-gray-400 mt-4">
              + {{ inventory.length - 5 }} more items. Click "View All" to manage.
            </p>
          </div>
        </div>

        <div class="bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8 hover:shadow-md transition-shadow duration-300">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-primary">Live Orders</h2>
            <span v-if="stats.orders > 0" class="bg-red-50 border border-red-100 text-red-600 text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5 shadow-sm animate-pulse">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full"></span>
              {{ stats.orders }} Pending
            </span>
          </div>

          <div class="space-y-5">
            <div v-if="activeOrders.length === 0" class="text-center text-gray-400 py-8">
              <p class="font-medium text-sm">No new orders yet.</p>
            </div>
            
            <div 
              v-for="order in activeOrders" 
              :key="order.id"
              class="border border-gray-100 rounded-3xl p-4 shadow-sm hover:shadow-lg hover:border-primary/20 transition-all duration-300 relative overflow-hidden group hover:-translate-y-0.5"
            >
              <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-accent-1 group-hover:bg-primary transition-colors duration-300"></div>
              
              <div class="flex justify-between items-start mb-2 pl-2">
                <h4 class="font-bold text-gray-900">{{ order.customerName }}</h4>
                <span class="text-xs font-bold text-gray-500 bg-gray-50 px-2 py-1 rounded-md">{{ order.time }}</span>
              </div>
              
              <p class="text-sm text-gray-600 font-medium pl-2 mb-4 flex items-center gap-1.5">
                <span class="text-base">{{ order.emoji }}</span>
                <span>1x <strong class="text-gray-800">{{ order.itemName }}</strong></span> 
                <span class="mx-1">•</span>
                <span class="text-primary font-bold">₹{{ order.total }}</span>
              </p>

              <div class="flex gap-2 pl-2">
                <button 
                  @click="updateOrderStatus(order.id, 'Declined')"
                  class="grow bg-gray-50 hover:bg-red-50 hover:text-red-600 text-gray-700 font-bold py-2 px-3 rounded-xl text-sm transition-colors duration-300 active:scale-95">
                  Decline
                </button>
                <button 
                  @click="updateOrderStatus(order.id, 'Accepted')"
                  class="grow bg-accent-1 text-primary hover:bg-primary hover:text-white font-bold py-2 px-3 rounded-xl text-sm transition-colors duration-300 shadow-sm active:scale-95">
                  Accept
                </button>
              </div>
            </div>
          </div>
          
        </div>

      </div>

    </main>

    <transition
      enter-active-class="transition duration-300 ease-out"
      enter-from-class="opacity-0 scale-95 translate-y-4"
      enter-to-class="opacity-100 scale-100 translate-y-0"
      leave-active-class="transition duration-200 ease-in"
      leave-from-class="opacity-100 scale-100 translate-y-0"
      leave-to-class="opacity-0 scale-95 translate-y-4"
    >
      <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center px-4">
        
        <div class="absolute inset-0 bg-gray-900/40 backdrop-blur-sm transition-opacity" @click="closeModal"></div>

        <div class="bg-white w-full max-w-lg rounded-4xl shadow-2xl p-8 relative transform z-10 border border-gray-100">
          
          <button @click="closeModal" class="absolute top-6 right-6 text-gray-400 hover:text-gray-700 bg-gray-50 hover:bg-gray-100 p-2 rounded-full transition-colors active:scale-95">
            <XIcon class="w-5 h-5" />
          </button>

          <h3 class="text-2xl font-bold text-gray-900 mb-6">Add New Item</h3>

          <form @submit.prevent="saveItem" class="space-y-5">
            
            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Item Name</label>
              <input 
                v-model="formData.name" 
                type="text" 
                placeholder="e.g. Seer Fish, Mutton Curry Cut"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 hover:border-gray-300"
                required
              />
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Category</label>
              <select 
                v-model="formData.category"
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none hover:border-gray-300 cursor-pointer"
                required
              >
                <option value="" disabled>Select a category</option>
                <option v-for="cat in categories" :key="cat" :value="cat">{{ cat }}</option>
              </select>
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Estimated Price (₹)</label>
                <input 
                  v-model="formData.price" 
                  type="number" 
                  min="0"
                  step="0.01"
                  placeholder="0.00"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 hover:border-gray-300"
                  required
                />
              </div>
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Per Unit</label>
                <select 
                  v-model="formData.unit"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none hover:border-gray-300 cursor-pointer"
                  required
                >
                  <option v-for="u in units" :key="u" :value="u">{{ u }}</option>
                </select>
              </div>
            </div>

            <div class="flex items-center justify-between p-4 bg-gray-50 rounded-2xl border border-gray-200 mt-2 hover:border-primary/30 transition-colors">
              <div>
                <p class="font-bold text-gray-900">Stock Status</p>
                <p class="text-xs text-gray-500 font-medium">Is this currently available?</p>
              </div>
              <button 
                type="button"
                @click="formData.inStock = !formData.inStock"
                class="relative w-14 h-8 rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:ring-offset-2 shadow-inner"
                :class="formData.inStock ? 'bg-primary' : 'bg-gray-300'"
              >
                <div 
                  class="absolute top-1 left-1 bg-white w-6 h-6 rounded-full transition-transform duration-300 shadow-sm"
                  :class="formData.inStock ? 'translate-x-6' : 'translate-x-0'"
                ></div>
              </button>
            </div>

            <div class="flex gap-3 pt-4 border-t border-gray-100">
              <button 
                type="button"
                @click="closeModal"
                class="w-1/3 bg-gray-100 text-gray-600 font-bold py-3.5 rounded-2xl hover:bg-gray-200 hover:text-gray-800 transition-colors active:scale-95"
              >
                Cancel
              </button>
              <button 
                type="submit"
                class="w-2/3 bg-primary text-white font-bold py-3.5 rounded-2xl hover:bg-primary/90 hover:shadow-lg hover:shadow-primary/30 hover:-translate-y-0.5 active:translate-y-0 active:scale-95 transition-all duration-300"
              >
                Add Item
              </button>
            </div>

          </form>
        </div>
      </div>
    </transition>

  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'
import { ref, onMounted, computed } from 'vue' 
import { useRouter } from 'vue-router'
import axios from 'axios'

import { 
  PlusIcon, ShoppingBagIcon, TrendingUpIcon, PackageIcon, 
  Edit2Icon, XIcon, StoreIcon, ClockIcon, CalendarDaysIcon, 
  FileTextIcon, CreditCardIcon, ReceiptIcon, TruckIcon , LifeBuoyIcon
} from 'lucide-vue-next'

const router = useRouter()
const vendorName = ref('Partner')

const inventory = ref([]) 
const activeOrders = ref([])

const stats = ref({
  orders: 0,
  revenue: 0,
  activeItems: 0
})

const calculatedFee = computed(() => {
  return (stats.value.revenue * 0.03).toFixed(2);
})

const shopSettings = ref({
  isOpen: true, 
  deliveryAvailable: false, 
  openTime: '08:00',
  closeTime: '21:00',
  days: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
})

const toggleDay = (day) => {
  if (shopSettings.value.days.includes(day)) {
    shopSettings.value.days = shopSettings.value.days.filter(d => d !== day)
  } else {
    shopSettings.value.days.push(day)
  }
}

const saveShopSettings = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.put('http://localhost:3000/api/auth/vendor/settings', 
      { 
        isOpen: shopSettings.value.isOpen,
        deliveryAvailable: shopSettings.value.deliveryAvailable,
        openTime: shopSettings.value.openTime,
        closeTime: shopSettings.value.closeTime
      },
      { headers: { Authorization: `Bearer ${token}` } }
    );
    if (response.data.success) {
      alert("Shop settings saved successfully!");
    }
  } catch (error) {
    alert("Failed to save shop settings.");
  }
}

const isModalOpen = ref(false)

// UPDATED: Syncing categories and units to the new meat/fish pivot
const categories = ['Fish & Seafood', 'Chicken', 'Mutton' ,' Beef', 'Duck & Poultry', 'Farm Eggs', 'Marinades & Spices']
const units = ['kg', 'gram', 'nos', 'dozen']

const formData = ref({
  name: '',
  category: '',
  price: '',
  unit: 'kg',
  inStock: true
})

const openAddModal = () => {
  formData.value = { name: '', category: '', price: '', unit: 'kg', inStock: true }
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}

const saveItem = async () => {
  try {
    const token = localStorage.getItem('token');
    const response = await axios.post('http://localhost:3000/api/inventory/add', formData.value, {
      headers: { Authorization: `Bearer ${token}` }
    });

    if(response.data.success) {
       inventory.value.unshift(response.data.product);
       stats.value.activeItems = inventory.value.length; 
       closeModal();
    }
  } catch (error) {
    console.error("Error saving item:", error);
    alert("Failed to save item to database.");
  }
}

const parseJwt = (token) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return JSON.parse(jsonPayload);
  } catch (e) {
    return null;
  }
}

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token) {
    const decoded = parseJwt(token);
    if (decoded && decoded.shopName) {
      vendorName.value = decoded.shopName;
    }

    try {
      const settingsResponse = await axios.get('http://localhost:3000/api/auth/vendor/settings', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if(settingsResponse.data.success) {
        shopSettings.value.isOpen = settingsResponse.data.isOpen;
        shopSettings.value.deliveryAvailable = settingsResponse.data.deliveryAvailable || false; 
        shopSettings.value.openTime = settingsResponse.data.openTime;
        shopSettings.value.closeTime = settingsResponse.data.closeTime;
      }
    } catch (settingsError) {
      console.warn("Could not fetch initial shop settings.", settingsError);
    }

    try {
      const invResponse = await axios.get('http://localhost:3000/api/inventory', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if(invResponse.data.success) {
        inventory.value = invResponse.data.products;
        stats.value.activeItems = inventory.value.length; 
      }

      const orderResponse = await axios.get('http://localhost:3000/api/inventory/orders', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if(orderResponse.data.success) {
        activeOrders.value = orderResponse.data.orders.map(order => ({
          id: order._id,
          customerName: order.customerName,
          itemName: order.item ? order.item.name : 'Unknown Item',
          emoji: order.item ? order.item.emoji : '📦',
          total: order.item ? order.item.price : '0', 
          time: 'Just now'
        }));

        stats.value.orders = activeOrders.value.length; 
        
        stats.value.revenue = activeOrders.value.reduce((sum, order) => {
          const safeTotalString = (order.total || '0').toString();
          const amount = parseInt(safeTotalString.replace(/[^0-9]/g, '')) || 0;
          return sum + amount;
        }, 0);  
      }
    } catch (error) {
      console.error("Failed to load dashboard data:", error);
    }
  }
})

const toggleStock = async (item) => {
  const token = localStorage.getItem('token');
  item.inStock = !item.inStock; 
  try {
    await axios.put(`http://localhost:3000/api/inventory/update/${item._id}`, 
      { inStock: item.inStock }, 
      { headers: { Authorization: `Bearer ${token}` } }
    );
  } catch (error) {
    item.inStock = !item.inStock;
    console.error("Failed to update stock status", error);
  }
}

const updateOrderStatus = async (orderId, newStatus) => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.put(`http://localhost:3000/api/orders/status/${orderId}`, 
      { status: newStatus },
      { headers: { Authorization: `Bearer ${token}` } }
    );

    if (response.data.success) {
      activeOrders.value = activeOrders.value.filter(o => o.id !== orderId);
      stats.value.orders = activeOrders.value.length; 
    }
  } catch (error) {
    console.error("Failed to update status", error);
  }
}

setInterval(async () => {
  const token = localStorage.getItem('token');
  if (!token) return;

  try {
    const orderResponse = await axios.get('http://localhost:3000/api/inventory/orders', {
      headers: { Authorization: `Bearer ${token}` }
    });
    if(orderResponse.data.success) {
      activeOrders.value = orderResponse.data.orders.map(order => ({
        id: order._id,
        customerName: order.customerName,
        itemName: order.item ? order.item.name : 'Unknown Item',
        emoji: order.item ? order.item.emoji : '📦',
        total: order.item ? order.item.price : '0', 
        time: 'Just now'
      }));
      stats.value.orders = activeOrders.value.length;
    }
  } catch (e) {
  }
}, 10000);
</script>