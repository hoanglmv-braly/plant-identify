import os

train_dir = "/Users/braly/Desktop/lmvh/plant-identify/dataset/train"  # Thay đường dẫn thư mục train của bạn
output_file = "classes.txt"   # File txt xuất ra

# Lấy danh sách class (thư mục con) và sắp xếp
class_names = [d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))]
class_names.sort()

# Ghi ra file
with open(output_file, "w", encoding="utf-8") as f:
    for idx, name in enumerate(class_names):
        f.write(f"{name},{idx}\n")

print(f"Đã xuất {len(class_names)} class vào {output_file}")
