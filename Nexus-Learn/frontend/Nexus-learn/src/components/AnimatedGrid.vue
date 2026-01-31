<script setup>
import { Motion } from 'motion-v'
import { ref, onMounted, onBeforeUnmount } from 'vue'

// Nexus Theme Colors (Vibrant)
const initialOrder = [
    "#22c55e", // Green
    "#3b82f6", // Blue
    "#a855f7", // Purple
    "#ec4899", // Pink
    "#06b6d4", // Cyan
    "#f59e0b", // Amber
]

const order = ref([...initialOrder])
let intervalId = null

onMounted(() => {
    intervalId = window.setInterval(() => {
        order.value = shuffle(order.value)
    }, 2000)
})

onBeforeUnmount(() => {
    if (intervalId !== null) clearInterval(intervalId)
})

function shuffle(array) {
    return [...array].sort(() => Math.random() - 0.5)
}

const spring = {
    type: 'spring',
    damping: 20,
    stiffness: 150,
}

const container = {
    position: 'relative',
    width: '180px',
    height: '110px',
    listStyle: 'none',
    padding: 0,
    margin: 0,
    // Ensure hovers don't get clipped
    overflow: 'visible' 
}

// GLASSMORPHISM STYLE 
const itemStyle = {
    position: 'absolute',
    borderRadius: '50%',
    
    // Glass Borders & Background
    border: "1px solid rgba(255, 255, 255, 0.4)",
    backdropFilter: "blur(12px)", 
    
    // Depth: Inner highlight + Drop shadow
    boxShadow: `
        inset 0 4px 10px rgba(255, 255, 255, 0.4), 
        inset 0 -4px 10px rgba(0, 0, 0, 0.2),
        0 8px 20px rgba(0, 0, 0, 0.3)
    `,
    
    cursor: 'pointer'
}

// Cloud Shape Positions
const positions = [
    { top: '0px',  left: '30px', width: '60px', height: '60px' }, // Top Left
    { top: '10px', left: '80px', width: '55px', height: '55px' }, // Top Right
    { top: '45px', left: '0px',  width: '65px', height: '65px' }, // Bottom Left
    { top: '50px', left: '55px', width: '60px', height: '60px' }, // Bottom Middle
    { top: '45px', left: '105px', width: '65px', height: '65px' }, // Bottom Right
    { top: '65px', left: '155px', width: '40px', height: '40px' }, // Small Tail
]
</script>

<template>
    <div :style="container">
        <Motion
            v-for="(pos, index) in positions"
            :key="index"
            :initial="false"
            
            :animate="{ 
                backgroundColor: order[index] 
            }" 
            
            :whileHover="{ 
                scale: 1.2, 
                zIndex: 20,
                boxShadow: '0 0 25px ' + order[index], // Colored glow on hover
                border: '2px solid rgba(255,255,255,0.8)'
            }"
            
            :transition="spring"
            :style="{ ...itemStyle, ...pos }"
        />
    </div>
</template>