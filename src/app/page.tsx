import Image from "next/image";
import Link from "next/link";

/* ─── DATA ─────────────────────────────────────────────── */
const services = [
  {
    title: "Syndic de copropriété",
    subtitle: "L'expertise de la\nMaison GCP Syndic",
    href: "/nos-metiers/syndic-de-copropriete",
    img: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=400&q=80",
  },
  {
    title: "Location",
    subtitle: "Louer en toute quiétude",
    href: "/nos-metiers/location",
    img: "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=400&q=80",
  },
  {
    title: "Gestion locative",
    subtitle: "Faire gérer votre bien\nen toute sérénité",
    href: "/nos-metiers/gestion-locative",
    img: "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=400&q=80",
  },
  {
    title: "Assurances",
    subtitle: "Nos solutions sécurité\npour assurer la gestion\nde votre bien",
    href: "/nos-metiers/assurances",
    img: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=400&q=80",
  },
  {
    title: "Vente",
    subtitle: "Un accompagnement\nsur-mesure",
    href: "/nos-metiers/vente",
    img: "https://images.unsplash.com/photo-1582407947304-fd86f28f8e3c?auto=format&fit=crop&w=400&q=80",
  },
];

/* ─── PAGE ─────────────────────────────────────────────── */
export default function Home() {
  return (
    <div className="w-full">

      {/* ═══════════════════════════════════════════════════
          HERO — full-height, text bottom-left like Atrium
      ════════════════════════════════════════════════════ */}
      <section className="relative h-[88vh] w-full flex items-end overflow-hidden">
        <div className="absolute inset-0">
          <Image
            src="/grand-theatre.jpeg"
            alt="GCP Syndic - La gestion de la confiance"
            fill
            className="object-cover object-center"
            priority
          />
          {/* dark gradient left → transparent right */}
          <div className="absolute inset-0 bg-gradient-to-r from-gcp-dark/90 via-gcp-dark/60 to-gcp-dark/20" />
          {/* subtle bottom fade */}
          <div className="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-gcp-dark/60 to-transparent" />
        </div>

        {/* Slideshow dots (visual only) */}
        <div className="absolute right-8 top-1/2 -translate-y-1/2 flex flex-col gap-2 z-10">
          {[0, 1, 2].map((i) => (
            <span key={i} className={`block rounded-full transition-all ${i === 0 ? "w-3 h-3 bg-white" : "w-2 h-2 bg-white/40"}`} />
          ))}
        </div>

        {/* Hero text block */}
        <div className="relative z-10 w-full max-w-container mx-auto px-6 pb-20">
          <div className="max-w-2xl">
            <p className="text-gcp-blue font-semibold uppercase tracking-[0.2em] text-xs mb-5">
              GCP Syndic · Maroc
            </p>
            <h1 className="text-5xl md:text-[62px] font-bold text-white leading-[1.12] mb-6">
              Faire battre le&nbsp;cœur<br />
              de votre quartier.
            </h1>
            <div className="w-16 h-1 bg-gcp-blue mb-6" />
            <p className="text-white/80 text-lg font-light mb-10 max-w-lg leading-relaxed">
              La satisfaction de nos clients au cœur de nos valeurs.
            </p>
            <Link
              href="/notre-maison"
              className="inline-block bg-gcp-blue hover:bg-gcp-blue-dark text-white font-bold text-xs uppercase tracking-[0.15em] py-4 px-10 transition-colors shadow-lg"
            >
              Découvrir GCP Syndic
            </Link>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════
          NOS MÉTIERS — 5-column panel (exact Atrium layout)
      ════════════════════════════════════════════════════ */}
      <section className="bg-white border-b border-gcp-border shadow-sm">
        <div className="max-w-container mx-auto">
          <div className="grid grid-cols-5">
            {services.map((s, i) => (
              <Link
                key={s.title}
                href={s.href}
                className={`group flex flex-col items-center text-center py-8 px-4 hover:bg-gcp-gray transition-colors ${i < 4 ? "border-r border-gcp-border" : ""}`}
              >
                <div className="relative w-full aspect-[4/3] mb-4 overflow-hidden bg-gray-100">
                  <Image
                    src={s.img}
                    alt={s.title}
                    fill
                    className="object-cover group-hover:scale-105 transition-transform duration-500"
                    unoptimized
                  />
                </div>
                <span className="font-bold text-gcp-dark group-hover:text-gcp-blue text-[13px] leading-snug transition-colors block mb-1">
                  {s.title}
                </span>
                <span className="text-gray-500 text-[12px] leading-relaxed whitespace-pre-line">
                  {s.subtitle}
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════
          INTRO / NOTRE MAISON — 2-col text + image
      ════════════════════════════════════════════════════ */}
      <section className="py-20 bg-white">
        <div className="max-w-container mx-auto px-6">
          <div className="grid lg:grid-cols-2 gap-16 items-center">

            {/* Text */}
            <div>
              <p className="text-gcp-blue font-bold uppercase tracking-[0.2em] text-xs mb-5">
                Notre maison
              </p>
              <h2 className="text-[38px] font-bold text-gcp-dark leading-tight mb-8">
                Votre partenaire<br />de confiance au Maroc
              </h2>
              <div className="space-y-4 text-gray-600 text-[15px] leading-relaxed mb-10">
                <p>
                  GCP Syndic est une société de gestion immobilière basée au Maroc,
                  spécialisée dans l'administration de copropriétés et la gestion
                  de patrimoine immobilier.
                </p>
                <p>
                  Avec notre tagline{" "}
                  <em className="not-italic font-semibold text-gcp-dark">
                    «&nbsp;La gestion de la confiance&nbsp;»
                  </em>
                  , nous plaçons la transparence, la proximité et l'expertise
                  au cœur de chaque mission.
                </p>
                <p>
                  Notre équipe d'experts accompagne copropriétaires, propriétaires
                  et locataires avec rigueur et réactivité, pour préserver et
                  valoriser votre patrimoine.
                </p>
              </div>
              <Link
                href="/notre-maison"
                className="inline-block border-2 border-gcp-dark text-gcp-dark font-bold text-xs uppercase tracking-[0.15em] py-3.5 px-8 hover:bg-gcp-dark hover:text-white transition-colors"
              >
                En savoir plus
              </Link>
            </div>

            {/* Image */}
            <div className="relative h-[460px] overflow-hidden">
              <Image
                src="https://images.unsplash.com/photo-1600880292089-90a7e086ee0c?auto=format&fit=crop&q=80&w=900"
                alt="Équipe GCP Syndic"
                fill
                className="object-cover"
                unoptimized
              />
              <div className="absolute bottom-0 left-0 right-0 bg-gcp-blue py-4 px-6">
                <p className="text-white font-semibold text-sm uppercase tracking-widest text-center">
                  La gestion de la confiance
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════
          VALEURS — 3 pillars on dark bg (Atrium-style)
      ════════════════════════════════════════════════════ */}
      <section className="bg-gcp-dark py-16">
        <div className="max-w-container mx-auto px-6">
          <div className="grid md:grid-cols-3 divide-y md:divide-y-0 md:divide-x divide-white/10">
            {[
              {
                num: "01",
                title: "Pour une véritable expertise locale",
                text: "Nos gestionnaires connaissent parfaitement le marché immobilier marocain et ses spécificités réglementaires.",
              },
              {
                num: "02",
                title: "Et une volonté d'indépendance",
                text: "Indépendant de tout groupe, GCP Syndic préserve une totale objectivité dans ses conseils et prestations.",
              },
              {
                num: "03",
                title: "Pour entretenir votre patrimoine",
                text: "Nous gérons votre bien avec le soin que vous lui portez, en optimisant sa valeur sur le long terme.",
              },
            ].map((v) => (
              <div key={v.num} className="px-10 py-10 text-center md:text-left">
                <span className="text-gcp-blue font-bold text-3xl block mb-4">{v.num}</span>
                <h3 className="font-bold text-white text-[16px] leading-snug mb-3">{v.title}</h3>
                <p className="text-white/60 text-[14px] leading-relaxed">{v.text}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════
          CHIFFRES CLÉS
      ════════════════════════════════════════════════════ */}
      <section className="bg-gcp-gray py-14 border-y border-gcp-border">
        <div className="max-w-container mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {[
              { num: "20+",  label: "Années d'expérience" },
              { num: "500+", label: "Copropriétés gérées" },
              { num: "98%",  label: "Clients satisfaits"  },
              { num: "24/7", label: "Support disponible"  },
            ].map((s) => (
              <div key={s.label}>
                <div className="text-4xl font-bold text-gcp-blue mb-2">{s.num}</div>
                <div className="text-gcp-dark text-xs uppercase tracking-widest font-semibold">{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ═══════════════════════════════════════════════════
          NOS BIENS — Acheter / Louer panels
      ════════════════════════════════════════════════════ */}
      <section className="py-20 bg-white">
        <div className="max-w-container mx-auto px-6">
          <div className="text-center mb-12">
            <p className="text-gcp-blue font-bold uppercase tracking-[0.2em] text-xs mb-4">Nos biens</p>
            <h2 className="text-[36px] font-bold text-gcp-dark">Trouver votre bien</h2>
          </div>
          <div className="grid md:grid-cols-2 gap-6">
            {[
              {
                label: "Acheter",
                img: "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=900&q=80",
                href: "/nos-biens/achat",
                desc: "Trouvez le bien idéal parmi nos annonces de vente",
              },
              {
                label: "Louer",
                img: "https://images.unsplash.com/photo-1416331108676-a22ccb276e35?auto=format&fit=crop&w=900&q=80",
                href: "/nos-biens/location",
                desc: "Découvrez nos offres de location disponibles",
              },
            ].map((b) => (
              <Link
                key={b.label}
                href={b.href}
                className="group relative overflow-hidden block h-80"
              >
                <Image
                  src={b.img}
                  alt={b.label}
                  fill
                  className="object-cover group-hover:scale-105 transition-transform duration-700"
                  unoptimized
                />
                <div className="absolute inset-0 bg-gcp-dark/55 group-hover:bg-gcp-dark/45 transition-colors" />
                <div className="absolute inset-0 flex flex-col justify-end p-8 text-white">
                  <h3 className="text-3xl font-bold mb-2">{b.label}</h3>
                  <p className="text-white/75 text-sm mb-5">{b.desc}</p>
                  <span className="inline-flex items-center gap-2 border border-white text-white text-xs font-bold uppercase tracking-widest py-2.5 px-6 w-fit group-hover:bg-white group-hover:text-gcp-dark transition-colors">
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

      {/* ═══════════════════════════════════════════════════
          RECRUTEMENT / CTA band — dark like Atrium
      ════════════════════════════════════════════════════ */}
      <section
        className="relative py-20 overflow-hidden"
        style={{ backgroundColor: "#0a2631" }}
      >
        {/* subtle background pattern */}
        <div className="absolute inset-0 opacity-5"
          style={{ backgroundImage: "url(\"data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E\")" }}
        />
        <div className="relative z-10 max-w-container mx-auto px-6">
          <div className="max-w-2xl">
            <p className="text-gcp-blue font-bold uppercase tracking-[0.2em] text-xs mb-5">
              Rejoignez-nous
            </p>
            <h2 className="text-[38px] font-bold text-white leading-tight mb-5">
              Vous avez la passion de<br />l'immobilier&nbsp;?
            </h2>
            <p className="text-white/65 text-[15px] leading-relaxed mb-10 max-w-lg">
              Partagez nos valeurs et rejoignez une équipe dynamique au service
              de la gestion immobilière au Maroc. Découvrez nos offres.
            </p>
            <Link
              href="/contact"
              className="inline-block bg-gcp-blue hover:bg-gcp-blue-dark text-white font-bold text-xs uppercase tracking-[0.15em] py-4 px-10 transition-colors"
            >
              Nous contacter
            </Link>
          </div>
        </div>
      </section>

    </div>
  );
}
