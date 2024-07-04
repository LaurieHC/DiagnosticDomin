
f-run:
	cd domin-front-end && npm run dev -- -o

b-run:
	cd back-end && cd dominBackEnd && poetry run python manage.py runserver