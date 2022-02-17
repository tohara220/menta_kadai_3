import pandas as pd
import eel
import os

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_name):
    # CSV存在判定
    if not os.path.exists(csv_name):
        with open(csv_name, mode="w", encoding="utf-8_sig") as f:
            f.write(",name\n0,たんじろう\n1,ねずこ\n2,ぎゆう\n3,いのすけ\n4,かんろじ\n5,かがや")
    # 検索対象取得
    df=pd.read_csv(f"./{csv_name}")
    source=list(df["name"])
    # 検索
    if word in source:
        eel.view_log_js(f"『{word}』はあります")
    else:
        eel.view_log_js(f"『{word}』はありません")
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
        eel.view_log_js(f"『{word}』を追加しました。")
        
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv(f"./{csv_name}",encoding="utf_8-sig")
    print(source)