import PropTypes from 'prop-types';
import './ErrorMessage.css';

/**
 * Komponen Error Message
 * ✅ Komponen Fungsional #2
 * ✅ Menggunakan PropTypes
 */
const ErrorMessage = ({ message, onRetry }) => {
  return (
    <div className="error-container">
      <div className="error-icon">⚠️</div>
      <h2>Oops! Terjadi Kesalahan</h2>
      <p>{message}</p>
      {onRetry && (
        <button onClick={onRetry} className="retry-button">
          Coba Lagi
        </button>
      )}
    </div>
  );
};

ErrorMessage.propTypes = {
  message: PropTypes.string.isRequired,
  onRetry: PropTypes.func
};

export default ErrorMessage;
