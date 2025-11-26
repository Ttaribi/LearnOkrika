import React from 'react'
import './Features.css'

const features = [
  {
    icon: '📚',
    title: 'Structured Lessons',
    description: 'Learn at your own pace with carefully designed lessons that take you from beginner to advanced levels.'
  },
  {
    icon: '🎯',
    title: 'Interactive Learning',
    description: 'Engage with interactive exercises, quizzes, and audio pronunciations to master the language effectively.'
  },
  {
    icon: '🗣️',
    title: 'Native Speaker Audio',
    description: 'Listen to authentic pronunciations from native Okrika speakers to perfect your accent and intonation.'
  },
  {
    icon: '🏛️',
    title: 'Cultural Context',
    description: 'Understand not just the language, but also the rich cultural heritage and traditions of Rivers State.'
  },
  {
    icon: '📱',
    title: 'Learn Anywhere',
    description: 'Access your lessons on any device - desktop, tablet, or mobile. Learn on the go, anytime, anywhere.'
  },
  {
    icon: '🏆',
    title: 'Track Progress',
    description: 'Monitor your learning journey with progress tracking, achievements, and personalized recommendations.'
  }
]

const Features = () => {
  return (
    <section id="features" className="features">
      <div className="container">
        <h2 className="section-title">Why Learn Okrika?</h2>
        <div className="features-grid">
          {features.map((feature, index) => (
            <div 
              key={index} 
              className="feature-card"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className="feature-icon">{feature.icon}</div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Features

