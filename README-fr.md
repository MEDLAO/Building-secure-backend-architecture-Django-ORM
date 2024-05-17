## Projet : Développez une architecture back-end sécurisée en utilisant Django ORM

[**English**](README.md)
<p>
  <img src="pictures/.png" />
</p>

### Tables des matières :
1. Description générale du projet/Scénario.
2. Configurations compatibles.
3. Installation du programme.
4. Fonctionnalités.
5. Authentification et permissions.
6. Démarrage du programme.
7. Gestion des utilsateurs via Django Admin Site.

## 1. Descripton générale du projet/Scénario :

Ce projet a été réalisé dans le cadre de la formation de
développeur Python proposée par OpenClassrooms. 

Epic Events, une entreprise de conseil et de gestion d'événements réputée pour ses "fêtes épiques", est confrontée à 
une situation urgente suite à une cyberattaque sur le fournisseur externe auquel nous faisions appel pour notre CRM. 
Cette attaque compromettant l'intégrité de certaines informations clients, il est impératif d'agir rapidement 
pour restaurer la confiance de notre clientèle.

Afin de faire face à ce défi de manière proactive, Epic Events a pris la décision de développer en interne
un système CRM sécurisé. Cette initiative vise à rassurer nos clients quant à la sécurité de leurs données
et à démontrer notre engagement envers la gestion professionnelle de leurs événements.

Pour mener à bien ce projet, il m’a été confié la conception de la première version du CRM. 
Cette solution sur mesure répondra aux besoins spécifiques de notre entreprise 
et contribuera à consolider notre réputation en tant que prestataire de choix pour des événements d'exception. 


## 2. Configurations compatibles :

* Python 3
* Windows 10
* MacOS
* Linux

## 3. Installation du programme :
Ce programme utilise les librairies Python suivantes :

```
asgiref 3.7.2
backports.zoneinfo 0.2.1
certifi 2023.5.7
cffi 1.15.1
charset-normalizer 3.2.0
cryptography 41.0.2
defusedxml 0.7.1
Django 4.2.2
django-allauth 0.54.0
django-phonenumber-field 7.1.0
django-rest-auth 0.9.5
django-rest-authtoken 2.1.4
djangorestframework 3.14.0
djangorestframework-simplejwt 5.2.2
idna 3.4
oauthlib 3.2.2
phonenumbers 8.13.15
psycopg2-binary 2.9.6
pycparser 2.21
PyJWT 2.7.0
python3-openid 3.2.0
pytz 2023.3
requests 2.31.0
requests-oauthlib 1.3.1
six 1.16.0
sqlparse 0.4.4
typing_extensions 4.7.0
urllib3 1.26.6

```

## 4. Fonctionnalités :

### Accès aux différentes données via les  points de terminaison qui sont répartis en quatre catégories : 

  * Authentification
  * Équipes-Employés
  * Clients-Contrats
  * Contrats-Événements

  Pour une explication détaillée de l'API et de ses "endpoints",
  consulter la [**documentation**](https://documenter.getpostman.com/view/25420128/2s946cfDj2).

## 5. Authentification et permissions :
    
  * L'**authentification** pour le back-end est assurée par **Django Rest Authentication**.
  * Pour la partie **autorisation** et **accès**, plusieurs **permissions** ont été mises en place selon le statut de
l'utilisateur effectuant la requête et conformément au cahier des charges.

## 6. Démarrage du programme :

1. Ouvrir un terminal (ex: Cygwin pour Windows, le terminal pour MacOS) ou dans un IDE (ex: PyCharm).
2. Cloner le repository dans un répertoire local :
  > $<b> git clone repository path</b> 
3. Se placer dans ce dossier sur le terminal.
4. Créer un environnement virtuel avec :
  > $<b> python -m venv <nom de l'environnement></b> 
5. Activer l'environnement virtuel en éxécutant :
  > $ <b>source env/bin/activate</b>  (sur MacOS et Linux) 

  > $ <b>env\Scripts\activate.bat</b> (sur Windows)
6. Installer les paquets présents dans le fichier requirements.txt (ce fichier se trouve dans le dossier du projet) avec :
  > $ <b>pip install -r requirements.txt</b> 
7. Finalement, exécuter le serveur de développement avec :
> $ <b>python manage.py runserver</b>
8. Consulter le site à l'adresse suivante et accéder aux différents endpoints :

      **http://127.0.0.1:8000/**

## 7. Gestion des utilisateurs via Django Admin Site :

1. Créer un Super User avec la commande suivante :
 > $ <b>python manage.py createsuperuser </b> 
2. Se connecter avec cet utilisateur à cette adresse :
 **http://127.0.0.1:8000/admin/**
3. Seul ce Super User aura un accès complet à l'application et aux différentes opérations C.R.U.D .
Il pourra, lors de la création d'un nouvel utilisateur le placer dans l'un des trois groupes de permissions présents :

   * Management-Team
   * Sales-Team
   * Support-Team
---