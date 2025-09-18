NLP Course Assignment - Lab 1 & Lab 2
1. Mô tả công việc
🔹 Lab 1

Cài đặt SimpleTokenizer:

Tokenizer đơn giản, tách câu dựa trên khoảng trắng.

Ưu điểm: dễ triển khai, tốc độ rất nhanh.

Nhược điểm: không xử lý được dấu câu và ký tự đặc biệt, phân biệt chữ hoa/thường, dễ làm vocabulary bị “bẩn”.
Ví dụ: covid-19 sẽ bị tách thành ['covid-19'] hoặc đôi khi giữ cả dấu chấm phẩy như document..

Cài đặt RegexTokenizer:

Sử dụng Regular Expression để tách token (ví dụ: \w+).

Ưu điểm: linh hoạt, loại bỏ dấu câu, chuẩn hóa token tốt hơn.

Nhược điểm: tốc độ chậm hơn một chút do phải xử lý bằng regex.

Cài đặt interface Tokenize trong interfaces.py:

Định nghĩa chuẩn chung cho tất cả tokenizer.

Giúp dễ dàng thay thế/hoán đổi tokenizer trong các module khác.

Cài đặt dataset loaders:

Load dữ liệu từ UD_English-EWT dưới dạng chuỗi văn bản.

Thử nghiệm hai tokenizer trên các câu trong dataset để quan sát sự khác biệt.

🔹 Lab 2

Xây dựng interface Vectorizer (abstract class).

Cài đặt CountVectorizer:

fit(corpus): tạo vocabulary từ corpus.

transform(documents): chuyển văn bản thành vector đếm từ.

fit_transform(corpus): kết hợp cả hai bước trên.

Tích hợp cả SimpleTokenizer và RegexTokenizer vào CountVectorizer để so sánh kết quả trên cùng corpus.

Chạy thử trên corpus mẫu và dataset UD_English-EWT.

2. Kết quả chạy code
🔹 Lab 1 (Tokenizers)

Input

Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the mosque in the town of

RegexTokenizer

Tokens:

['al', 'zaman', 'american', 'forces', 'killed', 'shaikh', 'abdullah', 'al', 'ani', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of']


Thời gian chạy: ~8.67 ms

SimpleTokenizer

Tokens:

['Al-Zaman', ':', 'American', 'forces', 'killed', 'Shaikh', 'Abdullah', 'al-Ani,', 'the', 'preacher', 'at', 'the', 'mosque', 'in', 'the', 'town', 'of']


Thời gian chạy: ~0.01 ms

👉 Nhận xét:

SimpleTokenizer cực nhanh nhưng giữ nguyên dấu câu (:, ,) và phân biệt chữ hoa/thường (Al-Zaman ≠ al-zaman).

RegexTokenizer xử lý văn bản sạch hơn, phù hợp hơn cho các tác vụ NLP, nhưng tốc độ chậm hơn.
