<template>
  <div class="min-h-screen bg-gray-50 flex flex-col font-sans selection:bg-secondary/40">
    
    <Navbar />

    <main class="grow flex items-center justify-center px-6 pt-28 pb-16">
      <div class="bg-white w-full max-w-3xl rounded-4xl shadow-xl border border-gray-100 p-8 sm:p-10 relative overflow-hidden">
        
        <div class="text-center mb-10">
          <h2 class="text-3xl font-bold text-primary tracking-tight">Partner with StockUndo</h2>
          <p class="text-gray-500 mt-2 font-medium">Get your local shop in front of thousands of nearby customers.</p>
        </div>

        <form @submit.prevent="handleVendorRegister" class="space-y-8">
          
          <div>
            <h3 class="text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4">Basic Information</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Shop/Business Name</label>
                <input 
                  v-model="regForm.shopName" 
                  type="text" 
                  placeholder="Your shop name"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Owner's Full Name</label>
                <input 
                  v-model="regForm.ownerName" 
                  type="text" 
                  placeholder="Your Name"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Business Email</label>
                <input 
                  v-model="regForm.email" 
                  type="email" 
                  placeholder="shop@example.com"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Phone Number</label>
                <input 
                  v-model="regForm.phone" 
                  type="tel" 
                  placeholder="+91"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4">Shop Location</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">State</label>
                <select 
                  v-model="regForm.address.state"
                  @change="handleStateChange"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none cursor-pointer"
                  required
                >
                  <option value="" disabled>Select State</option>
                  <option v-for="state in Object.keys(locationData)" :key="state" :value="state">{{ state }}</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">District</label>
                <select 
                  v-model="regForm.address.district"
                  @change="handleDistrictChange"
                  :disabled="!regForm.address.state"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
                  required
                >
                  <option value="" disabled>Select District</option>
                  <option v-for="district in availableDistricts" :key="district" :value="district">{{ district }}</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Area / Circle</label>
                <select 
                  v-model="regForm.address.area"
                  :disabled="!regForm.address.district"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
                  required
                >
                  <option value="" disabled>Select Area</option>
                  <option v-for="area in availableAreas" :key="area" :value="area">{{ area }}</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Building / Street Name</label>
                <input 
                  v-model="regForm.address.streetOrBuilding" 
                  type="text" 
                  placeholder="e.g. Near Grand Mall, Main Road"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>
            </div>

            <div>
              <label class="block text-sm font-bold text-gray-700 mb-2">Google Maps Link <span class="text-gray-400 font-normal">(Optional)</span></label>
              <input 
                v-model="regForm.mapUrl" 
                type="url" 
                placeholder="https://goo.gl/maps/..."
                class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
              />
              <p class="text-xs text-gray-500 mt-1.5">Paste the "Share" link from Google Maps so customers can find you easily.</p>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-bold text-gray-900 border-b border-gray-100 pb-2 mb-4">Security</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Create Password</label>
                <input 
                  v-model="regForm.password" 
                  type="password" 
                  placeholder="••••••••"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Confirm Password</label>
                <input 
                  v-model="regForm.confirmPassword" 
                  type="password" 
                  placeholder="••••••••"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all font-medium text-gray-800"
                  required
                />
              </div>
            </div>
          </div>

         <button 
            type="submit"
            :disabled="isLoading"
            class="w-full mt-6 bg-accent-1 text-primary font-bold text-lg py-4 rounded-2xl hover:brightness-95 active:scale-[0.98] transition-all shadow-sm flex justify-center items-center gap-2 disabled:opacity-70"
          >
            <Loader2Icon v-if="isLoading" class="w-6 h-6 animate-spin" />
            <span v-else>Register My Shop</span>
          </button>

        </form>

        <p class="text-center text-sm text-gray-600 mt-8 font-medium">
          Already a partner? 
          <router-link to="/vendor-login" class="text-primary font-bold hover:underline ml-1">
            Login here
          </router-link>
        </p>

      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Navbar from '../components/Navbar.vue'
import { Loader2Icon } from 'lucide-vue-next' 

const router = useRouter()
const isLoading = ref(false)

// NEW: Structured Location Data
// This is a sample structure. You can expand this JSON easily later.
const locationData = {
  "Kerala": {
    "Ernakulam": ["Kakkanad", "Edappally", "Kaloor", "Aluva", "Vyttila"],
    "Thiruvananthapuram": ["Kazhakootam", "Pattom", "Vazhuthacaud", "Kovalam"],
    "Kozhikode": ["Nadakkavu", "Mavoor Road", "Beach Road", "Thondayad"]
  },
  "Karnataka": {
    "Bengaluru Urban": ["Indiranagar", "Koramangala", "Whitefield", "Jayanagar", "Marathahalli"],
    "Mysuru": ["Gokulam", "Kuvempunagar", "Saraswathipuram", "Vijayanagar"]
  },
  "Tamil Nadu": {
    "Chennai": ["T Nagar", "Adyar", "Velachery", "Anna Nagar", "OMR"],
    "Coimbatore": ["RS Puram", "Peelamedu", "Gandhipuram", "Saravanampatti"]
  }
}

const regForm = ref({
  shopName: '',
  ownerName: '',
  email: '',
  phone: '',
  // Nested address object to match backend
  address: {
    state: '',
    district: '',
    area: '',
    streetOrBuilding: ''
  },
  mapUrl: '',
  password: '',
  confirmPassword: ''
})

// Dynamic computations for the dropdowns
const availableDistricts = computed(() => {
  if (!regForm.value.address.state) return [];
  return Object.keys(locationData[regForm.value.address.state]);
})

const availableAreas = computed(() => {
  if (!regForm.value.address.state || !regForm.value.address.district) return [];
  return locationData[regForm.value.address.state][regForm.value.address.district];
})

// Reset lower-level dropdowns when a higher-level one changes
const handleStateChange = () => {
  regForm.value.address.district = '';
  regForm.value.address.area = '';
}

const handleDistrictChange = () => {
  regForm.value.address.area = '';
}

const handleVendorRegister = async () => {
  if(regForm.value.password !== regForm.value.confirmPassword) {
    alert("Passwords do not match!")
    return
  }
  
  try {
    isLoading.value = true;
    
    // The structured 'address' object is sent seamlessly as part of regForm.value
    const response = await axios.post('http://localhost:3000/api/auth/vendor/register', regForm.value);
    
    localStorage.setItem('token', response.data.token);
    localStorage.setItem('userEmail', regForm.value.email);
    
    alert("Shop Registered Successfully!");
    router.push('/dashboard'); 
    
  } catch (error) {
    console.error("Registration Error:", error);
    alert(error.response?.data?.error || "Failed to register. Is your server running?");
  } finally {
    isLoading.value = false;
  }
}
</script>