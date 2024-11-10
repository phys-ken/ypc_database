import os
import re
from datetime import datetime

# csvフォルダのパス
csv_folder = "./csv"

# ypcログファイルのタイムスタンプを抽出する正規表現パターン
timestamp_pattern = re.compile(r'ypclog_(\d{8}_\d{6})\.csv')

# ypcログファイルを検索し、ファイル名からタイムスタンプを取得
ypclog_files = []
for file_name in os.listdir(csv_folder):
    match = timestamp_pattern.match(file_name)
    if match:
        timestamp_str = match.group(1)
        timestamp = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
        ypclog_files.append((timestamp, file_name))

# ypcログファイルがない場合はエラーメッセージを表示
if not ypclog_files:
    print("ypclogで始まるCSVファイルが見つかりません。")
else:
    # タイムスタンプで最新のファイルを選択
    latest_file = max(ypclog_files, key=lambda x: x[0])[1]
    latest_file_path = os.path.join(csv_folder, latest_file)
    relative_csv_path = os.path.relpath(latest_file_path).replace("\\", "/")  # バックスラッシュをスラッシュに変換

    # 更新対象のHTMLファイル
    html_files = ["index.html", "index2.html"]
    
    for html_file in html_files:
        # HTMLファイルの読み込み
        with open(html_file, "r", encoding="utf-8") as file:
            html_content = file.readlines()

        # `csvPath`指定行を検索し、最新のCSVパスに置き換え
        updated_html_content = []
        for line in html_content:
            # `csvPath`の行を最新のパスに置き換え
            new_line = re.sub(r"csvPath: 'csv/ypclog_\d{8}_\d{6}\.csv'", f"csvPath: '{relative_csv_path}'", line)
            new_line = re.sub(r"RequestCsvPath\('csv/ypclog_\d{8}_\d{6}\.csv'\)", f"RequestCsvPath('{relative_csv_path}')", new_line)
            updated_html_content.append(new_line)

        # 修正後のHTMLの保存
        with open(html_file, "w", encoding="utf-8") as file:
            file.writelines(updated_html_content)

        print(f"{html_file}内のCSVファイルパスを{relative_csv_path}に更新しました。")
