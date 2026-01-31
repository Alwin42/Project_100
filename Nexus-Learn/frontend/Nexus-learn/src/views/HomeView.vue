<script setup>
import { ref, onMounted } from 'vue'
import { Motion } from 'motion-v'
import { RouterLink } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { 
  CalendarClock, 
  Wallet, 
  BookOpen, 
  Trophy, 
  Cloud,
  ArrowRight
} from 'lucide-vue-next'

const widgets = ref([])
const loading = ref(true)
const user = ref({ username: 'Student' })

// --- 1. ANIMATION VARIANTS (From your snippet) ---
const cardVariants = {
  offscreen: {
    y: 300,
    opacity: 0
  },
  onscreen: {
    y: 50,
    rotate: -10,
    opacity: 1,
    transition: {
      type: "spring",
      bounce: 0.4,
      duration: 0.8,
    },
  },
}

// Helper to generate gradients
const hue = (h) => `hsl(${h}, 100%, 50%)`
const getGradient = (hA, hB) => `linear-gradient(306deg, ${hue(hA)}, ${hue(hB)})`

// --- 2. FETCH DATA & BUILD WIDGETS ---
onMounted(async () => {
  try {
    // Fetch User
    const userRes = await api.get('user/')
    user.value = userRes.data

    // Fetch All Data in Parallel
    const [timeRes, expRes, noteRes, actRes, fileRes] = await Promise.allSettled([
      api.get('timetable/'),
      api.get('expenses/'),
      api.get('notes/'),
      api.get('activities/'),
      api.get('files/')
    ])

    // Process Data into Widgets
    const newWidgets = []

    // 1. Timetable Widget
    if (timeRes.status === 'fulfilled') {
      const classes = timeRes.value.data.slice(0, 3) // Get first 3
      newWidgets.push({
        id: 'timetable',
        title: 'Timetable',
        icon: CalendarClock,
        hueA: 200, hueB: 240, // Blueish
        items: classes.map(c => ({ 
          main: c.subject_name, 
          sub: `${c.day} • ${c.start_time.slice(0,5)}` 
        })),
        link: '/dashboard/timetable'
      })
    }

    // 2. Expenses Widget
    if (expRes.status === 'fulfilled') {
      const expenses = expRes.value.data.slice(0, 3)
      const total = expRes.value.data.reduce((sum, item) => sum + parseFloat(item.amount||0), 0)
      newWidgets.push({
        id: 'expenses',
        title: 'Expenses',
        icon: Wallet,
        hueA: 140, hueB: 170, // Greenish
        stat: `₹${total.toFixed(2)}`, // Show Total
        statLabel: 'Total Spent',
        items: expenses.map(e => ({ 
          main: e.category, 
          sub: `₹${parseFloat(e.amount).toFixed(2)}` 
        })),
        link: '/dashboard/expenses'
      })
    }

    // 3. Notes Widget
    if (noteRes.status === 'fulfilled') {
      const notes = noteRes.value.data.slice(0, 3)
      newWidgets.push({
        id: 'notes',
        title: 'Study Notes',
        icon: BookOpen,
        hueA: 260, hueB: 290, // Purple
        items: notes.map(n => ({ 
          main: n.title, 
          sub: n.subject_name || 'General'
        })),
        link: '/dashboard/notes'
      })
    }

    // 4. Activities Widget
    if (actRes.status === 'fulfilled') {
      const acts = actRes.value.data.slice(0, 3)
      newWidgets.push({
        id: 'activities',
        title: 'Activities',
        icon: Trophy,
        hueA: 20, hueB: 50, // Orange
        items: acts.map(a => ({ 
          main: a.name, 
          sub: a.activity_type 
        })),
        link: '/dashboard/activities'
      })
    }

    // 5. Cloud Widget
    if (fileRes.status === 'fulfilled') {
      const files = fileRes.value.data.slice(0, 3)
      newWidgets.push({
        id: 'cloud',
        title: 'Cloud Files',
        icon: Cloud,
        hueA: 320, hueB: 350, // Pink/Red
        items: files.map(f => ({ 
          main: f.title, 
          sub: new Date(f.uploaded_at).toLocaleDateString()
        })),
        link: '/dashboard/cloud'
      })
    }

    widgets.value = newWidgets

  } catch (e) {
    console.error("Home Load Error", e)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="min-h-screen bg-[#09090b] text-white overflow-x-hidden">
    <div class="container mx-auto px-6 py-20">
      
      <div class="text-center mb-20 space-y-4">
        <h1 class="text-5xl md:text-7xl font-black tracking-tighter">
          Welcome, <span class="text-transparent bg-clip-text bg-gradient-to-r from-nexus-accent to-blue-500">{{ user.username }}</span>
        </h1>
        <p class="text-xl text-gray-400">Your entire academic life, stacked.</p>
      </div>

      <div class="flex flex-col items-center gap-32 pb-40">
        
        <div v-if="loading" class="text-gray-500 animate-pulse">Loading widgets...</div>

        <Motion 
          v-else
          v-for="(widget, index) in widgets" 
          :key="widget.id"
          class="relative w-full max-w-[500px] h-[500px] flex justify-center"
          initial="offscreen"
          whileInView="onscreen"
          :viewport="{ amount: 0.5 }"
        >
           <div class="splash absolute inset-0" 
                :style="{ background: getGradient(widget.hueA, widget.hueB) }">
           </div>

           <Motion class="card-content" :variants="cardVariants">
              
              <div class="flex items-center gap-3 mb-6">
                <div class="p-3 rounded-xl bg-white/90 shadow-sm">
                  <component :is="widget.icon" class="w-6 h-6 text-black" />
                </div>
                <h3 class="text-2xl font-bold text-black">{{ widget.title }}</h3>
              </div>

              <div v-if="widget.stat" class="mb-6 pb-6 border-b border-gray-200/50">
                <div class="text-gray-500 text-xs font-bold uppercase tracking-wider">{{ widget.statLabel }}</div>
                <div class="text-4xl font-black text-black">{{ widget.stat }}</div>
              </div>

              <div class="space-y-3 flex-1">
                 <div v-for="(item, i) in widget.items" :key="i" class="flex items-center justify-between p-3 rounded-lg bg-white/50 hover:bg-white/80 transition-colors">
                    <div>
                      <div class="font-bold text-gray-900 text-sm line-clamp-1">{{ item.main }}</div>
                      <div class="text-xs text-gray-500">{{ item.sub }}</div>
                    </div>
                 </div>
                 
                 <div v-if="widget.items.length === 0" class="text-center text-gray-400 py-4 italic">
                    No items found
                 </div>
              </div>

              <div class="mt-6 pt-4 border-t border-gray-200/50 w-full">
                <RouterLink :to="widget.link">
                  <Button class="w-full bg-black text-white hover:bg-gray-800 rounded-xl h-12 font-bold">
                    Open {{ widget.title }} <ArrowRight class="w-4 h-4 ml-2" />
                  </Button>
                </RouterLink>
              </div>

           </Motion>
        </Motion>

      </div>

    </div>
  </div>
</template>

<style scoped>
/* The Splash Shape from your code */
.splash {
  clip-path: path("M 0 303.5 C 0 292.454 8.995 285.101 20 283.5 L 460 219.5 C 470.085 218.033 480 228.454 480 239.5 L 500 430 C 500 441.046 491.046 450 480 450 L 20 450 C 8.954 450 0 441.046 0 430 Z");
  opacity: 0.8;
  filter: blur(10px);
  transform: scale(1.1);
}

.card-content {
  width: 320px;
  min-height: 480px;
  background: #f5f5f5; /* Light Card Background */
  border-radius: 24px;
  padding: 30px;
  display: flex;
  flex-direction: column;
  box-shadow: 
    0 0 1px hsl(0deg 0% 0% / 0.075), 
    0 0 2px hsl(0deg 0% 0% / 0.075), 
    0 0 4px hsl(0deg 0% 0% / 0.075), 
    0 0 8px hsl(0deg 0% 0% / 0.075), 
    0 0 16px hsl(0deg 0% 0% / 0.075);
  transform-origin: 10% 60%;
  position: relative;
  z-index: 10;
}
</style>