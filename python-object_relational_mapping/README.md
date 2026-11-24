# Python - Object-relational mapping

Scripts that connect to a MySQL server with MySQLdb and SQLAlchemy.

- 0-select_states.py: lists all states
- 1-filter_states.py: lists states starting with N
- 2-my_filter_states.py: filters states by name (format)
- 3-my_safe_filter_states.py: filters states by name (SQL injection safe)
- 4-cities_by_state.py: lists all cities with their state
- 5-filter_cities.py: lists the cities of a given state
- model_state.py: State class and Base
- 7-model_state_fetch_all.py: lists all State objects
- 8-model_state_fetch_first.py: prints the first State object
- 9-model_state_filter_a.py: lists states containing the letter a
- 10-model_state_my_get.py: prints the id of a state given its name
- 11-model_state_insert.py: adds the state Louisiana
- 12-model_state_update_id_2.py: renames the state with id 2
- 13-model_state_delete_a.py: deletes states containing the letter a
- model_city.py: City class
- 14-model_city_fetch_by_state.py: prints all cities with their state

Usage: ./<script> <mysql username> <mysql password> <database name> [arg]
