/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/atrium.html',
        permanent: false,
      },
    ];
  },
};

module.exports = nextConfig;
