<script setup>
import { ref, onMounted } from 'vue'
import { useTaskStore } from '@/stores/task'
import { useAuthStore } from '@/stores/auth'
import Navbar from '@/components/Navbar.vue' 
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Checkbox } from '@/components/ui/checkbox'
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'

const taskStore = useTaskStore()
const authStore = useAuthStore()
const newTaskTitle = ref('')

onMounted(() => {
  if (authStore.isAuthenticated) {
    taskStore.fetchTasks()
  }
})

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
  <div class="min-h-screen bg-nexus-main text-white">
    <main class="container mx-auto p-6 space-y-6">
      <div class="flex items-center justify-between border-b border-gray-800 pb-4">
        <div>
          <h1 class="text-3xl font-bold tracking-tight text-white">Dashboard</h1>
          <p class="text-gray-400">Welcome back to your workspace.</p>
        </div>
      </div>

      <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-7">
        
        <Card class="col-span-4 bg-nexus-card border-gray-800 text-white">
          <CardHeader>
            <CardTitle class="text-nexus-accent">Quick To-Do List</CardTitle>
          </CardHeader>
          <CardContent>
            
            <div class="flex w-full items-center space-x-2 mb-6">
              <Input 
                v-model="newTaskTitle" 
                type="text" 
                placeholder="Add a new task..." 
                class="bg-nexus-main border-gray-700 text-white focus:border-nexus-accent"
                @keyup.enter="handleAddTask"
              />
              <Button @click="handleAddTask" class="bg-nexus-accent hover:bg-nexus-dark text-black">
                Add
              </Button>
            </div>

            <div v-if="taskStore.loading" class="text-sm text-nexus-accent animate-pulse">Loading tasks...</div>
            
            <div v-else class="space-y-3">
              <div 
                v-for="task in taskStore.tasks" 
                :key="task.id" 
                class="flex items-center justify-between p-3 border border-gray-800 rounded-lg bg-nexus-main/50 hover:bg-nexus-main transition-colors"
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
                
                <Badge :variant="task.priority === 'High' ? 'destructive' : 'outline'" class="border-gray-600 text-gray-300">
                  {{ task.priority }}
                </Badge>
              </div>

              <div v-if="taskStore.tasks.length === 0" class="text-center text-gray-600 py-4">
                No tasks yet. Time to get productive!
              </div>
            </div>

          </CardContent>
        </Card>

        <Card class="col-span-3 bg-nexus-card border-gray-800 text-white">
          <CardHeader>
            <CardTitle class="text-nexus-accent">Notifications</CardTitle>
          </CardHeader>
          <CardContent>
            <p class="text-sm text-gray-500">No new notifications.</p>
          </CardContent>
        </Card>

      </div>
    </main>
  </div>
</template>