"use client";

import { useState, useEffect, useRef } from "react";
import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";

const metiers = [
  { title: "Syndic de copropriété", subtitle: "L'expertise GCP Syndic", href: "/nos-metiers-syndic.html", img: "/assets/wp-content/uploads/2021/05/m-metier-syndic-300x237.jpg" },
  { title: "Location", subtitle: "Louer en toute quiétude", href: "/nos-metiers-location.html", img: "/assets/wp-content/uploads/2021/05/m-metier-location-300x237.jpg" },
  { title: "Gestion locative", subtitle: "Gérer votre bien en sérénité", href: "/nos-metiers-gestion-locative.html", img: "/assets/wp-content/uploads/2021/05/m-metier-gestion-locative-300x237.jpg" },
  { title: "Assurances", subtitle: "Nos solutions pour votre bien", href: "/nos-metiers-assurances.html", img: "/assets/wp-content/uploads/2021/05/m-metier-assurance-300x237.jpg" },
  { title: "Vente", subtitle: "Un accompagnement sur-mesure", href: "/nos-metiers-vente.html", img: "/assets/wp-content/uploads/2021/05/m-metier-vente-300x237.jpg" },
];

const biens = [
  { label: "Achat", href: "/nos-biens-achat.html" },
  { label: "Location", href: "/nos-biens-location.html" },
];

export default function Header() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [metiersOpen, setMetiersOpen] = useState(false);
  const [biensOpen, setBiensOpen] = useState(false);
  const [mobileMetiersOpen, setMobileMetiersOpen] = useState(false);
  const [mobileBiensOpen, setMobileBiensOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const metiersRef = useRef<HTMLDivElement>(null);
  const biensRef = useRef<HTMLDivElement>(null);
  const pathname = usePathname();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (metiersRef.current && !metiersRef.current.contains(e.target as Node)) setMetiersOpen(false);
      if (biensRef.current && !biensRef.current.contains(e.target as Node)) setBiensOpen(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, []);

  // close mobile menu on route change
  useEffect(() => { setMobileOpen(false); }, [pathname]);

  const isActive = (href: string) => pathname === href || pathname.startsWith(href + "/");

  const navLinkClass = (href: string) =>
    `flex items-center h-full px-4 text-[18px] font-normal transition-all duration-200 border-b-2 ${
      isActive(href)
        ? "text-[#0a2631] font-bold border-[#0a2631]"
        : "text-[#0a2631] border-transparent hover:text-[#317bff] hover:border-[#317bff]"
    }`;

  return (
    <>
      {/* ══════════════════════════════════════════
          DESKTOP HEADER (lg and up)
      ══════════════════════════════════════════ */}
      <header
        className={`hidden lg:block sticky top-0 z-50 w-full bg-white transition-shadow duration-300 ${
          scrolled ? "shadow-lg" : "shadow-sm"
        }`}
        style={{ fontFamily: "'Signika', sans-serif" }}
      >
        <div className="mx-auto flex items-center justify-between" style={{ maxWidth: "1040px", padding: "0 20px" }}>

          {/* LOGO */}
          <Link href="/" aria-label="GCP Syndic - Accueil" className="flex-shrink-0 py-2">
            <Image
              src="/logo.png"
              alt="GCP Syndic"
              width={220}
              height={54}
              className="h-14 w-auto object-contain"
              priority
            />
          </Link>

          {/* DESKTOP NAV */}
          <nav className="flex items-center h-[90px]" aria-label="Navigation principale">

            {/* Notre maison */}
            <Link href="/notre-maison.html" className={navLinkClass("/notre-maison")}>
              Notre maison
            </Link>

            {/* Nos métiers dropdown */}
            <div
              ref={metiersRef}
              className="relative h-full flex items-center"
              onMouseEnter={() => setMetiersOpen(true)}
              onMouseLeave={() => setMetiersOpen(false)}
            >
              <button
                className={`flex items-center gap-1 h-full px-4 text-[18px] font-normal transition-all duration-200 border-b-2 cursor-pointer ${
                  pathname.includes("nos-metiers")
                    ? "text-[#0a2631] font-bold border-[#0a2631]"
                    : "text-[#0a2631] border-transparent hover:text-[#317bff] hover:border-[#317bff]"
                }`}
                aria-expanded={metiersOpen}
              >
                Nos métiers
                <svg className={`w-3.5 h-3.5 ml-0.5 transition-transform duration-200 ${metiersOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              {/* Mega dropdown */}
              <div
                className={`absolute top-full left-1/2 -translate-x-1/2 bg-white border-t-4 border-[#317bff] shadow-2xl transition-all duration-200 z-50 ${
                  metiersOpen ? "opacity-100 visible translate-y-0" : "opacity-0 invisible -translate-y-2 pointer-events-none"
                }`}
                style={{ width: "900px" }}
                onMouseEnter={() => setMetiersOpen(true)}
                onMouseLeave={() => setMetiersOpen(false)}
              >
                <div className="grid grid-cols-5 divide-x divide-gray-100">
                  {metiers.map((m) => (
                    <Link
                      key={m.title}
                      href={m.href}
                      className="group flex flex-col items-center text-center p-5 hover:bg-gray-50 transition-colors"
                      onClick={() => setMetiersOpen(false)}
                    >
                      <div className="relative w-full aspect-[4/3] mb-3 overflow-hidden bg-gray-100 rounded">
                        <Image
                          src={m.img}
                          alt={m.title}
                          fill
                          className="object-cover group-hover:scale-105 transition-transform duration-500"
                          unoptimized
                          onError={() => {}}
                        />
                      </div>
                      <span className="font-bold text-[#0a2631] group-hover:text-[#317bff] text-sm leading-tight transition-colors block mb-1">
                        {m.title}
                      </span>
                      <span className="text-gray-500 text-xs">{m.subtitle}</span>
                    </Link>
                  ))}
                </div>
                <div className="px-5 py-3 bg-gray-50 border-t border-gray-100">
                  <Link href="/nos-metiers.html" className="text-[#317bff] text-xs font-semibold hover:underline flex items-center gap-1" onClick={() => setMetiersOpen(false)}>
                    Voir tous nos métiers
                    <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" /></svg>
                  </Link>
                </div>
              </div>
            </div>

            {/* Nos biens dropdown */}
            <div
              ref={biensRef}
              className="relative h-full flex items-center"
              onMouseEnter={() => setBiensOpen(true)}
              onMouseLeave={() => setBiensOpen(false)}
            >
              <button
                className={`flex items-center gap-1 h-full px-4 text-[18px] font-normal transition-all duration-200 border-b-2 cursor-pointer ${
                  pathname.includes("nos-biens")
                    ? "text-[#0a2631] font-bold border-[#0a2631]"
                    : "text-[#0a2631] border-transparent hover:text-[#317bff] hover:border-[#317bff]"
                }`}
                aria-expanded={biensOpen}
              >
                Nos biens
                <svg className={`w-3.5 h-3.5 ml-0.5 transition-transform duration-200 ${biensOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.5" d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              <div
                className={`absolute top-full left-0 bg-white border-t-4 border-[#317bff] shadow-2xl transition-all duration-200 z-50 ${
                  biensOpen ? "opacity-100 visible translate-y-0" : "opacity-0 invisible -translate-y-2 pointer-events-none"
                }`}
                style={{ width: "200px" }}
                onMouseEnter={() => setBiensOpen(true)}
                onMouseLeave={() => setBiensOpen(false)}
              >
                {biens.map((item) => (
                  <Link
                    key={item.label}
                    href={item.href}
                    className="block px-5 py-3.5 text-[#0a2631] hover:bg-gray-50 hover:text-[#317bff] transition-colors text-[16px] border-b border-gray-100 last:border-0"
                    onClick={() => setBiensOpen(false)}
                  >
                    {item.label}
                  </Link>
                ))}
              </div>
            </div>

            {/* Nous rejoindre */}
            <Link href="/nous-rejoindre.html" className={navLinkClass("/nous-rejoindre")}>
              Nous rejoindre
            </Link>

            {/* CONTACT CTA button */}
            <div className="ml-4 flex items-center">
              <Link
                href="/contact.html"
                className="bg-[#317bff] hover:bg-[#1a56cc] text-white font-bold text-[14px] uppercase tracking-widest px-6 py-3 transition-all duration-200 hover:shadow-lg"
              >
                Contact
              </Link>
            </div>

          </nav>
        </div>
      </header>

      {/* ══════════════════════════════════════════
          MOBILE HEADER (below lg)
      ══════════════════════════════════════════ */}
      <header
        className="lg:hidden sticky top-0 z-50 w-full bg-white shadow-md"
        style={{ fontFamily: "'Signika', sans-serif" }}
      >
        <div className="flex items-center justify-between px-5 py-3">
          {/* LOGO */}
          <Link href="/" aria-label="GCP Syndic - Accueil">
            <Image src="/logo.png" alt="GCP Syndic" width={180} height={32} className="h-10 w-auto object-contain" priority />
          </Link>

          {/* Hamburger */}
          <button
            onClick={() => setMobileOpen(!mobileOpen)}
            className="text-[#0a2631] p-2 rounded hover:bg-gray-100 transition-colors"
            aria-label="Menu"
            aria-expanded={mobileOpen}
          >
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              {mobileOpen
                ? <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
                : <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16" />}
            </svg>
          </button>
        </div>

        {/* Mobile panel */}
        <div className={`bg-white border-t border-gray-100 shadow-lg overflow-hidden transition-all duration-300 ${mobileOpen ? "max-h-screen pb-4" : "max-h-0"}`}>
          <nav className="px-5 py-2 space-y-0">
            <Link href="/notre-maison.html" className="block py-4 text-[#0a2631] font-semibold border-b border-gray-100 text-sm hover:text-[#317bff]" onClick={() => setMobileOpen(false)}>
              Notre maison
            </Link>

            <div className="border-b border-gray-100">
              <button className="flex items-center justify-between w-full py-4 text-[#0a2631] font-semibold text-sm hover:text-[#317bff]" onClick={() => setMobileMetiersOpen(!mobileMetiersOpen)}>
                Nos métiers
                <svg className={`w-4 h-4 transition-transform ${mobileMetiersOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7" /></svg>
              </button>
              {mobileMetiersOpen && (
                <div className="pb-3 pl-4 space-y-1">
                  {metiers.map((m) => (
                    <Link key={m.title} href={m.href} className="block py-2.5 text-gray-600 hover:text-[#317bff] text-sm border-l-2 border-transparent hover:border-[#317bff] pl-3 transition-all" onClick={() => setMobileOpen(false)}>
                      {m.title}
                    </Link>
                  ))}
                </div>
              )}
            </div>

            <div className="border-b border-gray-100">
              <button className="flex items-center justify-between w-full py-4 text-[#0a2631] font-semibold text-sm hover:text-[#317bff]" onClick={() => setMobileBiensOpen(!mobileBiensOpen)}>
                Nos biens
                <svg className={`w-4 h-4 transition-transform ${mobileBiensOpen ? "rotate-180" : ""}`} fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 9l-7 7-7-7" /></svg>
              </button>
              {mobileBiensOpen && (
                <div className="pb-3 pl-4 space-y-1">
                  {biens.map((b) => (
                    <Link key={b.label} href={b.href} className="block py-2.5 text-gray-600 hover:text-[#317bff] text-sm border-l-2 border-transparent hover:border-[#317bff] pl-3 transition-all" onClick={() => setMobileOpen(false)}>
                      {b.label}
                    </Link>
                  ))}
                </div>
              )}
            </div>

            <Link href="/nous-rejoindre.html" className="block py-4 text-[#0a2631] font-semibold border-b border-gray-100 text-sm hover:text-[#317bff]" onClick={() => setMobileOpen(false)}>
              Nous rejoindre
            </Link>

            <Link href="/contact.html" className="block mt-4 text-center bg-[#317bff] text-white font-bold py-4 text-sm uppercase tracking-widest hover:bg-[#1a56cc] transition-colors" onClick={() => setMobileOpen(false)}>
              Contact
            </Link>
          </nav>
        </div>
      </header>
    </>
  );
}
