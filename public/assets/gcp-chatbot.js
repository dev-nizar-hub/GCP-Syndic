/**
 * GCP Syndic WhatsApp Chatbot
 * Adapted from Assurances 2M BotToWhatsApp component
 * Pure Vanilla JS — injectable into any HTML page
 */

(function () {
  'use strict';

  const PHONE = '212XXXXXXXXX'; // TODO: replace with real GCP Syndic WhatsApp number

  // ─── FLOWS ──────────────────────────────────────────────────────────────────

  const SYNDIC_BASE = [
    { key: 'sName',    botMessages: ['Quel est votre nom complet ?'], type: 'text' },
    { key: 'sPhone',   botMessages: ['Quel est votre numéro de téléphone ?'], type: 'tel' },
    { key: 'sCity',    botMessages: ['Dans quelle ville se trouve votre immeuble ?'], type: 'text' },
    { key: 'sLots',    botMessages: ['Combien de lots compte votre copropriété ?'], type: 'quickreply',
      options: ['Moins de 10', '10 – 30', '30 – 100', 'Plus de 100'] },
    { key: 'sDesc',    botMessages: ['Décrivez brièvement votre demande.'], type: 'text' },
    { key: 'done',
      botMessages: ['Parfait ! 🎉 Votre dossier est prêt.', 'Cliquez ci-dessous pour envoyer vos informations à notre conseiller GCP Syndic via WhatsApp.'],
      type: 'done' },
  ];

  const SYNDIC_FLOW = [
    {
      key: 'sService',
      botMessages: ['Quel type de service vous intéresse ?'],
      type: 'quickreply',
      options: ['Syndic de copropriété', 'Gestion locative', 'Location', 'Vente', 'Assurances', 'Autre'],
      onAnswer: function (answer) {
        if (answer === 'Assurances') {
          return [
            { key: 'sAssurType', botMessages: ['Quel type d\'assurance ?'], type: 'quickreply',
              options: ['Multirisque habitation', 'Garantie loyers impayés', 'Protection juridique', 'Autre'] },
            ...SYNDIC_BASE
          ];
        }
        if (answer === 'Vente') {
          return [
            { key: 'sVenteBien', botMessages: ['S\'agit-il d\'un bien à vendre ou à acheter ?'], type: 'quickreply',
              options: ['À vendre', 'À acheter'] },
            { key: 'sVenteType', botMessages: ['Quel type de bien ?'], type: 'quickreply',
              options: ['Appartement', 'Villa', 'Local commercial', 'Autre'] },
            ...SYNDIC_BASE
          ];
        }
        if (answer === 'Location') {
          return [
            { key: 'sLocType', botMessages: ['Vous souhaitez ?'], type: 'quickreply',
              options: ['Louer un bien', 'Mettre en location'] },
            { key: 'sLocBien', botMessages: ['Quel type de bien ?'], type: 'quickreply',
              options: ['Appartement', 'Villa', 'Bureau', 'Local commercial'] },
            ...SYNDIC_BASE
          ];
        }
        if (answer === 'Autre') {
          return [
            { key: 'sAutreDetail', botMessages: ['De quoi avez-vous besoin exactement ?'], type: 'text' },
            ...SYNDIC_BASE
          ];
        }
        return SYNDIC_BASE;
      }
    }
  ];

  const INITIAL_STEP = {
    key: 'clientType',
    botMessages: [
      '👋 Bonjour ! Bienvenue chez GCP Syndic.',
      'Je vais vous aider à préparer votre demande. Êtes-vous un particulier ou une entreprise / copropriété ?'
    ],
    type: 'quickreply',
    options: ['👤 Particulier', '🏢 Copropriété / Entreprise'],
    onAnswer: function (answer) {
      return SYNDIC_FLOW;
    }
  };

  // ─── STATE ───────────────────────────────────────────────────────────────────

  let currentStep = INITIAL_STEP;
  let queue = [];
  let answers = {};
  let isTyping = false;
  let isOpen = false;
  let msgIdCounter = 0;

  // ─── DOM ─────────────────────────────────────────────────────────────────────

  const styles = `
    #gcp-bot-fab {
      position: fixed; bottom: 24px; right: 24px; z-index: 9999;
    }
    #gcp-bot-toggle {
      width: 56px; height: 56px; border-radius: 50%;
      background: #0a2631; color: #fff; border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(10,38,49,0.45);
      transition: transform 0.2s, background 0.2s;
      position: relative;
    }
    #gcp-bot-toggle:hover { background: #317bff; transform: scale(1.06); }
    #gcp-bot-toggle svg { transition: transform 0.2s, opacity 0.2s; }
    #gcp-bot-ping {
      position: absolute; inset: 0; border-radius: 50%;
      background: #0a2631; animation: gcpPing 1.5s ease-out infinite;
      pointer-events: none;
    }
    @keyframes gcpPing {
      0% { transform: scale(1); opacity: 0.4; }
      100% { transform: scale(1.7); opacity: 0; }
    }
    #gcp-bot-window {
      position: fixed; bottom: 92px; right: 24px; z-index: 9998;
      width: 370px; max-width: calc(100vw - 48px);
      height: min(580px, calc(100vh - 120px));
      background: #fff; border-radius: 18px;
      box-shadow: 0 8px 48px rgba(10,38,49,0.2);
      display: flex; flex-direction: column; overflow: hidden;
      border: 1px solid #e5e7eb;
      transform-origin: bottom right;
      transition: opacity 0.22s, transform 0.22s;
    }
    #gcp-bot-window.gcp-bot-hidden {
      opacity: 0; transform: scale(0.94) translateY(10px); pointer-events: none;
    }
    @media (max-width: 480px) {
      #gcp-bot-window {
        bottom: 0; right: 0; left: 0; top: 0;
        width: 100%; max-width: 100%; height: 100dvh;
        border-radius: 0; border: none;
      }
    }
    #gcp-bot-header {
      background: #0a2631; padding: 14px 16px;
      display: flex; align-items: center; justify-content: space-between;
      flex-shrink: 0;
    }
    .gcp-bot-avatar {
      width: 40px; height: 40px; border-radius: 50%;
      background: #fff; display: flex; align-items: center; justify-content: center;
      position: relative; flex-shrink: 0;
    }
    .gcp-bot-avatar-dot {
      position: absolute; bottom: 1px; right: 1px;
      width: 11px; height: 11px; border-radius: 50%;
      background: #22c55e; border: 2px solid #0a2631;
    }
    .gcp-bot-header-info h3 { color: #fff; font-size: 14px; font-weight: 700; margin: 0; }
    .gcp-bot-header-info p  { color: rgba(255,255,255,0.7); font-size: 11px; margin: 0; }
    #gcp-bot-close {
      background: rgba(255,255,255,0.12); border: none; color: rgba(255,255,255,0.8);
      width: 30px; height: 30px; border-radius: 50%; cursor: pointer; display: flex;
      align-items: center; justify-content: center; transition: background 0.15s;
    }
    #gcp-bot-close:hover { background: rgba(255,255,255,0.25); }
    #gcp-bot-progress-bar {
      height: 3px; background: #e5e7eb; flex-shrink: 0;
    }
    #gcp-bot-progress-fill {
      height: 100%; background: #317bff;
      transition: width 0.5s ease;
    }
    #gcp-bot-messages {
      flex: 1; overflow-y: auto; padding: 14px; background: #f8f9fa;
      display: flex; flex-direction: column; gap: 10px;
    }
    .gcp-msg-row { display: flex; align-items: flex-end; gap: 6px; }
    .gcp-msg-row.user { justify-content: flex-end; }
    .gcp-msg-icon {
      width: 24px; height: 24px; border-radius: 50%;
      background: rgba(10,38,49,0.1); display: flex; align-items: center;
      justify-content: center; flex-shrink: 0; margin-bottom: 2px;
    }
    .gcp-bubble {
      padding: 10px 14px; border-radius: 18px; max-width: 82%;
      font-size: 13px; line-height: 1.55;
      animation: gcpFadeUp 0.22s ease both;
    }
    @keyframes gcpFadeUp {
      from { opacity: 0; transform: translateY(6px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    .gcp-bubble.bot {
      background: #fff; color: #1f2937;
      border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      border-bottom-left-radius: 4px;
    }
    .gcp-bubble.user {
      background: #0a2631; color: #fff;
      border-bottom-right-radius: 4px;
    }
    .gcp-typing {
      display: flex; align-items: flex-end; gap: 6px;
      animation: gcpFadeUp 0.2s ease both;
    }
    .gcp-typing-dots {
      background: #fff; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.06);
      padding: 12px 16px; border-radius: 18px; border-bottom-left-radius: 4px;
      display: flex; gap: 5px; align-items: center;
    }
    .gcp-dot {
      width: 7px; height: 7px; border-radius: 50%; background: #9ca3af;
      animation: gcpBounce 0.6s ease infinite;
    }
    .gcp-dot:nth-child(2) { animation-delay: 0.15s; }
    .gcp-dot:nth-child(3) { animation-delay: 0.30s; }
    @keyframes gcpBounce {
      0%,100% { transform: translateY(0); }
      50%      { transform: translateY(-5px); }
    }
    #gcp-quick-replies {
      display: flex; flex-wrap: wrap; gap: 7px;
      padding: 2px 0 2px 30px;
      animation: gcpFadeUp 0.22s ease both;
    }
    .gcp-qr-btn {
      padding: 6px 14px; border-radius: 999px;
      border: 1.5px solid #0a2631; background: #fff;
      color: #0a2631; font-size: 12px; font-weight: 600;
      cursor: pointer; transition: background 0.15s, color 0.15s;
    }
    .gcp-qr-btn:hover { background: #0a2631; color: #fff; }
    #gcp-bot-cta {
      margin: 4px 0;
      background: #f0fdf4; border: 1px solid #bbf7d0;
      border-radius: 14px; padding: 16px; text-align: center;
      animation: gcpFadeUp 0.3s ease both;
    }
    #gcp-bot-cta h4 { color: #166534; font-size: 14px; font-weight: 700; margin: 8px 0 4px; }
    #gcp-bot-cta p  { color: #15803d; font-size: 12px; margin: 0 0 12px; line-height: 1.5; }
    #gcp-bot-wa-btn {
      display: flex; align-items: center; justify-content: center; gap: 8px;
      background: #25d366; color: #fff; font-weight: 700; font-size: 14px;
      padding: 12px; border-radius: 12px; text-decoration: none;
      transition: background 0.15s, box-shadow 0.15s;
      box-shadow: 0 2px 12px rgba(37,211,102,0.4);
    }
    #gcp-bot-wa-btn:hover { background: #1da851; box-shadow: 0 4px 18px rgba(37,211,102,0.5); }
    #gcp-bot-input-area {
      padding: 10px 12px; background: #fff;
      border-top: 1px solid #f0f0f0; flex-shrink: 0;
    }
    #gcp-bot-input-area form { display: flex; gap: 8px; align-items: center; }
    #gcp-bot-input {
      flex: 1; background: #f3f4f6; border: none; border-radius: 999px;
      padding: 11px 16px; font-size: 13px; outline: none;
      transition: box-shadow 0.15s;
    }
    #gcp-bot-input:focus { box-shadow: 0 0 0 2px rgba(49,123,255,0.25); }
    #gcp-bot-send {
      width: 38px; height: 38px; border-radius: 50%;
      background: #0a2631; color: #fff; border: none; cursor: pointer;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0; transition: background 0.15s, opacity 0.15s;
    }
    #gcp-bot-send:disabled { opacity: 0.35; cursor: not-allowed; }
    #gcp-bot-send:not(:disabled):hover { background: #317bff; }
    #gcp-bot-hint {
      text-align: center; font-size: 11px; color: #9ca3af;
      padding: 8px; background: #fff; border-top: 1px solid #f0f0f0;
      flex-shrink: 0;
    }
  `;

  function injectStyles() {
    const tag = document.createElement('style');
    tag.textContent = styles;
    document.head.appendChild(tag);
  }

  function buildHTML() {
    const container = document.createElement('div');
    container.innerHTML = `
      <div id="gcp-bot-fab">
        <div id="gcp-bot-ping"></div>
        <button id="gcp-bot-toggle" aria-label="Ouvrir le chat GCP Syndic">
          <svg id="gcp-icon-chat" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
          <svg id="gcp-icon-close" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" style="display:none;">
            <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>

      <div id="gcp-bot-window" class="gcp-bot-hidden" role="dialog" aria-label="Chat GCP Syndic">
        <div id="gcp-bot-header">
          <div style="display:flex;align-items:center;gap:12px;">
            <div class="gcp-bot-avatar">
              <img src="/logo.png" alt="GCP Syndic" style="width:28px;height:28px;object-fit:contain;" onerror="this.style.display='none'"/>
              <div class="gcp-bot-avatar-dot"></div>
            </div>
            <div class="gcp-bot-header-info">
              <h3>Assistant GCP Syndic</h3>
              <p>Réponse rapide · En ligne</p>
            </div>
          </div>
          <button id="gcp-bot-close" aria-label="Fermer">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
              <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
            </svg>
          </button>
        </div>
        <div id="gcp-bot-progress-bar"><div id="gcp-bot-progress-fill" style="width:0%"></div></div>
        <div id="gcp-bot-messages"></div>
        <div id="gcp-bot-input-area" style="display:none;">
          <form id="gcp-bot-form">
            <input id="gcp-bot-input" type="text" placeholder="Votre réponse..." autocomplete="off"/>
            <button type="submit" id="gcp-bot-send" disabled>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
              </svg>
            </button>
          </form>
        </div>
        <div id="gcp-bot-hint" style="display:none;">Sélectionnez une option ci-dessus</div>
      </div>
    `;
    document.body.appendChild(container);
  }

  // ─── RENDERING ───────────────────────────────────────────────────────────────

  function getMessagesEl()   { return document.getElementById('gcp-bot-messages'); }
  function getProgressFill() { return document.getElementById('gcp-bot-progress-fill'); }

  function scrollToBottom() {
    const el = getMessagesEl();
    if (el) el.scrollTop = el.scrollHeight;
  }

  function addBotBubble(text) {
    const el = getMessagesEl();
    const row = document.createElement('div');
    row.className = 'gcp-msg-row';
    row.innerHTML = `
      <div class="gcp-msg-icon">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#0a2631" stroke-width="2" stroke-linecap="round">
          <rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
        </svg>
      </div>
      <div class="gcp-bubble bot"></div>
    `;
    row.querySelector('.gcp-bubble').textContent = text;
    el.appendChild(row);
    scrollToBottom();
  }

  function addUserBubble(text) {
    const el = getMessagesEl();
    const row = document.createElement('div');
    row.className = 'gcp-msg-row user';
    row.innerHTML = `<div class="gcp-bubble user"></div>`;
    row.querySelector('.gcp-bubble').textContent = text;
    el.appendChild(row);
    scrollToBottom();
  }

  function showTyping() {
    const el = getMessagesEl();
    const div = document.createElement('div');
    div.id = 'gcp-typing-indicator';
    div.className = 'gcp-typing';
    div.innerHTML = `
      <div class="gcp-msg-icon">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#0a2631" stroke-width="2" stroke-linecap="round">
          <rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
        </svg>
      </div>
      <div class="gcp-typing-dots">
        <div class="gcp-dot"></div>
        <div class="gcp-dot"></div>
        <div class="gcp-dot"></div>
      </div>
    `;
    el.appendChild(div);
    scrollToBottom();
  }

  function hideTyping() {
    const t = document.getElementById('gcp-typing-indicator');
    if (t) t.remove();
  }

  function clearInteractive() {
    const qr = document.getElementById('gcp-quick-replies');
    const cta = document.getElementById('gcp-bot-cta');
    if (qr)  qr.remove();
    if (cta) cta.remove();
    document.getElementById('gcp-bot-input-area').style.display = 'none';
    document.getElementById('gcp-bot-hint').style.display = 'none';
  }

  function renderStep(step) {
    clearInteractive();
    const el = getMessagesEl();

    if (step.type === 'quickreply') {
      const wrap = document.createElement('div');
      wrap.id = 'gcp-quick-replies';
      step.options.forEach(function(opt) {
        const btn = document.createElement('button');
        btn.className = 'gcp-qr-btn';
        btn.textContent = opt;
        btn.onclick = function() { handleAnswer(opt); };
        wrap.appendChild(btn);
      });
      el.appendChild(wrap);
      document.getElementById('gcp-bot-hint').style.display = 'block';
      scrollToBottom();
    } else if (step.type === 'text' || step.type === 'tel') {
      const area = document.getElementById('gcp-bot-input-area');
      const input = document.getElementById('gcp-bot-input');
      input.type = step.type === 'tel' ? 'tel' : 'text';
      input.value = '';
      area.style.display = 'block';
      setTimeout(function() { input.focus(); }, 50);
    } else if (step.type === 'done') {
      const cta = document.createElement('div');
      cta.id = 'gcp-bot-cta';
      cta.innerHTML = `
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>
        </svg>
        <h4>Dossier complet !</h4>
        <p>Toutes vos informations sont prêtes. Un clic suffit pour les envoyer à notre conseiller.</p>
        <a id="gcp-bot-wa-btn" href="${generateWhatsAppUrl()}" target="_blank" rel="noopener noreferrer">
          <svg viewBox="0 0 32 32" style="width:20px;height:20px;fill:#fff;" xmlns="http://www.w3.org/2000/svg">
            <path d="M16.002 3.2C9.374 3.2 4 8.574 4 15.2c0 2.252.618 4.352 1.686 6.148L4 28.8l7.656-1.66A11.76 11.76 0 0 0 16.002 28.8C22.628 28.8 28 23.426 28 16.8c0-6.626-5.372-12-11.998-12.6Zm6.58 16.87c-.273.766-1.598 1.464-2.178 1.558-.535.087-1.21.124-1.952-.12-.45-.146-1.03-.34-1.77-.665-3.115-1.346-5.147-4.51-5.303-4.72-.154-.21-1.25-1.663-1.25-3.174 0-1.51.793-2.256 1.075-2.563a1.14 1.14 0 0 1 .825-.37c.207 0 .413.003.594.012.19.009.446-.073.698.533.26.627.88 2.16.957 2.316.077.156.128.338.026.545-.1.206-.15.334-.3.514-.148.18-.315.402-.448.54-.15.154-.306.32-.132.63.174.31.776 1.28 1.666 2.073 1.145 1.022 2.113 1.338 2.42 1.493.306.154.484.128.662-.077.18-.205.764-.893 1.027-1.2.26-.306.516-.256.87-.154.354.103 2.26 1.065 2.648 1.26.39.192.65.29.745.45.097.16.097.924-.177 1.69Z"/>
          </svg>
          Envoyer sur WhatsApp
        </a>
      `;
      el.appendChild(cta);
      updateProgress(100);
      scrollToBottom();
    }
  }

  function updateProgress(val) {
    const fill = getProgressFill();
    if (fill) fill.style.width = val + '%';
  }

  // ─── LOGIC ───────────────────────────────────────────────────────────────────

  function getReaction(key, answer) {
    if (key === 'sName') return 'Enchanté(e), ' + answer + ' !';
    if (key === 'clientType') return answer.includes('Copropriété') ? 'Bienvenue ! 🏢' : 'Bienvenue ! 👤';
    return null;
  }

  function handleAnswer(answer) {
    if (isTyping) return;
    clearInteractive();
    addUserBubble(answer);
    answers[currentStep.key] = answer;

    // Update progress
    const answeredCount = Object.keys(answers).length;
    updateProgress(Math.min(answeredCount * 12, 90));

    const injected = currentStep.onAnswer ? currentStep.onAnswer(answer) : [];
    const newQueue = injected.concat(queue);
    if (newQueue.length === 0) return;

    const nextStep = newQueue[0];
    queue = newQueue.slice(1);

    const reaction = getReaction(currentStep.key, answer);
    const allMsgs = (reaction ? [reaction] : []).concat(nextStep.botMessages);

    isTyping = true;
    showTyping();

    allMsgs.forEach(function(text, i) {
      setTimeout(function() {
        hideTyping();
        addBotBubble(text);
        if (i < allMsgs.length - 1) showTyping();
        if (i === allMsgs.length - 1) {
          isTyping = false;
          currentStep = nextStep;
          renderStep(nextStep);
        }
      }, 550 + i * 500);
    });
  }

  function generateWhatsAppUrl() {
    const isCompany = (answers.clientType || '').includes('Copropriété');
    const service   = answers.sService   || '';
    const lines = [];

    if (isCompany) {
      lines.push('🏢 *Nouvelle demande Copropriété — GCP Syndic*', '');
    } else {
      lines.push('👤 *Nouvelle demande Particulier — GCP Syndic*', '');
    }

    lines.push('*Service souhaité :* ' + service);
    if (answers.sAssurType)   lines.push('*Type assurance :* '   + answers.sAssurType);
    if (answers.sVenteBien)   lines.push('*Vente/Achat :* '       + answers.sVenteBien);
    if (answers.sVenteType)   lines.push('*Type de bien :* '      + answers.sVenteType);
    if (answers.sLocType)     lines.push('*Location :* '          + answers.sLocType);
    if (answers.sLocBien)     lines.push('*Type de bien :* '      + answers.sLocBien);
    if (answers.sAutreDetail) lines.push('*Détail :* '            + answers.sAutreDetail);
    lines.push('*Nom :* '        + (answers.sName  || ''));
    lines.push('*Téléphone :* '  + (answers.sPhone || ''));
    lines.push('*Ville :* '      + (answers.sCity  || ''));
    if (answers.sLots) lines.push('*Nb. de lots :* ' + answers.sLots);
    lines.push('', '*Demande :*', answers.sDesc || '');

    return 'https://wa.me/' + PHONE + '?text=' + encodeURIComponent(lines.join('\n'));
  }

  // ─── INIT ────────────────────────────────────────────────────────────────────

  function openBot() {
    isOpen = true;
    document.getElementById('gcp-bot-window').classList.remove('gcp-bot-hidden');
    document.getElementById('gcp-bot-ping').style.display = 'none';
    document.getElementById('gcp-icon-chat').style.display = 'none';
    document.getElementById('gcp-icon-close').style.display = 'block';
  }

  function closeBot() {
    isOpen = false;
    document.getElementById('gcp-bot-window').classList.add('gcp-bot-hidden');
    document.getElementById('gcp-bot-ping').style.display = 'block';
    document.getElementById('gcp-icon-chat').style.display = 'block';
    document.getElementById('gcp-icon-close').style.display = 'none';
  }

  function initBot() {
    injectStyles();
    buildHTML();

    // Initial messages
    const el = getMessagesEl();
    INITIAL_STEP.botMessages.forEach(function(text) {
      addBotBubble(text);
    });
    renderStep(INITIAL_STEP);

    // Input events
    const input = document.getElementById('gcp-bot-input');
    const send  = document.getElementById('gcp-bot-send');
    input.addEventListener('input', function() {
      send.disabled = !input.value.trim();
    });
    document.getElementById('gcp-bot-form').addEventListener('submit', function(e) {
      e.preventDefault();
      const val = input.value.trim();
      if (!val || isTyping) return;
      input.value = '';
      send.disabled = true;
      handleAnswer(val);
    });

    // Toggle
    document.getElementById('gcp-bot-toggle').addEventListener('click', function() {
      isOpen ? closeBot() : openBot();
    });
    document.getElementById('gcp-bot-close').addEventListener('click', closeBot);
  }

  // Launch when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initBot);
  } else {
    initBot();
  }

})();
