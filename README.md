

## Conditions préalables:

Vous devez avoir déjà installé :

- python
- pip
- virtualenv

## Mise en place du projet

1. Décompressez le fichier
2. Allez dans le dossier du projet et installez un dossier d'environnement virtuel : 
```
virtualenv .venv
```

3. Activez l'environnement virtuel :
```
source .venv/bin/activate (linux)
.venv\Scripts\activate.bat (windows)
```

4. Installez toutes les bibliothèques et extensions requises pour ce projet. Toutes les dépendances sont répertoriées dans le fichier requirements.txt. Exécutez la commande ci-dessous pour les installer tous en une seule commande (windows ou linux) :

```
pip install -r requirements.txt
```


Le dossier de modèles (**models**) contient le modèle de tables de base de données (tables.py) et les objets Web Forms (forms.py).

Le dossier '**static**' est utilisé pour stocker les fichiers statiques couramment utilisés dans le front-end, tels que les fichiers CSS, les fichiers JS, les polices, les images, les vidéos, etc.

Le dossier '**templates**' contient tous les modèles utilisés pour rendre les écrans d'application. En particulier, base.html est un modèle utilisé comme base pour les autres modèles.

En dehors du dossier **app**, il y a le dossier tests, où nous conservons tous les fichiers de test. Nous exécutons ces tests via la commande "pytest tests". En plus du dossier tests, nous avons les fichiers run.py, qui est le premier fichier exécuté dans l'application, config.py, qui stocke les données de configuration de l'application, et populate_db.py. Ce dernier est un script spécial qui nous aide à créer des données dans la base de données pour tester l'application.

