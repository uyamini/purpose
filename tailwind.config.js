module.exports = {
  purge: [
    './templates/**/*.html',
    './main_app/templates/**/*.html',
    './theme/static/src/**/*.css',
  ],
  darkMode: false,
  theme: {
    extend: {
      colors: {
        indigo: {
           50: '#edf2ff',
           100: '#dbe4ff',
           200: '#bac8ff',
           300: '#91a7ff',
           400: '#748ffc',
           500: '#5c7cfa',
           600: '#4c6ef5',
           700: '#4263eb',
           800: '#3b5bdb',
           900: '#364fc7',
         },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
