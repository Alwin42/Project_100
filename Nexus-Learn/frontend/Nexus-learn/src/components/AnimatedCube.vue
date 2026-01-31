<script setup>
import { useAnimationFrame } from "motion-v"
import { ref } from "vue"

const cubeRef = ref(null)

useAnimationFrame((t) => {
    if (!cubeRef.value) return

    const rotate = Math.sin(t / 10000) * 200
    const y = (1 + Math.sin(t / 1000)) * -20 // Reduced movement slightly for header
    cubeRef.value.style.transform = `translateY(${y}px) rotateX(${rotate}deg) rotateY(${rotate}deg)`
})
</script>

<template>
    <div class="cube-container">
        <div class="cube" ref="cubeRef">
            <div class="side front" />
            <div class="side left" />
            <div class="side right" />
            <div class="side top" />
            <div class="side bottom" />
            <div class="side back" />
        </div>
    </div>
</template>

<style scoped>
.cube-container {
    perspective: 800px;
    width: 200px;
    height: 200px;
    /* Center in parent */
    display: flex;
    align-items: center;
    justify-content: center;
}

.cube {
    width: 100px; /* Smaller size for UI decoration */
    height: 100px;
    position: relative;
    transform-style: preserve-3d;
}

.side {
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0.3; /* Glass effect */
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 0 20px rgba(34, 197, 94, 0.2); /* Nexus Green Glow */
}

/* NEXUS THEME COLORS */
.front  { transform: rotateY(0deg) translateZ(50px); background: rgba(34, 197, 94, 0.4); } /* Green */
.right  { transform: rotateY(90deg) translateZ(50px); background: rgba(59, 130, 246, 0.4); } /* Blue */
.back   { transform: rotateY(180deg) translateZ(50px); background: rgba(168, 85, 247, 0.4); } /* Purple */
.left   { transform: rotateY(-90deg) translateZ(50px); background: rgba(236, 72, 153, 0.4); } /* Pink */
.top    { transform: rotateX(90deg) translateZ(50px); background: rgba(34, 197, 94, 0.2); }
.bottom { transform: rotateX(-90deg) translateZ(50px); background: rgba(59, 130, 246, 0.2); }
</style>