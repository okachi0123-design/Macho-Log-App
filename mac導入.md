以下をそのまま手順書として使えば、MacでVS Code導入 → Python環境作成 → FastAPI/Uvicorn導入 → `main.py`起動までできます。

このリポジトリは直下に`main.py`があり、`main.py`内で`FastAPI()`を作成し、`/exercises`と`/set-logs`の2つのAPIを定義しています。起動方法ファイルにも`uvicorn main:app --reload`と`/exercises`の確認URLが書かれています。([GitHub][1])

## 1. ターミナルを開く

Macで「ターミナル」を開きます。

`command + space` → 「ターミナル」と入力 → Enter。

## 2. Homebrewを入れる

HomebrewはMacでPythonやGitなどを入れるためのパッケージ管理ツールです。公式のインストールコマンドは以下です。([Homebrew][2])

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

インストール後、最後に「Next steps」と表示されたら、その指示をコピーして実行してください。

Apple Silicon、つまりM1/M2/M3/M4 Macなら、だいたい以下です。

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Intel Macなら、だいたい以下です。

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

確認します。

```bash
brew --version
```

## 3. Git・Python・VS Codeを入れる

```bash
brew install git python
brew install --cask visual-studio-code
```

確認します。

```bash
git --version
python3 --version
```

VS Codeをターミナルから`code .`で開けるようにします。VS Code公式も、MacではCommand Paletteから`Shell Command: Install 'code' command in PATH`を実行すると説明しています。([Visual Studio Code][3])

VS Codeを開いて、以下を実行してください。

```text
Cmd + Shift + P
→ shell command と入力
→ Shell Command: Install 'code' command in PATH を選択
```

そのあと、ターミナルを一回閉じて開き直します。

確認します。

```bash
code --version
```

## 4. 作業フォルダを作ってリポジトリをクローンする

```bash
mkdir -p ~/dev
cd ~/dev
git clone https://github.com/okachi0123-design/Macho-Log-App.git
cd Macho-Log-App
```

VS Codeで開きます。

```bash
code .
```

## 5. VS CodeにPython拡張を入れる

ターミナルで以下を実行します。

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

## 6. Python仮想環境を作る

Python公式のパッケージングガイドでは、プロジェクトごとに`.venv`を作成し、`source .venv/bin/activate`で有効化する手順が案内されています。([Python Packaging][4])

```bash
python3 -m venv .venv
source .venv/bin/activate
```

成功すると、ターミナルの左側に`(.venv)`のように表示されます。

確認します。

```bash
which python
```

以下のように出ればOKです。

```bash
/Users/あなたの名前/dev/Macho-Log-App/.venv/bin/python
```

pipも更新します。

```bash
python -m pip install --upgrade pip
```

## 7. FastAPIとUvicornを入れる

FastAPI公式ではFastAPIのインストールに`pip install fastapi`または標準依存込みのインストールが案内されています。今回はこのリポジトリを`uvicorn main:app --reload`で起動するため、Uvicornも明示的に入れます。Uvicorn公式では`uvicorn[standard]`を入れると開発時の`--reload`に必要な追加依存も入ると説明されています。([FastAPI][5])

```bash
python -m pip install fastapi "uvicorn[standard]"
```

確認します。

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

## 8. VS Codeで仮想環境を選ぶ

VS Codeで以下を実行します。

```text
Cmd + Shift + P
→ Python: Select Interpreter
→ .venv/bin/python を選択
```

## 9. main.pyを起動する

このリポジトリの`main.py`は`python main.py`ではなく、FastAPIアプリとしてUvicornから起動します。リポジトリ内の起動方法にも`uvicorn main:app --reload`と書かれています。([GitHub][6])

ターミナルで、必ずプロジェクト直下にいる状態で実行します。

```bash
cd ~/dev/Macho-Log-App
source .venv/bin/activate
python -m uvicorn main:app --reload
```

以下のように出れば成功です。

```bash
Uvicorn running on http://127.0.0.1:8000
```

## 10. ブラウザで確認する

ブラウザで以下を開きます。

```text
http://127.0.0.1:8000/exercises
```

以下のようなJSONが出ればOKです。

```json
[
  {
    "exercise_id": 1,
    "target": "足",
    "exercise": "デッドリフト"
  }
]
```

もう1つのAPIも確認できます。

```text
http://127.0.0.1:8000/set-logs
```

FastAPIの自動ドキュメントも開けます。

```text
http://127.0.0.1:8000/docs
```

## 11. 終了方法

サーバーを止めるときは、起動しているターミナルで以下です。

```text
Ctrl + C
```

## よくあるエラー

### `zsh: command not found: brew`

HomebrewのPATHが通っていません。Apple Siliconなら以下を実行します。

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Intel Macなら以下です。

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

### `ModuleNotFoundError: No module named 'fastapi'`

仮想環境が有効になっていないか、違うPythonにインストールしています。

```bash
cd ~/dev/Macho-Log-App
source .venv/bin/activate
python -m pip install fastapi "uvicorn[standard]"
python -m uvicorn main:app --reload
```

### `uvicorn: command not found`

`uvicorn`コマンドではなく、これで起動してください。

```bash
python -m uvicorn main:app --reload
```

### `Address already in use`

8000番ポートがすでに使われています。別ポートで起動します。

```bash
python -m uvicorn main:app --reload --port 8001
```

確認URLも変わります。

```text
http://127.0.0.1:8001/exercises
```

## 最短コマンドまとめ

すでにHomebrewが入っているなら、これで一気にいけます。

```bash
brew install git python
brew install --cask visual-studio-code

mkdir -p ~/dev
cd ~/dev
git clone https://github.com/okachi0123-design/Macho-Log-App.git
cd Macho-Log-App

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install fastapi "uvicorn[standard]"

python -m uvicorn main:app --reload
```

成功確認はこれです。

```text
http://127.0.0.1:8000/exercises
```

[1]: https://github.com/okachi0123-design/Macho-Log-App/blob/main/main.py "Macho-Log-App/main.py at main · okachi0123-design/Macho-Log-App · GitHub"
[2]: https://brew.sh/ "Homebrew: The Package Manager for Everywhere"
[3]: https://code.visualstudio.com/docs/setup/mac "Installing Visual Studio Code on macOS"
[4]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ "Install packages in a virtual environment using pip and venv - Python Packaging User Guide"
[5]: https://fastapi.tiangolo.com/ja/tutorial/ "チュートリアル - ユーザーガイド - FastAPI"
[6]: https://github.com/okachi0123-design/Macho-Log-App/blob/main/%E8%B5%B7%E5%8B%95%E6%96%B9%E6%B3%95 "Macho-Log-App/起動方法 at main · okachi0123-design/Macho-Log-App · GitHub"
