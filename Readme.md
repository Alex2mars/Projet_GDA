# Projet Informatique/Sécurité - GDA

## Création d'un docker PostgreSQL

Dossier **docker_postgres** du Git :
- build_image : Dossier contenant les fichiers nécessaires au build de l'image docker.
  - Lancer ./build.sh pour :
    1) Build l'image
    2) La sauvegarder dans le dossier **deployment**

- deployment : Dossier contenant le nécessaire pour déployer le docker
  - Lancer ./run.sh **la première fois**, ce qui va :
    1) Charger l'image dans docker
    2) Lancer *docker-compose -d up*, pour lancer le service et le passer en arrière plan
   
  - Par la suite, gérer le service avec *docker-compose*:
    - *docker-compose -d up* pour lancer le service s'il est éteint
    - *docker-compose down* pour arrêter le service s'il est lancé

Pour générer correctement le dossier **deployment**, lancer *build_image/build.sh* pour générer l'image et la charger dans le dossier de déploiement. (Github n'autorise pas un fichier >100 MB, l'image en fait +300MB, d'où la nécessité de regénérer l'image)
