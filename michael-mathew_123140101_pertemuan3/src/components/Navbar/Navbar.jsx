import { useContext } from 'react';
import { Link } from 'react-router-dom';
import { CartContext } from '../../context/CartContext';
import './Navbar.css';

/**
 * Komponen Navbar
 * ✅ Komponen Fungsional #3
 * ✅ Menggunakan useContext untuk akses CartContext
 */
const Navbar = () => {
  const { cartCount } = useContext(CartContext);

  return (
    <div className="navbar">
      <nav>
        <div className="container">
          <Link to="/" className="navbar-logo">
            <span className="logo-icon">🛍️</span>
            NashyaCommerce
          </Link>
          
          <ul>
            <li>
              <Link to="/">Produk Terbaru</Link>
            </li>
            <li>
              <Link to="/">Produk Terlaris</Link>
            </li>
            <li>
              <Link to="/">Promo</Link>
            </li>
            <li className="cart">
              <Link to="/cart">
                <span className="cart-icon">🛒</span>
                Keranjang
                {cartCount > 0 && (
                  <span className="cart-badge">{cartCount}</span>
                )}
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export default Navbar;
