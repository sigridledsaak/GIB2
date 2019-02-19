# GIB2
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