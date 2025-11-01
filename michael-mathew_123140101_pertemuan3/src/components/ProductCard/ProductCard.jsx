import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import { CartContext } from '../../context/CartContext';
import './ProductCard.css';

/**
 * Komponen ProductCard
 * ✅ Komponen Fungsional #4
 * ✅ Menggunakan Props dengan PropTypes validation
 * ✅ Menggunakan useContext dan useNavigate (React Router hooks)
 */
const ProductCard = ({ product }) => {
  const { addToCart } = useContext(CartContext);
  const navigate = useNavigate();

  const handleAddToCart = (e) => {
    e.stopPropagation();
    addToCart(product);
    alert(`${product.title} ditambahkan ke keranjang!`);
  };

  const handleCardClick = () => {
    navigate(`/product/${product.id}`);
  };

  // Menghitung diskon dummy untuk tampilan
  const originalPrice = product.price * 1.5;
  const discount = 33;

  return (
    <div className="product-card" onClick={handleCardClick}>
      <img src={product.image} alt={product.title} />
      <div className="info">
        <div className="product-title">{product.title}</div>
        <div className="product-category">{product.category}</div>
        <div className="price">${product.price.toFixed(2)}</div>
        <div>
          <span className="old-price">${originalPrice.toFixed(2)}</span>
          <span className="discount">{discount}% OFF</span>
        </div>
        <button className="button-buy" onClick={handleAddToCart}>
          Tambah ke Keranjang
        </button>
      </div>
    </div>
  );
};

ProductCard.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    image: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
    description: PropTypes.string,
    rating: PropTypes.shape({
      rate: PropTypes.number,
      count: PropTypes.number
    })
  }).isRequired
};

export default ProductCard;
