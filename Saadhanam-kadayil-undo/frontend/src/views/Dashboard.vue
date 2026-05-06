<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <!-- Header -->
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4 animate-in fade-in slide-in-from-bottom-4 duration-700 ease-out">
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

      <!-- Stat Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        
        <div class="bg-primary rounded-4xl p-6 text-white shadow-lg shadow-primary/20 relative overflow-hidden group hover:-translate-y-1.5 transition-all duration-300 cursor-default">
          <div class="absolute top-0 right-0 -mr-6 -mt-6 w-32 h-32 bg-white/10 rounded-full blur-2xl pointer-events-none group-hover:scale-150 transition-transform duration-700"></div>
          <div class="flex justify-between items-start mb-4 relative z-10">
            <div class="p-2.5 bg-white/20 rounded-2xl group-hover:scale-110 transition-transform duration-300">
              <ShoppingBagIcon class="w-6 h-6 text-white" />
            </div>
            <span class="bg-accent-1 text-primary text-xs font-bold px-3 py-1 rounded-full shadow-sm">+12% today</span>
          </div>
          <h3 class="text-white/90 font-medium mb-1 relative z-10">Total Orders</h3>
          <p class="text-4xl font-bold relative z-10">42</p>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:shadow-gray-200/50 hover:border-gray-200 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group cursor-default">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-secondary/20 rounded-2xl group-hover:bg-secondary/30 transition-colors duration-300">
              <TrendingUpIcon class="w-6 h-6 text-primary" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Today's Revenue</h3>
            <p class="text-3xl font-bold text-gray-900 group-hover:text-primary transition-colors duration-300">₹4,850</p>
          </div>
        </div>

        <div class="bg-white rounded-4xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:shadow-gray-200/50 hover:border-gray-200 hover:-translate-y-1.5 transition-all duration-300 flex flex-col justify-between group cursor-default">
          <div class="flex justify-between items-start mb-4">
            <div class="p-2.5 bg-accent-1/40 rounded-2xl group-hover:bg-accent-1/60 transition-colors duration-300">
              <PackageIcon class="w-6 h-6 text-accent-2" />
            </div>
          </div>
          <div>
            <h3 class="text-gray-500 font-medium mb-1">Active Items in Store</h3>
            <p class="text-3xl font-bold text-gray-900">128</p>
          </div>
        </div>

      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- Live Inventory Panel -->
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
              v-for="item in inventory" 
              :key="item.id"
              class="flex items-center justify-between p-4 bg-gray-50 rounded-3xl hover:bg-white hover:shadow-md hover:scale-[1.01] transition-all duration-300 border border-transparent hover:border-secondary/30 group"
            >
              <div class="flex items-center gap-4">
                <div class="w-14 h-14 bg-white rounded-2xl flex items-center justify-center text-3xl shadow-sm shrink-0 group-hover:shadow transition-shadow">
                  {{ item.emoji || '📦' }}
                </div>
                <div>
                  <h4 class="font-bold text-gray-900 group-hover:text-primary transition-colors">{{ item.name }}</h4>
                  <p class="text-sm font-medium text-gray-500">{{ item.price }}</p>
                </div>
              </div>

              <div class="flex items-center gap-4">
                <button 
                  @click="item.inStock = !item.inStock"
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
          </div>
        </div>

        <!-- Live Orders Panel -->
        <div class="bg-white rounded-4xl border border-gray-100 shadow-sm p-6 md:p-8 hover:shadow-md transition-shadow duration-300">
          <div class="flex justify-between items-center mb-6">
            <h2 class="text-xl font-bold text-primary">Live Orders</h2>
            <span class="bg-red-50 border border-red-100 text-red-600 text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5 shadow-sm animate-pulse">
              <span class="w-1.5 h-1.5 bg-red-500 rounded-full"></span>
              3 Pending
            </span>
          </div>

          <div class="space-y-5">
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
              
              <p class="text-sm text-gray-600 font-medium pl-2 mb-4">
                {{ order.itemsCount }} items • <span class="text-primary font-bold">{{ order.total }}</span>
              </p>

              <div class="flex gap-2 pl-2">
                <button class="grow bg-gray-50 hover:bg-red-50 hover:text-red-600 text-gray-700 font-bold py-2 rounded-xl text-sm transition-colors duration-300 active:scale-95">
                  Decline
                </button>
                <button class="grow bg-accent-1 text-primary hover:bg-primary hover:text-white font-bold py-2 rounded-xl text-sm transition-colors duration-300 shadow-sm active:scale-95">
                  Accept
                </button>
              </div>
            </div>
          </div>
          
        </div>

      </div>

    </main>

    <!-- Add Item Modal with Smooth Transition -->
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
                placeholder="e.g. Fresh Tomatoes"
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
                <label class="block text-sm font-bold text-gray-700 mb-2">Price (₹)</label>
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
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { PlusIcon, ShoppingBagIcon, TrendingUpIcon, PackageIcon, Edit2Icon, XIcon } from 'lucide-vue-next'

const router = useRouter()
const vendorName = ref('Partner')

// --- MODAL STATE ---
const isModalOpen = ref(false)
const categories = ['Vegetables', 'Fruits', 'Dairy & Eggs', 'Bakery', 'Pantry Essentials', 'Meat & Seafood', 'Beverages', 'Snacks']
const units = ['kg', 'gram', 'packet', 'liter', 'ml', 'nos', 'dozen']

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

const saveItem = () => {
  const newItem = {
    id: Date.now(),
    name: formData.value.name,
    emoji: '📦', 
    price: `₹${formData.value.price}/${formData.value.unit}`,
    inStock: formData.value.inStock
  }
  inventory.value.unshift(newItem)
  closeModal()
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

// Start with an empty array
const activeOrders = ref([]);

onMounted(async () => {
  const token = localStorage.getItem('token');
  if (token) {
    const decoded = parseJwt(token);
    if (decoded && decoded.shopName) {
      vendorName.value = decoded.shopName;
    }

    try {
      // 1. Fetch live Inventory
      const invResponse = await axios.get('http://localhost:3000/api/inventory', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if(invResponse.data.success) {
        inventory.value = invResponse.data.products;
      }

      // 2. NEW: Fetch live Orders
      const orderResponse = await axios.get('http://localhost:3000/api/inventory/orders', {
        headers: { Authorization: `Bearer ${token}` }
      });
      if(orderResponse.data.success) {
        // Map the DB output to your UI
        activeOrders.value = orderResponse.data.orders.map(order => ({
          id: order._id,
          customerName: order.customerName,
          itemsCount: order.itemsCount,
          total: order.total,
          time: 'Just now' // You can format order.createdAt using a date library later
        }));
      }

    } catch (error) {
      console.error("Failed to load dashboard data:", error);
    }
  }
})


</script>