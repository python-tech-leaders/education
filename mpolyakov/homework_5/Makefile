test:
	@pytest tests

test_cov:
	@pytest --cov-config=.coveragerc --cov=. tests/

install_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

install_dev_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.dev.txt

lint:
	@pylint *.py tests/

format:
	@black main.py tests/

.PHONY: test test_cov install_requirements install_dev_requirements lint format
