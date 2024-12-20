document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitButton = document.getElementById('submitButton');
    const successMessage = document.getElementById('submitSuccessMessage');
    const errorMessage = document.getElementById('submitErrorMessage');

    // Animation de l'icône d'enveloppe
    const envelopeIcon = document.querySelector('.bi-envelope');
    if (envelopeIcon) {
        envelopeIcon.parentElement.addEventListener('mouseenter', function() {
            envelopeIcon.style.transform = 'scale(1.2) rotate(15deg)';
        });
        
        envelopeIcon.parentElement.addEventListener('mouseleave', function() {
            envelopeIcon.style.transform = 'scale(1) rotate(0)';
        });
    }

    // Fonction de validation d'email
    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    // Fonction de validation de numéro de téléphone
    function isValidPhone(phone) {
        return /^[\d\s()-+]{8,}$/.test(phone);
    }

    // Gérer la validation en temps réel des champs
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('input', function() {
            validateField(this);
            checkFormValidity();
        });

        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
            validateField(this);
        });
    });

    // Valider un champ spécifique
    function validateField(field) {
        const feedback = field.parentElement.querySelector('.invalid-feedback');
        let isValid = true;

        if (field.hasAttribute('data-sb-validations')) {
            const validations = field.getAttribute('data-sb-validations').split(',');

            if (validations.includes('required') && !field.value.trim()) {
                isValid = false;
            }

            if (field.type === 'email' && validations.includes('email') && !isValidEmail(field.value)) {
                isValid = false;
            }

            if (field.type === 'tel' && !isValidPhone(field.value)) {
                isValid = false;
            }
        }

        if (!isValid) {
            field.classList.add('is-invalid');
            field.classList.remove('is-valid');
            if (feedback) feedback.style.display = 'block';
        } else {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
            if (feedback) feedback.style.display = 'none';
        }

        return isValid;
    }

    // Vérifier la validité du formulaire complet
    function checkFormValidity() {
        let isValid = true;
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });

        if (isValid) {
            submitButton.classList.remove('disabled');
        } else {
            submitButton.classList.add('disabled');
        }
    }

    // Gérer la soumission du formulaire
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            // Simulation d'envoi (à remplacer par votre logique d'envoi réelle)
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            successMessage.classList.remove('d-none');
            errorMessage.classList.add('d-none');
            form.reset();
            inputs.forEach(input => {
                input.classList.remove('is-valid');
            });
            submitButton.classList.add('disabled');
        } catch (error) {
            errorMessage.classList.remove('d-none');
            successMessage.classList.add('d-none');
        }
    });
});

// Ajout des styles CSS
const style = document.createElement('style');
style.textContent = `
    .form-floating {
        position: relative;
        transition: all 0.3s ease;
    }

    .form-control {
        transition: all 0.3s ease;
    }

    .form-floating.focused .form-control {
        border-color: #0d6efd;
        box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
    }

    .btn-primary {
        transition: all 0.3s ease;
    }

    .btn-primary:not(.disabled):hover {
        transform: translateY(-2px);
    }

    .bi-envelope {
        transition: all 0.3s ease;
    }

    .invalid-feedback {
        display: none;
        font-size: 0.875em;
        color: #dc3545;
    }

    .form-control.is-invalid {
        border-color: #dc3545;
        padding-right: calc(1.5em + 0.75rem);
        background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
        background-repeat: no-repeat;
        background-position: right calc(0.375em + 0.1875rem) center;
        background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
    }

    .form-control.is-valid {
        border-color: #198754;
        padding-right: calc(1.5em + 0.75rem);
        background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
        background-repeat: no-repeat;
        background-position: right calc(0.375em + 0.1875rem) center;
        background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
    }
`;
document.head.appendChild(style);