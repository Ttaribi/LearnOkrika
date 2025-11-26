import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './Hero.css'

const Hero = () => {
  const [isVisible, setIsVisible] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    setIsVisible(true)
  }, [])

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }

  return (
    <section id="hero" className={`hero ${isVisible ? 'visible' : ''}`}>
      <div className="hero-content">
        <h1 className="hero-title">Learn Okrika</h1>
        <p className="hero-subtitle">
          Discover the beautiful language of Rivers State, Nigeria. Connect with your heritage, 
          learn authentic Okrika, and explore the rich culture of the Niger Delta region.
        </p>
        <div className="hero-buttons">
          <button 
            className="cta-button primary"
            onClick={() => navigate('/lessons')}
          >
            Start Learning Today
          </button>
          <button 
            className="cta-button secondary"
            onClick={() => scrollToSection('about')}
          >
            Learn More
          </button>
        </div>
      </div>
      <div className="hero-decoration">
        <div className="decoration-circle"></div>
        <div className="decoration-circle"></div>
        <div className="decoration-circle"></div>
      </div>
    </section>
  )
}

export default Hero

