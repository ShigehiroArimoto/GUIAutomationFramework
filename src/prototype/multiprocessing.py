"""
メインモジュール
"""
# 標準ライブラリのインポート
import multiprocessing
import logging
import os,sys,datetime

# 自作モジュールのインポート
sys.path.append(os.path.dirname(__file__))  #　__file__ 実行中のPythonファイル名

import sub_modules.logging_config
import sub_modules.monitoring_error
import sub_modules.main_seq

"""
サブプロセスの生成と実行・メインプロセスの処理
・CPythonにはGIL機構があるため、マルチスレッドは並列処理でなく並行処理(同時実行できる実行単位はひとつのみ)になる。並列処理を実現するため、マルチプロセス環境を用いて実装する。
・各プロセスはOSにより個別のリソースが割り当てられるため、変数などオブジェクトを共有することはできない。
・マルチプロセス環境におけるログの記録は工夫が必要である。そこで、今回はメインプロセスのログだけを記録する。
"""

"""
def subprocess
メインプロセスが終了するまで、定期的に異常有無を検知する。異常発生時はエビデンスとして記録し、異常対応のGUI操作を実行する。
"""
def subprocess(a,b,process_event,evi_folder_path=r"./"):

    while process_event.wait(timeout=1) == False: # フラグがSetされるか、タイムアウトが発生するまで処理をブロックする。フラグがSetされた時だけTrueを返す。タイムアウト発生時はFalseを返す。
        sub_modules.monitoring_error.error_check(evi_folder_path)
    
    print("Subprocess is finished")


"""
if __name__ == '__main__'が必要な理由。

例えば、開始方式に spawn あるいは forkserver を使用した場合に以下のモジュールを実行すると RuntimeError で失敗します:
代わりに、次のように if __name__ == '__main__': を使用してプログラムの "エントリポイント" を保護すべきです:
"""

def setting_folder():

    cwd = os.path.dirname(__file__)
    log_folder_path = os.path.join(cwd,"logs")
    evi_folder_root_path = os.path.join(cwd,"evidence") 

    os.makedirs(log_folder_path,exist_ok=True)
    os.makedirs(evi_folder_root_path,exist_ok=True)  

    now_datetime = datetime.datetime.now()
    evi_folder_path = os.path.join(evi_folder_root_path,now_datetime.strftime('%Y%m%d-%H%M%S'))
    os.makedirs(evi_folder_path) 
    
    return log_folder_path,evi_folder_path

def setting_log(log_folder_path):

    sub_modules.logging_config.setting_process_root_logging(log_folder_path)   # メインプロセス用ルートロガーの設定
    log = logging.getLogger(__name__)   #モジュールレベルのロガーを作成

    return log   

if __name__ == "__main__":

    try:
        # 初期設定
        main_process_terminate_event = multiprocessing.Event()  # プロセス間で使用するイベントフラグの生成
        log_folder_path,evi_folder_path = setting_folder()

 
        log = setting_log(log_folder_path)

        log.info("プログラム開始")  

        # コマンドライン引数のチェック
        if len(sys.argv) < 2:   # テストデータが設定されていない場合は強制終了
            log.error("automation condition file does not exist.")
            sys.exit()
        else:
            condition_file_path = sys.argv[1]

            # サブプロセスの生成と実行
            for i in range(1,3):
                process_obj = multiprocessing.Process(target=subprocess,args=[i],kwargs={'b':i,'process_event':main_process_terminate_event,'evi_folder_path':evi_folder_path})   
                process_obj.start()
                log.info("プロセススタート")

            # メインプロセスの処理
            print("evi_folder_path",evi_folder_path)
            sub_modules.main_seq.main_sequence(condition_file_path,evi_folder_path)

    except Exception as e: # 基底クラスExcetion(システム終了以外の全例外)

        log.exception("Exception {} is happen!!!".format(e))    #ログメッセージに加え、例外情報をログに出力

    finally:    #例外発生の有無に関係なく最後に実行する処理

        # メインプロセスからサブプロセスを終了する。
        main_process_terminate_event.set() #イベントをTrueにセットし、各スレッドにメインスレッド終了の事実を伝達する。
        log.info("プログラム終了")