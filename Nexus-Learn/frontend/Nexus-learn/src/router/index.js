import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import SubjectsView from '../views/SubjectsView.vue' 
import LandingView from '../views/LandingView.vue'
import EditProfileView from '../views/forms/EditProfileView.vue'
import AddSubjectView from '../views/forms/AddSubjectView.vue'
import AddExpenseView from '../views/forms/AddExpenseView.vue'
import AddTimetableView from '../views/forms/AddTimetableView.vue'
import AddReminderView from '../views/forms/AddReminderView.vue'
import AddActivityView from '../views/forms/AddActivityView.vue'
import AddNoteView from '../views/forms/AddNoteView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: LandingView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',  
      name: 'register',
      component: RegisterView
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: SubjectsView
    },
    {
      path: '/dashboard', // Moved HomeView here
      name: 'dashboard',
      component: HomeView,
      // Optional: Add a meta field to check auth later
      meta: { requiresAuth: true }
    },
    { path: '/profile/edit', name: 'edit-profile', component: EditProfileView },
    { path: '/subjects/add', name: 'add-subject', component: AddSubjectView },
    { path: '/expenses/add', name: 'add-expense', component: AddExpenseView },
    { path: '/timetable/add', name: 'add-timetable', component: AddTimetableView },
    { path: '/reminders/add', name: 'add-reminder', component: AddReminderView },
    { path: '/activities/add', name: 'add-activity', component: AddActivityView },
    { path: '/notes/add', name: 'add-note', component: AddNoteView },
  ]
})

export default router