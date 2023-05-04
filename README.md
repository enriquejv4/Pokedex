# Pokedex
### Postgres' database from pokeapi generated by Python

In this python program we´re scraping the [pokeapi](https://pokeapi.co/) web page.
We're scraping 1010 Json files. Each Json file contains all information for each pokemon.

This Python code will extract selected information for each of these Json files and create a postgres database.

From line 6 to line 16, we're connecting to a postgres' database through hidden.py.
The file hidden.py is a python code that only contains a function with your postgre's database connection info.

```
def secrets(): 
    return {"host": "********",
            "port": ****,
            "database": "*********",
            "user": "*********",
            "pass": "*****"}
```

From lines 18 to 29 we are just defining two help functions.

From lines 31 to 43 we are creating a table with the columns we wish.

Finally, from line 45 a *for loop* fill the database's columns.

We will obtain a postgres' database with 1010 rows:

id | name       | type_1 | type_2 | hp | attack | defense | special_atack | special_defense | speed |
-- | :--------: | :----: | :----: | -- | :----: | :-----: | :-----------: | :-------------: | :---: |
1  | bulbasaur	| grass	 | poison |	45 |	49	| 49	  | 65	          | 65	            | 45    |
2  | ivysaur	| grass	 | poison |	60 |	62	| 63	  | 80	          | 80	            | 60    |
3  | venusaur	| grass	 | poison |	80 |	82	| 83	  | 100	          | 100	            | 80    |
4  | charmander	| fire	 |        | 39 |	52	| 43	  | 60	          | 50	            | 65    |
5  | charmeleon	| fire	 | 	      | 58 |	64	| 58	  | 80	          | 65	            | 80    |
6  | charizard	| fire	 | flying |	78 |	84	| 78	  | 109	          | 85	            | 100   |
7  | squirtle	| water	 | 	      | 44 |	48	| 65	  | 50	          | 64	            | 43    |
8  | wartortle	| water	 |        |	59 |	63	| 80	  | 65	          | 80	            | 58    |
9  | blastoise	| water	 |        |	79 |	83	| 100	  | 85	          | 105	            | 78    |
10 | caterpie	| bug	 | 	      | 45 |	30	| 35	  | 20	          | 20	            | 45    |
