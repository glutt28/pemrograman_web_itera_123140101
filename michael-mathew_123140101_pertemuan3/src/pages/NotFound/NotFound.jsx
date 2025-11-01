import { useNavigate } from 'react-router-dom';
import './NotFound.css';

/**
 * Halaman 404 Not Found
 * ✅ Error page untuk rute yang tidak ditemukan
 */
const NotFound = () => {
  const navigate = useNavigate();

  return (
    <div className="not-found-container">
      <div className="not-found-content">
        <h1 className="error-code">404</h1>
        <h2>Halaman Tidak Ditemukan</h2>
        <p>Maaf, halaman yang Anda cari tidak ada.</p>
        <button className="back-home-btn" onClick={() => navigate('/')}>
          Kembali ke Beranda
        </button>
      </div>
    </div>
  );
};

export default NotFound;
