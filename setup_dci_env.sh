#!/usr/bin/python
 
git clone http://github.com/caheba/dcinfo.git
python3 -m venv dcinfo
cd dcinfo
source bin/activate
python3 -m pip install django
cd dcinfo
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser


echo "zum Starten:"
echo "cd dcinfo"
echo "source bin/activate"
echo "python3 manage.py runserver
