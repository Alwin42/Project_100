<script setup>
import { useTime, useTransform, Motion } from 'motion-v'

const time = useTime()
const rotate = useTransform(
  time,
  [0, 10000], // Slower rotation (10s) for background
  [0, 360], 
  { clamp: false }
)

// --- STYLES ---

// 1. Tiny Boxes (Background particles)
const tinyBoxStyle = {
  width: '40px',
  height: '40px',
  backgroundColor: 'rgba(34, 197, 94, 0.2)', // Nexus Green (Low Opacity)
  borderRadius: '8px',
  rotate: useTransform(() => rotate.get() * 2), // 2x speed
}

// 2. Small Boxes (Mid layer)
const smallBoxStyle = {
  width: '80px',
  height: '80px',
  backgroundColor: 'rgba(59, 130, 246, 0.3)', // Blue (Low Opacity)
  borderRadius: '12px',
  rotate: useTransform(() => rotate.get() * 1.5), // 1.5x speed
}

// 3. Main Box (Center)
const boxStyle = {
  width: '120px',
  height: '120px',
  backgroundColor: 'rgba(255, 255, 255, 0.1)', // White (Glass)
  borderRadius: '20px',
  border: '1px solid rgba(255,255,255,0.2)',
  rotate,
}

const layer = {
  position: 'absolute',
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  pointerEvents: 'none', // Important: clicks pass through to buttons below
  overflow: 'hidden'
}

const boxContainer = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  flexWrap: 'wrap',
}
</script>

<template>
  <div class="absolute inset-0 overflow-hidden pointer-events-none opacity-60">
    
    <div :style="{ ...layer, filter: 'blur(8px)' }">
      <div :style="{ ...boxContainer, width: '120%', gap: '60px' }">
        <Motion v-for="n in 12" :key="'t'+n" :style="tinyBoxStyle" />
      </div>
    </div>

    <div :style="{ ...layer, filter: 'blur(4px)' }">
      <div :style="{ ...boxContainer, width: '80%', gap: '40px' }">
        <Motion v-for="n in 6" :key="'s'+n" :style="smallBoxStyle" />
      </div>
    </div>

    <div :style="layer">
      <Motion :style="boxStyle" />
    </div>

  </div>
</template>