# ログ用モジュール

import logging.config

import settings


def get_my_logger(name):
    logging.config.dictConfig(settings.LOGGING_CONF)
    return logging.getLogger(name)


logger = get_my_logger(__name__)

if __name__ == "__main__":
    # my_loggingを使ってみる
    logger.debug("DEBUG レベルです。")
    logger.info("INFO レベルです。")
    logger.warning("WARNING レベルです。")
    logger.error("ERROR レベルです。")
    logger.critical("CRITICAL レベルです。")
