"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import Image from "next/image";

const metiers = [
  {
    title: "Syndic de copropriété",
    subtitle: "L'expertise de la\nMaison GCP Syndic",
    href: "/nos-metiers/syndic-de-copropriete",
    img: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=300&q=80",
  },
  {
    title: "Location",
    subtitle: "Louer en toute quiétude",
    href: "/nos-metiers/location",
    img: "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=300&q=80",
  },
  {
    title: "Gestion locative",
    subtitle: "Faire gérer votre bien\nen toute sérénité",
    href: "/nos-metiers/gestion-locative",
    img: "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=300&q=80",
  },
  {
    title: "Assurances",
    subtitle: "Nos solutions sécurité\npour assurer la gestion\nde votre bien",
    href: "/nos-metiers/assurances",
    img: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=300&q=80",
  },
  {
    title: "Vente",
    subtitle: "Un accompagnement\nsur-mesure",
    href: "/nos-metiers/vente",
    img: "https://images.unsplash.com/photo-1582407947304-fd86f28f8e3c?auto=format&fit=crop&w=300&q=80",
  },
];

export default function Header() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [metiersOpen, setMetiersOpen] = useState(false);
  const [biensOpen, setBiensOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [mobileMetiersOpen, setMobileMetiersOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header className={`sticky top-0 z-50 w-full bg-white transition-shadow duration-300 ${scrolled ? "shadow-lg" : "shadow-sm"}`}>

      {/* ── TOP UTILITY BAR (like Atrium's red bar) ── */}
      <div className="bg-gcp-dark text-white text-xs">
        <div className="max-w-container mx-auto px-6 flex items-center justify-end h-9 gap-6">
          <a href="tel:+212522000000" className="flex items-center gap-1.5 hover:text-gcp-blue transition-colors">
            <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
            +212 5 22 00 00 00
          </a>
          <a href="mailto:contact@gcp-syndic.ma" className="flex items-center gap-1.5 hover:text-gcp-blue transition-colors">
            <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
            </svg>
            contact@gcp-syndic.ma
          </a>
          <div className="flex items-center gap-3 ml-2">
            <a href="#" aria-label="Facebook" className="hover:text-gcp-blue transition-colors">
              <svg className="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="#" aria-label="LinkedIn" className="hover:text-gcp-blue transition-colors">
              <svg className="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
          </div>
        </div>
      </div>

      {/* ── MAIN NAV BAR ── */}
      <div className="max-w-container mx-auto px-6">
        <div className="flex items-center justify-between h-[88px]">

          {/* ── LOGO ── */}
          <Link href="/" className="flex-shrink-0 flex items-center">
            <Image
              src="/logo/Gestion copropriété.png"
              alt="GCP Syndic"
              width={220}
              height={80}
              className="h-16 w-auto object-contain"
              priority
            />
          </Link>

          {/* ── DESKTOP NAV ── */}
          <nav className="hidden lg:flex items-center h-full">

            {/* Notre maison */}
            <Link
              href="/notre-maison"
              className="flex items-center h-full px-5 text-gcp-dark font-semibold text-[15px] hover:text-gcp-blue border-b-2 border-transparent hover:border-gcp-blue transition-all tracking-wide"
            >
              Notre maison
            </Link>

            {/* Nos métiers — mega dropdown */}
            <div
              className="relative h-full flex items-center"
              onMouseEnter={() => setMetiersOpen(true)}
              onMouseLeave={() => setMetiersOpen(false)}
            >
              <button className="flex items-center gap-1.5 h-full px-5 text-gcp-dark font-semibold text-[15px] hover:text-gcp-blue border-b-2 border-transparent hover:border-gcp-blue transition-all tracking-wide cursor-pointer">
                Nos métiers
                <svg className={`w-3.5 h-3.5 transition-transform duration-200 ${metiersOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              {/* Mega dropdown */}
              <div className={`absolute top-full left-1/2 -translate-x-1/2 bg-white border border-gray-100 shadow-2xl transition-all duration-200 ${metiersOpen ? "opacity-100 visible translate-y-0" : "opacity-0 invisible -translate-y-2"}`} style={{ width: "960px" }}>
                {/* Blue accent bar top */}
                <div className="h-1 w-full bg-gcp-blue" />
                <div className="grid grid-cols-5">
                  {metiers.map((m) => (
                    <Link
                      key={m.title}
                      href={m.href}
                      className="group flex flex-col items-center text-center p-5 border-r border-gray-100 last:border-0 hover:bg-gray-50 transition-colors"
                      onClick={() => setMetiersOpen(false)}
                    >
                      <div className="relative w-full aspect-[4/3] mb-3 overflow-hidden bg-gray-100">
                        <Image
                          src={m.img}
                          alt={m.title}
                          fill
                          className="object-cover group-hover:scale-105 transition-transform duration-500"
                          unoptimized
                        />
                      </div>
                      <span className="font-bold text-gcp-dark group-hover:text-gcp-blue text-sm leading-tight transition-colors block mb-1">
                        {m.title}
                      </span>
                      <span className="text-gray-500 text-xs leading-relaxed whitespace-pre-line">
                        {m.subtitle}
                      </span>
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Nos biens — dropdown */}
            <div
              className="relative h-full flex items-center"
              onMouseEnter={() => setBiensOpen(true)}
              onMouseLeave={() => setBiensOpen(false)}
            >
              <button className="flex items-center gap-1.5 h-full px-5 text-gcp-dark font-semibold text-[15px] hover:text-gcp-blue border-b-2 border-transparent hover:border-gcp-blue transition-all tracking-wide cursor-pointer">
                Nos biens
                <svg className={`w-3.5 h-3.5 transition-transform duration-200 ${biensOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              <div className={`absolute top-full left-0 bg-white border border-gray-100 shadow-2xl transition-all duration-200 ${biensOpen ? "opacity-100 visible translate-y-0" : "opacity-0 invisible -translate-y-2"}`} style={{ width: "260px" }}>
                <div className="h-1 w-full bg-gcp-blue" />
                <div className="py-2">
                  {[
                    { label: "Acheter", href: "/nos-biens/achat" },
                    { label: "Louer", href: "/nos-biens/location" },
                  ].map((item) => (
                    <Link
                      key={item.label}
                      href={item.href}
                      className="flex items-center gap-3 px-5 py-3 text-gcp-dark hover:bg-gray-50 hover:text-gcp-blue transition-colors text-sm font-semibold"
                      onClick={() => setBiensOpen(false)}
                    >
                      <svg className="w-4 h-4 text-gcp-blue flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
                      </svg>
                      {item.label}
                    </Link>
                  ))}
                </div>
              </div>
            </div>

            {/* Contact CTA */}
            <div className="ml-4 flex items-center">
              <Link
                href="/contact"
                className="bg-gcp-blue hover:bg-gcp-blue-dark text-white font-bold text-[13px] uppercase tracking-widest px-7 py-3 transition-colors"
              >
                Contact
              </Link>
            </div>
          </nav>

          {/* ── MOBILE TOGGLE ── */}
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className="lg:hidden text-gcp-dark p-2"
            aria-label="Menu"
          >
            <svg className="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {mobileOpen
                ? <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                : <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />}
            </svg>
          </button>
        </div>
      </div>

      {/* ── MOBILE MENU ── */}
      {mobileOpen && (
        <div className="lg:hidden bg-white border-t border-gray-100 shadow-xl">
          <div className="px-6 py-4 space-y-1">
            <Link href="/notre-maison" className="block py-4 text-gcp-dark font-semibold border-b border-gray-100 text-sm tracking-wide" onClick={() => setMobileOpen(false)}>
              Notre maison
            </Link>

            <div className="border-b border-gray-100">
              <button
                className="flex items-center justify-between w-full py-4 text-gcp-dark font-semibold text-sm tracking-wide"
                onClick={() => setMobileMetiersOpen(!mobileMetiersOpen)}
              >
                Nos métiers
                <svg className={`w-4 h-4 transition-transform ${mobileMetiersOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7" />
                </svg>
              </button>
              {mobileMetiersOpen && (
                <div className="pb-3 space-y-1 pl-4">
                  {metiers.map((m) => (
                    <Link key={m.title} href={m.href} className="block py-2 text-gray-600 hover:text-gcp-blue text-sm" onClick={() => setMobileOpen(false)}>
                      {m.title}
                    </Link>
                  ))}
                </div>
              )}
            </div>

            <div className="py-4 border-b border-gray-100">
              <p className="text-gcp-dark font-semibold text-sm tracking-wide mb-2">Nos biens</p>
              <div className="pl-4 space-y-1">
                <Link href="/nos-biens/achat" className="block py-1.5 text-gray-600 hover:text-gcp-blue text-sm" onClick={() => setMobileOpen(false)}>Acheter</Link>
                <Link href="/nos-biens/location" className="block py-1.5 text-gray-600 hover:text-gcp-blue text-sm" onClick={() => setMobileOpen(false)}>Louer</Link>
              </div>
            </div>

            <Link href="/contact" className="block mt-4 text-center bg-gcp-blue text-white font-bold py-4 text-sm uppercase tracking-widest" onClick={() => setMobileOpen(false)}>
              Contact
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
