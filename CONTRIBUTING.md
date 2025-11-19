# Contribuer au site

Merci de votre intérêt pour contribuer au site du Dr Jérôme Palazzolo !

## Comment contribuer

### Signaler un problème

Si vous trouvez un bug ou avez une suggestion :
1. Vérifiez que le problème n'a pas déjà été signalé dans les [Issues](https://github.com/antoine-palazz/site-dr-palazzolo/issues)
2. Créez une nouvelle issue avec une description détaillée
3. Incluez des captures d'écran si pertinent

### Proposer des changements

1. **Fork** le dépôt
2. **Clone** votre fork localement
3. Créez une **branche** pour vos modifications : `git checkout -b feature/ma-contribution`
4. Faites vos modifications
5. **Testez** localement (voir ci-dessous)
6. **Commit** avec des messages clairs
7. **Push** vers votre fork
8. Créez une **Pull Request**

## Configuration de l'environnement

### Prérequis

- **Quarto** >= 1.3.450 ([Installation](https://quarto.org/docs/get-started/))
- **Python** >= 3.10
- **Git**

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
```

## Tester localement

### Prévisualisation complète

```bash
# Utilisateurs standard
quarto preview

# Utilisateurs SSP Cloud
quarto preview --port 5000 --host 0.0.0.0
```

### Construire le site

```bash
quarto render
```

### Tester un fichier spécifique

Pour modifier uniquement certains fichiers pendant le développement :
- Éditez la section `render` dans `_quarto.yml`
- Gardez seulement les fichiers que vous testez
- **Important**: Restaurez `_quarto.yml` avant de faire votre PR !

### Vérifier les liens

```bash
python build/checkurl.py
```

## Structure du projet

```
site-dr-palazzolo/
├── content/              # Contenu du site
│   ├── le_docteur/      # Informations sur le docteur
│   ├── livres/          # Pages des livres
│   ├── publications_communications/
│   └── autres_activites/
├── img/                 # Images
├── scss/                # Styles SCSS modulaires
├── _quarto.yml         # Configuration principale
├── index.qmd           # Page d'accueil
└── docs/               # Documentation supplémentaire
```

## Guide de style

### Code
- **Python**: Suivre PEP 8, utiliser black pour le formatage
- **YAML**: 2 espaces d'indentation
- **Markdown**: Utiliser les conventions Quarto

### Commits
Format recommandé :
```
type: Description courte

Description détaillée si nécessaire
```

Types : `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Exemples :
- `feat: Ajouter page pour nouveau livre`
- `fix: Corriger lien cassé dans CV`
- `docs: Mettre à jour guide de contribution`

### Contenu
- Vérifier l'orthographe et la grammaire
- Optimiser les images avant de les ajouter
- Tester sur mobile et desktop
- Respecter la structure existante

## Ajouter du contenu

Consultez le [Guide de contenu](docs/CONTENT_GUIDE.md) pour :
- Ajouter un nouveau livre
- Modifier les informations du docteur
- Ajouter des publications

## Déploiement

Le site est automatiquement déployé via GitHub Actions lors d'un push sur `main`.

Voir [DEPLOYMENT.md](docs/DEPLOYMENT.md) pour plus de détails.

## Questions et support

- 📖 Consultez d'abord la [documentation](docs/)
- 💬 Ouvrez une [Discussion](https://github.com/antoine-palazz/site-dr-palazzolo/discussions)
- 🐛 Signalez les bugs via [Issues](https://github.com/antoine-palazz/site-dr-palazzolo/issues)

## Code de conduite

Soyez respectueux et professionnel dans toutes les interactions.

## Licence

En contribuant, vous acceptez que vos contributions soient sous [Licence MIT](LICENSE).
