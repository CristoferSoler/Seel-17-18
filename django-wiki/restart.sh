rm db.sqlite3
rm -r archive/migrations/
rm -r bsi/migrations/

python manage.py makemigrations bsi
python manage.py makemigrations archive
python manage.py migrate
