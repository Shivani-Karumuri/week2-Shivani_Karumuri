import logging
from pathlib import Path


# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# app.log will be created beside the app folder
LOG_FILE = PROJECT_ROOT / "app.log"


def configure_logging() -> None:
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Prevent duplicate handlers when uvicorn reloads the application
    already_configured = any(
        getattr(handler, "_is_application_handler", False)
        for handler in root_logger.handlers
    )

    if already_configured:
        return

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    console_handler = logging.StreamHandler()

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Mark these handlers so they are not added repeatedly
    setattr(file_handler, "_is_application_handler", True)
    setattr(console_handler, "_is_application_handler", True)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
