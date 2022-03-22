import datetime,os
import logging
import logging.handlers

"""
ロギングレベル
CRITICAL:50、ERROR:40、WARING:30、INFO:20、DEBUG:10、NOTSET:0
"""

def setting_process_root_logging(log_dirname=r"."):

    try:

        """
        ロガーの作成
        """
        root_logger = logging.getLogger('')
        root_logger.setLevel(logging.DEBUG) #ロガーの閾値を設定する。設定したレベルよりも低い深刻度のログメッセージは無視される。


        """
        フォーマッターの作成：ログ情報を整形するための情報を指定。
        """
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s -%(levelname)s  -%(processName)s -%(threadName)s -%(pathname)s -%(message)s')

        """
        ハンドラの作成
        """

        # File Handler
        now_datetime = datetime.datetime.now()
        log_basename = 'log_' + now_datetime.strftime('%Y%m%d-%H%M%S') + ".log"
        
        log_file_path = os.path.join(log_dirname,log_basename)

        file_handler = logging.handlers.RotatingFileHandler(filename=log_file_path,maxBytes=10000,backupCount=5,encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)


        """
        ハンドラをルートロガーに追加
        """
        root_logger.addHandler(file_handler)

    except:
        raise