# Site du Dr Jérôme Palazzolo

[![Deploy Status](https://github.com/antoine-palazz/site-dr-palazzolo/actions/workflows/deploy.yml/badge.svg)](https://github.com/antoine-palazz/site-dr-palazzolo/actions/workflows/deploy.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Site officiel du Dr Jérôme Palazzolo, psychiatre, psychothérapeute et professeur.

🌐 **[www.docteurjeromepalazzolo.fr](https://www.docteurjeromepalazzolo.fr/)**

## 📖 À propos

Ce site présente :
- Les livres publiés par le Dr Palazzolo
- Biographie et CV détaillés
- Publications scientifiques et communications
- Informations de consultation
- Activités d'enseignement et de recherche

## 🚀 Démarrage rapide

### Prérequis

- [Quarto](https://quarto.org/docs/get-started/) >= 1.3.450
- [Python](https://www.python.org/downloads/) >= 3.10
- Git

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/antoine-palazz/site-dr-palazzolo.git
cd site-dr-palazzolo

# Installer les dépendances Python
pip install -r requirements.txt

# Installer les extensions Quarto
chmod +x requirements.sh
./requirements.sh

# Prévisualiser le site
quarto preview
```

Le site sera accessible à l'adresse : http://localhost:4200

## 🏗️ Structure du projet

```
site-dr-palazzolo/
├── content/                    # Contenu du site
│   ├── le_docteur/            # Informations sur le docteur
│   ├── livres/                # Pages des livres (74 fichiers)
│   ├── publications_communications/  # Publications académiques
│   └── autres_activites/      # Autres activités
├── img/                       # Images (couvertures, photos)
├── scss/                      # Styles SCSS modulaires
│   ├── _variables.scss
│   ├── _buttons.scss
│   ├── _responsive.scss
│   └── ...
├── docs/                      # Documentation
│   ├── DEPLOYMENT.md
│   └── CONTENT_GUIDE.md
├── .github/
│   └── workflows/            # CI/CD avec GitHub Actions
├── _quarto.yml               # Configuration Quarto
├── index.qmd                 # Page d'accueil
└── README.md                 # Ce fichier
```

## 📚 Documentation

- **[Guide de contribution](CONTRIBUTING.md)** - Comment contribuer au projet
- **[Guide de contenu](docs/CONTENT_GUIDE.md)** - Ajouter/modifier du contenu
- **[Guide de déploiement](docs/DEPLOYMENT.md)** - Déployer le site
- **[Changelog](CHANGELOG.md)** - Historique des versions

## 🛠️ Technologies utilisées

- **[Quarto](https://quarto.org/)** - Framework de publication scientifique
- **Python** - Scripts et dépendances
- **SCSS** - Styles modulaires
- **GitHub Actions** - CI/CD automatisé
- **GitHub Pages** - Hébergement

## ✨ Fonctionnalités

### Frontend
- ✅ Design responsive (mobile, tablette, desktop)
- ✅ Recherche intégrée
- ✅ Navigation optimisée
- ✅ Mode sombre/clair
- ✅ Lightbox pour les images
- ✅ Animations GPU-accélérées
- ✅ Support préférence de mouvement réduit

### Analytics & Tracking
- ✅ Google Analytics (G-JWQSW5E8BY)
- ✅ Consentement aux cookies (RGPD)
- ✅ Intégration réseaux sociaux

### Accessibilité
- ✅ Navigation clavier complète
- ✅ Indicateurs de focus visibles
- ✅ Support lecteurs d'écran
- ✅ Contraste optimisé
- ✅ Skip-to-content link

### SEO
- ✅ Meta tags optimisés
- ✅ Twitter Cards
- ✅ Sitemap automatique
- ✅ robots.txt configuré
- ✅ URLs canoniques

## 🤝 Contribuer

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

### Processus de contribution

1. Fork le projet
2. Créez une branche (`git checkout -b feature/amelioration`)
3. Committez vos changements (`git commit -m 'feat: Ajouter une amélioration'`)
4. Pushez vers la branche (`git push origin feature/amelioration`)
5. Ouvrez une Pull Request

### Outils de développement

- **Pre-commit hooks** : `pip install pre-commit && pre-commit install`
- **Black formatting** : Automatique dans VSCode
- **Linting** : Flake8 configuré
- **Extensions VSCode** : Voir `.vscode/extensions.json`

## 📝 Licence

Ce projet est sous licence [MIT](LICENSE).

## 🔒 Sécurité

Pour signaler une vulnérabilité, consultez [SECURITY.md](.github/SECURITY.md).

## 👨‍💻 Développeur

Site développé par **[Antoine Palazzolo](https://www.linkedin.com/in/antoine-palazzolo/)**, inspiré du site de [Lino Galiana](https://github.com/linogaliana/python-datascientist).

## 📧 Contact

Pour toute question ou demande de rendez-vous :
- 📞 Secrétariat : 06 61 02 95 08
- 📍 Cabinet : 5 Quai des Deux Emmanuel, 06300 Nice
- 🌐 Site web : [docteurjeromepalazzolo.fr](https://www.docteurjeromepalazzolo.fr/)

## 🔗 Liens utiles

- [LinkedIn](https://www.linkedin.com/in/jerome-palazzolo/)
- [Facebook](https://www.facebook.com/DrPalazzolo/)
- [Instagram](https://www.instagram.com/palazz06/)
- [YouTube](https://www.youtube.com/channel/UCMF4Vhgt6gOYQaiE2jlKoHw)
- [X (Twitter)](https://twitter.com/palazz06)

---

⭐ Si vous trouvez ce projet utile, n'hésitez pas à lui donner une étoile !
