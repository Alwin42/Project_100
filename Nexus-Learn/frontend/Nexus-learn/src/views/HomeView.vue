<script setup>
import { ref, onMounted, computed } from 'vue'
import { useTaskStore } from '@/stores/task'
import { useAuthStore } from '@/stores/auth'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { Card, CardHeader, CardTitle, CardContent, CardDescription } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Progress } from '@/components/ui/progress' 
import { 
  BellIcon, 
  ClockIcon, 
  FileTextIcon, 
  ReaderIcon, 
  PieChartIcon,
  DownloadIcon,
  LightningBoltIcon,
  ActivityLogIcon
} from '@radix-icons/vue'

const taskStore = useTaskStore()
const authStore = useAuthStore()
const newTaskTitle = ref('')

// --- MOCK DATA ---
const timetable = ref([
  { id: 1, subject: 'Data Structures', time: '09:00 AM - 10:00 AM', room: 'LB-102', status: 'Upcoming' },
  { id: 2, subject: 'Database Mgmt', time: '10:15 AM - 11:15 AM', room: 'LB-105', status: 'Upcoming' },
  { id: 3, subject: 'Web Development', time: '01:00 PM - 02:00 PM', room: 'Lab-2', status: 'Finished' },
])

const notifications = ref([
  { id: 1, title: 'Exam Schedule Out', message: 'Mid-term dates have been published.', time: '2h ago' },
  { id: 2, title: 'Assignment Due', message: 'Submit DBMS Project by Friday.', time: '5h ago' },
])

const recentFiles = ref([
  { id: 1, title: 'DBMS_Notes_Unit1.pdf', date: 'Jan 28, 2026', type: 'PDF' },
  { id: 2, title: 'Project_Proposal.docx', date: 'Jan 29, 2026', type: 'DOC' },
])

const expenses = ref({
  total: 4500.00,
  recent: [
    { category: 'Food', amount: 120 },
    { category: 'Transport', amount: 50 },
  ]
})

// New Mock Data for Progress Bar
const attendance = ref([
  { subject: 'Data Structures', percent: 85 },
  { subject: 'Database Mgmt', percent: 72 },
  { subject: 'Web Dev', percent: 94 },
])

// --- COMPUTED ---
const studentName = computed(() => authStore.user?.first_name || authStore.user?.username || 'Student')
const studentCourse = computed(() => authStore.user?.profile?.course || 'Computer Science')
const studentCollege = computed(() => authStore.user?.profile?.college || 'Nexus Institute')

const initials = computed(() => {
  const name = studentName.value
  return name ? name.charAt(0).toUpperCase() : 'S'
})

// --- LIFECYCLE ---
onMounted(() => {
  if (authStore.isAuthenticated) {
    taskStore.fetchTasks()
  }
})

// --- HANDLERS ---
const handleAddTask = async () => {
  if (!newTaskTitle.value.trim()) return
  await taskStore.addTask(newTaskTitle.value, 'Medium')
  newTaskTitle.value = '' 
}

const handleToggle = async (task) => {
  await taskStore.toggleTask(task.id, !task.is_done)
}
</script>

<template>
  <div class="min-h-screen bg-nexus-main bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-gray-900 via-nexus-main to-nexus-main text-white pb-10">
    
    <main class="container mx-auto p-6 space-y-8">
      
      <div 
        class="flex flex-col md:flex-row items-start md:items-center justify-between border-b border-gray-800/50 pb-6 gap-4"
        v-motion
        :initial="{ opacity: 0, y: -20 }"
        :enter="{ opacity: 1, y: 0, transition: { duration: 500 } }"
      >
        <div>
          <h1 class="text-4xl font-extrabold tracking-tight text-white drop-shadow-md">
            Dashboard
          </h1>
          <p class="text-gray-400 mt-2 text-lg">
            Welcome back, <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-emerald-400 font-bold">{{ studentName }}</span>
          </p>
        </div>
        
        <div class="flex items-center gap-4 bg-white/5 border border-white/10 px-5 py-3 rounded-xl backdrop-blur-md shadow-lg hover:border-nexus-accent/30 transition-colors">
          <Avatar class="h-12 w-12 border-2 border-nexus-accent/20">
            <AvatarImage src="" alt="Student" />
            <AvatarFallback class="bg-nexus-accent text-black font-bold text-lg">
              {{ initials }}
            </AvatarFallback>
          </Avatar>
          <div class="text-sm">
            <div class="text-white font-bold text-base">{{ studentCourse }}</div>
            <div class="text-nexus-accent/80 text-xs uppercase tracking-wider">{{ studentCollege }}</div>
          </div>
        </div>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        
        <Card 
          class="bg-black/40 backdrop-blur-md border-white/10 text-white col-span-1 lg:col-span-2 shadow-xl hover:shadow-nexus-accent/5 transition-all duration-300"
          v-motion
          :initial="{ opacity: 0, x: -20 }"
          :enter="{ opacity: 1, x: 0, transition: { duration: 500, delay: 100 } }"
        >
          <CardHeader class="flex flex-row items-center justify-between pb-2 border-b border-white/5">
            <div class="space-y-1">
              <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
                <ClockIcon class="h-5 w-5" /> Today's Schedule
              </CardTitle>
              <CardDescription class="text-gray-400">Upcoming classes and labs</CardDescription>
            </div>
            <Badge variant="outline" class="border-nexus-accent/50 text-nexus-accent bg-nexus-accent/10 px-3 py-1">Wednesday</Badge>
          </CardHeader>
          <CardContent class="pt-6">
            <div class="space-y-3">
              <div v-for="cls in timetable" :key="cls.id" class="group flex items-center justify-between p-4 rounded-xl bg-white/5 border border-white/5 hover:border-nexus-accent/30 transition-all">
                <div class="flex items-center gap-4">
                  <div class="text-sm font-bold text-gray-400 w-32 group-hover:text-white transition-colors">{{ cls.time }}</div>
                  <div>
                    <div class="font-bold text-white text-base">{{ cls.subject }}</div>
                    <div class="text-xs text-nexus-accent/70 flex items-center gap-1">
                      <LightningBoltIcon class="h-3 w-3" /> Room: {{ cls.room }}
                    </div>
                  </div>
                </div>
                <Badge :class="cls.status === 'Upcoming' ? 'bg-blue-600 hover:bg-blue-500' : 'bg-gray-700 hover:bg-gray-600'">
                  {{ cls.status }}
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card 
          class="bg-black/40 backdrop-blur-md border-white/10 text-white shadow-xl hover:shadow-nexus-accent/5 transition-all duration-300"
          v-motion
          :initial="{ opacity: 0, x: 20 }"
          :enter="{ opacity: 1, x: 0, transition: { duration: 500, delay: 200 } }"
        >
          <CardHeader class="border-b border-white/5">
            <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
              <BellIcon class="h-5 w-5" /> Notifications
            </CardTitle>
          </CardHeader>
          <CardContent class="pt-6">
            <div class="space-y-4">
              <div v-for="notif in notifications" :key="notif.id" class="flex items-start gap-3 pb-3 border-b border-white/5 last:border-0">
                <div class="h-2 w-2 mt-2 rounded-full bg-nexus-accent shrink-0 shadow-[0_0_8px_rgba(29,205,159,0.8)]"></div>
                <div>
                  <p class="text-sm font-semibold text-white">{{ notif.title }}</p>
                  <p class="text-xs text-gray-400 mt-0.5">{{ notif.message }}</p>
                  <p class="text-[10px] text-gray-600 mt-1 font-mono">{{ notif.time }}</p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-7">
        
        <Card 
          class="col-span-1 lg:col-span-4 bg-black/40 backdrop-blur-md border-white/10 text-white h-fit shadow-xl"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :enter="{ opacity: 1, y: 0, transition: { duration: 500, delay: 300 } }"
        >
          <CardHeader class="border-b border-white/5">
            <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
              <ReaderIcon class="h-5 w-5" /> Task Manager
            </CardTitle>
            <CardDescription class="text-gray-400">Stay organized and productive</CardDescription>
          </CardHeader>
          <CardContent class="pt-6">
            
            <div class="flex w-full items-center space-x-2 mb-6">
              <Input 
                v-model="newTaskTitle" 
                type="text" 
                placeholder="What needs to be done?" 
                class="bg-white/5 border-white/10 text-white focus:border-nexus-accent placeholder:text-gray-500 h-11"
                @keyup.enter="handleAddTask"
              />
              <Button @click="handleAddTask" class="bg-nexus-accent hover:bg-nexus-dark text-black font-bold h-11 px-6">
                Add
              </Button>
            </div>

            <div v-if="taskStore.loading" class="text-sm text-nexus-accent animate-pulse flex items-center gap-2">
              <ActivityLogIcon class="animate-spin" /> Syncing tasks...
            </div>
            
            <div v-else class="space-y-3">
              <div 
                v-for="task in taskStore.tasks" 
                :key="task.id" 
                class="group flex items-center justify-between p-3 border border-white/5 rounded-lg bg-white/5 hover:bg-white/10 transition-colors"
              >
                <div class="flex items-center space-x-3">
                  <Checkbox 
                    :checked="task.is_done" 
                    @update:checked="handleToggle(task)"
                    class="border-gray-500 data-[state=checked]:bg-nexus-accent data-[state=checked]:text-black"
                  />
                  <span :class="{'line-through text-gray-500': task.is_done, 'font-medium text-gray-200': !task.is_done}">
                    {{ task.title }}
                  </span>
                </div>
                <Badge :variant="task.priority === 'High' ? 'destructive' : 'secondary'" class="text-[10px] uppercase tracking-wider">
                  {{ task.priority }}
                </Badge>
              </div>
              
              <div v-if="taskStore.tasks.length === 0" class="text-center py-10 opacity-50">
                <ReaderIcon class="h-10 w-10 mx-auto mb-2 text-gray-600" />
                <p class="text-gray-400 text-sm">No pending tasks. Relax!</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <div class="col-span-1 lg:col-span-3 space-y-6">
          
          <Card 
            class="bg-black/40 backdrop-blur-md border-white/10 text-white shadow-xl"
            v-motion
            :initial="{ opacity: 0, x: 20 }"
            :enter="{ opacity: 1, x: 0, transition: { duration: 500, delay: 400 } }"
          >
            <CardHeader class="pb-2 border-b border-white/5">
              <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
                <ActivityLogIcon class="h-5 w-5" /> Attendance
              </CardTitle>
            </CardHeader>
            <CardContent class="pt-4 space-y-4">
              <div v-for="(sub, i) in attendance" :key="i" class="space-y-1">
                <div class="flex justify-between text-xs text-gray-300">
                  <span>{{ sub.subject }}</span>
                  <span :class="sub.percent < 75 ? 'text-red-400' : 'text-emerald-400'">{{ sub.percent }}%</span>
                </div>
                <Progress :model-value="sub.percent" class="h-2 bg-gray-800" />
              </div>
            </CardContent>
          </Card>

          <Card 
            class="bg-black/40 backdrop-blur-md border-white/10 text-white shadow-xl"
            v-motion
            :initial="{ opacity: 0, x: 20 }"
            :enter="{ opacity: 1, x: 0, transition: { duration: 500, delay: 500 } }"
          >
            <CardHeader class="pb-2 border-b border-white/5">
              <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
                <PieChartIcon class="h-5 w-5" /> Expenses
              </CardTitle>
            </CardHeader>
            <CardContent class="pt-4">
              <div class="flex items-baseline justify-between mb-4">
                <div class="text-sm text-gray-400">Total this month</div>
                <div class="text-2xl font-bold tracking-tight text-white">₹{{ expenses.total }}</div>
              </div>
              <div class="space-y-2">
                <div v-for="(exp, i) in expenses.recent" :key="i" class="flex justify-between text-sm p-2 bg-white/5 rounded border border-white/5">
                  <span class="text-gray-300">{{ exp.category }}</span>
                  <span class="text-white font-mono">-₹{{ exp.amount }}</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card 
            class="bg-black/40 backdrop-blur-md border-white/10 text-white shadow-xl"
            v-motion
            :initial="{ opacity: 0, x: 20 }"
            :enter="{ opacity: 1, x: 0, transition: { duration: 500, delay: 600 } }"
          >
            <CardHeader class="pb-2 border-b border-white/5">
              <CardTitle class="text-nexus-accent flex items-center gap-2 text-lg">
                <FileTextIcon class="h-5 w-5" /> Cloud Storage
              </CardTitle>
            </CardHeader>
            <CardContent class="pt-4">
              <div class="space-y-3">
                <div v-for="file in recentFiles" :key="file.id" class="group flex items-center justify-between p-2 hover:bg-white/5 rounded-lg cursor-pointer transition-colors border border-transparent hover:border-white/5">
                  <div class="flex items-center gap-3 overflow-hidden">
                    <div class="bg-nexus-accent/10 p-2 rounded text-nexus-accent group-hover:bg-nexus-accent group-hover:text-black transition-colors">
                      <FileTextIcon />
                    </div>
                    <div class="truncate">
                      <div class="text-sm font-medium text-white truncate w-32">{{ file.title }}</div>
                      <div class="text-[10px] text-gray-500">{{ file.date }}</div>
                    </div>
                  </div>
                  <Button variant="ghost" size="icon" class="text-gray-500 hover:text-nexus-accent hover:bg-transparent">
                    <DownloadIcon class="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>

        </div>
      </div>

    </main>
  </div>
</template>