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
const uploadStatus = ref('') // 'uploading', 'success', 'error'
const rentals = ref([]) 

// 1. Fetch User Status on Load
onMounted(async () => {
  const userId = localStorage.getItem('user_id')
  const userEmail = localStorage.getItem('user_email') 

  // Redirect if not logged in
  if (!userId) {
    router.push('/login')
    return
  }
  
  // Set User Email
  user.value.email = userEmail || localStorage.getItem('email') || 'User' 

  try {
    // Correct Header: Token <key>
    const response = await axios.get(`${API_URL}/api/user/status/`, {
      headers: { Authorization: `Token ${localStorage.getItem('token')}` }
    })
    user.value.is_verified = response.data.is_verified
    user.value.has_uploaded_id = response.data.has_uploaded_id

  } catch (err) {
    console.error("Failed to fetch status")
  } finally {
    loading.value = false
  }
})

// 2. Handle File Selection
const onFileChange = (e) => {
  selectedFile.value = e.target.files[0]
}

// 3. Upload Logic
const handleUpload = async () => {
  if (!selectedFile.value) return

  // --- NEW: CHECK FILE SIZE ---
  const fileSizeInMB = selectedFile.value.size / 1024 / 1024; // Convert bytes to MB
  if (fileSizeInMB > 5) {
    alert("File is too large! Please upload an image smaller than 5MB.");
    return;
  }
  // ----------------------------

  uploadStatus.value = 'uploading'
  const formData = new FormData()
  formData.append('id_proof', selectedFile.value)

  // Retrieve the token
  const token = localStorage.getItem('token')

  try {
    await axios.post(`${API_URL}/api/user/upload-id/`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Token ${token}`
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

// 4. Logout
const handleLogout = () => {
  localStorage.clear()
  router.push('/')
}
</script>

<template>
  <div class="min-h-screen bg-[#061E29] pt-32 pb-20 px-4 relative overflow-hidden">
    
    <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-[#1D546D]/20 blur-[120px] rounded-full pointer-events-none"></div>

    <div class="max-w-5xl mx-auto relative z-10">
      
      <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12 border-b border-white/10 pb-6 gap-4">
        <div>
          <h1 class="text-3xl font-bold text-white mb-2">My Dashboard</h1>
          
          <div class="flex items-center gap-2 text-[#5F9598] bg-[#5F9598]/10 px-3 py-1 rounded-full w-fit border border-[#5F9598]/20">
            <ion-icon name="mail-outline"></ion-icon>
            <span class="text-sm font-medium tracking-wide">{{ user.email }}</span>
          </div>
        </div>

        <button @click="handleLogout" class="text-red-400 hover:text-red-300 text-sm font-bold uppercase tracking-wider flex items-center gap-2 transition-colors">
          <ion-icon name="log-out-outline" style="font-size: 18px;"></ion-icon>
          Sign Out
        </button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
        
        <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl">
          <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Account Status</h2>
          
          <div class="flex items-center gap-4 mb-6">
            <div class="w-16 h-16 rounded-full flex items-center justify-center text-2xl shadow-inner transition-colors duration-500"
              :class="user.is_verified ? 'bg-green-500/20 text-green-400 shadow-[0_0_15px_-3px_rgba(74,222,128,0.3)]' : 'bg-amber-500/20 text-amber-400'">
              <ion-icon :name="user.is_verified ? 'checkmark-circle' : 'time'"></ion-icon>
            </div>
            <div>
              <p class="text-white font-bold text-xl">
                {{ user.is_verified ? 'Verified Member' : 'Verification Pending' }}
              </p>
              <p class="text-sm text-gray-400">
                {{ user.is_verified ? 'Access granted for all premium rentals.' : 'Admin approval required to rent.' }}
              </p>
            </div>
          </div>

          <div class="space-y-4">
            <div class="flex items-center gap-3 text-sm">
              <ion-icon name="checkmark-circle" class="text-green-400"></ion-icon>
              <span class="text-gray-300">Email Verified</span>
            </div>
            <div class="flex items-center gap-3 text-sm">
              <ion-icon :name="user.has_uploaded_id ? 'checkmark-circle' : 'ellipse-outline'" 
                :class="user.has_uploaded_id ? 'text-green-400' : 'text-gray-500'"></ion-icon>
              <span class="text-gray-300">ID Proof Uploaded</span>
            </div>
            <div class="flex items-center gap-3 text-sm">
              <ion-icon :name="user.is_verified ? 'checkmark-circle' : 'ellipse-outline'" 
                 :class="user.is_verified ? 'text-green-400' : 'text-gray-500'"></ion-icon>
              <span class="text-gray-300">Admin Approval</span>
            </div>
          </div>
        </div>

        <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl relative overflow-hidden">
          <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">ID Verification</h2>

          <div v-if="user.is_verified" class="h-full flex flex-col items-center justify-center text-center pb-8">
             <ion-icon name="shield-checkmark" class="text-6xl text-green-400 mb-4"></ion-icon>
             <p class="text-white font-bold">You are all set!</p>
             <p class="text-gray-400 text-sm">Your ID has been verified.</p>
          </div>

          <div v-else>
            <p class="text-gray-300 text-sm mb-6">
              Please upload a clear photo of your Government ID (Driving License or Aadhaar) to unlock rentals.
            </p>

            <div class="border-2 border-dashed border-white/10 rounded-xl p-6 text-center hover:border-[#5F9598]/50 transition-colors bg-[#061E29]/30">
              <input type="file" @change="onFileChange" accept="image/*" class="block w-full text-sm text-gray-400
                file:mr-4 file:py-2 file:px-4
                file:rounded-full file:border-0
                file:text-xs file:font-semibold
                file:bg-[#5F9598] file:text-[#061E29]
                hover:file:bg-white
              "/>
            </div>

            <button 
              @click="handleUpload" 
              :disabled="!selectedFile || uploadStatus === 'uploading'"
              class="w-full mt-6 py-3 bg-white/10 hover:bg-[#5F9598] hover:text-[#061E29] text-white font-bold rounded-lg transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {{ uploadStatus === 'uploading' ? 'Uploading...' : 'Submit for Verification' }}
            </button>

            <div v-if="uploadStatus === 'success'" class="mt-4 p-3 bg-green-500/20 text-green-400 text-xs text-center rounded">
              Upload Successful! Please wait for approval.
            </div>
            <div v-if="uploadStatus === 'error'" class="mt-4 p-3 bg-red-500/20 text-red-400 text-xs text-center rounded">
              Upload Failed. Please try again.
            </div>
          </div>
        </div>
      </div>

      <div class="bg-[#0B2B38]/60 backdrop-blur-md rounded-2xl p-8 border border-white/5 shadow-xl">
        <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Your Garage History</h2>
        
        <div v-if="rentals.length > 0" class="overflow-x-auto">
          <table class="w-full text-left">
            <thead class="text-xs text-gray-400 uppercase tracking-wider border-b border-white/10">
              <tr>
                <th class="pb-4 pl-2">Vehicle</th>
                <th class="pb-4">Date</th>
                <th class="pb-4">Total Price</th>
                <th class="pb-4">Status</th>
                <th class="pb-4">Action</th>
              </tr>
            </thead>
            <tbody class="text-sm">
              <tr v-for="rent in rentals" :key="rent.id" class="border-b border-white/5 last:border-0 hover:bg-white/5 transition-colors">
                <td class="py-4 pl-2 font-bold text-white">{{ rent.model }}</td>
                <td class="py-4 text-gray-300">{{ rent.date }}</td>
                <td class="py-4 text-gray-300">₹{{ rent.price }}</td>
                <td class="py-4">
                  <span class="px-2 py-1 rounded text-[10px] font-bold uppercase tracking-wider"
                    :class="rent.status === 'Active' ? 'bg-green-500/20 text-green-400' : 'bg-gray-500/20 text-gray-400'">
                    {{ rent.status }}
                  </span>
                </td>
                <td class="py-4">
                  <button class="text-[#5F9598] hover:text-white text-xs font-bold uppercase tracking-wider">
                    View Details
                  </button>
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

    </div>
  </div>
</template>