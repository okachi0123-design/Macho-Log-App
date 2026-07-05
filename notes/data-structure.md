# Jsonデータ構造
## 保存データ
- "exercise" #種目
- "target" #部位
- "exercise_id" #種目ID 

## 記録データ
- "log_id"  #記録id
- "exercise_id" #種目
- "done_at"　#日時
- "weight" #重量
- "reps"　#回数
- "set" #セット数

＊記録データと保存データは別物で"exercise_id"だけ共有

## メモ
- 固定データは参照するためのデータ
- 記録データは入力されるたびに増えるデータ
- 両方は exercise_id でつながる

### 大事なポイント

固定データと記録データは別物。

でも、exercise_id だけ共有する。

記録データの exercise_id: 1
↓
固定データの exercise_id: 1
↓
ベンチプレスの記録だと分かる

### JSONとSQLの違い

JSONでは、

1つのデータ構造の中で
固定データと記録データを分ける

SQLでは、

固定データ系のテーブル
流動データ系のテーブル
に分ける
