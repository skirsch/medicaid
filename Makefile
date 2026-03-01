.PHONY: analyze help

.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  make analyze  - Run Medicaid provider spending analysis"
	@echo "  make help     - Show this help"

analyze:
	python3 analyze.py
