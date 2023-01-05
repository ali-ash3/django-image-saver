Steps to run this project on local(For Windows):

1. Create virtual environment:
    py -m venv venv
2. Activate environment:
    .\venv\Scripts\activate

3. Then:
    py manage.py makemigrations
    py manage.py migrate

4. For runing server:
    py manage.py runserver