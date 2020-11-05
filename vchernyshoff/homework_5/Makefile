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
install_lint:
    @pip install --no-cache-dir pylint

.PHONY: black
install_black:
    @pip install --no-cache-dir black

.PHONY: pytest_coverage
install_pytest_coverage:
    @pip install --no-cache-dir pip install pytest-cov
