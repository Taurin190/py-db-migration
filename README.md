# py-db-migration
ツールを作るもチーベーションは、Databaseのデータの移行を簡単にやりたい。
どのように作るかは検討中。
以下のユースケースで出来れば良いかと考え中。

## どのようなツールにするのか
1. 古いデータベースからデータを抽出して、新しいデータベースに全て入れる
1. 古いデータベースの更新部分のみを検知して差分のみを効率的にデータを入れる
1. テストデータ等を入れたい時に、データ数を制限したり出来る
1. データを複製して必要量のテストデータを生成してくれる

## 調べる事
- pythonでのORMの種類はどの程度あるのか
- スキーマの持ち方はどのようにすると良いのか
- どれほど汎用性を持たせられるか
  - そのままデータを入れ替えるだけならスキーマを定義する必要はない？
  - 異なる種類のデータベースに対応してデータの入れ替えを出来るか

## PythonのMySQL接続について
- SQLAlchemyが有名である
- とりあえず、MySQLdbを入れてみたものの、割と直接SQL文を書く感じで汎用的にしにくそう