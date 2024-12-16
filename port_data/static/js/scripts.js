/*!
* Start Bootstrap - Personal v1.0.1 (https://startbootstrap.com/template-overviews/personal)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-personal/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// Attend que la page soit complètement chargée
document.addEventListener('DOMContentLoaded', function() {
    // Exemple : Ajouter une classe 'active' aux liens du menu quand on clique dessus
    const menuLinks = document.querySelectorAll('nav a');
    menuLinks.forEach(link => {
        link.addEventListener('click', function() {
            menuLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Exemple : Gérer les formulaires
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            alert('Formulaire soumis !');
            // Ici vous pourrez ajouter votre logique de traitement du formulaire
        });
    });
});