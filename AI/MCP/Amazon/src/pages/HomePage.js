import React, { useState, useEffect } from 'react';
import ProductCard from '../components/ProductCard';
import './HomePage.css';

const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // In a real app, fetch from API. Here using mock data
    const fetchProducts = () => {
      setLoading(true);
      
      // Simulating API fetch delay
      setTimeout(() => {
        const mockProducts = [
          {
            id: 1,
            title: "Amazon Echo Dot (4th Gen) - Smart speaker with Alexa",
            price: 49.99,
            description: "Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small spaces.",
            category: "Electronics",
            image: "https://via.placeholder.com/300",
            rating: 4.5,
            ratingCount: 732
          },
          {
            id: 2,
            title: "Fire TV Stick 4K streaming device with Alexa Voice Remote",
            price: 39.99,
            description: "Cinematic experience - Watch in vibrant 4K Ultra HD with support for Dolby Vision, HDR, and HDR10+.",
            category: "Electronics",
            image: "https://via.placeholder.com/300",
            rating: 4.7,
            ratingCount: 458
          },
          {
            id: 3,
            title: "Nintendo Switch with Neon Blue and Neon Red Joy‑Con",
            price: 299.99,
            description: "Play your way with the Nintendo Switch gaming system. Whether you're at home or on the go, enjoy your favorite games.",
            category: "Gaming",
            image: "https://via.placeholder.com/300",
            rating: 4.8,
            ratingCount: 1243
          },
          {
            id: 4,
            title: "Apple MacBook Air Laptop: Apple M1 Chip, 13" Retina Display",
            price: 999.99,
            description: "All-Day Battery Life – Go longer than ever with up to 18 hours of battery life.",
            category: "Computers",
            image: "https://via.placeholder.com/300",
            rating: 4.9,
            ratingCount: 893
          },
          {
            id: 5,
            title: "Sony WH-1000XM4 Wireless Noise-Canceling Headphones",
            price: 348.00,
            description: "Industry-leading noise cancellation for an immersive sound experience.",
            category: "Electronics",
            image: "https://via.placeholder.com/300",
            rating: 4.7,
            ratingCount: 476
          },
          {
            id: 6,
            title: "Samsung 65-Inch Class QLED Q80A Series 4K Smart TV",
            price: 1297.99,
            description: "Direct Full Array backlighting with Quantum HDR 12X delivers an incredible viewing experience.",
            category: "Electronics",
            image: "https://via.placeholder.com/300",
            rating: 4.6,
            ratingCount: 341
          },
          {
            id: 7,
            title: "Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker",
            price: 119.99,
            description: "9-in-1 kitchen appliance with functions for pressure cook, slow cook, rice, yogurt, and more.",
            category: "Kitchen",
            image: "https://via.placeholder.com/300",
            rating: 4.7,
            ratingCount: 1452
          },
          {
            id: 8,
            title: "Fitbit Versa 3 Health & Fitness Smartwatch",
            price: 229.95,
            description: "Run, bike, hike and more with built-in GPS and a free 3-month Premium trial.",
            category: "Fitness",
            image: "https://via.placeholder.com/300",
            rating: 4.5,
            ratingCount: 627
          }
        ];
        
        setProducts(mockProducts);
        setLoading(false);
      }, 1000);
    };
    
    fetchProducts();
  }, []);
  
  return (
    <div className="home-page">
      <div className="hero-section">
        <div className="hero-image">
          <div className="hero-overlay">
            <div className="hero-content">
              <h1>Welcome to Amazon</h1>
              <p>Shop millions of products with fast, free delivery</p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="container">
        <h2 className="section-title">Today's Deals</h2>
        
        {loading ? (
          <div className="loading">Loading products...</div>
        ) : (
          <div className="products-grid">
            {products.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default HomePage;