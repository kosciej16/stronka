#  
First launch:
    Make sure you have docker and postgres installed.
    Open terminal:
    Type:
    docker run --name postgres-db -e POSTGRES_PASSWORD=password -p 25432:5432 -d postgres
Second launch:
    Open terminal:
    Type:
    docker start postgres-db

To open database:
    Open terminal:
    Type:
    psql -h 127.0.0.1 -p 25432 postgres postgres
        (-h hostname, -p port)
