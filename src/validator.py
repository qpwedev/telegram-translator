"""
Validates the environment variables in the .env file.
"""

import sys
from dotenv import dotenv_values
from logger import Logger


def validate_env_variables():
    """
    Validates the environment variables in the .env file.
    """
    env_vars = dotenv_values(".env")

    errors = []
    for var, value in env_vars.items():
        if not value.strip():
            errors.append(f"{var} is empty.")

    if errors:
        Logger.info("Errors in .env file found:")
        for error in errors:
            Logger.error(error)
        sys.exit(1)
    else:

        # show all variables and their values
        Logger.success("All environment variables are valid")
        for var, value in env_vars.items():
            Logger.debug(f"{var}={value}")
