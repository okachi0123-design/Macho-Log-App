# What I learned about schema

## What is schema
- データを受け取るときの受け取るデータの項目名・データ型・入力条件をあらかじめ定義するルール
- 例えば、JSONにして送るとき、予めキーと値の形式を決めることで、不正な入力の防止、入力チェックの簡略化、データ定義の統一を図る
- なければ、if で文字か数字かなどをいちいちチェックしないといけない

## The structure of schema
```
class TrainingLog(BaseModel):
    weight: float
    reps: int
    exercise: str
```
- class TrainingLog(BaseModel): 新たなschemaを立てるときの宣言
- weight: float　weightは浮動小数点の数、repは整数、excerciseは文字列みたいに指定する


