import React from 'react'
import './About.css'

const About = () => {
  return (
    <section id="about" className="about">
      <div className="container">
        <div className="about-content">
          <div className="about-text">
            <h2>About the Okrika Language</h2>
            <p>
              Okrika is a language spoken in Rivers State, Nigeria, primarily by the Okrika people. 
              It is part of the Ijo (Ijaw) language family, which is one of the major language groups 
              in the Niger Delta region.
            </p>
            <p>
              The language carries with it the rich history and traditions of the Okrika people, who 
              have been an integral part of the cultural and economic landscape of Rivers State for centuries.
            </p>
            <p>
              Learning Okrika opens doors to connecting with a vibrant community, understanding local 
              customs, and preserving an important part of Nigeria's linguistic heritage.
            </p>
          </div>
          <div className="about-highlight">
            <div className="highlight-icon">🌍</div>
            <h3>Preserve & Connect</h3>
            <p>
              Join us in preserving the Okrika language and connecting with fellow learners and 
              speakers from around the world.
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}

export default About

