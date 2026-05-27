import React from 'react'
import { NavLink, useLocation } from 'react-router-dom'
import { BookOpen, Globe, Home, Info, MessagesSquare } from 'lucide-react'
import './Sidebar.css'

const ICON_SIZE = 20
const ICON_STROKE = 2

const navItems = [
  { path: '/', label: 'Home', Icon: Home },
  { path: '/lessons', label: 'Learn', Icon: BookOpen },
  { path: '/stories', label: 'Stories', Icon: MessagesSquare },
]

const Sidebar = () => {
  const location = useLocation()

  const isActive = (path) => {
    if (path === '/') return location.pathname === '/'
    return location.pathname.startsWith(path)
  }

  const renderIcon = (Icon) => (
    <Icon className="sidebar-lucide-icon" size={ICON_SIZE} strokeWidth={ICON_STROKE} aria-hidden />
  )

  return (
    <>
      <nav className="sidebar" aria-label="Main navigation">
        <div className="sidebar-top">
          <div className="sidebar-logo">
            <Globe className="logo-lucide-icon" size={24} strokeWidth={ICON_STROKE} aria-hidden />
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
                  <span className="sidebar-icon">{renderIcon(item.Icon)}</span>
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
            <span className="sidebar-icon">{renderIcon(Info)}</span>
            <span className="sidebar-label">About Okrika</span>
          </NavLink>
        </div>
      </nav>

      <nav className="mobile-tab-bar" aria-label="Mobile navigation">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={`tab-item ${isActive(item.path) ? 'active' : ''}`}
            end={item.path === '/'}
          >
            <span className="tab-icon">{renderIcon(item.Icon)}</span>
            <span className="tab-label">{item.label}</span>
          </NavLink>
        ))}
      </nav>
    </>
  )
}

export default Sidebar
