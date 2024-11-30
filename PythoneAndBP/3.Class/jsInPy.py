


import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# 检查是否缺少execjs库，如果缺少则安装
try:
    import execjs
except ImportError:
    print("缺少execjs库，正在安装...")
    install("PyExecJS")
    import execjs
    # 创建一个PyExecJS的运行环境
    ctx = execjs.compile("""
                        
    function add(x, y) {
        return x + y;
    }
                        
    """)

    # 调用JavaScript函数
    result = ctx.call("add", 3, 4)
    print(result)  # 输出结果为7
