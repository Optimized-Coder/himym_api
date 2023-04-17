# HOW I MET YOUR MOTHER API

This is a simple API, written with Flask and Python with information about my favourite TV show during my early 20s, How I Met your Mother, inspired by the Breaking Bad API.

## Schemas
---
### Character
| Column | Datatype | Example |
|:------:|:--------:|:-------:|
|    id [PK]   |   Integer  |    1    |
|    name      |   String   |Ted Mosby|
|   full_name  |    String  |    1    |
| portrayed_by |    String  | Josh Radnor |
| home_town    |    String  | Shaker Heights, Ohio |
| date_of_birth|     Date   | 24/04/1978 |
| occupation   |    String  |    Architect    |
---
### Episode
| Column | Datatype | Example |
|:------:|:--------:|:-------:|
|    id [PK]   |   Integer  |    1    |
|    season_number      |   Integer   | 1 (s01) |
|   episode_number  |    Integer  |    1  (s01)|
| first_aired |    Date  | 19/09/2005 |
| director    |    String  | Pamela Fryman  |
| episode_name|     String   | Barney's Bet |
---

## Endpoints:
### GET
http://localhost:5000/api/characters/

> This will send a GET request to fetch a json object for all the characters

http://localhost:5000/api/characters/id/

> This takes in a number and will return the json for the character with the id provided

http://localhost:5000/api/episodes/

> This will send a GET request to fetch a json object for all the episodes

http://localhost:5000/api/episodes/id/

> This takes in a number and will return the json for the episode with the id provided

### Delete

http://localhost:5000/api/characters/id/delete

> This will send a DELETE request to the server to remove a character from the database

http://localhost:5000/api/characters/id/delete

> This will send a DELETE request to the server to remove an episode from the database
