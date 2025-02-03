# AI_OCR

## 機能概要

入力ファイルで指定したPDFファイルまたは画像ファイルをAI（gemini-2.0-flash-exp）でOCRして出力ファイルに出力する。

## 環境構築

前提：ローカルPCに **git、ptyhon3.12** がインストール済 ＆  ＆ **Gemini APIキー** 取得済

1. **ローカルPCにリポジトリのクーロン作成:**

   ```cmd
   git clone https://github.com/katsu-yoshimu/AI_OCR.git
   ```

2. **ローカルPCに仮想完了作成と仮想環境アクティベート:**

   ```cmd
   cd AI_OCR
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **ローカルPCに必要なPythonパッケージをインストール:**

   ```cmd
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Gemini APIキー値を環境変数に設定:**

   ```cmd:コマンドプロンプト
   set GEMINI_API_KEY=（ここは取得したAPIキー値で置き換えてください）
   ```

   ```PowerShell:PowerShell
   $Env:GEMINI_API_KEY = "（ここは取得したAPIキー値で置き換えてください）"
   ```

## 実行

1. Pythonスクリプト実行

   ```cmd
   python ai_ocr.py -infile サンプル.bmp -outfile サンプル.xlsx
   ```

    「ai_ocr.py」の使い方は「-h」でご確認ください。

   ```cmd
    (.venv) c:\work\AI_OCR>python ai_ocr.py -h
    usage: ai_ocr.py [-h] -infile INFILE [-outfile OUTFILE] [-outfiletype OUTFILETYPE]

    PDF/画像ファイルをOCRして出力します。

    options:
    -h, --help            show this help message and exit
    -infile INFILE        入力ファイル (PDFまたは画像)
    -outfile OUTFILE      出力ファイル (省略時は標準出力)
    -outfiletype OUTFILETYPE
                            出力ファイル形式 (txt, md, csv, html, xlsx) (省略時は出力ファイルの拡張子)
   ```

## 注意事項

- 規約の『プライベート情報、機密情報、または個人情報を送信 しないでください。』が許容できるか？
- 使いどころに注意。AIは実行のときどきでOCRの答えが揺れるっぽい。PDFは単純にテキスト抽出した方が正確性は高い。
- 無料枠なので1分間に15回。1日に1500回の実行上限がある。

## 補足：作成経緯

- PDFのOORを検討していた。
- ChatGPT APIは有料、Gemini APIは無料 → Gemini APIを選択。DeepSeekは出始めだったので選考外。
- Gemini はチャット形式で、画像を入力可能。だたし、PDFは入力できない。
- Vertex AI Studio はチャット形式で、PDFを入力可能。無料っぽいけど、クレジットカードの登録が必要だったので断念。
- ChatGPT はチャット形式で、PDFを入力可能。現状で無料で利用できる範囲ではPDFの中の画像はOCRしてくれないっぽい。
- ついでにpythonコードもAIに作っていただきました。完全に動作するものにならず、自分でデバックしたあとで、ふたたびAIにコードレビューしていただきました。

## 参考リンク

- [実行する AI | スクエニ ITエンジニア ブログ - 実行時の警告について確認しておく](https://blog.jp.square-enix.com/iteng-blog/posts/00095-vertexai-fcalling/#%E5%AE%9F%E8%A1%8C%E6%99%82%E3%81%AE%E8%AD%A6%E5%91%8A%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E7%A2%BA%E8%AA%8D%E3%81%97%E3%81%A6%E3%81%8A%E3%81%8F))

  同様なウォーニングエラーが発生しました。requirements.txtに `grpcio==1.60.1` を追加してエラーを解消しました。ありがとうございました。

- [Qiita 【完全無料】Gemini APIチュートリアル（所要時間10分） - APIキーの取得](https://qiita.com/zukki2/items/10bfeb1c4330aa18ff87#step1api%E3%82%AD%E3%83%BC%E3%81%AE%E5%8F%96%E5%BE%97)

    Gemini APIキーの取得方法を参考にさせていただきました。ありがとうございました。

- [Gemini API によるドキュメント処理機能の詳細 - ローカルに保存されている
 PDF](https://ai.google.dev/gemini-api/docs/document-processing?hl=ja&lang=python#local-pdfs)

    公式サイトです。PDFをプロンプトに設定するコードを参考にさせていただきました。ありがとうございました。

- [Gemini](https://gemini.google.com/)

    公式サイトです。pythonコードの作成＆コードレビューをしていただきました。ありがとうございました。

- [Vertex AI Studio](https://cloud.google.com/generative-ai-studio?hl=ja)

    公式サイトです。PDFファイルのOCRを試しました。pythonコードの作成をしていただきました。ありがとうございました。

- [ChatGPT](https://chatgpt.com/)

    公式サイトです。pythonコードの作成＆コードレビューをしていただきました。ありがとうございました。
