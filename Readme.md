Instructions:
1. Install the required packages by running the following command:
```
pip install -r requirements.txt
```
2- Create a .env file in the root directory and add the following variables:
```
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```
3-To create the database, run the following command:
```
python etl\dataLoader.py
```
4- To run the application, run the following command:
```
python app.py
```