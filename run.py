import subprocess
import sys
import os

# 获取正确的路径（支持 PyInstaller 打包）
if getattr(sys, 'frozen', False):
    # 打包后的环境
    base_path = sys._MEIPASS
else:
    # 开发环境
    base_path = os.path.dirname(__file__)

app_path = os.path.join(base_path, "app.py")

# 启动 Streamlit
subprocess.run([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    app_path,
    "--server.headless=true",
    "--server.port=8501"
])
