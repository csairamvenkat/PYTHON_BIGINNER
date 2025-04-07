import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import './ProductPage.css';

const ProductPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [quantity, setQuantity] = useState(1);
  const { addToCart } = useCart();
  
  useEffect(() => {
    // In a real app, fetch from API using the id
    const fetchProduct = () => {
      setLoading(true);
      
      // Simulating API fetch delay
      setTimeout(() => {
        // Mock product data
        const mockProduct = {
          id: parseInt(id),
          title: "Amazon Echo Dot (4th Gen) - Smart speaker with Alexa",
          price: 49.99,
          description: "Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small spaces. It has a sleek, compact design and comes in variety of colors to complement any room. You can play music, get the weather, set alarms, control compatible smart home devices, and more - just ask Alexa.",
          category: "Electronics",
          image: "https://via.placeholder.com/500",
          rating: 4.5,
          ratingCount: 732,
          features: [
            "New look, new sound - Echo Dot is our most popular smart speaker with Alexa. The sleek, compact design delivers crisp vocals and balanced bass for full sound.",
            "Voice control your entertainment - Stream songs from Amazon Music, Apple Music, Spotify, SiriusXM, and others. Play music, audiobooks, and podcasts throughout your home with multi-room music.",
            "Ready to help - Ask Alexa to tell a joke, play music, answer questions, play the news, check the weather, set alarms, and more.",
            "Control your smart home - Use your voice to turn on lights, adjust thermostats, and lock doors with compatible devices.",
            "Connect with others - Call almost anyone hands-free. Instantly drop in on other rooms or announce to the whole house that dinner's ready."
          ],
          stock: 15,
          specifications: {
            "Dimensions": "3.9\" x 3.9\" x 3.5\" (100 mm x 100 mm x 89 mm)",
            "Weight": "12 oz (341.3 g)",
            "Wi-Fi": "Dual-band Wi-Fi supports 802.11a/b/g/n/ac (2.4 and 5 GHz) networks",
            "Bluetooth": "Advanced Audio Distribution Profile (A2DP) support for audio streaming",
            "Audio": "1.6\" speaker"
          }
        };
        
        setProduct(mockProduct);
        setLoading(false);
      }, 1000);
    };
    
    fetchProduct();
  }, [id]);
  
  const handleQuantityChange = (e) => {
    const value = parseInt(e.target.value);
    if (value > 0 && value <= product.stock) {
      setQuantity(value);
    }
  };
  
  const decreaseQuantity = () => {
    if (quantity > 1) {
      setQuantity(quantity - 1);
    }
  };
  
  const increaseQuantity = () => {
    if (quantity < product.stock) {
      setQuantity(quantity + 1);
    }
  };
  
  const handleAddToCart = () => {
    if (product) {
      // Add product to cart multiple times based on quantity
      for (let i = 0; i < quantity; i++) {
        addToCart(product);
      }
    }
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
  
  if (loading) {
    return <div className="loading">Loading product...</div>;
  }
  
  if (!product) {
    return <div className="error">Product not found</div>;
  }
  
  return (
    <div className="product-page container">
      <div className="breadcrumb">
        <Link to="/">Home</Link> / <span>{product.category}</span> / <span>{product.title}</span>
      </div>
      
      <div className="product-details">
        <div className="product-image-container">
          <img src={product.image} alt={product.title} className="product-image" />
        </div>
        
        <div className="product-info">
          <h1 className="product-title">{product.title}</h1>
          
          <div className="product-rating">
            <div className="rating-stars">
              {renderRating(product.rating)}
            </div>
            <span className="rating-count">{product.ratingCount} ratings</span>
          </div>
          
          <div className="product-price">
            <span className="price-text">Price: </span>
            <span className="price-symbol">$</span>
            <span className="price-whole">{Math.floor(product.price)}</span>
            <span className="price-fraction">{(product.price % 1).toFixed(2).substring(2)}</span>
          </div>
          
          <div className="product-description">
            <p>{product.description}</p>
          </div>
          
          <div className="product-features">
            <h3>Features:</h3>
            <ul>
              {product.features.map((feature, index) => (
                <li key={index}>{feature}</li>
              ))}
            </ul>
          </div>
          
          <div className="stock-info">
            <span className={product.stock > 0 ? 'in-stock' : 'out-of-stock'}>
              {product.stock > 0 ? 'In Stock' : 'Out of Stock'}
            </span>
            {product.stock > 0 && (
              <span className="stock-count">({product.stock} available)</span>
            )}
          </div>
          
          <div className="quantity-selector">
            <span>Quantity:</span>
            <div className="quantity-input">
              <button onClick={decreaseQuantity} disabled={quantity <= 1}>-</button>
              <input 
                type="number" 
                value={quantity} 
                onChange={handleQuantityChange}
                min="1"
                max={product.stock}
              />
              <button onClick={increaseQuantity} disabled={quantity >= product.stock}>+</button>
            </div>
          </div>
          
          <div className="product-actions">
            <button 
              onClick={handleAddToCart} 
              className="add-to-cart-button btn-primary"
              disabled={product.stock === 0}
            >
              Add to Cart
            </button>
            <button className="buy-now-button btn-secondary">
              Buy Now
            </button>
          </div>
        </div>
      </div>
      
      <div className="product-details-tabs">
        <div className="tabs-container">
          <div className="tab-content">
            <h3>Product Specifications</h3>
            <table className="specifications-table">
              <tbody>
                {Object.entries(product.specifications).map(([key, value]) => (
                  <tr key={key}>
                    <td className="spec-name">{key}</td>
                    <td className="spec-value">{value}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductPage;