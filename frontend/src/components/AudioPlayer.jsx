import React, { useState, useRef, useEffect } from 'react'
import { AlertCircle, Loader2, Pause, Play } from 'lucide-react'
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
          <Loader2 className="audio-lucide-icon spinning" size={14} aria-hidden />
        ) : hasError ? (
          <AlertCircle className="audio-lucide-icon" size={14} aria-hidden />
        ) : isPlaying ? (
          <Pause className="audio-lucide-icon" size={14} aria-hidden />
        ) : (
          <Play className="audio-lucide-icon" size={14} aria-hidden />
        )}
      </button>
      {hasError && (
        <span className="audio-error-message">Audio unavailable</span>
      )}
    </div>
  )
}

export default AudioPlayer
