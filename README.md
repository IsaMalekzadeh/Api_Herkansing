# Sport Team Management API

 Welkom bij mijn Sport Team Management API! Dit project biedt een backend- en frontendoplossing voor het beheren van sportteams en gebruikers. De applicatie is gebouwd met FastAPI voor de backend en een eenvoudige HTML/CSS/JavaScript frontend, en stelt gebruikers in staat om CRUD-bewerkingen (maken, lezen, bijwerken en verwijderen) uit te voeren op sportteams en gebruikers.
Projectoverzicht

De Sport Team Management API is ontworpen om gebruikers te helpen bij het effectief beheren van sportteams. De applicatie biedt functies voor het aanmaken, lezen, bijwerken en verwijderen van teams en gebruikers. Bovendien biedt de API-eindpunten voor gebruikersauthenticatie, waardoor een veilige toegang tot het systeem wordt gegarandeerd.
Belangrijkste Kenmerken

Gebruikersbeheer: Maak nieuwe gebruikers aan, bekijk gebruikersdetails en verifieer gebruikers met JWT-tokens.
Teambeheer: Maak, lees, werk bij en verwijder teams. Teams zijn georganiseerd op basis van stad, zodat je teams kunt ophalen op basis van hun locatie.
Frontend-interface: Een gebruiksvriendelijke webinterface gebouwd met HTML, CSS en JavaScript om te communiceren met de API-eindpunten.

## Technologie Stack

Backend: FastAPI, SQLAlchemy, SQLite
Frontend: HTML, CSS, JavaScript
Containerisatie: Docker

### Aan de Slag
Volg de onderstaande stappen om aan de slag te gaan met dit project:


## POST (Het maken van een team.)
Hiervoor gebruik je de POST enpoint /teams.
Het team dat gemaakt is heet "Redstrike" in de stad "Hasselt"
![img.png](img.png)

## GET (Het bekijken van een specifiek team)
Hiervoor gebruik je de GET endpoint /teams/{team_id}.
Voor het voorbeeld zullen we het team pakken met id 5.
![img_1.png](img_1.png)

## GET (Het bekijken van alle teams die gemaakt zijn)
Hiervoor gebruik je de GET endpoint /teams
![img_2.png](img_2.png)

## GET (Het bekijken van een team(s) in een bepaalde stad)
Hiervoor gebruik je de GET endpoint /teams/by_city. Voor het voorbeeld zullen we "Geel" en "Genk" pakken

### Geel
![img_3.png](img_3.png)

### Genk
![img_4.png](img_4.png)

## PUT (Een team bijwerken)
Hiervoor gebruik je de PUT endpoint /teams/{team_id}. Voor het voorbeeld zullen we 
"Blue strike" uit "Brussel" nemen en de daam verranderen naar "BXL Strik".
![img_5.png](img_5.png)

Als je nu een GET request voor team 3 vraagt krijg je het volgende.
![img_6.png](img_6.png)

## DELETE (Een team verwijderen)
Hiervoor gebruik je de DELETE endpoint /teams/{team_id}. Voor het voorbeeld zullen we "Red Strike" uit "Hasselt"
verwijderen.
![img_7.png](img_7.png)

Als je nu een GET request doet voor alle teams zul je "Red Strike" niet terug kunnen vinden.
![img_8.png](img_8.png)

## POST (User aanmaken)
Hiervoor gebruik je de POST endpoint /users voor. In het voorbeeld gebruik ik mijn eigen naamn (Isa Malekzadeh)
![img_9.png](img_9.png)

### momenteel ben ik nog niet geauthenticeerd.
Dit kan ik zien als ik de GET endpoint /users/me gebruik.
![img_10.png](img_10.png)

## POST (Token maken)
maar als ik een token aanvraag kan ik wel geauthenticeerd worden.
![img_11.png](img_11.png)
![img_12.png](img_12.png)
![img_13.png](img_13.png)
