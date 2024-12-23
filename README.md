# YPC例会アルバム検索システム

* 検索サイトには[こちら](https://phys-ken.github.io/ypc_database/index2.html)からアクセスしてください。
* YPCの[過去の例会アルバム](https://www2.hamajima.co.jp/~tenjin/ypc/ypcalbum.html)を、より効率よく検索することができます。
* 単語単位の検索しかできません。and検索やor検索は非対応です。
* [Githubのリポジトリはここ](https://github.com/phys-ken/ypc_database)です。


## 参考サイト
* [index.htmlだけでCSVを検索するシステムをつくる](https://qiita.com/tamoco/items/87e344c8832c54d95cfb)


### 更新情報
* 2021/9/24(金)
  * URLをクリックすると、例会アルバムの記事に飛べるようにしました。
* 2024/12/16(月)
  * index.htmlの構造を改善しました。
  * ワークフロー全般を見直しました。Google colabではなく、ローカルのPCで実行するスクリプトに移行しました。
  * `run_all_tasks.py`を実行すると、スクレイピング→csvの作成→htmlの修正が一度に完了します。

### Q＆A
* 記事ごとに文章が分かれていない
  * htmlの`<p>タグ`を認識して分析をしています。元の例会アルバムでタグの構造が普段と違うと、うまく分割ができずに、文章に不備が生じてしまいます。
  * ***例*** 通し番号765「勝田さんの授業研究」は、元のサイトのpタグが閉じられていないので、うまく表示されません。


### 旧検索システム
* 2024年12月より前の検索システムは[こちら](https://phys-ken.github.io/ypc_database/index.html)からアクセスしてください。