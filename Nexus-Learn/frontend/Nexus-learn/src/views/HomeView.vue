<script setup>
import { ref, onMounted } from 'vue'
import { useTaskStore } from '@/stores/task'
import { useAuthStore } from '@/stores/auth' // Assuming you have this
import Navbar from '@/components/Navbar.vue' // Adjust if your navbar is elsewhere
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

// 1. Initialize Stores
const taskStore = useTaskStore()
const authStore = useAuthStore()

// 2. Local State
const newTaskTitle = ref('')

// 3. Fetch Data on Load
onMounted(() => {
  if (authStore.isAuthenticated) {
    taskStore.fetchTasks()
  }
})

// 4. Handle Adding a Task
const handleAddTask = async () => {
  if (!newTaskTitle.value.trim()) return
  
  await taskStore.addTask(newTaskTitle.value, 'Medium') // Default to Medium priority
  newTaskTitle.value = '' // Clear input
}

// 5. Handle Toggling Completion
const handleToggle = async (task) => {
  await taskStore.toggleTask(task.id, !task.is_done)
}
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    

    <main class="container mx-auto p-6 space-y-6">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-3xl font-bold tracking-tight">Dashboard</h1>
          <p class="text-muted-foreground">Welcome back to Nexus Learn.</p>
        </div>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-7">
        
        <Card class="col-span-4">
          <CardHeader>
            <CardTitle>Quick To-Do List</CardTitle>
          </CardHeader>
          <CardContent>
            
            <div class="flex w-full items-center space-x-2 mb-6">
              <Input 
                v-model="newTaskTitle" 
                type="text" 
                placeholder="Add a new task..." 
                @keyup.enter="handleAddTask"
              />
              <Button @click="handleAddTask">Add</Button>
            </div>

            <div v-if="taskStore.loading" class="text-sm text-gray-500">Loading tasks...</div>
            
            <div v-else class="space-y-4">
              <div 
                v-for="task in taskStore.tasks" 
                :key="task.id" 
                class="flex items-center justify-between p-3 border rounded-lg bg-white shadow-sm"
              >
                <div class="flex items-center space-x-3">
                  <Checkbox 
                    :checked="task.is_done" 
                    @update:checked="handleToggle(task)"
                  />
                  <span :class="{'line-through text-gray-400': task.is_done, 'font-medium': true}">
                    {{ task.title }}
                  </span>
                </div>
                
                <Badge :variant="task.priority === 'High' ? 'destructive' : 'secondary'">
                  {{ task.priority }}
                </Badge>
              </div>

              <div v-if="taskStore.tasks.length === 0" class="text-center text-gray-500 py-4">
                No tasks yet. Add one above!
              </div>
            </div>

          </CardContent>
        </Card>

        <Card class="col-span-3">
          <CardHeader>
            <CardTitle>Notifications</CardTitle>
          </CardHeader>
          <CardContent>
            <p class="text-sm text-muted-foreground">No new notifications.</p>
          </CardContent>
        </Card>

      </div>
    </main>
  </div>
</template>