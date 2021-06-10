r:
	@python wsgi.py
run:
	@flask run

envvar:
	@export FLASK_APP=app
	@export FLASK_DEBUG=1

show_remote:
	@git remote -v

heroku_log:
	@heroku logs --tail

heroku_restart:
	@heroku restart