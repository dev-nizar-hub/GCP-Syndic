/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
      {
        protocol: 'https',
        hostname: 'i.pravatar.cc',
      },
    ],
    // Allow unoptimized for local dev speed
    formats: ['image/avif', 'image/webp'],
  },
  async redirects() {
    return [
      {
        source: '/',
        destination: '/atrium.html',
        permanent: false,
      },
    ];
  },
  async rewrites() {
    return [
      { source: '/atrium',                    destination: '/atrium.html' },
      { source: '/contact',                   destination: '/contact.html' },
      { source: '/nos-metiers',               destination: '/nos-metiers.html' },
      { source: '/nos-metiers/syndic-de-copropriete', destination: '/nos-metiers-syndic.html' },
      { source: '/nos-metiers/gestion-locative',      destination: '/nos-metiers-gestion-locative.html' },
      { source: '/nos-metiers/vente',                 destination: '/nos-metiers-vente.html' },
      { source: '/nos-metiers/location',              destination: '/nos-metiers-location.html' },
      { source: '/nos-metiers/assurances',            destination: '/nos-metiers-assurances.html' },
      { source: '/nos-biens/achat',                   destination: '/nos-biens-achat.html' },
      { source: '/nos-biens/location',                destination: '/nos-biens-location.html' },
      { source: '/notre-maison',                      destination: '/notre-maison.html' },
      { source: '/nous-rejoindre',                    destination: '/nous-rejoindre.html' },
    ];
  },
};

module.exports = nextConfig;
