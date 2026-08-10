/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'gcp-dark':      '#0a2631',
        'gcp-blue':      '#317bff',
        'gcp-blue-dark': '#1a56cc',
        'gcp-light':     '#f0f5fa',
        'gcp-muted':     '#8a9bb0',
        'gcp-gray':      '#f5f7fa',
        'gcp-border':    '#e2eaf4',
      },
      fontFamily: {
        sans: ['var(--font-poppins)', 'Raleway', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
      maxWidth: {
        'container': '1380px',
      },
      boxShadow: {
        'gcp': '0 4px 24px rgba(10, 38, 49, 0.12)',
        'gcp-lg': '0 12px 48px rgba(10, 38, 49, 0.18)',
      },
      transitionTimingFunction: {
        'smooth': 'cubic-bezier(0.25, 0.8, 0.25, 1)',
      },
    },
  },
  plugins: [],
};
