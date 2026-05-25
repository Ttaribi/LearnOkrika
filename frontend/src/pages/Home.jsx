import React from 'react'
import { useNavigate } from 'react-router-dom'
import './Home.css'

const UPDATES_AS_OF = 'May 25, 2026'

const latestUpdates = [
  {
    date: UPDATES_AS_OF,
    title: 'Family & Relationships refreshed',
    description:
      'Updated family vocabulary with Okrika terms for mother, father, grandparents, siblings, children, and spouse.',
    lessonId: 4,
  },
  {
    date: UPDATES_AS_OF,
    title: 'New lesson: Connector Words',
    description:
      'Learn words that link ideas — because, but, if, while, and, and more — with examples and a quiz.',
    lessonId: 10,
  },
  {
    date: UPDATES_AS_OF,
    title: 'Common Verbs expanded',
    description:
      'Added understand, listen, hear, and talk/speak with full tense conjugations (àbè, mè, sàm, bìà).',
    lessonId: 3,
  },
  {
    date: UPDATES_AS_OF,
    title: 'Question Words updated',
    description: 'Added how many things (ndàyê) and how much money (ndàìgbíkì) to the question words lesson.',
    lessonId: 8,
  },
]

function Home() {
  const navigate = useNavigate()

  return (
    <div className="home-page">
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

      <div className="section">
        <h2 className="section-title">Latest Updates</h2>
        <p className="updates-intro">
          New lessons and vocabulary added as of {UPDATES_AS_OF}. Tap an update to jump straight to that lesson.
        </p>
        <ul className="updates-list">
          {latestUpdates.map((update, index) => (
            <li key={index}>
              <button
                type="button"
                className="update-card"
                onClick={() => update.lessonId != null && navigate(`/lessons/${update.lessonId}`)}
              >
                <span className="update-date">{update.date}</span>
                <h3 className="update-title">{update.title}</h3>
                <p className="update-description">{update.description}</p>
                {update.lessonId != null && (
                  <span className="update-link">View lesson →</span>
                )}
              </button>
            </li>
          ))}
        </ul>
      </div>

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
