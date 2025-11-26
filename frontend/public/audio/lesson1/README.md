# Audio Files for Lesson 1: Basic Greetings

This directory contains audio pronunciation files for Lesson 1 vocabulary items.

## Expected Audio Files

### Vocabulary Words

Please add the following audio files for vocabulary words:

1. `i-basa.m4a` - Pronunciation of "Í ḅásà" (Good morning) ✓
2. `bawa-iria.m4a` - Pronunciation of "ḅàwàị̀rị̀à" (Good night)
3. `i-bosa.m4a` - Pronunciation of "í ḅòsà" (Welcome) ✓
4. `ari-i-kereni-me.m4a` - Pronunciation of "Àri Í kéréní mè" (I greet you)
5. `nde-ani-la-oku.m4a` - Pronunciation of "Ñdè ànì là òkù?" (How are you?)
6. `nde-iya-furo-sime-oku.m4a` - Pronunciation of "Ñdè íyá fúró sìmè òkù?" (How is your family?)
7. `ibi-me.m4a` - Pronunciation of "Ìbì mé" (I am good)
8. `i-omi.m4a` - Pronunciation of "Í ómì?" (You There?) ✓
9. `a-omi-e.m4a` - Pronunciation of "À ómì-e" (I'm here) ✓
10. `i-bu-dein-warau.m4a` - Pronunciation of "Í bù dèìñ wáráù?" (Are you alright?)
11. `i-bu-dein-me.m4a` - Pronunciation of "Ì bù dèìñ mè" (I'm alright)

### Example Sentences

Please add the following audio files for example sentences:

1. `example-opubo-i-basa.m4a` - "Opúbọ̀, í ḅásà" (Good morning Opubo)
2. `example-lolia-bawa-iria.m4a` - "Lòliā, ḅàwàị̀rị̀à" (Good night Lolia)
3. `example-nyingima-i-bosa.m4a` - "Nyingima í ḅòsà" (Welcome mother)
4. `example-dabo-ari-i-kereni-me.m4a` - "Dabo, Àri Í kéréní mè" (I greet you father)
5. `example-mimgba-nde-ani-la-oku.m4a` - "Mímgbà, ñdé ànì là òkú?" (How are you today?)
6. `example-boma-nde-iya-furo-sime-oku.m4a` - "Boma, ñdè íyá fúró sìmè òkù?" (Boma, how is your family?)
7. `example-ibi-me-miegbaka.m4a` - "Ìbì mé, mìébákà" (I am good, thank you.)
8. `example-dabo-i-omi.m4a` - "Dabo, í ómì?" (Father, you there?)
9. `example-iin-a-omi-e.m4a` - "Ììn, à ómì-e" (Yes, I'm here.)
10. `example-mitchell-i-bu-dein-warau.m4a` - "Mitchell, Í bù dèìñ wáráù?" (Mitchell, are you alright?)
11. `example-iin-i-bu-dein-me.m4a` - "Ììñ, Ì bù dèìñ mè" (Yes, I'm alright.)

## Audio File Requirements

- **Format**: MP3 (recommended) or other web-compatible formats (WAV, OGG)
- **Quality**: Clear, natural pronunciation
- **Sample Rate**: 44.1 kHz or higher
- **Bit Rate**: 128 kbps or higher for MP3

## Usage

Once audio files are placed in this directory, they will automatically be available through the AudioPlayer component in the lesson interface. The files are served from `/audio/lesson1/` path.

## Notes

- Audio files are served statically from the `public` folder in Vite
- In production, these files will be included in the build output
- Make sure file names match exactly with the `audioUrl` values in the backend API

