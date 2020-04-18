# abborrfjallet_django
Django version of abborrfjallet. To play around with, might replace previous website

## installation
`sudo apt install python-virtualenv git`

`virtualenv v_env -p python3; source v_env/bin/activate`

`pip install django`

`git clone https://github.com/nakceb/abborrfjallet_django.git`

`cd abborrfjallet_django`

`python manage.py migrate`

#### create your superusers

`python manage.py createsuperuser`

`python manage.py runserver`