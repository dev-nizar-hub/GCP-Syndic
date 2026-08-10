/**
 * Intercept all form submissions and redirect to WhatsApp
 * WhatsApp number: 212708066188 (07 08 06 61 88)
 */

(function () {
  'use strict';

  const PHONE_NUMBER = '212708066188';

  function getFieldName(input) {
    if (input.name) return input.name;
    if (input.id) return input.id;
    if (input.placeholder) return input.placeholder;
    // For Formidable forms, sometimes the label is right before it
    const parent = input.closest('.frm_form_field');
    if (parent) {
      const label = parent.querySelector('label.frm_primary_label');
      if (label) {
        return label.innerText.replace('*', '').trim();
      }
    }
    return 'Champ inconnu';
  }

  function handleFormSubmit(e) {
    const form = e.target;
    
    // Ignore chatbot form or search forms
    if (form.id === 'gcp-bot-form' || form.id === 'searchform' || form.classList.contains('search-form')) {
      return;
    }

    e.preventDefault();
    e.stopPropagation();

    const inputs = form.querySelectorAll('input, textarea, select');
    const fields = [];

    inputs.forEach(input => {
      if (['hidden', 'submit', 'button', 'image', 'reset', 'file'].includes(input.type)) return;
      
      const value = input.value.trim();
      if (!value) return;

      const name = getFieldName(input);
      fields.push(`*${name}:* ${value}`);
    });

    if (fields.length === 0) {
      alert("Veuillez remplir le formulaire avant de l'envoyer.");
      return;
    }

    let pageName = document.title.split('-')[0].trim();
    if (!pageName) pageName = "le site web";

    let messageLines = [
      `*Nouvelle Demande depuis ${pageName}*`,
      ''
    ];

    // ── Include property card details if the page has them (demande-bien.html) ──
    const propTitle = document.getElementById('prop-title');
    const propDesc  = document.getElementById('prop-desc');
    
    if (propTitle && propTitle.innerText && propTitle.innerText !== 'Chargement des détails...') {
      messageLines.push(`*Bien sélectionné :* ${propTitle.innerText}`);
      if (propDesc && propDesc.innerText) {
        messageLines.push(`*Détails :* ${propDesc.innerText}`);
      }
      messageLines.push('');
    }

    // ── Client contact fields ──
    messageLines.push('*Coordonnées du client :*');
    messageLines = messageLines.concat(fields);

    const message = messageLines.join('\n');
    const waUrl = `https://wa.me/${PHONE_NUMBER}?text=${encodeURIComponent(message)}`;

    // Update button text briefly
    const submitBtn = form.querySelector('[type="submit"], button:not([type="button"])');
    if (submitBtn) {
      const originalText = submitBtn.innerText || submitBtn.value;
      if (submitBtn.tagName === 'INPUT') {
        submitBtn.value = "Redirection...";
      } else {
        submitBtn.innerText = "Redirection vers WhatsApp...";
      }
      setTimeout(() => {
        if (submitBtn.tagName === 'INPUT') {
          submitBtn.value = originalText;
        } else {
          submitBtn.innerText = originalText;
        }
      }, 3000);
    }

    window.open(waUrl, '_blank');
  }

  document.addEventListener('submit', handleFormSubmit, true);

})();
