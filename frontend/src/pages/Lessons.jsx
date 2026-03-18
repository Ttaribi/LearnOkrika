import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './Lessons.css'

const stepColors = ['#6C63FF', '#1DB89A', '#E5A100', '#E8567F', '#3B82F6', '#A855F7']

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
      <div className="lessons-loading">
        <div className="loading-spinner"></div>
        <p>Loading lessons...</p>
      </div>
    )
  }

  return (
    <div className="lessons-page">
      <div className="lessons-container">
        <div className="lessons-header">
          <h1>Your Learning Path</h1>
          <p>Work through each lesson in order to build your Okrika skills step by step</p>
        </div>

        {/* Sequential lesson path */}
        <div className="lesson-path">
          {lessons.map((lesson, index) => {
            const color = stepColors[index % stepColors.length]
            return (
              <div
                key={lesson.id}
                className="path-item"
                onClick={() => handleLessonClick(lesson.id)}
                style={{ '--step-color': color }}
              >
                {/* Connector line */}
                {index < lessons.length - 1 && <div className="path-connector" />}

                {/* Step number circle */}
                <div className="path-step">
                  <span className="step-number">{index + 1}</span>
                </div>

                {/* Lesson card */}
                <div className="path-card">
                  <div className="path-card-top">
                    <span className={`path-level ${lesson.level}`}>{lesson.level}</span>
                    <span className="path-duration">{lesson.duration}</span>
                  </div>
                  <h3>{lesson.title}</h3>
                  <p>{lesson.description}</p>
                  <button className="path-btn">
                    {index === 0 ? 'Start Here →' : 'Begin Lesson →'}
                  </button>
                </div>
              </div>
            )
          })}
        </div>

        {lessons.length === 0 && (
          <div className="no-lessons">
            <p>No lessons available yet. Check back soon!</p>
          </div>
        )}
      </div>
    </div>
  )
}

export default Lessons
