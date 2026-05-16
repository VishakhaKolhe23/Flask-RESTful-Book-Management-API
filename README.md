# 📚 Flask RESTful Book Management API

A simple and scalable RESTful API built using **Flask** to manage book data.  
This project demonstrates full **CRUD operations** (Create, Read, Update, Delete) and API testing using Postman.

---

## 🚀 Features

- 📖 Get all books  
- 🔍 Get a book by ID  
- ➕ Add a new book  
- ✏️ Update book details  
- ❌ Delete a book  
- 📦 JSON-based responses  
- ⚠️ Error handling (404, 400)

---

## 🛠 Tech Stack

- Python  
- Flask  
- Postman (API testing)

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| GET | `/api/books` | Get all books |
| GET | `/api/books/<id>` | Get book by ID |
| POST | `/api/books` | Add a new book |
| PUT | `/api/books/update/<id>` | Update book |
| DELETE | `/api/books/remove/<id>` | Delete book |

---

## 🧪 API Testing (Postman)

### 📖 Get All Books
![Get All Books](screenshots/get_all_books_after_delete.png)

### 🔍 Get Book by ID
![Get Book](screenshots/get_book_by_id.png)

### ➕ Add Book (POST)
![Post Book](screenshots/post_add_book.png)

### ✏️ Update Book (PUT)
![Update Book](screenshots/put_update_book.png)

### ❌ Delete Book
![Delete Book](screenshots/delete_book.png)

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/Flask-RESTful-Book-Management-API.git

# Navigate to project folder
cd Flask-RESTful-Book-Management-API

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
