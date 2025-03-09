#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from tqdm import tqdm

# 设置路径
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PIX3D_DIR = os.path.join('./pix3d')
MODEL_DIR = os.path.join(PIX3D_DIR, 'model')
BINVOX_PATH = os.path.join('./binvox')

# 确保binvox可执行
def ensure_executable(path):
    if not os.access(path, os.X_OK):
        os.chmod(path, 0o755)
        print(f"已将 {path} 设置为可执行文件")

# 处理单个模型文件
def process_model(model_path):
    try:
        # 构建命令
        # print(f"正在处理: {model_path}")
        cmd = [BINVOX_PATH, '-e', '-d', '32', model_path]
        # print(cmd)
        # 执行命令
        result = subprocess.run(cmd, 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE,
                               text=True,
                               check=True)
        
        return True, None
    except subprocess.CalledProcessError as e:
        return False, f"执行错误: {e}, stderr: {e.stderr}"
    except Exception as e:
        return False, f"未知错误: {e}"

# 主函数
def main():
    # 确保binvox可执行
    ensure_executable(BINVOX_PATH)
    
    # 收集所有model.obj文件
    model_files = []
    for category in os.listdir(MODEL_DIR):
        category_path = os.path.join(MODEL_DIR, category)
        if not os.path.isdir(category_path):
            continue
            
        for model_name in os.listdir(category_path):
            model_folder = os.path.join(category_path, model_name)
            if not os.path.isdir(model_folder):
                continue
                
            model_file = os.path.join(model_folder, 'model.obj')
            if os.path.isfile(model_file):
                model_files.append(model_file)
    
    print(f"找到 {len(model_files)} 个模型文件")
    
    # 处理所有模型文件
    success_count = 0
    failed_models = []
    
    for model_file in tqdm(model_files, desc="处理模型"):
        success, error = process_model(model_file)
        if success:
            success_count += 1
        else:
            relative_path = os.path.relpath(model_file, PIX3D_DIR)
            failed_models.append((relative_path, error))
    
    # 输出结果
    print(f"\n处理完成: {success_count}/{len(model_files)} 个模型成功转换")
    
    if failed_models:
        print(f"\n{len(failed_models)} 个模型处理失败:")
        for model, error in failed_models:
            print(f"  - {model}: {error}")

if __name__ == "__main__":
    main()