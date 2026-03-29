import React from 'react'
import './About.css'

const About = () => {
  return (
    <div className="about-page">
      <div className="about-container">

        <div className="about-header">
          <h1>About Learn Okrika</h1>
          <p>Learn, preserve, and connect through language</p>
        </div>

        <div className="about-card">
          <h2>About Learn Okrika</h2>
          <p>
            Welcome to the Learn Okrika Website. This website's purpose is to provide a platform for
            people to learn Okrika by offering different levels of lessons that one can work through
            to aid them in improving their Okrika language skills.
          </p>
          <p>
            Okrika is spoken primarily by the Okrika people of Rivers State, Nigeria. Like many indigenous
            languages, it contains unique tonal and diacritic patterns that make it a vibrant mode of
            communication. Learn Okrika leverages technology to bring these nuances into a user-friendly
            interface.
          </p>
        </div>

        <div className="about-card">
          <h2>Motivation</h2>
          <p>
            I created this website because as someone trying to learn the Okrika language, there are not
            many resources available online. So with Learn Okrika, I wanted to make it easy so that
            someone with no prior knowledge would know where to start.
          </p>
          <p>
            Already there is a good amount of lessons and stories that one can use to aid their learning,
            but this website will only continue to grow. I want this website to be an anchor of our culture
            and a go-to resource when you want to submerge yourself in our language. I hope to have many
            more lessons and stories that can deepen your knowledge.
          </p>
          <p>
            I would also like to give a thank you to the Wakirike Development Coalition and Levi Sika
            for their assistance with translations.
          </p>
        </div>

        <div className="about-footer-card">
          <p className="about-credit">Developed and Envisioned by Tamunoopubo Taribi</p>
          <div className="about-links">
            <a href="https://www.linkedin.com/in/tamunoopubo-taribi" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className="about-link">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
              </svg>
              LinkedIn
            </a>
            <a href="https://github.com/tamunoopubo-taribi" target="_blank" rel="noopener noreferrer" aria-label="GitHub" className="about-link">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/>
              </svg>
              GitHub
            </a>
          </div>
        </div>

      </div>
    </div>
  )
}

export default About
