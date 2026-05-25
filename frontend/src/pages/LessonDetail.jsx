import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import AudioPlayer from '../components/AudioPlayer'
import { supabase } from '../lib/supabaseClient'
import './LessonDetail.css'

function shuffleArray(items) {
  const copy = [...items]
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[copy[i], copy[j]] = [copy[j], copy[i]]
  }
  return copy
}

function prepareQuizQuestions(questions) {
  return shuffleArray(questions).map((q) => ({
    ...q,
    options: shuffleArray(q.options),
  }))
}

function extractQuizWord(question) {
  const match = question.match(/"([^"]+)"/)
  return match ? match[1] : null
}

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
  const [quizQuestions, setQuizQuestions] = useState([]) // Shuffled questions + options
  const [incorrectAnswers, setIncorrectAnswers] = useState([]) // Mistakes during quiz
  const [expandedConjugations, setExpandedConjugations] = useState({}) // Track expanded conjugations: {itemIndex-tense: true/false}
  const [userId, setUserId] = useState(null)

  useEffect(() => {
    fetchLesson()
  }, [lessonId])

  useEffect(() => {
    if (!supabase) {
      setUserId(null)
      return
    }

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
    setIncorrectAnswers([])

    const part = lesson?.content?.parts?.[currentPart]
    if (part?.type === 'quiz' && part.questions?.length) {
      setQuizQuestions(prepareQuizQuestions(part.questions))
    } else {
      setQuizQuestions([])
    }
  }, [currentPart, lesson])

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
    const placeholders = {
      2: {
        id: 2,
        title: 'Pronouns',
        level: 'beginner',
        description: 'Learn personal pronouns in Okrika',
        content: {
          sections: [
            {
              title: 'Coming soon',
              type: 'text',
              content: 'This lesson content will load automatically once the backend API is reachable in production.'
            }
          ]
        }
      },
      3: {
        id: 3,
        title: 'Common Verbs',
        level: 'beginner',
        description: 'Learn essential verbs and their conjugations in Okrika',
        content: {
          sections: [
            {
              title: 'Coming soon',
              type: 'text',
              content: 'This lesson content will load automatically once the backend API is reachable in production.'
            }
          ]
        }
      },
      4: {
        id: 4,
        title: 'Family and Relationships',
        level: 'beginner',
        description: 'Learn vocabulary for family members and relationships',
        content: {
          sections: [
            {
              title: 'Coming soon',
              type: 'text',
              content: 'This lesson content will load automatically once the backend API is reachable in production.'
            }
          ]
        }
      },
      5: {
        id: 5,
        title: 'Food and Dining',
        level: 'intermediate',
        description: 'Essential phrases and vocabulary for food and dining',
        content: {
          sections: [
            {
              title: 'Coming soon',
              type: 'text',
              content: 'This lesson content will load automatically once the backend API is reachable in production.'
            }
          ]
        }
      },
      7: {
        id: 7,
        title: 'Showing Time',
        level: 'beginner',
        description: 'Learn words and phrases for expressing time in Okrika.',
        duration: '15 minutes',
        content: {
          parts: [
            {
              part: 1,
              title: 'Learn time words',
              type: 'vocabulary',
              items: [
                { okrika: 'míókù', english: 'now; this moment', partOfSpeech: 'adverb', definition: 'At the present time', example: 'Míókù í bô au?', exampleTranslation: 'Are you coming now?' },
                { okrika: 'kélédīkī', english: 'afterwards; sometime later', partOfSpeech: 'adverb', definition: 'At a later or future time', example: 'kélédīkī à mèngí bû bià?', exampleTranslation: 'Later I will drink water' },
                { okrika: 'mímgbà', english: 'today', partOfSpeech: 'noun', definition: 'On or in the course of this present day', example: 'Mímgbà ò dàdíkì gíén mè', exampleTranslation: 'He wrote his exam today' },
                { okrika: 'sìméògbò', english: 'while', partOfSpeech: 'conjunction', definition: 'During the time that', example: 'Sìméògbò í ómì, bô yéfí', exampleTranslation: 'While you are here, come and eat' },
                { okrika: 'bịá', english: 'yesterday', partOfSpeech: 'noun', definition: 'The day before today', example: 'Bịá ó só mè', exampleTranslation: 'He left yesterday' },
                { okrika: 'bá', english: 'tomorrow', partOfSpeech: 'noun', definition: 'The day after today', example: 'Bá í múñ be?', exampleTranslation: 'Will you go tomorrow?' },
                { okrika: 'Ḍíñ-ógbò', english: 'midnight', partOfSpeech: 'noun', definition: 'The middle of the night' },
                { okrika: 'gbásó', english: 'forever', partOfSpeech: 'adverb', definition: 'For all time; eternally' },
                { okrika: 'N̄gịsị̀', english: 'never', partOfSpeech: 'adverb', definition: 'At no time; not ever' },
                { okrika: 'Ólómú sịkị', english: 'ancient times', partOfSpeech: 'phrase', definition: 'A long time ago in the past' },
                { okrika: 'Sị́kị́ná sị́kị́ná', english: 'as time goes on; eventually; time and again', partOfSpeech: 'phrase', definition: 'Over time; in the end; repeatedly' },
                { okrika: 'Sị́kị́ mámgbà', english: 'every time', partOfSpeech: 'phrase', definition: 'On each occasion; always when' },
                { okrika: 'Ótókú', english: 'noon', partOfSpeech: 'noun', definition: 'Twelve o\'clock in the day; midday' },
                { okrika: 'Súsú bẹ́-ẹ́né', english: 'three days ago', partOfSpeech: 'phrase', definition: 'Three days before today' },
                { okrika: 'Básó', english: 'early morning', partOfSpeech: 'noun', definition: 'The first part of the morning' },
                { okrika: 'Dèdè fúñ fúñ', english: 'very early in the morning', partOfSpeech: 'phrase', definition: 'At dawn; very early before sunrise' },
                { okrika: 'Bé réñ-béré-éné', english: 'day before yesterday', partOfSpeech: 'phrase', definition: 'Two days ago' },
                { okrika: 'Bá bọ́rọ́ bé réñ-béré-éné', english: 'day after tomorrow', partOfSpeech: 'phrase', definition: 'Two days from now' },
                { okrika: 'Dị́ñ', english: 'night', partOfSpeech: 'noun', definition: 'The period of darkness between sunset and sunrise' },
                { okrika: 'Éné tíḅì', english: 'daily', partOfSpeech: 'adverb', definition: 'Every day; each day' },
                { okrika: 'Éné góyè gòyè, éné máñgbà', english: 'every day', partOfSpeech: 'phrase', definition: 'Each day without exception' },
                { okrika: 'Éné kákà (kúḅù)', english: 'day time', partOfSpeech: 'phrase', definition: 'The time when it is light; daytime' },
                { okrika: 'Dàsìkì', english: 'sometimes', partOfSpeech: 'adverb', definition: 'On some occasions; occasionally' },
                { okrika: 'Bàkà síkí (bụ̀)', english: 'most times', partOfSpeech: 'phrase', definition: 'Usually; on most occasions' },
                { okrika: 'Sị́kị́ góyè gòyè', english: 'regularly', partOfSpeech: 'adverb', definition: 'At consistent intervals; habitually' },
                { okrika: 'Sịkị fámá', english: 'delay', partOfSpeech: 'noun', definition: 'A period of time by which something is late' },
                { okrika: 'Sịkị fámá ká bù', english: 'immediately', partOfSpeech: 'adverb', definition: 'At once; without delay' }
              ]
            }
          ]
        }
      },
      8: {
        id: 8,
        title: 'Question Words',
        level: 'beginner',
        description: 'Learn how to ask questions in Okrika with who, what, when, where, and whom.',
        duration: '15 minutes',
        content: {
          parts: [
            {
              part: 1,
              title: 'Learn question words',
              type: 'vocabulary',
              items: [
                { okrika: 'ñdèjù', english: 'where', partOfSpeech: 'pronoun', definition: 'Asking for information specifying a location', example: 'Ñdèjù ìní ñwòñ mũñ àù?', exampleTranslation: 'Where are they going?' },
                { okrika: 'ñdè sịkị', english: 'when', partOfSpeech: 'pronoun', definition: 'Asking about time', example: 'Ñdè sịkị í bô?', exampleTranslation: 'When are you coming?' },
                { okrika: 'ñdè bọ̀', english: 'who', partOfSpeech: 'pronoun', definition: 'Asking about a person', example: 'Ñdè bọ̀ ọ́ wú?', exampleTranslation: 'Who is that?' },
                { okrika: 'àṇị̀ bọ̀ mị̀', english: 'whom', partOfSpeech: 'pronoun', definition: 'Asking about which person (object)', example: 'Àṇị̀ bọ̀ mị̀ í kéréní?', exampleTranslation: 'Whom did you greet?' },
                { okrika: 'chèyè', english: 'what', partOfSpeech: 'pronoun', definition: 'Asking about a thing or action', example: 'Chèyè í sọ?', exampleTranslation: 'What did you say?' },
                { okrika: 'chèyè pàkà', english: 'what happened', partOfSpeech: 'phrase', definition: 'Asking about an event or occurrence', example: 'Chèyè pàkà?', exampleTranslation: 'What happened?' },
                { okrika: 'ndàyê', english: 'how many things', partOfSpeech: 'interrogative', definition: 'Asking about the quantity of things', example: '', exampleTranslation: '' },
                { okrika: 'ndàìgbíkì', english: 'how much money', partOfSpeech: 'interrogative', definition: 'Asking about an amount of money', example: '', exampleTranslation: '' }
              ]
            }
          ]
        }
      },
      10: {
        id: 10,
        title: 'Connector Words',
        level: 'beginner',
        description: 'Learn words that link ideas in Okrika — because, also, while, and more.',
        duration: '15 minutes',
        content: {
          parts: [
            {
              part: 1,
              title: 'Learn connector words',
              type: 'vocabulary',
              items: [
                { okrika: 'ànìàtíbí', english: 'because', partOfSpeech: 'conjunction', definition: 'Gives a reason or cause', example: 'À chik-fi-a muñ bìà ànìàtíbí fị́yè ị̀ tàrị̀ àḅẹ̀', exampleTranslation: "I will go to chik-fil-a because I'm hungry" },
                { okrika: 'soni', english: 'also; too', partOfSpeech: 'adverb', definition: 'Adds another idea or includes something more', example: '', exampleTranslation: '' },
                { okrika: 'sìméògbò', english: 'while', partOfSpeech: 'conjunction', definition: 'Links two actions happening at the same time', example: 'Sìméògbò í ómì, bô yéfí', exampleTranslation: 'While you are here, come and eat' },
                { okrika: 'kà', english: 'and; what about', partOfSpeech: 'conjunction', definition: 'Connects ideas or turns the question back to someone', example: 'Í ḅásà. Ìyà èrè ànì Tonye. Írí ka?', exampleTranslation: 'Good morning. My name is Tonye. And you?' },
                { okrika: 'ànì', english: 'that', partOfSpeech: 'pronoun', definition: 'Points to or identifies something already mentioned', example: 'Ànì ìbì mè', exampleTranslation: 'That is good' },
                { okrika: 'ììñ', english: 'yes', partOfSpeech: 'particle', definition: 'Affirms or agrees before continuing a thought', example: 'Ììñ, À bùkùró mà bìà', exampleTranslation: 'Yes, I will try hard' },
                { okrika: 'Ọ̀kùmà', english: 'but', partOfSpeech: 'conjunction', definition: 'Used to introduce a statement contrasting with a previous statement', example: 'Ọ̀kùmà, ị̀rị̀ yèḍìyè bọ̀-ẹ̀', exampleTranslation: 'But, I am a teacher.' },
                { okrika: 'nwòfá/némíkásè', english: 'if, whether', partOfSpeech: 'conjunction', definition: 'Introduces a conditional clause', example: 'Nwòfá í múñ, à mónō bìà', exampleTranslation: 'If you go, I will sleep' },
                { okrika: 'mị̀ẹ̀ sè', english: 'so that', partOfSpeech: 'adverb', definition: 'In order that', example: 'Àníjú kpọ̀njị́sìmé mị̀ẹ̀ sè ó ọrí bìà', exampleTranslation: 'Sit there so that he will see you' },
                { okrika: 'nà', english: 'and', partOfSpeech: 'conjunction', definition: 'Joins two words, phrases, or clauses together', example: 'Tìtì mà á pékéré mè nà á mùñ Káínè', exampleTranslation: 'Titi answered her and said she was going to Kaine' }
              ]
            }
          ]
        }
      }
    }
    return lessons[id] || placeholders[id] || lessons[1]
  }

  // Check if lesson has parts structure (for lessons 1 and 2)
  const hasParts = lesson?.content?.parts && Array.isArray(lesson.content.parts)
  const parts = hasParts ? lesson.content.parts : []
  const sections = !hasParts ? (lesson?.content?.sections || []) : []
  
  // Get current part or section data
  const currentPartData = hasParts ? parts[currentPart] : null
  const currentSectionData = !hasParts ? sections[currentSection] : null

  // Quiz handlers
  const handleAnswerSelect = (answer, question) => {
    if (showAnswer) return // Don't allow selection after answer is shown
    setSelectedAnswer(answer)
    setShowAnswer(true)

    if (answer !== question.correctAnswer) {
      const word = extractQuizWord(question.question)
      const mistake = {
        id: question.id ?? question.question,
        word: word || question.question,
        question: question.question,
        yourAnswer: answer,
        correctAnswer: question.correctAnswer,
      }
      setIncorrectAnswers((prev) =>
        prev.some((m) => m.id === mistake.id) ? prev : [...prev, mistake]
      )
    }
  }

  const nextQuestion = () => {
    if (currentQuestion < quizQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
      setSelectedAnswer(null)
      setShowAnswer(false)
    }
  }

  const activeQuizQuestion = quizQuestions[currentQuestion]

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
      if (!supabase) return
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
                            {item.partOfSpeech && (
                              <span className="vocab-part-of-speech">({item.partOfSpeech})</span>
                            )}
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
                      <div className="vocab-example">
                        <div className="example-okrika">
                          <strong>Example:</strong> {item.example || ''}
                          {item.example && item.exampleAudioUrl && (
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
                        <div className="example-translation">
                          <strong>Translation:</strong> {item.exampleTranslation || ''}
                        </div>
                      </div>
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
                {quizQuestions.length > 0 && activeQuizQuestion && (
                  <div className="quiz-container">
                    <div className="question-header">
                      <span className="question-number">
                        Question {currentQuestion + 1} of {quizQuestions.length}
                      </span>
                    </div>
                    <div className="question-text">
                      <h3>{activeQuizQuestion.question}</h3>
                    </div>
                    <div className="quiz-options">
                      {activeQuizQuestion.options.map((option, index) => {
                        const isSelected = selectedAnswer === option
                        const isCorrect = option === activeQuizQuestion.correctAnswer
                        const showFeedback = showAnswer
                        let optionClass = ''
                        
                        if (showFeedback) {
                          if (isCorrect) {
                            optionClass = 'correct'
                          } else if (isSelected && !isCorrect) {
                            optionClass = 'incorrect'
                          }
                        } else if (isSelected) {
                          optionClass = 'selected'
                        }
                        
                        return (
                          <button
                            key={index}
                            className={`quiz-option ${optionClass}`}
                            onClick={() => handleAnswerSelect(option, activeQuizQuestion)}
                            disabled={showFeedback}
                          >
                            {option}
                          </button>
                        )
                      })}
                    </div>
                    {showAnswer && (
                      <div className="quiz-feedback">
                        {selectedAnswer === activeQuizQuestion.correctAnswer ? (
                          <p className="feedback-correct">✓ Correct! Well done!</p>
                        ) : (
                          <p className="feedback-incorrect">✗ Incorrect. The correct answer is: <strong>{activeQuizQuestion.correctAnswer}</strong></p>
                        )}
                        {currentQuestion < quizQuestions.length - 1 && (
                          <button className="quiz-next-button" onClick={nextQuestion}>
                            Next Question →
                          </button>
                        )}
                      </div>
                    )}
                    {incorrectAnswers.length > 0 && (
                      <details className="quiz-review-dropdown">
                        <summary className="quiz-review-summary">
                          Review mistakes ({incorrectAnswers.length})
                        </summary>
                        <ul className="quiz-review-list">
                          {incorrectAnswers.map((mistake) => (
                            <li key={mistake.id} className="quiz-review-item">
                              <span className="quiz-review-word">{mistake.word}</span>
                              <span className="quiz-review-detail">
                                You chose <strong>{mistake.yourAnswer}</strong>
                                {' · '}
                                Correct: <strong>{mistake.correctAnswer}</strong>
                              </span>
                            </li>
                          ))}
                        </ul>
                      </details>
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
                              {item.partOfSpeech && (
                                <span className="vocab-part-of-speech">({item.partOfSpeech})</span>
                              )}
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
                        <div className="vocab-example">
                          <div className="example-okrika">
                            <strong>Example:</strong> {item.example || ''}
                            {item.example && item.exampleAudioUrl && (
                              <AudioPlayer 
                                audioUrl={item.exampleAudioUrl} 
                                label={`Play pronunciation of example: "${item.example}"`}
                              />
                            )}
                          </div>
                          <div className="example-translation">
                            <strong>Translation:</strong> {item.exampleTranslation || ''}
                          </div>
                        </div>
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
