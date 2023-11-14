compose:
	docker compose up -d

stop:
	docker compose down

lint:
	flake8 form_app

type_check:
	mypy form_app
