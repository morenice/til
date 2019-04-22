django-admin startproject rest .

python manage.py startapp webapi

python manage.py migrate

python manage.py createsuperuser
Username: admin
Email address: admin@test.com
Password:
.
.
.
Superuser created successfully.

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU1NjAzMDgwNCwianRpIjoiNThjZjhiYmQwNTAxNDQzNGFjYzliMTI2MWZjNTdiNWMiLCJ1c2VyX2lkIjoxfQ.vQlWx9SS67_cWwBCjM8D8PyIg70W1wqaAfu7BzanxSc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU1OTQ0NzA0LCJqdGkiOiJmNGVlNzA4MTNiODU0NzBiYmEwNWE3ZTMxZTcwMTczNiIsInVzZXJfaWQiOjF9.Ppox77dTG4j48ULze4B3f3LfK8rDRvvyNAjkuobiG7s"
}

curl -H "Authorization: Bearer ey..."  http://localhost:8000/api/hello2
