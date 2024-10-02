# Description

**correlation_analysis** est un package Python destiné à l'analyse de corrélations entre variables dans des ensembles de données. Il fournit des outils pour tester la normalité des données, évaluer la linéarité, détecter les déséquilibres et les valeurs aberrantes, ainsi que pour calculer et visualiser les coefficients de corrélation.

# Fonctionnalités

- **Test de normalité** avec la méthode de Shapiro-Wilk.
- **Test de linéarité** à l'aide de Durbin-Watson.
- **Test de non-linéarité** avec le test RESET de Ramsey.
- **Détection de déséquilibres** et de valeurs aberrantes dans les variables.
- Choix automatique de la méthode de corrélation (Pearson, Spearman, Kendall) selon la distribution des données.
- Visualisation des relations entre variables avec des graphiques.

# Installation

Pour installer le package, utilisez `pip` :

```bash
pip install correlation_analysis
```

# Utilisation

```
import pandas as pd
from correlation_analysis import correlation_analysis as ca

# Chargement d'un DataFrame
df = pd.read_csv('votre_fichier.csv')

# Analyser la corrélation entre deux variables
correlation, method = ca.analyser_correlation(df, 'var1', 'var2')

print(f"Corrélation entre var1 et var2 : {correlation} (Méthode : {method})")

```

# Tests

```
pytest tests/

```

Pour exécuter les tests unitaires, assurez-vous d'avoir `pytest` installé et exécutez :

# Contribuer

Les contributions sont les bienvenues ! Veuillez suivre ces étapes :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/YourFeature`)
3. Faites vos modifications et validez (`git commit -m 'Add some feature'`)
4. Poussez vers la branche (`git push origin feature/YourFeature`)
5. Ouvrez une pull request

# License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

# Auteurs

CHABI ADJOBO AYEDESSO

aurelus.chabi@gmail.com
