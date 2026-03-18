import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './Home.css'

const stats = [
  { number: '1,000+', label: 'Active Learners', icon: '👥', color: '#6C63FF' },
  { number: '50+', label: 'Lessons', icon: '📖', color: '#1DB89A' },
  { number: '24/7', label: 'Access', icon: '🌐', color: '#E5A100' },
  { number: 'Free', label: 'To Start', icon: '✨', color: '#E8567F' },
]

function Home() {
  const navigate = useNavigate()
  const [lessons, setLessons] = useState([])

  useEffect(() => {
    fetchLessons()
  }, [])

  const fetchLessons = async () => {
    try {
      const response = await fetch('/api/lessons')
      const data = await response.json()
      setLessons((data.lessons || []).slice(0, 3))
    } catch (error) {
      setLessons([
        { id: 0, title: 'Introduction to Okrika', level: 'beginner', description: 'Get started with an introduction to the language.', duration: '10 minutes' },
        { id: 1, title: 'Basic Greetings', level: 'beginner', description: 'Learn essential greetings in Okrika.', duration: '15 minutes' },
        { id: 2, title: 'Pronouns', level: 'beginner', description: 'Learn personal pronouns in Okrika.', duration: '20 minutes' },
      ])
    }
  }

  return (
    <div className="home-page">
      {/* Welcome Banner */}
      <div className="welcome-banner">
        <div className="welcome-content">
          <div className="welcome-text">
            <h1>Welcome to Learn Okrika</h1>
            <p>
              Discover the beautiful Okrika language from Rivers State, Nigeria.
              Start your journey into this rich cultural heritage today.
            </p>
            <button className="start-btn" onClick={() => navigate('/lessons')}>
              Start Learning
            </button>
          </div>
          <div className="welcome-graphic">
            <span className="welcome-emoji">🌍</span>
          </div>
        </div>
      </div>

      {/* Continue Learning */}
      <div className="section">
        <div className="continue-card" onClick={() => navigate('/lessons/0')}>
          <div className="continue-icon">📚</div>
          <div className="continue-info">
            <h3>Continue Learning</h3>
            <p>Introduction to Okrika</p>
            <div className="continue-progress">
              <div className="continue-progress-bar">
                <div className="continue-progress-fill" style={{ width: '10%' }}></div>
              </div>
              <span className="continue-progress-text">Just started</span>
            </div>
          </div>
          <div className="continue-arrow">→</div>
        </div>
      </div>

      {/* Quick Stats */}
      <div className="section">
        <h2 className="section-title">Your Learning Journey</h2>
        <div className="stats-grid">
          {stats.map((stat, index) => (
            <div key={index} className="stat-card" style={{ borderTop: `3px solid ${stat.color}` }}>
              <span className="stat-icon">{stat.icon}</span>
              <span className="stat-number" style={{ color: stat.color }}>{stat.number}</span>
              <span className="stat-label">{stat.label}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Featured Lessons */}
      <div className="section">
        <div className="section-header">
          <h2 className="section-title">Featured Lessons</h2>
          <button className="view-all-btn" onClick={() => navigate('/lessons')}>
            View all →
          </button>
        </div>
        <div className="featured-grid">
          {lessons.map((lesson, index) => (
            <div
              key={lesson.id}
              className="featured-card"
              onClick={() => navigate(`/lessons/${lesson.id}`)}
            >
              <div style={{ flex: 1 }}>
                <div className="featured-card-top">
                  <span className={`level-badge ${lesson.level}`}>{lesson.level}</span>
                  <span className="duration">{lesson.duration}</span>
                </div>
                <h3>Lesson {index + 1}: {lesson.title}</h3>
                <p>{lesson.description}</p>
              </div>
              <button className="featured-btn">Start →</button>
            </div>
          ))}
        </div>
      </div>

      {/* About Okrika */}
      <div className="section">
        <div className="about-card">
          <div className="about-card-icon">🌍</div>
          <div className="about-card-content">
            <h2>About the Okrika Language</h2>
            <p>
              Okrika is a language spoken in Rivers State, Nigeria, part of the Ijo (Ijaw) language
              family. It carries the rich history and traditions of the Okrika people, who have been
              an integral part of the cultural landscape of Rivers State for centuries.
            </p>
            <p>
              Learning Okrika connects you with a vibrant community and helps preserve an important
              part of Nigeria's linguistic heritage.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home
