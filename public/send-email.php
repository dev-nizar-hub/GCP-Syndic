<?php
/**
 * GCP Syndic - Traitement de la demande de bien
 * Envoi d'un email à l'admin, d'un email de confirmation au client,
 * et redirection vers WhatsApp.
 */

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 1. Récupération et nettoyage des données
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $phone = htmlspecialchars(trim($_POST['phone'] ?? ''));
    $email = filter_var(trim($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
    
    $property_type = htmlspecialchars(trim($_POST['property_type'] ?? 'Bien'));
    $property_city = htmlspecialchars(trim($_POST['property_city'] ?? ''));
    $property_rooms = htmlspecialchars(trim($_POST['property_rooms'] ?? ''));

    // Validation basique
    if (empty($name) || empty($phone) || empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Erreur: Données invalides. Veuillez remplir tous les champs correctement.");
    }

    // 2. Configuration des emails
    // /!\ A MODIFIER : L'adresse email de l'administrateur
    $admin_email = "contact@gcp-syndic.ma"; // L'email de l'agence
    $from_email = "noreply@gcp-syndic.ma";  // L'adresse d'expédition (doit souvent exister sur le domaine)

    // Formatage des détails du bien
    $property_details = $property_type;
    if ($property_city) $property_details .= " à " . $property_city;
    if ($property_rooms) $property_details .= " (" . $property_rooms . ")";

    // ---------------------------------------------------------
    // 3. Email à l'Administrateur
    // ---------------------------------------------------------
    $admin_subject = "Nouvelle demande de bien : $property_details";
    
    $admin_message = "Bonjour,\n\n";
    $admin_message .= "Une nouvelle demande de contact a été soumise depuis le site web.\n\n";
    $admin_message .= "DÉTAILS DU CLIENT :\n";
    $admin_message .= "Nom : $name\n";
    $admin_message .= "Téléphone : $phone\n";
    $admin_message .= "Email : $email\n\n";
    $admin_message .= "DÉTAILS DU BIEN :\n";
    $admin_message .= "Type : $property_type\n";
    $admin_message .= "Ville : $property_city\n";
    if ($property_rooms) {
        $admin_message .= "Détails : $property_rooms\n";
    }
    $admin_message .= "\nLe client va également être redirigé vers le WhatsApp de l'agence.\n";

    $admin_headers = "From: GCP Syndic Website <$from_email>\r\n";
    $admin_headers .= "Reply-To: $email\r\n";
    
    // Envoi de l'email admin
    @mail($admin_email, $admin_subject, $admin_message, $admin_headers);

    // ---------------------------------------------------------
    // 4. Email de confirmation au Client
    // ---------------------------------------------------------
    $client_subject = "GCP Syndic - Confirmation de votre demande";
    
    $client_message = "Bonjour $name,\n\n";
    $client_message .= "Nous vous confirmons la bonne réception de votre demande concernant le bien suivant :\n";
    $client_message .= "- $property_details\n\n";
    $client_message .= "Un conseiller GCP Syndic traitera votre demande et vous recontactera rapidement au $phone.\n\n";
    $client_message .= "Cordialement,\n";
    $client_message .= "L'équipe GCP Syndic\n";
    $client_message .= "https://gcp-syndic.ma\n";

    $client_headers = "From: GCP Syndic <$from_email>\r\n";
    $client_headers .= "Reply-To: $admin_email\r\n";

    // Envoi de l'email client
    @mail($email, $client_subject, $client_message, $client_headers);

    // ---------------------------------------------------------
    // 5. Redirection vers WhatsApp
    // ---------------------------------------------------------
    $whatsapp_number = "212662081784";
    
    $wa_msg = "Bonjour GCP Syndic,\n\nJe m'appelle *$name* et je suis intéressé(e) par l'annonce suivante :\n\n";
    $wa_msg .= "📍 *Bien :* $property_type à $property_city\n";
    if ($property_rooms) {
        $wa_msg .= "🛏 *Détails :* $property_rooms\n";
    }
    $wa_msg .= "\nMon adresse e-mail : $email\n";
    $wa_msg .= "Pouvez-vous me recontacter au $phone pour plus d'informations ?";

    $whatsapp_url = "https://wa.me/" . $whatsapp_number . "?text=" . rawurlencode($wa_msg);
    
    // Redirection
    header("Location: " . $whatsapp_url);
    exit;
    
} else {
    // Si on accède directement au script sans poster, on renvoie vers l'accueil
    header("Location: /");
    exit;
}
