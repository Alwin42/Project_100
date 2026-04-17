/** @type {import('tailwindcss').Config} */
export default {
  // This tells Tailwind to scan your index.html and all Vue/JS files in the src folder
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}