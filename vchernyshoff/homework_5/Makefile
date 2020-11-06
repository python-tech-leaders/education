.PHONY: test
test:
	@pytest tests

.PHONY: install_requirements
install_requirements:
	@pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

.PHONY: install_requirements_dev
install_requirements_dev:
    @pip install --no-cache-dir -r requirements.dev.txt

.PHONY: lint
check_lint:
    @pylint main.py

.PHONY: black
gofmt_black:
    @black main.py

.PHONY: pytest_coverage
start_pytest_coverage:
    @coverage run -m pytest && coverage report -m
