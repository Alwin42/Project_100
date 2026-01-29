import './assets/main.css'
import { MotionPlugin } from '@vueuse/motion'
import { createApp } from 'vue'
import { createPinia } from 'pinia' // Import Pinia for Auth
import App from './App.vue'
import router from './router'       // Import the Router

const app = createApp(App)

app.use(createPinia()) // Enable Pinia (Required for Login)
app.use(router)        // Enable Router (Required for Navigation)
app.use(MotionPlugin)
app.mount('#app')