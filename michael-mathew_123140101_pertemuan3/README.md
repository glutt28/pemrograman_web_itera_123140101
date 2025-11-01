# NashyaCommerce - React E-Commerce Application 
Web ini merupakan hasil pengerjaan soal UTS lama (sebelum ada update dari Pak Habib)

## Fitur Aplikasi

### 1. Home Page

- Menampilkan daftar produk dari Fake Store API
![daftarproduk](/michael-mathew_123140101_pertemuan3/img/tampilandaftarproduk.png)

- Search produk real-time dengan debounce
![cariproduk](/michael-mathew_123140101_pertemuan3/img/fungsipencarian.png)

- Filter berdasarkan kategori
![filtering](/michael-mathew_123140101_pertemuan3/img/filtering.png)

- Grid layout responsif (3 kolom)

### 2. Product Detail
![infoproduk](/michael-mathew_123140101_pertemuan3/img/detailproduk.png)
- Informasi lengkap produk
- Rating dan review count
- Quantity selector
- Tambah ke keranjang
- Beli langsung (redirect ke cart)

### 3. Shopping Cart
- Daftar produk di keranjang
![daftarkeranjang](/michael-mathew_123140101_pertemuan3/img/daftardikeranjang.png)
- Update quantity
![tambahbarang](/michael-mathew_123140101_pertemuan3/img/updatequantity.png)
- Hapus item
- Total harga otomatis
- Checkout simulation
![checkout](/michael-mathew_123140101_pertemuan3/img/simulasico.png)

### 4. Navigation
- Sticky navbar
- Cart badge dengan jumlah item
- Responsive menu
 - **Programmatic Navigation:** useNavigate di berbagai komponen
 - **Error Page:** NotFound component untuk rute tidak ditemukan

### 5. State Management
 - **Context API (useContext):**
  - `CartContext` - Global state untuk keranjang belanja
  - Fitur: addToCart, removeFromCart, updateQuantity, clearCart
  - Computed values: cartTotal, cartCount

## Teknologi yang Digunakan
- **React 18** - Library UI
- **React Router DOM v6** - Routing
- **Vite** - Build tool & dev server
- **PropTypes** - Type checking
- **Fake Store API** - Data produk
- **CSS3** - Styling

## Instalasi

1. **Install dependencies:**
```bash
npm install
```

2. **Jalankan development server:**
```bash
npm run dev
```

3. **Build untuk production:**
```bash
npm run build
```

## Fitur Aplikasi

### 1. Home Page
- Menampilkan daftar produk dari Fake Store API
- Search produk real-time dengan debounce
- Filter berdasarkan kategori
- Grid layout responsif (3 kolom)

### 2. Product Detail
- Informasi lengkap produk
- Rating dan review count
- Quantity selector
- Tambah ke keranjang
- Beli langsung (redirect ke cart)

### 3. Shopping Cart
- Daftar produk di keranjang
- Update quantity
- Hapus item
- Total harga otomatis
- Checkout simulation

### 4. Navigation
- Sticky navbar
- Cart badge dengan jumlah item
- Responsive menu

## Struktur Project
```
src/
├── components/
│   ├── ErrorMessage/
│   │   ├── ErrorMessage.jsx
│   │   └── ErrorMessage.css
│   ├── Loading/
│   │   ├── Loading.jsx
│   │   └── Loading.css
│   ├── Navbar/
│   │   ├── Navbar.jsx
│   │   └── Navbar.css
│   ├── ProductCard/
│   │   ├── ProductCard.jsx
│   │   └── ProductCard.css
│   └── ProductList/
│       ├── ProductList.jsx
│       └── ProductList.css
├── context/
│   └── CartContext.jsx
├── hooks/
│   ├── useFetch.js
│   └── useDebounce.js
├── pages/
│   ├── Cart/
│   │   ├── Cart.jsx
│   │   └── Cart.css
│   ├── Home/
│   │   ├── Home.jsx
│   │   └── Home.css
│   ├── NotFound/
│   │   ├── NotFound.jsx
│   │   └── NotFound.css
│   └── ProductDetail/
│       ├── ProductDetail.jsx
│       └── ProductDetail.css
├── App.jsx
├── App.css
├── main.jsx
└── index.css
```

## Key Concepts yang Diimplementasikan

### Context API
```javascript
// Shared state menggunakan Context
const { cartItems, addToCart, cartTotal } = useContext(CartContext);
```

### Custom Hooks
```javascript
// Reusable logic untuk fetching
const { data, loading, error } = useFetch(url);
```

### Memoization
```javascript
// useMemo untuk komputasi
const cartTotal = useMemo(() => {
  return cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
}, [cartItems]);
```

### Dynamic Routing
```javascript
// Parameter routing
<Route path="/product/:id" element={<ProductDetail />} />
```

## API
Menggunakan **Fake Store API** (https://fakestoreapi.com/)
- `GET /products` - Daftar semua produk
- `GET /products/:id` - Detail produk

## Responsive Design
- Desktop: 3 kolom grid
- Tablet: 2 kolom grid
- Mobile: 1 kolom grid

