# Sistem Manajemen Perpustakaan Sederhana

Sistem manajemen perpustakaan sederhana yang mengimplementasikan konsep Object-Oriented Programming (OOP) dalam Python.

## Fitur

Sistem ini mengimplementasikan konsep-konsep OOP berikut:

### 1. **Abstract Class**
- `LibraryItem` adalah abstract base class yang menggunakan `ABC` (Abstract Base Class)
- Memiliki abstract methods: `get_info()` dan `get_type()` yang harus diimplementasikan oleh subclass

### 2. **Inheritance**
- `Book` dan `Magazine` adalah subclass yang mewarisi dari `LibraryItem`
- Setiap subclass mengimplementasikan abstract methods dari parent class
- Menggunakan `super()` untuk memanggil constructor parent class

### 3. **Encapsulation**
- **Protected attributes** (menggunakan `_`): `_item_id`, `_title`, `_year`, `_author`, `_pages`, `_issue_number`, `_publisher`
- **Private attributes** (menggunakan `__`): `__available` di `LibraryItem`, `__items` di `Library`
- **Protected methods**: `_find_item_by_id()` di class `Library`

### 4. **Polymorphism**
- Method `get_info()` dan `get_type()` diimplementasikan berbeda di setiap subclass
- `Library` dapat menyimpan dan memproses berbagai tipe `LibraryItem` tanpa perlu mengetahui tipe spesifiknya

### 5. **Property Decorator**
- Menggunakan `@property` untuk mengakses protected/private attributes dengan aman
- Implementasi property setter untuk `available` dengan validasi
- Property digunakan di: `item_id`, `title`, `year`, `available`, `author`, `pages`, `issue_number`, `publisher`

## Struktur Class

### LibraryItem (Abstract Base Class)
```python
- item_id: str (protected)
- title: str (protected)
- year: int (protected)
- available: bool (private, dengan property)
- get_info() -> str (abstract method)
- get_type() -> str (abstract method)
```

### Book (Subclass dari LibraryItem)
```python
- author: str (protected, dengan property)
- pages: int (protected, dengan property)
- get_info() -> str (implementasi)
- get_type() -> str (implementasi)
```

### Magazine (Subclass dari LibraryItem)
```python
- issue_number: int (protected, dengan property)
- publisher: str (protected, dengan property)
- get_info() -> str (implementasi)
- get_type() -> str (implementasi)
```

### Library (Management Class)
```python
- name: str (protected, dengan property)
- items: List[LibraryItem] (private)
- add_item(item: LibraryItem) -> bool
- display_all_items() -> None
- search_by_title(title: str) -> List[LibraryItem]
- search_by_id(item_id: str) -> Optional[LibraryItem]
- get_item_count() -> int
- get_available_items() -> List[LibraryItem]
```

## Cara Menggunakan

### Menjalankan Program
```bash
python library_system.py
```

### Contoh Penggunaan dalam Code

```python
from library_system import Library, Book, Magazine

# Membuat instance Library
library = Library("Perpustakaan Universitas")

# Membuat item
book1 = Book("B001", "Python Programming", 2023, "John Doe", 350)
magazine1 = Magazine("M001", "Tech Weekly", 2024, 15, "Tech Publications")

# Menambahkan item ke perpustakaan
library.add_item(book1)
library.add_item(magazine1)

# Menampilkan semua item
library.display_all_items()

# Mencari berdasarkan judul
results = library.search_by_title("Python")
for item in results:
    print(item.get_info())

# Mencari berdasarkan ID
item = library.search_by_id("B001")
if item:
    print(item.get_info())

# Mengubah status ketersediaan (menggunakan property)
book1.available = False
print(f"Status: {book1.available}")
```

## Demonstrasi Konsep OOP

Program ini mendemonstrasikan:

1. **Abstract Class**: Tidak dapat diinstansiasi langsung, harus melalui subclass
2. **Inheritance**: Subclass mewarisi attributes dan methods dari parent class
3. **Encapsulation**: Data penting dilindungi dengan access modifiers
4. **Polymorphism**: Method yang sama (`get_info()`) menghasilkan output berbeda tergantung tipe objek
5. **Property**: Kontrol akses yang aman ke attributes dengan validasi

## Catatan

- Semua ID item harus unik
- Pencarian berdasarkan judul bersifat case-insensitive
- Status ketersediaan dapat diubah menggunakan property setter dengan validasi


