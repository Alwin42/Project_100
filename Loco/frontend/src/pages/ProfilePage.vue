<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { 
  User, Mail, Phone, MapPin, Calendar, Edit2, Camera, 
  CheckCircle, Star, Briefcase
} from 'lucide-vue-next'

// Dummy user data (in a real app, this comes from your auth store/backend)
const user = ref({
  name: 'Alwin',
  email: 'alwin@example.com',
  phone: '+1 (555) 123-4567',
  location: 'San Francisco, CA',
  joinedDate: 'October 2023',
  avatar: 'A',
  stats: {
    completedBookings: 14,
    totalSpent: 1240,
    reviewsGiven: 12
  }
})

const isEditing = ref(false)

const editForm = ref({
  name: user.value.name,
  email: user.value.email,
  phone: user.value.phone,
  location: user.value.location
})

const toggleEdit = () => {
  isEditing.value = !isEditing.value
  if (!isEditing.value) {
    // Save changes (in real app, send to backend)
    user.value.name = editForm.value.name
    user.value.email = editForm.value.email
    user.value.phone = editForm.value.phone
    user.value.location = editForm.value.location
  }
}

const cancelEdit = () => {
  editForm.value = {
    name: user.value.name,
    email: user.value.email,
    phone: user.value.phone,
    location: user.value.location
  }
  isEditing.value = false
}
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- Profile Header -->
      <div class="bg-white border border-gray-100 rounded-2xl overflow-hidden mb-6">
        <div class="h-32 bg-gradient-to-r from-primary to-secondary"></div>
        <div class="px-6 pb-6">
          <div class="flex flex-col sm:flex-row sm:items-end sm:justify-between -mt-16 gap-4">
            <!-- Avatar -->
            <div class="relative">
              <div class="w-32 h-32 rounded-full bg-white border-4 border-white shadow-lg flex items-center justify-center text-5xl font-bold text-primary">
                {{ user.avatar }}
              </div>
              <button class="absolute bottom-2 right-2 w-10 h-10 bg-highlight rounded-full flex items-center justify-center text-white hover:opacity-90 transition shadow-md">
                <Camera class="w-5 h-5" />
              </button>
            </div>

            <!-- Edit Button -->
            <button 
              @click="toggleEdit"
              class="flex items-center gap-2 px-5 py-2.5 bg-primary text-white font-semibold rounded-xl hover:bg-primary/90 transition shadow-sm"
            >
              <Edit2 class="w-4 h-4" />
              {{ isEditing ? 'Save Changes' : 'Edit Profile' }}
            </button>
          </div>
        </div>
      </div>

      <div class="grid md:grid-cols-3 gap-6">
        
        <!-- Left Column: User Info -->
        <div class="md:col-span-2">
          <div class="bg-white border border-gray-100 rounded-2xl p-6">
            <h2 class="text-xl font-bold text-gray-900 mb-6">Personal Information</h2>
            
            <div class="space-y-5">
              <!-- Name -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                    <User class="w-5 h-5 text-primary" />
                  </div>
                  <input 
                    v-if="isEditing"
                    v-model="editForm.name"
                    type="text"
                    class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                  />
                  <span v-else class="text-gray-900 font-medium">{{ user.name }}</span>
                </div>
              </div>

              <!-- Email -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg bg-highlight/10 flex items-center justify-center flex-shrink-0">
                    <Mail class="w-5 h-5 text-secondary" />
                  </div>
                  <input 
                    v-if="isEditing"
                    v-model="editForm.email"
                    type="email"
                    class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                  />
                  <span v-else class="text-gray-900 font-medium">{{ user.email }}</span>
                </div>
              </div>

              <!-- Phone -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg bg-accent/20 flex items-center justify-center flex-shrink-0">
                    <Phone class="w-5 h-5 text-secondary" />
                  </div>
                  <input 
                    v-if="isEditing"
                    v-model="editForm.phone"
                    type="tel"
                    class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                  />
                  <span v-else class="text-gray-900 font-medium">{{ user.phone }}</span>
                </div>
              </div>

              <!-- Location -->
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Location</label>
                <div class="flex items-center gap-3">
                  <div class="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                    <MapPin class="w-5 h-5 text-primary" />
                  </div>
                  <input 
                    v-if="isEditing"
                    v-model="editForm.location"
                    type="text"
                    class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                  />
                  <span v-else class="text-gray-900 font-medium">{{ user.location }}</span>
                </div>
              </div>

              <!-- Cancel Button -->
              <div v-if="isEditing" class="pt-4 border-t border-gray-100">
                <button 
                  @click="cancelEdit"
                  class="px-5 py-2.5 text-gray-700 font-semibold border border-gray-200 rounded-xl hover:bg-gray-50 transition"
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Stats -->
        <div class="space-y-6">
          
          <!-- Account Stats -->
          <div class="bg-white border border-gray-100 rounded-2xl p-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4">Account Stats</h3>
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-9 h-9 rounded-lg bg-highlight/10 flex items-center justify-center">
                    <CheckCircle class="w-4 h-4 text-secondary" />
                  </div>
                  <span class="text-sm text-gray-600">Completed</span>
                </div>
                <span class="text-lg font-bold text-gray-900">{{ user.stats.completedBookings }}</span>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-9 h-9 rounded-lg bg-primary/10 flex items-center justify-center">
                    <Briefcase class="w-4 h-4 text-primary" />
                  </div>
                  <span class="text-sm text-gray-600">Total Spent</span>
                </div>
                <span class="text-lg font-bold text-gray-900">${{ user.stats.totalSpent }}</span>
              </div>

              <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-9 h-9 rounded-lg bg-red-50 flex items-center justify-center">
                    <Star class="w-4 h-4 text-red-500" />
                  </div>
                  <span class="text-sm text-gray-600">Reviews</span>
                </div>
                <span class="text-lg font-bold text-gray-900">{{ user.stats.reviewsGiven }}</span>
              </div>
            </div>
          </div>

          <!-- Member Since -->
          <div class="bg-white border border-gray-100 rounded-2xl p-6">
            <div class="flex items-center gap-3 mb-3">
              <Calendar class="w-5 h-5 text-gray-400" />
              <span class="text-sm text-gray-500">Member since</span>
            </div>
            <p class="text-lg font-bold text-gray-900">{{ user.joinedDate }}</p>
          </div>

        </div>
      </div>

    </main>
  </div>
</template>