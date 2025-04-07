import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import './Header.css';

const Header = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const { cart } = useCart();
  
  // Calculate total items in cart
  const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
  
  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };
  
  const handleSearchSubmit = (e) => {
    e.preventDefault();
    // Implement search functionality
    console.log('Searching for:', searchQuery);
  };

  return (
    <header className="header">
      <div className="header-container">
        <Link to="/" className="header-logo">
          <img src="/amazon-logo.png" alt="Amazon" />
        </Link>
        
        <div className="header-search">
          <form onSubmit={handleSearchSubmit}>
            <input
              type="text"
              placeholder="Search Amazon"
              value={searchQuery}
              onChange={handleSearchChange}
            />
            <button type="submit">
              <i className="fas fa-search"></i>
            </button>
          </form>
        </div>
        
        <nav className="header-nav">
          <Link to="/login" className="header-link">
            <div className="header-option">
              <span className="header-option-line1">Hello, Sign in</span>
              <span className="header-option-line2">Account & Lists</span>
            </div>
          </Link>
          
          <Link to="/orders" className="header-link">
            <div className="header-option">
              <span className="header-option-line1">Returns</span>
              <span className="header-option-line2">& Orders</span>
            </div>
          </Link>
          
          <Link to="/cart" className="header-link header-cart">
            <i className="fas fa-shopping-cart"></i>
            <span className="cart-count">{totalItems}</span>
            <span className="header-option-line2">Cart</span>
          </Link>
        </nav>
      </div>
      
      <div className="header-bottom">
        <div className="header-bottom-container">
          <div className="header-bottom-nav">
            <div className="header-bottom-link">
              <i className="fas fa-bars"></i> All
            </div>
            <Link to="/" className="header-bottom-link">Today's Deals</Link>
            <Link to="/" className="header-bottom-link">Customer Service</Link>
            <Link to="/" className="header-bottom-link">Registry</Link>
            <Link to="/" className="header-bottom-link">Gift Cards</Link>
            <Link to="/" className="header-bottom-link">Sell</Link>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;