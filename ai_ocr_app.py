import re
from pathlib import Path
import streamlit as st
import google.generativeai as genai

# GeminiのAPIキーを環境変数から取得
GEMINI_API_KEY = st.secrets["gemini"]["api_key"] 
if not GEMINI_API_KEY:
    st.error("Gemini APIキーが設定されていません。環境変数にGEMINI_API_KEYを設定してください。")
    st.stop()

# Geminiの設定
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

def get_mime_type(file):
    """ファイルの拡張子からMIMEタイプを取得する"""
    ext = Path(file.name).suffix.lower()[1:]
    mime_types = {
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "png": "image/png",
        "tiff": "image/tiff",
        "tif": "image/tiff",
        "bmp": "image/bmp",
        "gif": "image/gif",
        "pdf": "application/pdf",
    }
    return mime_types.get(ext)

def extract_file_content(response_text):
    """Geminiのレスポンスからコードブロック＝ファイル内容を抽出する"""
    # コードブロックの正規表現パターン
    pattern = r'```(?:[^\n]*\n)?([\s\S]*?)(?:```|$)'
    
    # 最初のコードブロックを検索
    match = re.search(pattern, response_text)
    
    if match:
        # コードブロックの内容を返す
        return match.group(1).strip()
    else:
        # コードブロックが見つからない場合はNoneを返す
        return None

def upload_file():
    """ファイルアップロード画面を表示し、アップロードされたファイルを返す"""
    st.header("ファイルアップロード")
    uploaded_file = st.file_uploader("PDFまたは画像ファイルをアップロードしてください", type=["pdf", "png", "jpg", "jpeg", "tif", "tiff", "bmp", "gif"])
    return uploaded_file

def convert_to_html(file):
    """アップロードされたファイルをGeminiを使用してHTMLに変換する"""
    try:
        # ファイルのMIMEタイプを取得
        mime_type = get_mime_type(file)
        if not mime_type:
            st.error("対応していないファイル形式です。")
            return None

        # ファイルを読み込む
        file_data = file.read()

        # プロンプトを作成
        prompt = "このファイルを読み込んでHTMLに変換してください。表はstyleで見やすくしてください。"

        # Geminiにファイルデータとプロンプトを渡す
        content = [{'mime_type': mime_type, 'data': file_data}, prompt]
        response = model.generate_content(content)

        # レスポンスからHTMLを抽出
        html_content = extract_file_content(response.text)
        return html_content if html_content else response.text
    except Exception as e:
        st.error(f"ファイルの変換中にエラーが発生しました: {e}")
        return None

def display_html(html_content):
    """生成されたHTMLを表示する"""
    st.header("変換されたHTML")
    st.components.v1.html(html_content, height=600, scrolling=True)

def main():
    """メインのアプリケーションロジック"""
    st.title("AI OCR - PDF・画像ファイルをHTMLに変換するWebアプリ")

    # ファイルアップロード画面
    uploaded_file = upload_file()

    if uploaded_file is not None:
        # ファイルをHTMLに変換
        html_content = convert_to_html(uploaded_file)

        if html_content:
            # 変換されたHTMLを表示
            display_html(html_content)

if __name__ == "__main__":
    main()
