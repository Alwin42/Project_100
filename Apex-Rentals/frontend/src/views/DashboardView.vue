<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const API_URL = "http://127.0.0.1:8000"

// State
const loading = ref(true)
const user = ref({ email: '', is_verified: false, has_uploaded_id: false })
const selectedFile = ref(null)
const uploadStatus = ref('')
const rentals = ref([]) // Stores the rental history

onMounted(async () => {
  const userId = localStorage.getItem('user_id')
  const userEmail = localStorage.getItem('user_email') 

  if (!userId) {
    router.push('/login')
    return
  }
  
  user.value.email = userEmail || localStorage.getItem('email') || 'User' 

  try {
    const token = localStorage.getItem('token')
    
    // 1. Fetch User Status
    const statusRes = await axios.get(`${API_URL}/api/user/status/`, {
      headers: { Authorization: `Token ${token}` }
    })
    user.value.is_verified = statusRes.data.is_verified
    user.value.has_uploaded_id = statusRes.data.has_uploaded_id

    // 2. Fetch Rental History (Crucial Fix)
    // We use the new URL: /api/rentals/history/
    const historyRes = await axios.get(`${API_URL}/api/rentals/history/`, {
      headers: { Authorization: `Token ${token}` }
    })
    rentals.value = historyRes.data
    // Debugging: Check console to see if data arrives
    console.log("Rental History:", rentals.value) 

  } catch (err) {
    console.error("Failed to fetch dashboard data", err)
  } finally {
    loading.value = false
  }
})

// File Upload Logic
const onFileChange = (e) => {
  selectedFile.value = e.target.files[0]
}

const handleUpload = async () => {
  if (!selectedFile.value) return
  if (selectedFile.value.size / 1024 / 1024 > 5) {
    alert("File too large (>5MB)")
    return
  }

  uploadStatus.value = 'uploading'
  const formData = new FormData()
  formData.append('id_proof', selectedFile.value)

  try {
    await axios.post(`${API_URL}/api/user/upload-id/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Token ${localStorage.getItem('token')}`
      }
    })
    uploadStatus.value = 'success'
    user.value.has_uploaded_id = true
    setTimeout(() => uploadStatus.value = '', 3000)
  } catch (err) {
    console.error("Upload failed", err)
    uploadStatus.value = 'error'
  }
}

const handleLogout = () => {
  localStorage.clear()
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen bg-[#061E29] pt-32 pb-20 px-4 relative overflow-hidden">
    <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-[#1D546D]/20 blur-[120px] rounded-full pointer-events-none"></div>

    <div class="max-w-6xl mx-auto relative z-10">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 border-b border-white/10 pb-6 gap-4">
        <div>
          <h1 class="text-3xl font-bold text-white mb-2">My Dashboard</h1>
          <div class="flex items-center gap-2 text-[#5F9598] bg-[#5F9598]/10 px-3 py-1 rounded-full w-fit border border-[#5F9598]/20">
            <ion-icon name="mail-outline"></ion-icon>
            <span class="text-sm font-medium tracking-wide">{{ user.email }}</span>
          </div>
        </div>
        <button @click="handleLogout" class="text-red-400 hover:text-red-300 text-sm font-bold uppercase tracking-wider flex items-center gap-2 transition-colors">
          <ion-icon name="log-out-outline" style="font-size: 18px;"></ion-icon> Sign Out
        </button>
      </div>
      <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl">
        <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Your Garage History</h2>
        
        <div v-if="rentals.length > 0" class="overflow-x-auto">
          <table class="w-full text-left">
            <thead class="text-xs text-gray-400 uppercase tracking-wider border-b border-white/10">
              <tr>
                <th class="pb-4 pl-2">Vehicle</th>
                <th class="pb-4">Dates</th>
                <th class="pb-4">Total</th>
                <th class="pb-4">Status</th>
                <th class="pb-4">Receipt</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr v-for="rent in rentals" :key="rent.id" class="border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors">
                <td class="py-4 pl-2 font-bold text-white">
                   {{ rent.car ? rent.car.manufacturer : 'Unknown' }} {{ rent.car ? rent.car.model : 'Car' }}
                </td>
                
                <td class="py-4 text-gray-300">{{ rent.start_date }}</td>
                <td class="py-4 text-gray-300">₹{{ Number(rent.total_price).toLocaleString() }}</td>
                
                <td class="py-4">
                  <span class="px-2 py-1 rounded text-[10px] font-bold uppercase tracking-wider"
                    :class="{
                      'bg-green-500/20 text-green-400': rent.status === 'Active' || rent.status === 'Completed',
                      'bg-amber-500/20 text-amber-400': rent.status === 'Pending Approval',
                      'bg-red-500/20 text-red-400': rent.status === 'Rejected'
                    }">
                    {{ rent.status }}
                  </span>
                </td>
                
                <td class="py-4">
                   <a v-if="rent.payment_proof" :href="rent.payment_proof.startsWith('http') ? rent.payment_proof : API_URL + rent.payment_proof" target="_blank" class="text-[#5F9598] hover:text-white text-xs font-bold uppercase tracking-wider">
                     View
                   </a>
                   <span v-else class="text-gray-600 text-xs">No Receipt</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-else class="text-center py-12 border border-dashed border-white/10 rounded-xl">
           <ion-icon name="car-sport-outline" class="text-4xl text-gray-600 mb-2"></ion-icon>
           <p class="text-gray-400">You haven't rented any cars yet.</p>
           <router-link to="/fleet" class="text-[#5F9598] text-sm font-bold hover:text-white mt-2 inline-block">
             Browse Fleet →
           </router-link>
        </div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
        <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl">
          <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Account Status</h2>
          <div class="flex items-center gap-4 mb-6">
            <div class="w-16 h-16 rounded-full flex items-center justify-center text-2xl shadow-inner transition-colors duration-500"
              :class="user.is_verified ? 'bg-green-500/20 text-green-400 shadow-[0_0_15px_-3px_rgba(74,222,128,0.3)]' : 'bg-amber-500/20 text-amber-400'">
              <ion-icon :name="user.is_verified ? 'checkmark-circle' : 'time'"></ion-icon>
            </div>
            <div>
              <p class="text-white font-bold text-xl">{{ user.is_verified ? 'Verified Member' : 'Verification Pending' }}</p>
              <p class="text-sm text-gray-400">{{ user.is_verified ? 'Access granted for all premium rentals.' : 'Admin approval required.' }}</p>
            </div>
          </div>
        </div>

        <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl">
          <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">ID Verification</h2>
          <div v-if="user.is_verified" class="h-full flex flex-col items-center justify-center text-center pb-8">
             <ion-icon name="shield-checkmark" class="text-6xl text-green-400 mb-4"></ion-icon>
             <p class="text-white font-bold">You are all set!</p>
             <p class="text-gray-400 text-sm">Your ID has been verified.</p>
          </div>
          <div v-else>
            <p class="text-gray-300 text-sm mb-6">Please upload a clear photo of your Government ID.</p>
            <div class="border-2 border-dashed border-white/10 rounded-xl p-6 text-center hover:border-[#5F9598]/50 transition-colors bg-[#061E29]/30">
              <input type="file" @change="onFileChange" accept="image/*" class="block w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-[#5F9598] file:text-[#061E29] hover:file:bg-white"/>
            </div>
            <button @click="handleUpload" :disabled="!selectedFile || uploadStatus === 'uploading'" class="w-full mt-6 py-3 bg-white/10 hover:bg-[#5F9598] hover:text-[#061E29] text-white font-bold rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed">
              {{ uploadStatus === 'uploading' ? 'Uploading...' : 'Submit for Verification' }}
            </button>
            <div v-if="uploadStatus === 'success'" class="mt-4 p-3 bg-green-500/20 text-green-400 text-xs text-center rounded">Upload Successful!</div>
          </div>
        </div>
      </div>



    </div>
  </div>
</template>