import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import './Profile.css'
import { supabase } from '../lib/supabaseClient'

function Profile() {
  const navigate = useNavigate()
  const [user, setUser] = useState(null)
  const [lessons, setLessons] = useState([])
  const [stories, setStories] = useState([])
  const [loading, setLoading] = useState(true)
  const [progressLoading, setProgressLoading] = useState(true)

  const [completedLessonIds, setCompletedLessonIds] = useState(new Set())
  const [completedStoryIds, setCompletedStoryIds] = useState(new Set())

  useEffect(() => {
    let unsubscribe = null
    supabase.auth
      .getUser()
      .then(({ data: { user } }) => setUser(user))
      .catch(() => setUser(null))

    const { data } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null)
    })

    unsubscribe = data?.subscription
    return () => {
      try {
        if (unsubscribe?.unsubscribe) unsubscribe.unsubscribe()
      } catch (e) {}
    }
  }, [])

  useEffect(() => {
    // Load lesson/story metadata for rendering.
    Promise.all([fetch('/api/lessons').then((r) => r.json()), fetch('/api/stories').then((r) => r.json())])
      .then(([lessonsData, storiesData]) => {
        setLessons(lessonsData.lessons || [])
        setStories(storiesData.stories || [])
      })
      .catch(() => {
        // Minimal fallback so the UI still works if the backend is unavailable.
        setLessons([
          { id: 0, title: 'Introduction to Okrika', level: 'beginner', duration: '10 minutes' },
          { id: 1, title: 'Lesson 1: Basic Greetings', level: 'beginner', duration: '15 minutes' },
          { id: 2, title: 'Pronouns', level: 'beginner', duration: '20 minutes' },
        ])
        setStories([{ id: 0, title: 'Introduction in Okrika', level: 'beginner', readingTime: '5 minutes' }])
      })
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    if (!user) return
    setProgressLoading(true)

    const run = async () => {
      try {
        const { data: lessonRows, error: lessonError } = await supabase
          .from('lesson_progress')
          .select('lesson_id, completed')
          .eq('user_id', user.id)

        if (!lessonError && Array.isArray(lessonRows)) {
          const completedSet = new Set(lessonRows.filter((r) => r.completed).map((r) => r.lesson_id))
          setCompletedLessonIds(completedSet)
        }
      } catch (e) {
        // If tables/policies aren't ready yet, show empty progress.
        setCompletedLessonIds(new Set())
      }

      try {
        const { data: storyRows, error: storyError } = await supabase
          .from('story_progress')
          .select('story_id, completed')
          .eq('user_id', user.id)

        if (!storyError && Array.isArray(storyRows)) {
          const completedSet = new Set(storyRows.filter((r) => r.completed).map((r) => r.story_id))
          setCompletedStoryIds(completedSet)
        }
      } catch (e) {
        setCompletedStoryIds(new Set())
      } finally {
        setProgressLoading(false)
      }
    }

    run()
  }, [user])

  if (loading) {
    return (
      <div className="profile-page">
        <div className="profile-loading">
          <div className="loading-spinner" />
          <p>Loading profile...</p>
        </div>
      </div>
    )
  }

  const displayEmail = user?.email || '—'
  const displayName =
    user?.user_metadata?.display_name ||
    user?.user_metadata?.name ||
    (user?.email ? user.email.split('@')[0] : '')

  const completedLessons = lessons.filter((l) => completedLessonIds.has(l.id))
  const completedStoriesList = stories.filter((s) => completedStoryIds.has(s.id))

  const lessonsCompletedCount = completedLessons.length
  const storiesCompletedCount = completedStoriesList.length

  return (
    <div className="profile-page">
      <div className="profile-container">
        <h1 className="profile-heading">My Profile</h1>

        {!user ? (
          <div className="profile-empty">
            <p style={{ marginBottom: '1rem' }}>Log in to save your progress.</p>
            <button type="button" className="profile-cta" onClick={() => navigate('/login')}>
              Go to login →
            </button>
          </div>
        ) : (
          <div className="profile-card">
          <div className="profile-avatar">
            <span className="profile-avatar-placeholder">
              {displayName ? displayName.charAt(0).toUpperCase() : '?'}
            </span>
          </div>
          <div className="profile-info">
            <h2 className="profile-name">{displayName || 'Learner'}</h2>
            <p className="profile-email">{displayEmail}</p>
            <p className="profile-joined">
              {user.created_at ? new Date(user.created_at).toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : ''}
            </p>
            <div className="profile-stats">
              <div className="profile-stat">
                <span className="profile-stat-value">{0}</span>
                <span className="profile-stat-label">Day streak</span>
              </div>
              <div className="profile-stat">
                <span className="profile-stat-value">{lessonsCompletedCount}</span>
                <span className="profile-stat-label">Lessons completed</span>
              </div>
              <div className="profile-stat">
                <span className="profile-stat-value">{storiesCompletedCount}</span>
                <span className="profile-stat-label">Stories completed</span>
              </div>
            </div>
          </div>
        </div>
        )}

        {/* Completed lessons */}
        <section className="profile-section">
          <h2 className="profile-section-title">Completed Lessons</h2>
          {user && progressLoading ? (
            <p className="profile-empty">Loading completed lessons...</p>
          ) : completedLessons.length === 0 ? (
            <p className="profile-empty">No lessons completed yet. Start learning!</p>
          ) : (
            <ul className="profile-lesson-list">
              {completedLessons.map((lesson) => (
                <li
                  key={lesson.id}
                  className="profile-lesson-item"
                  onClick={() => navigate(`/lessons/${lesson.id}`)}
                >
                  <span className="profile-lesson-check">✓</span>
                  <div className="profile-lesson-details">
                    <span className="profile-lesson-title">{lesson.title}</span>
                    <span className="profile-lesson-meta">
                      {lesson.level} · {lesson.duration}
                    </span>
                  </div>
                  <span className="profile-lesson-arrow">→</span>
                </li>
              ))}
            </ul>
          )}
          <button
            type="button"
            className="profile-cta"
            onClick={() => navigate('/lessons')}
          >
            {completedLessons.length === 0 ? 'Browse lessons' : 'Continue learning'} →
          </button>
        </section>

        {/* Completed stories */}
        <section className="profile-section">
          <h2 className="profile-section-title">Completed Stories</h2>
          {user && progressLoading ? (
            <p className="profile-empty">Loading completed stories...</p>
          ) : completedStoriesList.length === 0 ? (
            <p className="profile-empty">No stories completed yet.</p>
          ) : (
            <ul className="profile-lesson-list">
              {completedStoriesList.map((story) => (
                <li
                  key={story.id}
                  className="profile-lesson-item"
                  onClick={() => navigate(`/stories/${story.id}`)}
                >
                  <span className="profile-lesson-check">✓</span>
                  <div className="profile-lesson-details">
                    <span className="profile-lesson-title">{story.title}</span>
                    <span className="profile-lesson-meta">
                      {story.level} · {story.readingTime}
                    </span>
                  </div>
                  <span className="profile-lesson-arrow">→</span>
                </li>
              ))}
            </ul>
          )}
          <button
            type="button"
            className="profile-cta profile-cta-secondary"
            onClick={() => navigate('/stories')}
          >
            Browse stories →
          </button>
        </section>
      </div>
    </div>
  )
}

export default Profile
