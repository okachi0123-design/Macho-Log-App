# The flow of converting data to JSON
## What is JSON
- JSONはJavascriptのオブジェクトの捉え方
- データの内容や構造をなるべく保ちながら、他のプログラムでも読める共通の文字形式に変える
- {}内でひと固まり　一項目について、`キー:値`(`重量:50kgみたいに`)で構成され、`,`でそれぞれのデータを区切る

## The method of converting data to JSON
- 参考コード1
```
d = {
    '重量':['50kg'],
    '回数':['30回'],
    '種目':['ベンチプレス'],
}
import json
json_text = json.dumps(d,ensure_ascii=False)
print(json_text)
```
- データを用意
- `import json`をファイルに書いて、JSONを扱う機能を読み込む
- ensure_ascii=FalseはASCII以外の文字が自動でエスケープされないようにする

- 結果
‐  python3 jsonst.py 
{"重量": ["50kg"], "回数": ["30回"], "種目": ["ベンチプレス"]}

- 参考コード2
```
d = {
    '重量':['50kg'],
    '回数':['30回'],
    '種目':['ベンチプレス'],
}
import json
with open('test.json', 'w') as fo:
    json.dump(d, fo, ensure_ascii=False)
```

- `with open`や`open+close`  ＊withはopenを自動でcloseしてくれる
- with open('test.json', 'w')はファイル`test.json`をfoという名前で書きこみ形式で開く
- json.dump(d, fo, ensure_ascii=False)はデータ`d`をJSON形式にして、先ほど開いたファイル`fo`に書きこむという意味

- - 結果
  - 上の結果がファイルに書き込まれる
