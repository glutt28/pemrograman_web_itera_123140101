import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { CartContext } from '../../context/CartContext';
import './Cart.css';

/**
 * Halaman Cart
 * ✅ Mendemonstrasikan penggunaan Context untuk state management
 * ✅ Navigasi programatis
 */
const Cart = () => {
  const { cartItems, removeFromCart, updateQuantity, clearCart, cartTotal } = useContext(CartContext);
  const navigate = useNavigate();

  const handleQuantityChange = (productId, newQuantity) => {
    updateQuantity(productId, newQuantity);
  };

  const handleCheckout = () => {
    if (cartItems.length === 0) {
      alert('Keranjang kosong!');
      return;
    }
    alert(`Checkout berhasil! Total: $${cartTotal.toFixed(2)}`);
    clearCart();
    navigate('/');
  };

  if (cartItems.length === 0) {
    return (
      <div className="container">
        <div className="empty-cart">
          <div className="empty-icon">🛒</div>
          <h2>Keranjang Belanja Kosong</h2>
          <p>Yuk, mulai belanja sekarang!</p>
          <button className="continue-shopping" onClick={() => navigate('/')}>
            Belanja Sekarang
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <div className="cart-page">
        <h1>Keranjang Belanja</h1>
        
        <div className="cart-content">
          <div className="cart-items">
            {cartItems.map(item => (
              <div key={item.id} className="cart-item">
                <img src={item.image} alt={item.title} />
                
                <div className="item-details">
                  <h3>{item.title}</h3>
                  <p className="item-category">{item.category}</p>
                  <p className="item-price">${item.price.toFixed(2)}</p>
                </div>

                <div className="item-actions">
                  <div className="quantity-controls">
                    <button onClick={() => handleQuantityChange(item.id, item.quantity - 1)}>
                      -
                    </button>
                    <span>{item.quantity}</span>
                    <button onClick={() => handleQuantityChange(item.id, item.quantity + 1)}>
                      +
                    </button>
                  </div>
                  
                  <div className="item-total">
                    ${(item.price * item.quantity).toFixed(2)}
                  </div>
                  
                  <button 
                    className="remove-btn"
                    onClick={() => removeFromCart(item.id)}
                  >
                    🗑️ Hapus
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <h2>Ringkasan Belanja</h2>
            <div className="summary-row">
              <span>Total Item:</span>
              <span>{cartItems.reduce((sum, item) => sum + item.quantity, 0)}</span>
            </div>
            <div className="summary-row total">
              <span>Total Harga:</span>
              <span>${cartTotal.toFixed(2)}</span>
            </div>
            
            <button className="checkout-btn" onClick={handleCheckout}>
              Checkout
            </button>
            <button className="clear-cart-btn" onClick={clearCart}>
              Kosongkan Keranjang
            </button>
            <button className="continue-btn" onClick={() => navigate('/')}>
              Lanjut Belanja
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart;
