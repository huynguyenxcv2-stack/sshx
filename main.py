import subprocess
import time
from keep_alive import keep_alive

# 1. Khởi động Web Server giả để Render không tắt service
print("Starting Web Server...")
keep_alive()

# 2. Chạy lệnh cài đặt và khởi động sshx
# Lệnh này sẽ tải sshx và chạy nó ngay lập tức
cmd = "curl -sSf https://sshx.io/get | sh -s run"

print("Starting SSHX...")
# Sử dụng subprocess để chạy lệnh shell trong Python
# Shell=True để chạy được chuỗi lệnh có dấu pipe (|)
try:
    subprocess.run(cmd, shell=True, check=True)
except KeyboardInterrupt:
    print("Stopped by user")
except Exception as e:
    print(f"Error: {e}")
