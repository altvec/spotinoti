install: .env
	poetry install

.env:
	@test ! -f .env && cp .env.example .env

lint:
	poetry run flake8 spotinoty

selfcheck:
	poetry check

check: selfcheck lint

build: check
	poetry build

.PHONY: install lint selfcheck check build