import logging,os
import subprocess
import pyautogui
import csv,pprint

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

log = logging.getLogger(__name__)

def execute_automation_object(object_path):

    try:
        subprocess.Popen(['start',object_path],shell=True)

    except:
        raise
 

def read_automation_condition(condition_file_path):

    try:
        cond_list = []

        with open(condition_file_path,"r") as cond_file:    # with文を使用することで、終了処理が自動的に実行される。
           
            reader = csv.DictReader(cond_file)  # ヘッダー行の各要素が辞書のキーとなる。
            print(reader)

            for row in reader:
                cond_list.append(row)
                
            pprint.pprint(cond_list)

        return cond_list

    except:
        raise

def automation_seqence(automation_cond_obj,evi_folder_path):

    try:

        width,height = pyautogui.size()
        print(pyautogui.size())

        pyautogui.moveTo(100,100,duration=0.25) # 指定した絶対座標にマウスカーソルを移動する。duration:移動に要する時間

        for i in range(5):
            pyautogui.moveRel(10,10,duration=0.25) #現地点を基準とした相対的な座標にマウスカーソルを移動する。

        print(pyautogui.position())

        pyautogui.click(0,1070,button='left')
        pyautogui.click(button='right')
        pyautogui.doubleClick()

        pyautogui.moveTo(width/3,height/3,duration=0.25)
        pyautogui.doubleClick()

        pyautogui.dragRel(0,100,duration=1)


        x,y = pyautogui.locateCenterOnScreen(os.path.join(os.path.dirname(__file__),"command.png"),confidence=0.8,region=(0,500,1927,1079))
        pyautogui.click(x,y)

        pyautogui.write("ShigehiroArimoto")
        
        pyperclip.copy(u"リラックマ")
        pyautogui.hotkey('ctrl','v')

        pyautogui.press("enter")

        screenshot = pyautogui.screenshot()
        screenshot.save(os.path.join(evi_folder_path,"test.png"))


    except:
        raise


def main_sequence(condition_file_path,evi_folder_path):

    try:

        # 自動化対象となるアプリケーションの起動
        execute_automation_object(r"C:\Windows\System32\calc.exe")
        log.info("Start GUI Automation Object")

        # 自動化操作の条件ファイルを取得
        automation_cond = read_automation_condition(condition_file_path)
        log.info("Read Automation Condition{}".format(condition_file_path))

        # 自動化シーケンスの実行とエビデンスの取得・保存
        
        automation_seqence(automation_cond,evi_folder_path)
        log.info("Automation Sequence is finished.")

    except:
        raise

if __name__ == "__main__":
    import pyperclip

    #main_sequence(r'C:\Users\Shigehiro\Desktop\python_emb\source\learing\multiprocess_guiautomation\condition_files\calc_test_conditions.csv',r"./evidence")

    #read_automation_condition(r'C:\Users\Shigehiro\Desktop\python_emb\source\learing\multiprocess_guiautomation\condition_files\calc_test_conditions.csv')

