import useFetch from '../../hooks/useFetch';
import Loading from '../../components/Loading/Loading';
import ErrorMessage from '../../components/ErrorMessage/ErrorMessage';
import ProductList from '../../components/ProductList/ProductList';
import './Home.css';

/**
 * Halaman Home
 * ✅ Menggunakan Custom Hook (useFetch) untuk API call
 * ✅ Implementasi Loading State
 * ✅ Implementasi Error Handling
 */
const Home = () => {
  const { data: products, loading, error } = useFetch('https://fakestoreapi.com/products');

  if (loading) {
    return <Loading message="Memuat produk..." />;
  }

  if (error) {
    return <ErrorMessage message={error} />;
  }

  return (
    <div className="container">
      <div className="hero-section">
        <h1>Selamat Datang di NashyaCommerce</h1>
        <p>Temukan produk terbaik dengan harga terjangkau</p>
      </div>
      
      {products && <ProductList products={products} title="Produk Terbaru" />}
    </div>
  );
};

export default Home;
