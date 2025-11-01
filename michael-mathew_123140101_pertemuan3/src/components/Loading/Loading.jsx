import PropTypes from 'prop-types';
import './Loading.css';

/**
 * Komponen Loading
 * ✅ Komponen Fungsional #1
 * ✅ Menggunakan PropTypes
 */
const Loading = ({ message = 'Loading...' }) => {
  return (
    <div className="loading-container">
      <div className="spinner"></div>
      <p>{message}</p>
    </div>
  );
};

Loading.propTypes = {
  message: PropTypes.string
};

export default Loading;
