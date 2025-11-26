import React, { useState, useEffect, useRef } from 'react'
import './Stats.css'

const stats = [
  { number: 1000, suffix: '+', label: 'Active Learners' },
  { number: 50, suffix: '+', label: 'Interactive Lessons' },
  { number: 24, suffix: '/7', label: 'Access Anywhere' },
  { number: 100, suffix: '%', label: 'Free to Start' }
]

const Stats = () => {
  const [counters, setCounters] = useState([0, 0, 0, 0])
  const [hasAnimated, setHasAnimated] = useState(false)
  const sectionRef = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !hasAnimated) {
            setHasAnimated(true)
            animateCounters()
          }
        })
      },
      { threshold: 0.5 }
    )

    if (sectionRef.current) {
      observer.observe(sectionRef.current)
    }

    return () => {
      if (sectionRef.current) {
        observer.unobserve(sectionRef.current)
      }
    }
  }, [hasAnimated])

  const animateCounters = () => {
    stats.forEach((stat, index) => {
      const duration = 2000
      const steps = 60
      const increment = stat.number / steps
      let current = 0

      const timer = setInterval(() => {
        current += increment
        if (current >= stat.number) {
          setCounters((prev) => {
            const newCounters = [...prev]
            newCounters[index] = stat.number
            return newCounters
          })
          clearInterval(timer)
        } else {
          setCounters((prev) => {
            const newCounters = [...prev]
            newCounters[index] = Math.floor(current)
            return newCounters
          })
        }
      }, duration / steps)
    })
  }

  return (
    <section className="stats" ref={sectionRef}>
      <div className="container">
        <div className="stats-grid">
          {stats.map((stat, index) => (
            <div key={index} className="stat-item">
              <h3 className="stat-number">
                {counters[index]}{stat.suffix}
              </h3>
              <p className="stat-label">{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Stats

