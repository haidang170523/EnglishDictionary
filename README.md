# 📚 English Dictionary (Tkinter GUI)

Một ứng dụng từ điển tiếng Anh có giao diện đồ họa sử dụng Python, hỗ trợ nhập từ khóa bằng tay hoặc giọng nói, gợi ý từ, phát âm nghĩa và tìm kiếm nghĩa của từ dựa vào cơ sở dữ liệu từ vựng lớn.

---

## 🚀 Tính năng

- 🔍 Tìm kiếm nghĩa của từ tiếng Anh (dữ liệu từ `data.json`)
- 💡 Gợi ý từ khi đang nhập (auto-complete)
- 🎤 Nhận diện giọng nói để nhập từ (sử dụng micro)
- 🔊 Đọc to nghĩa của từ
- 🧹 Nút xóa và thoát giao diện
- ✅ Giao diện đẹp, dễ sử dụng (dựa trên thư viện `Tkinter`)

---

## 🗂 Cấu trúc dự án

```
📁 project/
├── main.py              # Tập tin chính khởi chạy ứng dụng
├── gui.py               # Giao diện ứng dụng (Tkinter)
├── functions.py         # Các chức năng xử lý logic
├── data.json            # Dữ liệu từ vựng (dictionary)
└── Photos/
    ├── bg.png
    ├── search.png
    ├── mic.png
    ├── speaker.png
    ├── clear.png
    └── exit.png
```

---

## 🛠 Cài đặt

### 1. Môi trường yêu cầu

- Python 3.7 trở lên
- Các thư viện Python cần thiết:

```bash
pip install speechrecognition pyttsx3
```

> ✅ `tkinter` thường được cài sẵn cùng với Python.

---

## ▶️ Cách sử dụng

### 1. Chạy chương trình:

```bash
python main.py
```

### 2. Hướng dẫn sử dụng:

- Gõ từ vào ô "Enter Word" hoặc nhấn biểu tượng 🎤 để nhập bằng giọng nói
- Nhấn nút 🔍 hoặc Enter để tìm kiếm
- Nhấn 🔊 để phát âm nghĩa
- Nhấn 🧹 để xóa
- Nhấn ❌ để thoát ứng dụng

---

## 📚 Nguồn dữ liệu

- File `data.json` chứa hàng ngàn từ tiếng Anh cùng với định nghĩa, mô tả rõ ràng.
- Ứng dụng sử dụng `difflib.get_close_matches()` để gợi ý từ gần giống nếu từ bạn nhập không có trong dữ liệu.

---

## 💡 Gợi ý mở rộng

- ✅ Tích hợp API để tra cứu online
- 📈 Lưu lại lịch sử tra cứu
- 🌐 Hỗ trợ nhiều ngôn ngữ

---

## 📄 Giấy phép

Dự án này phát hành theo giấy phép **MIT** – bạn có thể sử dụng và chỉnh sửa tự do.

---

## 👤 Tác giả

- Tên: lighthouse23\_
- Github: haidang170523
