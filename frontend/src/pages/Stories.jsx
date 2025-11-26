import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import Header from '../components/Header'
import Footer from '../components/Footer'
import './Stories.css'

const Stories = () => {
  const [stories, setStories] = useState([])
  const [loading, setLoading] = useState(true)
  const navigate = useNavigate()

  useEffect(() => {
    fetchStories()
  }, [])

  const fetchStories = async () => {
    try {
      const response = await fetch('/api/stories')
      const data = await response.json()
      setStories(data.stories || [])
    } catch (error) {
      console.error('Error fetching stories:', error)
      // Fallback to default stories if API fails
      setStories([
        {
          id: 0,
          title: 'A Morning in Okrika',
          level: 'beginner',
          description: 'A simple story about a morning greeting between friends',
          readingTime: '5 minutes',
          category: 'daily_life'
        }
      ])
    } finally {
      setLoading(false)
    }
  }

  const handleStoryClick = (storyId) => {
    navigate(`/stories/${storyId}`)
  }

  if (loading) {
    return (
      <>
        <Header />
        <div className="stories-loading">
          <div className="loading-spinner"></div>
          <p>Loading stories...</p>
        </div>
        <Footer />
      </>
    )
  }

  return (
    <>
      <Header />
      <div className="stories-page">
        <div className="stories-container">
          <div className="stories-header">
            <h1>Read Stories in Okrika</h1>
            <p>Explore conversational Okrika through engaging stories and dialogues</p>
          </div>

          <div className="stories-grid">
            {stories.map((story) => (
              <div 
                key={story.id} 
                className="story-card"
                onClick={() => handleStoryClick(story.id)}
              >
                <div className="story-card-header">
                  <span className="story-level">{story.level}</span>
                  <span className="story-reading-time">📖 {story.readingTime}</span>
                </div>
                <h3>{story.title}</h3>
                <p>{story.description}</p>
                <button className="story-button">
                  Read Story →
                </button>
              </div>
            ))}
          </div>

          {stories.length === 0 && (
            <div className="no-stories">
              <p>No stories available yet. Check back soon!</p>
            </div>
          )}
        </div>
      </div>
      <Footer />
    </>
  )
}

export default Stories

