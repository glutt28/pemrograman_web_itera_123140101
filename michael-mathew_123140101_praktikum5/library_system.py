"""
Sistem Manajemen Perpustakaan Sederhana
Mengimplementasikan konsep OOP: Abstract Class, Inheritance, Encapsulation, dan Polymorphism
"""

from abc import ABC, abstractmethod
from typing import List, Optional


class LibraryItem(ABC):
    """
    Abstract base class untuk semua item di perpustakaan.
    Menggunakan abstract method untuk memastikan semua subclass mengimplementasikan method tertentu.
    """
    
    def __init__(self, item_id: str, title: str, year: int):
        """
        Constructor untuk LibraryItem
        
        Args:
            item_id: ID unik untuk item
            title: Judul item
            year: Tahun publikasi
        """
        self._item_id = item_id  # Protected attribute
        self._title = title  # Protected attribute
        self._year = year  # Protected attribute
        self.__available = True  # Private attribute
    
    @property
    def item_id(self) -> str:
        """Property untuk mengakses item_id"""
        return self._item_id
    
    @property
    def title(self) -> str:
        """Property untuk mengakses title"""
        return self._title
    
    @property
    def year(self) -> int:
        """Property untuk mengakses year"""
        return self._year
    
    @property
    def available(self) -> bool:
        """Property untuk mengakses status ketersediaan (encapsulation)"""
        return self.__available
    
    @available.setter
    def available(self, value: bool):
        """Setter untuk mengubah status ketersediaan"""
        if isinstance(value, bool):
            self.__available = value
        else:
            raise ValueError("Available status must be a boolean")
    
    @abstractmethod
    def get_info(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh semua subclass.
        Mengembalikan informasi lengkap tentang item.
        """
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """
        Abstract method yang harus diimplementasikan oleh semua subclass.
        Mengembalikan tipe item.
        """
        pass
    
    def __str__(self) -> str:
        """String representation dari LibraryItem"""
        status = "Tersedia" if self.__available else "Tidak Tersedia"
        return f"[{self._item_id}] {self._title} ({self._year}) - {status}"


class Book(LibraryItem):
    """
    Subclass dari LibraryItem untuk merepresentasikan buku.
    Mengimplementasikan inheritance dan polymorphism.
    """
    
    def __init__(self, item_id: str, title: str, year: int, author: str, pages: int):
        """
        Constructor untuk Book
        
        Args:
            item_id: ID unik untuk buku
            title: Judul buku
            year: Tahun publikasi
            author: Penulis buku
            pages: Jumlah halaman
        """
        super().__init__(item_id, title, year)
        self._author = author  # Protected attribute
        self._pages = pages  # Protected attribute
    
    @property
    def author(self) -> str:
        """Property untuk mengakses author dengan validasi"""
        return self._author
    
    @property
    def pages(self) -> int:
        """Property untuk mengakses pages"""
        return self._pages
    
    def get_info(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan informasi lengkap tentang buku.
        """
        status = "Tersedia" if self.available else "Dipinjam"
        return (f"Buku: {self._title}\n"
                f"  ID: {self._item_id}\n"
                f"  Penulis: {self._author}\n"
                f"  Tahun: {self._year}\n"
                f"  Halaman: {self._pages}\n"
                f"  Status: {status}")
    
    def get_type(self) -> str:
        """Implementasi abstract method untuk mendapatkan tipe item"""
        return "Buku"


class Magazine(LibraryItem):
    """
    Subclass dari LibraryItem untuk merepresentasikan majalah.
    Mengimplementasikan inheritance dan polymorphism.
    """
    
    def __init__(self, item_id: str, title: str, year: int, issue_number: int, publisher: str):
        """
        Constructor untuk Magazine
        
        Args:
            item_id: ID unik untuk majalah
            title: Judul majalah
            year: Tahun publikasi
            issue_number: Nomor edisi
            publisher: Penerbit
        """
        super().__init__(item_id, title, year)
        self._issue_number = issue_number  # Protected attribute
        self._publisher = publisher  # Protected attribute
    
    @property
    def issue_number(self) -> int:
        """Property untuk mengakses issue_number"""
        return self._issue_number
    
    @property
    def publisher(self) -> str:
        """Property untuk mengakses publisher"""
        return self._publisher
    
    def get_info(self) -> str:
        """
        Implementasi abstract method dari LibraryItem.
        Mengembalikan informasi lengkap tentang majalah.
        """
        status = "Tersedia" if self.available else "Dipinjam"
        return (f"Majalah: {self._title}\n"
                f"  ID: {self._item_id}\n"
                f"  Penerbit: {self._publisher}\n"
                f"  Tahun: {self._year}\n"
                f"  Edisi: #{self._issue_number}\n"
                f"  Status: {status}")
    
    def get_type(self) -> str:
        """Implementasi abstract method untuk mendapatkan tipe item"""
        return "Majalah"


class Library:
    """
    Class untuk mengelola koleksi item perpustakaan.
    Mengimplementasikan encapsulation dengan private attributes.
    """
    
    def __init__(self, name: str):
        """
        Constructor untuk Library
        
        Args:
            name: Nama perpustakaan
        """
        self._name = name  # Protected attribute
        self.__items: List[LibraryItem] = []  # Private attribute untuk menyimpan koleksi
    
    @property
    def name(self) -> str:
        """Property untuk mengakses nama perpustakaan"""
        return self._name
    
    def add_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item ke perpustakaan.
        Menggunakan polymorphism - menerima objek LibraryItem apapun.
        
        Args:
            item: Objek LibraryItem (Book, Magazine, dll)
            
        Returns:
            True jika berhasil ditambahkan, False jika ID sudah ada
        """
        # Cek apakah ID sudah ada
        if self._find_item_by_id(item.item_id) is not None:
            return False
        
        self.__items.append(item)
        return True
    
    def _find_item_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Protected method untuk mencari item berdasarkan ID.
        Encapsulation - method ini tidak seharusnya dipanggil dari luar class.
        
        Args:
            item_id: ID item yang dicari
            
        Returns:
            LibraryItem jika ditemukan, None jika tidak ditemukan
        """
        for item in self.__items:
            if item.item_id == item_id:
                return item
        return None
    
    def display_all_items(self) -> None:
        """
        Menampilkan daftar semua item yang tersedia di perpustakaan.
        Menggunakan polymorphism - memanggil method yang sama untuk semua tipe item.
        """
        if not self.__items:
            print(f"\nPerpustakaan {self._name} masih kosong.")
            return
        
        print(f"\n{'='*60}")
        print(f"Daftar Item di Perpustakaan: {self._name}")
        print(f"{'='*60}")
        
        for idx, item in enumerate(self.__items, 1):
            print(f"{idx}. {item}")
        
        print(f"{'='*60}")
        print(f"Total: {len(self.__items)} item\n")
    
    def search_by_title(self, title: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan judul (case-insensitive).
        Menggunakan polymorphism.
        
        Args:
            title: Judul yang dicari
            
        Returns:
            List of LibraryItem yang judulnya mengandung kata kunci
        """
        title_lower = title.lower()
        results = []
        
        for item in self.__items:
            if title_lower in item.title.lower():
                results.append(item)
        
        return results
    
    def search_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID.
        
        Args:
            item_id: ID item yang dicari
            
        Returns:
            LibraryItem jika ditemukan, None jika tidak ditemukan
        """
        return self._find_item_by_id(item_id)
    
    def get_item_count(self) -> int:
        """
        Mengembalikan jumlah total item di perpustakaan.
        
        Returns:
            Jumlah item
        """
        return len(self.__items)
    
    def get_available_items(self) -> List[LibraryItem]:
        """
        Mengembalikan daftar item yang tersedia (belum dipinjam).
        
        Returns:
            List of LibraryItem yang tersedia
        """
        return [item for item in self.__items if item.available]


def main():
    """
    Fungsi utama untuk demonstrasi sistem manajemen perpustakaan.
    """
    print("="*60)
    print("SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA")
    print("="*60)
    
    # Membuat instance Library
    library = Library("Perpustakaan Universitas")
    
    # Menambahkan beberapa buku
    print("\n1. Menambahkan item ke perpustakaan...")
    book1 = Book("B001", "Python Programming", 2023, "John Doe", 350)
    book2 = Book("B002", "Data Structures and Algorithms", 2022, "Jane Smith", 450)
    book3 = Book("B003", "Machine Learning Basics", 2024, "Alice Johnson", 280)
    
    magazine1 = Magazine("M001", "Tech Weekly", 2024, 15, "Tech Publications")
    magazine2 = Magazine("M002", "Science Today", 2024, 8, "Science Press")
    
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(magazine1)
    library.add_item(magazine2)
    
    print("[OK] Item berhasil ditambahkan!")
    
    # Menampilkan semua item
    print("\n2. Menampilkan semua item di perpustakaan...")
    library.display_all_items()
    
    # Mencari berdasarkan judul
    print("\n3. Mencari item berdasarkan judul 'Python'...")
    results = library.search_by_title("Python")
    if results:
        print(f"Ditemukan {len(results)} item:")
        for item in results:
            print(f"  - {item}")
    else:
        print("Tidak ditemukan item dengan judul tersebut.")
    
    # Mencari berdasarkan ID
    print("\n4. Mencari item berdasarkan ID 'B002'...")
    item = library.search_by_id("B002")
    if item:
        print("Item ditemukan:")
        print(item.get_info())
    else:
        print("Item tidak ditemukan.")
    
    # Demonstrasi polymorphism - memanggil get_info() untuk berbagai tipe
    print("\n5. Demonstrasi Polymorphism - Informasi Detail Item...")
    print("\n" + "-"*60)
    for item in library.get_available_items()[:2]:  # Ambil 2 item pertama
        print(item.get_info())
        print("-"*60)
    
    # Demonstrasi encapsulation - mengubah status ketersediaan
    print("\n6. Demonstrasi Encapsulation - Mengubah Status Ketersediaan...")
    book1.available = False
    print(f"Status '{book1.title}' diubah menjadi: {book1.available}")
    print(f"Menggunakan property: {book1.available}")
    
    # Menampilkan item yang tersedia saja
    print("\n7. Menampilkan item yang tersedia...")
    available = library.get_available_items()
    print(f"Total item tersedia: {len(available)}")
    for item in available:
        print(f"  - {item}")
    
    print("\n" + "="*60)
    print("DEMONSTRASI SELESAI")
    print("="*60)


if __name__ == "__main__":
    main()

