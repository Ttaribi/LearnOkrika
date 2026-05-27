import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { ArrowRight } from 'lucide-react'
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
        },
        {
          id: 2,
          title: 'Pronouns',
          level: 'beginner',
          description: 'Learn personal pronouns in Okrika',
          duration: '20 minutes',
          category: 'grammar'
        },
        {
          id: 3,
          title: 'Common Verbs',
          level: 'beginner',
          description: 'Learn essential verbs and their conjugations in Okrika',
          duration: '25 minutes',
          category: 'grammar'
        },
        {
          id: 4,
          title: 'Family and Relationships',
          level: 'beginner',
          description: 'Learn vocabulary for family members and relationships',
          duration: '25 minutes',
          category: 'vocabulary'
        },
        {
          id: 5,
          title: 'Food and Dining',
          level: 'intermediate',
          description: 'Essential phrases and vocabulary for food and dining',
          duration: '30 minutes',
          category: 'vocabulary'
        },
        {
          id: 7,
          title: 'Showing Time: Part 1',
          level: 'beginner',
          description: 'Learn core words and phrases for expressing time in Okrika.',
          duration: '15 minutes',
          category: 'vocabulary'
        },
        {
          id: 9,
          title: 'Showing Time: Part 2',
          level: 'beginner',
          description: 'Continue learning time expressions and frequency words in Okrika.',
          duration: '15 minutes',
          category: 'vocabulary'
        },
        {
          id: 8,
          title: 'Question Words',
          level: 'beginner',
          description: 'Learn how to ask questions in Okrika with who, what, when, where, and whom.',
          duration: '15 minutes',
          category: 'vocabulary'
        },
        {
          id: 10,
          title: 'Connector Words',
          level: 'beginner',
          description: 'Learn words that link ideas in Okrika — because, also, while, and more.',
          duration: '15 minutes',
          category: 'grammar'
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
                  <h3>{lesson.title}</h3>
                  <p>{lesson.description}</p>
                  <button className="path-btn">
                    {index === 0 ? 'Start Here' : 'Begin Lesson'}
                    <ArrowRight size={16} aria-hidden />
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
