import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Header from '../components/Header'
import Footer from '../components/Footer'
import './StoryDetail.css'

const StoryDetail = () => {
  const { storyId } = useParams()
  const navigate = useNavigate()
  const [story, setStory] = useState(null)
  const [loading, setLoading] = useState(true)
  const [vocabulary, setVocabulary] = useState({}) // Dictionary of Okrika words/phrases to English
  const [activeTooltip, setActiveTooltip] = useState(null) // Track which word's tooltip is shown
  const [showFullTranslations, setShowFullTranslations] = useState({}) // Track which sentences show full translation

  useEffect(() => {
    fetchVocabulary()
    fetchStory()
  }, [storyId])

  // Close tooltip when clicking outside
  useEffect(() => {
    const handleClickOutside = () => {
      setActiveTooltip(null)
    }
    if (activeTooltip) {
      document.addEventListener('click', handleClickOutside)
      return () => document.removeEventListener('click', handleClickOutside)
    }
  }, [activeTooltip])

  const fetchVocabulary = async () => {
    // Fallback vocabulary dictionary
    
    const fallbackVocab = {
      'í ḅásà': 'Good morning',
      'ñdè ànì là òkù': 'How are you?',
      'ìbì': 'good',
      'mìébákà': 'Thank you',
      'í ḅòsà': 'Welcome',
      'ñdè íyá fúró sìmè òkù?': 'How is your family?',
      'ì bù dèìñ mè': "I'm alright",
      'dèìñ mè': "I'm alright",
      'soni': 'too / also',
      'írí kà': 'And you',
      'ñde àngà í bò?': 'Where are you from?',
      'ñdè àngà í paka bo?': 'Where are you from?',
      'à àngà mè': 'I live in',
      'ànìjú': 'There',
      'ìyà fúrō àngà mè': 'my family lives',
      'fúrō àngà mè': 'family lives',
      'fìrìnwèngí': 'to work',
      'ànì íbì mè': 'That is good',
      'ànì': 'That/Is',
      'ndè ànì là òkù?': 'How are you?',
      'ììñ': 'Yes',
      'ìrí software engineer': 'I\'m a software engineer',
      'í': 'you',
      'írí': 'you',
      'nyànà': 'to have',
      'ìgbìkì': 'money',
      'à': 'I',
      'némí': 'to know',
      'kélédīkī': 'later',
      'chè': 'what ',
      'dírídáwò': 'study',
      'muñ': 'to go',
      'bìà': '(continuous auxilary)',
      'bùkùró mà': 'try hard',
      'mè': 'past tense/continuous auxilary',
      'yéè': 'to do',
      'ìyà': 'my',
      'íyá': 'your',
      'èrè': 'name',
      'ka': 'what about',
      'àngà': 'to live/lives',
      'ìríma': 'myself',
      'bo': 'come',
      'páká': 'to come out',
      'sùkùlù': 'school',
      'nwon chì\'n': 'to think',
      'ànìàtíbí': 'because',
      'fị́yè ị̀ tàrị̀ àḅẹ̀': 'I\'m hungry',
      'bì': 'to want'

      
  
    



    }
    
    try {
      // Fetch lesson 1 to get vocabulary
      const response = await fetch('/api/lessons/1')
      if (response.ok) {
        const lesson = await response.json()
        const vocabDict = { ...fallbackVocab }
        
        // Extract vocabulary from lesson parts
        if (lesson.content?.parts) {
          lesson.content.parts.forEach(part => {
            if (part.type === 'vocabulary' && part.items) {
              part.items.forEach(item => {
                // Store both the exact phrase and individual words
                const okrikaText = item.okrika.trim()
                vocabDict[okrikaText.toLowerCase()] = item.english
                
                // Also store singular/plural forms if available
                if (item.singular) {
                  vocabDict[item.singular.trim().toLowerCase()] = item.english
                }
                if (item.plural) {
                  vocabDict[item.plural.trim().toLowerCase()] = item.english
                }
              })
            }
          })
        }
        
        setVocabulary(vocabDict)
      } else {
        setVocabulary(fallbackVocab)
      }
    } catch (error) {
      console.error('Error fetching vocabulary:', error)
      setVocabulary(fallbackVocab)
    }
  }

  const fetchStory = async () => {
    try {
      const response = await fetch(`/api/stories/${storyId}`)
      if (response.ok) {
        const data = await response.json()
        console.log('Fetched story:', data) // Debug log
        setStory(data)
      } else {
        console.log('Story not found, using default')
        setStory(getDefaultStory(parseInt(storyId)))
      }
    } catch (error) {
      console.error('Error fetching story:', error)
      setStory(getDefaultStory(parseInt(storyId)))
    } finally {
      setLoading(false)
    }
  }

  const getDefaultStory = (id) => {
    const stories = {
      0: {
        id: 0,
        title: 'A Morning in Okrika',
        level: 'beginner',
        description: 'A simple story about a morning greeting between friends',
        readingTime: '5 minutes',
        content: {
          type: 'dialogue',
          exchanges: [
            {
              speaker: 'Dede',
              okrika: 'Í ḅásà, Tonye! Ñdè ànì là òkù?',
              english: 'Good morning, Tonye! How are you?'
            },
            {
              speaker: 'Tonye',
              okrika: 'Í ḅásà, Dede! Ì bìmé, mìébákà. Ñdè ànì là òkù wẹ?',
              english: 'Good morning, Dede! I am fine, thank you. How are you?'
            }
          ]
        }
      }
    }
    return stories[id] || stories[0]
  }

  // Parse text and make words/phrases clickable
  const parseText = (text, uniquePrefix = '') => {
    if (!text) {
      return [{ type: 'text', content: '' }]
    }
    
    // If vocabulary is empty, just return the text as-is
    if (Object.keys(vocabulary).length === 0) {
      return [{ type: 'text', content: text }]
    }
    
    try {
      // Get phrases sorted by length (longer first to match multi-word phrases)
      const phrases = Object.keys(vocabulary).sort((a, b) => b.length - a.length)
      const result = []
      let i = 0
      let lastTextEnd = 0
      let wordIndex = 0 // Counter for unique word keys
      
      while (i < text.length) {
        let matched = false
        
        // Try to match phrases (longer ones first)
        for (const phrase of phrases) {
          const phraseLower = phrase.toLowerCase().trim()
          if (!phraseLower) continue
          
          const textSlice = text.slice(i).toLowerCase()
          
          // Check if phrase matches at current position
          if (textSlice.startsWith(phraseLower)) {
            // Check word boundaries - allow start of string, after space/punctuation
            // For the end, be more lenient: match if at end OR followed by space/punctuation OR 
            // followed by uppercase letter (new word) OR if it's a complete phrase
            const beforeOk = i === 0 || /[\s.,!?;:]/.test(text[i - 1])
            const afterIndex = i + phrase.length
            const afterChar = afterIndex >= text.length ? ' ' : text[afterIndex]
            // Match if: at end of text, followed by space/punctuation, or followed by uppercase (new word)
            // Also allow if phrase ends with punctuation (complete phrase)
            const phraseEndsWithPunct = /[.,!?;:]/.test(phrase.slice(-1))
            const afterOk = afterIndex >= text.length || 
                           /[\s.,!?;:]/.test(afterChar) || 
                           /[A-ZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜ]/.test(afterChar) ||
                           phraseEndsWithPunct
            
            if (beforeOk && afterOk) {
              // Add any text before the match
              if (i > lastTextEnd) {
                const beforeText = text.slice(lastTextEnd, i)
                if (beforeText) {
                  if (result.length > 0 && result[result.length - 1].type === 'text') {
                    result[result.length - 1].content += beforeText
                  } else {
                    result.push({ type: 'text', content: beforeText })
                  }
                }
              }
              
              // Add the matched phrase as clickable (preserve original case from text)
              const matchedText = text.slice(i, i + phrase.length)
              const translation = vocabulary[phrase]
              
              if (translation) {
                // Create unique key using prefix, position, and word index
                const uniqueKey = `${uniquePrefix}-word-${i}-${wordIndex}-${matchedText.substring(0, 5)}`
                result.push({
                  type: 'word',
                  content: matchedText,
                  translation: translation,
                  key: uniqueKey
                })
                wordIndex++
              } else {
                // If no translation found, add as regular text
                if (result.length > 0 && result[result.length - 1].type === 'text') {
                  result[result.length - 1].content += matchedText
                } else {
                  result.push({ type: 'text', content: matchedText })
                }
              }
              
              i += phrase.length
              lastTextEnd = i
              matched = true
              break
            }
          }
        }
        
        if (!matched) {
          i++
        }
      }
      
      // Add any remaining text
      if (lastTextEnd < text.length) {
        const remainingText = text.slice(lastTextEnd)
        if (result.length > 0 && result[result.length - 1].type === 'text') {
          result[result.length - 1].content += remainingText
        } else {
          result.push({ type: 'text', content: remainingText })
        }
      }
      
      return result.length > 0 ? result : [{ type: 'text', content: text }]
    } catch (error) {
      console.error('Error parsing text:', error)
      return [{ type: 'text', content: text }]
    }
  }

  const handleWordClick = (wordKey, translation, event) => {
    event.stopPropagation()
    if (activeTooltip === wordKey) {
      setActiveTooltip(null)
    } else {
      setActiveTooltip(wordKey)
    }
  }

  const renderClickableText = (text, uniquePrefix = '') => {
    if (!text) return null
    
    try {
      const parsed = parseText(text, uniquePrefix)
      
      if (!parsed || parsed.length === 0) {
        return <span>{text}</span>
      }
      
      return parsed.map((item, index) => {
        if (item.type === 'word' && item.translation) {
          const isActive = activeTooltip === item.key
          return (
            <span
              key={item.key || `word-${index}`}
              className={`clickable-word ${isActive ? 'active' : ''}`}
              onClick={(e) => handleWordClick(item.key, item.translation, e)}
            >
              {item.content}
              {isActive && (
                <span className="word-tooltip">{item.translation}</span>
              )}
            </span>
          )
        } else {
          return <span key={`text-${index}`}>{item.content}</span>
        }
      })
    } catch (error) {
      console.error('Error rendering clickable text:', error)
      return <span>{text}</span>
    }
  }

  if (loading) {
    return (
      <>
        <Header />
        <div className="story-loading">
          <div className="loading-spinner"></div>
          <p>Loading story...</p>
        </div>
        <Footer />
      </>
    )
  }

  if (!story && !loading) {
    return (
      <>
        <Header />
        <div className="story-error">
          <h2>Story not found</h2>
          <p>Story ID: {storyId}</p>
          <button onClick={() => navigate('/stories')}>Back to Stories</button>
        </div>
        <Footer />
      </>
    )
  }

  if (!story) {
    return null // Still loading
  }

  return (
    <>
      <Header />
      <div className="story-detail-page" onClick={() => setActiveTooltip(null)}>
        <div className="story-detail-container">
          <div className="story-header">
            <button className="back-button" onClick={() => navigate('/stories')}>
              ← Back to Stories
            </button>
            <div className="story-title-section">
              <span className="story-badge">{story.level}</span>
              <h1>{story.title}</h1>
              <p className="story-description">{story.description}</p>
              <p className="story-reading-time">📖 Reading time: {story.readingTime}</p>
            </div>
          </div>

          <div className="story-content">
            <div className="story-instruction">
              <p>💡 Click on any Okrika word or phrase to see its English translation. Click the eye icon next to each sentence to see the full translation.</p>
            </div>
            {story.content?.type === 'dialogue' ? (
              <div className="story-dialogue">
                {story.content.exchanges && story.content.exchanges.length > 0 ? (
                  <div className="dialogue-exchanges">
                    {story.content.exchanges.map((exchange, index) => (
                      <div key={index} className="dialogue-exchange">
                        <div className="exchange-speaker">{exchange.speaker}:</div>
                        <div className="exchange-content">
                          <div className="exchange-okrika-container">
                            <div className="exchange-okrika">
                              {renderClickableText(exchange.okrika, `exchange-${index}`) || exchange.okrika}
                            </div>
                            {exchange.english && (
                              <button
                                className="translation-toggle-btn"
                                onClick={() => {
                                  setShowFullTranslations(prev => ({
                                    ...prev,
                                    [`exchange-${index}`]: !prev[`exchange-${index}`]
                                  }))
                                }}
                                title={showFullTranslations[`exchange-${index}`] ? 'Hide translation' : 'Show translation'}
                              >
                                {showFullTranslations[`exchange-${index}`] ? '👁️' : '👁️‍🗨️'}
                              </button>
                            )}
                          </div>
                          {showFullTranslations[`exchange-${index}`] && exchange.english && (
                            <div className="exchange-english-full">
                              {exchange.english}
                            </div>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p>No dialogue content available.</p>
                )}
              </div>
            ) : story.content?.paragraphs ? (
              story.content.paragraphs.length > 0 ? (
                story.content.paragraphs.map((paragraph, index) => (
                  <div key={index} className="story-paragraph">
                    <div className="paragraph-okrika-container">
                      <div className="paragraph-okrika">
                        <p>{renderClickableText(paragraph.okrika, `paragraph-${index}`) || paragraph.okrika}</p>
                      </div>
                      {paragraph.english && (
                        <button
                          className="translation-toggle-btn"
                          onClick={() => {
                            setShowFullTranslations(prev => ({
                              ...prev,
                              [`paragraph-${index}`]: !prev[`paragraph-${index}`]
                            }))
                          }}
                          title={showFullTranslations[`paragraph-${index}`] ? 'Hide translation' : 'Show translation'}
                        >
                          {showFullTranslations[`paragraph-${index}`] ? '👁️' : '👁️‍🗨️'}
                        </button>
                      )}
                    </div>
                    {showFullTranslations[`paragraph-${index}`] && paragraph.english && (
                      <div className="paragraph-english-full">
                        <p>{paragraph.english}</p>
                      </div>
                    )}
                  </div>
                ))
              ) : (
                <p>No content available.</p>
              )
            ) : (
              <p>No content available.</p>
            )}
          </div>

          <div className="story-complete">
            <h3>✨ Story Complete!</h3>
            <p>Great job reading this story in Okrika! Keep practicing to improve your understanding.</p>
            <div className="story-actions">
              <button className="action-button" onClick={() => navigate('/stories')}>
                Read More Stories
              </button>
              <button className="action-button secondary" onClick={() => navigate('/lessons')}>
                Try Lessons
              </button>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </>
  )
}

export default StoryDetail

