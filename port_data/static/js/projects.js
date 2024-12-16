// Attend que le DOM soit chargé
document.addEventListener('DOMContentLoaded', function() {
    // Animation des cartes de projets lors du défilement
    const projectCards = document.querySelectorAll('.card');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    projectCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = 'all 0.5s ease-out';
        observer.observe(card);
    });

    // Animation du texte gradient
    const textGradient = document.querySelector('.text-gradient');
    if (textGradient) {
        textGradient.style.backgroundSize = '200% auto';
        textGradient.style.animation = 'gradient 3s linear infinite';
    }

    // Ajout d'effets hover sur les boutons
    const projectButtons = document.querySelectorAll('.btn-outline-primary, .btn-outline-secondary');
    projectButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.transition = 'transform 0.2s ease';
        });

        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // Gestion du chargement des images
    const projectImages = document.querySelectorAll('.img-fluid');
    projectImages.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        
        img.style.opacity = '0';
        img.style.transition = 'opacity 0.5s ease';
    });

    // Animation de la section Call to Action
    const ctaSection = document.querySelector('.bg-gradient-primary-to-secondary');
    if (ctaSection) {
        window.addEventListener('scroll', () => {
            const rect = ctaSection.getBoundingClientRect();
            const isVisible = rect.top < window.innerHeight && rect.bottom >= 0;
            
            if (isVisible) {
                ctaSection.style.transform = 'scale(1)';
                ctaSection.style.opacity = '1';
            }
        });
        
        ctaSection.style.opacity = '0';
        ctaSection.style.transform = 'scale(0.95)';
        ctaSection.style.transition = 'all 0.5s ease';
    }
});

// Ajouter les styles CSS nécessaires
const style = document.createElement('style');
style.textContent = `
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }

    .btn {
        transition: all 0.3s ease;
    }

    .text-gradient {
        background: linear-gradient(45deg, #007bff, #6610f2, #6f42c1);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        background-size: 200% auto;
    }
`;
document.head.appendChild(style);