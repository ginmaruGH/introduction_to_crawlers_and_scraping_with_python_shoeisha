# 設定ファイル

import os

import colorlog


BASE_DIR = os.path.realpath(os.path.dirname(__file__))
# ログファイルディレクトリ
LOG_DIR = os.path.join(BASE_DIR, "logs")

# ログファイルディレクトリがなければ作成する
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING_CONF = {
    # 必須
    "version": 1,
    # logger設定粗ｈ理が重複しても上書きする
    "disable_existing_loggers": True,
    # 出力フォーマットの設定
    "formatters": {
        # デフォルトのフォーマット
        "default": {
            # colorlogライブラリの適用
            "()": colorlog.ColoredFormatter,
            "format": "\t".join([
                # ログレベル
                "%(log_color)s[%(levelname)s]",
                # ログの出力日時
                "asctime:%(asctime)s",
                # ログ出力が実行されたプロセス名
                "process:%(process)d",
                # ログ出力が実行されたスレッドID
                "thread:%(thread)d",
                # ログ出力が実行されたモジュール名
                "module:%(module)s",
                # ログ出力が実行されたモジュールのパスと行番号
                "%(pathname)s:%(lineno)d",
                # ログ出力されるメッセージ
                "message:%(message)s",
            ]),
            # asctimeで出力されるログ出力日時の形式
            "datefmt": "%Y-%m-%d %H:%M:%S",
            # ログレベルに応じて色を付ける
            "log_colors": {
                "DEBUG": "bold_black",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        },
        # ログ出力要素を減らしたシンプル版のフォーマット
        "simple": {
            "()": "colorlog.ColoredFormatter",
            "format": "\t".join([
                "%(log_color)s[%(levelname)s]",
                "%(asctime)s",
                # 要素はログレベル、ログ出力日時、メッセージのみ
                "%(message)s",
            ]),
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "log_colors": {
                "DEBUG": "bold_black",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        },
        # SQLクエリのログ出力用のフォーマット
        "query": {
            "()": "colorlog.ColoredFormatter",
            # クエリのみ出力する
            "format": "%(cyan)s[SQL] %(message)s"
        },
    },
    # ログの出力先を決めるハンドラーの設定
    "handlers": {
        # ファイルにログを出力するハンドラー設定
        "file": {
            # logger.levelがDEBUG以上で出力
            "level": "DEBUG",
            # ログサイズが一定量を超えると自動的に新しいログファイルを作成（ローテート）するハンドラー
            "class": "logging.handlers.RotatingFileHandler",
            # ログファイルのパスを指定
            "filename": os.path.join(LOG_DIR, "crawler_2.log"),
            # このハンドラーではデフォルトのフォーマットでログを出力する
            "formatter": "default",
            # 古くなったログファイルは3世代分保持する指定
            "backupCount": 3,
            # ログサイズが2MBを超えたらログファイルをローテートする
            "maxBytes": 1024 * 1024 * 2,
        },
        # ターミナルにログを出力するハンドラー設定
        "console": {
            "level": "DEBUG",
            # ターミナルにログを出力するハンドラー
            "class": "logging.StreamHandler",
            # このハンドラーではデフォルトのフォーマットでログを出力する
            "formatter": "default",
        },
        # ターミナルにログを出力するハンドラーのシンプルフォーマット版
        "console_simple": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            # シンプル版フォーマットを指定する
            "formatter": "simple",
        },
        # ターミナルにSQLクエリログを出力するハンドラー
        "query": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            # SQLクエリ用フォーマットを指定する
            "formatter": "query",
        },
    },
    # デフォルト設定
    "root": {
        # 先述のfile, consoleの設定で出力
        "handlers": ["file", "console_simple"],
        "level": "DEBUG",
    },
    # ロガー名とロガーに紐づくハンドラー、ログレベルの設定
    "loggers": {
        # logging.getLogger(__name__)の__name__で参照される名前がキーになる
        "celery": {
            "handlers": ["console", "file"],
            # CeleryのログはWARNING以上しか出力しない
            "level": "WARNING",
            # rootロガーにログイベントを渡さない指定
            "propagate": False,
        },
        # my_project.pyモジュールで使うためのロガー
        "my_project": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        }
    }
}
