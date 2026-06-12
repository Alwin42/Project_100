<template>
  <div class="min-h-screen bg-gray-50 font-sans selection:bg-secondary/40 pb-20">
    
    <Navbar />

    <main class="max-w-6xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-10 gap-4">
        <div>
          <h1 class="text-3xl font-bold text-gray-900 tracking-tight">Inventory Management</h1>
          <p class="text-gray-500 mt-1 font-medium">Add, edit, or remove items from your live store.</p>
        </div>
        <button 
          @click="openAddModal"
          class="bg-primary text-white font-bold px-6 py-3 rounded-full hover:bg-primary/90 hover:shadow-lg hover:shadow-primary/30 hover:-translate-y-0.5 active:scale-95 transition-all duration-300 flex items-center gap-2 group"
        >
          <PlusIcon class="w-5 h-5 transition-transform duration-300 group-hover:rotate-90" />
          Add New Item
        </button>
      </div>

      <div class="bg-white p-4 rounded-3xl border border-gray-100 shadow-sm flex items-center gap-4 mb-8 group hover:shadow-md transition-shadow duration-300">
        <div class="flex items-center bg-gray-50 rounded-2xl grow h-12 px-4 border border-gray-200 focus-within:border-primary focus-within:ring-4 focus-within:ring-primary/10 transition-all duration-300">
          <SearchIcon class="w-5 h-5 text-gray-400 group-focus-within:text-primary transition-colors duration-300" />
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search your inventory..." 
            class="bg-transparent grow px-3 text-gray-800 placeholder-gray-400 focus:outline-none font-medium w-full"
          >
        </div>
      </div>

      <div class="bg-white rounded-4xl border border-gray-100 shadow-sm p-4 md:p-6 transition-all duration-300">
        
        <div v-if="Object.keys(groupedInventory).length === 0" class="p-16 text-center text-gray-500 flex flex-col items-center">
          <PackageOpenIcon class="w-16 h-16 mb-4 text-gray-300 animate-bounce" />
          <p class="font-bold text-xl text-gray-700">No items found.</p>
          <p class="text-sm mt-1">Click "Add New Item" to stock your shop.</p>
        </div>

        <div v-else class="space-y-8">
          
          <div v-for="(items, category) in groupedInventory" :key="category" class="animate-in fade-in duration-500">
            
            <div class="flex items-center gap-3 mb-4 pl-2">
              <h3 class="text-xl font-bold text-gray-900">{{ category }}</h3>
              <span class="bg-gray-100 text-gray-500 text-xs font-bold px-2.5 py-1 rounded-full">{{ items.length }}</span>
            </div>

            <div class="space-y-3">
              <div 
                v-for="item in items" 
                :key="item._id"
                class="flex flex-col md:flex-row items-start md:items-center justify-between p-4 bg-white rounded-3xl hover:bg-gray-50 hover:shadow-md hover:scale-[1.005] transition-all duration-300 border border-gray-100 group gap-4"
              >
                <div class="flex items-center gap-4">
                  <div class="w-14 h-14 bg-secondary/10 rounded-2xl flex items-center justify-center text-primary shadow-sm shrink-0 group-hover:bg-primary group-hover:text-white transition-colors duration-300">
                    <span class="text-2xl">{{ item.emoji || '🥩' }}</span>
                  </div>
                  <div>
                    <h4 class="font-bold text-gray-900 text-lg leading-tight group-hover:text-primary transition-colors duration-300">{{ item.name }}</h4>
                    <div class="flex items-center gap-2 mt-1">
                      <span class="text-sm font-bold text-primary">Est. ₹{{ item.price }} / {{ item.unit }}</span>
                    </div>
                  </div>
                </div>

                <div class="flex items-center gap-4 w-full md:w-auto justify-between md:justify-end border-t md:border-t-0 border-gray-100 pt-3 md:pt-0">
                  
                  <div class="flex items-center gap-3 bg-gray-50 px-3 py-1.5 rounded-2xl border border-gray-100 group-hover:border-gray-200 transition-colors">
                    <button 
                      @click="toggleStock(item)"
                      class="relative w-12 h-6 rounded-full transition-colors duration-300 focus:outline-none focus:ring-2 focus:ring-primary/50 focus:ring-offset-2"
                      :class="item.inStock ? 'bg-primary' : 'bg-gray-300'"
                    >
                      <div 
                        class="absolute top-1 left-1 bg-white w-4 h-4 rounded-full transition-transform duration-300 shadow-sm"
                        :class="item.inStock ? 'translate-x-6' : 'translate-x-0'"
                      ></div>
                    </button>
                    <span class="text-sm font-bold w-16 transition-colors duration-300" :class="item.inStock ? 'text-primary' : 'text-gray-400'">
                      {{ item.inStock ? 'In Stock' : 'Out' }}
                    </span>
                  </div>

                  <div class="flex items-center gap-2">
                    <button @click="openEditModal(item)" class="p-2.5 text-gray-400 hover:text-primary hover:bg-secondary/10 transition-all duration-300 bg-white rounded-xl shadow-sm border border-gray-100 hover:border-primary/30 active:scale-95">
                      <Edit2Icon class="w-4 h-4" />
                    </button>
                    <button @click="deleteItem(item._id)" class="p-2.5 text-gray-400 hover:text-red-600 hover:bg-red-50 transition-all duration-300 bg-white rounded-xl shadow-sm border border-gray-100 hover:border-red-200 active:scale-95">
                      <Trash2Icon class="w-4 h-4" />
                    </button>
                  </div>
                </div>
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

          <h3 class="text-2xl font-bold text-gray-900 mb-6">{{ isEditing ? 'Edit Item' : 'Add New Item' }}</h3>

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
                {{ isEditing ? 'Save Changes' : 'Add Item' }}
              </button>
            </div>

          </form>
        </div>
      </div>
    </transition>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue' 
import axios from 'axios' 
import Navbar from '../components/Navbar.vue'
import { PlusIcon, SearchIcon, Edit2Icon, Trash2Icon, PackageOpenIcon, XIcon } from 'lucide-vue-next'

const categories = ['Fish & Seafood', 'Chicken', 'Mutton & Beef', 'Duck & Poultry', 'Farm Eggs', 'Marinades & Spices']
const units = ['kg', 'gram', 'nos', 'dozen']

const inventory = ref([]) 

const searchQuery = ref('')
const isModalOpen = ref(false)
const isEditing = ref(false)
const currentItemId = ref(null)

const formData = ref({
  name: '',
  category: '',
  price: '',
  unit: 'kg', 
  inStock: true
})

const fetchInventory = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.get('http://localhost:3000/api/inventory', {
      headers: { Authorization: `Bearer ${token}` }
    });
    if (response.data.success) {
      inventory.value = response.data.products;
    }
  } catch (error) {
    console.error("Failed to load inventory:", error);
  }
}

onMounted(() => {
  fetchInventory();
})

const groupedInventory = computed(() => {
  let items = inventory.value;
  
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    items = items.filter(item => 
      item.name.toLowerCase().includes(query) || 
      item.category.toLowerCase().includes(query)
    )
  }

  const groups = {};
  items.forEach(item => {
    if (!groups[item.category]) {
      groups[item.category] = [];
    }
    groups[item.category].push(item);
  });

  return groups; 
})

const openAddModal = () => {
  isEditing.value = false
  currentItemId.value = null
  formData.value = { name: '', category: '', price: '', unit: 'kg', inStock: true }
  isModalOpen.value = true
}

const openEditModal = (item) => {
  isEditing.value = true
  currentItemId.value = item._id 
  formData.value = { ...item } 
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}

const saveItem = async () => {
  const token = localStorage.getItem('token');
  try {
    if (isEditing.value) {
      const response = await axios.put(`http://localhost:3000/api/inventory/update/${currentItemId.value}`, formData.value, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (response.data.success) {
        const index = inventory.value.findIndex(item => item._id === currentItemId.value);
        if (index !== -1) inventory.value[index] = response.data.product;
      }
    } else {
      const response = await axios.post('http://localhost:3000/api/inventory/add', formData.value, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (response.data.success) {
        inventory.value.unshift(response.data.product); 
      }
    }
    closeModal();
  } catch (error) {
    console.error("Failed to save item", error);
  }
}

const toggleStock = async (item) => {
  const token = localStorage.getItem('token');
  item.inStock = !item.inStock; 
  try {
    await axios.put(`http://localhost:3000/api/inventory/update/${item._id}`, { inStock: item.inStock }, {
      headers: { Authorization: `Bearer ${token}` }
    });
  } catch (error) {
    item.inStock = !item.inStock;
    console.error("Failed to update stock status", error);
  }
}

const deleteItem = async (id) => {
  if(confirm("Are you sure you want to delete this item?")) {
    const token = localStorage.getItem('token');
    try {
      await axios.delete(`http://localhost:3000/api/inventory/delete/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      inventory.value = inventory.value.filter(item => item._id !== id);
    } catch (error) {
      console.error("Failed to delete item", error);
    }
  }
}
</script>