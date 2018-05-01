## Industry Price Quote Model

This project cleans and loads a couple of text (csv) 
files to a postgres database.

*Read this in other languages: [Brazilian Portuguese](README.ptbr.md).*

### Installation (dev only):

1) Create a virtualenv with python 3.5;
1) Add the .csv files to the 'data' directory;
1) Install requirements:
_Important: Run the following on the project directory!_
```
pip install -r requirements.txt
```

### Executing:
 
1) Start a docker postgres with all the tables create (but empty);
1) Start the python process (don't forget to check if the data folder has all csv files) \
_Important: Run the following on the project directory!_
```
make db-up
make run
```

### Projects directory tree:

- data/: Source csv file;
- db/: Database design and docker configuration;
- dw/: ETL for data warehouse tables;
- util/: Other util functions;

### DB Model:

(db/model.png)
- component_dimension: 
	- Contain all the data from comp_boss.csv. All boolean colums converted to 1 or 0;
	- All N/A values were kept with the same string;
	- All strings are upper cased;
- tube_assembly_dimension:
	- Contains bill_of_materials info;
	- Columns were unpivoted to remove N/A values and simplify future aggregations;
- price_quote:
	- Contain price quote info;
	- Has another bonus/sample table 'annual_cost', applying the cost calculation.
	
### To do:
This section contains possible improvements to this project:
- Add to a pipeline framework (e.g: luigi, apache airflow);
- Create unit and integrated tests;
- Create CD scripts to build and push the docker image to docker hub;
- Automated deploy in case of multiple executions;
