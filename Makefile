install: # установка зависимостей
	poetry install

brain-games: # запустить приложение
	poetry run brain-games

build: # сборка пакета
	poetry build

publish: # публикация пакета
	poetry publish --dry-run

package-install: # установка пакета из дистрибутива
	python3 -m pip install --user dist/*.whl

lint: # проверка линтером
	poetry run flake8 brain_games

package-uninstall: # удаление пакета
	python3 -m pip uninstall dist/*.whl