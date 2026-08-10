import Image from "next/image";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "GCP Syndic — La gestion de la confiance | Maroc",
  description: "GCP Syndic, votre partenaire immobilier de proximité au Maroc. Syndic de copropriété, gestion locative, vente et assurances à Casablanca, Rabat, Marrakech et Tanger.",
};

/* ─── DATA ─────────────────────────────────────────────── */
const services = [
  {
    title: "Syndic de copropriété",
    subtitle: "L'expertise de la\nMaison GCP Syndic",
    href: "/nos-metiers-syndic.html",
    img: "https://images.unsplash.com/photo-1486325212027-8081e485255e?auto=format&fit=crop&w=600&q=80",
  },
  {
    title: "Location",
    subtitle: "Louer en toute quiétude",
    href: "/nos-metiers-location.html",
    img: "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=600&q=80",
  },
  {
    title: "Gestion locative",
    subtitle: "Faire gérer votre bien\nen toute sérénité",
    href: "/nos-metiers-gestion-locative.html",
    img: "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=600&q=80",
  },
  {
    title: "Assurances",
    subtitle: "Nos solutions sécurité\npour votre bien",
    href: "/nos-metiers-assurances.html",
    img: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=600&q=80",
  },
  {
    title: "Vente",
    subtitle: "Un accompagnement\nsur-mesure",
    href: "/nos-metiers-vente.html",
    img: "https://images.unsplash.com/photo-1582407947304-fd86f28f8e3c?auto=format&fit=crop&w=600&q=80",
  },
];

const stats = [
  { num: "20+",  label: "Années d'expérience", icon: "🏆" },
  { num: "500+", label: "Copropriétés gérées", icon: "🏢" },
  { num: "98%",  label: "Clients satisfaits",  icon: "⭐" },
  { num: "4",    label: "Villes au Maroc",     icon: "📍" },
];

const valeurs = [
  {
    num: "01",
    title: "Une expertise locale marocaine",
    text: "Nos gestionnaires connaissent parfaitement le marché immobilier marocain, ses réglementations et ses spécificités locales pour chaque ville.",
  },
  {
    num: "02",
    title: "Une totale indépendance",
    text: "Indépendant de tout groupe financier, GCP Syndic préserve une objectivité absolue dans ses conseils et préconisations.",
  },
  {
    num: "03",
    title: "La valorisation de votre patrimoine",
    text: "Nous gérons votre bien avec le soin d'un propriétaire, en optimisant sa valeur et sa rentabilité sur le long terme.",
  },
];

const testimonials = [
  {
    quote: "GCP Syndic gère notre résidence depuis 3 ans. Professionnalisme, réactivité et transparence — exactement ce qu'on attendait.",
    author: "Mehdi A.",
    city: "Casablanca",
    avatar: "https://i.pravatar.cc/60?img=11",
  },
  {
    quote: "Notre bien locatif est entre de bonnes mains. Les rapports sont clairs et l'équipe est toujours disponible.",
    author: "Nadia B.",
    city: "Rabat",
    avatar: "https://i.pravatar.cc/60?img=5",
  },
  {
    quote: "La vente de notre appartement s'est faite en 3 semaines. Un accompagnement vraiment sur-mesure.",
    author: "Karim L.",
    city: "Marrakech",
    avatar: "https://i.pravatar.cc/60?img=15",
  },
];

/* ─── PAGE ─────────────────────────────────────────────── */
export default function Home() {
  return (
    <div className="w-full">

      {/* ══════════════════════════════════════════════════════════
          HERO — Morocco Grand Théâtre, full-height, overlay
      ═══════════════════════════════════════════════════════════ */}
      <section className="relative h-[90vh] min-h-[580px] w-full flex items-end overflow-hidden" aria-label="Bannière principale">
        <div className="absolute inset-0">
          <Image
            src="/grand-theatre.jpeg"
            alt="GCP Syndic - La gestion de la confiance au Maroc"
            fill
            className="object-cover object-center"
            priority
          />
          {/* Gradient overlay */}
          <div className="absolute inset-0 bg-gradient-to-r from-[#0a2631]/92 via-[#0a2631]/65 to-[#0a2631]/20" />
          <div className="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-[#0a2631]/70 to-transparent" />
        </div>

        {/* Subtle dots decoration */}
        <div className="absolute right-8 top-1/2 -translate-y-1/2 flex flex-col gap-2.5 z-10">
          {[0, 1, 2].map((i) => (
            <span key={i} className={`block rounded-full transition-all ${i === 0 ? "w-3 h-3 bg-white" : "w-2 h-2 bg-white/35"}`} />
          ))}
        </div>

        {/* Hero content */}
        <div className="relative z-10 w-full max-w-7xl mx-auto px-6 pb-20 md:pb-28">
          <div className="max-w-2xl">
            <p className="text-[#317bff] font-semibold uppercase tracking-[0.25em] text-xs mb-5 flex items-center gap-2">
              <span className="w-6 h-px bg-[#317bff]" />
              GCP Syndic · Maroc
            </p>
            <h1 className="text-5xl md:text-[64px] font-bold text-white leading-[1.1] mb-6">
              Faire battre le&nbsp;cœur<br />
              de votre quartier.
            </h1>
            <div className="w-16 h-1 bg-[#317bff] mb-7" />
            <p className="text-white/75 text-lg font-light mb-10 max-w-xl leading-relaxed">
              La satisfaction de nos clients au cœur de nos valeurs.<br />
              Votre partenaire immobilier de confiance au Maroc.
            </p>
            <div className="flex flex-wrap gap-4">
              <Link
                href="/notre-maison.html"
                className="inline-block bg-[#317bff] hover:bg-[#1a56cc] text-white font-bold text-xs uppercase tracking-[0.18em] py-4 px-10 transition-all duration-200 hover:shadow-xl hover:shadow-blue-900/40"
              >
                Découvrir GCP Syndic
              </Link>
              <Link
                href="/contact.html"
                className="inline-block border-2 border-white/70 text-white font-bold text-xs uppercase tracking-[0.18em] py-4 px-8 hover:bg-white hover:text-[#0a2631] transition-all duration-200"
              >
                Nous contacter
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          NOS MÉTIERS — 5-column panel
      ═══════════════════════════════════════════════════════════ */}
      <section className="bg-white border-b border-[#e2eaf4] shadow-md">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-5">
            {services.map((s, i) => (
              <Link
                key={s.title}
                href={s.href}
                className={`group flex flex-col items-center text-center py-8 px-4 hover:bg-[#f5f7fa] transition-colors duration-200 ${i < 4 ? "border-r border-[#e2eaf4]" : ""}`}
              >
                <div className="relative w-full aspect-[4/3] mb-4 overflow-hidden bg-gray-100">
                  <Image
                    src={s.img}
                    alt={s.title}
                    fill
                    className="object-cover group-hover:scale-105 transition-transform duration-700"
                    unoptimized
                  />
                  <div className="absolute inset-0 bg-[#0a2631]/0 group-hover:bg-[#317bff]/10 transition-colors duration-300" />
                </div>
                <span className="font-bold text-[#0a2631] group-hover:text-[#317bff] text-[13px] leading-snug transition-colors block mb-1">
                  {s.title}
                </span>
                <span className="text-gray-500 text-[11px] leading-relaxed whitespace-pre-line">
                  {s.subtitle}
                </span>
                <span className="mt-3 text-[#317bff] text-[10px] uppercase tracking-widest font-bold opacity-0 group-hover:opacity-100 transition-opacity flex items-center gap-1">
                  Découvrir
                  <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7"/></svg>
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          NOTRE MAISON — 2-col text + Morocco image
      ═══════════════════════════════════════════════════════════ */}
      <section className="py-24 bg-white" aria-labelledby="section-maison">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid lg:grid-cols-2 gap-16 items-center">

            {/* Image side */}
            <div className="relative h-[520px] overflow-hidden order-2 lg:order-1">
              <Image
                src="https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&q=80&w=900"
                alt="Immeuble résidentiel au Maroc"
                fill
                className="object-cover"
                unoptimized
              />
              {/* Floating stats card */}
              <div className="absolute bottom-8 right-0 translate-x-0 bg-[#317bff] text-white p-6 shadow-2xl">
                <div className="text-4xl font-bold mb-1">20+</div>
                <div className="text-xs font-semibold uppercase tracking-widest text-white/80">Années d'expérience</div>
              </div>
              {/* Accent border */}
              <div className="absolute top-0 left-0 w-1 h-full bg-[#317bff]" />
            </div>

            {/* Text side */}
            <div className="order-1 lg:order-2">
              <p className="text-[#317bff] font-bold uppercase tracking-[0.22em] text-xs mb-5 flex items-center gap-2">
                <span className="w-6 h-px bg-[#317bff]" />
                Notre maison
              </p>
              <h2 id="section-maison" className="text-[40px] font-bold text-[#0a2631] leading-tight mb-8">
                Votre partenaire<br />de confiance au Maroc
              </h2>
              <div className="space-y-4 text-gray-600 text-[15px] leading-relaxed mb-10">
                <p>
                  GCP Syndic est une société de gestion immobilière marocaine,
                  spécialisée dans l&apos;administration de copropriétés et la gestion
                  de patrimoine immobilier depuis plus de 20 ans.
                </p>
                <p>
                  Avec notre signature{" "}
                  <em className="not-italic font-semibold text-[#0a2631]">
                    «&nbsp;La gestion de la confiance&nbsp;»
                  </em>
                  , nous plaçons la transparence, la proximité et l&apos;expertise
                  au cœur de chaque mission — à Casablanca, Rabat, Marrakech et Tanger.
                </p>
                <p>
                  Notre équipe de professionnels accompagne copropriétaires, propriétaires
                  et locataires avec rigueur et réactivité, pour préserver et valoriser
                  votre patrimoine immobilier.
                </p>
              </div>
              <div className="flex flex-wrap gap-4">
                <Link
                  href="/notre-maison.html"
                  className="inline-block border-2 border-[#0a2631] text-[#0a2631] font-bold text-xs uppercase tracking-[0.15em] py-3.5 px-8 hover:bg-[#0a2631] hover:text-white transition-all duration-200"
                >
                  En savoir plus
                </Link>
                <Link
                  href="/nous-rejoindre.html"
                  className="inline-block text-[#317bff] font-semibold text-xs uppercase tracking-[0.15em] py-3.5 px-4 hover:underline transition-all duration-200 flex items-center gap-2"
                >
                  Rejoindre l&apos;équipe
                  <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7"/></svg>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          VALEURS — 3 pillars on dark navy bg
      ═══════════════════════════════════════════════════════════ */}
      <section className="bg-[#0a2631] py-20" aria-label="Nos valeurs">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-14">
            <p className="text-[#317bff] font-bold uppercase tracking-[0.22em] text-xs mb-4">Pourquoi GCP Syndic</p>
            <h2 className="text-[34px] font-bold text-white">Nos engagements</h2>
          </div>
          <div className="grid md:grid-cols-3 gap-0 divide-y md:divide-y-0 md:divide-x divide-white/10">
            {valeurs.map((v) => (
              <div key={v.num} className="px-10 py-10 text-center md:text-left group hover:bg-white/5 transition-colors duration-300">
                <span className="text-[#317bff] font-bold text-4xl block mb-5 leading-none">{v.num}</span>
                <h3 className="font-bold text-white text-[17px] leading-snug mb-4">{v.title}</h3>
                <p className="text-white/55 text-[14px] leading-relaxed">{v.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          CHIFFRES CLÉS
      ═══════════════════════════════════════════════════════════ */}
      <section className="bg-[#f5f7fa] py-16 border-y border-[#e2eaf4]" aria-label="Nos chiffres clés">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {stats.map((s) => (
              <div key={s.label} className="group">
                <div className="text-3xl mb-2">{s.icon}</div>
                <div className="text-4xl font-bold text-[#317bff] mb-2 group-hover:scale-105 transition-transform">{s.num}</div>
                <div className="text-[#0a2631] text-xs uppercase tracking-widest font-semibold">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          NOS BIENS — Acheter / Louer panels
      ═══════════════════════════════════════════════════════════ */}
      <section className="py-24 bg-white" aria-labelledby="section-biens">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-14">
            <p className="text-[#317bff] font-bold uppercase tracking-[0.22em] text-xs mb-4">Nos biens</p>
            <h2 id="section-biens" className="text-[36px] font-bold text-[#0a2631]">Trouvez votre bien au Maroc</h2>
            <p className="text-gray-500 mt-4 text-[15px] max-w-xl mx-auto">Consultez nos annonces de vente et de location à travers le Maroc.</p>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {[
              {
                label: "Acheter",
                img: "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=900&q=80",
                href: "/nos-biens-achat.html",
                desc: "Trouvez le bien idéal parmi nos annonces de vente au Maroc",
              },
              {
                label: "Louer",
                img: "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?auto=format&fit=crop&w=900&q=80",
                href: "/nos-biens-location.html",
                desc: "Découvrez nos offres de location disponibles à travers le pays",
              },
            ].map((b) => (
              <Link
                key={b.label}
                href={b.href}
                className="group relative overflow-hidden block h-80"
                aria-label={b.label}
              >
                <Image
                  src={b.img}
                  alt={b.label}
                  fill
                  className="object-cover group-hover:scale-105 transition-transform duration-700"
                  unoptimized
                />
                <div className="absolute inset-0 bg-[#0a2631]/55 group-hover:bg-[#0a2631]/45 transition-colors duration-300" />
                <div className="absolute inset-0 flex flex-col justify-end p-8 text-white">
                  <h3 className="text-3xl font-bold mb-2">{b.label}</h3>
                  <p className="text-white/75 text-sm mb-5">{b.desc}</p>
                  <span className="inline-flex items-center gap-2 border border-white text-white text-xs font-bold uppercase tracking-widest py-2.5 px-6 w-fit group-hover:bg-white group-hover:text-[#0a2631] transition-colors duration-200">
                    Voir les annonces
                    <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 5l7 7-7 7" />
                    </svg>
                  </span>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          TÉMOIGNAGES
      ═══════════════════════════════════════════════════════════ */}
      <section className="bg-[#f5f7fa] py-20 border-t border-[#e2eaf4]" aria-label="Témoignages clients">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-14">
            <p className="text-[#317bff] font-bold uppercase tracking-[0.22em] text-xs mb-4">Ils nous font confiance</p>
            <h2 className="text-[34px] font-bold text-[#0a2631]">Ce que disent nos clients</h2>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {testimonials.map((t, i) => (
              <div key={i} className="bg-white p-8 shadow-sm border border-[#e2eaf4] hover:shadow-md hover:-translate-y-1 transition-all duration-300">
                {/* Stars */}
                <div className="flex gap-1 mb-4">
                  {[...Array(5)].map((_, j) => (
                    <svg key={j} className="w-4 h-4 text-amber-400" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                  ))}
                </div>
                <p className="text-gray-600 text-[14px] leading-relaxed mb-6 italic">&ldquo;{t.quote}&rdquo;</p>
                <div className="flex items-center gap-3">
                  <Image src={t.avatar} alt={t.author} width={40} height={40} className="rounded-full" unoptimized />
                  <div>
                    <p className="font-bold text-[#0a2631] text-sm">{t.author}</p>
                    <p className="text-gray-400 text-xs">{t.city}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ══════════════════════════════════════════════════════════
          RECRUTEMENT CTA — dark band
      ═══════════════════════════════════════════════════════════ */}
      <section className="relative py-24 overflow-hidden bg-[#0a2631]" aria-label="Nous rejoindre">
        {/* Subtle background texture */}
        <div className="absolute inset-0 opacity-[0.03]"
          style={{ backgroundImage: "url(\"data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E\")" }}
        />
        {/* Blue accent image */}
        <div className="absolute right-0 top-0 bottom-0 w-2/5 hidden lg:block">
          <Image
            src="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=800&q=80"
            alt="Équipe GCP Syndic"
            fill
            className="object-cover opacity-20"
            unoptimized
          />
          <div className="absolute inset-0 bg-gradient-to-r from-[#0a2631] to-transparent" />
        </div>
        <div className="relative z-10 max-w-7xl mx-auto px-6">
          <div className="max-w-2xl">
            <p className="text-[#317bff] font-bold uppercase tracking-[0.22em] text-xs mb-5 flex items-center gap-2">
              <span className="w-6 h-px bg-[#317bff]" />
              Rejoignez-nous
            </p>
            <h2 className="text-[40px] font-bold text-white leading-tight mb-6">
              Vous avez la passion de<br />l&apos;immobilier&nbsp;?
            </h2>
            <p className="text-white/60 text-[15px] leading-relaxed mb-10 max-w-lg">
              Partagez nos valeurs et rejoignez une équipe dynamique au service
              de la gestion immobilière au Maroc. Découvrez nos offres d&apos;emploi.
            </p>
            <div className="flex flex-wrap gap-4">
              <Link
                href="/nous-rejoindre.html"
                className="inline-block bg-[#317bff] hover:bg-[#1a56cc] text-white font-bold text-xs uppercase tracking-[0.18em] py-4 px-10 transition-all duration-200 hover:shadow-xl hover:shadow-blue-900/40"
              >
                Voir les offres
              </Link>
              <Link
                href="/contact.html"
                className="inline-block border border-white/40 text-white font-bold text-xs uppercase tracking-[0.18em] py-4 px-8 hover:border-white hover:bg-white/10 transition-all duration-200"
              >
                Nous contacter
              </Link>
            </div>
          </div>
        </div>
      </section>

    </div>
  );
}
