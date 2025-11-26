import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import Header from '../components/Header'
import Footer from '../components/Footer'
import './Lessons.css'

const Lessons = () => {
  const [lessons, setLessons] = useState([])
  const [loading, setLoading] = useState(true)
  const navigate = useNavigate()

  useEffect(() => {
    fetchLessons()
  }, [])

  const fetchLessons = async () => {
    try {
      const response = await fetch('/api/lessons')
      const data = await response.json()
      setLessons(data.lessons || [])
    } catch (error) {
      console.error('Error fetching lessons:', error)
      // Fallback to default lessons if API fails
      setLessons([
        {
          id: 0,
          title: 'Introduction to Okrika',
          level: 'beginner',
          description: 'Welcome to learning Okrika! Get started with an introduction to the language.',
          duration: '10 minutes',
          category: 'introduction'
        },
        {
          id: 1,
          title: 'Lesson 1: Basic Greetings',
          level: 'beginner',
          description: 'Learn essential greetings and how to say hello in Okrika',
          duration: '15 minutes',
          category: 'greetings'
        }
      ])
    } finally {
      setLoading(false)
    }
  }

  const handleLessonClick = (lessonId) => {
    navigate(`/lessons/${lessonId}`)
  }

  if (loading) {
    return (
      <>
        <Header />
        <div className="lessons-loading">
          <div className="loading-spinner"></div>
          <p>Loading lessons...</p>
        </div>
        <Footer />
      </>
    )
  }

  return (
    <>
      <Header />
      <div className="lessons-page">
        <div className="lessons-container">
          <div className="lessons-header">
            <h1>Start Learning Okrika</h1>
            <p>Choose a lesson to begin your journey learning the Okrika language</p>
          </div>

          <div className="lessons-grid">
            {lessons.map((lesson) => (
              <div 
                key={lesson.id} 
                className="lesson-card"
                onClick={() => handleLessonClick(lesson.id)}
              >
                <div className="lesson-card-header">
                  <span className="lesson-level">{lesson.level}</span>
                  <span className="lesson-duration">⏱️ {lesson.duration}</span>
                </div>
                <h3>{lesson.title}</h3>
                <p>{lesson.description}</p>
                <button className="lesson-button">
                  Start Lesson →
                </button>
              </div>
            ))}
          </div>

          {lessons.length === 0 && (
            <div className="no-lessons">
              <p>No lessons available yet. Check back soon!</p>
            </div>
          )}
        </div>
      </div>
      <Footer />
    </>
  )
}

export default Lessons

