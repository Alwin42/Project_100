<script setup>
// NEXUS THEME COLORS
const colors = {
  green: '#22c55e',
  blue: '#3b82f6',
  purple: '#a855f7',
  pink: '#ec4899'
}

const getTransition = (i) => ({
  // 1. Initial State: Hidden and slightly lower
  initial: { 
    pathLength: 0, 
    opacity: 0, 
    scale: 0.8, 
    y: 20 
  },
  
  // 2. Enter State: Draw + Fade In + Start Floating
  enter: { 
    pathLength: 1, 
    opacity: 1, 
    scale: 1,
    y: [0, -15, 0], // Continuous Float Animation (Keyframes)
    transition: {
      // Drawing Animation (Smooth easeInOut)
      pathLength: { delay: i * 200, duration: 1500, ease: "easeInOut" },
      opacity: { delay: i * 200, duration: 800 },
      scale: { delay: i * 200, duration: 800, type: 'spring' },
      
      // Floating Animation (Infinite Loop)
      y: {
        duration: 3000, 
        repeat: Infinity, 
        ease: "easeInOut", 
        delay: i * 200 // Stagger the float so they don't move in sync
      }
    }
  },

  // 3. Hover State: Glow & Pop
  hovered: {
    scale: 1.2,
    strokeWidth: 12,
    filter: 'drop-shadow(0px 0px 15px currentColor)', // Glows with the shape's color
    transition: {
      type: 'spring',
      stiffness: 300,
      damping: 15
    }
  }
})

const shapeStyle = {
  strokeWidth: 8, // Slightly thinner for elegance
  strokeLinecap: "round",
  fill: "transparent",
  cursor: "pointer",
  transformBox: "fill-box",
  transformOrigin: "center"
}
</script>

<template>
  <svg
    viewBox="0 0 600 600"
    class="w-full max-w-[80vw] md:max-w-md mx-auto overflow-visible pointer-events-none"
  >
    <circle
      cx="100" cy="100" r="80"
      :stroke="colors.purple"
      :style="shapeStyle"
      class="pointer-events-auto text-purple-500"
      v-motion="getTransition(1)"
    />
    
    <line
      x1="220" y1="30" x2="360" y2="170"
      :stroke="colors.green"
      :style="shapeStyle"
      class="pointer-events-auto text-green-500"
      v-motion="getTransition(1.5)"
    />
    <line
      x1="220" y1="170" x2="360" y2="30"
      :stroke="colors.green"
      :style="shapeStyle"
      class="pointer-events-auto text-green-500"
      v-motion="getTransition(1.8)"
    />

    <rect
      width="140" height="140" x="410" y="30" rx="30"
      :stroke="colors.blue"
      :style="shapeStyle"
      class="pointer-events-auto text-blue-500"
      v-motion="getTransition(2)"
    />

    <circle
      cx="100" cy="300" r="80"
      :stroke="colors.blue"
      :style="shapeStyle"
      class="pointer-events-auto text-blue-500"
      v-motion="getTransition(2.5)"
    />

    <line
      x1="220" y1="230" x2="360" y2="370"
      :stroke="colors.pink"
      :style="shapeStyle"
      class="pointer-events-auto text-pink-500"
      v-motion="getTransition(3)"
    />
    <line
      x1="220" y1="370" x2="360" y2="230"
      :stroke="colors.pink"
      :style="shapeStyle"
      class="pointer-events-auto text-pink-500"
      v-motion="getTransition(3.3)"
    />

    <rect
      width="140" height="140" x="410" y="230" rx="30"
      :stroke="colors.green"
      :style="shapeStyle"
      class="pointer-events-auto text-green-500"
      v-motion="getTransition(3.8)"
    />

    <circle
      cx="100" cy="500" r="80"
      :stroke="colors.green"
      :style="shapeStyle"
      class="pointer-events-auto text-green-500"
      v-motion="getTransition(4.2)"
    />

    <line
      x1="220" y1="430" x2="360" y2="570"
      :stroke="colors.blue"
      :style="shapeStyle"
      class="pointer-events-auto text-blue-500"
      v-motion="getTransition(4.8)"
    />
    <line
      x1="220" y1="570" x2="360" y2="430"
      :stroke="colors.blue"
      :style="shapeStyle"
      class="pointer-events-auto text-blue-500"
      v-motion="getTransition(5.1)"
    />

    <rect
      width="140" height="140" x="410" y="430" rx="30"
      :stroke="colors.purple"
      :style="shapeStyle"
      class="pointer-events-auto text-purple-500"
      v-motion="getTransition(5.5)"
    />
  </svg>
</template>