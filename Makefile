install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=mylib --cov=calcCLI test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py

# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	echo "Deploying... is not implemented yet"
		
all: install lint test format deploy