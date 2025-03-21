/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [

    "./templates/**/*.html", // Templates at the project level
    "./**/templates/**/*.html", // Templates inside apps
    './templates/**/*.html',
    './static/**/*.css'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

module.exports = {
  theme: {
    extend: {
      animation: {
        'fade-scale': 'fadeScale 3s ease-in-out infinite',
      },
      keyframes: {
        fadeScale: {
          '0%': { opacity: 0, transform: 'scale(0.95)' },
          '50%': { opacity: 1, transform: 'scale(1)' },
          '100%': { opacity: 0, transform: 'scale(0.95)' },
        },
      },
    },
  },
  plugins: [],
}
module.exports = {
  darkMode: "class", // Enables dark mode using a class
  theme: {
    extend: {},
  },
  plugins: [],
};
module.exports = {
  theme: {
    extend: {
      writingMode: {
        'vertical-rl': 'vertical-rl',
        'vertical-lr': 'vertical-lr',
      }
    }
  }
}