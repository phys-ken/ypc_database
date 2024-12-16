import subprocess
import sys

# 実行するスクリプトのリスト（順番に実行する）
scripts = [
    "get_ypc_datas.py",
    "csvfix.py",
    "upload_html.py"
]

def run_script(script_name):
    """
    指定されたPythonスクリプトを実行する関数。
    """
    print(f"\n--- 実行中: {script_name} ---")
    try:
        # subprocessで外部Pythonスクリプトを実行
        result = subprocess.run([sys.executable, script_name], check=True)
        print(f"✅ {script_name} の実行が完了しました！")
    except subprocess.CalledProcessError as e:
        print(f"❌ {script_name} の実行中にエラーが発生しました: {e}")
        sys.exit(1)  # エラーが発生したら終了する
    except FileNotFoundError:
        print(f"❌ {script_name} が見つかりません。ファイル名や場所を確認してください。")
        sys.exit(1)

def main():
    """
    3つのスクリプトを順番に実行するメイン関数。
    """
    print("=== Pythonタスクの一括実行を開始します ===")
    for script in scripts:
        run_script(script)
    print("\n🎉 すべてのスクリプトが正常に実行されました！ 🎉")

if __name__ == "__main__":
    main()
