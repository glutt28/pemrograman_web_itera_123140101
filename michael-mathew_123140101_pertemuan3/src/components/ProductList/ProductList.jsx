import { useState, useMemo, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
import ProductCard from '../ProductCard/ProductCard';
import useDebounce from '../../hooks/useDebounce';
import './ProductList.css';

/**
 * Komponen ProductList
 * ✅ Komponen Fungsional #5
 * ✅ Menggunakan useState, useEffect, useRef, useMemo
 * ✅ Menggunakan Custom Hook (useDebounce)
 * ✅ Mendemonstrasikan Props drilling
 */
const ProductList = ({ products, title = 'Produk Terbaru' }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const searchInputRef = useRef(null);
  
  // ✅ Custom Hook
  const debouncedSearch = useDebounce(searchTerm, 300);

  // ✅ useEffect untuk focus search input saat mount
  useEffect(() => {
    if (searchInputRef.current) {
      searchInputRef.current.focus();
    }
  }, []);

  // ✅ useMemo untuk filter produk (komputasi tinggi)
  const categories = useMemo(() => {
    const cats = ['all', ...new Set(products.map(p => p.category))];
    return cats;
  }, [products]);

  const filteredProducts = useMemo(() => {
    return products.filter(product => {
      const matchesSearch = product.title
        .toLowerCase()
        .includes(debouncedSearch.toLowerCase());
      
      const matchesCategory = selectedCategory === 'all' || 
        product.category === selectedCategory;
      
      return matchesSearch && matchesCategory;
    });
  }, [products, debouncedSearch, selectedCategory]);

  return (
    <div className="product-list-container">
      <div className="subtitle">
        <span>{title}</span>
        <span className="product-count">({filteredProducts.length} produk)</span>
      </div>

      {/* Filter Section */}
      <div className="filter-section">
        <div className="search-box">
          <input
            ref={searchInputRef}
            type="text"
            placeholder="Cari produk..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>

        <div className="category-filter">
          {categories.map(category => (
            <button
              key={category}
              className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category === 'all' ? 'Semua' : category}
            </button>
          ))}
        </div>
      </div>

      {/* Products Grid */}
      <div className="product-grid">
        {filteredProducts.length > 0 ? (
          filteredProducts.map(product => (
            <ProductCard key={product.id} product={product} />
          ))
        ) : (
          <div className="no-products">
            <p>Tidak ada produk yang ditemukan</p>
          </div>
        )}
      </div>
    </div>
  );
};

ProductList.propTypes = {
  products: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
      image: PropTypes.string.isRequired,
      category: PropTypes.string.isRequired
    })
  ).isRequired,
  title: PropTypes.string
};

export default ProductList;
