<script setup>
import { Motion } from 'motion-v'
import { ref, onMounted, onBeforeUnmount } from 'vue'

const initialOrder = [
    "#ff0088",
    "#dd00ee",
    "#9911ff",
    "#0d63f8",
]

const order = ref([...initialOrder])
let intervalId = null

onMounted(() => {
    intervalId = window.setInterval(() => {
        order.value = shuffle(order.value)
    }, 1000)
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
    stiffness: 300,
}

const container = {
    listStyle: 'none',
    padding: '0px',
    margin: '0px',
    position: 'relative',
    display: 'flex',
    flexWrap: 'wrap',
    gap: '10px',
    width: '300px',
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
}

const itemStyle = {
    width: "100px",
    height: "100px",
    borderRadius: "10px",
    cursor: "pointer", // Cursor effect
    boxShadow: "0 10px 15px -3px rgba(0, 0, 0, 0.3)" // Added depth
}
</script>

<template>
    <ul :style="container">
        <Motion
            is="li"
            v-for="backgroundColor in order"
            :key="backgroundColor"
            layout
            :transition="spring"
            :style="{ ...itemStyle, backgroundColor }"
            
            :whileHover="{ 
                scale: 1.1, 
                rotate: 5, 
                zIndex: 10,
                boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.4)'
            }"
            :whileTap="{ scale: 0.95 }"
        />
    </ul>
</template>