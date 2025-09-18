
# NLP Course Assignment - Lab 1

## 1. Mô tả công việc

### 🔹 Lab 1
- Cài đặt **`SimpleTokenizer`**:
  - Tokenizer đơn giản, tách câu dựa trên khoảng trắng.
  - Ưu điểm: dễ triển khai, nhanh.
  - Nhược điểm: không xử lý tốt các ký tự đặc biệt (.,!?).

- Cài đặt **`RegexTokenizer`**:
  - Sử dụng Regular Expression để tách token, loại bỏ dấu câu.
  - Ưu điểm: linh hoạt, chính xác hơn khi xử lý văn bản có dấu câu.
  - Nhược điểm: chậm hơn một chút do sử dụng regex.

- Cài đặt interface **`Tokenize`** trong `interfaces.py`:
  - Định nghĩa chuẩn chung cho tất cả tokenizer.
  - Giúp dễ dàng thay thế/hoán đổi tokenizer trong các module khác.
- Cài đặt **`dataset loaders`**:
  - Xử dụng dataset loaders để lưu dữ liệu UD_English-EWT dưới dạng chuỗi văn bản.
  - Sử dụng 100 ký tự đầu tiên của dataset để thử nghiệm 2 phương pháp Tokenize
 
## 2. Kết quả chạy code

**Input** : Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the
mosque in the town of
### 🔹 SimpleTokenizer
Tokens using RegexTokenizer:
Tokens using SimpleTokenizer:
['Al', '-', 'Zaman', ':', 'American', 'forces', 'killed', 'Shaikh', 'Abdullah', 'al', '-', 'Ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of']

### 🔹 RegexTokenizer
Tokens using RegexTokenizer:
['Al', '-', 'Zaman', ':', 'American', 'forces', 'killed', 'Shaikh', 'Abdullah', 'al', '-', 'Ani', ',', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of']




