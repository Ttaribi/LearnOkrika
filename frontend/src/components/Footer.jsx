import React from 'react'
import './Footer.css'

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>🌍 Learn Okrika</h3>
            <p>Preserving the language of Rivers State, Nigeria</p>
          </div>
          <div className="footer-section">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="#features">Features</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#start">Get Started</a></li>
            </ul>
          </div>
          <div className="footer-section">
            <h4>Connect</h4>
            <p>Join our community of learners</p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 Learn Okrika. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}

export default Footer

