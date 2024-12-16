document.addEventListener('DOMContentLoaded', function() {
    // Animation du titre
    const textGradient = document.querySelector('.text-gradient');
    if (textGradient) {
        textGradient.style.backgroundSize = '200% auto';
        textGradient.style.animation = 'gradient 3s linear infinite';
    }

    // Animation de la carte d'article
    const articleCard = document.querySelector('.card');
    if (articleCard) {
        // Animation initiale
        articleCard.style.opacity = '0';
        articleCard.style.transform = 'translateY(20px)';
        
        // Animation d'entrée
        setTimeout(() => {
            articleCard.style.opacity = '1';
            articleCard.style.transform = 'translateY(0)';
        }, 300);

        // Effet au survol
        articleCard.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });

        articleCard.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    }

    // Animation du lien "Voir plus"
    const linkArticle = document.querySelector('.linku-projects1');
    if (linkArticle) {
        linkArticle.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(10px)';
        });

        linkArticle.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
        });
    }

    // Gestion de l'image
    const articleImage = document.querySelector('.img-fluid');
    if (articleImage) {
        articleImage.addEventListener('load', function() {
            this.style.opacity = '1';
        });
        
        articleImage.style.opacity = '0';
        articleImage.style.transition = 'opacity 0.5s ease';
    }
});

// Ajout des styles CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .text-gradient {
        background: linear-gradient(45deg, #007bff, #6610f2, #6f42c1);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        background-size: 200% auto;
    }

    .card {
        transition: all 0.3s ease;
    }

    .linku-projects1 {
        display: inline-block;
        color: #007bff;
        text-decoration: none;
        transition: all 0.3s ease;
        padding: 5px 0;
        position: relative;
    }

    .linku-projects1:after {
        content: '';
        position: absolute;
        width: 100%;
        height: 2px;
        bottom: 0;
        left: 0;
        background-color: #007bff;
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }

    .linku-projects1:hover:after {
        transform: scaleX(1);
    }

    .img-fluid {
        transition: transform 0.3s ease;
    }

    .img-fluid:hover {
        transform: scale(1.05);
    }
`;
document.head.appendChild(style);