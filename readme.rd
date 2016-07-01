Waffle vs Gargoyle

https://github.com/jsocol/django-waffle
(https://waffle.readthedocs.io/en/v0.11.1/)

https://github.com/YPlan/gargoyle
(https://gargoyle-yplan.readthedocs.io/en/latest/index.html)
--------------------------------------------------------------------------------
+ Waffle has a better documentation
+ Waffle is easy to set up, less requirements
+ Waffle flags & switches is simpler to configure

- with Waffle you have to care about how you deploy new flags to your servers.
--------------------------------------------------------------------------------
+ with Gargoyle - you can add new flags to GARGOYLE_SWITCH_DEFAULTS and they
  will be created in db automatically, which is big advantage in deploy process.
+ signals (switch_updated, switch_status_updated, switch_condition_deleted, etc)

- Poor docs
- You have to install separate nexus fronted, because you can't configure
  conditions with default django admin. Also you have to add an url to it somewhere
--------------------------------------------------------------------------------

Waffle conditions:
    - percent
    - superuser
    - staff
    - authenticated
    - languages
    - groups
    - users

Gargoyle conditions:
    - hostname
    - IP: address percent
    - IP: particular addressess
    - IP: internal address
    - anonymous
    - username
    - email
    - user percent
    - staff
    - superuser
    - users joined on or after

--------------------------------------------------------------------------------
Waffle notes:

pip install django-waffle
python manage.py migrate
python manage.py loaddata waffle_flags.json  # also we have to load 2 flags in fresh db

index_waffle.html page for playground
http://localhost:8000/w/
--------------------------------------------------------------------------------
Gargoyle notes:

Requires PostgreSQL ≥ 9.4 and Psycopg2 ≥ 2.5.4. (due to usage of JSONField)

pip install gargoyle-yplan
python manage.py migrate

1.  Flags specified in GARGOYLE_SWITCH_DEFAULTS would be created in db automatically,
    BUT only if you start using them in your code.

2.  The default admin page for Switches doesn't provide tools to create selective
    rules. Thus we have to add Nexus frontend package and url for it.
    The static files in this package are handled by python, as this page only
    for admin - it's fine. But if you want to serve this files via nginx
    - it will became a pain in the ass.

index_gargoyle.html page for playground
http://localhost:8000/g/

url for nexus-frontend feature flags management page
http://localhost:8000/admin/feature-flags/gargoyle/
