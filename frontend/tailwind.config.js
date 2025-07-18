module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      animation: {
        // Optional: a slow spin
        'spin-slow': 'spin 6s linear infinite',
      }
    }
  },
  plugins: [],
}
