import React from 'react';
import { Link } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import './ProductCard.css';

const ProductCard = ({ product }) => {
  const { addToCart } = useCart();
  
  const { id, title, price, image, rating, ratingCount } = product;
  
  const handleAddToCart = () => {
    addToCart(product);
  };
  
  // Function to render star ratings
  const renderRating = (rating) => {
    const fullStars = Math.floor(rating);
    const halfStar = rating % 1 >= 0.5;
    const stars = [];
    
    // Add full stars
    for (let i = 0; i < fullStars; i++) {
      stars.push(<i key={`full-${i}`} className="fas fa-star"></i>);
    }
    
    // Add half star if needed
    if (halfStar) {
      stars.push(<i key="half" className="fas fa-star-half-alt"></i>);
    }
    
    // Add empty stars
    const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(<i key={`empty-${i}`} className="far fa-star"></i>);
    }
    
    return stars;
  };

  return (
    <div className="product-card">
      <Link to={`/product/${id}`} className="product-link">
        <img src={image} alt={title} className="product-image" />
        <div className="product-info">
          <h3 className="product-title">{title}</h3>
          <div className="product-rating">
            <div className="rating-stars">
              {renderRating(rating)}
            </div>
            <span className="rating-count">{ratingCount}</span>
          </div>
          <div className="product-price">
            <span className="price-symbol">$</span>
            <span className="price-whole">{Math.floor(price)}</span>
            <span className="price-fraction">{(price % 1).toFixed(2).substring(2)}</span>
          </div>
        </div>
      </Link>
      <button 
        onClick={handleAddToCart}
        className="add-to-cart-button btn-primary"
      >
        Add to Cart
      </button>
    </div>
  );
};

export default ProductCard;