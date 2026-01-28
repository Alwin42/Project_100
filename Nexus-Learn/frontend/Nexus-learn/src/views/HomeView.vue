<template>
  <div class="p-6 space-y-6 bg-slate-50 min-h-screen">
    
    <div class="flex items-center justify-between mb-8">
      <div>
        <h1 class="text-3xl font-bold tracking-tight text-slate-900">Dashboard</h1>
        <p class="text-slate-500">Welcome back! Here is your daily overview.</p>
      </div>
      <Button variant="default">Add New Task</Button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-6">
      
      <Card class="lg:col-span-4 shadow-sm">
        <CardHeader>
          <CardTitle class="flex items-center gap-2">
            📝 Quick To-Do
          </CardTitle>
          <CardDescription>Your priority tasks for today</CardDescription>
        </CardHeader>
        <CardContent>
          <div class="space-y-4">
            <div v-for="task in todos" :key="task.id" class="flex items-start space-x-3 items-center">
              <Checkbox :id="'task-' + task.id" :checked="task.done" />
              <div class="grid gap-1.5 leading-none">
                <label :for="'task-' + task.id" class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70">
                  {{ task.title }}
                </label>
                <p v-if="task.priority === 'High'" class="text-xs text-red-500 font-semibold">High Priority</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card class="lg:col-span-8 shadow-sm">
        <CardHeader>
          <CardTitle>📅 Today's Timetable</CardTitle>
          <CardDescription>Tuesday, Jan 30</CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead class="w-[100px]">Time</TableHead>
                <TableHead>Subject</TableHead>
                <TableHead>Room</TableHead>
                <TableHead class="text-right">Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              <TableRow v-for="slot in timetable" :key="slot.id">
                <TableCell class="font-medium">{{ slot.time }}</TableCell>
                <TableCell>{{ slot.subject }}</TableCell>
                <TableCell>{{ slot.room }}</TableCell>
                <TableCell class="text-right">
                  <Badge variant="outline" :class="slot.isNext ? 'bg-blue-100 text-blue-800 border-blue-200' : ''">
                    {{ slot.isNext ? 'Next Class' : 'Scheduled' }}
                  </Badge>
                </TableCell>
              </TableRow>
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      <Card class="lg:col-span-6 shadow-sm">
        <CardHeader>
          <CardTitle>⏰ Reminders</CardTitle>
        </CardHeader>
        <CardContent>
          <div class="space-y-4">
            <div v-for="reminder in reminders" :key="reminder.id" class="flex items-center justify-between p-3 border rounded-lg bg-white">
              <div class="space-y-1">
                <p class="text-sm font-medium leading-none">{{ reminder.desc }}</p>
                <p class="text-xs text-slate-500">{{ reminder.date }}</p>
              </div>
              <Badge variant="secondary">Upcoming</Badge>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card class="lg:col-span-6 shadow-sm">
        <CardHeader>
          <CardTitle>🔔 Notifications</CardTitle>
        </CardHeader>
        <CardContent>
          <ScrollArea class="h-[200px] w-full rounded-md border p-4">
            <div v-for="notif in notifications" :key="notif.id" class="mb-4 grid grid-cols-[25px_1fr] items-start last:mb-0 last:pb-0">
              <span class="flex h-2 w-2 translate-y-1 rounded-full bg-sky-500" />
              <div class="space-y-1">
                <p class="text-sm font-medium leading-none">{{ notif.title }}</p>
                <p class="text-sm text-slate-500">{{ notif.text }}</p>
              </div>
            </div>
          </ScrollArea>
        </CardContent>
      </Card>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// Shadcn Components
import { Button } from '@/components/ui/button'
import { Checkbox } from '@/components/ui/checkbox'
import { Badge } from '@/components/ui/badge'
import { ScrollArea } from '@/components/ui/scroll-area'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

// --- DUMMY DATA ---
const todos = ref([
  { id: 1, title: 'Submit AI Assignment', done: false, priority: 'High' },
  { id: 2, title: 'Read Chapter 4 of OS', done: true, priority: 'Low' },
  { id: 3, title: 'Register for Hackathon', done: false, priority: 'Medium' },
])

const reminders = ref([
  { id: 1, date: 'Tomorrow, 10:00 AM', desc: 'Database Lab Exam' },
  { id: 2, date: 'Jan 30, 5:00 PM', desc: 'Project Submission Deadline' },
])

const notifications = ref([
  { id: 1, title: 'New Assignment', text: 'Uploaded in Cloud Computing module.' },
  { id: 2, title: 'Library Alert', text: 'You have a fine due: ₹50' },
  { id: 3, title: 'Event', text: 'Guest lecture on Vue.js tomorrow at 2 PM.' },
  { id: 4, title: 'System', text: 'Password changed successfully.' },
])

const timetable = ref([
  { id: 1, time: '09:00 - 10:00', subject: 'Data Structures', room: 'LH-101', isNext: false },
  { id: 2, time: '10:00 - 11:00', subject: 'Operating Systems', room: 'LH-102', isNext: true },
  { id: 3, time: '11:15 - 12:15', subject: 'Python Lab', room: 'Lab-3', isNext: false },
])
</script>