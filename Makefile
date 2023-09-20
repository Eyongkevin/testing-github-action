eyong-start:
	python manage.py runserver --settings=config.settings.dev_eyong
	
dev-start:
	python manage.py runserver --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt

dev-migrate:
	python manage.py migrate $(app) --settings=config.settings.dev

eyong-migrate:
	python manage.py migrate $(app) --settings=config.settings.dev_eyong

eyong-shell:
	python manage.py shell  --settings=config.settings.dev_eyong

dev-makemigrations:
	python manage.py makemigrations $(app) --settings=config.settings.dev

eyong-makemigrations:
	python manage.py makemigrations $(app) --settings=config.settings.dev_eyong

dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev

dev-sqlmigrate:
	python manage.py sqlmigrate $(app) $(m) --settings=config.settings.dev

dev-shell:
	python manage.py shell --settings=config.settings.dev_eyong

dev-test:
	python manage.py test $(k) --settings=config.settings.dev_eyong