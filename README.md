# GIB2
Denne applikasjonen setter opp et kart for arrangement i Trondheim

Lag et python virtuelt miljø (virtualenv), med navn venv og plassert i prosjektmappen.

Naviger til prosjektmappen og kjør
```bash
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

for å aktivere venv.
```source venv/bin/activate ``` 

for å starte server, installer postgresql med følgende verdier
``` 
user = postgres
password = password
databasename = postgres
port = 5432
host = localhost
```
Installer postgis extension til postgresql server
når installert, gå til serveren, høyreklikk og velg query tools og kjør
````
create extension postgis;
````

set System variables
``` 
APP_SETTINGS="config.DevelopmentConfig"
DATABASE_URL="postgresql://localhost/beacons"

```
Hvordan jobbe med dette inntil videre for Mons, Jakob og Sigrid:
```
git checkout frontMons
git pull
git checkout -b <tasknavn>
```
Når ferdig med tasken og du vet at det fungerer
```
git add .
git commit -m "Beskrivelse av task"
git push --set-upstream origin <tasknavn>

git checkout frontMons
git pull origin <tasknavn>
git add . 
git commit -m "tasknavn"
git push
```
