import { useState, useContext, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { CartContext } from '../../context/CartContext';
import useFetch from '../../hooks/useFetch';
import Loading from '../../components/Loading/Loading';
import ErrorMessage from '../../components/ErrorMessage/ErrorMessage';
import './ProductDetail.css';

/**
 * Halaman Product Detail
 * ✅ Dynamic Routing dengan useParams
 * ✅ Navigasi Programatis dengan useNavigate
 * ✅ useState untuk quantity management
 * ✅ useEffect untuk scroll to top
 */
const ProductDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { addToCart } = useContext(CartContext);
  const [quantity, setQuantity] = useState(1);

  const { data: product, loading, error } = useFetch(`https://fakestoreapi.com/products/${id}`);

  // ✅ useEffect - scroll to top saat component mount
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [id]);

  const handleQuantityChange = (type) => {
    if (type === 'increase') {
      setQuantity(prev => prev + 1);
    } else if (type === 'decrease' && quantity > 1) {
      setQuantity(prev => prev - 1);
    }
  };

  const handleAddToCart = () => {
    for (let i = 0; i < quantity; i++) {
      addToCart(product);
    }
    alert(`${quantity} ${product.title} ditambahkan ke keranjang!`);
  };

  const handleBuyNow = () => {
    handleAddToCart();
    navigate('/cart');
  };

  if (loading) {
    return <Loading message="Memuat detail produk..." />;
  }

  if (error) {
    return <ErrorMessage message={error} />;
  }

  if (!product) {
    return <ErrorMessage message="Produk tidak ditemukan" />;
  }

  const originalPrice = product.price * 1.5;
  const discount = 33;

  return (
    <div className="container">
      <button className="back-button" onClick={() => navigate(-1)}>
        ← Kembali
      </button>

      <div className="product-detail">
        <div className="product-image-section">
          <img src={product.image} alt={product.title} />
        </div>

        <div className="product-info-section">
          <div className="category-badge">{product.category}</div>
          <h1>{product.title}</h1>
          
          <div className="rating">
            <span className="stars">⭐ {product.rating?.rate || 0}</span>
            <span className="review-count">({product.rating?.count || 0} reviews)</span>
          </div>

          <div className="price-section">
            <div className="current-price">${product.price.toFixed(2)}</div>
            <div className="price-details">
              <span className="old-price">${originalPrice.toFixed(2)}</span>
              <span className="discount-badge">{discount}% OFF</span>
            </div>
          </div>

          <div className="description">
            <h3>Deskripsi Produk</h3>
            <p>{product.description}</p>
          </div>

          <div className="quantity-section">
            <label>Jumlah:</label>
            <div className="quantity-controls">
              <button onClick={() => handleQuantityChange('decrease')}>-</button>
              <span>{quantity}</span>
              <button onClick={() => handleQuantityChange('increase')}>+</button>
            </div>
          </div>

          <div className="action-buttons">
            <button className="add-to-cart-btn" onClick={handleAddToCart}>
              Tambah ke Keranjang
            </button>
            <button className="buy-now-btn" onClick={handleBuyNow}>
              Beli Sekarang
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetail;
