#  

First launch:
python3 -m venv  -  virtual enviroment for your requirements and stuff
    docker run --name postgres-db -e POSTGRES_PASSWORD=password -p 25432:5432 -d postgres
    python3 -m venv .venv
    pip install -r requirements.txt
    python app.py
Second launch:
    docker start postgres-db
    python app.py

To open database:
    psql -h 127.0.0.1 -p 25432 postgres postgres
        (-h hostname, -p port)