install: .env
	poetry install

.env:
	@test ! -f .env && cp .env.example .env

lint:
	poetry run flake8 spotinoti

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

publish:
	poetry publish -r pypi-test

.PHONY: install lint selfcheck check build