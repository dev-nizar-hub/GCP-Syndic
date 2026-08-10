/**
 * Intercept all form submissions and redirect to WhatsApp
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
    // If it's a specific form that shouldn't be intercepted (like a search form), you can add a class to ignore it
    const form = e.target;
    
    // Ignore chatbot form or search forms
    if (form.id === 'gcp-bot-form' || form.id === 'searchform' || form.classList.contains('search-form')) {
      return; // let it do its thing
    }

    e.preventDefault();
    e.stopPropagation(); // Stop Formidable AJAX handler if any

    const inputs = form.querySelectorAll('input, textarea, select');
    const fields = [];

    inputs.forEach(input => {
      // Ignore hidden, submit, button, image, reset fields
      if (['hidden', 'submit', 'button', 'image', 'reset', 'file'].includes(input.type)) return;
      
      const value = input.value.trim();
      if (!value) return; // Skip empty fields

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

    messageLines = messageLines.concat(fields);

    const message = messageLines.join('\n');
    const waUrl = `https://wa.me/${PHONE_NUMBER}?text=${encodeURIComponent(message)}`;

    // Show a small success message on the page instead of completely hiding the form?
    // Let's just open WhatsApp.
    
    // Try to find the button and change its text to "Redirection..."
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

  // Attach to document to catch all forms, even dynamically added ones
  document.addEventListener('submit', handleFormSubmit, true);

})();
