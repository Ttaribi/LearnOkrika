from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Learn Okrika API is running',
        'version': '1.0.0'
    }), 200

@api_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get website statistics"""
    return jsonify({
        'active_learners': 1000,
        'interactive_lessons': 50,
        'access_24_7': True,
        'free_to_start': True
    }), 200

@api_bp.route('/lessons', methods=['GET'])
def get_lessons():
    """Get all available lessons"""
    lessons = [
        {
            'id': 0,
            'title': 'Introduction to Okrika',
            'level': 'beginner',
            'description': 'Welcome to learning Okrika! Get started with an introduction to the language.',
            'duration': '10 minutes',
            'category': 'introduction'
        },
        {
            'id': 1,
            'title': 'Lesson 1: Basic Greetings',
            'level': 'beginner',
            'description': 'Learn essential greetings and how to say hello in Okrika',
            'duration': '15 minutes',
            'category': 'greetings'
        },
        {
            'id': 2,
            'title': 'Pronouns',
            'level': 'beginner',
            'description': 'Learn personal pronouns in Okrika',
            'duration': '20 minutes',
            'category': 'grammar'
        },
        {
            'id': 3,
            'title': 'Common Phrases',
            'level': 'beginner',
            'description': 'Master everyday phrases used in Okrika conversations',
            'duration': '20 minutes',
            'category': 'phrases'
        },
        {
            'id': 4,
            'title': 'Family and Relationships',
            'level': 'beginner',
            'description': 'Learn vocabulary for family members and relationships',
            'duration': '25 minutes',
            'category': 'vocabulary'
        },
        {
            'id': 5,
            'title': 'Food and Dining',
            'level': 'intermediate',
            'description': 'Essential phrases and vocabulary for food and dining',
            'duration': '30 minutes',
            'category': 'vocabulary'
        }
    ]
    
    # Optional filtering
    level = request.args.get('level')
    category = request.args.get('category')
    
    filtered_lessons = lessons
    if level:
        filtered_lessons = [l for l in filtered_lessons if l['level'] == level]
    if category:
        filtered_lessons = [l for l in filtered_lessons if l['category'] == category]
    
    return jsonify({
        'lessons': filtered_lessons,
        'total': len(filtered_lessons),
        'filters': {
            'level': level,
            'category': category
        }
    }), 200

@api_bp.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    """Get a specific lesson by ID"""
    # In production, this would fetch from database
    lesson_data = {
        0: {
            'id': 0,
            'title': 'Introduction to Okrika',
            'level': 'beginner',
            'description': 'Welcome to learning Okrika! Get started with an introduction to the language.',
            'duration': '10 minutes',
            'content': {
                'sections': [
                    {
                        'title': 'Welcome!',
                        'type': 'text',
                        'content': 'Welcome to Learn Okrika! This platform is designed to help you learn the beautiful Okrika language from Rivers State, Nigeria. Through interactive lessons, you will discover words, phrases, and sentences that will help you communicate in Okrika.'
                    },
                    {
                        'title': 'About the Okrika Language',
                        'type': 'text',
                        'content': 'Okrika is part of the Ijo (Ijaw) language family, spoken primarily in Rivers State, Nigeria. Learning Okrika connects you with a rich cultural heritage and vibrant community. The language carries with it the rich history and traditions of the Okrika people, who have been an integral part of the cultural and economic landscape of Rivers State for centuries.'
                    },
                    {
                        'title': 'How to Use This Platform',
                        'type': 'text',
                        'content': 'Each lesson contains words, phrases, and sentences. Practice pronunciation, study the vocabulary, and complete exercises to master the language. Navigate through each section using the Previous and Next buttons. Take your time to learn and practice each concept before moving on.'
                    }
                ]
            }
        },
        1: {
            'id': 1,
            'title': 'Lesson 1: Basic Greetings',
            'level': 'beginner',
            'description': 'Learn essential greetings and how to say hello in Okrika',
            'duration': '15 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn New Words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'Í ḅásà',
                                'english': 'Good morning',
                                'singular': 'Í ḅásà',
                                'plural': 'Ó ḅásà',
                                'example': 'Opúbọ̀, í ḅásà',
                                'exampleTranslation': 'Good morning Opubo',
                                'audioUrl': '/audio/lesson1/i-basa.m4a',
                                'exampleAudioUrl': '/audio/lesson1/i-basa-exe.m4a'
                            },
                            {
                                'okrika': 'ḅàwàị̀rị̀à',
                                'english': 'Good night',
                                'singular': 'ḅàwàị̀rị̀à',
                                'plural': 'ò ḅàwàị̀rị̀à',
                                'example': 'Lòliā, ḅàwàị̀rị̀à',
                                'exampleTranslation': 'Good night Lolia',
                                'audioUrl': '/audio/lesson1/bawairia.m4a',
                                'exampleAudioUrl': '/audio/lesson1/bawairia-exe.m4a'
                            },
                            {
                                'okrika': 'í ḅòsà',
                                'english': 'Welcome',
                                'singular': 'í ḅòsà',
                                'plural': 'ò ḅòsà',
                                'example': 'Nyingima, í ḅòsà',
                                'exampleTranslation': 'Welcome mother',
                                'audioUrl': '/audio/lesson1/i-bosa.m4a',
                                'exampleAudioUrl': '/audio/lesson1/i-bosa-exe.m4a'
                            },
                            {
                                'okrika': 'Àri Í kéréní mè',
                                'english': 'I greet you',
                                'singular': 'Àri Í kéréní mè',
                                'example': 'Dabo, Àri Í kéréní mè',
                                'exampleTranslation': 'I greet you father',
                                'audioUrl': '/audio/lesson1/ari-i-kerine-me.m4a',
                                'exampleAudioUrl': '/audio/lesson1/ari-i-kerine-me-exe.m4a'
                            },
                            {   
                                'okrika': 'Ñdè ànì là òkù?',
                                'english': 'How are you?',
                                'singular': 'Ñdè ànì là òkù?',
                                'example': 'Mímgbà, ñdé ànì là òkú?',
                                'exampleTranslation': 'How are you today?',
                                'audioUrl': '/audio/lesson1/nde-ani-la-oku.m4a',
                                'exampleAudioUrl': '/audio/lesson1/nde-ani-la-oku-exe.m4a'
                            },
                            {   
                                'okrika': 'Ñdè íyá fúró sìmè òkù?',
                                'english': 'How is your family?',
                                'singular': 'Ñdè ànì là òkù?',
                                'example': 'Boma, ñdè íyá fúró sìmè òkù?',
                                'exampleTranslation': 'Boma, how is your family?',
                                'audioUrl': '/audio/lesson1/nde-iya-furo-sime-oku.m4a',
                                'exampleAudioUrl': '/audio/lesson1/nde-iya-furo-sime-oku-exe.m4a'
                            },
                            {
                                'okrika': 'Ìbì mé',
                                'english': 'I am good',
                                'singular': 'Ìbì mé',
                                'example': 'Ìbì mé, mìébákà',
                                'exampleTranslation': 'I am good, thank you.',
                                'audioUrl': '/audio/lesson1/ibi-me.m4a',
                                'exampleAudioUrl': '/audio/lesson1/ibi-me-exe.m4a'
                            },
                            {
                                'okrika': 'Í ómì?',
                                'english': 'You There?',
                                'singular': 'Í ómì?',
                                'plural': 'Ó mín ómi?',
                                'example': 'Dabo, í ómì?',
                                'exampleTranslation': 'Father, you there?',
                                'audioUrl': '/audio/lesson1/i-omi.m4a',
                                'exampleAudioUrl': '/audio/lesson1/i-omi-exe.m4a'
                            },
                            {
                                'okrika': 'À ómì-e',
                                'english': "I'm here",
                                'singular': 'À ómì-e',
                                'example': 'Ììn, à ómì-e',
                                'exampleTranslation': "Yes, I'm here.",
                                'audioUrl': '/audio/lesson1/a-omi-e.m4a',
                                'exampleAudioUrl': '/audio/lesson1/a-omi-e-exe.m4a'
                            },
                            {
                                'okrika': 'Í bù dèìñ wáráù?',
                                'english': 'Are you alright?',
                                'singular': 'Í bù dèìñ wáráù?',
                                'example': 'Mitchell, Í bù dèìñ wáráù?',
                                'exampleTranslation': 'Mitchell, are you alright?',
                                'audioUrl': '/audio/lesson1/i-bu-dein-warau.m4a',
                                'exampleAudioUrl': '/audio/lesson1/i-bu-dein-warau-exe.m4a'
                            },
                            {
                                'okrika': 'Ì bù dèìñ mè',
                                'english': "I'm alright",
                                'singular': 'Ì bù dèìñ mè',
                                'example': 'Ììñ, Ì bù dèìñ mè',
                                'exampleTranslation': "Yes, I'm alright.",
                                'audioUrl': '/audio/lesson1/i-bu-dein-me.m4a',
                                'exampleAudioUrl': '/audio/lesson1/i-bu-dein-me-exe.m4a'
                            }
                        ]
                    },
                    {
                        'part': 2,
                        'title': 'Test Your Knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "Í ḅásà" mean?',
                                'correctAnswer': 'Good morning',
                                'options': ['Good morning', 'Good night', 'Welcome', 'How are you?']
                            },
                            {
                                'id': 2,
                                'question': 'What does "ḅàwàị̀rị̀à" mean?',
                                'correctAnswer': 'Good night',
                                'options': ['Good morning', 'Good night', 'Welcome', 'I am fine']
                            },
                            {
                                'id': 3,
                                'question': 'What does "í ḅòsà" mean?',
                                'correctAnswer': 'Welcome',
                                'options': ['Good morning', 'I greet you', 'Welcome', 'How are you?']
                            },
                            {
                                'id': 4,
                                'question': 'What does "Àri Í kéréní mè" mean?',
                                'correctAnswer': 'I greet you',
                                'options': ['How are you?', 'I greet you', 'I am fine', 'Good morning']
                            },
                            {
                                'id': 5,
                                'question': 'What does "Ñdè ànì là òkù?" mean?',
                                'correctAnswer': 'How are you?',
                                'options': ['I am fine', 'How are you?', 'Good morning', 'Welcome']
                            },
                            {
                                'id': 6,
                                'question': 'What does "Ì bìmé" mean?',
                                'correctAnswer': 'I am fine',
                                'options': ['How are you?', 'I am fine', 'Good night', 'Welcome']
                            },
                            {
                                'id': 7,
                                'question': 'What does "Ñdè íyá fúró sìmè òkù?" mean?',
                                'correctAnswer': 'How is your family?',
                                'options': ['How are you?', 'How is your family?', 'I am fine', 'Welcome']
                            },
                            {
                                'id': 8,
                                'question': 'What does "Í ómì?" mean?',
                                'correctAnswer': "You There?",
                                'options': ["I'm here", "You There?", 'Are you alright?', 'Good morning']
                            },
                            {
                                'id': 9,
                                'question': 'What does "À ómì" mean?',
                                'correctAnswer': "I'm here",
                                'options': ["You There?", "I'm here", 'I am fine', 'Welcome']
                            },
                            {
                                'id': 10,
                                'question': 'What does "Í bù dèìñ wáráù?" mean?',
                                'correctAnswer': 'Are you alright?',
                                'options': ['I am fine', 'Are you alright?', "I'm alright", 'How are you?']
                            },
                            {
                                'id': 11,
                                'question': 'What does "Ì bù dèìñ mè" mean?',
                                'correctAnswer': "I'm alright",
                                'options': ['Are you alright?', "I'm alright", 'I am fine', 'How are you?']
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Dialogue Examples',
                        'type': 'dialogue',
                        'dialogues': [
                            {
                                'title': 'Morning Greeting',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Í ḅásà!',
                                        'english': 'Good morning!'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Í ḅásà! Ñdé àní laa òkú?',
                                        'english': 'Good morning! How are you?'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Ì bìmé, mìébákà. Ñdé àní laa òkú wẹ?',
                                        'english': 'I am fine, thank you. How are you?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ì bìmé!',
                                        'english': 'I am fine!'
                                    }
                                ]
                            },
                            {
                                'title': 'Welcoming a Guest',
                                'exchanges': [
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'í ḅòsà! Àri Í kéréní mè!',
                                        'english': 'Welcome! I greet you!'
                                    },
                                    {
                                        'speaker': 'Guest',
                                        'okrika': 'Mìébákà! Ñdé àní laa òkú?',
                                        'english': 'Thank you! How are you?'
                                    },
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'Ì bìmé, mìébákà!',
                                        'english': 'I am fine, thank you!'
                                    }
                                ]
                            },
                            {
                                'title': 'Evening Farewell',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'ḅàwàị̀rị̀à!',
                                        'english': 'Good night!'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'ḅàwàị̀rị̀à!',
                                        'english': 'Good night!'
                                    }
                                ]
                            },
                            {
                                'title': 'Checking on Someone',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Dabo, í ómì?',
                                        'english': 'Father, you there?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ììn, à ómì-e',
                                        'english': "Yes, I'm here."
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Í bù dèìñ wáráù?',
                                        'english': 'Are you alright?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ììñ, Ì bù dèìñ mè',
                                        'english': "Yes, I'm alright."
                                    }
                                ]
                            },
                            {
                                'title': 'Asking About Family',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Boma, ñdè íyá fúró sìmè òkù?',
                                        'english': 'Boma, how is your family?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ì bìmé, mìébákà',
                                        'english': 'I am fine, thank you.'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Í ḅásà!',
                                        'english': 'Good morning!'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Í ḅásà! Ñdè ànì là òkù?',
                                        'english': 'Good morning! How are you?'
                                    }
                                ]
                            },
                            {
                                'title': 'Complete Greeting Exchange',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'í ḅòsà! Àri Í kéréní mè!',
                                        'english': 'Welcome! I greet you!'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Mìébákà! Ñdè ànì là òkù?',
                                        'english': 'Thank you! How are you?'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Ì bìmé púrú. Ñdè íyá fúró sìmè òkù?',
                                        'english': 'I am fine too. How is your family?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ì bù dèìñ mè, mìébákà!',
                                        'english': "I'm alright, thank you!"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        2: {
            'id': 2,
            'title': 'Pronouns',
            'level': 'beginner',
            'description': 'Learn personal pronouns in Okrika',
            'duration': '20 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn New Words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'ìrì',
                                'english': 'I(me)',
                                'form': 'singular',
                                'example': 'Ìrì éréméníbò-è',
                                'exampleTranslation': 'I am a woman'
                            },
                            {
                                'okrika': 'írí',
                                'english': 'you',
                                'form': 'singular',
                                'example': 'Írí ówúbó-è',
                                'exampleTranslation': 'You are a man'
                            },
                            {
                                'okrika': 'ómínē',
                                'english': 'you',
                                'form': 'plural',
                                'example': 'Ómínē ómí no-è!',
                                'exampleTranslation': "Greetings"
                            },
                            {
                                'okrika': 'àrì',
                                'english': 'her',
                                'form': 'singular',
                                'example': 'Àrì ìbìsìkì bó mè',
                                'exampleTranslation': 'She came early'
                            },
                            {
                                'okrika': 'òrì',
                                'english': 'he',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'árì',
                                'english': 'she',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'árá',
                                'english': 'her',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'áráyè',
                                'english': 'herself',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'árìmà',
                                'english': 'hers',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'òrìbè',
                                'english': 'himself',
                                'form': 'singular',
                                'example': 'Wẹ ḅírí',
                                'exampleTranslation': 'They are fine'
                            },
                            {
                                'okrika': 'òràyè',
                                'english': 'his',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'ànì',
                                'english': 'it, that',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': '...'
                            },
                            {
                                'okrika': 'àrí mà/àrí àyè à',
                                'english': 'those',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'má yè mà',
                                'english': 'these',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'mì/mìmì',
                                'english': 'this',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ìnì',
                                'english': 'they',
                                'form': 'plural',
                                'example': 'Ìnì nèmì kè',
                                'exampleTranslation': "They don't know"
                            },
                            {
                                'okrika': 'ìnìá',
                                'english': 'their',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ìnìáyè',
                                'english': 'theirs',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ìnìmà/ìnìàbù',
                                'english': 'themselves',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ìyàyè',
                                'english': 'Mine',
                                'form': 'singular',
                                'example': 'Mì ìyàyè-è',
                                'exampleTranslation': "This is mine"
                            },
                            {
                                'okrika': 'íyá yè',
                                'english': 'yours',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ómínàyè',
                                'english': 'yours',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'ìyà',
                                'english': 'my',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'íyá',
                                'english': 'your',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            
                            {
                                'okrika': 'ìrìmā',
                                'english': 'myself',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "T..."
                            },
                            {
                                'okrika': 'mínāyè',
                                'english': 'ours',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'mínā',
                                'english': 'our',
                                'form': 'plural',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'mínè',
                                'english': 'we, us, ourselves',
                                'form': 'plural',
                                'example': 'Mínè Kìrìkènì-àpù-è',
                                'exampleTranslation': "We are from Okrika"
                            },
                            {
                                'okrika': 'ásémíníbò',
                                'english': 'mr/mister',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },
                            {
                                'okrika': 'àmàtà',
                                'english': 'mrs/miss',
                                'form': 'singular',
                                'example': '...',
                                'exampleTranslation': "..."
                            },

                        ]
                    },
                    {
                        'part': 2,
                        'title': 'Test Your Knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "Mẹ́" mean?',
                                'correctAnswer': 'I / Me',
                                'options': ['I / Me', 'You', 'He / She', 'We']
                            },
                            {
                                'id': 2,
                                'question': 'What does "Í" mean?',
                                'correctAnswer': 'You (singular)',
                                'options': ['I / Me', 'You (singular)', 'You (plural)', 'He / She']
                            },
                            {
                                'id': 3,
                                'question': 'What does "Ó" mean?',
                                'correctAnswer': 'You (plural)',
                                'options': ['You (singular)', 'You (plural)', 'We', 'They']
                            },
                            {
                                'id': 4,
                                'question': 'What does "À" mean?',
                                'correctAnswer': 'He / She / It',
                                'options': ['I / Me', 'You', 'He / She / It', 'We']
                            },
                            {
                                'id': 5,
                                'question': 'What does "Wẹ́" mean?',
                                'correctAnswer': 'We / Us',
                                'options': ['I / Me', 'You', 'We / Us', 'They']
                            },
                            {
                                'id': 6,
                                'question': 'What does "Wẹ" mean?',
                                'correctAnswer': 'They / Them',
                                'options': ['We / Us', 'They / Them', 'You (plural)', 'He / She']
                            },
                            {
                                'id': 7,
                                'question': 'Which pronoun would you use to say "We are fine"?',
                                'correctAnswer': 'Wẹ́',
                                'options': ['Mẹ́', 'Wẹ́', 'Wẹ', 'Ó']
                            },
                            {
                                'id': 8,
                                'question': 'Which pronoun would you use to say "They are here"?',
                                'correctAnswer': 'Wẹ',
                                'options': ['Wẹ́', 'Wẹ', 'À', 'Í']
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Dialogue Examples',
                        'type': 'dialogue',
                        'dialogues': [
                            {
                                'title': 'Using Pronouns in Greetings',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Í ḅásà! Ñdè ànì là òkù?',
                                        'english': 'You (say) good morning! How are you?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Mẹ́ ḅírí, mìébákà. Kí ḅírí ḅí wẹ?',
                                        'english': 'I am fine, thank you. How are you?'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Mẹ́ ḅírí púrú',
                                        'english': 'I am fine too'
                                    }
                                ]
                            },
                            {
                                'title': 'Talking About Others',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'À ómì?',
                                        'english': 'Is he/she here?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ììn, à ómì',
                                        'english': "Yes, he/she is here"
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Wẹ ḅírí?',
                                        'english': 'Are they fine?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ììñ, wẹ ḅírí',
                                        'english': 'Yes, they are fine'
                                    }
                                ]
                            },
                            {
                                'title': 'Group Conversation',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Ó ḅásà!',
                                        'english': 'You all (say) good morning!'
                                    },
                                    {
                                        'speaker': 'Group',
                                        'okrika': 'Í ḅásà!',
                                        'english': 'You (say) good morning!'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Wẹ́ ḅírí?',
                                        'english': 'Are we fine?'
                                    },
                                    {
                                        'speaker': 'Group',
                                        'okrika': 'Ììñ, wẹ́ ḅírí',
                                        'english': 'Yes, we are fine'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        3: {
            'id': 3,
            'title': 'Common Phrases',
            'level': 'beginner',
            'description': 'Master everyday phrases used in Okrika conversations',
            'duration': '20 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn New Words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'Mìébákà',
                                'english': 'Thank you',
                                'example': 'Mìébákà púrú',
                                'exampleTranslation': 'Thank you very much'
                            },
                            {
                                'okrika': 'Kí ḅírí ḅí?',
                                'english': 'How are you?',
                                'example': 'Kí ḅírí ḅí gbá?',
                                'exampleTranslation': 'How are you today?'
                            },
                            {
                                'okrika': 'Mẹ́ ḅírí',
                                'english': 'I am fine',
                                'example': 'Mẹ́ ḅírí, ḅá ḅí',
                                'exampleTranslation': 'I am fine, thank you'
                            },
                            {
                                'okrika': 'ḅó ḅírí gbá',
                                'english': 'Have a nice day',
                                'example': 'ḅó ḅírí gbá!',
                                'exampleTranslation': 'Have a nice day!'
                            },
                            {
                                'okrika': 'Í ḅòsà',
                                'english': 'Welcome',
                                'example': 'Í ḅòsà nyingima',
                                'exampleTranslation': 'Welcome mother'
                            }
                        ]
                    },
                    {
                        'part': 2,
                        'title': 'Test Your Knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "Mìébákà" mean?',
                                'correctAnswer': 'Thank you',
                                'options': ['Thank you', 'Good morning', 'How are you?', 'Welcome']
                            },
                            {
                                'id': 2,
                                'question': 'What does "Kí ḅírí ḅí?" mean?',
                                'correctAnswer': 'How are you?',
                                'options': ['I am fine', 'How are you?', 'Thank you', 'Good night']
                            },
                            {
                                'id': 3,
                                'question': 'What does "Mẹ́ ḅírí" mean?',
                                'correctAnswer': 'I am fine',
                                'options': ['How are you?', 'I am fine', 'Thank you', 'Welcome']
                            },
                            {
                                'id': 4,
                                'question': 'What does "ḅó ḅírí gbá" mean?',
                                'correctAnswer': 'Have a nice day',
                                'options': ['Good morning', 'How are you?', 'Have a nice day', 'Thank you']
                            },
                            {
                                'id': 5,
                                'question': 'What does "Í ḅòsà" mean?',
                                'correctAnswer': 'Welcome',
                                'options': ['Thank you', 'Welcome', 'I am fine', 'Good evening']
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Dialogue Examples',
                        'type': 'dialogue',
                        'dialogues': [
                            {
                                'title': 'Greeting Conversation',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Íḅásà, kí ḅírí ḅí?',
                                        'english': 'Good morning, how are you?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Mẹ́ ḅírí, mìébákà. Kí ḅírí ḅí wẹ?',
                                        'english': 'I am fine, thank you. How are you?'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Mẹ́ ḅírí púrú. ḅó ḅírí gbá!',
                                        'english': 'I am fine too. Have a nice day!'
                                    }
                                ]
                            },
                            {
                                'title': 'Welcoming Someone',
                                'exchanges': [
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'Í ḅòsà! Í ḅòsà nyingima!',
                                        'english': 'Welcome! Welcome mother!'
                                    },
                                    {
                                        'speaker': 'Guest',
                                        'okrika': 'Mìébákà púrú!',
                                        'english': 'Thank you very much!'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        4: {
            'id': 4,
            'title': 'Family and Relationships',
            'level': 'beginner',
            'description': 'Learn vocabulary for family members and relationships',
            'duration': '25 minutes',
            'content': {
                'sections': [
                    {
                        'title': 'Family Members',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'Mímgbà',
                                'english': 'Mother',
                                'example': 'Mímgbà ḅó ḅírí',
                                'exampleTranslation': 'Mother is fine'
                            },
                            {
                                'okrika': 'Dabo',
                                'english': 'Father',
                                'example': 'Dabo ḅírí',
                                'exampleTranslation': 'Father is fine'
                            },
                            {
                                'okrika': 'Nyingima',
                                'english': 'My mother',
                                'example': 'Nyingima íḅòsà',
                                'exampleTranslation': 'Welcome mother'
                            },
                            {
                                'okrika': 'Dabo',
                                'english': 'My father',
                                'example': 'Dabo, Àri Í kéréní mè',
                                'exampleTranslation': 'I greet you father'
                            }
                        ]
                    },
                    {
                        'title': 'More Family Terms',
                        'type': 'phrases',
                        'items': [
                            {
                                'okrika': 'Sibling',
                                'english': 'Brother/Sister',
                                'example': 'Example in Okrika',
                                'exampleTranslation': 'Example translation'
                            },
                            {
                                'okrika': 'Child',
                                'english': 'Son/Daughter',
                                'example': 'Example in Okrika',
                                'exampleTranslation': 'Example translation'
                            }
                        ]
                    }
                ]
            }
        }
    }
    
    lesson = lesson_data.get(lesson_id)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404
    
    return jsonify(lesson), 200

@api_bp.route('/about', methods=['GET'])
def get_about():
    """Get information about the Okrika language"""
    return jsonify({
        'language': 'Okrika',
        'region': 'Rivers State, Nigeria',
        'language_family': 'Ijo (Ijaw)',
        'description': 'Okrika is a language spoken in Rivers State, Nigeria, primarily by the Okrika people. It is part of the Ijo (Ijaw) language family, which is one of the major language groups in the Niger Delta region.',
        'cultural_context': 'The language carries with it the rich history and traditions of the Okrika people, who have been an integral part of the cultural and economic landscape of Rivers State for centuries.',
        'features': [
            'Rich cultural heritage',
            'Part of the Niger Delta linguistic tradition',
            'Vibrant community of speakers',
            'Growing interest in language preservation'
        ]
    }), 200

@api_bp.route('/stories', methods=['GET'])
def get_stories():
    """Get all available stories"""
    stories = [
        {
            'id': 0,
            'title': 'Introduction in Okrika',
            'level': 'beginner',
            'description': 'A simple story about two people meeting for the first time',
            'readingTime': '5 minutes',
            'category': 'daily_life'
        },
        {
            'id': 1,
            'title': 'Family Gathering',
            'level': 'beginner',
            'description': 'A story about a family coming together for a meal',
            'readingTime': '7 minutes',
            'category': 'family'
        },
        {
            'id': 2,
            'title': 'Market Day',
            'level': 'intermediate',
            'description': 'Follow a conversation at the local market',
            'readingTime': '10 minutes',
            'category': 'daily_life'
        }
    ]
    
    # Optional filtering
    level = request.args.get('level')
    category = request.args.get('category')
    
    filtered_stories = stories
    if level:
        filtered_stories = [s for s in filtered_stories if s['level'] == level]
    if category:
        filtered_stories = [s for s in filtered_stories if s['category'] == category]
    
    return jsonify({
        'stories': filtered_stories,
        'total': len(filtered_stories),
        'filters': {
            'level': level,
            'category': category
        }
    }), 200

@api_bp.route('/stories/<int:story_id>', methods=['GET'])
def get_story(story_id):
    """Get a specific story by ID"""
    story_data = {
        0: {
            'id': 0,
            'title': 'Introduction in Okrika',
            'level': 'beginner',
            'description': 'A simple story about two people meeting for the first time',
            'readingTime': '5 minutes',
            'content': {
                'type': 'dialogue',
                'exchanges': [
                    {
                        'speaker': 'Dede',
                        'okrika': 'Í ḅásà, íyá èrè chè?',
                        'english': 'Good morning, what is your name?'
                    },
                    {
                        'speaker': 'Tonye',
                        'okrika': 'Í ḅásà. ìyà èrè ànì Tonye. Írí ka?',
                        'english': 'Good morning. My name is Tonye. And you?'
                    },
                    {
                        'speaker': 'Dede',
                        'okrika': 'Ìyà èrè ànì Dede',
                        'english': 'My name is Dede'
                    },
                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ndè ànì là òkù?',
                        'english': 'How are you?'
                    },
                    {
                        'speaker': 'Dede',
                        'okrika': 'ìbì mè',
                        'english': 'I am good'
                    },
                    
                    {
                        'speaker': 'Dede',
                        'okrika': 'Ñdè àngà Í paka bo?',
                        'english': 'Where do  you come from?'
                    },
                    
                    {
                        'speaker': 'Tonye',
                        'okrika': 'Port Harcourt à àngà me',
                        'english': 'I live in Port Harcourt'
                    },

                    {
                        'speaker': 'Dede',
                        'okrika': 'Ahh, ànìjú ìyà fúrō àngà mè!',
                        'english': 'Ahh, my family lives there!'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ànì ìbì mè',
                        'english': 'That is good'
                    },
                    
                    {
                        'speaker': 'Dede',
                        'okrika': 'Í fìrìnwèngí?',
                        'english': 'Do you work?'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ììn, Ìrí software engineer',
                        'english': 'Yes, I\'m a software engineer'
                    },
                    
                    {
                        'speaker': 'Dede',
                        'okrika': 'Í ìgbìkì nyànà mo!',
                        'english': 'You have money!'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ììñ, À némí mè!',
                        'english': 'Yes, I know!'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Kélédīkī, Í chè yéè be?',
                        'english': 'Later, what will you do?'
                    },
                    
                    {
                        'speaker': 'Dede',
                        'okrika': 'À nwon chì\'n kélédīkī À chik-fi-a muñ bìà ànìàtíbí fị́yè ị̀ tàrị̀ àḅẹ̀',
                        'english': 'I think later I will go to chik-fil-a because I\'m hungry'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ìríma, À sùkùlù muñ bìà. À dírídáwò bì mè.',
                        'english': 'Myself, I will go to school. I want to study.'
                    },
                    
                    {
                        'speaker': 'Dede',
                        'okrika': 'Bùkùró mà',
                        'english': 'Try hard'
                    },

                    {
                        'speaker': 'Tonye',
                        'okrika': 'Ììñ, À bùkùró mà bìà',
                        'english': 'Yes, I will try'
                    }
                    
                ]
            }
        }
    }
    
    story = story_data.get(story_id)
    if not story:
        return jsonify({'error': 'Story not found'}), 404
    
    return jsonify(story), 200

@api_bp.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if not all([name, email, message]):
        return jsonify({'error': 'Missing required fields: name, email, and message are required'}), 400
    
    # Validate email format (basic)
    if '@' not in email:
        return jsonify({'error': 'Invalid email format'}), 400
    
    # In production, you would:
    # - Send an email notification
    # - Save to database
    # - Send confirmation email to user
    
    return jsonify({
        'message': 'Thank you for contacting us! We will get back to you soon.',
        'status': 'success',
        'submitted_by': name
    }), 200

