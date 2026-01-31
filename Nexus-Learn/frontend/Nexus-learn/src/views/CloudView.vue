<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/services/api'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Cloud, Plus, File, Download, Trash2, HardDrive, UploadCloud } from 'lucide-vue-next'

// Import the new Animation
import AnimatedGrid from '@/components/AnimatedGrid.vue'

const router = useRouter()
const files = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await api.get('files/')
    files.value = res.data
  } catch (e) {
    console.error("Failed to load files", e)
  } finally {
    loading.value = false
  }
})

const deleteFile = async (id) => {
  if(!confirm("Delete this file permanently?")) return
  try {
    await api.delete(`files/${id}/`)
    files.value = files.value.filter(f => f.id !== id)
  } catch (e) {
    alert("Failed to delete file")
  }
}
</script>

<template>
  <div class="space-y-8 animate-in fade-in duration-500 max-w-7xl mx-auto p-4 md:p-8">
    
    <div class="relative overflow-hidden rounded-3xl bg-gradient-to-r from-blue-900/20 to-black p-8 border border-white/10 shadow-2xl backdrop-blur-3xl flex flex-col md:flex-row justify-between items-center gap-6">
      
      <div class="relative z-10 space-y-2">
        <div class="flex items-center gap-2 mb-2">
            <UploadCloud class="w-5 h-5 text-blue-400" />
            <span class="text-sm font-medium text-blue-400/80 tracking-wider uppercase">Cloud Storage</span>
        </div>
        <h1 class="text-3xl md:text-5xl font-extrabold text-white tracking-tight">
          My <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">Drive</span>
        </h1>
        <p class="text-gray-400 text-lg max-w-md">Securely store, manage, and access your academic resources from anywhere.</p>
        
        <div class="pt-4">
           <Button class="bg-blue-500 hover:bg-blue-600 text-white font-bold shadow-[0_0_20px_rgba(59,130,246,0.3)] hover:shadow-[0_0_30px_rgba(59,130,246,0.5)] transition-all" @click="router.push('/dashboard/add-file')">
            <Plus class="w-5 h-5 mr-2" /> Upload New File
          </Button>
        </div>
      </div>

      <div class="relative z-10 shrink-0">
         <AnimatedGrid />
      </div>

      <div class="absolute right-0 top-0 w-64 h-64 bg-blue-500/10 rounded-full blur-[100px] pointer-events-none"></div>
    </div>

    <div v-if="loading" class="text-center py-20 flex flex-col items-center gap-4">
      <div class="animate-spin w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full"></div>
      <span class="text-gray-500">Syncing with cloud...</span>
    </div>

    <div v-else-if="files.length === 0" class="flex flex-col items-center justify-center py-24 bg-white/5 rounded-3xl border border-white/10 border-dashed">
      <div class="p-6 bg-black/40 rounded-full mb-4 border border-white/5">
         <HardDrive class="w-12 h-12 text-gray-600" />
      </div>
      <h3 class="text-xl text-white font-bold">Storage is empty</h3>
      <p class="text-gray-400 mt-2 mb-6">Upload your first file to get started.</p>
      <Button variant="outline" class="border-white/10 text-gray-300 hover:text-white hover:bg-white/10" @click="router.push('/dashboard/add-file')">
        Upload File
      </Button>
    </div>

    <div v-else class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <Card v-for="file in files" :key="file.id" class="bg-black/40 border-white/10 text-white group hover:border-blue-500/40 hover:bg-white/[0.02] transition-all duration-300 overflow-hidden relative">
        
        <div class="absolute top-0 right-0 w-24 h-24 bg-blue-500/10 rounded-full blur-[40px] -translate-y-10 translate-x-10 group-hover:bg-blue-500/20 transition-all"></div>

        <CardContent class="p-5 flex flex-col justify-between h-full space-y-5 relative z-10">
          <div class="flex items-start justify-between">
            <div class="p-3.5 bg-gradient-to-br from-blue-500/20 to-transparent rounded-xl text-blue-400 border border-blue-500/10 group-hover:scale-110 transition-transform duration-300">
              <File class="w-8 h-8" />
            </div>
            <button @click="deleteFile(file.id)" class="text-gray-600 hover:text-red-400 p-2 hover:bg-red-500/10 rounded-lg transition-all" title="Delete File">
              <Trash2 class="w-4 h-4" />
            </button>
          </div>
          
          <div>
            <h4 class="font-bold text-lg truncate text-gray-100 group-hover:text-blue-200 transition-colors" :title="file.title">{{ file.title }}</h4>
            <div class="flex items-center gap-2 mt-2 text-xs text-gray-500">
               <span class="bg-white/5 px-2 py-0.5 rounded text-gray-400">{{ new Date(file.uploaded_at).toLocaleDateString() }}</span>
            </div>
          </div>

          <a :href="file.file" target="_blank">
            <Button variant="outline" class="w-full border-white/10 bg-white/5 text-gray-300 hover:bg-blue-500 hover:text-white hover:border-blue-500 transition-all shadow-sm">
              <Download class="w-4 h-4 mr-2" /> Download
            </Button>
          </a>
        </CardContent>
      </Card>
    </div>
  </div>
</template>