@echo off
chcp 65001 > nul
echo ===================================================
echo   瑠璃ちゃんチャット Androidアプリ テスト起動スクリプト
echo ===================================================
echo.
echo 必要なライブラリ (flet, flet-webview) を自動インストール/更新しています...
python -m pip install -U flet flet-webview

if %ERRORLEVEL% neq 0 (
    echo.
    echo [エラー] ライブラリのインストールに失敗しました。
    echo Python 3 がインストールされ、環境変数 PATH が通っているか確認してください。
    pause
    exit /b
)

echo.
echo ---------------------------------------------------
echo  アプリをWebモード（ブラウザプレビュー）で起動します...
echo  ※ブラウザ上にAndroidと同じフルスクリーンWebViewが展開されます。
echo  ※実行後、自動的にブラウザが起動します。
echo ---------------------------------------------------
echo.
python main.py

pause
