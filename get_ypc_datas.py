from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import tqdm
import datetime
import os

# スクレイピングするURL
url = "https://www2.hamajima.co.jp/~tenjin/ypc/ypcalbum.html"
r = requests.get(url)
time.sleep(3)
soup = BeautifulSoup(r.content, "html.parser")

# タイトルとURLを取得
titles_html = soup.find_all("dt")
titles = []
for title in titles_html:
    titles.append(title.find("a"))

top_url = "https://www2.hamajima.co.jp/~tenjin/ypc/"

url_list = []
for title in titles:
    url_list.append([title.get_text(), top_url + title.get("href")])

print("全部で" + str(len(url_list)) + "回処理を行います。")

# 各URLページから情報を取得
for i in tqdm.tqdm(range(len(url_list))):
    r = requests.get(url_list[i][1])
    time.sleep(3)
    soup = BeautifulSoup(r.content, "html.parser")

    ps = soup.find_all("p")
    strip_p = []
    for p in ps:
        if p.get("align") is None:
            strip_p.append(p)

    theme_list = []
    counter = -1

    # テキストの整理
    for p in strip_p:
        try:
            if p.find("font").get("size") == "+3":
                counter += 1
                theme_list.append([p.find("font").get_text()])
                theme_list[counter].append("")
                theme_list[counter][1] += p.get_text().strip().replace('\n', '.').replace('\r', '.')
            else:
                theme_list[counter][1] += p.get_text().strip().replace('\n', '.').replace('\r', '.')
        except:
            try:
                theme_list[counter][1] += p.get_text().strip().replace('\n', '.').replace('\r', '.')
            except:
                pass

    url_list[i].append(theme_list)
    
print("スクレイピングが終了しました。")

# DataFrameに変換
df = pd.DataFrame()

for i in range(len(url_list)):
    df_tmp = pd.DataFrame(url_list[i][2], columns=["発表タイトル", "本文"])
    df_tmp["日時"] = url_list[i][0]
    df_tmp["URL"] = url_list[i][1]
    df = pd.concat([df, df_tmp])

# indexをNo.として1列目に追加し、reset_indexを使ってデータフレームをリセット
df = df.reset_index(drop=True)
df.index += 1  # インデックスを1から開始
df.index.name = 'No.'  # インデックスに「No.」という見出しを設定

# 保存フォルダを確認して作成
save_folder = "./csv"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# タイムスタンプをつけてCSV出力
now = datetime.datetime.now()
filename = os.path.join(save_folder, 'ypclog_' + now.strftime('%Y%m%d_%H%M%S') + '.csv')
df.to_csv(filename, encoding='utf-8-sig')

print(f"データは {filename} に保存されました。")
