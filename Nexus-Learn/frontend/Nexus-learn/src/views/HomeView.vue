<script setup>
import { onMounted, computed } from 'vue'
import { useTaskStore } from '@/stores/task'
import { useAuthStore } from '@/stores/auth'
import { useDashboardStore } from '@/stores/dashboard' // <--- New Store
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { Card, CardHeader, CardTitle, CardContent, CardDescription } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { 
  BellIcon, ClockIcon, ReaderIcon, 
  PieChartIcon, LightningBoltIcon, ActivityLogIcon
} from '@radix-icons/vue'
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  navigationMenuTriggerStyle,
} from '@/components/ui/navigation-menu'
import { PlusIcon, Pencil1Icon } from '@radix-icons/vue'


const taskStore = useTaskStore()
const authStore = useAuthStore()
const dashboardStore = useDashboardStore()

const studentName = computed(() => authStore.user?.first_name || authStore.user?.username || 'Student')
const studentCourse = computed(() => authStore.user?.profile?.course || 'Student')
const initials = computed(() => studentName.value.charAt(0).toUpperCase())

// --- HELPER: Format Time (14:00:00 -> 02:00 PM) ---
const formatTime = (timeStr) => {
  if (!timeStr) return ''
  const [hours, minutes] = timeStr.split(':')
  const date = new Date()
  date.setHours(hours, minutes)
  return date.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })
}

// --- HELPER: Get Today's Day Name ---
const todayName = computed(() => {
  return new Date().toLocaleDateString('en-US', { weekday: 'long' })
})

onMounted(async () => {
  if (authStore.isAuthenticated) {
    // Fetch all real data in parallel
    await Promise.all([
      taskStore.fetchTasks(),
      dashboardStore.fetchTimetable(),
      dashboardStore.fetchReminders()
    ])
  }
})

const handleAddTask = async () => {
  // Your existing task logic (make sure to implement newTaskTitle ref)
  // For brevity, assuming you kept the ref from previous code
}
</script>
<template>
  <div class="min-h-screen bg-nexus-main bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-gray-900 via-nexus-main to-nexus-main text-white pb-10">
    <main class="container mx-auto p-6 space-y-8">
      
      <div class="flex flex-col md:flex-row items-start md:items-center justify-between border-b border-gray-800/50 pb-6 gap-4">
        <div>
          <h1 class="text-4xl font-extrabold tracking-tight text-white">Dashboard</h1>
          <p class="text-gray-400 mt-2">Welcome back, <span class="text-nexus-accent font-bold">{{ studentName }}</span></p>
        </div>

        <div class="flex items-center gap-4">
          
          <NavigationMenu>
            <NavigationMenuList>
              <NavigationMenuItem>
                <NavigationMenuTrigger class="bg-white/5 text-white hover:bg-white/10 hover:text-nexus-accent border border-white/10 data-[state=open]:bg-white/10">
                  <PlusIcon class="mr-2 h-4 w-4" /> Quick Actions
                </NavigationMenuTrigger>
                <NavigationMenuContent class="bg-nexus-card border-gray-800 text-white min-w-[200px] p-2 rounded-md shadow-xl backdrop-blur-xl">
                  <div class="grid gap-2 p-2">
                    <router-link to="/timetable/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Add Class to Timetable</div>
                      <p class="line-clamp-2 text-xs leading-snug text-gray-400">Schedule a new lecture or lab</p>
                    </router-link>
                    
                    <router-link to="/subjects/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Add Subject</div>
                    </router-link>

                    <router-link to="/expenses/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Add Expense</div>
                    </router-link>

                    <router-link to="/reminders/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Set Reminder</div>
                    </router-link>

                     <router-link to="/activities/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Log Activity</div>
                    </router-link>

                    <router-link to="/notes/add" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="text-sm font-medium leading-none">Upload Notes</div>
                    </router-link>

                    <div class="border-t border-gray-700 my-1"></div>

                    <router-link to="/profile/edit" class="block select-none space-y-1 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-nexus-accent/10 hover:text-nexus-accent">
                      <div class="flex items-center text-sm font-medium leading-none">
                        <Pencil1Icon class="mr-2 h-3.5 w-3.5"/> Edit Profile
                      </div>
                    </router-link>
                  </div>
                </NavigationMenuContent>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>

          <div class="flex items-center gap-4 bg-white/5 px-5 py-3 rounded-xl border border-white/10">
            <Avatar class="h-12 w-12 border-2 border-nexus-accent/20">
              <AvatarFallback class="bg-nexus-accent text-black font-bold">{{ initials }}</AvatarFallback>
            </Avatar>
            <div class="text-sm hidden sm:block">
              <div class="text-white font-bold">{{ studentCourse }}</div>
              <div class="text-nexus-accent/80 text-xs uppercase">Nexus Student</div>
            </div>
          </div>
        </div>
      </div>

      </main>
  </div>
</template>