import pytest


def pytest_addoption(parser):
    """Agregar opción --headless a pytest"""
    parser.addoption(
        '--headless', 
        action='store_true', 
        default=False,
        help='Run browser tests in headless mode'
    )