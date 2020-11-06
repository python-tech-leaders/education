.PHONY: test
test:
	@pytest tests

.PHONY: test_cov
test_cov:
	@pytest --cov-config=.coveragerc --cov=. tests/


.PHONY: install_requirements
install_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt


.PHONY: install_requirements_dev
install_requirements_dev:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.dev.txt


.PHONY: lint
lint:
	@pylint *py tests/

.PHONY: format
format:
	@black main.py tests/
