import os
import re
import requests

# 读取原始 Typst 文件
typst_file = input("input filename:")  # 你的 Typst 文件名
output_file = output("output filename:")  # 生成的新 Typst 文件
image_folder = "images"  # 本地存放图片的目录

# 确保本地图片存放目录存在
os.makedirs(image_folder, exist_ok=True)

# 读取 Typst 文件内容
with open(typst_file, "r", encoding="utf-8") as f:
    content = f.read()

# 正则表达式匹配 Typst 中的图片 URL
pattern = r'#(figure|box)\(image\("([^"]+)"\)(?:,\s*caption:\s*\[([^\]]*)\])?\s*\)'

def download_image(url):
    """下载图片到本地 images 目录，并返回本地路径"""
    filename = os.path.join(image_folder, os.path.basename(url))  # 取 URL 文件名
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as img_file:
            for chunk in response.iter_content(chunk_size=8192):
                img_file.write(chunk)
        print(f"下载成功: {filename}")
        return filename
    except requests.RequestException as e:
        print(f"下载失败: {url}，错误: {e}")
        return None

# 处理 Typst 文件内容，替换 URL 为本地路径
def replace_images(match):
    url = match.group(2)  # 直接获取 URL 字符串
    local_path = download_image(url)
    if local_path:
        return f'#{match.group(1)}(image("{local_path}"))'  # 保留原始的 figure/box
    return match.group(0)  # 下载失败则不修改

# 替换所有匹配的图片链接
new_content = re.sub(pattern, replace_images, content)

# 将新内容写入输出文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ 处理完成，已生成: {output_file}")
