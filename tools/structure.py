import os

def print_folders_structure(root_dir, indent=0):
    # Duyệt qua tất cả các thư mục con
    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):  # Chỉ xử lý nếu là thư mục
            print("    " * indent + f"- {folder}")
            print_folders_structure(folder_path, indent + 1)

# Ví dụ sử dụng:
root_path = "/Users/braly/Desktop/lmvh/plant-identify/dataset"  # Đường dẫn thư mục gốc
print_folders_structure(root_path)
