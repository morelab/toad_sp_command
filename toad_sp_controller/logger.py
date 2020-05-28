import logging

from toad_sp_controller.config import LOGGER_VERBOSE

verbose = LOGGER_VERBOSE

# configure logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def log_info(msg):  # pragma: no cover
    logger.info(msg)


def log_error(msg):  # pragma: no cover
    logger.error(msg)


def log_info_verbose(msg):  # pragma: no cover
    if verbose:
        logger.info(msg)


def log_error_verbose(msg):  # pragma: no cover
    if verbose:
        logger.error(msg)
