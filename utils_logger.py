"""
Logger Setup Script
File: utils_logger.py

This script provides logging functions for the project. 
Logging is an essential way to track events and issues during execution. 

Features:
- Logs information, warnings, and errors to a designated log file.
- Ensures the log directory exists.

THIS LOGGER SHOULD WORK WITHOUT NEEDING MODIFICATION.
Just put a copy in your root project folder and import in your scripts as shown in the examples.
"""

# Imports from Python Standard Library
import pathlib

# Imports from external packages
from loguru import logger

# Get this file name without the extension
CURRENT_SCRIPT = pathlib.Path(__file__).stem

# Set directory where logs will be stored
LOG_FOLDER: pathlib.Path = pathlib.Path("logs")

# Set the name of the log file
LOG_FILE: pathlib.Path = LOG_FOLDER.joinpath("project_log.log")

# Ensure the log folder exists or create it
try:
    LOG_FOLDER.mkdir(exist_ok=True)
    logger.info(f"Log folder created at: {LOG_FOLDER}")
except Exception as e:
    logger.error(f"Error creating log folder: {e}")

# Configure Loguru to write to the log file
try:
    logger.add(LOG_FILE, level="INFO")
    logger.info(f"Logging to file: {LOG_FILE}")
except Exception as e:
    logger.error(f"Error configuring logger to write to file: {e}")


def get_log_file_path() -> pathlib.Path:
    """Return the path to the log file."""
    return LOG_FILE


def log_example() -> None:
    """Example logging function to demonstrate logging behavior."""
    try:
        logger.info("This is an example info message.")
        logger.warning("This is an example warning message.")
        logger.error("This is an example error message.")
    except Exception as e:
        logger.error(f"An error occurred during logging: {e}")


def main() -> None:
    """Main function to execute logger setup and demonstrate its usage."""
    logger.info(f"STARTING {CURRENT_SCRIPT}.py")

    # Call the example logging function
    log_example()

    logger.info(f"View the log output at {LOG_FILE}")
    logger.info(f"EXITING {CURRENT_SCRIPT}.py.")


# Conditional execution block that calls main() only when this file is executed directly
if __name__ == "__main__":
    main()
