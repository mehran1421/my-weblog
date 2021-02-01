# My Weblog

**this is a practice project**

## Need to be done
- [ ] use Celery and use Redis and MongoDB for it 
- [ ] use PostgresSQL 
- [ ] Dockerize project 
- [ ] use Selenium
- [ ] login with phone number
- [ ] use django-rest-framework 
- [X] ~~regester user and send email him~~

# Install required packages:
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
# how to run project
## first make file .env and write your informations:
```
SECRET_KEY = 'sample'

EMAIL_HOST_PASSWORD='sample'
EMAIL_HOST='sample'
EMAIL_PORT=sample
EMAIL_HOST_USER='sample'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'sample'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'sample'
```
## and you should write terminal this:
```
celery -A blog_mehran worker -l INFO
python manage.py runserver
```
