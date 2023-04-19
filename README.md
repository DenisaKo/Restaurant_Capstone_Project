Please generate your own credentials for SECRET_KEY and mysql databese,

for SECRET_KEY:

after downloading the project, activate your virtual environment and run python shell

    python3 manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
printed output is your SECRET_KEY, copy & paste in settings.py

API paths:

/restaurant/menu/

/restaurant/menu/pk

/restaurant/booking/tables/