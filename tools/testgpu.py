import torch

# Kiểm tra MPS có khả dụng không
if torch.backends.mps.is_available():
    print("✅ MPS khả dụng, bạn có thể train trên GPU của Mac!")
else:
    print("❌ MPS không khả dụng, sẽ train trên CPU.")

# Kiểm tra CUDA (trên Mac hầu như luôn False)
print("CUDA available:", torch.cuda.is_available())
