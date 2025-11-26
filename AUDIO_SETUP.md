# Audio Setup Guide

This guide explains how to add audio pronunciation files to Lesson 1: Basic Greetings.

## Overview

Audio functionality has been added to Lesson 1, allowing users to play pronunciation audio for each vocabulary item. The audio player appears as a circular play button next to each Okrika word.

## File Structure

Audio files should be placed in:
```
frontend/public/audio/lesson1/
```

## Adding Audio Files

1. **Record or obtain audio files** for each vocabulary item in Lesson 1
2. **Name the files** according to the mapping in `frontend/public/audio/lesson1/README.md`
3. **Place the files** in the `frontend/public/audio/lesson1/` directory
4. **File format**: MP3 (recommended), WAV, or OGG

## Current Vocabulary Items with Audio Support

All 11 vocabulary items in Lesson 1 now have audio URL fields configured:

1. Í ḅásà (Good morning) → `i-basa.mp3`
2. ḅàwàị̀rị̀à (Good night) → `bawa-iria.mp3`
3. í ḅòsà (Welcome) → `i-bosa.mp3`
4. Àri Í kéréní mè (I greet you) → `ari-i-kereni-me.mp3`
5. Ñdè ànì là òkù? (How are you?) → `nde-ani-la-oku.mp3`
6. Ñdè íyá fúró sìmè òkù? (How is your family?) → `nde-iya-furo-sime-oku.mp3`
7. Ìbì mé (I am good) → `ibi-me.mp3`
8. Í ómì? (You There?) → `i-omi.mp3`
9. À ómì (I'm here) → `a-omi.mp3`
10. Í bù dèìñ wáráù? (Are you alright?) → `i-bu-dein-warau.mp3`
11. Ì bù dèìñ mè (I'm alright) → `i-bu-dein-me.mp3`

## How It Works

- **Backend**: Audio URLs are defined in `backend/routes/api.py` in the Lesson 1 vocabulary items
- **Frontend**: The `AudioPlayer` component (in `frontend/src/components/AudioPlayer.jsx`) handles playback
- **UI**: Play buttons appear next to each vocabulary word when audio URLs are present

## Testing

1. Add at least one audio file to `frontend/public/audio/lesson1/`
2. Start the development server:
   ```bash
   cd frontend && npm run dev
   ```
3. Navigate to Lesson 1: Basic Greetings
4. You should see play buttons next to vocabulary items with audio files
5. Click the play button to hear the pronunciation

## Audio Player Features

- **Play/Pause**: Click to play or pause audio
- **Visual Feedback**: Button changes color when playing
- **Error Handling**: Shows error icon if audio file is missing or fails to load
- **Loading State**: Shows loading spinner while audio is loading

## Adding Audio to Other Lessons

To add audio to other lessons:

1. Add `audioUrl` field to vocabulary items in `backend/routes/api.py`
2. Create a corresponding directory (e.g., `frontend/public/audio/lesson2/`)
3. Add the audio files with matching names
4. The AudioPlayer component will automatically work with the new audio URLs

## Notes

- Audio files in the `public` folder are served statically by Vite
- In production builds, these files are included automatically
- Missing audio files will show an error indicator but won't break the page


