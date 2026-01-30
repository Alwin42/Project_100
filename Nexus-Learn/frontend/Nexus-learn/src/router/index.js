import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Layouts
import DashboardLayout from '@/layouts/DashboardLayout.vue'

// Views
import LoginView from '../views/LoginView.vue'
import LandingView from '../views/LandingView.vue'
import DashboardView from '../views/DashboardView.vue' 
import RegisterView from '../views/RegisterView.vue'

// Forms
import EditProfileView from '../views/forms/EditProfileView.vue'
import AddSubjectView from '../views/forms/AddSubjectView.vue'
import AddExpenseView from '../views/forms/AddExpenseView.vue'
import AddTimetableView from '../views/forms/AddTimetableView.vue'
import AddReminderView from '../views/forms/AddReminderView.vue'
import AddActivityView from '../views/forms/AddActivityView.vue'
import AddNoteView from '../views/forms/AddNoteView.vue'

// Lists (Grid Views)
import NoteListView from '../views/lists/NoteListView.vue'
import ActivityListView from '../views/lists/ActivityListView.vue'
import ExpenseListView from '../views/lists/ExpenseListView.vue'
import TimetableListView from '../views/lists/TimetableListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Public Routes
    { path: '/', name: 'landing', component: LandingView },
    { path: '/login', name: 'login', component: LoginView },
    { path: '/register', name: 'register', component: RegisterView },
    
    // PROTECTED ROUTES (Wrapped in DashboardLayout)
    {
      path: '/dashboard',
      component: DashboardLayout, 
      meta: { requiresAuth: true },
      children: [
        // Main Dashboard (http://localhost:5173/dashboard)
        { path: '', name: 'dashboard', component: DashboardView }, 
        
        // List Views (Grids)
        // FIX: Removed leading slash '/' so these nest correctly under /dashboard
        { path: 'notes', name: 'notes-list', component: NoteListView }, 
        { path: 'profile', name: 'profile', component: EditProfileView },
        { path: 'activities', name: 'activities-list', component: ActivityListView }, // Fixed
        { path: 'expenses', name: 'expenses-list', component: ExpenseListView },     // Fixed
        { path: 'timetable', name: 'timetable-list', component: TimetableListView }, // Fixed

        // Forms
        { path: 'add-note', name: 'add-note', component: AddNoteView },
        { path: 'add-activity', name: 'add-activity', component: AddActivityView },
        { path: 'add-expense', name: 'add-expense', component: AddExpenseView },
        { path: 'add-timetable', name: 'add-timetable', component: AddTimetableView },
        { path: 'add-subject', name: 'add-subject', component: AddSubjectView },
        { path: 'add-reminder', name: 'add-reminder', component: AddReminderView },
      ]
    }
  ]
})

// Navigation Guard (Protect Dashboard)
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  
  // Redirect to login if not authenticated
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router