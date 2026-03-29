import React, { useState } from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import './Sidebar.css'

const Sidebar = () => {
  const location = useLocation()

  const navItems = [
    { path: '/', label: 'Home', icon: '🏠' },
    { path: '/lessons', label: 'Learn', icon: '📚' },
    { path: '/stories', label: 'Stories', icon: '💬' },
    { path: '/profile', label: 'Profile', icon: '👤' },
  ]

  const isActive = (path) => {
    if (path === '/') return location.pathname === '/'
    return location.pathname.startsWith(path)
  }

  return (
    <>
      {/* Desktop Sidebar */}
      <nav className="sidebar" aria-label="Main navigation">
        <div className="sidebar-top">
          <div className="sidebar-logo">
            <span className="logo-icon">🌍</span>
            <span className="logo-text">Learn Okrika</span>
          </div>
          <ul className="sidebar-nav">
            {navItems.map((item) => (
              <li key={item.path}>
                <NavLink
                  to={item.path}
                  className={`sidebar-link ${isActive(item.path) ? 'active' : ''}`}
                  end={item.path === '/'}
                >
                  <span className="sidebar-icon">{item.icon}</span>
                  <span className="sidebar-label">{item.label}</span>
                </NavLink>
              </li>
            ))}
          </ul>
        </div>
        <div className="sidebar-bottom">
          <NavLink
            to="/about"
            className={`sidebar-link ${isActive('/about') ? 'active' : ''}`}
          >
            <span className="sidebar-icon">ℹ️</span>
            <span className="sidebar-label">About Okrika</span>
          </NavLink>
        </div>
      </nav>

      {/* Mobile Bottom Tab Bar */}
      <nav className="mobile-tab-bar" aria-label="Mobile navigation">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={`tab-item ${isActive(item.path) ? 'active' : ''}`}
            end={item.path === '/'}
          >
            <span className="tab-icon">{item.icon}</span>
            <span className="tab-label">{item.label}</span>
          </NavLink>
        ))}
      </nav>
    </>
  )
}

export default Sidebar
