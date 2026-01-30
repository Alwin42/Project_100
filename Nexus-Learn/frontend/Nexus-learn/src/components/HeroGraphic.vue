<script setup>
// Helper function to generate the animation variants based on index 'i'
const getTransition = (i) => ({
  initial: { pathLength: 0, opacity: 0, scale: 1 },
  enter: { 
    pathLength: 1, 
    opacity: 1,
    scale: 1,
    transition: {
      pathLength: { delay: i * 500, type: 'spring', duration: 1500, bounce: 0 },
      opacity: { delay: i * 500, duration: 10 }
    }
  },
  // --- NEW: Interactive Hover State ---
  hovered: {
    scale: 1.15,      // Grow slightly
    strokeWidth: 15,  // Make lines thicker
    filter: 'drop-shadow(0px 0px 10px rgba(255, 255, 255, 0.5))', // Add Glow
    transition: {
      type: 'spring',
      stiffness: 400,
      damping: 10
    }
  }
})

// Common styles for the shapes
const shapeStyle = {
  strokeWidth: 10,
  strokeLinecap: "round",
  fill: "transparent",
  cursor: "pointer" // Changes mouse to Hand icon
}
</script>

<template>
  <svg
    viewBox="0 0 600 600"
    class="w-full max-w-[80vw] md:max-w-md mx-auto overflow-visible pointer-events-none"
  >
    <circle
      cx="100" cy="100" r="80"
      stroke="#ff0088"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(1)"
    />
    
    <line
      x1="220" y1="30" x2="360" y2="170"
      stroke="#4ff0b7"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(2)"
    />
    <line
      x1="220" y1="170" x2="360" y2="30"
      stroke="#4ff0b7"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(2.5)"
    />

    <rect
      width="140" height="140" x="410" y="30" rx="20"
      stroke="#0d63f8"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(3)"
    />

    <circle
      cx="100" cy="300" r="80"
      stroke="#0d63f8"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(2)"
    />

    <line
      x1="220" y1="230" x2="360" y2="370"
      stroke="#ff0088"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(3)"
    />
    <line
      x1="220" y1="370" x2="360" y2="230"
      stroke="#ff0088"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(3.5)"
    />

    <rect
      width="140" height="140" x="410" y="230" rx="20"
      stroke="#4ff0b7"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(4)"
    />

    <circle
      cx="100" cy="500" r="80"
      stroke="#4ff0b7"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(3)"
    />

    <line
      x1="220" y1="430" x2="360" y2="570"
      stroke="#0d63f8"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(4)"
    />
    <line
      x1="220" y1="570" x2="360" y2="430"
      stroke="#0d63f8"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(4.5)"
    />

    <rect
      width="140" height="140" x="410" y="430" rx="20"
      stroke="#ff0088"
      :style="shapeStyle"
      class="pointer-events-auto"
      v-motion="getTransition(5)"
    />
  </svg>
</template>