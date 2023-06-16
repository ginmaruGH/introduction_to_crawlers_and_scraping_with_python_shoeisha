from logging import (
    getLogger,
    Formatter,
    FileHandler,
    StreamHandler,
    DEBUG,
    ERROR
)

import requests


# ロガー: __name__ には実行モジュール名 logging_sample.py が入る。
logger = getLogger(__name__)

# 出力フォーマット
default_format = "[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s"
default_formatter = Formatter(default_format)
funcname_formatter = Formatter(default_format + " (%(funcName)s)")

# ログ用ハンドラー： コンソール出力用
log_stream_handler = StreamHandler()
log_stream_handler.setFormatter(default_formatter)
log_stream_handler.setLevel(DEBUG)

# ログ用ハンドラー: ファイル出力用
log_file_handler = FileHandler(filename="crawler_1.log")
log_file_handler.setFormatter(funcname_formatter)
log_file_handler.setLevel(ERROR)

# ロガーにハンドラーとレベルをセット
logger.setLevel(DEBUG)
logger.addHandler(log_stream_handler)
logger.addHandler(log_file_handler)


def logging_example():
    # INFOレベルでメッセージを出力する
    logger.info("クローリングを開始します。")
    # WARNINGレベルでメッセージを出力する
    logger.warning("外部サイトのリンクのためクロールしません。")
    # ERRORレベルでメッセージを出力する
    logger.error("ページが見つかりません。")

    try:
        r = requests.get("#invalid_url", timeout=1)
    except requests.exceptions.RequestException as e:
        logger.exception("リクエスト中に例外が起きました。: %r", e)

if __name__ == "__main__":
    logging_example()
