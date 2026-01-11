/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        navy: '#061E29',       // Main Background
        'navy-light': '#0B2B38', // Cards / Secondary BG
        teal: '#5F9598',       // Accents / Borders
        blue: '#1D546D',       // Primary Buttons
        white: '#F3F4F4',      // Text
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Clean, modern font
      }
    },
  },
  plugins: [],
}