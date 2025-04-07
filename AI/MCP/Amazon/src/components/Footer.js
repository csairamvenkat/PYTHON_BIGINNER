import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  return (
    <footer className="footer">
      <div className="back-to-top" onClick={scrollToTop}>
        Back to top
      </div>
      
      <div className="footer-links">
        <div className="footer-links-column">
          <h3>Get to Know Us</h3>
          <Link to="/">Careers</Link>
          <Link to="/">About Amazon</Link>
          <Link to="/">Investor Relations</Link>
          <Link to="/">Amazon Devices</Link>
        </div>
        
        <div className="footer-links-column">
          <h3>Make Money with Us</h3>
          <Link to="/">Sell products on Amazon</Link>
          <Link to="/">Sell on Amazon Business</Link>
          <Link to="/">Sell apps on Amazon</Link>
          <Link to="/">Become an Affiliate</Link>
        </div>
        
        <div className="footer-links-column">
          <h3>Amazon Payment Products</h3>
          <Link to="/">Amazon Business Card</Link>
          <Link to="/">Shop with Points</Link>
          <Link to="/">Reload Your Balance</Link>
          <Link to="/">Amazon Currency Converter</Link>
        </div>
        
        <div className="footer-links-column">
          <h3>Let Us Help You</h3>
          <Link to="/">Your Account</Link>
          <Link to="/">Your Orders</Link>
          <Link to="/">Shipping Rates & Policies</Link>
          <Link to="/">Help Center</Link>
        </div>
      </div>
      
      <div className="footer-bottom">
        <div className="footer-logo">
          <img src="/amazon-logo-white.png" alt="Amazon" />
        </div>
        <div className="footer-copyright">
          <p>&copy; {new Date().getFullYear()} Amazon Clone. All Rights Reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;