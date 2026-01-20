<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const API_URL = "http://127.0.0.1:8000"

const car = ref(null)
const loading = ref(true)
const processing = ref(false)
const success = ref(false)
const selectedFile = ref(null)

onMounted(async () => {
  try {
    // We only fetch the specific Car. 
    // The backend Car model now includes 'qr_image' and 'upi_id'.
    const carRes = await axios.get(`${API_URL}/api/cars/${route.params.id}/`)
    car.value = carRes.data
  } catch (err) {
    console.error("Error loading data", err)
  } finally {
    loading.value = false
  }
})

// Handle File Select
const onFileChange = (e) => {
  selectedFile.value = e.target.files[0]
}

// Handle Payment Submission
const handlePayment = async () => {
  if (!selectedFile.value) {
    alert("Please upload the payment screenshot first!")
    return
  }
  
  processing.value = true
  
  try {
    const token = localStorage.getItem('token')
    
    // Use FormData to send the file and car ID
    const formData = new FormData()
    formData.append('car_id', car.value.id)
    formData.append('payment_proof', selectedFile.value)

    await axios.post(`${API_URL}/api/rentals/create/`, formData, {
      headers: { 
        'Authorization': `Token ${token}`,
        'Content-Type': 'multipart/form-data' 
      }
    })
    
    processing.value = false
    success.value = true
    
    // Redirect to Dashboard after 3 seconds
    setTimeout(() => {
      router.push('/dashboard')
    }, 3000)
    
  } catch (err) {
    console.error("Booking failed", err)
    alert("Booking failed. Please try again.")
    processing.value = false
  }
}
</script>

<template>
  <div class="min-h-screen bg-[#061E29] flex items-center justify-center p-4 relative overflow-hidden">
    <div class="absolute top-0 left-0 w-[500px] h-[500px] bg-[#5F9598]/10 blur-[120px] rounded-full pointer-events-none"></div>

    <div v-if="success" class="bg-[#0B2B38] p-10 rounded-2xl border border-green-500/30 text-center animate-bounce-in shadow-2xl z-10 max-w-md">
      <div class="w-20 h-20 bg-green-500/20 rounded-full flex items-center justify-center mx-auto mb-4 text-green-400 text-4xl">
        <ion-icon name="checkmark"></ion-icon>
      </div>
      <h2 class="text-2xl font-bold text-white mb-2">Request Submitted!</h2>
      <p class="text-gray-400 mb-4">Your payment proof has been sent to the owner.</p>
      <div class="bg-amber-500/10 text-amber-500 p-3 rounded text-sm">
        Status: <strong>Pending Approval</strong>
      </div>
      <p class="text-xs text-gray-500 mt-4">Redirecting to Dashboard...</p>
    </div>

    <div v-else-if="car" class="max-w-5xl w-full grid grid-cols-1 md:grid-cols-2 gap-8 z-10">
      
      <div class="bg-[#0B2B38]/60 backdrop-blur-md p-8 rounded-2xl border border-white/5 h-fit">
        <h2 class="text-[#5F9598] font-bold uppercase tracking-widest text-xs mb-6">Order Summary</h2>
        
        <img :src="car.image.startsWith('http') ? car.image : API_URL + car.image" class="w-full h-90 object-cover rounded-lg mb-6 border border-white/10" />
        
        <h3 class="text-2xl font-bold text-white">{{ car.model }}</h3>
        <p class="text-gray-400 text-sm mb-6">{{ car.manufacturer }} Series</p>
        
        <div class="space-y-2 mb-6">
           <div class="flex justify-between text-sm text-gray-400">
             <span>Owner</span>
             <span class="text-white">{{ car.owner_name }}</span>
           </div>
           <div class="flex justify-between text-sm text-gray-400">
             <span>Contact</span>
             <span class="text-white">{{ car.owner_phone }}</span>
           </div>
        </div>

        <div class="flex justify-between items-center border-t border-white/10 pt-4">
          <span class="text-gray-300">Total Amount</span>
          <span class="text-2xl font-bold text-[#5F9598]">₹{{ Number(car.price_per_day).toLocaleString() }}</span>
        </div>
      </div>

      <div class="bg-[#0B2B38] p-8 rounded-2xl border border-white/5 shadow-2xl">
        <h2 class="text-white font-bold text-xl mb-6 flex items-center gap-2">
          <ion-icon name="qr-code-outline"></ion-icon> Scan & Pay
        </h2>

        <div class="text-center ">
           <div v-if="car.qr_image" class="bg-white p-4 rounded-xl inline-block mb-4 shadow-lg">
              <img :src="car.qr_image.startsWith('http') ? car.qr_image : API_URL + car.qr_image" class="w-70 h-60 object-contain">
           </div>
           
           <div v-else class="h-48 flex items-center justify-center text-gray-500 bg-black/20 rounded-xl mb-4 border border-white/10">
              <div class="text-center px-4">
                 <ion-icon name="image-outline" class="text-3xl mb-2 opacity-50"></ion-icon>
                 <p class="text-xs">No QR Code available.</p>
                 <p class="text-xs text-[#5F9598] mt-1">Please contact {{ car.owner_phone }}</p>
              </div>
           </div>

           <p class="text-gray-400 text-sm mb-2">Scan via GPay, PhonePe, or Paytm</p>
           
           <div class="bg-black/30 p-2 rounded mb-6 flex justify-center items-center gap-2">
             <span class="text-[#5F9598] font-mono text-sm">{{ car.upi_id || 'UPI ID Unavailable' }}</span>
             <ion-icon name="copy-outline" class="text-gray-400 cursor-pointer hover:text-white" title="Copy UPI ID"></ion-icon>
           </div>
           
           <div class="border-t border-white/10 pt-6">
             <label class="block text-left text-xs text-gray-400 uppercase tracking-wider mb-2">Upload Payment Screenshot</label>
             
             <div class="relative">
               <input type="file" @change="onFileChange" accept="image/*" class="w-full bg-[#061E29] border border-white/10 rounded-lg p-3 text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-[#5F9598] file:text-[#061E29] hover:file:bg-white transition cursor-pointer">
             </div>

             <button 
               @click="handlePayment" 
               :disabled="processing || !selectedFile"
               class="w-full mt-6 bg-[#5F9598] hover:bg-white text-[#061E29] font-bold py-4 rounded-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed"
             >
               {{ processing ? 'Verifying...' : 'Submit Payment Proof' }}
             </button>
           </div>
        </div>

      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes bounceIn {
  0% { transform: scale(0.3); opacity: 0; }
  50% { transform: scale(1.05); opacity: 1; }
  70% { transform: scale(0.9); }
  100% { transform: scale(1); }
}
.animate-bounce-in {
  animation: bounceIn 0.6s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
}
</style>