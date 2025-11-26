import React, { useState, useRef, useEffect } from 'react'
import './AudioPlayer.css'

const AudioPlayer = ({ audioUrl, label = 'Play pronunciation' }) => {
  const [isPlaying, setIsPlaying] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [hasError, setHasError] = useState(false)
  const audioRef = useRef(null)

  useEffect(() => {
    const audio = audioRef.current
    
    const handleEnded = () => {
      setIsPlaying(false)
      setIsLoading(false)
    }

    const handleError = () => {
      setIsPlaying(false)
      setIsLoading(false)
      setHasError(true)
    }

    const handleCanPlay = () => {
      setIsLoading(false)
    }

    const handleLoadStart = () => {
      setIsLoading(true)
    }

    if (audio) {
      audio.addEventListener('ended', handleEnded)
      audio.addEventListener('error', handleError)
      audio.addEventListener('canplay', handleCanPlay)
      audio.addEventListener('loadstart', handleLoadStart)
    }

    return () => {
      if (audio) {
        audio.removeEventListener('ended', handleEnded)
        audio.removeEventListener('error', handleError)
        audio.removeEventListener('canplay', handleCanPlay)
        audio.removeEventListener('loadstart', handleLoadStart)
      }
    }
  }, [])

  const togglePlay = async () => {
    const audio = audioRef.current
    
    if (!audio || !audioUrl) {
      setHasError(true)
      return
    }

    try {
      if (isPlaying) {
        audio.pause()
        setIsPlaying(false)
      } else {
        setIsLoading(true)
        setHasError(false)
        await audio.play()
        setIsPlaying(true)
      }
    } catch (error) {
      console.error('Error playing audio:', error)
      setHasError(true)
      setIsLoading(false)
      setIsPlaying(false)
    }
  }

  if (!audioUrl) {
    return null
  }

  return (
    <div className="audio-player-wrapper">
      <audio ref={audioRef} src={audioUrl} preload="metadata" />
      <button
        className={`audio-play-button ${isPlaying ? 'playing' : ''} ${hasError ? 'error' : ''}`}
        onClick={togglePlay}
        disabled={isLoading}
        aria-label={label}
        title={label}
      >
        {isLoading ? (
          <span className="audio-icon loading">⟳</span>
        ) : hasError ? (
          <span className="audio-icon error">⚠</span>
        ) : isPlaying ? (
          <span className="audio-icon pause">⏸</span>
        ) : (
          <span className="audio-icon play">▶</span>
        )}
      </button>
      {hasError && (
        <span className="audio-error-message">Audio unavailable</span>
      )}
    </div>
  )
}

export default AudioPlayer

