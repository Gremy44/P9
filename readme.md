# Projet P9-LITReview

* Cloner le git dans le repertoire souhaité 
`git clone https://github.com/Gremy44/P9.git`
* Rendez vous dans le repertoire P9 
`cd P9`
* Créer votre environnement virtuel 
`python -m venv p9env`
* Activer l'environnement virtuel
`p9env\Scripts\activate`
* Installer les librairies grâce au fichier 'requirements.txt' avec la commande 
`pip install -r requirements.txt`
* Demarrer le serveur local avec la commande 
`python manage.py runserver`
* Accedez à l'url :
`http://127.0.0.1:8000/`

## Profil d'utilisateurs
Pour pouvoir tester les fonctionnalités de l'application, plusieurs profils utilisateurs éxistent déjà. Vous pouvez vous connecter avec l'un d'eux pour voir les posts qui ont déjà été faits :
>ID : User_1
MDP : User_1

>ID : User_2
MDP : User_2

>ID : User_3
MDP : User_3

>ID : User_4
MDP : User_4

>ID : User_5
MDP : User_5

Il vous est toujours possible de créer votre propre profil d'utilisateur pour naviguer dans l'application.

## Utilisation
Une fois que vous avez démarré le serveur local, vous arriverez sur la page de 'Bienvenue' du site. Vous pourrez soit vous connecter avec un des profils déjà créé ou vous inscrire. Une fois connecté vous arrivez sur la page principal. Un menu de navigation est disponible sous le titre du site. Plusieurs catégories y sont accéssibles : 
* Flux 
* Posts 
* Abonnements
* Déconnexion

#### -Flux
Page principale, affiche les tickets et critiques des personnes que vous suivez et vous-même du plus récent au plus ancien.
#### -Posts
Cette page liste vos tickets et reviews, pour lecture, modification ou suppression.
#### -Abonnements
Cette page liste les personnes que vous suivez avec la possibilité d'en suivre des nouvelles ou de vous désabonner à celle que vous suivez déjà.
#### -Déconnexion
Se déconnecte de votre profile et vous renvoi sur la page de déconnexion.

## Rapport Flake8
Un rapport des directives Flake8 est présent dans le dossier. 
Si vous souhaitez tester vous-même si les scripts suivent les directives pep8, vous pouvez générer votre propre rapport en utilisant cette ligne de code :
`flake8 --format=html --htmldir=flake-report`
