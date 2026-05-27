import React, { useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { Globe } from 'lucide-react'
import './Header.css'

const Header = () => {
  const [isScrolled, setIsScrolled] = useState(false)
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)
  const navigate = useNavigate()
  const location = useLocation()

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const scrollToSection = (sectionId) => {
    if (location.pathname !== '/') {
      navigate('/')
      // Wait for navigation, then scroll
      setTimeout(() => {
        const element = document.getElementById(sectionId)
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' })
        }
      }, 100)
    } else {
      const element = document.getElementById(sectionId)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    }
    setIsMobileMenuOpen(false)
  }

  const handleLogoClick = () => {
    if (location.pathname !== '/') {
      navigate('/')
    } else {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }
    setIsMobileMenuOpen(false)
  }

  const handleNavClick = (e, action) => {
    e.preventDefault()
    action()
  }

  return (
    <header className={`header ${isScrolled ? 'scrolled' : ''}`}>
      <nav className="nav">
        <div className="logo" onClick={handleLogoClick}>
          <Globe size={22} strokeWidth={2} aria-hidden />
          <span>Learn Okrika</span>
        </div>
        <ul className={`nav-links ${isMobileMenuOpen ? 'active' : ''}`}>
          {location.pathname === '/' ? (
            <>
              <li><a href="#features" onClick={(e) => handleNavClick(e, () => scrollToSection('features'))}>Features</a></li>
              <li><a href="#about" onClick={(e) => handleNavClick(e, () => scrollToSection('about'))}>About</a></li>
              <li><a href="#start" onClick={(e) => handleNavClick(e, () => scrollToSection('start'))}>Get Started</a></li>
            </>
          ) : (
            <>
              <li><a href="/" onClick={(e) => handleNavClick(e, () => navigate('/'))}>Home</a></li>
              <li><a href="/lessons" onClick={(e) => handleNavClick(e, () => navigate('/lessons'))}>Lessons</a></li>
              <li><a href="/stories" onClick={(e) => handleNavClick(e, () => navigate('/stories'))}>Stories</a></li>
            </>
          )}
        </ul>
        <button 
          className={`mobile-menu-toggle ${isMobileMenuOpen ? 'active' : ''}`}
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          aria-label="Toggle menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </nav>
    </header>
  )
}

export default Header

