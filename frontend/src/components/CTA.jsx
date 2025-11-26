import React from 'react'
import { useNavigate } from 'react-router-dom'
import './CTA.css'

const CTA = () => {
  const navigate = useNavigate()

  return (
    <section id="start" className="cta-section">
      <div className="cta-content">
        <h2>Ready to Begin Your Journey?</h2>
        <p>
          Start learning Okrika today and take the first step towards connecting with 
          this beautiful language and culture.
        </p>
        <button 
          className="cta-button large"
          onClick={() => navigate('/lessons')}
        >
          Start Learning Now
        </button>
      </div>
      <div className="cta-background"></div>
    </section>
  )
}

export default CTA

