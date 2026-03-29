import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import AppLayout from './components/AppLayout'
import Home from './pages/Home'
import Lessons from './pages/Lessons'
import LessonDetail from './pages/LessonDetail'
import Stories from './pages/Stories'
import StoryDetail from './pages/StoryDetail'
import Profile from './pages/Profile'
import Auth from './pages/Auth'
import About from './components/About'

function App() {
  return (
    <Router>
      <AppLayout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/lessons" element={<Lessons />} />
          <Route path="/lessons/:lessonId" element={<LessonDetail />} />
          <Route path="/stories" element={<Stories />} />
          <Route path="/stories/:storyId" element={<StoryDetail />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/login" element={<Auth />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </AppLayout>
    </Router>
  )
}

export default App
