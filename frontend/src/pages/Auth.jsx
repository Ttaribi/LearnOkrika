import React, { useMemo, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { supabase } from '../lib/supabaseClient'
import './Auth.css'

function Auth() {
  const navigate = useNavigate()
  const [mode, setMode] = useState('login') // 'login' | 'signup'
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const heading = mode === 'login' ? 'Log in' : 'Create account'
  const submitLabel = mode === 'login' ? 'Log in' : 'Sign up'

  const onSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      if (mode === 'login') {
        const { error: signInError } = await supabase.auth.signInWithPassword({
          email,
          password,
        })
        if (signInError) throw signInError
      } else {
        const { error: signUpError } = await supabase.auth.signUp({
          email,
          password,
        })
        if (signUpError) throw signUpError
      }

      // Ensure we land on profile after auth completes.
      // If email confirmation is enabled, Supabase will not create a session until confirmed.
      const {
        data: { user },
      } = await supabase.auth.getUser()

      if (user) {
        navigate('/profile')
      } else {
        setError('Check your email to confirm your account, then log in.')
      }
    } catch (err) {
      setError(err?.message || 'Something went wrong.')
    } finally {
      setLoading(false)
    }
  }

  const toggleText = useMemo(
    () => (mode === 'login' ? 'Need an account? Sign up' : 'Already have an account? Log in'),
    [mode]
  )

  return (
    <div className="auth-page">
      <div className="auth-container">
        <h1>{heading}</h1>

        <p className="auth-subtitle">
          Save your progress and see your completed lessons.
        </p>

        <form className="auth-form" onSubmit={onSubmit}>
          <label className="auth-label">
            Email
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              type="email"
              placeholder="you@example.com"
              required
            />
          </label>

          <label className="auth-label">
            Password
            <input
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              type="password"
              placeholder="••••••••"
              required
              minLength={6}
            />
          </label>

          {error ? <div className="auth-error">{error}</div> : null}

          <button type="submit" className="auth-button" disabled={loading}>
            {loading ? 'Please wait...' : submitLabel}
          </button>
        </form>

        <button
          type="button"
          className="auth-toggle"
          onClick={() => {
            setError('')
            setMode((m) => (m === 'login' ? 'signup' : 'login'))
          }}
          disabled={loading}
        >
          {toggleText}
        </button>

        <button type="button" className="auth-back" onClick={() => navigate('/')}>
          Back to Home
        </button>
      </div>
    </div>
  )
}

export default Auth

