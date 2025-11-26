import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Lessons from './pages/Lessons'
import LessonDetail from './pages/LessonDetail'
import Stories from './pages/Stories'
import StoryDetail from './pages/StoryDetail'

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/lessons" element={<Lessons />} />
          <Route path="/lessons/:lessonId" element={<LessonDetail />} />
          <Route path="/stories" element={<Stories />} />
          <Route path="/stories/:storyId" element={<StoryDetail />} />
        </Routes>
      </div>
    </Router>
  )
}

export default App
