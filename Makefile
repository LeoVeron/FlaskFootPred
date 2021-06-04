run:
	@flask run

envvar:
	@export FLASK_APP=app
	@export FLASK_DEBUG=1


create_app:
	@python scripts/create_app.py