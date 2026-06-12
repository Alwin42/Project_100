<template>
  <div class="min-h-screen bg-gray-50 font-sans pb-20">
    
    <Navbar />

    <main class="max-w-5xl mx-auto px-6 w-full pt-28 md:pt-32">
      
      <div class="mb-10 animate-in fade-in slide-in-from-bottom-4 duration-700">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-900 tracking-tight">Customer Dashboard</h1>
        <p class="text-gray-500 font-medium mt-1">Manage your account, get help, and share feedback.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-1 space-y-8">
          
          <div class="bg-white border border-gray-100 rounded-4xl p-6 shadow-sm hover:shadow-md transition-shadow duration-300">
            <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
              <UserIcon class="w-8 h-8 text-primary" />
            </div>
            <h2 class="text-sm font-bold text-gray-500 uppercase tracking-wider mb-1">Account Profile</h2>
            <p class="text-md font-bold text-gray-900 truncate" title="userEmail">{{ userEmail }}</p>
            <div class="mt-4 inline-flex items-center gap-1.5 px-3 py-1 bg-secondary/20 text-primary text-xs font-bold rounded-full">
              <span class="w-2 h-2 rounded-full bg-primary animate-pulse"></span>
              Active Customer
            </div>
          </div>

          <div class="bg-primary rounded-4xl p-6 text-white shadow-lg shadow-primary/20 relative overflow-hidden group">
            <div class="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full blur-2xl pointer-events-none group-hover:scale-150 transition-transform duration-700 -mr-10 -mt-10"></div>
            
            <div class="relative z-10">
              <div class="p-3 bg-white/20 w-fit rounded-2xl mb-4">
                <HeadphonesIcon class="w-6 h-6 text-white" />
              </div>
              <h2 class="text-lg font-bold text-white mb-2">Need immediate help?</h2>
              <p class="text-white/80 text-sm mb-4">Our support team is available 24/7 to assist you with orders and refunds.</p>
              
              <div class="bg-white/10 border border-white/20 rounded-2xl p-4 flex items-center gap-3 backdrop-blur-sm">
                <PhoneIcon class="w-5 h-5 text-accent-1" />
                <div>
                  <p class="text-xs text-white/70 font-medium">Toll-Free Helpline</p>
                  <p class="font-bold text-lg tracking-wide">1-800-STOCKUNDO</p>
                </div>
              </div>
            </div>
          </div>

        </div>

        <div class="lg:col-span-2 space-y-8">
          
          <div class="bg-white border border-gray-100 rounded-4xl p-6 md:p-8 shadow-sm transition-shadow duration-300">
            <div class="flex items-center gap-3 mb-6">
              <div class="p-2.5 bg-red-50 rounded-xl text-red-500">
                <LifeBuoyIcon class="w-6 h-6" />
              </div>
              <div>
                <h2 class="text-xl font-bold text-gray-900">Raise an Issue</h2>
                <p class="text-sm text-gray-500 font-medium">Having trouble with a vendor or an order?</p>
              </div>
            </div>

            <form @submit.prevent="submitTicket" class="space-y-4">
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Issue Type</label>
                <select 
                  v-model="ticketForm.type"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 appearance-none hover:border-gray-300 cursor-pointer"
                  required
                >
                  <option value="" disabled>Select the type of issue</option>
                  <option value="missing_item">Missing Item from Order</option>
                  <option value="quality">Poor Quality / Stale Items</option>
                  <option value="payment">Payment / Refund Issue</option>
                  <option value="vendor">Vendor Behavior</option>
                  <option value="other">Other App Issue</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Description</label>
                <textarea 
                  v-model="ticketForm.description"
                  rows="3"
                  placeholder="Please describe what went wrong..."
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 hover:border-gray-300 resize-none"
                  required
                ></textarea>
              </div>

              <div class="flex justify-end pt-2">
                <button 
                  type="submit"
                  :disabled="isTicketSubmitting"
                  class="bg-gray-900 text-white font-bold px-8 py-3.5 rounded-full hover:bg-gray-800 hover:-translate-y-0.5 active:scale-95 transition-all duration-300 disabled:opacity-70 flex items-center gap-2"
                >
                  <Loader2Icon v-if="isTicketSubmitting" class="w-5 h-5 animate-spin" />
                  <SendIcon v-else class="w-4 h-4" />
                  {{ isTicketSubmitting ? 'Submitting...' : 'Submit Ticket' }}
                </button>
              </div>
            </form>
          </div>

          <div class="bg-white border border-gray-100 rounded-4xl p-6 md:p-8 shadow-sm transition-shadow duration-300">
            <div class="flex items-center gap-3 mb-6">
              <div class="p-2.5 bg-accent-1/30 rounded-xl text-accent-2">
                <MessageSquareHeartIcon class="w-6 h-6" />
              </div>
              <div>
                <h2 class="text-xl font-bold text-gray-900">App Feedback</h2>
                <p class="text-sm text-gray-500 font-medium">Help us make StockUndo better for everyone.</p>
              </div>
            </div>

            <form @submit.prevent="submitFeedback" class="space-y-5">
              
              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Rate your experience</label>
                <div class="flex gap-2">
                  <StarIcon 
                    v-for="star in 5" 
                    :key="star"
                    @click="feedbackForm.rating = star"
                    @mouseenter="hoverRating = star"
                    @mouseleave="hoverRating = 0"
                    class="w-8 h-8 cursor-pointer transition-all duration-200 hover:scale-110"
                    :class="(hoverRating ? star <= hoverRating : star <= feedbackForm.rating) ? 'fill-accent-2 text-accent-2' : 'text-gray-200 fill-gray-100'"
                  />
                </div>
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-700 mb-2">Suggestions or Comments (Optional)</label>
                <textarea 
                  v-model="feedbackForm.comment"
                  rows="2"
                  placeholder="What do you love? What can we improve?"
                  class="w-full px-5 py-3.5 bg-gray-50 border border-gray-200 rounded-2xl focus:ring-4 focus:ring-primary/10 focus:border-primary outline-none transition-all font-medium text-gray-800 hover:border-gray-300 resize-none"
                ></textarea>
              </div>

              <div class="flex justify-end pt-2">
                <button 
                  type="submit"
                  :disabled="isFeedbackSubmitting || feedbackForm.rating === 0"
                  class="bg-primary text-white font-bold px-8 py-3.5 rounded-full hover:bg-primary/90 hover:-translate-y-0.5 active:scale-95 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
                >
                  <Loader2Icon v-if="isFeedbackSubmitting" class="w-5 h-5 animate-spin" />
                  {{ isFeedbackSubmitting ? 'Sending...' : 'Send Feedback' }}
                </button>
              </div>
            </form>
          </div>

        </div>
      </div>

    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from '../components/Navbar.vue'
import { 
  UserIcon, HeadphonesIcon, PhoneIcon, LifeBuoyIcon, 
  SendIcon, Loader2Icon, MessageSquareHeartIcon, StarIcon 
} from 'lucide-vue-next'

const userEmail = ref('Loading...')

// Form States
const isTicketSubmitting = ref(false)
const ticketForm = ref({
  type: '',
  description: ''
})

const isFeedbackSubmitting = ref(false)
const hoverRating = ref(0)
const feedbackForm = ref({
  rating: 0,
  comment: ''
})

// Fetch email from local storage on mount
onMounted(() => {
  const email = localStorage.getItem('userEmail')
  if (email) {
    userEmail.value = email
  } else {
    // Fallback if accessed without strict login state
    userEmail.value = 'guest@stockundo.com' 
  }
})

// Dummy function to simulate ticket submission
const submitTicket = () => {
  isTicketSubmitting.value = true
  
  // Simulate network delay
  setTimeout(() => {
    isTicketSubmitting.value = false
    alert(`Support Ticket Raised Successfully!\n\nIssue: ${ticketForm.value.type}\n\nOur team will contact you at ${userEmail.value} shortly.`)
    
    // Reset form
    ticketForm.value.type = ''
    ticketForm.value.description = ''
  }, 1000)
}

// Dummy function to simulate feedback submission
const submitFeedback = () => {
  isFeedbackSubmitting.value = true
  
  // Simulate network delay
  setTimeout(() => {
    isFeedbackSubmitting.value = false
    alert(`Thank you for rating us ${feedbackForm.value.rating} stars! We appreciate your feedback.`)
    
    // Reset form
    feedbackForm.value.rating = 0
    feedbackForm.value.comment = ''
  }, 1000)
}
</script>