import os
import re
import pandas as pd
from datetime import datetime

def get_latest_ypclog_file(csv_folder="./csv"):
    timestamp_pattern = re.compile(r'ypclog_(\d{8}_\d{6})\.csv')
    ypclog_files = []

    for file_name in os.listdir(csv_folder):
        match = timestamp_pattern.match(file_name)
        if match:
            timestamp_str = match.group(1)
            timestamp = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
            ypclog_files.append((timestamp, file_name))

    if not ypclog_files:
        print("ypclogで始まるCSVファイルが見つかりません。")
        return None
    
    # 最新のypclogファイルを取得
    latest_file = max(ypclog_files, key=lambda x: x[0])[1]
    return os.path.join(csv_folder, latest_file)

def process_ypclog_file():
    latest_file_path = get_latest_ypclog_file()
    if not latest_file_path:
        return

    # CSVデータの読み込み
    df = pd.read_csv(latest_file_path, encoding="utf-8-sig")

    # 1列目の列名を取得
    first_col_name = df.columns[0]

    # 1列目が数値型でない場合はエラーを出力
    try:
        df[first_col_name] = pd.to_numeric(df[first_col_name], errors='raise')
    except ValueError:
        print(f"{latest_file_path}の1列目が数値ではありません。処理をスキップします。")
        return

    # 1列目が既に降順になっている場合は処理をスキップ
    if df[first_col_name].is_monotonic_decreasing:
        print("1列目は既に上に行くほど大きな値になっています。処理をスキップします。")
        return

    # 1列目を上に行くほど大きな値に設定（降順に振り直す）
    df[first_col_name] = range(len(df), 0, -1)

    # 処理後のCSVファイルの上書き保存
    df.to_csv(latest_file_path, index=False, encoding="utf-8-sig")
    print(f"{latest_file_path}の1列目を上に行くほど大きな値に更新しました。")

# 関数の実行
if __name__ == "__main__":
    process_ypclog_file()
