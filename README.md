# YPC例会アルバム検索システム

* 検索サイトには[こちら](https://phys-ken.github.io/ypc_database/index.html)からアクセスしてください。
* YPCの[過去の例会アルバム](https://www2.hamajima.co.jp/~tenjin/ypc/ypcalbum.html)を、より効率よく検索することができます。
* 単語単位の検索しかできません。and検索やor検索は非対応です。
* [Githubのリポジトリはここ](https://github.com/phys-ken/ypc_database)です。
* こちらの[Colabのノートブック](https://github.com/phys-ken/ypc_database/blob/master/ypc_database_tool.ipynb)で、スクレイピングしてデータを取得しています。

## 参考サイト
* [index.htmlだけでCSVを検索するシステムをつくる](https://qiita.com/tamoco/items/87e344c8832c54d95cfb)

### Q＆A
* 表示結果が明らかにおかしい。
  * htmlの`<p>タグ`を認識して分析をしています。元の例会アルバムでタグの構造が普段と違うと、うまく分割ができずに、文章に不備が生じてしまいます。
  * ***例*** 通し番号765「勝田さんの授業研究」は、元のサイトのpタグが閉じられていないので、うまく表示されません。