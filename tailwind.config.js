const path = require('path')

module.exports = (ctx) => ({
  content: [],
  theme: {
    extend: {},
  },
  plugins: [
    require('tailwindcss')(path.resolve(__dirname, 'tailwind.config.css')),
    require('autoprefixer'),
    process.env.DJANGO_PROD === 'production' && require('@fullhuman/postcss-purgecss')({
      content: [
        path.resolve(__dirname, 'templates/**/*.html')
      ],
      defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
    })
  ],
})
