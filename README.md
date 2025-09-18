# NLP Course Assignment - Lab 1 & Lab 2

## 1. Mô tả công việc

###  Lab 1
- Cài đặt **`SimpleTokenizer`**:
  - Tokenizer đơn giản, tách câu dựa trên khoảng trắng.
  - Ưu điểm: dễ triển khai, rất nhanh.
  - Nhược điểm: không xử lý tốt dấu câu, dễ làm mất ngữ nghĩa (ví dụ: *covid-19* có thể bị tách sai).

- Cài đặt **`RegexTokenizer`**:
  - Sử dụng Regular Expression để tách token, xử lý tốt hơn văn bản có dấu câu.
  - Ưu điểm: linh hoạt, chính xác hơn trong nhiều trường hợp.
  - Nhược điểm: tốc độ chậm hơn một chút so với tokenizer đơn giản.

- Cài đặt interface **`Tokenize`** trong `interfaces.py`:
  - Định nghĩa chuẩn chung cho tất cả tokenizer.
  - Giúp dễ dàng thay thế hoặc hoán đổi tokenizer trong các module khác.

- Cài đặt **`dataset loaders`**:
  - Load dataset **UD_English-EWT** dưới dạng chuỗi văn bản.
  - Sử dụng **100 ký tự đầu tiên** của dataset để thử nghiệm hai phương pháp Tokenize.

###  Lab 2
- **Mục tiêu**  
  - Biểu diễn văn bản dưới dạng số bằng mô hình **Bag-of-Words (BoW)**.  
  - Chuẩn bị dữ liệu văn bản để sử dụng trong các mô hình Machine Learning.  
  - Tái sử dụng Tokenizer đã cài đặt từ Lab 1.  

- **Task 1: Xây dựng Vectorizer Interface**  
  - Tạo lớp trừu tượng `Vectorizer` trong `src/core/interfaces.py`.  
  - Gồm 3 phương thức bắt buộc:  
    1. `fit(corpus)` – học vocabulary từ dữ liệu.  
    2. `transform(documents)` – biến đổi document thành vector số.  
    3. `fit_transform(corpus)` – kết hợp 2 bước trên.  

- **Task 2: Cài đặt CountVectorizer**  
  - Tạo file `src/representations/count_vectorizer.py`.  
  - Cài đặt lớp `CountVectorizer` kế thừa `Vectorizer`.  
  - Quy trình:  
    - Trong `fit`: tokenize toàn bộ corpus, thu thập token duy nhất, tạo `vocabulary_` ánh xạ token → index.  
    - Trong `transform`: với mỗi document, khởi tạo vector 0, sau đó tăng số đếm cho token xuất hiện.  
    - Trong `fit_transform`: gọi tuần tự `fit` và `transform`.  

- **Task 3: Evaluation / Testing**  
  - Tạo file `test/lab2_test.py`.  
  - Dùng `RegexTokenizer` từ Lab 1.  
  - Khởi tạo `CountVectorizer` và chạy trên corpus mẫu:  

## 2. Kết quả chạy code

###  Lab 1
```
**Input**:  Al-Zaman : American forces killed Shaikh Abdullah al-Ani, the preacher at the mosque in the town of
```


#### RegexTokenizer
- **Thời gian chạy**: ~8.67 ms
```
- **Tokens**:  ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh',
'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the',
'mosque', 'in', 'the', 'town', 'of']
```

#### SimpleTokenizer
- **Thời gian chạy**: ~0.01 ms
```
- **Tokens**:  ['al', '-', 'zaman', ':', 'american', 'forces', 'killed', 'shaikh',
'abdullah', 'al', '-', 'ani', ',', 'the', 'preacher', 'at', 'the',
'mosque', 'in', 'the', 'town', 'of']
```

---

### Lab 2
**Input corpus**:
```
   [
        "I love NLP.",
        "I love programming.",
        "NLP is a subfield of AI."
    ]
```
**RegexTokenizer**

Vocabulary:
```
{'.': 0, 'a': 1, 'and': 2, 'another': 3, 'document': 4, 'example': 5, 'is': 6, 'one': 7, 'sample': 8, 'the': 9, 'third': 10, 'this': 11}
```
Vectors:
```
[1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
[1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1]
[1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1]
```

**SimpleTokenizer**
Vocabulary:
```
{'.': 0, 'a': 1, 'and': 2, 'another': 3, 'document': 4, 'example': 5, 'is': 6, 'one': 7, 'sample': 8, 'the': 9, 'third': 10, 'this': 11}
```
Vectors:
```
[1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1]
[1, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 1]
[1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1]
```
## 3. Giải thích kết quả
### Lab 1

1. **Số lượng token**:  
   - Cả hai tokenizer cho kết quả giống nhau trong ví dụ này vì chuỗi test đơn giản, chưa có trường hợp phức tạp như dấu chấm câu liên tiếp, .  

2. **Tốc độ xử lý**:  
   - `SimpleTokenizer` nhanh hơn rõ rệt (~0.01 ms so với ~8.67 ms).  
   - Nguyên nhân: SimpleTokenizer chỉ dùng hàm `split()` trên khoảng trắng, trong khi RegexTokenizer phải biên dịch và áp dụng pattern regex phức tạp.  

3. **Chất lượng phân tách**:  
   - Trong các văn bản phức tạp, `RegexTokenizer` có ưu thế vượt trội vì xử lý được dấu câu, ký hiệu đặc biệt, hoặc từ viết liền với dấu.  
   - `SimpleTokenizer` dễ bị lỗi tách sai, ví dụ:  
     ```
     Input: covid-19 is dangerous.
     SimpleTokenizer → ['covid-19', 'is', 'dangerous.']
     RegexTokenizer   → ['covid', '-', '19', 'is', 'dangerous']
     ```

4. **Kết luận**:  
   - Khi cần tốc độ và dữ liệu đơn giản → dùng **SimpleTokenizer**.  
   - Khi cần độ chính xác, đặc biệt trong NLP thực tế → dùng **RegexTokenizer**.
### Lab 2

1. **Vocabulary**  
   - Cả hai tokenizer tạo ra vocabulary giống hệt nhau trong ví dụ này.  
   - Lý do: corpus nhỏ, không có trường hợp đặc biệt.
    

2. **Document-term matrix**  
   - Kết quả vector hóa từ `SimpleTokenizer` và `RegexTokenizer` hoàn toàn giống nhau.  
   - Số lần xuất hiện của mỗi từ trong từng document được biểu diễn đúng trong các vector.  

3. **Ý nghĩa**  
   - `CountVectorizer` biến văn bản thành biểu diễn số, giúp mô hình ML có thể xử lý.  
   - Với corpus lớn hơn, sử dụng CountVectorizer sẽ tạo thành các ma trận thưa.

4. **Kết luận**  
   - Trong ví dụ nhỏ, kết quả tương tự nhau.  
   - Trong thực tế, chọn tokenizer phù hợp ảnh hưởng trực tiếp đến chất lượng vocabulary và vector hóa.  




