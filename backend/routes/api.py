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
            'title': 'Common Verbs',
            'level': 'beginner',
            'description': 'Learn essential verbs and their conjugations in Okrika',
            'duration': '25 minutes',
            'category': 'grammar'
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
        },
        {
            'id': 7,
            'title': 'Showing Time: Part 1',
            'level': 'beginner',
            'description': 'Learn core words and phrases for expressing time in Okrika.',
            'duration': '15 minutes',
            'category': 'vocabulary'
        },
        {
            'id': 9,
            'title': 'Showing Time: Part 2',
            'level': 'beginner',
            'description': 'Continue learning time expressions and frequency words in Okrika.',
            'duration': '15 minutes',
            'category': 'vocabulary'
        },
        {
            'id': 8,
            'title': 'Question Words',
            'level': 'beginner',
            'description': 'Learn how to ask questions in Okrika with who, what, when, where, and whom.',
            'duration': '15 minutes',
            'category': 'vocabulary'
        },
        {
            'id': 10,
            'title': 'Connector Words',
            'level': 'beginner',
            'description': 'Learn words that link ideas in Okrika — because, also, while, and more.',
            'duration': '15 minutes',
            'category': 'grammar'
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
                                        'okrika': 'Ì bìmé, mìébákà. Ñdé àní laa òkú?',
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
                                        'okrika': 'Ìnìa bù dèìñ wárábe, mìébákà',
                                        'english': 'They\'re doing fine, thank you.'
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
                                        'okrika': 'Mìébákà! Í ómì?',
                                        'english': 'Thank you! You there?'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'À ómì-e. Ñdè íyá fúró sìmè òkù?',
                                        'english': 'I\'m here. How is your family?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Íní ómì, mìébákà!',
                                        'english': "They\'re there, thank you!"
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
                                        'okrika': 'Mẹ́ ḅírí',
                                        'english': 'I am fine'
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
            'title': 'Common Verbs',
            'level': 'beginner',
            'description': 'Learn everyday action verbs in Okrika: jump, run, sit, walk, read, write, listen, hear, understand, speak and more.',
            'duration': '25 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Understanding Tenses',
                        'type': 'text',
                        'content': 'In Okrika, verbs are conjugated to express different time references by adding specific tense markers after the verb. Understanding these tense markers will help you communicate about actions in the past, present, and future.\n\nHere are the tense markers used in Okrika:\n\n• Present Continuous: Add "àbè" after the verb (e.g., "bô àbè" = coming/am coming)\n• Past Tense: Add "mè" after the verb (e.g., "bô mè" = came)\n• Past Participle: Add "sàm" after the verb (e.g., "bô sàm" = have come/have been)\n• Future: Add "bìà" after the verb (e.g., "bô bìà" = will come)\n\nThe verb itself remains the same; by adding these markers after it, you change the tense. For example, the verb "bô" (come) becomes:\n\n• "À bô àbè" = I am coming (Present Continuous)\n• "À bô mè" = I came (Past Tense)\n• "Ó bô sàm" = He has come (Past Participle)\n• "Íní bô bìà" = They will come (Future)\n\nClick on each tense in the conjugations section below to see more examples of how these tense markers are used with different verbs.'
                    },
                    {
                        'part': 2,
                        'title': 'Learn Common Verbs (with conjugations)',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'bô',
                                'english': 'come',
                                'example': 'Daniel, bô',
                                'exampleTranslation': 'Daniel, come',
                                'audioUrl': '/audio/lesson3/wono.m4a',
                                'exampleAudioUrl': '/audio/lesson3/wono-exe.m4a',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'À bô àbè',
                                        'exampleTranslation': 'I am coming',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À bô mè',
                                        'exampleTranslation': 'I came',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó bô sàm',
                                        'exampleTranslation': 'He has come',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní bô bìà',
                                        'exampleTranslation': 'They will come',
                                        'audioUrl': ''
                                    }
                                }
                            },
                            {
                                'okrika': 'múñ',
                                'english': 'go',
                                'example': 'Múñ fiye ma oki bo',
                                'exampleTranslation': 'Go and bring the food',
                                'audioUrl': '/audio/lesson3/wono.m4a',
                                'exampleAudioUrl': '/audio/lesson3/wono-exe.m4a',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'Í múñ àbè',
                                        'exampleTranslation': 'I am coming',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À múñ mè',
                                        'exampleTranslation': 'I came',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó múñ sàm',
                                        'exampleTranslation': 'He have come',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní múñ bìà',
                                        'exampleTranslation': 'They will come',
                                        'audioUrl': ''
                                    }
                                }
                            },
                            {
                                'okrika': 'kàínbó',
                                'english': 'to understand',
                                'partOfSpeech': 'verb',
                                'definition': 'Perceive the intended meaning of (words, a language, or speaker)',
                                'example': 'Í kàínbó?',
                                'exampleTranslation': 'Do you understand?',
                                'audioUrl': '',
                                'exampleAudioUrl': '',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'À kàínbó àbè',
                                        'exampleTranslation': 'I am understanding',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À kàínbó mè',
                                        'exampleTranslation': 'I understood',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó kàínbó sàm',
                                        'exampleTranslation': 'He has understood',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní kàínbó bìà',
                                        'exampleTranslation': 'They will understand',
                                        'audioUrl': ''
                                    }
                                }
                            },
                            {
                                'okrika': 'pókī',
                                'english': 'to listen',
                                'partOfSpeech': 'verb',
                                'example': 'Ị́ pókī',
                                'exampleTranslation': 'You listen',
                                'audioUrl': '',
                                'exampleAudioUrl': '',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'Í pókī àbè',
                                        'exampleTranslation': 'You are listening',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À pókī mè',
                                        'exampleTranslation': 'I listened',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó pókī sàm',
                                        'exampleTranslation': 'He has listened',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní pókī bìà',
                                        'exampleTranslation': 'They will listen',
                                        'audioUrl': ''
                                    }
                                }
                            },
                            {
                                'okrika': 'nàa',
                                'english': 'to hear',
                                'partOfSpeech': 'verb',
                                'example': 'Ị́ nàa',
                                'exampleTranslation': 'You hear',
                                'audioUrl': '',
                                'exampleAudioUrl': '',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'Í nàa àbè',
                                        'exampleTranslation': 'You are hearing',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À nàa mè',
                                        'exampleTranslation': 'I heard',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó nàa sàm',
                                        'exampleTranslation': 'He has heard',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní nàa bìà',
                                        'exampleTranslation': 'They will hear',
                                        'audioUrl': ''
                                    }
                                }
                            },
                            {
                                'okrika': 'ókúẹín',
                                'english': 'to talk or speak',
                                'partOfSpeech': 'verb',
                                'example': 'Ị́ ókúẹín',
                                'exampleTranslation': 'You talk',
                                'audioUrl': '',
                                'exampleAudioUrl': '',
                                'conjugations': {
                                    'presentContinuous': {
                                        'example': 'Í ókúẹín àbè',
                                        'exampleTranslation': 'You are talking',
                                        'audioUrl': ''
                                    },
                                    'pastTense': {
                                        'example': 'À ókúẹín mè',
                                        'exampleTranslation': 'I talked',
                                        'audioUrl': ''
                                    },
                                    'pastParticiple': {
                                        'example': 'Ó ókúẹín sàm',
                                        'exampleTranslation': 'He has talked',
                                        'audioUrl': ''
                                    },
                                    'future': {
                                        'example': 'Íní ókúẹín bìà',
                                        'exampleTranslation': 'They will talk',
                                        'audioUrl': ''
                                    }
                                }
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Movement and posture',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'fúkù',
                                'english': 'jump',
                                'singular': 'fúkù',
                                'example': 'Ị́ fúkù',
                                'exampleTranslation': 'You jump'
                            },
                            {
                                'okrika': 'màñgị̀',
                                'english': 'run',
                                'singular': 'màñgị̀',
                                'example': 'Ọ màñgị̀',
                                'exampleTranslation': 'He/she runs'
                            },
                            {
                                'okrika': 'símè',
                                'english': 'sit',
                                'singular': 'símè',
                                'example': 'Ị́ símè',
                                'exampleTranslation': 'You sit'
                            },
                            {
                                'okrika': 'kpọ́njị̀ símè',
                                'english': 'sit down',
                                'singular': 'kpọ́njị̀ símè',
                                'example': 'Kpọ́njị̀ símè',
                                'exampleTranslation': 'Sit down'
                            },
                            {
                                'okrika': 'sòmbī',
                                'english': 'squat',
                                'singular': 'sòmbī',
                                'example': 'Ọ sòmbī',
                                'exampleTranslation': 'He/she squats'
                            },
                            {
                                'okrika': 'wẹ́́ñgị́',
                                'english': 'walk',
                                'singular': 'wẹ́́ñgị́',
                                'example': 'À wẹ́́ñgị́',
                                'exampleTranslation': 'I walk'
                            },
                            {
                                'okrika': 'bẹ́ é wẹ́ñgị́',
                                'english': 'walk fast',
                                'singular': 'bẹ́ é wẹ́ñgị́',
                                'example': 'Bẹ́ é wẹ́ñgị́',
                                'exampleTranslation': 'Walk fast'
                            },
                            {
                                'okrika': 'tànjị̀',
                                'english': 'climb',
                                'singular': 'tànjị̀',
                                'example': 'Ọ tànjị̀',
                                'exampleTranslation': 'He/she climbs'
                            }
                        ]
                    },
                    {
                        'part': 4,
                        'title': 'Daily actions',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'yé fị̀',
                                'english': 'eat',
                                'singular': 'yé fị̀',
                                'example': 'Yé fị̀ / fị́yé fị̀',
                                'exampleTranslation': 'Eat'
                            },
                            {
                                'okrika': 'ị́ñọ́ sárá',
                                'english': 'rest',
                                'singular': 'ị́ñọ́ sárá',
                                'example': 'Ị́ñọ́ sárá',
                                'exampleTranslation': 'Rest'
                            },
                            {
                                'okrika': 'ànwúà',
                                'english': 'yawn',
                                'singular': 'ànwúà',
                                'example': 'Ọ ànwúà',
                                'exampleTranslation': 'He/she yawns'
                            },
                            {
                                'okrika': 'góō',
                                'english': 'read',
                                'singular': 'góō',
                                'example': 'Ị́ góō',
                                'exampleTranslation': 'You read'
                            },
                            {
                                'okrika': 'kị̀ẹ́ñ',
                                'english': 'count',
                                'singular': 'kị̀ẹ́ñ',
                                'example': 'À kị̀ẹ́ñ',
                                'exampleTranslation': 'I count'
                            },
                            {
                                'okrika': 'gị̀ẹ́ñ',
                                'english': 'write',
                                'singular': 'gị̀ẹ́ñ',
                                'example': 'Ọ gị̀ẹ́ñ',
                                'exampleTranslation': 'He/she writes'
                            },
                            {
                                'okrika': 'ọ̣́kwẹ́ị́ñ',
                                'english': 'speak',
                                'singular': 'ọ̣́kwẹ́ị́ñ',
                                'example': 'Ọ̣́kwẹ́ị́ñ Kịrịkị',
                                'exampleTranslation': 'Speak Okrika'
                            }
                        ]
                    },
                    {
                        'part': 5,
                        'title': 'Other actions',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'ọ́sụ́ñ',
                                'english': 'vomit',
                                'singular': 'ọ́sụ́ñ',
                                'example': 'Ọ́sụ́ñ / ọ̀kọ̀',
                                'exampleTranslation': 'Vomit'
                            },
                            {
                                'okrika': 'ọ́lọ́',
                                'english': 'cough',
                                'singular': 'ọ́lọ́',
                                'example': 'Ọ ọ́lọ́',
                                'exampleTranslation': 'He/she coughs'
                            },
                            {
                                'okrika': 'ḅị́ẹ́',
                                'english': 'defecate',
                                'singular': 'ḅị́ẹ́',
                                'example': 'Ḅị́ẹ́',
                                'exampleTranslation': 'Defecate'
                            },
                            {
                                'okrika': 'sán̄',
                                'english': 'urinate',
                                'singular': 'sán̄',
                                'example': 'Ọ sán̄',
                                'exampleTranslation': 'He/she urinates'
                            }
                        ]
                    },
                    {
                        'part': 6,
                        'title': 'Test your knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "fúkù" mean?',
                                'correctAnswer': 'jump',
                                'options': ['jump', 'run', 'sit', 'walk']
                            },
                            {
                                'id': 2,
                                'question': 'What does "màñgị̀" mean?',
                                'correctAnswer': 'run',
                                'options': ['run', 'jump', 'walk', 'climb']
                            },
                            {
                                'id': 3,
                                'question': 'What does "símè" mean?',
                                'correctAnswer': 'sit',
                                'options': ['sit', 'sit down', 'squat', 'rest']
                            },
                            {
                                'id': 4,
                                'question': 'What does "kpọ́njị̀ símè" mean?',
                                'correctAnswer': 'sit down',
                                'options': ['sit', 'sit down', 'squat', 'rest']
                            },
                            {
                                'id': 5,
                                'question': 'What does "sòmbī" mean?',
                                'correctAnswer': 'squat',
                                'options': ['squat', 'sit', 'run', 'rest']
                            },
                            {
                                'id': 6,
                                'question': 'What does "ànwúà" mean?',
                                'correctAnswer': 'yawn',
                                'options': ['yawn', 'rest', 'eat', 'cough']
                            },
                            {
                                'id': 7,
                                'question': 'What does "ị́ñọ́ sárá" mean?',
                                'correctAnswer': 'rest',
                                'options': ['rest', 'yawn', 'sit', 'walk']
                            },
                            {
                                'id': 8,
                                'question': 'What does "wẹ́́ñgị́" mean?',
                                'correctAnswer': 'walk',
                                'options': ['walk', 'run', 'climb', 'sit']
                            },
                            {
                                'id': 9,
                                'question': 'What does "bẹ́ é wẹ́ñgị́" mean?',
                                'correctAnswer': 'walk fast',
                                'options': ['walk fast', 'walk', 'run', 'climb']
                            },
                            {
                                'id': 10,
                                'question': 'What does "yé fị̀" mean?',
                                'correctAnswer': 'eat',
                                'options': ['eat', 'yawn', 'read', 'write']
                            },
                            {
                                'id': 11,
                                'question': 'What does "ọ́sụ́ñ" mean?',
                                'correctAnswer': 'vomit',
                                'options': ['vomit', 'cough', 'urinate', 'eat']
                            },
                            {
                                'id': 12,
                                'question': 'What does "ọ́lọ́" mean?',
                                'correctAnswer': 'cough',
                                'options': ['cough', 'vomit', 'defecate', 'yawn']
                            },
                            {
                                'id': 13,
                                'question': 'What does "ḅị́ẹ́" mean?',
                                'correctAnswer': 'defecate',
                                'options': ['defecate', 'urinate', 'vomit', 'cough']
                            },
                            {
                                'id': 14,
                                'question': 'What does "sán̄" mean?',
                                'correctAnswer': 'urinate',
                                'options': ['urinate', 'defecate', 'yawn', 'climb']
                            },
                            {
                                'id': 15,
                                'question': 'What does "tànjị̀" mean?',
                                'correctAnswer': 'climb',
                                'options': ['climb', 'sit', 'run', 'walk']
                            },
                            {
                                'id': 16,
                                'question': 'What does "góō" mean?',
                                'correctAnswer': 'read',
                                'options': ['read', 'write', 'count', 'listen']
                            },
                            {
                                'id': 17,
                                'question': 'What does "kị̀ẹ́ñ" mean?',
                                'correctAnswer': 'count',
                                'options': ['count', 'read', 'write', 'speak']
                            },
                            {
                                'id': 18,
                                'question': 'What does "gị̀ẹ́ñ" mean?',
                                'correctAnswer': 'write',
                                'options': ['write', 'count', 'read', 'speak']
                            },
                            {
                                'id': 19,
                                'question': 'What does "pókī" mean?',
                                'correctAnswer': 'to listen',
                                'options': ['to listen', 'to hear', 'to understand', 'to speak']
                            },
                            {
                                'id': 20,
                                'question': 'What does "ọ̣́kwẹ́ị́ñ" mean?',
                                'correctAnswer': 'speak',
                                'options': ['speak', 'to listen', 'to hear', 'read']
                            },
                            {
                                'id': 21,
                                'question': 'What does "kàínbó" mean?',
                                'correctAnswer': 'to understand',
                                'options': ['to understand', 'to hear', 'to listen', 'to speak']
                            },
                            {
                                'id': 22,
                                'question': 'What does "nàa" mean?',
                                'correctAnswer': 'to hear',
                                'options': ['to hear', 'to listen', 'to understand', 'to speak']
                            },
                            {
                                'id': 23,
                                'question': 'What does "ókúẹín" mean?',
                                'correctAnswer': 'to talk or speak',
                                'options': ['to talk or speak', 'to hear', 'to listen', 'to understand']
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
                'parts': [
                    {
                        'part': 1,
                        'title': 'Family Members',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'ñyèñgìbọ̀',
                                'english': 'Mother',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'dàbọ̀',
                                'english': 'Father',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'ìmbìrè',
                                'english': 'Brother',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'ịmbụ̀rà',
                                'english': 'Sister',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'ówú tọ́kụ̀',
                                'english': 'Son',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'éréméní tọ̀kù',
                                'english': 'Daughter',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'tàā',
                                'english': 'Wife',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'dèbọ̀',
                                'english': 'Husband',
                                'example': '',
                                'exampleTranslation': ''
                            }
                        ]
                    },
                    {
                        'part': 2,
                        'title': 'More Family Terms',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'òpùdàbọ̀',
                                'english': 'Grandfather',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'òpùnyēǹgíbọ̀',
                                'english': 'Grandmother',
                                'example': '',
                                'exampleTranslation': ''
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Test Your Knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "ñyèñgìbọ̀" mean?',
                                'correctAnswer': 'Mother',
                                'options': ['Mother', 'Father', 'Grandmother', 'Sister']
                            },
                            {
                                'id': 2,
                                'question': 'What does "dàbọ̀" mean?',
                                'correctAnswer': 'Father',
                                'options': ['Father', 'Mother', 'Grandfather', 'Son']
                            },
                            {
                                'id': 3,
                                'question': 'What does "ìmbìrè" mean?',
                                'correctAnswer': 'Brother',
                                'options': ['Brother', 'Sister', 'Son', 'Daughter']
                            },
                            {
                                'id': 4,
                                'question': 'What does "ịmbụ̀rà" mean?',
                                'correctAnswer': 'Sister',
                                'options': ['Sister', 'Brother', 'Wife', 'Mother']
                            },
                            {
                                'id': 5,
                                'question': 'What does "ówú tọ́kụ̀" mean?',
                                'correctAnswer': 'Son',
                                'options': ['Son', 'Daughter', 'Brother', 'Father']
                            },
                            {
                                'id': 6,
                                'question': 'What does "éréméní tọ̀kù" mean?',
                                'correctAnswer': 'Daughter',
                                'options': ['Daughter', 'Son', 'Sister', 'Wife']
                            },
                            {
                                'id': 7,
                                'question': 'What does "tàā" mean?',
                                'correctAnswer': 'Wife',
                                'options': ['Wife', 'Husband', 'Mother', 'Sister']
                            },
                            {
                                'id': 8,
                                'question': 'What does "dèbọ̀" mean?',
                                'correctAnswer': 'Husband',
                                'options': ['Husband', 'Wife', 'Father', 'Son']
                            },
                            {
                                'id': 9,
                                'question': 'What does "òpùdàbọ̀" mean?',
                                'correctAnswer': 'Grandfather',
                                'options': ['Grandfather', 'Grandmother', 'Father', 'Mother']
                            },
                            {
                                'id': 10,
                                'question': 'What does "òpùnyēǹgíbọ̀" mean?',
                                'correctAnswer': 'Grandmother',
                                'options': ['Grandmother', 'Grandfather', 'Mother', 'Wife']
                            }
                        ]
                    }
                ]
            }
        },
        5: {
            'id': 5,
            'title': 'Food and Dining',
            'level': 'intermediate',
            'description': 'Learn cooking methods, food prep, and eating phrases in Okrika.',
            'duration': '30 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Food preparation vocabulary',
                        'type': 'text',
                        'content': 'This lesson covers everyday words for cooking, preparing food, and eating in Okrika (Kịrịkị). You will learn cooking methods like steam, boil, roast, and smoke, plus actions like chop, peel, and scoop. Focus on the phrases you would use in a kitchen or at the table.'
                    },
                    {
                        'part': 2,
                        'title': 'Cooking methods',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'chụ̀ọ̀',
                                'english': 'cook',
                                'singular': 'chụ̀ọ̀',
                                'example': 'À fị̀yẹ̀ chụ̀ọ̀ ḅimẹ̀',
                                'exampleTranslation': 'I want to cook'
                            },
                            {
                                'okrika': 'sù',
                                'english': 'steam',
                                'singular': 'sù',
                                'example': 'Tátárị́ ị̀njị mị̀ sù',
                                'exampleTranslation': 'First, steam the fish'
                            },
                            {
                                'okrika': 'ḍàrị̀',
                                'english': 'boil',
                                'singular': 'ḍàrị̀',
                                'example': 'Mẹ̀ngị̀ mị̀ ḍárị́ sà?',
                                'exampleTranslation': 'Has the water boiled?'
                            },
                            {
                                'okrika': 'fọ̀ị̀',
                                'english': 'roast',
                                'singular': 'fọ̀ị̀',
                                'example': 'Ọ̀ fọ̀ị̀ mbị̀nà fẹ̀ ḅò mẹ̀',
                                'exampleTranslation': 'He bought roasted plantain'
                            },
                            {
                                'okrika': 'ị́rụ̀ọ̀',
                                'english': 'smoke',
                                'singular': 'ị́rụ̀ọ̀',
                                'example': 'Ị̀rụ̀ọ̀ sàmị̀nà ị̀njị ḅàkà mẹ̀',
                                'exampleTranslation': 'There was a lot of smoked-dried fish'
                            },
                            {
                                'okrika': 'ànànà',
                                'english': 'grill / smoke (fish)',
                                'singular': 'ànànà',
                                'example': 'Árị́ ị̀njị ànànà àḅẹ̀',
                                'exampleTranslation': 'She is smoking fish'
                            }
                        ]
                    },
                    {
                        'part': 3,
                        'title': 'Food prep actions',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'tèmì',
                                'english': 'pound',
                                'singular': 'tèmì',
                                'example': 'Ìkù Ị́ tèmì ḍị̀ñ?',
                                'exampleTranslation': 'Do you know how to pound cocoyam?'
                            },
                            {
                                'okrika': 'gbẹ́ị̀ñ',
                                'english': 'grind',
                                'singular': 'gbẹ́ị̀ñ',
                                'example': 'Kẹ̀lẹ̀ fụ́lọ̀ chụ̀ạ̀ àyẹmà gbẹ̀ị̀ñ ị̀ pị̀rị̀',
                                'exampleTranslation': 'Please grind the soup ingredients for me'
                            },
                            {
                                'okrika': 'sẹ́ngị̀',
                                'english': 'slice',
                                'singular': 'sẹ́ngị̀',
                                'example': 'Ị́jápụ́ mị́, ị́ sẹ̣́ngị́ sà?',
                                'exampleTranslation': 'Have you sliced the cassava?'
                            },
                            {
                                'okrika': 'kị́rị́',
                                'english': 'chop',
                                'singular': 'kị́rị́',
                                'example': 'Fụ̀lọ̀ chụ̀ọ̀ ị̀ñyàñyà mà kị̀rị̀',
                                'exampleTranslation': 'Chop the green (soup) vegetables'
                            },
                            {
                                'okrika': 'wólì',
                                'english': 'cut',
                                'singular': 'wólì',
                                'example': 'Námá mị̀ ọ̀ wòlì sàm',
                                'exampleTranslation': 'He has chopped the meat'
                            },
                            {
                                'okrika': 'ọ̀ngị̀',
                                'english': 'peel (oranges)',
                                'singular': 'ọ̀ngị̀',
                                'example': 'Èlẹ̀lẹ̀ndà mà ọ̀ngị̄ wà pị̀rị̀',
                                'exampleTranslation': 'Peel the oranges for us'
                            },
                            {
                                'okrika': 'pị́nị́',
                                'english': 'peel (plantain, cassava)',
                                'singular': 'pị́nị́',
                                'example': 'Mbị́nà mà pị̀nị̀',
                                'exampleTranslation': 'Peel the plantains'
                            },
                            {
                                'okrika': 'ñwọ̀ị̀ñ',
                                'english': 'scrape',
                                'singular': 'ñwọ̀ị̀ñ',
                                'example': 'Fọ̀ị̀ mbị́nà mà ñwọ̀ị̀ñ',
                                'exampleTranslation': 'Scrape the roasted plantains'
                            },
                            {
                                'okrika': 'ḍù',
                                'english': 'scoop',
                                'singular': 'ḍù',
                                'example': 'Àkị́ḍị̀ ḍū ọ̣̀ pị̀rị̀',
                                'exampleTranslation': 'Scoop beans for him'
                            }
                        ]
                    },
                    {
                        'part': 4,
                        'title': 'Eating and drinking',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'fị́',
                                'english': 'eat',
                                'singular': 'fị́',
                                'example': 'Ḅò yẹ fị̀',
                                'exampleTranslation': 'Come and eat'
                            },
                            {
                                'okrika': 'tòkùrù',
                                'english': 'chew',
                                'singular': 'tòkùrù',
                                'example': 'Ìḅịọ̀kụ̀ mà ànị́ tòkùrù',
                                'exampleTranslation': 'Chew it very well'
                            },
                            {
                                'okrika': 'mị̀nị̀',
                                'english': 'swallow',
                                'singular': 'mị̀nị̀',
                                'example': 'Ḅù ḍịrị mị̀ mị̀nị̀',
                                'exampleTranslation': 'Swallow the tablets'
                            },
                            {
                                'okrika': 'ḅù',
                                'english': 'drink',
                                'singular': 'ḅù',
                                'example': 'Mẹ̀ngị̀ mị̀, ḅù',
                                'exampleTranslation': 'Drink the water'
                            },
                            {
                                'okrika': 'féní',
                                'english': 'rice',
                                'singular': 'féní',
                                'example': 'Á féní fị́yẹ chụ̀ọ̄ àḅẹ̀',
                                'exampleTranslation': 'She is cooking rice'
                            },
                            {
                                'okrika': 'ị̀njị',
                                'english': 'fish',
                                'singular': 'ị̀njị',
                                'example': 'Tátárị́ ị̀njị mị̀ sù',
                                'exampleTranslation': 'First, steam the fish'
                            },
                            {
                                'okrika': 'mbị̀nà',
                                'english': 'plantain',
                                'singular': 'mbị̀nà',
                                'example': 'Mbị́nà mà pị̀nị̀',
                                'exampleTranslation': 'Peel the plantains'
                            },
                            {
                                'okrika': 'mẹ̀ngị̀',
                                'english': 'water',
                                'singular': 'mẹ̀ngị̀',
                                'example': 'Mẹ̀ngị̀ mị̀, ḅù',
                                'exampleTranslation': 'Drink the water'
                            },
                            {
                                'okrika': 'àkị́ḍị̀',
                                'english': 'beans',
                                'singular': 'àkị́ḍị̀',
                                'example': 'Àkị́ḍị̀ ḍū ọ̣̀ pị̀rị̀',
                                'exampleTranslation': 'Scoop beans for him'
                            },
                            {
                                'okrika': 'námá',
                                'english': 'meat',
                                'singular': 'námá',
                                'example': 'Námá mị̀ ọ̀ wòlì sàm',
                                'exampleTranslation': 'He has chopped the meat'
                            }
                        ]
                    },
                    {
                        'part': 5,
                        'title': 'Test your knowledge',
                        'type': 'quiz',
                        'questions': [
                            {
                                'id': 1,
                                'question': 'What does "chụ̀ọ̀" mean?',
                                'correctAnswer': 'cook',
                                'options': ['cook', 'eat', 'drink', 'boil']
                            },
                            {
                                'id': 2,
                                'question': 'What does "sù" mean?',
                                'correctAnswer': 'steam',
                                'options': ['steam', 'roast', 'boil', 'smoke']
                            },
                            {
                                'id': 3,
                                'question': 'What does "fị́" mean?',
                                'correctAnswer': 'eat',
                                'options': ['drink', 'eat', 'cook', 'chew']
                            },
                            {
                                'id': 4,
                                'question': 'What does "ḅù" mean?',
                                'correctAnswer': 'drink',
                                'options': ['eat', 'drink', 'swallow', 'cook']
                            },
                            {
                                'id': 5,
                                'question': 'How do you say "Come and eat" in Okrika?',
                                'correctAnswer': 'Ḅò yẹ fị̀',
                                'options': ['Ḅò yẹ fị̀', 'Mẹ̀ngị̀ mị̀, ḅù', 'Ị́njị mị̀ sù', 'Àkị́ḍị̀ ḍù']
                            },
                            {
                                'id': 6,
                                'question': 'What does "mbị̀nà" mean?',
                                'correctAnswer': 'plantain',
                                'options': ['rice', 'fish', 'plantain', 'beans']
                            },
                            {
                                'id': 7,
                                'question': 'What does "pị́nị́" mean?',
                                'correctAnswer': 'peel (plantain, cassava)',
                                'options': ['chop', 'slice', 'peel (plantain, cassava)', 'scrape']
                            },
                            {
                                'id': 8,
                                'question': 'What does "tòkùrù" mean?',
                                'correctAnswer': 'chew',
                                'options': ['eat', 'chew', 'swallow', 'drink']
                            }
                        ]
                    },
                    {
                        'part': 6,
                        'title': 'At the table',
                        'type': 'dialogue',
                        'dialogues': [
                            {
                                'title': 'Mealtime',
                                'exchanges': [
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'Ḅò yẹ fị̀',
                                        'english': 'Come and eat'
                                    },
                                    {
                                        'speaker': 'Guest',
                                        'okrika': 'Mìébákà.',
                                        'english': 'Thank you.'
                                    },
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'Mẹ̀ngị̀ mị̀, ḅù.',
                                        'english': 'Drink the water.'
                                    },
                                    {
                                        'speaker': 'Host',
                                        'okrika': 'Ìḅịọ̀kụ̀ mà ànị́ tòkùrù.',
                                        'english': 'Chew it very well.'
                                    }
                                ]
                            },
                            {
                                'title': 'In the kitchen',
                                'exchanges': [
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'À fị̀yẹ̀ chụ̀ọ̀ ḅimẹ̀. Mẹ̀ngị̀ mị̀ ḍárị́ sà?',
                                        'english': 'I want to cook. Has the water boiled?'
                                    },
                                    {
                                        'speaker': 'Person B',
                                        'okrika': 'Ììn. Tátárị́ ị̀njị mị̀ sù.',
                                        'english': 'Yes. First, steam the fish.'
                                    },
                                    {
                                        'speaker': 'Person A',
                                        'okrika': 'Kẹ̀lẹ̀ fụ́lọ̀ chụ̀ạ̀ àyẹmà gbẹ̀ị̀ñ ị̀ pị̀rị̀.',
                                        'english': 'Please grind the soup ingredients for me.'
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        7: {
            'id': 7,
            'title': 'Showing Time: Part 1',
            'level': 'beginner',
            'description': 'Learn core words and phrases for expressing time in Okrika.',
            'duration': '15 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn time words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'míókù',
                                'english': 'now; this moment',
                                'partOfSpeech': 'adverb',
                                'definition': 'At the present time',
                                'example': 'Míókù í bô au?',
                                'exampleTranslation': 'Are you coming now?'
                            },
                            {
                                'okrika': 'kélédīkī',
                                'english': 'afterwards; sometime later',
                                'partOfSpeech': 'adverb',
                                'definition': 'At a later or future time',
                                'example': 'kélédīkī à mèngí bû bià?',
                                'exampleTranslation': 'Later I will drink water'
                            },
                            {
                                'okrika': 'mímgbà',
                                'english': 'today',
                                'partOfSpeech': 'noun',
                                'definition': 'On or in the course of this present day',
                                'example': 'Mímgbà ò dàdíkì gíén mè',
                                'exampleTranslation': 'He wrote his exam today'
                            },
                            {
                                'okrika': 'sìméògbò',
                                'english': 'while',
                                'partOfSpeech': 'conjunction',
                                'definition': 'During the time that',
                                'example': 'Sìméògbò í ómì, bô yéfí',
                                'exampleTranslation': 'While you are here, come and eat'
                            },
                            {
                                'okrika': 'bịá',
                                'english': 'yesterday',
                                'partOfSpeech': 'noun',
                                'definition': 'The day before today',
                                'example': 'Bịá ó só mè',
                                'exampleTranslation': 'He left yesterday'
                            },
                            {
                                'okrika': 'bá',
                                'english': 'tomorrow',
                                'partOfSpeech': 'noun',
                                'definition': 'The day after today',
                                'example': 'Bá í múñ be?',
                                'exampleTranslation': 'Will you go tomorrow?'
                            },
                            {
                                'okrika': 'Ḍíñ-ógbò',
                                'english': 'midnight',
                                'partOfSpeech': 'noun',
                                'definition': 'The middle of the night',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'gbásó',
                                'english': 'forever',
                                'partOfSpeech': 'adverb',
                                'definition': 'For all time; eternally',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'N̄gịsị̀',
                                'english': 'never',
                                'partOfSpeech': 'adverb',
                                'definition': 'At no time; not ever',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Ólómú sịkị',
                                'english': 'ancient times',
                                'partOfSpeech': 'phrase',
                                'definition': 'A long time ago in the past',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Sị́kị́ná sị́kị́ná',
                                'english': 'as time goes on; eventually; time and again',
                                'partOfSpeech': 'phrase',
                                'definition': 'Over time; in the end; repeatedly',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Sị́kị́ mámgbà',
                                'english': 'every time',
                                'partOfSpeech': 'phrase',
                                'definition': 'On each occasion; always when',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Ótókú',
                                'english': 'noon',
                                'partOfSpeech': 'noun',
                                'definition': 'Twelve o\'clock in the day; midday',
                                'example': '',
                                'exampleTranslation': ''
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
                                'question': 'What does "míókù" mean?',
                                'correctAnswer': 'now; this moment',
                                'options': ['now; this moment', 'today', 'yesterday', 'tomorrow']
                            },
                            {
                                'id': 2,
                                'question': 'What does "mímgbà" mean?',
                                'correctAnswer': 'today',
                                'options': ['today', 'yesterday', 'tomorrow', 'never']
                            },
                            {
                                'id': 3,
                                'question': 'What does "bịá" mean?',
                                'correctAnswer': 'yesterday',
                                'options': ['yesterday', 'tomorrow', 'today', 'now; this moment']
                            },
                            {
                                'id': 4,
                                'question': 'What does "bá" mean?',
                                'correctAnswer': 'tomorrow',
                                'options': ['tomorrow', 'yesterday', 'today', 'forever']
                            },
                            {
                                'id': 5,
                                'question': 'What does "kélédīkī" mean?',
                                'correctAnswer': 'afterwards; sometime later',
                                'options': ['afterwards; sometime later', 'now; this moment', 'never', 'while']
                            },
                            {
                                'id': 6,
                                'question': 'What does "N̄gịsị̀" mean?',
                                'correctAnswer': 'never',
                                'options': ['never', 'forever', 'every time', 'noon']
                            },
                            {
                                'id': 7,
                                'question': 'What does "gbásó" mean?',
                                'correctAnswer': 'forever',
                                'options': ['forever', 'never', 'midnight', 'noon']
                            },
                            {
                                'id': 8,
                                'question': 'What does "Ótókú" mean?',
                                'correctAnswer': 'noon',
                                'options': ['noon', 'midnight', 'today', 'yesterday']
                            }
                        ]
                    }
                ]
            }
        },
        9: {
            'id': 9,
            'title': 'Showing Time: Part 2',
            'level': 'beginner',
            'description': 'Continue learning time expressions and frequency words in Okrika.',
            'duration': '15 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'More time words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'Súsú bẹ́-ẹ́né',
                                'english': 'three days ago',
                                'partOfSpeech': 'phrase',
                                'definition': 'Three days before today',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Básó',
                                'english': 'early morning',
                                'partOfSpeech': 'noun',
                                'definition': 'The first part of the morning',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Dèdè fúñ fúñ',
                                'english': 'very early in the morning',
                                'partOfSpeech': 'phrase',
                                'definition': 'At dawn; very early before sunrise',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Bé réñ-béré-éné',
                                'english': 'day before yesterday',
                                'partOfSpeech': 'phrase',
                                'definition': 'Two days ago',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Bá bọ́rọ́ bé réñ-béré-éné',
                                'english': 'day after tomorrow',
                                'partOfSpeech': 'phrase',
                                'definition': 'Two days from now',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Dị́ñ',
                                'english': 'night',
                                'partOfSpeech': 'noun',
                                'definition': 'The period of darkness between sunset and sunrise',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Éné tíḅì',
                                'english': 'daily',
                                'partOfSpeech': 'adverb',
                                'definition': 'Every day; each day',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Éné góyè gòyè, éné máñgbà',
                                'english': 'every day',
                                'partOfSpeech': 'phrase',
                                'definition': 'Each day without exception',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Éné kákà (kúḅù)',
                                'english': 'day time',
                                'partOfSpeech': 'phrase',
                                'definition': 'The time when it is light; daytime',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Dàsìkì',
                                'english': 'sometimes',
                                'partOfSpeech': 'adverb',
                                'definition': 'On some occasions; occasionally',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Bàkà síkí (bụ̀)',
                                'english': 'most times',
                                'partOfSpeech': 'phrase',
                                'definition': 'Usually; on most occasions',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Sị́kị́ góyè gòyè',
                                'english': 'regularly',
                                'partOfSpeech': 'adverb',
                                'definition': 'At consistent intervals; habitually',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Sịkị fámá',
                                'english': 'delay',
                                'partOfSpeech': 'noun',
                                'definition': 'A period of time by which something is late',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'Sịkị fámá ká bù',
                                'english': 'immediately',
                                'partOfSpeech': 'adverb',
                                'definition': 'At once; without delay',
                                'example': '',
                                'exampleTranslation': ''
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
                                'question': 'What does "Dị́ñ" mean?',
                                'correctAnswer': 'night',
                                'options': ['night', 'day time', 'early morning', 'daily']
                            },
                            {
                                'id': 2,
                                'question': 'What does "Básó" mean?',
                                'correctAnswer': 'early morning',
                                'options': ['early morning', 'night', 'day after tomorrow', 'sometimes']
                            },
                            {
                                'id': 3,
                                'question': 'What does "Bé réñ-béré-éné" mean?',
                                'correctAnswer': 'day before yesterday',
                                'options': ['day before yesterday', 'day after tomorrow', 'three days ago', 'every day']
                            },
                            {
                                'id': 4,
                                'question': 'What does "Bá bọ́rọ́ bé réñ-béré-éné" mean?',
                                'correctAnswer': 'day after tomorrow',
                                'options': ['day after tomorrow', 'day before yesterday', 'three days ago', 'immediately']
                            },
                            {
                                'id': 5,
                                'question': 'What does "Éné tíḅì" mean?',
                                'correctAnswer': 'daily',
                                'options': ['daily', 'sometimes', 'regularly', 'most times']
                            },
                            {
                                'id': 6,
                                'question': 'What does "Dàsìkì" mean?',
                                'correctAnswer': 'sometimes',
                                'options': ['sometimes', 'daily', 'immediately', 'never']
                            },
                            {
                                'id': 7,
                                'question': 'What does "Sịkị fámá ká bù" mean?',
                                'correctAnswer': 'immediately',
                                'options': ['immediately', 'delay', 'regularly', 'most times']
                            },
                            {
                                'id': 8,
                                'question': 'What does "Súsú bẹ́-ẹ́né" mean?',
                                'correctAnswer': 'three days ago',
                                'options': ['three days ago', 'day before yesterday', 'day after tomorrow', 'every day']
                            }
                        ]
                    }
                ]
            }
        },
        8: {
            'id': 8,
            'title': 'Question Words',
            'level': 'beginner',
            'description': 'Learn how to ask questions in Okrika with who, what, when, where, and whom.',
            'duration': '15 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn question words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'ñdèjù',
                                'english': 'where',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Asking for information specifying a location',
                                'example': 'Ñdèjù ìní ñwòñ mũñ àù?',
                                'exampleTranslation': 'Where are they going?'
                            },
                            {
                                'okrika': 'ñdè sịkị',
                                'english': 'when',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Asking about time',
                                'example': 'Ñdè sịkị í bô bìà?',
                                'exampleTranslation': 'When are you coming?'
                            },
                            {
                                'okrika': 'túbọ̀',
                                'english': 'who',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Asking about a person',
                                'example': 'Àní túbọ̀?',
                                'exampleTranslation': 'Who is that?'
                            },
                            {
                                'okrika': 'àṇị̀ bọ̀ mị̀',
                                'english': 'whom',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Asking about which person (object)',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'chèyè',
                                'english': 'what',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Asking about a thing or action',
                                'example': 'Chèyè í nwōñ bèé?',
                                'exampleTranslation': 'What did you say?'
                            },
                            {
                                'okrika': 'chèyè pàkà',
                                'english': 'what happened',
                                'partOfSpeech': 'phrase',
                                'definition': 'Asking about an event or occurrence',
                                'example': 'Chèyè pàkà?',
                                'exampleTranslation': 'What happened?'
                            },
                            {
                                'okrika': 'ndàyê',
                                'english': 'how many things',
                                'partOfSpeech': 'interrogative',
                                'definition': 'Asking about the quantity of things',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'ndàìgbíkì',
                                'english': 'how much money',
                                'partOfSpeech': 'interrogative',
                                'definition': 'Asking about an amount of money',
                                'example': '',
                                'exampleTranslation': ''
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
                                'question': 'What does "ñdèjù" mean?',
                                'correctAnswer': 'where',
                                'options': ['where', 'when', 'who', 'what']
                            },
                            {
                                'id': 2,
                                'question': 'What does "ñdè sịkị" mean?',
                                'correctAnswer': 'when',
                                'options': ['when', 'where', 'who', 'whom']
                            },
                            {
                                'id': 3,
                                'question': 'What does "ñdè bọ̀" mean?',
                                'correctAnswer': 'who',
                                'options': ['who', 'whom', 'what', 'where']
                            },
                            {
                                'id': 4,
                                'question': 'What does "àṇị̀ bọ̀ mị̀" mean?',
                                'correctAnswer': 'whom',
                                'options': ['whom', 'who', 'what', 'where']
                            },
                            {
                                'id': 5,
                                'question': 'What does "chèyè" mean?',
                                'correctAnswer': 'what',
                                'options': ['what', 'who', 'where', 'when']
                            },
                            {
                                'id': 6,
                                'question': 'What does "chèyè pàkà" mean?',
                                'correctAnswer': 'what happened',
                                'options': ['what happened', 'what', 'where', 'when']
                            },
                            {
                                'id': 7,
                                'question': 'What does "ndàyê" mean?',
                                'correctAnswer': 'how many things',
                                'options': ['how many things', 'how much money', 'what', 'where']
                            },
                            {
                                'id': 8,
                                'question': 'What does "ndàìgbíkì" mean?',
                                'correctAnswer': 'how much money',
                                'options': ['how much money', 'how many things', 'when', 'who']
                            }
                        ]
                    }
                ]
            }
        },
        10: {
            'id': 10,
            'title': 'Connector Words',
            'level': 'beginner',
            'description': 'Learn words that link ideas in Okrika — because, also, while, and more.',
            'duration': '15 minutes',
            'content': {
                'parts': [
                    {
                        'part': 1,
                        'title': 'Learn connector words',
                        'type': 'vocabulary',
                        'items': [
                            {
                                'okrika': 'ànìàtíbí',
                                'english': 'because',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Gives a reason or cause',
                                'example': 'À chik-fi-a muñ bìà ànìàtíbí fị́yè ị̀ tàrị̀ àḅẹ̀',
                                'exampleTranslation': 'I will go to chik-fil-a because I\'m hungry'
                            },
                            {
                                'okrika': 'soni',
                                'english': 'also; too',
                                'partOfSpeech': 'adverb',
                                'definition': 'Adds another idea or includes something more',
                                'example': '',
                                'exampleTranslation': ''
                            },
                            {
                                'okrika': 'sìméògbò',
                                'english': 'while',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Links two actions happening at the same time',
                                'example': 'Sìméògbò í ómì, bô yéfí',
                                'exampleTranslation': 'While you are here, come and eat'
                            },
                            {
                                'okrika': 'kà',
                                'english': 'and; what about',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Connects ideas or turns the question back to someone',
                                'example': 'Í ḅásà. Ìyà èrè ànì Tonye. Írí ka?',
                                'exampleTranslation': 'Good morning. My name is Tonye. And you?'
                            },
                            {
                                'okrika': 'ànì',
                                'english': 'that',
                                'partOfSpeech': 'pronoun',
                                'definition': 'Points to or identifies something already mentioned',
                                'example': 'Ànì ìbì mè',
                                'exampleTranslation': 'That is good'
                            },
                            {
                                'okrika': 'ììñ',
                                'english': 'yes',
                                'partOfSpeech': 'particle',
                                'definition': 'Affirms or agrees before continuing a thought',
                                'example': 'Ììñ, À bùkùró mà bìà',
                                'exampleTranslation': 'Yes, I will try hard'
                            },
                            {
                                'okrika': 'Ọ̀kùmà',
                                'english': 'but',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Used to introduce a statement contrasting with a previous statement',
                                'example': 'Ọ̀kùmà, ị̀rị̀ yèḍìyè bọ̀-ẹ̀',
                                'exampleTranslation': 'But, I am a teacher.'
                            },
                            {
                                'okrika': 'nwòfá/némíkásè',
                                'english': 'if, whether',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Introduces a conditional clause',
                                'example': 'Nwòfá í múñ, à mónō bìà',
                                'exampleTranslation': 'If you go, I will sleep'
                            },
                            {
                                'okrika': 'mị̀ẹ̀ sè',
                                'english': 'so that',
                                'partOfSpeech': 'adverb',
                                'definition': 'In order that',
                                'example': 'Àníjú kpọ̀njị́sìmé mị̀ẹ̀ sè ó ọrí bìà',
                                'exampleTranslation': 'Sit there so that he will see you'
                            },
                            {
                                'okrika': 'nà',
                                'english': 'and',
                                'partOfSpeech': 'conjunction',
                                'definition': 'Joins two words, phrases, or clauses together',
                                'example': 'Tìtì mà á pékéré mè nà á mùñ Káínè',
                                'exampleTranslation': 'Titi answered her and said she was going to Kaine'
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
                                'question': 'What does "ànìàtíbí" mean?',
                                'correctAnswer': 'because',
                                'options': ['because', 'also', 'while', 'that']
                            },
                            {
                                'id': 2,
                                'question': 'What does "soni" mean?',
                                'correctAnswer': 'also; too',
                                'options': ['also; too', 'because', 'yes', 'while']
                            },
                            {
                                'id': 3,
                                'question': 'What does "sìméògbò" mean?',
                                'correctAnswer': 'while',
                                'options': ['while', 'because', 'that', 'and; what about']
                            },
                            {
                                'id': 4,
                                'question': 'What does "kà" mean?',
                                'correctAnswer': 'and; what about',
                                'options': ['and; what about', 'because', 'yes', 'that']
                            },
                            {
                                'id': 5,
                                'question': 'What does "ànì" mean?',
                                'correctAnswer': 'that',
                                'options': ['that', 'because', 'also; too', 'while']
                            },
                            {
                                'id': 6,
                                'question': 'What does "ììñ" mean?',
                                'correctAnswer': 'yes',
                                'options': ['yes', 'no', 'because', 'and; what about']
                            },
                            {
                                'id': 7,
                                'question': 'What does "Ọ̀kùmà" mean?',
                                'correctAnswer': 'but',
                                'options': ['but', 'if, whether', 'so that', 'because']
                            },
                            {
                                'id': 8,
                                'question': 'What does "nwòfá" mean?',
                                'correctAnswer': 'if, whether',
                                'options': ['if, whether', 'but', 'so that', 'while']
                            },
                            {
                                'id': 9,
                                'question': 'What does "mị̀ẹ̀ sè" mean?',
                                'correctAnswer': 'so that',
                                'options': ['so that', 'but', 'if, whether', 'because']
                            },
                            {
                                'id': 10,
                                'question': 'What does "nà" mean?',
                                'correctAnswer': 'and',
                                'options': ['and', 'but', 'because', 'if, whether']
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

@api_bp.route('/profile', methods=['GET'])
def get_profile():
    """Get current user profile with fake data (lessons completed, etc.)"""
    # Fake profile data — in production this would come from auth + database
    return jsonify({
        'user': {
            'id': 1,
            'name': 'Alex',
            'email': 'alex@example.com',
            'avatar': None,
            'joinedAt': '2025-01-15',
            'streak': 5,
            'totalLessonsCompleted': 2,
            'totalStoriesCompleted': 1,
        },
        'completedLessonIds': [0, 1],
        'completedStoryIds': [0],
    }), 200

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
            'title': '"Tátárí gō ḍìrì" by Levi Sika, Vol.1',
            'level': 'intermediate',
            'description': 'Follow Amba on a morning trip to the market, where she runs into Titi and learns about Kaine — a seamstress who sews and sells goods under a tree.',
            'readingTime': '7 minutes',
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
        },
        1: {
            'id': 1,
            'title': '"Tátárí gō ḍìrì" by Levi Sika, Vol.1',
            'level': 'intermediate',
            'description': 'Follow Amba on a morning trip to the market, where she runs into Titi and learns about Kaine — a seamstress who sews and sells goods under a tree.',
            'readingTime': '7 minutes',
            'content': {
                'type': 'paragraphs',
                'paragraphs': [
                    {
                        'okrika': 'Dèdè bìè mí Ámbà má á páká ògòñò mùñ yè è',
                        'english': 'So, it was in the morning, that Amba went out to the Market.'
                    },
                    {
                        'okrika': 'Àtèlì ògbò á bò àrì sìkì á Tìtí má nà bìáñ mà sé,',
                        'english': 'As she was coming on the way, she ran into Titi'
                    },
                    {
                        'okrika': 'á gbèlà mè ñwò fà á ògòñò mùñ á òtùbò?',
                        'english': 'and asked her if she was going to the Market.'
                    },
                    {
                        'okrika': 'Tìtì mà á pékéré mè nà á mùñ Káínè mà bàrà búchùáyè ñwò fè òmū àbè.',
                        'english': 'Titi answered her and said, that she was going to Kaine to buy clothes'
                    },
                    {
                        'okrika': 'Káínè mà á búchùáyè gbìñ gbìñ mè, píkínà dòkò dòkò àyè dèrì dèrì mè.',
                        'english': 'Kaine, sews clothes and also sells various little items'
                    },
                    {
                        'okrika': 'Éjìé chùkù á sìmè árá yè gbìñ gbìñ mè, mìè sè Írùá á lá èkà bàrà.',
                        'english': 'She sews under a tree so that the sun will not beat her'
                    },
                    {
                        'okrika': 'Á gbìñ só sà tòñā búchùáyè á ñwò sè éjìé bù sùkà sùkà mè.',
                        'english': 'She hangs a lot of the clothes she sewed on the tree.'
                    },
                    {
                        'okrika': 'Á víñpìkì bò sìkì á élèlèñdà fè bò mè',
                        'english': 'On her return she bought oranges.'
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

