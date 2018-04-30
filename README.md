## Industry Price Quote Model

This project cleans and loads a couple of text (csv) 
files to a postgres database.

*Read this in other languages: [English](README.md), [Portuguese Brazil](README.ptbr.md)

### Installation (dev only):

1) Create a virtualenv with python 3.5;
1) Add the .csv files to the 'data' directory;
1) Install requirements:
```
pip install -r requirements.txt
```

### Executing:

1) Start the sample docker postgres database :
```
make dev-up
```

### Projects directory tree:

- data/: Source csv file;
- db/: Database design and docker configuration;
- dw/: ETL for data warehouse tables;
- util/: Other util functions;