<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import { 
  User, Mail, Phone, MapPin, Calendar, Edit2, Camera, 
  CheckCircle, Star, Briefcase, Globe
} from 'lucide-vue-next'
import axios from 'axios'

const router = useRouter()

// Initialize with a loading state
const isLoading = ref(true)
const user = ref({
  name: '',
  email: '',
  phone: '',
  city_town: '',
  country: '',
  joinedDate: 'Recently',
  avatar: 'U',
  stats: {
    completedBookings: 0,
    totalSpent: 0,
    reviewsGiven: 0
  }
})

const isEditing = ref(false)
const editForm = ref({
  name: '',
  email: '',
  phone: '',
  city_town: '',
  country: ''
})

// Fetch real user data from backend on mount
onMounted(async () => {
  try {
    const token = localStorage.getItem('token')
    if (!token) {
      router.push('/auth')
      return
    }

    // Call the backend /api/users/me endpoint
    const response = await axios.get('http://localhost:8000/api/users/me', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    const data = response.data
    
    // Map backend data to frontend state
    user.value = {
      name: data.name,
      email: data.email,
      phone: data.phone || 'Not provided',
      city_town: data.city_town || 'Not provided',
      country: data.country || 'Not provided',
      joinedDate: data.date_of_join 
        ? new Date(data.date_of_join).toLocaleDateString('en-US', { year: 'numeric', month: 'long' }) 
        : 'Recently',
      avatar: data.name ? data.name.charAt(0).toUpperCase() : 'U',
      stats: {
        completedBookings: data.total_services_completed || 0,
        totalSpent: data.total_spent_on_services || 0,
        reviewsGiven: 0 // Can be updated later when reviews are implemented
      }
    }
    
    // Initialize edit form with real data
    editForm.value = {
      name: user.value.name,
      email: user.value.email,
      phone: user.value.phone === 'Not provided' ? '' : user.value.phone,
      city_town: user.value.city_town === 'Not provided' ? '' : user.value.city_town,
      country: user.value.country === 'Not provided' ? '' : user.value.country
    }
  } catch (error) {
    console.error('Failed to fetch user data:', error)
    // If token is invalid, redirect to login
    localStorage.removeItem('token')
    router.push('/auth')
  } finally {
    isLoading.value = false
  }
})

const toggleEdit = () => {
  if (isEditing.value) {
    // TODO: Add API call here to save changes to the backend (PUT /api/users/me)
    // For now, we just update the local state
    user.value.name = editForm.value.name
    user.value.phone = editForm.value.phone
    user.value.city_town = editForm.value.city_town
    user.value.country = editForm.value.country
    user.value.avatar = user.value.name.charAt(0).toUpperCase()
  }
  isEditing.value = !isEditing.value
}

const cancelEdit = () => {
  editForm.value = {
    name: user.value.name,
    email: user.value.email,
    phone: user.value.phone === 'Not provided' ? '' : user.value.phone,
    city_town: user.value.city_town === 'Not provided' ? '' : user.value.city_town,
    country: user.value.country === 'Not provided' ? '' : user.value.country
  }
  isEditing.value = false
}
</script>

<template>
  <div class="min-h-screen bg-gray-50/50 font-sans text-gray-900 antialiased">
    <Navbar />

    <main class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 md:py-12">
      
      <!-- Loading State -->
      <div v-if="isLoading" class="flex items-center justify-center min-h-[60vh]">
        <div class="text-primary font-semibold text-lg animate-pulse">Loading profile...</div>
      </div>

      <!-- Profile Content -->
      <div v-else>
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

                <!-- Email (Read-only) -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-lg bg-highlight/10 flex items-center justify-center flex-shrink-0">
                      <Mail class="w-5 h-5 text-secondary" />
                    </div>
                    <span class="text-gray-900 font-medium">{{ user.email }}</span>
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

                <!-- City/Town -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">City / Town</label>
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                      <MapPin class="w-5 h-5 text-primary" />
                    </div>
                    <input 
                      v-if="isEditing"
                      v-model="editForm.city_town"
                      type="text"
                      class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                    />
                    <span v-else class="text-gray-900 font-medium">{{ user.city_town }}</span>
                  </div>
                </div>

                <!-- Country -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Country</label>
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-lg bg-primary/10 flex items-center justify-center flex-shrink-0">
                      <Globe class="w-5 h-5 text-primary" />
                    </div>
                    <input 
                      v-if="isEditing"
                      v-model="editForm.country"
                      type="text"
                      class="flex-1 px-4 py-2.5 border border-gray-200 rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition"
                    />
                    <span v-else class="text-gray-900 font-medium">{{ user.country }}</span>
                  </div>
                </div>

                <!-- Cancel Button -->
                <div v-if="isEditing" class="pt-4 border-t border-gray-100 flex gap-3">
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
      </div>
    </main>
  </div>
</template>