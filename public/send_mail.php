<?php
header('Content-Type: application/json');

// Only allow POST requests
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form fields and remove whitespace
    $name    = strip_tags(trim($_POST["name"] ?? ''));
    $email   = filter_var(trim($_POST["email"] ?? ''), FILTER_SANITIZE_EMAIL);
    $phone   = strip_tags(trim($_POST["phone"] ?? ''));
    $subject = strip_tags(trim($_POST["subject"] ?? 'Demande de contact'));
    $message = trim($_POST["message"] ?? '');

    // Check that data was sent to the mailer.
    if (empty($name) OR empty($message) OR !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(["status" => "error", "message" => "Veuillez remplir tous les champs correctement."]);
        exit;
    }

    // ----------------------------------------------------
    // 1. Email to GCP Syndic
    // ----------------------------------------------------
    $recipient = "contact@gcp.ma";
    $email_subject = "Nouveau message du site GCP : $subject";

    $email_content = "Vous avez reçu un nouveau message depuis le formulaire de contact du site Web.\n\n";
    $email_content .= "Nom : $name\n";
    $email_content .= "Email : $email\n";
    $email_content .= "Téléphone : $phone\n\n";
    $email_content .= "Message :\n$message\n";

    $email_headers = "From: GCP Website <no-reply@gcp.ma>\r\n";
    $email_headers .= "Reply-To: $email\r\n";
    $email_headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send the email to you
    $success = mail($recipient, $email_subject, $email_content, $email_headers);

    // ----------------------------------------------------
    // 2. Auto-reply to the client
    // ----------------------------------------------------
    if ($success) {
        $client_subject = "GCP Syndic Maroc - Confirmation de réception";
        
        $client_content = "Bonjour $name,\n\n";
        $client_content .= "Nous avons bien reçu votre message et nous vous en remercions.\n";
        $client_content .= "Notre équipe traitera votre demande dans les plus brefs délais et vous contactera très prochainement.\n\n";
        $client_content .= "Rappel de votre message :\n";
        $client_content .= "--------------------------------------------------\n";
        $client_content .= "$message\n";
        $client_content .= "--------------------------------------------------\n\n";
        $client_content .= "Cordialement,\n";
        $client_content .= "L'équipe GCP Syndic Maroc\n";
        $client_content .= "Téléphone: +212 6 62 08 17 84\n";
        $client_content .= "Email: contact@gcp.ma\n";

        $client_headers = "From: GCP Syndic Maroc <contact@gcp.ma>\r\n";
        $client_headers .= "Reply-To: contact@gcp.ma\r\n";
        $client_headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

        // Send the auto-reply
        mail($email, $client_subject, $client_content, $client_headers);

        http_response_code(200);
        echo json_encode(["status" => "success"]);
    } else {
        http_response_code(500);
        echo json_encode(["status" => "error", "message" => "Une erreur s'est produite."]);
    }

} else {
    // Not a POST request
    http_response_code(403);
    echo json_encode(["status" => "error", "message" => "Méthode non autorisée."]);
}
?>
