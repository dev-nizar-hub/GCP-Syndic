import Link from "next/link";
import Image from "next/image";

export default function Footer() {
  return (
    <footer className="bg-[#1b1b1b] text-white pt-16 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Top Social Section */}
        <div className="flex flex-col md:flex-row justify-between items-center border-b border-gray-700 pb-8 mb-12">
          <h3 className="text-xl font-bold uppercase tracking-widest mb-4 md:mb-0">Suivez-nous</h3>
          <div className="flex space-x-6">
            <a href="#" className="hover:text-gcp-blue transition-colors">
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="#" className="hover:text-gcp-blue transition-colors">
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          {/* Column 1: Logo */}
          <div>
            <Image 
              src="/logo/Gestion copropriété.png" 
              alt="GCP Syndic" 
              width={240} 
              height={80} 
              className="mb-6 w-56 h-auto object-contain bg-white rounded-md p-3"
            />
            <p className="text-gray-400 text-sm">
              La gestion de la confiance.<br />
              Votre partenaire immobilier au Maroc.
            </p>
          </div>

          {/* Column 2: Nos métiers */}
          <div>
            <h4 className="text-lg font-bold mb-6 uppercase tracking-wider text-white">L'expertise GCP Syndic</h4>
            <ul className="space-y-4">
              <li><Link href="/syndic-copropriete" className="text-gray-400 hover:text-white transition-colors">Syndic de copropriété</Link></li>
              <li><Link href="/location" className="text-gray-400 hover:text-white transition-colors">Location</Link></li>
              <li><Link href="/gestion-locative" className="text-gray-400 hover:text-white transition-colors">Gestion locative</Link></li>
              <li><Link href="/assurances" className="text-gray-400 hover:text-white transition-colors">Assurances</Link></li>
              <li><Link href="/vente" className="text-gray-400 hover:text-white transition-colors">Vente</Link></li>
            </ul>
          </div>

          {/* Column 3: Contact */}
          <div>
            <h4 className="text-lg font-bold mb-6 uppercase tracking-wider text-white">Nous trouver</h4>
            <ul className="space-y-4">
              <li><Link href="/contact" className="text-gray-400 hover:text-white transition-colors">Nous contacter</Link></li>
              <li><Link href="/nos-biens" className="text-gray-400 hover:text-white transition-colors">Nos biens</Link></li>
            </ul>
          </div>

          {/* Column 4: Legal */}
          <div>
            <h4 className="text-lg font-bold mb-6 uppercase tracking-wider text-white">Liens utiles</h4>
            <ul className="space-y-4">
              <li><Link href="/mentions-legales" className="text-gray-400 hover:text-white transition-colors">Mentions légales</Link></li>
              <li><Link href="/politique-confidentialite" className="text-gray-400 hover:text-white transition-colors">Politique de confidentialité</Link></li>
              <li><Link href="/plan-du-site" className="text-gray-400 hover:text-white transition-colors">Plan du site</Link></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
          <p>&copy; {new Date().getFullYear()} GCP Syndic. Tous droits réservés.</p>
        </div>
      </div>
    </footer>
  );
}
