import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import AudioPlayer from '../components/AudioPlayer'
import { supabase } from '../lib/supabaseClient'
import './LessonDetail.css'

const LessonDetail = () => {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const [lesson, setLesson] = useState(null)
  const [loading, setLoading] = useState(true)
  const [currentSection, setCurrentSection] = useState(0)
  const [currentPart, setCurrentPart] = useState(0) // For lesson 2's three-part structure
  const [currentQuestion, setCurrentQuestion] = useState(0) // For quiz
  const [selectedAnswer, setSelectedAnswer] = useState(null) // For quiz
  const [showAnswer, setShowAnswer] = useState(false) // For quiz
  const [expandedConjugations, setExpandedConjugations] = useState({}) // Track expanded conjugations: {itemIndex-tense: true/false}
  const [userId, setUserId] = useState(null)

  useEffect(() => {
    fetchLesson()
  }, [lessonId])

  useEffect(() => {
    let unsubscribe = null
    supabase.auth
      .getUser()
      .then(({ data: { user } }) => setUserId(user?.id ?? null))
      .catch(() => setUserId(null))

    const { data } = supabase.auth.onAuthStateChange((_event, session) => {
      setUserId(session?.user?.id ?? null)
    })

    unsubscribe = data?.subscription
    return () => {
      try {
        if (unsubscribe?.unsubscribe) unsubscribe.unsubscribe()
      } catch (e) {}
    }
  }, [])

  useEffect(() => {
    // Reset quiz state when changing parts
    setCurrentQuestion(0)
    setSelectedAnswer(null)
    setShowAnswer(false)
  }, [currentPart])

  const fetchLesson = async () => {
    try {
      const response = await fetch(`/api/lessons/${lessonId}`)
      if (response.ok) {
        const data = await response.json()
        setLesson(data)
      } else {
        // Fallback to default lesson data
        setLesson(getDefaultLesson(parseInt(lessonId)))
      }
    } catch (error) {
      console.error('Error fetching lesson:', error)
      setLesson(getDefaultLesson(parseInt(lessonId)))
    } finally {
      setLoading(false)
    }
  }

  const getDefaultLesson = (id) => {
    const lessons = {
      0: {
        id: 0,
        title: 'Introduction to Okrika',
        level: 'beginner',
        description: 'Welcome to learning Okrika! Get started with an introduction to the language.',
        content: {
          sections: [
            {
              title: 'Welcome!',
              type: 'text',
              content: 'Welcome to Learn Okrika! This platform is designed to help you learn the beautiful Okrika language from Rivers State, Nigeria.'
            },
            {
              title: 'About the Okrika Language',
              type: 'text',
              content: 'Okrika is part of the Ijo (Ijaw) language family, spoken primarily in Rivers State, Nigeria. Learning Okrika connects you with a rich cultural heritage and vibrant community.'
            },
            {
              title: 'How to Use This Platform',
              type: 'text',
              content: 'Each lesson contains words, phrases, and sentences. Practice pronunciation, study the vocabulary, and complete exercises to master the language.'
            }
          ]
        }
      },
      1: {
        id: 1,
        title: 'Lesson 1: Basic Greetings',
        level: 'beginner',
        description: 'Learn essential greetings and how to say hello in Okrika',
        content: {
          sections: [
            {
              title: 'Common Greetings',
              type: 'vocabulary',
              items: [
                { okrika: 'Íḅásà', english: 'Good morning', example: 'Íḅásà, kí ḅírí ḅí?', exampleTranslation: 'Good morning, how are you?' },
                { okrika: 'Íyá', english: 'Good afternoon', example: 'Íyá, bírí ḅí?', exampleTranslation: 'Good afternoon, how are you?' },
                { okrika: 'Íyé', english: 'Good evening', example: 'Íyé, kí ḅírí ḅí?', exampleTranslation: 'Good evening, how was your day?' },
                { okrika: 'Bóḅó', english: 'Hello', example: 'Bóḅó, mẹ́ ḅí!', exampleTranslation: 'Hello, my friend!' }
              ]
            },
            {
              title: 'How Are You?',
              type: 'phrases',
              items: [
                { okrika: 'Kí ḅírí ḅí?', english: 'How are you?', example: 'Kí ḅírí ḅí gbá?', exampleTranslation: 'How are you today?' },
                { okrika: 'Mẹ́ ḅírí', english: 'I am fine', example: 'Mẹ́ ḅírí, ḅá ḅí', exampleTranslation: 'I am fine, thank you.' },
                { okrika: 'ḅá ḅí', english: 'Thank you', example: 'ḅá ḅí púrú', exampleTranslation: 'Thank you very much!' }
              ]
            },
            {
              title: 'Practice Sentences',
              type: 'sentences',
              items: [
                { okrika: 'Íḅásà, kí ḅírí ḅí?', english: 'Good morning, how are you?', example: 'Íḅásà, kí ḅírí ḅí?', exampleTranslation: 'Good morning, how are you?' },
                { okrika: 'Mẹ́ ḅírí, ḅá ḅí. Kí ḅírí ḅí wẹ?', english: 'I am fine, thank you. How about you?', example: 'Mẹ́ ḅírí, ḅá ḅí. Kí ḅírí ḅí wẹ?', exampleTranslation: 'I am fine, thank you. How about you?' },
                { okrika: 'ḅó ḅírí gbá!', english: 'Have a nice day!', example: 'ḅó ḅírí gbá!', exampleTranslation: 'Have a nice day!' }
              ]
            }
          ]
        }
      }
    }
    return lessons[id] || lessons[1]
  }

  // Check if lesson has parts structure (for lessons 1 and 2)
  const hasParts = lesson?.content?.parts && Array.isArray(lesson.content.parts)
  const parts = hasParts ? lesson.content.parts : []
  const sections = !hasParts ? (lesson?.content?.sections || []) : []
  
  // Get current part or section data
  const currentPartData = hasParts ? parts[currentPart] : null
  const currentSectionData = !hasParts ? sections[currentSection] : null

  // Quiz handlers
  const handleAnswerSelect = (answer) => {
    if (showAnswer) return // Don't allow selection after answer is shown
    setSelectedAnswer(answer)
    setShowAnswer(true)
  }

  const nextQuestion = () => {
    const quizPart = parts.find(p => p.type === 'quiz')
    if (currentQuestion < quizPart.questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
      setSelectedAnswer(null)
      setShowAnswer(false)
    }
  }

  const nextPart = () => {
    if (currentPart < parts.length - 1) {
      setCurrentPart(currentPart + 1)
    }
  }

  const prevPart = () => {
    if (currentPart > 0) {
      setCurrentPart(currentPart - 1)
    }
  }

  // Regular section navigation (for non-lesson-2)
  const nextSection = () => {
    if (currentSection < sections.length - 1) {
      setCurrentSection(currentSection + 1)
    }
  }

  const prevSection = () => {
    if (currentSection > 0) {
      setCurrentSection(currentSection - 1)
    }
  }

  // Save progress for logged-in users.
  useEffect(() => {
    const run = async () => {
      if (!userId || !lesson) return
      if (!lessonId) return

      const numericLessonId = Number(lessonId)
      if (Number.isNaN(numericLessonId)) return

      try {
        if (hasParts) {
          const lastPart = currentPart
          const completed = parts.length > 0 && currentPart === parts.length - 1
          await supabase.from('lesson_progress').upsert(
            {
              user_id: userId,
              lesson_id: numericLessonId,
              last_part: lastPart,
              completed,
            },
            { onConflict: 'user_id,lesson_id' }
          )
        } else {
          const lastPart = currentSection
          const completed = sections.length > 0 && currentSection === sections.length - 1
          await supabase.from('lesson_progress').upsert(
            {
              user_id: userId,
              lesson_id: numericLessonId,
              last_part: lastPart,
              completed,
            },
            { onConflict: 'user_id,lesson_id' }
          )
        }
      } catch (e) {
        // If tables/policies aren't ready yet, don't crash the UI.
        // eslint-disable-next-line no-console
        console.error('Failed to save lesson progress:', e?.message || e)
      }
    }

    run()
  }, [userId, lessonId, lesson, hasParts, currentPart, currentSection, parts.length, sections.length])

  if (loading) {
    return (
      <div className="lesson-loading">
        <div className="loading-spinner"></div>
        <p>Loading lesson...</p>
      </div>
    )
  }

  if (!lesson) {
    return (
      <div className="lesson-error">
        <h2>Lesson not found</h2>
        <button onClick={() => navigate('/lessons')}>Back to Lessons</button>
      </div>
    )
  }

  return (
    <div className="lesson-detail-page">
        <div className="lesson-detail-container">
          <div className="lesson-header">
            <button className="back-button" onClick={() => navigate('/lessons')}>
              ← Back to Lessons
            </button>
            <div className="lesson-title-section">
              <span className="lesson-badge">{lesson.level}</span>
              <h1>{lesson.title}</h1>
              <p className="lesson-description">{lesson.description}</p>
            </div>
          </div>

          {/* Progress bar */}
          {hasParts ? (
            <div className="lesson-progress">
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${((currentPart + 1) / parts.length) * 100}%` }}
                ></div>
              </div>
              <p className="progress-text">
                Part {currentPart + 1} of {parts.length}
              </p>
            </div>
          ) : (
            <div className="lesson-progress">
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${((currentSection + 1) / sections.length) * 100}%` }}
                ></div>
              </div>
              <p className="progress-text">
                Section {currentSection + 1} of {sections.length}
              </p>
            </div>
          )}

          {/* Part navigation tabs */}
          {hasParts && (
            <div className="part-navigation">
              {parts.map((part, index) => (
                <button
                  key={index}
                  className={`part-tab ${currentPart === index ? 'active' : ''}`}
                  onClick={() => setCurrentPart(index)}
                >
                  {part.title}
                </button>
              ))}
            </div>
          )}

          <div className="lesson-content">
            {/* Text Part */}
            {hasParts && currentPartData?.type === 'text' && (
              <div className="lesson-section">
                <h2>{currentPartData.title}</h2>
                <div className="text-content">
                  <p style={{ whiteSpace: 'pre-line' }}>{currentPartData.content}</p>
                </div>
              </div>
            )}

            {/* Vocabulary Part */}
            {hasParts && currentPartData?.type === 'vocabulary' && (
              <div className="lesson-section">
                <h2>{currentPartData.title}</h2>
                <div className="vocabulary-list">
                  {currentPartData.items?.map((item, index) => (
                    <div key={index} className="vocabulary-item">
                      <div className="vocab-main">
                        <div className="vocab-okrika">
                          <div className="vocab-okrika-header">
                            <h3>{item.okrika}</h3>
                            {item.audioUrl && (
                              <AudioPlayer 
                                audioUrl={item.audioUrl} 
                                label={`Play pronunciation of "${item.okrika}"`}
                              />
                            )}
                          </div>
                          {item.singular && item.plural && (
                            <div className="vocab-forms">
                              <span className="form-label">Singular:</span> {item.singular}
                              <span className="form-separator">|</span>
                              <span className="form-label">Plural:</span> {item.plural}
                            </div>
                          )}
                        </div>
                        <div className="vocab-english">
                          <p>{item.english}</p>
                        </div>
                      </div>
                      {item.example && (
                        <div className="vocab-example">
                          <div className="example-okrika">
                            <strong>Example:</strong> {item.example}
                            {item.exampleAudioUrl && (
                              <AudioPlayer 
                                audioUrl={item.exampleAudioUrl} 
                                label={`Play pronunciation of example: "${item.example}"`}
                              />
                            )}
                          </div>
                          {item.form && (
                            <div className="form-indicator">
                              <strong>Form:</strong> {item.form === 'singular' ? 'Singular' : 'Plural'}
                            </div>
                          )}
                          {item.exampleTranslation && (
                            <div className="example-translation">
                              <strong>Translation:</strong> {item.exampleTranslation}
                            </div>
                          )}
                        </div>
                      )}
                      {item.conjugations && (
                        <div className="vocab-conjugations">
                          <h4 className="conjugations-title">Conjugations:</h4>
                          <div className="conjugations-dropdown">
                            {item.conjugations.presentContinuous?.example && (
                              <div className="conjugation-dropdown-item">
                                <button 
                                  className="conjugation-dropdown-header"
                                  onClick={() => {
                                    const key = `${index}-presentContinuous`
                                    setExpandedConjugations(prev => ({
                                      ...prev,
                                      [key]: !prev[key]
                                    }))
                                  }}
                                >
                                  <span className="conjugation-label">Present Continuous:</span>
                                  <span className="dropdown-arrow">
                                    {expandedConjugations[`${index}-presentContinuous`] ? '▼' : '▶'}
                                  </span>
                                </button>
                                {expandedConjugations[`${index}-presentContinuous`] && (
                                  <div className="conjugation-dropdown-content">
                                    <div className="conjugation-example">
                                      <strong>Example:</strong> {item.conjugations.presentContinuous.example}
                                      {item.conjugations.presentContinuous.audioUrl && (
                                        <AudioPlayer 
                                          audioUrl={item.conjugations.presentContinuous.audioUrl} 
                                          label={`Play pronunciation of example: "${item.conjugations.presentContinuous.example}"`}
                                        />
                                      )}
                                      {item.conjugations.presentContinuous.exampleTranslation && (
                                        <span className="conjugation-example-translation"> - {item.conjugations.presentContinuous.exampleTranslation}</span>
                                      )}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}
                            {item.conjugations.pastTense?.example && (
                              <div className="conjugation-dropdown-item">
                                <button 
                                  className="conjugation-dropdown-header"
                                  onClick={() => {
                                    const key = `${index}-pastTense`
                                    setExpandedConjugations(prev => ({
                                      ...prev,
                                      [key]: !prev[key]
                                    }))
                                  }}
                                >
                                  <span className="conjugation-label">Past Tense:</span>
                                  <span className="dropdown-arrow">
                                    {expandedConjugations[`${index}-pastTense`] ? '▼' : '▶'}
                                  </span>
                                </button>
                                {expandedConjugations[`${index}-pastTense`] && (
                                  <div className="conjugation-dropdown-content">
                                    <div className="conjugation-example">
                                      <strong>Example:</strong> {item.conjugations.pastTense.example}
                                      {item.conjugations.pastTense.audioUrl && (
                                        <AudioPlayer 
                                          audioUrl={item.conjugations.pastTense.audioUrl} 
                                          label={`Play pronunciation of example: "${item.conjugations.pastTense.example}"`}
                                        />
                                      )}
                                      {item.conjugations.pastTense.exampleTranslation && (
                                        <span className="conjugation-example-translation"> - {item.conjugations.pastTense.exampleTranslation}</span>
                                      )}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}
                            {item.conjugations.pastParticiple?.example && (
                              <div className="conjugation-dropdown-item">
                                <button 
                                  className="conjugation-dropdown-header"
                                  onClick={() => {
                                    const key = `${index}-pastParticiple`
                                    setExpandedConjugations(prev => ({
                                      ...prev,
                                      [key]: !prev[key]
                                    }))
                                  }}
                                >
                                  <span className="conjugation-label">Past Participle:</span>
                                  <span className="dropdown-arrow">
                                    {expandedConjugations[`${index}-pastParticiple`] ? '▼' : '▶'}
                                  </span>
                                </button>
                                {expandedConjugations[`${index}-pastParticiple`] && (
                                  <div className="conjugation-dropdown-content">
                                    <div className="conjugation-example">
                                      <strong>Example:</strong> {item.conjugations.pastParticiple.example}
                                      {item.conjugations.pastParticiple.audioUrl && (
                                        <AudioPlayer 
                                          audioUrl={item.conjugations.pastParticiple.audioUrl} 
                                          label={`Play pronunciation of example: "${item.conjugations.pastParticiple.example}"`}
                                        />
                                      )}
                                      {item.conjugations.pastParticiple.exampleTranslation && (
                                        <span className="conjugation-example-translation"> - {item.conjugations.pastParticiple.exampleTranslation}</span>
                                      )}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}
                            {item.conjugations.future?.example && (
                              <div className="conjugation-dropdown-item">
                                <button 
                                  className="conjugation-dropdown-header"
                                  onClick={() => {
                                    const key = `${index}-future`
                                    setExpandedConjugations(prev => ({
                                      ...prev,
                                      [key]: !prev[key]
                                    }))
                                  }}
                                >
                                  <span className="conjugation-label">Future:</span>
                                  <span className="dropdown-arrow">
                                    {expandedConjugations[`${index}-future`] ? '▼' : '▶'}
                                  </span>
                                </button>
                                {expandedConjugations[`${index}-future`] && (
                                  <div className="conjugation-dropdown-content">
                                    <div className="conjugation-example">
                                      <strong>Example:</strong> {item.conjugations.future.example}
                                      {item.conjugations.future.audioUrl && (
                                        <AudioPlayer 
                                          audioUrl={item.conjugations.future.audioUrl} 
                                          label={`Play pronunciation of example: "${item.conjugations.future.example}"`}
                                        />
                                      )}
                                      {item.conjugations.future.exampleTranslation && (
                                        <span className="conjugation-example-translation"> - {item.conjugations.future.exampleTranslation}</span>
                                      )}
                                    </div>
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Part 2: Quiz */}
            {hasParts && currentPartData?.type === 'quiz' && (
              <div className="lesson-section quiz-section">
                <h2>{currentPartData.title}</h2>
                {currentPartData.questions && currentPartData.questions.length > 0 && (
                  <div className="quiz-container">
                    <div className="question-header">
                      <span className="question-number">
                        Question {currentQuestion + 1} of {currentPartData.questions.length}
                      </span>
                    </div>
                    <div className="question-text">
                      <h3>{currentPartData.questions[currentQuestion].question}</h3>
                    </div>
                    <div className="quiz-options">
                      {currentPartData.questions[currentQuestion].options.map((option, index) => {
                        const isSelected = selectedAnswer === option
                        const isCorrect = option === currentPartData.questions[currentQuestion].correctAnswer
                        const showFeedback = showAnswer
                        let optionClass = ''
                        
                        if (showFeedback) {
                          // When feedback is shown, highlight correct answer in green
                          if (isCorrect) {
                            optionClass = 'correct'
                          } else if (isSelected && !isCorrect) {
                            // Wrong selected answer shows in red
                            optionClass = 'incorrect'
                          }
                        } else if (isSelected) {
                          // Before feedback, show selected state
                          optionClass = 'selected'
                        }
                        
                        return (
                          <button
                            key={index}
                            className={`quiz-option ${optionClass}`}
                            onClick={() => handleAnswerSelect(option)}
                            disabled={showFeedback}
                          >
                            {option}
                          </button>
                        )
                      })}
                    </div>
                    {showAnswer && (
                      <div className="quiz-feedback">
                        {selectedAnswer === currentPartData.questions[currentQuestion].correctAnswer ? (
                          <p className="feedback-correct">✓ Correct! Well done!</p>
                        ) : (
                          <p className="feedback-incorrect">✗ Incorrect. The correct answer is: <strong>{currentPartData.questions[currentQuestion].correctAnswer}</strong></p>
                        )}
                        {currentQuestion < currentPartData.questions.length - 1 && (
                          <button className="quiz-next-button" onClick={nextQuestion}>
                            Next Question →
                          </button>
                        )}
                      </div>
                    )}
                  </div>
                )}
              </div>
            )}

            {/* Part 3: Dialogue */}
            {hasParts && currentPartData?.type === 'dialogue' && (
              <div className="lesson-section dialogue-section">
                <h2>{currentPartData.title}</h2>
                <div className="dialogues-list">
                  {currentPartData.dialogues?.map((dialogue, index) => (
                    <div key={index} className="dialogue-item">
                      <h3 className="dialogue-title">{dialogue.title}</h3>
                      <div className="dialogue-exchanges">
                        {dialogue.exchanges.map((exchange, exIndex) => (
                          <div key={exIndex} className="dialogue-exchange">
                            <div className="exchange-speaker">{exchange.speaker}:</div>
                            <div className="exchange-content">
                              <div className="exchange-okrika">
                                <span>{exchange.okrika}</span>
                                {exchange.audioUrl && (
                                  <AudioPlayer 
                                    audioUrl={exchange.audioUrl} 
                                    label={`Play pronunciation of "${exchange.okrika}"`}
                                  />
                                )}
                              </div>
                              <div className="exchange-english">{exchange.english}</div>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Regular lesson structure (lessons without parts) */}
            {!hasParts && currentSectionData && (
              <div className="lesson-section">
                <h2>{currentSectionData.title}</h2>
                
                {currentSectionData.type === 'text' && (
                  <div className="text-content">
                    <p>{currentSectionData.content}</p>
                  </div>
                )}

                {(currentSectionData.type === 'vocabulary' || 
                  currentSectionData.type === 'phrases' || 
                  currentSectionData.type === 'sentences') && (
                  <div className="vocabulary-list">
                    {currentSectionData.items?.map((item, index) => (
                      <div key={index} className="vocabulary-item">
                        <div className="vocab-main">
                          <div className="vocab-okrika">
                            <div className="vocab-okrika-header">
                              <h3>{item.okrika}</h3>
                              {item.audioUrl && (
                                <AudioPlayer 
                                  audioUrl={item.audioUrl} 
                                  label={`Play pronunciation of "${item.okrika}"`}
                                />
                              )}
                            </div>
                          </div>
                          <div className="vocab-english">
                            <p>{item.english}</p>
                          </div>
                        </div>
                        {item.example && (
                          <div className="vocab-example">
                            <div className="example-okrika">
                              <strong>Example:</strong> {item.example}
                              {item.exampleAudioUrl && (
                                <AudioPlayer 
                                  audioUrl={item.exampleAudioUrl} 
                                  label={`Play pronunciation of example: "${item.example}"`}
                                />
                              )}
                            </div>
                            {item.exampleTranslation && (
                              <div className="example-translation">
                                <strong>Translation:</strong> {item.exampleTranslation}
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Navigation buttons */}
          {hasParts ? (
            <div className="lesson-navigation">
              <button 
                className="nav-button prev" 
                onClick={prevPart}
                disabled={currentPart === 0}
              >
                ← Previous
              </button>
              <button 
                className="nav-button next" 
                onClick={nextPart}
                disabled={currentPart === parts.length - 1}
              >
                Next →
              </button>
            </div>
          ) : (
            <div className="lesson-navigation">
              <button 
                className="nav-button prev" 
                onClick={prevSection}
                disabled={currentSection === 0}
              >
                ← Previous
              </button>
              <button 
                className="nav-button next" 
                onClick={nextSection}
                disabled={currentSection === sections.length - 1}
              >
                Next →
              </button>
            </div>
          )}

          {/* Completion message */}
          {hasParts && currentPart === parts.length - 1 && (
            <div className="lesson-complete">
              <h3>🎉 Lesson Complete!</h3>
              <p>Great job completing this lesson. Keep practicing!</p>
              <button className="complete-button" onClick={() => navigate('/lessons')}>
                Back to Lessons
              </button>
            </div>
          )}

          {!hasParts && currentSection === sections.length - 1 && (
            <div className="lesson-complete">
              <h3>🎉 Lesson Complete!</h3>
              <p>Great job completing this lesson. Keep practicing!</p>
              <button className="complete-button" onClick={() => navigate('/lessons')}>
                Back to Lessons
              </button>
            </div>
          )}
        </div>
      </div>
  )
}

export default LessonDetail
