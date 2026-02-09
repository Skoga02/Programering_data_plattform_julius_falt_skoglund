# Worshop lecture


## Basics 
- 1. Vad gör FastAPI?
* FastApi är ett pythonramverk för att bygga API:er. API är en uppsättning me URL:er som låter en mjukvarudel prata med en annan. Till exempel kan väderappen på din mobil anrop en URL som GET /weather?city=Berlin. Servern svarar med sturkturerad data (oftast JSON), som temperaturer och prognos. 

- 2. Vad gör Pydantic?
* Pydantic är et tpython biblotek som används för datavalidering och inställningar med hjälp av pythons "type hints". Den ser till så att datan som kommer in i vår applikation stämmer övernes med den förväntade strukturen. 

* Pydantic kan även användas till att konvertera data så att den rätta typen. Till exempel "123" till 123.

* Definerar Typer (BaseModel): Du använder standard python-klasser för att definera strukturen på din data.

* Underlättat JSON hantering: Pydantic gör det enkelt att serialisera (göra om till JSON) men även deserialisera (läsa från JSON) komplexa datastrukturer.

* Används i Webbanrop: Pydatnic är standardbiblioteket för datavalidering i moderna webbramverk som FastAPI, där det används för att validera inkommande förfrågningar (requests) och utgående svar (responses).

- 3. Vad gör Psycopg3?
* Högpresterande databasadapter för att koppla Python till PostgreSQL. Den möjliggör exekvering av SQL-queris, stöder asynkron programmering (sync/await) för högra prestanda, erbjuder förbättrad trådsäkerhet och har inbyggt stöd för moderna funktioner som COPY-operationer och typing.


## Trasnaction 

- 1. Vad betyder "Allt eller inget"?
* All or nothing innebär attantingen genomförs  alla steg i en operation - eller så genomförs inga steg alls.

- 2. Vad hände rom något krashar mitt i?
* Utan transaktion 
Om man skulle köra detta manuellt 
```sql
INSERT INTO orders ...
UPDATE accounts SET balance = balance - 500
```

Skulle resultatet bli följande: 
- Order finns i Database
- Pengar drogs inte
- Systemet är nu inkonsistent 

Följderna blir: 
- Rensa manuellet 
- Gissa vad som gick fel 
- Förlorat förtroende 

* Med transaktion 
```sql
BEGIN;
INSERT INTO orders ...
UPDATE accounts SET balance = balance - 500
COMMIT;
```
Om detta skulle krascha innan COMMIT så skulle PostgreSQL rulla tillbaka allt automatiskt. Database förblir exakt likadant som innan. Detta är Atomicity, Consistency och Crash-safe.

- 3. arför är .transaction() viktigare än .commit()?
.commit() betyder i princip, "spara det som redan har hänt". Men den skyddar inte mot halvfärdiga operationer. Gör ingenting om något kraschar innan commit. Vet inte vilka steg som hör ihop.

.transaction() betyder, "De hä rstegen hör ihop. Behandla dem som EN enhet". 
Exempel i psycopg / FastAPI
```python
with conn.transaction():
    insert_order()
    update_balance()
```

Automatisk rolback vid exception. Ingen risk för halv data och mycket tydligare affärslogik.
Med andra ord, använd .transaction()


## Data-types
- 1. Vad är ett python-objekt? 
En struktur i minnet som innehåller data + metoder

Exempel
```python
product = ProductSchema(
    product_id="123",
    name="Coffee",
    price=49.9,
    currency="SEK"
)
```

Detta obejekt lever i python, har typer (str, float), har metadata (Pydantic och validering), finns bara sp länge programmet körs (RAM).

Python-objekt kan vara 
* class instances 
* Dictionaries
* Lists 
* Pydantic-models
* Extremly flexible

- 2. Vad förstår PostgreSQL? 
PostgreSQL förstår sig på SQL SQL och datatyper som:
* TEXT
* INTEGER
* FLOAT
* BOOLEAN 
* JSON / JSONB
* TIMESTAMP

Exemepel som PostgreSQL förstår: 
```sql 
INSERT INTO products_raw (product)
VALUES ('{"name": "Coffee", "price": 49.9}');
```

Detta förstår inte PostgreSQL
```sql 
INSERT INTO products_raw VALUES (ProductSchema(...)) 
```

PostgreSQL kan inte läsa python klasser, kan inte läsa Pydatnic och kan itne heller läsa typer som Union[str, None]

- 3. Varför måste vi "översätta" data?
Data måste översättas för att Python och PostgreSQL lever i olika världar. De kan inte prata direkt med varandra.

Python-världen 
* Objekt 
* Typer
* Klasser 
* Validering 
* Logik 

Databas-världen
* Rader 
* Kolumner
* Strikta typer
* Permanens (lagras på disk)

## Data structure 
- 1. När är JSONB bra?
JSONB är bäst när datan är:
* Ostrukturerad eller halvstrukturerad 
* Föränderlig över tid 
* Inte fullt ut definerad från början 

Typiska use cases
* API-payloads 
* Event data
* Loggar
* Inkommande data från externa system 
* Prototyper / tidiga faser

Fördelar med JSONB
* Kräver inga schemaändringar när nya fält dyker upp 
* Snabb att komma igång med 
* Bevarar orginaldatan exakt som den kom in
* PostgreSQL kan indexera JSONB (!)

- 2. När är kolumner bättre? 
Kolumner är bättre när strukturen är känd, datan är stabil och datan ska analyseras, aggregeras eller joinas.

Fördelar med kolumner 
* Snabbare queries
* Enklare index 
* Datatyper garanteras 
* Lättare att göra 
    * SUM(price)
    * AVG(price)
    * GROUP BY category
* Enklare för BI-verktyg (Power BI, Locker etc)

- 3. Varför har vi "raw tables"? 
Det här är nyckeln till allt i data-plattformar.

En raw table är en tabell som lagrar data exakt som den kom in, utan tolkning eller transformation. 

Detta är viktigt för att:
* Spårbarhet: Du kan alltid gå tillbaka till orginaldatan
* Reproducerbarhet: Om affärslogik ändras -> kör om transforamtioner 
* Felsäkerhet: Bug i appen förstör inte datan 
* Flexibilitet: Nya behov i framtiden kräver inte ny insamling 

## Code & Logic
- 1. Om vi ksickar product; ProductSchema till databasen - vad är det?
ProductSchema är ett python-objekt, mer specifikt en Pydantic-modell som endast lever i Python-världen. 

- 2. Fungerar det att skicka ett Python-objekt direkt till databasen?
Nej det går inte.

PostgreSQL kan inte tollka: Python-ojekt, Pydantic-modeller eller Python-dicts (utan konvetering).
Detta har att göra med att PostgreSQL endast förstår SQL och datatyper. 

- 3. Vad är SQL och vad är parametrar? 

