# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - English question bank (course 210, subject
37534, a 37-chapter shell created this session, chapter names copied
verbatim/live-queried from course 38's "English").

Authored content (not content partner data - loaded with source='synthetic'
via scripts/load_by_chapter_id.py). Same reasoning as
scripts/content/grade11_english.py: linking to course 38's real English
content was reverted after finding it was 100% old
"[SYNTHETIC PLACEHOLDER]" filler.

Content-honesty note: the 37 chapters split into three kinds.
(1) Grammar/language-skill units (Doubt Clearing Session, Critical
Thinking, Idioms and Phrases, Sound System, Punctuation, Dictionary Use,
Parts of Speech, Adjectives and Adverbs, Prepositions,
Conjunctions/Connectives, Reported Speech, Voice, Tense and Aspects,
Question Tag) and (2) Writing Task units (1/2/3) have no single named
text, so content covers general English grammar/usage and writing-skill
concepts - no academic-integrity risk.
(3) Named literary/prose texts (chapters 37552-37571) carry real
academic-integrity risk if a specific plot/character claim I cannot
verify were asserted as fact. For each, questions are grounded ONLY in:
the author's name/nationality where confidently and safely known
(standard literary knowledge - e.g. Anita Desai for "A Devoted Son",
Raymond Carver for "Neighbors", Kate Chopin for "A Respectable Woman",
Gabriel García Márquez for "A Very Old Man with Enormous Wings", H.G.
Wells for "The Treasure in the Forest", Lu Xun for "My Old Home",
Bertrand Russell for "Knowledge and Wisdom"), the genre, and - for texts
whose plot/theme is extremely well-known, canonical public knowledge -
broad, safely-known thematic facts. For titles whose specific source I
am not confident enough to assert (e.g. "The Bull", "A Day", "Soft
Storm", "The Awakening Age"), questions stay at the safe genre/
literary-craft level with NO authorship or plot claim. No invented
quotes, character names, or plot details are presented as fact. Keyed by
verified integer chapter_id. Never presented as content partner content or
as evidence about real students.

This file is authored in batches - batch 1 covers the first six
grammar/language-skill units.
"""

QUESTIONS = {
    37535: [  # Doubt Clearing Session
        {"q": "In a language course, a 'doubt clearing session' typically serves what purpose?", "options": [
            "To review and resolve students' questions about earlier grammar or content", "To introduce entirely new, unrelated material with no review",
            "To administer a final examination", "To avoid any discussion of prior lessons"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is a correctly formed present perfect continuous sentence?", "options": [
            "She has been studying for three hours.", "She has study for three hours.",
            "She had been study for three hours.", "She been studying for three hours."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Identify the sentence with correct subject-verb agreement.", "options": [
            "Each of the students has completed the task.", "Each of the students have completed the task.",
            "Each of the student has completed the task.", "Each of the students completing the task."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses a conditional (Type 3, past unreal)?", "options": [
            "If she had studied harder, she would have passed.", "If she studied harder, she would have passed.",
            "If she had studied harder, she would pass.", "If she studies harder, she would have passed."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Choose the sentence that correctly avoids a common comma splice error.", "options": [
            "She finished her work; then she went home.", "She finished her work, then she went home.",
            "She finished her work then, she went home.", "She finished her work, then, she went home."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses 'fewer' vs. 'less'?", "options": [
            "There are fewer students in this class.", "There are less students in this class.",
            "There is fewer students in this class.", "There are less student in this class."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Identify the correctly formed passive voice sentence in the past tense.", "options": [
            "The report was submitted yesterday.", "The report submitted yesterday.",
            "The report is submitted yesterday.", "The report was submit yesterday."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses 'who' vs. 'whom'?", "options": [
            "She is the person whom I met yesterday.", "She is the person who I met yesterday to.",
            "She is the person whom met me yesterday.", "Both A and the standard informal usage of 'who' are commonly accepted, but 'whom' is grammatically correct here as the object."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Choose the sentence with the correctly placed only modifier.", "options": [
            "She only ate an apple for lunch.", "Only she ate an apple for lunch, and this changes the meaning compared to the first sentence.",
            "Both sentences above always mean exactly the same thing.", "Neither placement of 'only' changes the sentence's meaning."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the primary purpose of reviewing common grammar mistakes in a doubt-clearing session?", "options": [
            "To reinforce correct usage and address recurring student errors", "To introduce mistakes deliberately for entertainment",
            "To avoid any focus on accuracy", "To replace all prior instruction with new content"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence correctly uses a semicolon to join two independent clauses?", "options": [
            "The exam was difficult; however, she passed.", "The exam was difficult, however she passed.",
            "The exam was difficult: however she passed.", "The exam, was difficult; however she passed."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Identify the sentence with the correctly formed reported (indirect) speech.", "options": [
            "He said that he would come the next day.", "He said that he will come the next day.",
            "He said that he would came the next day.", "He said that he coming the next day."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of these correctly demonstrates subject-verb agreement with a collective noun?", "options": [
            "The team is playing well this season.", "The team are playing well this season, using British usage exclusively without regional variation noted.",
            "The team be playing well this season.", "The team playing well this season."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Choose the sentence that correctly uses an apostrophe for possession.", "options": [
            "The students' books were left on the table.", "The student's books were left on the table, referring to multiple students in this specific context.",
            "The students books were left on the table.", "The students's books were left on the table."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence avoids a common dangling modifier error?", "options": [
            "Having finished the exam, she left the room.", "Having finished the exam, the room was left by her.",
            "The room was left, having finished the exam.", "Having finished the exam, the door was closed by the room."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the correct usage in the sentence: 'Neither the teacher nor the students ___ ready.'?", "options": [
            "were", "was", "is", "be"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Identify the sentence with correct use of a gerund phrase as subject.", "options": [
            "Reading books regularly improves vocabulary.", "To reading books regularly improves vocabulary.",
            "Read books regularly improves vocabulary.", "Reads books regularly improves vocabulary."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly demonstrates the use of a conditional with 'unless'?", "options": [
            "Unless you study, you will fail the exam.", "Unless you will study, you will fail the exam.",
            "Unless you studied, you will fail the exam.", "Unless you don't study, you will fail the exam."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might reviewing frequently confused word pairs (e.g. 'affect'/'effect') be useful in a doubt-clearing session?", "options": [
            "It helps students avoid common errors that persist despite earlier instruction", "Such pairs have no relevance to grammar review",
            "This topic is unrelated to language accuracy", "Confused word pairs should never be addressed directly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of a 'Doubt Clearing Session' chapter in an English course is to:", "options": [
            "Consolidate and reinforce correct grammar and usage through targeted review", "Introduce entirely unrelated new vocabulary with no grammar focus",
            "Avoid addressing any student questions or errors", "Replace grammar instruction with unrelated content"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37536: [  # Critical Thinking
        {"q": "In the context of an English language course, 'critical thinking' skills are typically applied to:", "options": [
            "Analysing and evaluating texts, arguments, and information objectively", "Memorising vocabulary lists with no analysis",
            "Avoiding any evaluation of what is read", "A term unrelated to reading comprehension"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why is identifying an author's bias considered a critical thinking skill in reading comprehension?", "options": [
            "Recognising bias helps readers evaluate whether a text presents information fairly", "Bias has no relevance to reading comprehension",
            "All texts are inherently free of any bias", "This skill is unrelated to critical reading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'evaluating evidence' mean when critically reading a persuasive text?", "options": [
            "Assessing whether the evidence presented actually supports the claims made", "Accepting all stated evidence without question",
            "A term unrelated to critical reading", "Ignoring evidence entirely and reading only for entertainment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might critical thinking exercises ask readers to distinguish fact from opinion in a passage?", "options": [
            "This distinction helps assess a text's objectivity and reliability", "Facts and opinions are always identical",
            "This distinction is irrelevant to reading comprehension", "Opinions are always more reliable than facts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'logical fallacy', a concept often covered in critical thinking units?", "options": [
            "A flaw in reasoning that weakens the validity of an argument", "A term unrelated to argumentation",
            "A synonym for a well-supported argument", "A purely grammatical error"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might critical thinking exercises involve comparing two texts on the same topic?", "options": [
            "Comparison can reveal differing perspectives, biases, or levels of evidence", "Comparing texts has no analytical value",
            "This exercise is unrelated to critical thinking", "Two texts on the same topic always present identical views"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'inference' mean in critical reading?", "options": [
            "A conclusion drawn from evidence and reasoning, not directly stated in the text", "A term unrelated to reading comprehension",
            "A synonym for a directly stated fact", "Guessing with no reference to the text"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is questioning an argument's underlying assumptions considered valuable in critical thinking?", "options": [
            "Unexamined assumptions can weaken or undermine an otherwise reasonable-sounding argument", "Assumptions never need to be examined",
            "This practice is unrelated to critical thinking", "Questioning assumptions always weakens the reader's own understanding"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of asking students to summarise an argument before critiquing it?", "options": [
            "It ensures the argument is fully understood before being evaluated", "Summarising has no role in critical analysis",
            "This step is unrelated to critical thinking exercises", "Critique should always precede understanding"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'objectivity' mean when evaluating a written argument?", "options": [
            "Judging based on evidence and reasoning rather than personal feelings", "A term unrelated to critical analysis",
            "A synonym for emotional reasoning", "The complete absence of any reasoning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might critical thinking be considered essential for evaluating information encountered online?", "options": [
            "Online information varies widely in reliability, making evaluation skills especially important", "Online information requires no evaluation at all",
            "This skill is unrelated to modern reading habits", "All online sources are equally trustworthy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'correlation does not imply causation' mean as a critical thinking principle?", "options": [
            "Two things occurring together does not necessarily mean one causes the other", "Correlation always proves causation",
            "This principle is unrelated to critical reasoning", "Causation is irrelevant when analysing data"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an exercise ask students to identify the strongest and weakest points in an argument?", "options": [
            "It develops the skill of critically weighing the relative merits of different claims", "Identifying strong/weak points has no analytical value",
            "This exercise is unrelated to critical thinking", "All points in an argument are always equally strong"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes reasoning intended to persuade using logic and evidence?", "options": [
            "'Argumentation'", "'Photosynthesis'", "'Trigonometry'", "'Onomatopoeia'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might critical thinking exercises include identifying a writer's purpose (to inform, persuade, entertain)?", "options": [
            "Understanding purpose shapes how a reader should interpret and evaluate the text", "Purpose has no bearing on how a text should be read",
            "This skill is unrelated to critical reading", "All texts share exactly the same purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'counter-argument' mean, and why is considering one a valuable critical thinking skill?", "options": [
            "An opposing viewpoint; considering it can strengthen or refine one's own position", "Counter-arguments have no value in reasoning",
            "This concept is unrelated to critical thinking", "Considering opposing views always weakens an argument"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might critical thinking exercises ask students to identify unsupported generalisations in a text?", "options": [
            "Broad claims without evidence can weaken an argument's credibility", "Generalisations are always well-supported by definition",
            "This skill is unrelated to evaluating written arguments", "Unsupported claims should never be questioned"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'source credibility' mean when critically evaluating a piece of writing?", "options": [
            "The reliability and trustworthiness of where information comes from", "A term unrelated to critical reading",
            "A synonym for a text's length", "All sources are equally credible by default"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is critical thinking considered a transferable skill beyond the English classroom?", "options": [
            "It supports informed decision-making and analysis in many academic and real-world contexts", "Critical thinking has no application outside language study",
            "This skill is unrelated to real-world situations", "Critical thinking is useful only for literary analysis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of a 'Critical Thinking' unit in an English course is to:", "options": [
            "Build the ability to analyse, question, and evaluate texts and arguments rigorously", "Memorise unrelated vocabulary with no analytical purpose",
            "Avoid questioning or evaluating any text", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37537: [  # Idioms and Phrases
        {"q": "What is an 'idiom'?", "options": [
            "A phrase whose meaning cannot be understood from the literal meaning of its individual words", "A phrase whose meaning is always literal",
            "A term unrelated to language study", "A grammatical rule about verb tense"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the idiom 'break the ice' mean?", "options": [
            "To initiate conversation in a social setting to ease tension", "To literally break a piece of ice",
            "To end a friendship abruptly", "To cause a serious problem"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the idiom 'once in a blue moon' mean?", "options": [
            "Very rarely", "Every single day", "Very frequently", "Immediately"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the idiom 'hit the books' mean?", "options": [
            "To study intensively", "To physically strike a book",
            "To sell used books", "To avoid studying entirely"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the phrase 'under the weather' mean?", "options": [
            "Feeling slightly unwell", "Standing outside during rain",
            "Feeling extremely energetic", "Discussing meteorology"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the idiom 'bite the bullet' mean?", "options": [
            "To face a difficult situation with courage", "To literally eat a bullet",
            "To avoid a challenge entirely", "To celebrate a victory"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the idiom 'let the cat out of the bag' mean?", "options": [
            "To accidentally reveal a secret", "To release an actual cat",
            "To keep a secret successfully", "To adopt a new pet"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'a piece of cake' mean when describing a task?", "options": [
            "Something very easy to do", "Something involving actual dessert",
            "Something extremely difficult", "Something related to cooking only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the idiom 'burn the midnight oil' mean?", "options": [
            "To work or study late into the night", "To waste resources carelessly",
            "To finish work early in the morning", "To light a lamp for decoration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'cost an arm and a leg' mean?", "options": [
            "To be very expensive", "To be completely free",
            "To cause physical injury", "To be moderately priced"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the idiom 'the ball is in your court' mean?", "options": [
            "It is now your turn to take action or make a decision", "A literal reference to a sports match",
            "The decision has already been made by someone else", "The matter is permanently unresolved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'beat around the bush' mean?", "options": [
            "To avoid saying something directly", "To speak very directly and bluntly",
            "To literally strike vegetation", "To finish a task quickly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the idiom 'a blessing in disguise' mean?", "options": [
            "Something that seems bad at first but turns out to be beneficial", "Something that is purely bad with no benefit",
            "A literal religious ceremony", "Something entirely unrelated to fortune"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'get cold feet' mean?", "options": [
            "To become nervous or hesitant about doing something", "To literally have cold feet due to weather",
            "To feel extremely confident", "To finish a race successfully"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the idiom 'kill two birds with one stone' mean?", "options": [
            "To accomplish two things with a single action", "To literally harm birds",
            "To fail at two tasks simultaneously", "To focus on only one task at a time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'to add insult to injury' mean?", "options": [
            "To make a bad situation even worse", "To apologise sincerely for a mistake",
            "To improve a difficult situation", "To ignore a problem entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does the idiom 'see eye to eye' mean?", "options": [
            "To agree with someone", "To physically stand at the same height",
            "To strongly disagree with someone", "To avoid eye contact"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is understanding idioms important for advanced English learners?", "options": [
            "Idioms are common in everyday and literary language, and literal translation often fails to convey their meaning", "Idioms have no practical relevance to language learning",
            "This topic is unrelated to reading comprehension", "Idioms are used only in formal academic writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the phrase 'to turn over a new leaf' mean?", "options": [
            "To make a fresh start or change one's behaviour for the better", "To literally flip a leaf from a plant",
            "To repeat the same mistake again", "To end a relationship"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying 'Idioms and Phrases' in an English course is to:", "options": [
            "Build fluency and comprehension of natural, figurative English expressions", "Memorise unrelated vocabulary with no practical application",
            "Avoid using figurative language entirely", "Focus exclusively on unrelated grammar rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37538: [  # Sound System
        {"q": "The study of the 'sound system' of a language is formally known as:", "options": [
            "Phonetics/phonology", "Syntax", "Morphology", "Semantics"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'phoneme'?", "options": [
            "The smallest unit of sound that can distinguish meaning in a language", "A written letter of the alphabet",
            "A complete sentence", "A term unrelated to sound study"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes a 'vowel sound' in English?", "options": [
            "A speech sound produced with an open vocal tract, without significant airflow obstruction", "A sound produced by completely blocking airflow with the lips or tongue",
            "A term unrelated to pronunciation", "A written symbol with no connection to pronunciation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What distinguishes a 'consonant sound' from a vowel sound?", "options": [
            "Consonants typically involve some obstruction or restriction of airflow in the vocal tract", "Consonants involve no articulation at all",
            "There is no meaningful distinction between the two", "Vowels always involve blocked airflow while consonants do not"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'stress' mean in the context of English pronunciation?", "options": [
            "The emphasis placed on a particular syllable in a word", "A term unrelated to pronunciation",
            "A synonym for punctuation", "An emotional state unrelated to sound"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why does word stress matter in spoken English (e.g. 'PRESent' the noun vs. 'preSENT' the verb)?", "options": [
            "Stress placement can change a word's meaning or grammatical function", "Stress placement never affects meaning",
            "This topic is unrelated to pronunciation study", "All English words are stressed identically regardless of context"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is 'intonation' in spoken English?", "options": [
            "The rise and fall of pitch in speech, which can convey meaning or emotion", "A term unrelated to pronunciation",
            "A synonym for vocabulary choice", "A purely written, non-spoken language feature"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might rising intonation typically be used at the end of a yes/no question in English?", "options": [
            "It signals to the listener that a question, rather than a statement, is being asked", "Rising intonation has no functional purpose in speech",
            "This pattern is unrelated to spoken English", "Intonation patterns never vary between questions and statements"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does the International Phonetic Alphabet (IPA) provide?", "options": [
            "A standardised set of symbols to represent the sounds of spoken language precisely", "A grammar system for sentence structure",
            "A term unrelated to pronunciation study", "A vocabulary list of formal words only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is a 'diphthong'?", "options": [
            "A single syllable sound formed by combining two vowel sounds", "A type of consonant cluster only",
            "A term unrelated to phonetics", "A written punctuation mark"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might non-native English learners find certain English sounds (e.g. 'th') particularly challenging?", "options": [
            "Some sounds do not exist in every learner's native language, making them harder to produce accurately", "All learners find every English sound equally easy",
            "This challenge is unrelated to phonetics", "The 'th' sound presents no difficulty for any learner"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'minimal pair' mean in phonetics (e.g. 'ship' vs. 'sheep')?", "options": [
            "Two words differing by only one sound, used to illustrate that sound's role in distinguishing meaning", "A term unrelated to pronunciation study",
            "A synonym for a rhyming pair of words", "Two words with completely different meanings and spellings only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is understanding the sound system important for effective spoken communication?", "options": [
            "Accurate pronunciation helps ensure a speaker is understood clearly by listeners", "Pronunciation has no effect on being understood",
            "This topic is unrelated to communication skills", "Written accuracy alone guarantees clear spoken communication"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'syllable' mean?", "options": [
            "A unit of pronunciation typically consisting of a vowel sound, with or without surrounding consonants", "A term unrelated to pronunciation",
            "A synonym for a complete sentence", "A written punctuation mark"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might mispronunciation of stress patterns lead to miscommunication in English?", "options": [
            "Listeners often rely on stress patterns to identify words and their intended meaning", "Stress patterns have no effect on how words are understood",
            "This topic is unrelated to spoken communication", "All English words are understood identically regardless of stress"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'connected speech' refer to (e.g. sounds blending together in natural speech)?", "options": [
            "The way sounds change or link together in fluent, natural spoken language", "A term unrelated to spoken English",
            "A synonym for written punctuation", "Speech where every word is pronounced in complete isolation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a language course include practice in listening to and identifying different sounds?", "options": [
            "It builds listening comprehension and pronunciation accuracy together", "Listening practice has no connection to pronunciation skills",
            "This activity is unrelated to studying the sound system", "Sound recognition is irrelevant to language learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the difference between 'voiced' and 'voiceless' consonant sounds?", "options": [
            "Voiced sounds involve vibration of the vocal cords, while voiceless sounds do not", "There is no distinction between voiced and voiceless sounds",
            "Voiceless sounds are always louder than voiced sounds", "This distinction applies only to vowels, not consonants"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is the study of a language's sound system relevant even for advanced learners focused on writing?", "options": [
            "Pronunciation awareness can support spelling accuracy and overall language fluency", "Sound system study has no connection to writing skills",
            "This topic is relevant only to beginner learners", "Advanced learners never need to consider pronunciation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying the 'Sound System' in an English course is to:", "options": [
            "Build accurate pronunciation and listening skills alongside language comprehension", "Memorise unrelated vocabulary with no phonetic relevance",
            "Avoid any focus on spoken language", "Focus exclusively on written grammar with no attention to sound"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37539: [  # Punctuation
        {"q": "Which punctuation mark is used to end a declarative sentence?", "options": [
            "A period/full stop (.)", "A question mark (?)", "An exclamation mark (!)", "A semicolon (;)"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence uses a comma correctly to separate items in a list?", "options": [
            "She bought apples, oranges, and bananas.", "She bought apples oranges and bananas.",
            "She bought apples, oranges and, bananas.", "She bought, apples oranges and bananas."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the correct use of an apostrophe in 'the dog's bone'?", "options": [
            "To show possession - the bone belongs to the dog", "To indicate a plural form only",
            "An apostrophe is not needed in this phrase", "To indicate a contraction of two words"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence correctly uses a semicolon?", "options": [
            "She loves reading; he prefers watching movies.", "She loves reading, he prefers watching movies.",
            "She loves reading: he prefers watching movies.", "She loves reading; and he prefers watching movies."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "When is a colon typically used in a sentence?", "options": [
            "To introduce a list, explanation, or quotation", "To separate items in a simple list only",
            "To end every declarative sentence", "A colon is never used in standard English writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses quotation marks?", "options": [
            "She said, \"I will be there soon.\"", "She said, I will be there soon.",
            "She said \"I will be there soon\"", "She said: I will be there soon."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the correct use of a hyphen in compound adjectives (e.g. 'a well-known author')?", "options": [
            "To join two words functioning together as a single adjective before a noun", "Hyphens are never used in compound adjectives",
            "To separate unrelated words with no grammatical function", "To indicate the end of a sentence"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses an em dash for emphasis or interruption?", "options": [
            "She was about to leave — when the phone rang.", "She was about to leave, when the phone rang, using no dash at all in this version.",
            "She was about to leave... when the phone rang, using only ellipsis.", "She was about to leave; when the phone rang."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the correct use of parentheses in a sentence?", "options": [
            "To add extra, non-essential information", "To indicate the main clause of a sentence",
            "To end a question", "Parentheses are never used in formal writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly avoids a comma splice?", "options": [
            "She finished her homework, and then she watched television.", "She finished her homework, then she watched television.",
            "She finished her homework, she watched television.", "She finished her homework then she watched, television."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of an ellipsis (...) in writing?", "options": [
            "To indicate an omission of words or a trailing off of thought", "To end every sentence definitively",
            "To indicate a strong command", "Ellipses are never used in written English"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly punctuates a direct question?", "options": [
            "Where are you going?", "Where are you going.", "Where are you going!", "Where are you going,"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the correct punctuation for joining two independent clauses with a coordinating conjunction?", "options": [
            "She was tired, but she kept working.", "She was tired but, she kept working.",
            "She was tired; but she kept working.", "She was tired but she kept, working."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is correct punctuation important in formal academic or professional writing?", "options": [
            "It ensures clarity and prevents misinterpretation of meaning", "Punctuation has no effect on how writing is understood",
            "Punctuation is only relevant in casual writing", "Formal writing does not require punctuation at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the correct use of a question mark within quotation marks (e.g. reporting a direct question)?", "options": [
            "She asked, \"Are you coming?\"", "She asked, \"Are you coming\"?",
            "She asked \"Are you coming?\".", "She asked, \"Are you coming.\""],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses commas around a non-essential (non-restrictive) clause?", "options": [
            "My brother, who lives in Kathmandu, is visiting us.", "My brother who lives in Kathmandu is visiting us, with no commas at all.",
            "My brother, who lives in Kathmandu is visiting us.", "My brother who, lives in Kathmandu, is visiting us."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of a capital letter at the start of a proper noun?", "options": [
            "To indicate the word refers to a specific, named person, place, or thing", "Capital letters have no grammatical function",
            "To indicate the end of a sentence", "To indicate a question is being asked"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence correctly punctuates an exclamatory statement?", "options": [
            "What a beautiful sunset!", "What a beautiful sunset.", "What a beautiful sunset?", "What a beautiful sunset,"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might incorrect comma placement change the meaning of a sentence?", "options": [
            "Commas can affect how phrases and clauses are grouped, altering interpretation", "Comma placement never affects meaning",
            "This topic is unrelated to sentence clarity", "All comma placements produce identical meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Punctuation' in an English course is to:", "options": [
            "Build accuracy and clarity in written communication", "Memorise unrelated vocabulary with no grammatical relevance",
            "Avoid using punctuation in writing", "Focus exclusively on spoken language with no attention to writing"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37540: [  # Dictionary Use
        {"q": "What is the primary purpose of a dictionary?", "options": [
            "To provide definitions, pronunciations, and usage information for words", "To provide only a list of synonyms with no definitions",
            "To replace the need for grammar study entirely", "To provide historical dates unrelated to language"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In a dictionary entry, what does the phonetic transcription (often in brackets) typically indicate?", "options": [
            "How the word is pronounced", "The word's grammatical category only",
            "A list of synonyms", "The word's historical origin only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does the abbreviation 'n.' typically indicate in a dictionary entry?", "options": [
            "The word is a noun", "The word is a verb", "The word is an adjective", "The word is an adverb"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does 'etymology' refer to in a dictionary entry?", "options": [
            "The historical origin and development of a word", "The word's current pronunciation only",
            "A term unrelated to dictionaries", "A list of the word's synonyms"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a dictionary entry list multiple definitions for a single word?", "options": [
            "Many words have multiple meanings depending on context", "Every word has only ever one single meaning",
            "This practice is unrelated to how dictionaries are structured", "Multiple definitions indicate an error in the dictionary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'thesaurus' typically used for, as distinct from a dictionary?", "options": [
            "Finding synonyms and antonyms for a word", "Finding the phonetic pronunciation of a word only",
            "A term unrelated to vocabulary resources", "Finding a word's grammatical origin only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is understanding dictionary abbreviations (e.g. 'v.', 'adj.', 'prep.') useful?", "options": [
            "It helps readers quickly identify a word's grammatical function", "Such abbreviations have no practical use",
            "This skill is unrelated to dictionary use", "Abbreviations are used only in outdated dictionaries"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does an example sentence in a dictionary entry typically demonstrate?", "options": [
            "How the word is used in context", "The word's pronunciation only",
            "The word's historical origin only", "A list of unrelated vocabulary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a dictionary indicate whether a word is 'formal' or 'informal'?", "options": [
            "To help users choose appropriate vocabulary for different contexts", "Formality has no relevance to word choice",
            "This distinction is unrelated to dictionary entries", "All words are considered equally formal in every context"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of guide words at the top of a printed dictionary page?", "options": [
            "To indicate the first and last entries on that page, aiding quick navigation", "To provide a summary of the entire dictionary",
            "A term unrelated to dictionary structure", "To indicate the dictionary's publication date"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a learner consult a dictionary while reading an unfamiliar text?", "options": [
            "To clarify the meaning of unknown words and improve comprehension", "Dictionaries have no role in reading comprehension",
            "This practice is unrelated to vocabulary development", "Consulting a dictionary while reading is discouraged"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does 'synonym' mean, a concept often included in dictionary entries?", "options": [
            "A word with a similar meaning to another word", "A word with the opposite meaning of another word",
            "A term unrelated to vocabulary", "A grammatical rule about sentence structure"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does 'antonym' mean?", "options": [
            "A word with the opposite meaning of another word", "A word with a similar meaning to another word",
            "A term unrelated to vocabulary", "A synonym for pronunciation"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might online/digital dictionaries include audio pronunciation alongside phonetic transcription?", "options": [
            "Audio can help learners hear accurate pronunciation directly, complementing phonetic symbols", "Audio pronunciation has no added value over written transcription",
            "This feature is unrelated to dictionary use", "Digital dictionaries never include audio features"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'bilingual dictionary'?", "options": [
            "A dictionary that translates words between two languages", "A dictionary containing only synonyms",
            "A term unrelated to dictionary types", "A dictionary limited to a single specific field of study"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might understanding a word's part of speech (from a dictionary entry) help with correct sentence construction?", "options": [
            "Knowing whether a word is a noun, verb, etc. helps use it grammatically correctly in a sentence", "Part of speech has no bearing on sentence construction",
            "This information is unrelated to using a dictionary effectively", "All words function identically regardless of part of speech"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does a dictionary's 'usage note' typically clarify?", "options": [
            "Special considerations about how or when a word is appropriately used", "The word's phonetic pronunciation only",
            "A term unrelated to dictionary entries", "The word's historical origin only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is dictionary skill considered valuable for independent vocabulary building?", "options": [
            "It allows learners to look up and understand new words on their own, beyond classroom instruction", "Dictionary skills have no connection to independent learning",
            "This skill is unrelated to vocabulary development", "Learners should never look up words independently"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'idiomatic usage', sometimes noted in dictionary entries, refer to?", "options": [
            "A word or phrase's figurative meaning distinct from its literal definition", "A term unrelated to dictionary entries",
            "A synonym for a word's grammatical category", "The word's pronunciation only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Dictionary Use' in an English course is to:", "options": [
            "Build practical reference skills for vocabulary, pronunciation, and usage", "Memorise the entire contents of a dictionary",
            "Avoid using reference tools while reading or writing", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37541: [  # Parts of Speech
        {"q": "How many traditional parts of speech are commonly recognised in English grammar?", "options": [
            "Eight", "Three", "Twelve", "Five"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is the word 'quickly' in the sentence 'She ran quickly'?", "options": [
            "Adverb", "Noun", "Adjective", "Preposition"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is the word 'beautiful' in the sentence 'She has a beautiful garden'?", "options": [
            "Adjective", "Verb", "Adverb", "Conjunction"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is 'and' in the sentence 'She likes tea and coffee'?", "options": [
            "Conjunction", "Preposition", "Interjection", "Pronoun"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is 'under' in the sentence 'The cat is under the table'?", "options": [
            "Preposition", "Adverb", "Noun", "Verb"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is 'she' in the sentence 'She went to the market'?", "options": [
            "Pronoun", "Noun", "Adjective", "Conjunction"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech is used to express strong emotion, such as 'Wow!'?", "options": [
            "Interjection", "Preposition", "Conjunction", "Article"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the sentence 'The dog barked loudly,' which word is the verb?", "options": [
            "Barked", "Dog", "Loudly", "The"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What part of speech are 'a', 'an', and 'the' classified as?", "options": [
            "Articles (a type of determiner)", "Verbs", "Adverbs", "Conjunctions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which part of speech typically functions as the subject or object of a sentence?", "options": [
            "Noun", "Preposition", "Conjunction", "Interjection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What part of speech is 'run' in the sentence 'He likes to run every morning'?", "options": [
            "Verb (infinitive form)", "Noun", "Adjective", "Preposition"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is understanding parts of speech considered foundational to grammar study?", "options": [
            "It helps identify how each word functions within a sentence's structure", "Parts of speech have no connection to sentence structure",
            "This topic is unrelated to grammar", "Parts of speech are relevant only to advanced linguistics, not general grammar"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which part of speech can a single word sometimes belong to depending on context (e.g. 'run' as noun or verb)?", "options": [
            "Many English words can function as different parts of speech depending on how they are used", "Every English word belongs to exactly one fixed part of speech with no exceptions",
            "This flexibility is unrelated to English grammar", "Only nouns can ever change part of speech"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What part of speech is 'happily' in the sentence 'They happily agreed to help'?", "options": [
            "Adverb", "Adjective", "Noun", "Preposition"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In the sentence 'Books are important,' which word functions as the noun?", "options": [
            "Books", "Are", "Important", "The sentence contains no noun"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the function of a conjunction in a sentence?", "options": [
            "To connect words, phrases, or clauses", "To describe a noun's qualities",
            "To indicate a strong emotion", "To show possession"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What part of speech is 'this' in the sentence 'This is my book'?", "options": [
            "Pronoun (demonstrative)", "Adjective", "Adverb", "Preposition"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might identifying the part of speech of an unfamiliar word help a reader infer its meaning?", "options": [
            "Knowing a word's grammatical role can provide context clues about its likely function and meaning", "Part of speech has no connection to inferring word meaning",
            "This strategy is unrelated to vocabulary building", "Only a dictionary, never grammatical context, can reveal a word's meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What part of speech is 'very' in the sentence 'She is very talented'?", "options": [
            "Adverb (intensifier)", "Adjective", "Noun", "Conjunction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying 'Parts of Speech' in an English course is to:", "options": [
            "Build a foundational understanding of how words function grammatically within sentences", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid analysing sentence structure entirely", "Focus exclusively on spoken pronunciation with no attention to grammar"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37542: [  # Adjectives and Adverbs
        {"q": "What is the primary function of an adjective?", "options": [
            "To describe or modify a noun or pronoun", "To describe or modify a verb, adjective, or another adverb",
            "To connect two clauses", "To indicate a strong emotion"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the primary function of an adverb?", "options": [
            "To modify a verb, adjective, or another adverb", "To modify a noun exclusively",
            "To function only as the subject of a sentence", "To indicate possession"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Identify the adjective in the sentence: 'She wore a red dress.'", "options": [
            "Red", "Wore", "Dress", "She"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Identify the adverb in the sentence: 'He spoke softly.'", "options": [
            "Softly", "Spoke", "He", "None of the words is an adverb"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is the correct comparative form of 'good'?", "options": [
            "Better", "Gooder", "More good", "Goodest"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is the correct superlative form of 'bad'?", "options": [
            "Worst", "Baddest", "More bad", "Most bad"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses a comparative adjective?", "options": [
            "This book is more interesting than that one.", "This book is more interestinger than that one.",
            "This book is interestinger than that one.", "This book is most interesting than that one."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the difference between 'good' and 'well' in standard English usage?", "options": [
            "'Good' is typically an adjective, while 'well' is typically an adverb", "There is no meaningful difference between the two",
            "'Well' is always an adjective and 'good' is always an adverb", "Both words are always interchangeable in every context"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly places the adjective before the noun it modifies?", "options": [
            "She has a beautiful house.", "She has a house beautiful.",
            "She has beautiful a house.", "Beautiful she has a house."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does 'demonstrative adjective' mean (e.g. 'this', 'that' when modifying a noun)?", "options": [
            "An adjective that points out or specifies which particular noun is meant", "A term unrelated to adjectives",
            "An adjective describing a noun's quality only", "A synonym for a comparative adjective"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses an adverb of frequency?", "options": [
            "She always arrives on time.", "She arrives always on time.",
            "Always she arrives on time.", "She arrives on time always is unclear phrasing."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'adverb of manner' mean (e.g. 'quickly', 'carefully')?", "options": [
            "An adverb describing how an action is performed", "An adverb describing when an action occurs",
            "An adverb describing where an action occurs", "A term unrelated to adverbs"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses an adverb of place?", "options": [
            "The children played outside.", "The children played outside is grammatically incorrect in this form.",
            "Outside the children is playing.", "The children outside played is grammatically reversed incorrectly."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the correct order when multiple adjectives modify the same noun (e.g. size before colour)?", "options": [
            "A small, red car (typically follows a general convention of opinion, size, then colour, etc.)", "A red, small car is always the only correct order",
            "Adjective order never follows any convention in English", "Adjectives must always be listed alphabetically"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses an adverb to modify an adjective?", "options": [
            "She is extremely talented.", "She is talented extremely is an unusual word order.",
            "She extremely is talented is grammatically incorrect.", "Extremely she is talented is grammatically incorrect."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'participial adjective' mean (e.g. 'interesting' vs. 'interested')?", "options": [
            "An adjective formed from a verb's participle form, often distinguishing an active vs. passive sense", "A term unrelated to adjectives",
            "A synonym for a comparative adjective", "An adjective that can never be derived from a verb"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of these correctly demonstrates the distinction between 'interesting' and 'interested'?", "options": [
            "The lecture was interesting, and the students were interested.", "The lecture was interested, and the students were interesting.",
            "Both words are always fully interchangeable in every context.", "Neither word can ever function as an adjective."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'adverb of degree' mean (e.g. 'very', 'quite', 'too')?", "options": [
            "An adverb indicating the intensity or extent of an adjective, verb, or another adverb", "An adverb describing location only",
            "A term unrelated to adverbs", "An adverb describing time only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is correct use of adjectives and adverbs important for clear, precise writing?", "options": [
            "They add necessary descriptive detail and can significantly affect a sentence's meaning and tone", "Adjectives and adverbs have no effect on writing clarity",
            "This topic is unrelated to effective writing", "Removing all adjectives and adverbs always improves writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying 'Adjectives and Adverbs' in an English course is to:", "options": [
            "Build precision and descriptive skill in both spoken and written English", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid using descriptive language in writing", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37543: [  # Prepositions
        {"q": "What is the primary function of a preposition?", "options": [
            "To show the relationship between a noun/pronoun and other words in a sentence", "To describe a noun's qualities directly",
            "To connect two independent clauses", "To indicate strong emotion"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Identify the preposition in the sentence: 'The book is on the table.'", "options": [
            "On", "Book", "Table", "Is"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which preposition correctly completes: 'She is interested ___ music.'?", "options": [
            "in", "on", "at", "for"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which preposition correctly completes: 'The meeting is scheduled ___ 5 p.m.'?", "options": [
            "at", "in", "on", "by"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'He arrived ___ Kathmandu yesterday.'?", "options": [
            "in", "at", "on", "to"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'She is good ___ mathematics.'?", "options": [
            "at", "in", "on", "for"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'prepositional phrase'?", "options": [
            "A group of words beginning with a preposition and ending with its object", "A complete independent clause",
            "A term unrelated to prepositions", "A phrase that always functions as the main verb"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'The cat jumped ___ the wall.'?", "options": [
            "over", "in", "under is only correct if describing going beneath, not jumping across", "at"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a preposition of time?", "options": [
            "During", "Under", "Beside", "Through"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'We will meet ___ the library.'?", "options": [
            "at", "on", "in front is incomplete without 'of' in this option's form", "to"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the difference between 'in' and 'on' when referring to locations?", "options": [
            "'In' is typically used for enclosed spaces, while 'on' is used for surfaces", "There is no meaningful difference between the two",
            "'On' is always used for enclosed spaces and 'in' for surfaces", "Both prepositions are always fully interchangeable"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which preposition correctly completes: 'She apologised ___ being late.'?", "options": [
            "for", "of", "at", "to"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'The gift was given ___ the whole family.'?", "options": [
            "to", "for", "at", "by"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'preposition of movement' mean (e.g. 'into', 'through', 'across')?", "options": [
            "A preposition indicating motion from one place to another", "A preposition indicating a fixed, static location only",
            "A term unrelated to prepositions", "A preposition used only with time expressions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which preposition correctly completes: 'He has been working here ___ 2019.'?", "options": [
            "since", "for", "from", "at"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which preposition correctly completes: 'They travelled ___ car to the village.'?", "options": [
            "by", "in", "on", "with"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why do prepositions often need to be memorised through common phrase usage rather than strict rules?", "options": [
            "Preposition usage in English is often idiomatic and does not always follow predictable logical rules", "Prepositions always follow completely consistent, predictable rules",
            "This challenge is unrelated to learning English grammar", "Prepositions are the easiest part of English grammar to master through rules alone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which preposition correctly completes: 'The book was written ___ a famous author.'?", "options": [
            "by", "from", "with", "of"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is correct preposition usage important for fluent, natural-sounding English?", "options": [
            "Incorrect prepositions can make sentences sound unnatural or unclear to native speakers", "Preposition choice has no effect on how natural writing sounds",
            "This topic is unrelated to fluency", "Any preposition can be substituted for another with no change in meaning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying 'Prepositions' in an English course is to:", "options": [
            "Build accuracy in expressing relationships of time, place, and manner in sentences", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid using prepositions in writing", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37544: [  # Conjunctions/ Connectives
        {"q": "What is the primary function of a conjunction?", "options": [
            "To connect words, phrases, or clauses", "To describe a noun's qualities",
            "To indicate the relationship between a noun and other words", "To express strong emotion"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is a coordinating conjunction?", "options": [
            "And", "Although", "Because", "Since"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is a subordinating conjunction?", "options": [
            "Because", "And", "Or", "But"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses a coordinating conjunction to join two independent clauses?", "options": [
            "She was tired, but she kept working.", "She was tired but she kept, working.",
            "She was tired, but, she kept working.", "She was, tired but she kept working."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses a subordinating conjunction?", "options": [
            "Although it was raining, they went outside.", "Although it raining, they went outside.",
            "It was raining although, they went outside.", "They went outside, although it raining."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'connective' mean, a term often used alongside 'conjunction' in language study?", "options": [
            "A word or phrase linking ideas together, showing logical relationships between them", "A term unrelated to sentence structure",
            "A synonym for a noun", "A word used only to end sentences"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which conjunction correctly completes: 'She studied hard, ___ she passed the exam.'?", "options": [
            "so", "although", "unless", "whereas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which conjunction correctly completes: 'You will fail ___ you study.'?", "options": [
            "unless", "so", "and", "or"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'correlative conjunction' mean (e.g. 'either...or', 'neither...nor')?", "options": [
            "A pair of conjunctions that work together to join balanced sentence elements", "A term unrelated to conjunctions",
            "A synonym for a single coordinating conjunction", "A conjunction used only at the start of a sentence"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses a correlative conjunction?", "options": [
            "Neither the manager nor the employees were satisfied.", "Neither the manager or the employees were satisfied.",
            "Either the manager nor the employees were satisfied.", "Neither the manager, nor the employees, were satisfied is punctuated unusually."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of a connective like 'however' in linking ideas across sentences?", "options": [
            "To show contrast between the previous idea and the one that follows", "To show that two ideas are identical",
            "A term unrelated to logical connection", "To indicate the end of a paragraph with no other function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which connective correctly shows a cause-and-effect relationship?", "options": [
            "Therefore", "However", "Meanwhile", "Similarly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which connective correctly shows addition of a similar idea?", "options": [
            "Furthermore", "However", "Nevertheless", "Whereas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses 'while' as a subordinating conjunction of contrast?", "options": [
            "While he enjoys sports, his brother prefers reading.", "While he enjoys sports his brother, prefers reading.",
            "He enjoys sports, while, his brother prefers reading.", "His brother prefers reading while, he enjoys sports is punctuated unusually."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why are connectives important for coherence in extended writing (e.g. essays)?", "options": [
            "They help link ideas logically across sentences and paragraphs, improving flow", "Connectives have no effect on writing coherence",
            "This topic is unrelated to essay writing", "Removing all connectives always improves clarity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which conjunction correctly completes: 'He was late ___ the heavy traffic.'?", "options": [
            "because of", "although", "unless", "so that"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'so that' typically express when used as a connective?", "options": [
            "Purpose or intended result", "Contrast between two ideas",
            "A term unrelated to logical connection", "A simple list of unrelated items"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses 'whereas' to show contrast between two clauses?", "options": [
            "She likes tea, whereas he prefers coffee.", "She likes tea whereas, he prefers coffee.",
            "Whereas, she likes tea he prefers coffee.", "She likes tea, whereas he prefer coffee."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might overusing the conjunction 'and' throughout a piece of writing weaken its style?", "options": [
            "It can make sentence relationships (cause, contrast, sequence) less precise than more specific connectives", "Overusing 'and' always improves writing clarity",
            "This topic is unrelated to effective writing style", "'And' is the only conjunction that should ever be used in formal writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Conjunctions/Connectives' in an English course is to:", "options": [
            "Build skill in logically linking ideas within and across sentences", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid connecting ideas in writing", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37545: [  # Reported Speech
        {"q": "What is 'reported speech' (also called indirect speech)?", "options": [
            "Reporting what someone said without quoting their exact words", "Quoting someone's exact words directly, in quotation marks",
            "A term unrelated to grammar", "A style used only in formal legal writing"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Convert to reported speech: He said, \"I am tired.\"", "options": [
            "He said that he was tired.", "He said that he is tired.",
            "He said that I am tired.", "He said that he tired."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Convert to reported speech: She said, \"I will call you tomorrow.\"", "options": [
            "She said that she would call me the next day.", "She said that she will call me tomorrow.",
            "She said that she would call me tomorrow exactly as spoken with no tense change.", "She said that she call me the next day."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: He said, \"I have finished my homework.\"", "options": [
            "He said that he had finished his homework.", "He said that he has finished his homework.",
            "He said that he finished his homework is missing the correct backshift.", "He said that he have finished his homework."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is 'backshift' in reported speech?", "options": [
            "Shifting the tense of the reported clause one step back into the past", "Keeping the exact same tense as the original statement always",
            "A term unrelated to reported speech", "Changing only pronouns with no change to verb tense"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: She asked, \"Where do you live?\"", "options": [
            "She asked where I lived.", "She asked where do I live.",
            "She asked where I live is missing correct tense backshift.", "She asked where you live."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "How is a yes/no question typically converted to reported speech?", "options": [
            "Using 'if' or 'whether' to introduce the reported clause", "Using 'that' to introduce the reported clause",
            "Keeping the question mark and exact word order", "A term unrelated to reported speech"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: He asked, \"Did you finish the report?\"", "options": [
            "He asked if I had finished the report.", "He asked did I finish the report.",
            "He asked that I finish the report.", "He asked I had finished the report is missing 'if'."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "How is an imperative (command) typically converted to reported speech?", "options": [
            "Using an infinitive verb form, often introduced by 'told... to'", "Keeping the exact command form with no change",
            "A term unrelated to reported speech", "Always converting it into a question"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: The teacher said, \"Close the door.\"", "options": [
            "The teacher told them to close the door.", "The teacher said close the door.",
            "The teacher said that close the door.", "The teacher told close the door is grammatically incomplete."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why do pronouns often need to change when converting direct speech to reported speech?", "options": [
            "The speaker's perspective is being reported by someone else, requiring pronoun adjustment", "Pronouns never need to change in reported speech",
            "This topic is unrelated to reported speech", "Only proper nouns need to change, never pronouns"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Convert to reported speech: 'This is my book,' she said.", "options": [
            "She said that was her book.", "She said that this is my book.",
            "She said that this was her book is also acceptable in many treatments.", "She said this is her book is missing correct backshift."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "How does the time expression 'tomorrow' typically change in reported speech?", "options": [
            "It typically becomes 'the next day' or 'the following day'", "It always remains exactly 'tomorrow' with no change",
            "It becomes 'yesterday'", "Time expressions never change in reported speech"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: \"I saw her yesterday,\" he said.", "options": [
            "He said that he had seen her the day before.", "He said that he saw her yesterday with no change.",
            "He said that he sees her yesterday.", "He said that he will see her yesterday."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might modal verbs (e.g. 'can', 'may') also shift in reported speech (e.g. 'can' to 'could')?", "options": [
            "Certain modal verbs follow the same backshift pattern as other verb tenses", "Modal verbs never change form in reported speech",
            "This topic is unrelated to reported speech rules", "Modal verbs are the only words that never change in any grammatical transformation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to reported speech: \"I can help you,\" she said.", "options": [
            "She said that she could help me.", "She said that she can help me with no change.",
            "She said that she could help you.", "She said that she cans help me."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is understanding reported speech especially useful for writing narratives or reports?", "options": [
            "It allows writers to summarise or convey what someone said without direct quotation", "Reported speech has no practical writing application",
            "This topic is unrelated to narrative or report writing", "Direct quotation is always preferred over reported speech in every context"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which reporting verb might replace 'said' to add more nuance (e.g. for a command)?", "options": [
            "'Ordered' or 'told'", "'Asked' is used only for statements, never commands",
            "A term unrelated to reported speech", "Reporting verbs never vary; only 'said' can be used"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Convert to reported speech: \"Please help me,\" she requested.", "options": [
            "She requested him to help her.", "She requested that please help her.",
            "She requested please help me.", "She requested to help her is grammatically incomplete."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Reported Speech' in an English course is to:", "options": [
            "Build accuracy in conveying others' statements, questions, and commands indirectly", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid ever reporting what someone else said", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37546: [  # Voice
        {"q": "What is the difference between 'active voice' and 'passive voice'?", "options": [
            "In active voice the subject performs the action; in passive voice the subject receives the action", "There is no meaningful difference between the two",
            "Passive voice always uses the present tense only", "Active voice is used only in questions"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Convert to passive voice: 'She wrote the letter.'", "options": [
            "The letter was written by her.", "The letter is written by her.",
            "The letter wrote by her.", "The letter written by her."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Convert to passive voice: 'They are building a new school.'", "options": [
            "A new school is being built by them.", "A new school was being built by them.",
            "A new school is build by them.", "A new school being built by them."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'He has completed the project.'", "options": [
            "The project has been completed by him.", "The project has completed by him.",
            "The project is completed by him.", "The project had been completed by him is a different tense."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence is written in active voice?", "options": [
            "The chef cooked the meal.", "The meal was cooked by the chef.",
            "The meal is cooked.", "The meal has been cooked."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence is written in passive voice?", "options": [
            "The award was given to her.", "She received the award.",
            "They gave her the award.", "She was given the award and she accepted it actively, blending both voices confusingly."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might passive voice be used when the performer of an action is unknown or unimportant?", "options": [
            "It allows the focus to remain on the action or the object receiving it, rather than the doer", "Passive voice always requires naming the performer explicitly",
            "This use is unrelated to passive voice construction", "Passive voice can never be used when the doer is unknown"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'The company will launch a new product.'", "options": [
            "A new product will be launched by the company.", "A new product will launch by the company.",
            "A new product is launched by the company.", "A new product was launched by the company is a different tense."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is active voice often preferred in clear, direct writing (e.g. journalism)?", "options": [
            "It is generally more concise and directly identifies who performs the action", "Active voice is always grammatically incorrect in formal writing",
            "This preference is unrelated to writing style", "Passive voice is always clearer than active voice in every context"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'Someone stole my bicycle.'", "options": [
            "My bicycle was stolen.", "My bicycle stole.",
            "My bicycle is stolen by someone with present tense incorrectly applied.", "My bicycle has stole."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might passive voice be commonly used in scientific or academic writing?", "options": [
            "It can emphasise the process or result rather than who performed the action", "Passive voice is never used in scientific writing",
            "This use is unrelated to academic writing conventions", "Scientific writing always avoids passive voice entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'The teacher explains the lesson every day.'", "options": [
            "The lesson is explained by the teacher every day.", "The lesson explains by the teacher every day.",
            "The lesson was explained by the teacher every day is a different tense.", "The lesson explaining by the teacher every day."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the passive voice structure typically composed of?", "options": [
            "A form of 'be' plus the past participle of the main verb", "The main verb alone with no auxiliary",
            "A term unrelated to voice construction", "Only the present participle form of the verb"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Convert to passive voice: 'People speak English all over the world.'", "options": [
            "English is spoken all over the world.", "English speaks all over the world.",
            "English was spoken all over the world is a different tense.", "English speaking all over the world."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might overusing passive voice make writing feel less direct or engaging?", "options": [
            "It can obscure who is responsible for an action and add unnecessary wordiness", "Passive voice always makes writing more engaging",
            "This effect is unrelated to writing style", "Passive voice has no impact on how direct writing feels"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'The government has passed a new law.'", "options": [
            "A new law has been passed by the government.", "A new law has passed by the government.",
            "A new law is passed by the government is a different tense.", "A new law passed by the government."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following sentence types cannot typically be converted to passive voice?", "options": [
            "A sentence with an intransitive verb (no direct object), such as 'She slept.'", "A sentence with a transitive verb and clear object",
            "A term unrelated to active/passive voice", "Every sentence type can always be converted to passive voice"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Convert to passive voice: 'They will announce the results tomorrow.'", "options": [
            "The results will be announced tomorrow.", "The results will announce tomorrow.",
            "The results are announced tomorrow is a different tense.", "The results announced tomorrow."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is understanding both active and passive voice useful for varied, effective writing?", "options": [
            "It allows writers to choose the structure that best fits their intended emphasis and clarity", "Only one voice is ever grammatically correct in English",
            "This topic is unrelated to writing skill development", "Passive voice should never be used under any circumstances"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of studying 'Voice' in an English course is to:", "options": [
            "Build flexibility and precision in choosing active or passive sentence structures", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid using passive voice under any circumstances", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37547: [  # Tense and Aspects
        {"q": "How many main tenses (past, present, future) are commonly recognised in English?", "options": [
            "Three", "Two", "Five", "Twelve"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence is written in the simple present tense?", "options": [
            "She walks to school every day.", "She walked to school yesterday.",
            "She will walk to school tomorrow.", "She has walked to school."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence is written in the present continuous (progressive) aspect?", "options": [
            "She is walking to school now.", "She walks to school every day.",
            "She has walked to school.", "She walked to school."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'aspect' refer to in English grammar, as distinct from 'tense'?", "options": [
            "Whether an action is complete, ongoing, or habitual, rather than simply when it occurs", "A synonym for tense with no distinction",
            "A term unrelated to verb forms", "Only whether a sentence is a question or statement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses the present perfect aspect?", "options": [
            "She has finished her homework.", "She finished her homework.",
            "She finishes her homework.", "She is finishing her homework."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses the present perfect continuous aspect?", "options": [
            "She has been studying for three hours.", "She has studied for three hours.",
            "She studies for three hours.", "She is studying for three hours."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence is written in the simple past tense?", "options": [
            "He visited his grandmother last week.", "He visits his grandmother every week.",
            "He will visit his grandmother next week.", "He has visited his grandmother."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which sentence correctly uses the past continuous aspect?", "options": [
            "She was reading when the phone rang.", "She read when the phone rang.",
            "She has read when the phone rang.", "She reads when the phone rang."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses the past perfect aspect?", "options": [
            "She had left before he arrived.", "She left before he arrived.",
            "She has left before he arrived.", "She was leaving before he arrived."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses the future continuous aspect?", "options": [
            "She will be traveling next week.", "She will travel next week.",
            "She travels next week.", "She has been traveling next week."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly uses the future perfect aspect?", "options": [
            "By next year, she will have graduated.", "By next year, she will graduate.",
            "By next year, she graduates.", "By next year, she has graduated."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why does English use the present perfect (rather than simple past) to describe an action with present relevance?", "options": [
            "It connects a past action to its ongoing or current relevance to the present moment", "There is no functional difference between the two forms",
            "This distinction is unrelated to tense/aspect study", "The present perfect is used only for future events"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence best illustrates the use of the simple present tense for a habitual action?", "options": [
            "She drinks coffee every morning.", "She is drinking coffee right now.",
            "She drank coffee this morning.", "She will drink coffee tomorrow."],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is correct tense/aspect usage important when narrating a sequence of past events?", "options": [
            "It helps clarify the order and relationship between events in time", "Tense/aspect has no effect on how a narrative is understood",
            "This topic is unrelated to narrative writing", "Any tense can be used interchangeably with no effect on meaning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly combines past perfect with simple past to show sequence?", "options": [
            "After she had finished dinner, she went for a walk.", "After she finished dinner, she had gone for a walk in reversed sequence.",
            "After she has finished dinner, she went for a walk.", "After she finishing dinner, she went for a walk."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'progressive/continuous aspect' generally emphasise about an action?", "options": [
            "That the action is ongoing or in progress at a particular point in time", "That the action is fully completed with no ongoing element",
            "A term unrelated to verb aspect", "That the action will never occur"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which sentence correctly uses the simple future tense?", "options": [
            "She will call you tomorrow.", "She calls you tomorrow.",
            "She is calling you tomorrow with different implied meaning of a scheduled plan.", "She called you tomorrow."],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a writer choose present continuous over simple present to describe a temporary situation?", "options": [
            "Present continuous often conveys a temporary or currently ongoing state, unlike the more permanent-sounding simple present", "There is no distinction in meaning between these two forms",
            "This choice is unrelated to tense/aspect nuance", "Present continuous is used only for future scheduled events"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which sentence correctly demonstrates the perfect continuous aspect in the past?", "options": [
            "She had been working there for five years before she resigned.", "She had worked there for five years before she resigned with no continuous aspect.",
            "She has been working there for five years before she resigned with incorrect tense.", "She was working there for five years before she resigned."],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Tense and Aspects' in an English course is to:", "options": [
            "Build precise control over expressing time and the nature of actions in sentences", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid using any verb tense consistently", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37548: [  # Question Tag
        {"q": "What is a 'question tag'?", "options": [
            "A short phrase added to the end of a statement to turn it into a question", "A term unrelated to sentence structure",
            "A synonym for a full independent question", "A punctuation mark used only in formal writing"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which question tag correctly completes: 'She is coming, ___?'", "options": [
            "isn't she", "is she", "doesn't she", "isn't it"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which question tag correctly completes: 'They don't like coffee, ___?'", "options": [
            "do they", "don't they", "are they", "will they"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'You can swim, ___?'", "options": [
            "can't you", "can you", "couldn't you", "won't you"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the general rule for forming a question tag after a positive (affirmative) statement?", "options": [
            "Use a negative tag", "Use another positive tag",
            "A term unrelated to question tag formation", "Always use 'isn't it' regardless of the main verb"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the general rule for forming a question tag after a negative statement?", "options": [
            "Use a positive tag", "Use another negative tag",
            "A term unrelated to question tag formation", "No tag can be used after a negative statement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'He has finished his work, ___?'", "options": [
            "hasn't he", "doesn't he", "isn't he", "won't he"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which question tag correctly completes: 'Let's go to the market, ___?'", "options": [
            "shall we", "will we", "don't we", "aren't we"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which question tag correctly completes: 'I am right, ___?'", "options": [
            "aren't I", "am I not exactly, though this is a more formal variant", "isn't I", "amn't I is nonstandard"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which question tag correctly completes: 'Nobody called, ___?'", "options": [
            "did they", "didn't they", "did he", "does he"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a question tag be used in spoken English to seek confirmation or agreement?", "options": [
            "It invites the listener to confirm or respond to the speaker's statement", "Question tags have no communicative function",
            "This use is unrelated to spoken English", "Question tags are used only in written academic English"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'You won't forget, ___?'", "options": [
            "will you", "won't you", "don't you", "do you"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why does rising or falling intonation on a question tag matter in spoken English?", "options": [
            "Rising intonation often signals genuine uncertainty, while falling intonation often signals seeking agreement", "Intonation on a question tag has no communicative meaning",
            "This topic is unrelated to question tags", "All question tags are always spoken with identical intonation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which question tag correctly completes: 'She never lies, ___?'", "options": [
            "does she", "doesn't she", "is she", "isn't she"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which question tag correctly completes: 'We should leave now, ___?'", "options": [
            "shouldn't we", "should we", "shall we is an alternative but less standard here", "wouldn't we"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'This is your book, ___?'", "options": [
            "isn't it", "is it", "doesn't it", "isn't this"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might question tags be especially important to master for natural-sounding conversational English?", "options": [
            "They are a very common feature of everyday spoken English used to engage a listener", "Question tags are rarely used in spoken English",
            "This topic is unrelated to conversational fluency", "Question tags are used only in formal, written English"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'He can't drive, ___?'", "options": [
            "can he", "can't he", "does he", "doesn't he"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which question tag correctly completes: 'Everyone enjoyed the party, ___?'", "options": [
            "didn't they", "did they", "didn't it", "weren't they"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The overall purpose of studying 'Question Tag' in an English course is to:", "options": [
            "Build fluency in a common, natural feature of spoken English used to confirm or invite agreement", "Memorise unrelated vocabulary with no grammatical purpose",
            "Avoid using tag questions in conversation", "Focus exclusively on unrelated punctuation rules"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37549: [  # Writing Task: 1
        {"q": "A 'Writing Task 1' unit in an exam-oriented English course typically focuses on which kind of writing?", "options": [
            "A shorter, more structured writing task (e.g. a formal letter or a short descriptive/report piece)", "An extended novel-length work of fiction",
            "A term unrelated to writing skill assessment", "A purely spoken presentation with no written component"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the typical structure of a formal letter, a common Writing Task 1 genre?", "options": [
            "Sender's address, date, recipient's address, salutation, body, closing, and signature", "A single unstructured paragraph with no formal elements",
            "A bulleted list with no prose at all", "A term unrelated to letter writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is a clear, appropriate salutation (e.g. 'Dear Sir/Madam') important in a formal letter?", "options": [
            "It sets the correct tone of respect and formality for the intended reader", "Salutations have no effect on a letter's tone",
            "This element is unrelated to formal writing", "Salutations are used only in informal writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of the closing line in a formal letter (e.g. 'Yours faithfully')?", "options": [
            "To end the letter politely and appropriately for its formal tone", "To introduce a new topic",
            "A term unrelated to letter structure", "To restate the recipient's address"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a short descriptive writing task, what is the primary goal?", "options": [
            "To vividly convey a scene, object, or experience using sensory detail", "To present a purely statistical argument with no description",
            "A term unrelated to descriptive writing", "To avoid any use of descriptive language"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is staying within a specified word limit important for a structured writing task?", "options": [
            "It demonstrates the ability to be concise and organise ideas efficiently", "Word limits have no relevance to writing tasks",
            "This constraint is unrelated to structured writing assessment", "Longer responses are always considered better regardless of word limits"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a clear topic sentence in each paragraph of a short writing task?", "options": [
            "It signals the main idea the rest of the paragraph will develop", "Topic sentences have no organisational function",
            "A term unrelated to paragraph structure", "Topic sentences should always be placed only at the very end of a paragraph"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a formal complaint letter (a common Writing Task 1 scenario), what should the body typically include?", "options": [
            "A clear explanation of the issue and a reasonable request for resolution", "Purely emotional language with no factual explanation",
            "A term unrelated to complaint letter writing", "No mention of the actual problem being reported"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a short report-style writing task require the use of headings or clear paragraph divisions?", "options": [
            "It helps organise information clearly for the reader to follow", "Headings have no effect on how a report is read",
            "This structural choice is unrelated to report writing", "Reports should never be divided into sections"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of proofreading a short writing task before submission?", "options": [
            "To catch and correct grammar, spelling, and clarity issues", "Proofreading has no value for exam-style writing tasks",
            "A term unrelated to writing tasks", "Proofreading should be skipped to save time regardless of accuracy"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In an informal letter (as opposed to a formal one), what tone is typically appropriate?", "options": [
            "A warmer, more personal and conversational tone", "A strictly formal, impersonal tone",
            "A term unrelated to letter writing", "A tone identical to a formal business letter"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a Writing Task 1 exercise specify a particular audience (e.g. 'write to your school principal')?", "options": [
            "Audience awareness shapes appropriate tone, formality, and content", "Audience specification has no effect on how a task should be approached",
            "This detail is unrelated to writing task instructions", "The audience never affects tone or content choices"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a clear purpose statement early in a formal letter (e.g. 'I am writing to...')?", "options": [
            "It immediately signals to the reader why the letter is being written", "Purpose statements are unnecessary in formal letters",
            "A term unrelated to letter structure", "Purpose statements should always be placed at the very end"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is task-specific vocabulary (e.g. appropriate terms for a complaint vs. an invitation) important in Writing Task 1 responses?", "options": [
            "It demonstrates the writer's ability to adapt language appropriately to different real-world writing purposes", "Vocabulary choice has no bearing on task-specific writing",
            "This topic is unrelated to structured writing assessment", "The same vocabulary should be used regardless of the writing task's purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'register' mean in the context of choosing appropriate language for a writing task?", "options": [
            "The level of formality and style suited to a specific audience and purpose", "A term unrelated to writing tasks",
            "A synonym for grammar accuracy alone", "A purely technical term with no connection to tone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might planning briefly before writing (e.g. jotting down key points) improve a structured writing task response?", "options": [
            "It helps organise ideas logically before committing to the final written response", "Planning has no impact on the quality of a writing task response",
            "This practice is unrelated to structured writing tasks", "Planning should always be skipped to save time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a common feature expected in an invitation letter, a possible Writing Task 1 scenario?", "options": [
            "Clear details of the event, including date, time, and location", "Vague or missing information about the event",
            "A term unrelated to invitation letter writing", "A strictly negative tone throughout"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might examiners assess coherence (logical flow) as well as grammar in a Writing Task 1 response?", "options": [
            "Clear organisation of ideas is as important as grammatical accuracy for effective communication", "Coherence has no relevance to writing task assessment",
            "This assessment criterion is unrelated to structured writing", "Only grammar is ever assessed in writing tasks, never organisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is understanding the specific genre conventions (letter vs. report vs. description) important for Writing Task 1?", "options": [
            "Each genre has distinct expected structures and conventions that affect how successfully the task is completed", "All writing genres share identical structures and conventions",
            "This topic is unrelated to structured writing tasks", "Genre conventions are irrelevant to exam-style writing assessment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of a 'Writing Task 1' unit in an English course is to:", "options": [
            "Build practical, structured writing skills for real-world short-form communication", "Memorise unrelated vocabulary with no practical writing application",
            "Avoid any structured or formal writing practice", "Focus exclusively on unrelated grammar drills with no writing component"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37550: [  # Writing Task: 2
        {"q": "A 'Writing Task 2' unit typically builds on Writing Task 1 by focusing on which kind of writing?", "options": [
            "A more extended piece, such as an essay or article requiring developed argumentation", "An even shorter task than Writing Task 1 with less development",
            "A term unrelated to writing skill progression", "A purely spoken task with no written component"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is the typical structure of an argumentative/opinion essay, a common Writing Task 2 genre?", "options": [
            "Introduction with thesis, body paragraphs with supporting points, and a conclusion", "A single unstructured paragraph with no clear organisation",
            "A bulleted list with no prose at all", "A term unrelated to essay writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is a clear thesis statement important in the introduction of an essay?", "options": [
            "It signals the essay's main argument and guides the reader's expectations", "Thesis statements have no organisational function",
            "This element is unrelated to essay structure", "Thesis statements should always be placed only in the conclusion"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of including a counter-argument in a persuasive essay?", "options": [
            "To acknowledge an opposing view and then respond to it, strengthening the essay's own position", "Counter-arguments always weaken an essay's persuasive power",
            "A term unrelated to persuasive writing", "Essays should never consider opposing viewpoints"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is providing specific evidence or examples important in an argumentative essay?", "options": [
            "It supports claims and makes the argument more convincing", "Evidence has no bearing on how convincing an argument is",
            "A term unrelated to essay writing", "Essays are more persuasive when claims are left entirely unsupported"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a concluding paragraph in an essay?", "options": [
            "To summarise the main points and reinforce the overall argument", "To introduce an entirely new argument",
            "A term unrelated to essay structure", "To simply repeat the introduction word for word"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'coherence' mean in the context of an extended essay response?", "options": [
            "Logical flow of ideas from one paragraph to the next", "Using as many complex words as possible with no logical connection",
            "A term unrelated to essay writing", "Writing with no punctuation at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an article (a possible Writing Task 2 genre) use a catchy title and engaging opening?", "options": [
            "To capture the reader's interest from the start, appropriate to the genre's more public audience", "Titles and openings have no effect on reader engagement",
            "This technique is unrelated to article writing", "Articles should always begin with the most technical, dry information"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of transition words (e.g. 'furthermore', 'however') in an extended essay?", "options": [
            "To show the logical relationship between ideas across sentences and paragraphs", "Transition words have no function in essay writing",
            "A term unrelated to essay coherence", "Transition words should be avoided entirely in formal writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is planning an essay's structure before writing considered valuable for Writing Task 2 responses?", "options": [
            "It helps ensure the argument develops logically and stays within scope", "Planning has no impact on the quality of an extended essay",
            "This practice is unrelated to essay writing", "Planning should always be skipped to save time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'unity' mean when evaluating a paragraph within a longer essay?", "options": [
            "All the sentences in the paragraph relate clearly to a single main idea", "A paragraph containing many completely unrelated ideas",
            "A term unrelated to paragraph structure", "A paragraph consisting of only one very short sentence"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay task ask students to consider multiple perspectives on an issue?", "options": [
            "It develops critical thinking and a more nuanced, well-rounded argument", "Considering multiple perspectives always weakens an essay",
            "This requirement is unrelated to essay writing skill", "Essays should always present only one narrow, unexamined viewpoint"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of a strong concluding sentence that restates the thesis in different words?", "options": [
            "It reinforces the essay's central argument for the reader without exact repetition", "Repeating the exact same thesis sentence verbatim is always preferred",
            "A term unrelated to essay conclusions", "Conclusions should introduce a completely unrelated new topic"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay on a social issue (a common Writing Task 2 prompt type) require balanced, well-reasoned argument rather than pure emotion?", "options": [
            "Reasoned argument tends to be more persuasive and credible to a general reader", "Pure emotional appeal is always more effective than reasoned argument",
            "This requirement is unrelated to persuasive essay writing", "Essays on social issues should avoid any reasoning entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'paragraph unity and coherence together' contribute to an extended essay?", "options": [
            "They ensure both individual paragraphs and the essay as a whole read logically and clearly", "They have no combined effect on essay quality",
            "This combination is unrelated to essay assessment", "Only one of the two is ever assessed, never both together"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might examiners assess the range of vocabulary used in a Writing Task 2 response?", "options": [
            "Varied, appropriate vocabulary can demonstrate stronger command of the language", "Vocabulary range has no bearing on essay quality",
            "This assessment criterion is unrelated to extended writing", "Simpler vocabulary is always preferred over varied vocabulary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of addressing the specific essay prompt directly, rather than writing generally about the topic?", "options": [
            "It ensures the response fully answers what was actually asked", "Addressing the prompt directly has no bearing on task success",
            "A term unrelated to essay writing assessment", "General, unfocused writing is always preferred over addressing the prompt directly"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay use a mix of sentence lengths and structures?", "options": [
            "Varied sentence structure can improve readability and demonstrate stronger writing control", "Sentence variety has no effect on writing quality",
            "This technique is unrelated to essay writing style", "All sentences in an essay should always be exactly the same length"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is revising a draft essay for both content and grammar considered good writing practice?", "options": [
            "It allows the writer to improve both the argument's clarity and its technical accuracy", "Revision has no value once a first draft is written",
            "This practice is unrelated to essay writing", "Only grammar should ever be revised, never the content or argument"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of a 'Writing Task 2' unit in an English course is to:", "options": [
            "Build skills in developing extended, well-organised argumentative or expository writing", "Memorise unrelated vocabulary with no practical writing application",
            "Avoid any extended or argumentative writing practice", "Focus exclusively on unrelated grammar drills with no writing component"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37551: [  # Writing Task: 3
        {"q": "A 'Writing Task 3' unit typically builds further by focusing on which kind of writing?", "options": [
            "A more advanced or creative writing task, such as a narrative, review, or reflective piece", "An even shorter, more basic task than Writing Task 1",
            "A term unrelated to writing skill progression", "A purely multiple-choice grammar exercise"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What is a key structural feature of narrative writing, a possible Writing Task 3 genre?", "options": [
            "A clear sequence of events, often including a setting, conflict, and resolution", "A purely factual, list-based structure with no story elements",
            "A term unrelated to narrative writing", "Narrative writing avoids any use of characters or plot"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a narrative writing task encourage the use of descriptive, sensory language?", "options": [
            "It helps immerse the reader in the story's setting and events", "Descriptive language has no place in narrative writing",
            "This technique is unrelated to narrative writing", "Sensory language always distracts from a narrative's plot"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a 'hook' or engaging opening in a creative writing task?", "options": [
            "To capture the reader's attention from the very first line", "Openings have no effect on reader engagement",
            "A term unrelated to creative writing", "The opening should always be the least interesting part of a story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is a 'review' as a writing genre (e.g. a book or film review), a possible Writing Task 3 type?", "options": [
            "A piece evaluating and giving an opinion on a work, supported by specific reasons", "A purely factual summary with no evaluation or opinion",
            "A term unrelated to writing genres", "A review must always be entirely negative in tone"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a review include specific examples to support its evaluation?", "options": [
            "Specific examples make the reviewer's opinion more credible and persuasive", "Examples have no bearing on how convincing a review is",
            "A term unrelated to review writing", "Reviews should never reference specific details from the work being reviewed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'reflective writing' typically involve, as a possible Writing Task 3 genre?", "options": [
            "Personal exploration of one's own thoughts, feelings, or experiences on a topic", "A purely objective, impersonal report with no personal voice",
            "A term unrelated to writing genres", "Reflective writing must always avoid any first-person perspective"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a narrative writing task assess the use of dialogue?", "options": [
            "Well-crafted dialogue can reveal character and advance the plot effectively", "Dialogue has no role in narrative writing assessment",
            "This element is unrelated to narrative writing", "Dialogue should always be avoided in narrative writing tasks"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a clear climax or turning point in narrative writing?", "options": [
            "It provides the story's central moment of tension or change that drives toward resolution", "A climax has no structural function in a narrative",
            "A term unrelated to narrative writing", "Stories should never include any turning point or climax"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might reflective writing tasks ask students to connect a personal experience to a broader lesson or insight?", "options": [
            "It develops the ability to derive meaning from experience, a valued reflective writing skill", "Connecting experience to insight has no value in reflective writing",
            "This requirement is unrelated to reflective writing tasks", "Reflective writing should never draw any broader conclusion from experience"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'voice' mean in creative or reflective writing, as distinct from formal essay writing?", "options": [
            "The distinctive personal style and tone through which a writer expresses themselves", "A term unrelated to creative writing",
            "A purely technical grammatical concept", "A synonym for volume in spoken presentation only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a narrative writing task specify a word limit despite its creative nature?", "options": [
            "It still requires the writer to demonstrate concise, well-structured storytelling", "Word limits are irrelevant to creative writing tasks",
            "This requirement is unrelated to structured writing assessment", "Creative writing tasks never have any length constraints"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of a satisfying resolution at the end of a short narrative?", "options": [
            "It brings closure to the story's central conflict or tension", "Resolutions have no function in narrative structure",
            "A term unrelated to narrative writing", "Stories should always end abruptly with no resolution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a book or film review balance both strengths and weaknesses of the work being reviewed?", "options": [
            "A balanced evaluation is often considered more credible and thoughtful than a one-sided view", "Reviews should always focus exclusively on either strengths or weaknesses, never both",
            "This balance is unrelated to review writing", "Balanced evaluation has no effect on a review's credibility"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'characterisation' mean in the context of narrative writing tasks?", "options": [
            "The way a writer develops and reveals a character's personality through action and description", "A term unrelated to narrative writing",
            "A purely grammatical concept with no connection to storytelling", "A synonym for plot summary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might reflective writing be considered valuable for developing self-awareness alongside writing skill?", "options": [
            "It encourages thoughtful examination of one's own experiences and their significance", "Reflective writing has no connection to self-awareness",
            "This value is unrelated to writing task purpose", "Self-awareness is irrelevant to developing writing skill"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the effect of a well-chosen title on a piece of creative or reflective writing?", "options": [
            "It can set expectations and draw the reader's interest before they even begin reading", "Titles have no effect on how a piece of writing is received",
            "This element is unrelated to writing task assessment", "Titles should always be avoided in creative writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might examiners assess creativity and originality alongside technical accuracy in a Writing Task 3 response?", "options": [
            "Advanced writing tasks often value imaginative and personal expression, not just correctness", "Creativity is never assessed alongside grammar in writing tasks",
            "This assessment criterion is unrelated to advanced writing tasks", "Only technical accuracy is ever assessed, never creative quality"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is it useful to revise a creative or reflective piece for both narrative flow and grammatical accuracy?", "options": [
            "Both elements contribute to how effectively and clearly the piece communicates its meaning", "Only grammar matters in creative writing revision, never narrative flow",
            "This practice is unrelated to writing task quality", "Revision is unnecessary once a first draft is complete"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The overall purpose of a 'Writing Task 3' unit in an English course is to:", "options": [
            "Build advanced, expressive writing skills across creative and reflective genres", "Memorise unrelated vocabulary with no practical writing application",
            "Avoid any creative or personal writing practice", "Focus exclusively on unrelated grammar drills with no writing component"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37552: [  # A Matter of Husbands
        {"q": "'A Matter of Husbands' is best classified as which literary form?", "options": [
            "A one-act play (drama)", "A formal scientific essay", "A personal travel memoir", "A legal document"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title 'A Matter of Husbands' suggest about the play's likely central subject?", "options": [
            "A situation or conflict centred on marriage or relationships between spouses", "A purely technical description of legal contracts",
            "An unrelated discussion of scientific research", "A description of a natural landscape"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In drama, why might a play centred on marital or domestic conflict use humour to explore its themes?", "options": [
            "Comic tone can make relationship dynamics and misunderstandings more engaging and accessible to an audience", "Humour is never used to explore relationship themes in drama",
            "This technique is unrelated to dramatic writing", "Domestic conflict cannot be portrayed comedically"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'domestic comedy' mean as a dramatic sub-genre potentially relevant to this play's likely subject?", "options": [
            "A comedic play centred on household or marital relationships and situations", "A term unrelated to dramatic genres",
            "A synonym for a purely tragic drama", "A genre that never involves any humour"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a one-act play focused on a single domestic scenario use a small cast of characters?", "options": [
            "A small cast allows focused character development and dialogue within a brief, compact format", "Small casts are never used in plays exploring relationship themes",
            "This structural choice is unrelated to dramatic writing", "A small cast means the play has no meaningful theme"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is 'characterisation through dialogue' in a play exploring marital dynamics?", "options": [
            "Revealing a character's personality and views on marriage primarily through what they say", "Revealing character only through stage directions",
            "A term unrelated to playwriting", "Ignoring character development entirely in favour of plot"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a play about marriage explore differing perspectives between characters on the same relationship?", "options": [
            "Contrasting viewpoints can reveal complexity and generate dramatic or comic tension", "Differing perspectives have no dramatic function",
            "This technique is unrelated to plays about relationships", "All characters in such a play always share an identical viewpoint"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'irony' mean, a device potentially relevant to a comedic exploration of marital misunderstanding?", "options": [
            "A contrast between what is expected or said and what is actually true", "A term unrelated to comedic drama",
            "A synonym for a purely literal, straightforward statement", "A device used only in tragedy, never comedy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might plays exploring marriage or relationships remain popular subjects across many dramatic traditions?", "options": [
            "Relationship dynamics are a broadly relatable human experience across cultures and eras", "Marriage has never been a common subject in drama",
            "This appeal is unrelated to why certain themes recur in literature", "Relationship-themed plays are considered a modern, recent innovation with no history"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a play's central problem or tension that drives the action?", "options": [
            "'Conflict'", "'Trigonometry'", "'Photosynthesis'", "'Diaspora'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a comedic play about marriage end with a resolution restoring harmony between characters?", "options": [
            "Comic structure often moves toward reconciliation or a satisfying resolution of misunderstanding", "Comedic plays never resolve their central conflict",
            "This structural choice is unrelated to comedic drama", "Resolutions are used only in tragic, not comic, plays"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'stage direction' mean in the context of a play exploring domestic settings?", "options": [
            "Written instructions describing setting, movement, or delivery, distinct from spoken dialogue", "The dialogue spoken by characters",
            "The audience's applause", "A synonym for the play's title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a play use a household or domestic setting to explore broader social attitudes toward marriage?", "options": [
            "A familiar domestic setting can ground broader social commentary in relatable, everyday circumstance", "Domestic settings have no connection to broader social themes",
            "This technique is unrelated to dramatic writing", "Plays exploring social attitudes never use domestic settings"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of comprehension questions asking readers to identify a character's motivation in a scene from this play?", "options": [
            "Understanding motivation helps interpret why characters act and speak as they do", "Motivation has no relevance to understanding drama",
            "This question type is unrelated to studying plays", "Characters in drama never have any clear motivation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this play be considered relevant for exploring gender roles and expectations within marriage?", "options": [
            "Plays about marriage often engage with social expectations placed on spouses", "Gender roles are never explored in plays about marriage",
            "This topic is unrelated to the play's likely themes", "Marriage-themed plays avoid any social commentary"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'comic timing' mean as a dramatic technique potentially relevant to this play?", "options": [
            "The placement and pacing of a line or event to maximise its comedic effect", "A term unrelated to comedic drama",
            "A synonym for a play's overall length", "Timing has no connection to how humour is perceived"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is close reading of a play's dialogue especially important, since plays are meant to be performed?", "options": [
            "Dialogue carries much of the meaning that narration would in prose fiction", "Dialogue is unimportant compared to stage directions",
            "Plays contain no meaningful dialogue", "Close reading is unnecessary for dramatic texts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the general educational value of studying a one-act play centred on relationship dynamics in an English course?", "options": [
            "It develops appreciation of dramatic structure and dialogue while engaging with a relatable social theme", "Studying such plays has no educational value",
            "One-act plays about relationships are considered inappropriate for study", "This topic is unrelated to English literature study"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this play ask readers to compare two characters' differing attitudes toward marriage?", "options": [
            "Comparing perspectives develops the skill of analysing contrast and characterisation in drama", "Comparing characters has no analytical value",
            "This question type is unrelated to studying plays", "All characters in the play necessarily hold identical views"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'A Matter of Husbands' in an English course is to:", "options": [
            "Build appreciation of dramatic technique and characterisation through a relatable social theme", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with drama exploring relationships or social roles", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37553: [  # Facing Death
        {"q": "'Facing Death' is best classified as which type of text?", "options": [
            "A reflective/expository essay", "A one-act comic play", "A formal legal contract", "A travel itinerary"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title 'Facing Death' suggest the essay is likely to explore?", "options": [
            "Human attitudes, fears, or philosophical perspectives toward mortality", "A purely technical medical procedure with no reflection",
            "An unrelated discussion of financial planning", "A description of a fictional adventure story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay on mortality explore how different cultures or individuals cope with the idea of death?", "options": [
            "Comparing perspectives can offer insight into universal human responses to a difficult, shared reality", "Cultural perspectives have no relevance to essays on mortality",
            "This topic is unrelated to reflective essay writing", "Such essays never compare differing viewpoints"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of a reflective essay exploring a difficult, universal topic like mortality?", "options": [
            "To prompt readers toward thoughtful consideration of meaning, value, and perspective in life", "Such essays have no purpose or effect on readers",
            "This topic is unrelated to reflective writing", "Reflective essays never invite reader self-examination"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a writer use a calm, measured tone when writing about a topic as emotionally weighty as death?", "options": [
            "A measured tone can invite thoughtful reflection rather than overwhelming the reader emotionally", "Tone has no bearing on how a reader engages with a serious topic",
            "This choice is unrelated to essay writing", "Serious topics must always be written about in an anxious, urgent tone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'philosophical reflection' mean as a quality relevant to an essay considering mortality?", "options": [
            "Thoughtful consideration of deep, fundamental questions about existence and meaning", "A term unrelated to essays on this topic",
            "A synonym for a purely factual, non-reflective statement", "A purely comedic device with no serious content"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay on facing mortality discuss the value of living meaningfully in the present?", "options": [
            "Reflecting on death can, for many writers, reframe how one thinks about valuing life while living it", "Such a connection is never made in essays on mortality",
            "This topic is unrelated to reflective writing on death", "Essays about mortality never touch on how to live"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'acceptance' mean as a possible theme in an essay reflecting on death?", "options": [
            "Coming to terms with a difficult reality rather than resisting or denying it", "A term unrelated to reflective essays",
            "A synonym for complete indifference toward the topic", "A purely legal or medical classification"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might such an essay be considered emotionally challenging but valuable to include in a literature curriculum?", "options": [
            "It engages students with a universal human experience through thoughtful, structured reflection", "Difficult emotional topics have no place in an English curriculum",
            "This topic is inappropriate for any academic study", "Essays on mortality are unrelated to language or literature learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What vocabulary term describes writing that expresses personal contemplation on a serious topic?", "options": [
            "'Introspective'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay use a personal anecdote (e.g. losing a loved one) to ground a broader reflection on mortality?", "options": [
            "Personal experience can make an abstract, universal topic feel immediate and relatable", "Personal anecdotes have no place in essays about serious topics",
            "This technique is unrelated to reflective essay writing", "Such essays must remain entirely impersonal and abstract"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the effect of open-ended questions posed within a reflective essay on mortality?", "options": [
            "They can invite the reader to engage in their own reflection rather than simply receive an answer", "Open-ended questions always weaken a reflective essay",
            "This technique is unrelated to essay writing", "Essays should never pose questions they do not fully answer"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might different religious or philosophical traditions be referenced in an essay exploring attitudes toward death?", "options": [
            "Such traditions often offer distinct frameworks for understanding mortality worth comparing", "Religious or philosophical traditions have no connection to this topic",
            "This topic is unrelated to reflective essay writing", "Only one single viewpoint is ever valid when discussing mortality"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'universal theme' mean, relevant to why an essay on mortality might resonate broadly?", "options": [
            "An idea broadly relatable to human experience regardless of background", "A term unrelated to literary analysis",
            "A synonym for an idea relevant to only one narrow group", "A purely local, culturally specific concept with no wider relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this essay ask readers to identify its central argument or perspective?", "options": [
            "To test the ability to extract the main idea from a reflective, philosophical text", "Identifying central arguments has no value in comprehension",
            "This question type is unrelated to essay analysis", "Reflective essays on mortality never present a clear perspective"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'legacy' mean as a concept potentially explored in an essay about mortality?", "options": [
            "The lasting impact or influence a person leaves behind after death", "A term unrelated to reflective essays on this topic",
            "A purely financial or legal inheritance only", "A synonym for immediate, short-term achievement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay balance discussing fear of death with a message of hope or meaning?", "options": [
            "A balanced approach can present a fuller, more nuanced reflection rather than pure despair", "Balance has no value in essays about difficult topics",
            "This approach is unrelated to reflective essay writing", "Essays on mortality must always focus exclusively on fear"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of studying essays on difficult universal themes in developing empathy and maturity?", "options": [
            "It can build emotional and intellectual capacity to engage thoughtfully with life's hardest questions", "Studying such essays has no connection to emotional or intellectual growth",
            "This educational value is unrelated to literature study", "Essays on serious topics should always be avoided in education"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'candour' mean, a quality often valued in essays honestly confronting difficult topics?", "options": [
            "Openness and honesty in expressing one's thoughts", "A term unrelated to essay writing",
            "A synonym for deliberate vagueness", "A purely legal or formal term"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The general educational value of studying 'Facing Death' in an English course is to:", "options": [
            "Develop skills in analysing reflective, philosophical writing on a significant universal theme", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on difficult or serious topics", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37554: [  # The Bull
        {"q": "'The Bull' is best classified, based on its concise title, as most likely which literary form in this curriculum context?", "options": [
            "A poem or short piece of descriptive/narrative writing", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a short literary piece use a single animal as its central image or subject?", "options": [
            "A focused central image can carry symbolic or descriptive weight efficiently within a short form", "Animals are never used as central subjects in short literary works",
            "This technique is unrelated to concise literary writing", "A single-subject focus always weakens a short piece's impact"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What literary device is at work when an animal is described in a way that suggests broader symbolic meaning (e.g. strength, endurance)?", "options": [
            "Symbolism", "A purely literal description with no figurative meaning", "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might descriptive writing about an animal use vivid, sensory language (sight, sound, movement)?", "options": [
            "It helps the reader vividly picture the subject and its qualities", "Sensory language has no role in descriptive writing",
            "This technique is unrelated to short descriptive pieces", "Descriptive detail always distracts from a piece's central image"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'imagery' mean as a literary technique likely central to a short piece focused on a single vivid subject?", "options": [
            "Descriptive language appealing to the senses to create a vivid impression", "A term unrelated to literary analysis",
            "A purely factual, non-descriptive style of writing", "A synonym for the piece's rhyme scheme only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a writer use rhythm or repetition (if the piece is a poem) to convey the physicality or power of its subject?", "options": [
            "Rhythmic language can mirror the energy or movement being described", "Rhythm has no connection to conveying physical qualities in writing",
            "This technique is unrelated to poetic description", "Repetition is never used to convey energy or movement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'tone' mean when analysing a short descriptive piece about a powerful or striking subject?", "options": [
            "The emotional attitude conveyed through the writer's language and description", "A term unrelated to literary analysis",
            "Only the literal meaning of the words with no emotional layer", "A synonym for the piece's title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a short piece focused on an animal be read as exploring themes of nature and human observation?", "options": [
            "Close, attentive description of a natural subject can reflect on humanity's relationship with the natural world", "Nature writing never explores humanity's relationship to it",
            "This thematic reading is unrelated to literary analysis", "Animal-focused writing has no connection to broader thematic meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes writing that vividly describes a scene, object, or subject?", "options": [
            "'Descriptive'", "'Trigonometry'", "'Photosynthesis'", "'Jurisdiction'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might close reading of word choice be especially important in a very short, concentrated literary piece?", "options": [
            "In compact writing, each word carries more weight since there is less room for elaboration", "Word choice has no particular significance in short pieces",
            "This analytical approach is unrelated to studying concise texts", "Close reading is unnecessary for short literary works"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a writer contrast an animal's calm and its potential power or ferocity within a description?", "options": [
            "Contrast can heighten the reader's sense of the subject's complexity or latent energy", "Contrast has no descriptive or thematic effect",
            "This technique is unrelated to descriptive writing", "Calm and power are never juxtaposed in descriptive writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'personification' mean, a device potentially relevant if the piece attributes human-like qualities to its subject?", "options": [
            "Giving human characteristics to a non-human thing", "A term unrelated to literary technique",
            "A synonym for a purely factual description", "A device used only in comedic writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on a short descriptive piece ask about its central image's significance?", "options": [
            "Understanding a central image is often key to grasping the piece's overall meaning or theme", "Central images carry no particular significance for comprehension",
            "This question type is unrelated to studying short literary pieces", "Such pieces never contain a clearly identifiable central image"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'concision' mean as a quality of a very short literary piece?", "options": [
            "Expressing meaning efficiently using relatively few words", "Using as many words as possible to fill space",
            "A term unrelated to literary style", "A synonym for vagueness or lack of clarity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might such a short piece still be considered rich material for literary analysis despite its brevity?", "options": [
            "Concentrated, carefully chosen language can carry significant thematic and descriptive depth", "Short pieces are always too simple to analyse meaningfully",
            "This value is unrelated to studying concise literary forms", "Length is the only factor that determines a text's analytical richness"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'observation' mean as a skill relevant to writing detailed descriptive pieces about a natural subject?", "options": [
            "Careful, attentive noticing of details, which can then be conveyed vividly in writing", "A term unrelated to descriptive writing",
            "A synonym for guessing without any careful attention", "A purely scientific method with no literary application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comparing this short piece with other animal-focused literary works be a useful analytical exercise?", "options": [
            "It can reveal different ways writers use animals symbolically or descriptively across texts", "Such comparison has no analytical value",
            "This approach is unrelated to literary study", "Animal-focused works can never meaningfully be compared to one another"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the general educational value of studying a short, image-focused literary piece in an English course?", "options": [
            "It builds close-reading skills and appreciation for how concise language can convey rich meaning", "Studying short pieces has no educational value",
            "Short literary works are considered too simple for serious study", "This topic is unrelated to developing literary analysis skills"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this piece ask readers to describe the mood created by its language?", "options": [
            "Identifying mood tests the ability to connect word choice and imagery to overall emotional effect", "Mood has no relevance to understanding a descriptive piece",
            "This question type is unrelated to studying short literary works", "Descriptive pieces never create any discernible mood"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'The Bull' in an English course is to:", "options": [
            "Develop close-reading and descriptive-analysis skills through a concentrated literary text", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with short or image-focused literary forms", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37555: [  # On Libraries
        {"q": "'On Libraries' is best classified as which type of text?", "options": [
            "A reflective/expository essay", "A one-act comic play", "A formal legal contract", "A travel itinerary"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title 'On Libraries' suggest about the essay's likely focus?", "options": [
            "A reflection on the value, role, or experience of libraries", "A purely technical architectural blueprint",
            "An unrelated discussion of financial markets", "A description of a fictional adventure story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay on libraries discuss their role in providing access to knowledge?", "options": [
            "Libraries are widely valued as institutions that democratise access to information and learning", "Libraries have no connection to access to knowledge",
            "This topic is unrelated to essays about libraries", "Such essays never discuss the purpose of libraries"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'public good' mean, a concept potentially relevant to an essay on the social value of libraries?", "options": [
            "A resource or benefit available to and valuable for the whole community", "A term unrelated to essays on libraries",
            "A purely private, individually-owned resource only", "A synonym for a resource of no communal value"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay reflect on the personal, nostalgic value of libraries alongside their practical function?", "options": [
            "Personal reflection can complement broader argument, showing both emotional and practical significance", "Personal reflection has no place in an essay about institutions",
            "This combination is unrelated to essay writing", "Essays about libraries must remain purely factual with no personal reflection"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of an essay arguing for the continued relevance of libraries in the digital age?", "options": [
            "To address the perception that libraries may be less necessary given online information access", "Such essays never address concerns about libraries' relevance",
            "This topic is unrelated to essays about libraries", "Libraries are considered entirely irrelevant in every modern essay on the topic"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay discuss libraries as spaces for quiet reflection and community alongside their role as information repositories?", "options": [
            "Libraries can serve multiple social and personal functions beyond simply storing books", "Libraries are only ever discussed as storage spaces with no social function",
            "This topic is unrelated to essays about libraries", "Quiet reflection has no connection to library spaces"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'literacy' mean, a concept often connected to essays discussing the value of libraries?", "options": [
            "The ability to read and write, foundational to accessing knowledge", "A term unrelated to essays about libraries",
            "A purely mathematical skill with no connection to reading", "A synonym for illiteracy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay on libraries reference their historical role in preserving knowledge across generations?", "options": [
            "Libraries have long served as repositories preserving human knowledge over time", "Libraries have no historical connection to preserving knowledge",
            "This topic is unrelated to essays about libraries", "Such essays never reference the historical role of libraries"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes writing that explains and informs using evidence and reasoning?", "options": [
            "'Expository'", "'Alliteration'", "'Diaspora'", "'Nostalgia'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay discuss unequal access to libraries or reading materials as a social issue?", "options": [
            "It highlights how access to knowledge resources is not always evenly distributed", "Unequal access has no connection to essays about libraries",
            "This topic is unrelated to essays on this theme", "All communities are assumed to have identical access to libraries"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'intellectual freedom' mean, a concept sometimes connected to essays about libraries?", "options": [
            "The right to access information and ideas freely, often associated with library values", "A term unrelated to essays about libraries",
            "A purely legal concept with no connection to reading or information access", "A synonym for restricted access to information"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a personal essay on libraries include a specific memory of a formative reading experience?", "options": [
            "A concrete personal example can make an abstract argument about libraries' value more relatable", "Personal memories are irrelevant to essays about libraries",
            "This technique is unrelated to essay writing", "Formative reading experiences are never discussed in such essays"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of comprehension questions asking readers to summarise the essay's central argument about libraries?", "options": [
            "To test the ability to identify and condense the central idea of an expository/reflective text", "Summarising has no value for comprehension",
            "This question type is unrelated to essay analysis", "Essays about libraries never present a clear central argument"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay discuss how libraries have adapted (e.g. digital resources) rather than becoming obsolete?", "options": [
            "It can support an argument that libraries remain relevant by evolving alongside technology", "Libraries are always presented as entirely unchanged institutions",
            "This topic is unrelated to essays about libraries", "Adaptation has no connection to essays on institutional relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'civic institution' mean, a term potentially relevant to describing a library's social role?", "options": [
            "An institution serving the public and contributing to community life", "A term unrelated to essays about libraries",
            "A purely private business with no public function", "A synonym for a strictly religious institution"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this essay be considered relevant reading for students, given its subject matter?", "options": [
            "It reflects directly on an institution central to education and learning, like the one students are part of", "This essay has no relevance to students",
            "This connection is unrelated to studying the essay", "Libraries have no connection to students' educational experience"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'accessibility' mean in the context of an essay discussing who benefits from libraries?", "options": [
            "The ease with which people, especially from varied backgrounds, can use a resource", "A term unrelated to essays about libraries",
            "A purely architectural concept with no social dimension", "A synonym for exclusivity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is studying an essay reflecting on institutions like libraries valuable in an English course?", "options": [
            "It builds both expository reading skills and appreciation for institutions supporting learning and access to knowledge", "Such essays have no educational value",
            "This topic is inappropriate for an English curriculum", "Essays about libraries are unrelated to language learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'On Libraries' in an English course is to:", "options": [
            "Develop appreciation for expository/reflective writing while considering the value of knowledge institutions", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on institutions or social value", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37556: [  # Marriage as a Social Institution
        {"q": "'Marriage as a Social Institution' is best classified as which type of text?", "options": [
            "An expository/sociological essay", "A one-act comic play", "A personal travel memoir", "A legal contract"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title suggest the essay's central approach to marriage will be?", "options": [
            "Examining marriage as a structured social practice with broader societal functions, not just a personal relationship", "A purely personal, emotional account with no social analysis",
            "An unrelated discussion of economic trade policy", "A description of a fictional romance story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'social institution' mean as a sociological concept relevant to this essay's title?", "options": [
            "An established, structured pattern of social behaviour that fulfils a recognised societal function", "A term unrelated to sociology or social analysis",
            "A synonym for a single individual's private choice with no social dimension", "A purely legal term with no connection to social patterns"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay examine how marriage customs vary across different cultures?", "options": [
            "Comparing practices can reveal both the diversity and shared social functions of marriage across societies", "Marriage customs are identical in every culture, requiring no comparison",
            "This topic is unrelated to essays about marriage as an institution", "Cultural comparison has no place in sociological essay writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What social functions might an essay argue marriage traditionally serves (e.g. economic partnership, family structure)?", "options": [
            "Organising family life, economic cooperation, and social stability, among other functions", "Marriage is argued to serve no social function whatsoever",
            "This topic is unrelated to essays on this theme", "Such essays never discuss the functions of marriage"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay discuss how attitudes toward marriage have changed over time?", "options": [
            "Social institutions often evolve alongside broader shifts in values and circumstances", "Marriage as an institution has never changed throughout history",
            "This topic is unrelated to essays about social institutions", "Such essays never discuss historical change"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'gender roles within marriage' mean as a topic potentially explored in this essay?", "options": [
            "The expectations and responsibilities traditionally or currently assigned to spouses based on gender", "A term unrelated to essays about marriage as an institution",
            "A purely legal classification with no social dimension", "A synonym for an entirely fixed, unchanging concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay on this theme discuss both the benefits and challenges associated with marriage as an institution?", "options": [
            "A balanced sociological analysis considers both supportive and critical perspectives", "Such essays only ever present one entirely one-sided view",
            "This balance is unrelated to expository essay writing", "Challenges associated with marriage are never discussed in such essays"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of using a sociological/analytical lens (rather than purely personal opinion) in this kind of essay?", "options": [
            "It allows for a broader, evidence-informed examination of marriage's societal role", "A sociological lens has no advantage over personal opinion alone",
            "This approach is unrelated to essay writing", "Analytical essays never draw on any broader social perspective"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes writing that explains and informs using evidence and structured reasoning?", "options": [
            "'Expository'", "'Alliteration'", "'Nostalgia'", "'Onomatopoeia'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay discuss the economic dimensions historically associated with marriage (e.g. dowry, inheritance)?", "options": [
            "Economic considerations have historically been intertwined with marriage practices in many societies", "Economic factors have no historical connection to marriage",
            "This topic is unrelated to essays on marriage as a social institution", "Such essays never discuss economic dimensions of marriage"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social stability' mean as a function sometimes attributed to institutions like marriage?", "options": [
            "The maintenance of consistent, predictable social structures and relationships within a community", "A term unrelated to essays about social institutions",
            "A purely individual, private concept with no communal dimension", "A synonym for social chaos"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay compare arranged marriage traditions with marriage based primarily on individual romantic choice?", "options": [
            "It can illustrate differing cultural approaches to how marriage is understood and organised", "Such a comparison is never made in sociological essays",
            "This topic is unrelated to essays about marriage as an institution", "Arranged and romantic-choice marriage are considered identical with no meaningful distinction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of comprehension questions asking readers to identify the essay's main argument about marriage's social role?", "options": [
            "To test the ability to extract the central thesis from an expository/sociological text", "Identifying the main argument has no value for comprehension",
            "This question type is unrelated to essay analysis", "Such essays never present a clear central argument"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay discuss changing legal definitions or rights connected to marriage over time?", "options": [
            "Legal frameworks around marriage often reflect and shape broader social attitudes", "Legal definitions of marriage have never changed historically",
            "This topic is unrelated to essays about marriage as a social institution", "Such essays never discuss legal dimensions of marriage"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'cultural relativism' mean, a concept potentially relevant to comparing marriage customs across societies?", "options": [
            "Understanding a culture's practices within its own context rather than judging by another culture's standards", "A term unrelated to essays comparing social practices",
            "A synonym for judging all cultures by a single fixed standard", "A purely legal, not sociological, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this essay be considered relevant to Nepali students specifically, given ongoing discussions of marriage customs in Nepali society?", "options": [
            "Marriage practices and their evolution are a live, relevant topic within Nepali society", "This topic has no relevance to Nepali students",
            "Nepal has no distinct marriage customs or traditions to discuss", "This topic is unrelated to the Nepali social context"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'social analysis' mean as an approach used in essays examining institutions like marriage?", "options": [
            "Examining a topic in terms of its broader patterns, functions, and impact within society", "A term unrelated to expository essay writing",
            "A purely personal, subjective account with no broader analytical framework", "A synonym for creative fiction writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying an essay analysing a social institution like marriage valuable in an English course?", "options": [
            "It builds expository reading skills alongside critical engagement with social structures and change", "Such essays have no educational value",
            "This topic is inappropriate for an English curriculum", "Essays about social institutions are unrelated to language learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Marriage as a Social Institution' in an English course is to:", "options": [
            "Develop expository reading and analytical skills while engaging with a significant social topic", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on social institutions or structures", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37557: [  # Knowledge and Wisdom
        {"q": "'Knowledge and Wisdom' is best classified as which type of text?", "options": [
            "A reflective/philosophical essay", "A one-act comic play", "A formal legal contract", "A travel itinerary"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Knowledge and Wisdom' is widely attributed to Bertrand Russell, a writer and thinker associated with which broad field?", "options": [
            "Philosophy", "Professional theatre acting", "International diplomacy exclusively", "Culinary arts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What central distinction does the essay's title suggest it will explore?", "options": [
            "The difference between accumulated factual information (knowledge) and the deeper judgment of how to use it well (wisdom)", "A purely technical scientific classification system",
            "An unrelated discussion of economic policy", "A description of a fictional adventure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a philosophical essay argue that knowledge alone does not guarantee wise action?", "options": [
            "Facts and information do not automatically translate into good judgment or ethical decision-making", "Knowledge always guarantees wise action with no exception",
            "This distinction is unrelated to philosophical essay writing", "Wisdom and knowledge are argued to be entirely identical concepts"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'wisdom' typically mean as distinguished from mere factual knowledge in philosophical writing?", "options": [
            "The capacity for sound judgment, especially about how to live and act well", "A synonym for simply possessing many facts",
            "A term unrelated to philosophical discussion", "A purely academic credential with no connection to judgment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might Russell, known for work in both logic/mathematics and broader philosophy, be particularly interested in this distinction?", "options": [
            "His background across rigorous formal reasoning and broader human concerns lends particular insight into this question", "This connection is unrelated to his intellectual background",
            "Formal reasoning has no connection to reflecting on wisdom", "Philosophers never write about the distinction between knowledge and wisdom"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of a philosophical essay using clear, logical argumentation to explore an abstract concept?", "options": [
            "To build a reasoned, persuasive case for the writer's perspective on the topic", "Logical argumentation has no place in philosophical essays",
            "This approach is unrelated to essay writing", "Philosophical essays should rely purely on unsupported assertion"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay on this theme discuss the risks of technological or scientific power without corresponding wisdom?", "options": [
            "It can illustrate the essay's argument that knowledge/capability without wisdom can be dangerous", "Technological power has no connection to this essay's likely argument",
            "This topic is unrelated to essays on knowledge and wisdom", "Such essays never connect their abstract argument to real-world consequence"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'ethical judgment' mean as a component potentially central to the essay's conception of wisdom?", "options": [
            "The capacity to discern right from wrong or good from harmful courses of action", "A term unrelated to philosophical writing",
            "A synonym for simply memorising moral rules", "A purely legal, not ethical, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes reasoning intended to build a persuasive, logical case?", "options": [
            "'Argumentation'", "'Photosynthesis'", "'Trigonometry'", "'Onomatopoeia'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might the essay argue that education should aim to cultivate wisdom, not just impart knowledge?", "options": [
            "This reflects a common philosophical concern that pure information transfer is insufficient for good judgment", "Education is argued to have no connection to either knowledge or wisdom",
            "This topic is unrelated to essays on this theme", "Such essays never make claims about educational purpose"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'objectivity' mean as a quality valued in this kind of philosophical/expository writing?", "options": [
            "Presenting reasoning based on logic and evidence rather than pure personal bias", "A term unrelated to philosophical essay writing",
            "A synonym for purely emotional argument", "The complete absence of any reasoning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay use historical or hypothetical examples to illustrate the difference between knowledge and wisdom?", "options": [
            "Concrete examples make an abstract philosophical distinction more understandable", "Examples have no illustrative value in philosophical writing",
            "This technique is unrelated to essay writing", "Such essays never use examples to support abstract claims"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of comprehension questions asking readers to explain the essay's central distinction in their own words?", "options": [
            "It tests genuine understanding of the philosophical argument, not just surface-level recall", "Paraphrasing an argument has no value for comprehension",
            "This question type is unrelated to essay analysis", "Philosophical essays never present a distinction worth explaining"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this essay remain relevant reading well beyond its original time of writing?", "options": [
            "Its exploration of a timeless human question about knowledge and good judgment retains broad relevance", "The essay has no lasting relevance to modern readers",
            "This appeal is unrelated to philosophical writing", "Only essays written very recently can be considered relevant"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'discernment' mean, a quality closely related to the essay's likely conception of wisdom?", "options": [
            "The ability to judge well and distinguish soundly between options or ideas", "A term unrelated to philosophical writing",
            "A synonym for simply accumulating information", "A purely legal or procedural concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might the essay be considered a good example of clear, persuasive expository writing for students to study?", "options": [
            "It likely models how to build and support a reasoned argument on an abstract topic clearly", "Philosophical essays are never useful models for expository writing skill",
            "This topic is unrelated to studying essay-writing technique", "Clarity has no connection to studying persuasive writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is Bertrand Russell often studied as a significant 20th-century intellectual figure?", "options": [
            "His extensive work across philosophy, logic, and public writing is widely recognised as influential", "Russell had no significant influence on 20th-century thought",
            "This reputation is unrelated to why his essays are studied", "Russell is studied only for unrelated biographical details"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying a philosophical essay on knowledge and wisdom valuable within a broader English curriculum?", "options": [
            "It builds both expository reading skills and engagement with significant intellectual questions", "Philosophical essays have no place in an English curriculum",
            "This topic is unrelated to English language and literature study", "Such essays are studied only for their vocabulary, not their ideas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Knowledge and Wisdom' in an English course is to:", "options": [
            "Develop analytical skills around philosophical argument while considering a significant intellectual distinction", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on abstract or philosophical topics", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37558: [  # Humility
        {"q": "'Humility' is best classified as which type of text?", "options": [
            "A reflective/expository essay", "A one-act comic play", "A formal legal contract", "A travel itinerary"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the essay's title suggest its central focus will be?", "options": [
            "An exploration of the quality of humility as a personal or ethical value", "A purely technical scientific description",
            "An unrelated discussion of economic policy", "A description of a fictional adventure story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'humility' generally mean as a personal quality?", "options": [
            "A modest view of one's own importance, without excessive pride or arrogance", "Excessive pride and self-importance",
            "A term unrelated to personal character", "Complete lack of self-worth or self-respect"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay distinguish humility from low self-esteem?", "options": [
            "Humility is often framed as a balanced, secure perspective, not the same as feeling worthless", "Humility and low self-esteem are argued to be identical concepts",
            "This distinction is unrelated to essays about humility", "Such essays never clarify what humility does or does not mean"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay argue that humility supports learning and personal growth?", "options": [
            "Acknowledging one's limitations can open a person to new knowledge and self-improvement", "Humility is argued to have no connection to learning or growth",
            "This topic is unrelated to essays on this theme", "Such essays never connect humility to personal development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is the purpose of an essay exploring humility's role in healthy relationships?", "options": [
            "To examine how humility can foster empathy, cooperation, and mutual respect between people", "Humility is argued to have no connection to relationships",
            "This topic is unrelated to essays on this theme", "Such essays never connect humility to interpersonal life"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay discuss the difference between genuine humility and false modesty?", "options": [
            "To distinguish sincere humility from performative self-deprecation that may not reflect real character", "This distinction is never made in essays on humility",
            "False modesty and genuine humility are argued to be identical", "This topic is unrelated to essays exploring character traits"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'ethical virtue' mean, a concept potentially relevant to how the essay frames humility?", "options": [
            "A morally valuable character trait considered admirable or beneficial", "A term unrelated to essays on personal qualities",
            "A purely legal classification with no connection to character", "A synonym for a moral flaw or vice"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay on humility discuss examples of leaders or figures admired for this quality?", "options": [
            "Concrete examples can illustrate the abstract value of humility in action", "Examples have no illustrative role in essays about character",
            "This technique is unrelated to essay writing", "Such essays never reference examples of humble figures"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What vocabulary term describes writing exploring an abstract personal or ethical quality?", "options": [
            "'Reflective'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay argue that humility and confidence are not necessarily opposites?", "options": [
            "A person can be humble about their limitations while still being secure and confident in their abilities", "Humility and confidence are argued to always be mutually exclusive",
            "This distinction is unrelated to essays about character", "Such essays never explore the relationship between these two qualities"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'self-awareness' mean, a quality often connected to humility in reflective essays?", "options": [
            "An accurate, honest understanding of one's own strengths and limitations", "A term unrelated to essays on personal character",
            "A synonym for excessive self-criticism", "A purely academic term with no personal application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay discuss cultural or philosophical traditions that particularly value humility?", "options": [
            "Different traditions can offer varied, informative perspectives on why humility is considered valuable", "Cultural traditions have no connection to essays about humility",
            "This topic is unrelated to essays on this theme", "Only one single cultural view of humility exists worth discussing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of comprehension questions asking readers to explain why the essay values humility?", "options": [
            "It tests understanding of the essay's central argument and supporting reasoning", "Such questions have no value for comprehension",
            "This question type is unrelated to essay analysis", "Essays on humility never present reasoning worth explaining"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay caution against the dangers of excessive pride or arrogance as a contrast to humility?", "options": [
            "Contrasting humility with its opposite can sharpen the argument for why humility is valuable", "Pride and arrogance are never discussed in essays about humility",
            "This contrast is unrelated to essay-writing technique", "Such essays never critique the opposite of their central value"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'reflective essay' mean as a genre relevant to this piece?", "options": [
            "A piece of writing exploring the writer's thoughts and insights on a topic", "A purely factual, unemotional report",
            "A term unrelated to essay writing", "A synonym for a strictly persuasive argument with no reflection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this essay be considered relevant to students navigating academic and social life?", "options": [
            "Reflecting on humility can support healthier learning attitudes and relationships with peers", "This essay has no relevance to students' daily lives",
            "This connection is unrelated to studying the essay", "Humility has no bearing on how students engage with school or peers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'ethical reflection' mean as a broader category this essay likely belongs to?", "options": [
            "Thoughtful consideration of moral values and how they should guide behaviour", "A term unrelated to essays on personal character",
            "A purely legal, not ethical, form of analysis", "A synonym for purely factual, non-evaluative writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying an essay on a personal virtue like humility valuable within an English curriculum?", "options": [
            "It builds reading and reflective skills alongside consideration of values relevant to personal growth", "Such essays have no educational value",
            "This topic is inappropriate for an English curriculum", "Essays about character traits are unrelated to language learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Humility' in an English course is to:", "options": [
            "Develop reflective reading skills while engaging with a significant personal and ethical value", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on character or values", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37559: [  # Human Rights and the Age of Inequality
        {"q": "'Human Rights and the Age of Inequality' is best classified as which type of text?", "options": [
            "An expository/persuasive essay on a contemporary social issue", "A one-act comic play", "A personal travel memoir", "A legal contract"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title suggest the essay's central concern will be?", "options": [
            "The relationship between fundamental human rights and rising social/economic inequality", "A purely technical scientific description",
            "An unrelated discussion of ancient mythology", "A description of a fictional adventure story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What are 'human rights', a foundational concept for this essay?", "options": [
            "Fundamental rights and freedoms believed to belong to every person", "Rights granted only to a select few by governments",
            "A term unrelated to legal or ethical discussion", "Privileges that can be freely revoked without reason"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does 'economic inequality' mean, a key term in this essay's title?", "options": [
            "Unequal distribution of wealth, income, or resources among individuals or groups", "Complete equality of wealth across all individuals",
            "A term unrelated to social or economic analysis", "A purely legal classification with no economic dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay argue that inequality can threaten the practical realisation of human rights?", "options": [
            "Significant economic disparity can limit meaningful access to rights like education, healthcare, or political voice", "Inequality is argued to have no connection to human rights",
            "This topic is unrelated to essays on this theme", "Such essays never connect economic and rights-based concerns"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of citing statistics or examples of global inequality in a persuasive essay on this theme?", "options": [
            "To provide concrete evidence supporting the essay's argument about the scale of the issue", "Statistics are irrelevant to essays on social issues",
            "This technique is unrelated to persuasive/expository writing", "Such essays never cite any supporting evidence"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay discuss the role of policy or institutions in addressing inequality?", "options": [
            "Structural and policy-level solutions are often argued to be necessary alongside individual awareness", "Policy has no connection to addressing inequality",
            "This topic is unrelated to essays on this theme", "Such essays argue inequality can never be meaningfully addressed"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social justice' mean, a concept closely related to this essay's likely themes?", "options": [
            "Fair and equitable distribution of rights, opportunities, and resources within a society", "A term unrelated to essays on human rights",
            "A purely legal term with no ethical dimension", "A synonym for unrestrained inequality"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this essay discuss both civil/political rights and economic/social rights?", "options": [
            "A fuller discussion of human rights often includes both categories, showing their interconnection", "Civil and economic rights are argued to be entirely unrelated concepts",
            "This topic is unrelated to essays about human rights", "Such essays only ever discuss one narrow category of rights"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes writing intended to persuade using evidence and reasoning?", "options": [
            "'Persuasive'", "'Trigonometry'", "'Photosynthesis'", "'Onomatopoeia'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might an essay on this theme discuss global versus local perspectives on inequality?", "options": [
            "Inequality manifests differently across contexts, and both scales offer useful perspective", "Global and local perspectives are argued to always be identical",
            "This topic is unrelated to essays on this theme", "Such essays only ever discuss a single, narrow geographic scope"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'systemic inequality' mean as a concept potentially explored in this essay?", "options": [
            "Inequality embedded within institutions and social structures, rather than isolated individual cases", "A term unrelated to essays about social issues",
            "A synonym for inequality caused only by individual choices", "A purely legal term with no structural dimension"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might an essay balance a critique of inequality with proposed solutions or a hopeful outlook?", "options": [
            "A balanced approach can make an argument feel constructive rather than purely critical", "Essays on inequality never propose any solutions",
            "This balance is unrelated to persuasive essay writing", "Such essays must always end on an entirely negative note"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the purpose of comprehension questions asking readers to identify the essay's proposed solutions or recommendations?", "options": [
            "It tests understanding of the essay's constructive argument, not just its critique", "Identifying proposed solutions has no value for comprehension",
            "This question type is unrelated to essay analysis", "Persuasive essays on this theme never propose solutions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an essay reference international frameworks (e.g. the Universal Declaration of Human Rights) when discussing this topic?", "options": [
            "Such frameworks provide a recognised standard supporting the essay's argument about human rights", "International frameworks are irrelevant to essays on human rights",
            "This topic is unrelated to essays on this theme", "Such essays never reference any international standards"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'marginalised groups' mean, a term potentially relevant to discussions of inequality?", "options": [
            "Groups who face systemic disadvantage or reduced access to resources and opportunity", "A term unrelated to essays about inequality",
            "A synonym for the wealthiest members of society", "A purely legal classification with no social dimension"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this essay be considered especially relevant for students studying English in the contemporary world?", "options": [
            "It engages with pressing, real-world social issues relevant to informed citizenship", "This essay has no relevance to contemporary students",
            "This connection is unrelated to studying the essay", "Social issues are considered irrelevant to English language education"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'advocacy' mean, a concept potentially connected to essays arguing for human rights protections?", "options": [
            "Active support or promotion of a cause, such as human rights protection", "A term unrelated to essays on this theme",
            "A purely legal classification with no connection to persuasive writing", "A synonym for opposition to a cause"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying a persuasive essay on human rights and inequality valuable within an English curriculum?", "options": [
            "It builds critical reading and argumentative analysis skills while engaging with a significant global issue", "Such essays have no educational value",
            "This topic is inappropriate for an English curriculum", "Essays about social issues are unrelated to language learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Human Rights and the Age of Inequality' in an English course is to:", "options": [
            "Build critical reading and argument-analysis skills while engaging with a significant contemporary issue", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with essays on social or political topics", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37560: [  # A Day
        {"q": "'A Day' is best classified, given its concise title, as most likely which literary form?", "options": [
            "A poem", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a poem with a simple, everyday title like 'A Day' focus on ordinary experience?", "options": [
            "It can find deeper meaning or reflection within the seemingly unremarkable events of daily life", "Ordinary experience is never a subject explored in poetry",
            "This technique is unrelated to poetic themes", "Such titles always signal an entirely fantastical, unrealistic subject"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What literary device might a poem about a single day use to structure its progression?", "options": [
            "A chronological structure following events from morning to night, or a similar temporal arc", "A structure with no reference to time at all",
            "A term unrelated to poetic structure", "A purely random, unordered structure with no discernible pattern"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem reflecting on 'a day' use precise, sensory imagery?", "options": [
            "Vivid sensory detail can make an ordinary experience feel immediate and meaningful to the reader", "Sensory imagery has no role in poetry about everyday experience",
            "This technique is unrelated to poetic analysis", "Descriptive detail always distracts from a poem's central theme"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'imagery' mean as a literary technique likely relevant to this poem?", "options": [
            "Descriptive language appealing to the senses to create a vivid impression", "A term unrelated to literary analysis",
            "A purely factual, non-descriptive style of writing", "A synonym for the poem's rhyme scheme only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem about a single day explore themes of the passage of time or mortality?", "options": [
            "A single day can serve as a microcosm reflecting on larger questions about time and life", "Poems about a single day never connect to broader themes",
            "This thematic connection is unrelated to poetic analysis", "Time and mortality are never explored through small, everyday moments in poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'microcosm' mean as a literary concept, potentially relevant to a poem using one day to reflect broader ideas?", "options": [
            "A small-scale representation of something larger or more general", "A term unrelated to literary analysis",
            "A synonym for a purely factual report", "A purely scientific term with no literary application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poem's tone shift subtly as it moves through the events of a described day?", "options": [
            "Tonal shifts can mirror changes in mood or perspective that naturally occur across a day's experiences", "Tone always remains completely static throughout a poem",
            "This technique is unrelated to poetic analysis", "Tonal shifts are never used meaningfully in poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'tone' mean when analysing a poem's emotional attitude toward its subject?", "options": [
            "The emotional attitude conveyed through the poem's language and imagery", "A term unrelated to poetic analysis",
            "Only the literal meaning of the words with no emotional layer", "A synonym for the poem's title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might close reading of a short, simply-titled poem be considered valuable for developing analytical skill?", "options": [
            "Even seemingly simple poems can reward careful attention to word choice and structure", "Simple poems never contain material worth close analysis",
            "This value is unrelated to literary study", "Only long, complex poems are worth close reading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What vocabulary term describes a poem's pattern of rhyming words at the ends of lines?", "options": [
            "'Rhyme scheme'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a poem about a day use present-tense narration rather than past tense?", "options": [
            "Present tense can create a sense of immediacy, as if events are unfolding as the reader reads", "Tense choice has no effect on a poem's impact",
            "This technique is unrelated to poetic narration", "Present tense is never used meaningfully in poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poem reflecting on daily routine explore themes of gratitude or appreciation?", "options": [
            "Attentive reflection on ordinary moments can lead to a renewed sense of appreciation for everyday life", "Gratitude is never a theme explored in poetry about daily life",
            "This thematic reading is unrelated to poetic analysis", "Ordinary routine has no connection to themes of appreciation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'free verse' mean as a poetic form potentially relevant to a reflective poem like this one?", "options": [
            "Poetry without a fixed metrical pattern or regular rhyme scheme", "A term unrelated to poetic form",
            "A synonym for poetry that must follow strict traditional rules", "A purely prose form with no connection to poetry"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this poem ask readers to identify its overall mood?", "options": [
            "Identifying mood tests the ability to connect imagery and word choice to overall emotional effect", "Mood has no relevance to understanding a short reflective poem",
            "This question type is unrelated to poetry analysis", "Such poems never create any discernible mood"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'reflective poetry' mean as a broader category this poem likely belongs to?", "options": [
            "Poetry that contemplates personal experience, thought, or observation", "A term unrelated to poetic categorisation",
            "A synonym for poetry focused only on external, factual description", "A purely narrative form with no reflective element"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might the poem's structure move through distinct moments (morning, afternoon, evening) within a day?", "options": [
            "It can mirror the natural rhythm and progression of daily experience", "Such structural choices have no connection to a poem's meaning",
            "This technique is unrelated to poetic structure", "Poems about a day never follow any structured temporal progression"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might reading and discussing poetry about everyday experience be valuable for students?", "options": [
            "It can encourage mindful attention to one's own daily life and surroundings", "Poetry about everyday experience has no educational value",
            "This topic is unrelated to studying poetry", "Only poetry about extraordinary or fantastical events is worth studying"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'observation' mean as a skill relevant to writing or appreciating a poem grounded in ordinary daily detail?", "options": [
            "Careful, attentive noticing of details, which can then be conveyed vividly in writing", "A term unrelated to poetic technique",
            "A synonym for guessing without any careful attention", "A purely scientific method with no literary application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'A Day' in an English course is to:", "options": [
            "Develop close-reading skills and appreciation for how poetry can find meaning in everyday experience", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with reflective or personal poetry", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37561: [  # Every Morning I Wake
        {"q": "'Every Morning I Wake' is best classified, given its title, as most likely which literary form?", "options": [
            "A poem", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title's reference to waking each morning suggest as a likely central theme?", "options": [
            "Reflection on daily renewal, routine, or the recurring nature of life", "A purely technical description of sleep science",
            "An unrelated discussion of economic policy", "A description of a fictional battle scene"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem use the daily act of waking as a metaphor for renewal or fresh possibility?", "options": [
            "Waking each day can symbolically represent a new chance or a continuing cycle of life", "Waking has no symbolic potential in poetry",
            "This technique is unrelated to poetic analysis", "Such metaphors are never used in reflective poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What literary device is at work when a repeated daily action (waking) is used to explore a larger idea about life?", "options": [
            "Symbolism", "A purely literal description with no figurative meaning", "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem with a first-person, present-tense title ('I Wake') create a sense of immediacy?", "options": [
            "It can make the reflection feel personal and ongoing, as if happening in real time", "First-person present tense has no effect on how a poem is experienced",
            "This technique is unrelated to poetic voice", "Present tense is never used meaningfully in reflective poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'repetition' as a poetic device (e.g. repeating 'every morning') typically achieve?", "options": [
            "It can create rhythm and emphasise the recurring, cyclical nature of an experience", "Repetition always weakens a poem's emotional impact",
            "This technique is unrelated to poetic structure", "Repeated phrases are never used meaningfully in poetry"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem reflecting on daily waking explore both routine and the possibility of change within that routine?", "options": [
            "It can hold in tension the comfort of habit alongside openness to something new each day", "Routine and change are never explored together in reflective poetry",
            "This thematic tension is unrelated to poetic analysis", "Poems about daily routine never touch on the idea of change"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'tone' mean when analysing this poem's attitude toward the recurring experience of waking?", "options": [
            "The emotional attitude conveyed through the poem's language and imagery", "A term unrelated to poetic analysis",
            "Only the literal meaning of the words with no emotional layer", "A synonym for the poem's title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this poem be read as an expression of gratitude or mindfulness about being alive each day?", "options": [
            "Reflecting on the simple act of waking can lead to appreciation for life and its continuation", "Gratitude is never explored in poems about daily routine",
            "This thematic reading is unrelated to poetic analysis", "Waking has no connection to themes of appreciation or mindfulness"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a poem's underlying meaning or central idea?", "options": [
            "'Theme'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a poem use short, simple lines to reflect a quiet, contemplative moment like waking?", "options": [
            "Simple, unadorned language can suit an intimate, reflective mood", "Simple lines always weaken a poem's emotional depth",
            "This technique is unrelated to poetic style", "Contemplative poems must always use long, complex sentence structures"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'free verse' mean as a poetic form potentially relevant to a reflective poem like this one?", "options": [
            "Poetry without a fixed metrical pattern or regular rhyme scheme", "A term unrelated to poetic form",
            "A synonym for poetry that must follow strict traditional rules", "A purely prose form with no connection to poetry"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this poem ask readers to consider what waking 'each morning' might symbolise?", "options": [
            "Interpreting a poem's central symbol is often key to understanding its deeper meaning", "Symbols in poetry carry no particular significance for comprehension",
            "This question type is unrelated to poetry analysis", "This poem contains no interpretable central image"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem about waking each day connect personal routine to broader reflections on resilience?", "options": [
            "Continuing to face each new day can be read as a quiet act of endurance or hope", "Resilience is never explored through the theme of daily waking",
            "This thematic connection is unrelated to poetic analysis", "Personal routine has no connection to broader ideas about endurance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'mindfulness' mean, a concept potentially relevant to a poem reflecting attentively on a daily experience?", "options": [
            "Present-moment awareness and attentiveness to one's experience", "A term unrelated to reflective poetry",
            "A synonym for distraction or inattentiveness", "A purely clinical, non-literary concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem be considered relatable to a wide range of readers?", "options": [
            "Waking each morning is a universal human experience that many readers share", "Waking is an experience unique to only a small number of readers",
            "This appeal is unrelated to why the poem might resonate broadly", "The poem's theme is considered irrelevant to most readers' lives"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'universal theme' mean, relevant to why this poem's subject might resonate broadly?", "options": [
            "An idea broadly relatable to human experience regardless of background", "A term unrelated to literary analysis",
            "A synonym for an idea relevant to only one narrow group", "A purely local, culturally specific concept with no wider relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem be paired thematically with other reflective works exploring time or daily life?", "options": [
            "It contributes to a broader exploration of how literature finds meaning in everyday, recurring experience", "This poem has no thematic connection to other reflective literature",
            "This pairing is unrelated to studying poetry thematically", "Poems about daily life can never meaningfully be compared to one another"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying a short reflective poem like this one valuable for developing close-reading skills?", "options": [
            "Its concise form requires careful attention to how each word and image contributes to meaning", "Short poems have no value for developing close-reading skills",
            "This value is unrelated to literary study", "Only long, complex poems are worth close, careful reading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Every Morning I Wake' in an English course is to:", "options": [
            "Develop close-reading skills and appreciation for reflective poetry grounded in everyday experience", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with reflective or personal poetry", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37562: [  # I Was My Own Route
        {"q": "'I Was My Own Route' is best classified, given its title, as most likely which literary form?", "options": [
            "A poem", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title 'I Was My Own Route' suggest as a likely central theme?", "options": [
            "Personal self-determination and forging one's own path in life", "A purely technical description of geographic navigation",
            "An unrelated discussion of economic policy", "A description of a fictional battle scene"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What literary device is at work when a person's life journey is compared to a 'route' or path?", "options": [
            "Metaphor", "A purely literal, non-figurative statement", "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a first-person poem asserting 'I was my own route' be read as expressing independence or self-authorship?", "options": [
            "The declarative, first-person framing suggests the speaker claiming agency over their own life direction", "First-person declarative statements never convey a sense of independence",
            "This reading is unrelated to poetic interpretation", "The title suggests dependence on others rather than self-direction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'self-determination' mean as a theme potentially central to this poem?", "options": [
            "The capacity to make one's own choices and shape one's own life course", "A term unrelated to poetic themes",
            "A synonym for being entirely controlled by external forces", "A purely legal or political classification only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poem asserting personal agency use strong, declarative first-person statements?", "options": [
            "Direct, assertive language can powerfully convey a sense of self-ownership and confidence", "Declarative statements always weaken a poem's emotional impact",
            "This technique is unrelated to poetic voice", "Assertive language is never used meaningfully in poetry about identity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'tone' mean when analysing this poem's likely confident or assertive attitude?", "options": [
            "The emotional attitude conveyed through the poem's language and imagery", "A term unrelated to poetic analysis",
            "Only the literal meaning of the words with no emotional layer", "A synonym for the poem's title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem about self-determination be especially meaningful when considering barriers a speaker may have faced?", "options": [
            "Asserting one's own path can carry particular significance if written against social or personal constraints", "Overcoming barriers is never a relevant context for such poems",
            "This thematic reading is unrelated to poetic analysis", "Self-determination poems never engage with any social context"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the effect of using the past tense ('was') combined with a present sense of identity in the title?", "options": [
            "It can suggest reflecting on a journey already taken while affirming its lasting significance to who the speaker is", "Past tense has no effect on how a poem's meaning is conveyed",
            "This technique is unrelated to poetic analysis", "Past tense always removes any connection between the poem and the present"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a comparison between two unlike things without using 'like' or 'as'?", "options": [
            "'Metaphor'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a poem use the extended image of a 'route' or journey throughout its structure?", "options": [
            "Sustaining a single central metaphor can unify the poem's exploration of a broader idea about life", "Extended metaphors are never used to structure a poem",
            "This technique is unrelated to poetic structure", "A sustained metaphor always confuses rather than clarifies a poem's meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem be read as challenging external expectations or a path chosen by others?", "options": [
            "Asserting one's 'own route' can imply a contrast with a path that might have been expected or imposed", "This reading has no connection to the poem's likely theme",
            "This interpretation is unrelated to poetic analysis", "The poem's title suggests total conformity to external expectation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'agency' mean, a concept closely related to this poem's likely central theme?", "options": [
            "The capacity to act independently and make one's own choices", "A term unrelated to poetic themes of identity",
            "A synonym for complete lack of control over one's life", "A purely legal or bureaucratic term only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this poem ask readers to interpret the central metaphor of a 'route'?", "options": [
            "Interpreting a poem's central metaphor is often key to understanding its deeper meaning", "Metaphors in poetry carry no particular significance for comprehension",
            "This question type is unrelated to poetry analysis", "This poem contains no interpretable central image"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this poem be considered empowering, particularly to readers who have faced obstacles to self-direction?", "options": [
            "Its assertive declaration of self-authorship can resonate as affirming and inspiring", "The poem's theme has no connection to empowerment",
            "This reading is unrelated to poetic interpretation", "Poems about personal agency are never considered empowering"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'identity' mean as a broader theme this poem likely explores through its central metaphor?", "options": [
            "A sense of who one is, shaped by one's choices, values, and experiences", "A term unrelated to poetic themes",
            "A purely legal classification with no personal dimension", "A synonym for total conformity to external expectation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem's brevity (if short) intensify the impact of its central declarative statement?", "options": [
            "A concise form can give a bold personal statement more focused, memorable weight", "Brevity always weakens the impact of an assertive statement",
            "This technique is unrelated to poetic form", "Only long poems can meaningfully convey a strong personal statement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem be considered relevant to students reflecting on their own life choices and independence?", "options": [
            "Its theme of charting one's own path can resonate with readers navigating their own decisions", "This poem has no relevance to students' lives",
            "This connection is unrelated to studying the poem", "Themes of self-determination are considered irrelevant to student readers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is studying a poem centred on a strong personal declaration valuable for developing interpretive skill?", "options": [
            "It encourages careful attention to how tone, metaphor, and voice combine to convey a powerful personal statement", "Such poems have no value for developing interpretive skill",
            "This value is unrelated to literary study", "Poems about personal identity are considered too simple for serious analysis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'I Was My Own Route' in an English course is to:", "options": [
            "Develop skills in analysing metaphor and voice through a poem centred on self-determination", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with poetry about identity or personal agency", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37563: [  # The Awakening Age
        {"q": "'The Awakening Age' is best classified, given its title, as most likely which literary form?", "options": [
            "A poem", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title 'The Awakening Age' suggest as a likely central theme?", "options": [
            "A period of growing awareness, change, or transformation", "A purely technical description of a historical dating system",
            "An unrelated discussion of economic trade statistics", "A description of a fictional battle scene"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What literary device is at work when 'awakening' is used to describe growing awareness rather than literally waking from sleep?", "options": [
            "Metaphor", "A purely literal, non-figurative statement", "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem use the metaphor of 'awakening' to describe social or personal change?", "options": [
            "Awakening evokes a vivid sense of newly gained awareness or understanding, apt for describing transformation", "Awakening has no symbolic potential in poetry",
            "This technique is unrelated to poetic analysis", "Such metaphors are never used to describe change or transformation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does the phrase 'the age' in the title suggest about the poem's scope?", "options": [
            "The poem may reflect on a broader era or period, not just an individual moment", "The poem is necessarily about a single day only",
            "This phrase has no bearing on the poem's likely scope", "'Age' in this context refers only to a person's numerical age"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poem about an 'awakening age' explore themes of collective or societal change?", "options": [
            "The framing suggests reflection on a broader shift affecting more than just one individual", "Such poems never connect personal awakening to broader societal themes",
            "This thematic connection is unrelated to poetic analysis", "The poem's scope is necessarily limited only to private, individual experience"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'transformation' mean as a literary theme, relevant to a poem about an 'awakening'?", "options": [
            "A significant change in form, character, or circumstance", "A term unrelated to poetic themes",
            "A synonym for complete stagnation with no change", "A purely legal or bureaucratic concept only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem on this theme use imagery of light or dawn to reinforce the idea of awakening?", "options": [
            "Light and dawn imagery conventionally symbolise new understanding, hope, or beginning", "Light imagery has no symbolic connection to the idea of awakening",
            "This technique is unrelated to poetic analysis", "Dawn imagery is never used to represent change or new beginnings"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'imagery' mean as a literary technique likely central to this poem?", "options": [
            "Descriptive language appealing to the senses to create a vivid impression", "A term unrelated to literary analysis",
            "A purely factual, non-descriptive style of writing", "A synonym for the poem's rhyme scheme only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem about a broader 'age' of awakening carry a hopeful or optimistic tone?", "options": [
            "Reflecting on newfound awareness or change often carries a sense of possibility and hope", "Such poems are always written in an entirely pessimistic tone",
            "This tonal choice is unrelated to poetic analysis", "Hope is never associated with themes of awakening or change in poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a poem's underlying meaning or central idea?", "options": [
            "'Theme'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might such a poem be read as addressing generational or societal shifts in awareness (e.g. about social issues)?", "options": [
            "Framing change as an 'awakening age' can reflect on how understanding evolves across a broader period or generation", "Generational shifts are never connected to poetic themes of awakening",
            "This thematic reading is unrelated to poetic analysis", "The poem's theme necessarily excludes any connection to social change"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'symbolism' mean as a literary technique potentially central to this poem's exploration of change?", "options": [
            "The use of an object, image, or event to represent a deeper meaning", "A term unrelated to literary analysis",
            "A purely decorative element with no meaning", "A synonym for literal, non-figurative description"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this poem ask readers to interpret what 'awakening' represents in context?", "options": [
            "Interpreting a poem's central metaphor is often key to understanding its deeper meaning", "Metaphors in poetry carry no particular significance for comprehension",
            "This question type is unrelated to poetry analysis", "This poem contains no interpretable central image"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this poem be considered relevant to discussions of progress or social consciousness?", "options": [
            "Its theme of awakening awareness connects naturally to ideas about societal progress and change", "This poem has no thematic connection to social progress",
            "This reading is unrelated to poetic interpretation", "Themes of awakening are never connected to broader social discussion"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'consciousness' mean, a concept potentially relevant to a poem about growing awareness?", "options": [
            "Awareness or perception of one's surroundings, thoughts, or a broader reality", "A term unrelated to reflective poetry",
            "A purely medical/clinical term with no literary application", "A synonym for total unawareness"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poem's structure move from an initial state of unawareness toward eventual clarity or realisation?", "options": [
            "This progression can mirror the very process of 'awakening' the poem's title describes", "Such structural progression has no connection to the poem's theme",
            "This technique is unrelated to poetic structure", "Poems about awakening never follow any progression toward clarity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might reading and discussing poetry about societal or personal awakening be valuable for students?", "options": [
            "It can encourage reflection on how awareness and understanding develop over time", "Such poetry has no educational value",
            "This topic is unrelated to studying poetry", "Only poetry with no thematic depth is considered worth studying"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is studying a poem centred on an abstract theme like 'awakening' valuable for developing interpretive skill?", "options": [
            "It requires readers to move beyond literal meaning to interpret symbolic and thematic significance", "Abstract themes have no value for developing interpretive skill",
            "This value is unrelated to literary study", "Poems about abstract themes are considered too simple for serious analysis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'The Awakening Age' in an English course is to:", "options": [
            "Develop skills in analysing symbolism and theme through a poem centred on change and awareness", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with poetry about change or transformation", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37564: [  # Soft Storm
        {"q": "'Soft Storm' is best classified, given its title, as most likely which literary form?", "options": [
            "A poem", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What literary device is at work in the title 'Soft Storm', combining two seemingly contradictory words?", "options": [
            "Oxymoron (a figure of speech combining contradictory terms)", "A purely literal, non-figurative description",
            "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is an 'oxymoron' as a literary device?", "options": [
            "A figure of speech that combines two normally contradictory terms for effect", "A term unrelated to figurative language",
            "A synonym for a simple, literal description", "A device used only in comedic writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poet pair contradictory words like 'soft' and 'storm' in a title?", "options": [
            "It can create tension and complexity, suggesting an experience that is both gentle and turbulent at once", "Such pairing has no thematic or stylistic purpose",
            "This technique is unrelated to poetic titling", "Contradictory word pairing always confuses readers with no artistic value"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What might the image of a 'storm' conventionally symbolise in poetry?", "options": [
            "Turbulence, conflict, or intense emotion", "Purely calm and untroubled conditions",
            "A term unrelated to symbolic imagery", "A synonym for stability and predictability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might describing a storm as 'soft' complicate or deepen this conventional symbolism?", "options": [
            "It suggests an emotional experience with both gentle and intense qualities simultaneously", "This combination removes all meaning from the storm imagery",
            "This technique is unrelated to poetic complexity", "Softness and storms can never be meaningfully combined in poetic imagery"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'imagery' mean as a literary technique likely central to this poem's title and content?", "options": [
            "Descriptive language appealing to the senses to create a vivid impression", "A term unrelated to literary analysis",
            "A purely factual, non-descriptive style of writing", "A synonym for the poem's rhyme scheme only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem use weather imagery (like a storm) to reflect internal emotional states?", "options": [
            "Weather is a common poetic device for externalising and conveying inner feeling", "Weather imagery has no connection to conveying emotion in poetry",
            "This technique is unrelated to poetic analysis", "Such imagery is used only in scientific, non-literary writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'pathetic fallacy' mean as a device potentially relevant to weather-based emotional imagery?", "options": [
            "Attributing human emotion to nature or the natural environment", "A term unrelated to literary technique",
            "A synonym for a purely factual meteorological description", "A device used only in comedic writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem's tone shift or hold multiple emotional qualities simultaneously, mirroring its 'soft storm' title?", "options": [
            "Complex emotional experiences are often not purely one thing, and poetic tone can reflect that nuance", "A poem's tone must always remain singular and uncomplicated",
            "This technique is unrelated to poetic analysis", "Tonal complexity is never used meaningfully in poetry"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes language that appeals to the reader's senses?", "options": [
            "'Imagery'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might comprehension questions on this poem ask readers to interpret the significance of its contradictory title?", "options": [
            "Interpreting a poem's central image or paradox is often key to understanding its deeper meaning", "Titles carry no particular significance for comprehension",
            "This question type is unrelated to poetry analysis", "This poem's title has no interpretable meaning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a poem exploring paradoxical emotion (calm and turbulent at once) resonate with readers' own complex experiences?", "options": [
            "Human emotion is often genuinely mixed or contradictory, making such imagery relatable", "Human emotion is always simple and singular, never mixed",
            "This resonance is unrelated to poetic interpretation", "Contradictory emotional imagery has no connection to lived experience"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'paradox' mean as a broader literary concept relevant to this poem's title?", "options": [
            "A statement or situation that seems contradictory but may reveal a deeper truth", "A term unrelated to literary analysis",
            "A synonym for a straightforward, uncomplicated statement", "A purely logical or mathematical term only"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a poet choose an evocative, image-based title (like 'Soft Storm') rather than a purely descriptive one?", "options": [
            "An evocative title can intrigue the reader and hint at the poem's emotional complexity before it is even read", "Evocative titles have no effect on how a poem is approached by readers",
            "This choice is unrelated to poetic titling", "Descriptive, literal titles are always considered more effective than evocative ones"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'connotation' mean, relevant to why 'storm' carries emotional weight beyond its literal meteorological meaning?", "options": [
            "The implied or associated meaning of a word beyond its literal definition", "A term unrelated to poetic language",
            "A synonym for a word's dictionary definition alone", "A purely grammatical concept with no connection to meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this poem be considered a good example for teaching students about oxymoron and paradox?", "options": [
            "Its title directly demonstrates how contradictory terms can create rich poetic meaning", "This poem has no useful connection to teaching these devices",
            "This educational use is unrelated to literary study", "Oxymoron and paradox are never usefully illustrated through poetry titles"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is close attention to word choice especially important when analysing a title as compact as 'Soft Storm'?", "options": [
            "In a very short title, each word carries significant interpretive weight", "Word choice in titles has no bearing on a poem's meaning",
            "This analytical approach is unrelated to studying poetry", "Titles should never be closely analysed, only the poem's body text"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might reading poetry that captures emotional complexity (rather than simple, single emotions) be valuable for students?", "options": [
            "It can build appreciation for nuance and the layered nature of real human feeling", "Emotional complexity has no educational value in poetry study",
            "This topic is unrelated to studying poetry", "Only poems expressing simple, singular emotions are worth studying"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Soft Storm' in an English course is to:", "options": [
            "Develop skills in analysing paradox, imagery, and emotional nuance in poetry", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with poetry exploring complex or contradictory emotion", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37565: [  # Neighbors
        {"q": "'Neighbors' is best classified as which literary genre?", "options": [
            "A short story", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Neighbors' is widely attributed to Raymond Carver, a writer associated with which literary tradition?", "options": [
            "20th-century American short fiction, particularly known for minimalist style", "Ancient Roman epic poetry",
            "Contemporary Nepali drama", "Medieval English romance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Carver is broadly recognised in literary history for pioneering which distinctive prose style?", "options": [
            "'Minimalism' - spare, understated prose with restrained description", "Highly ornate, elaborate prose with extensive description",
            "A term unrelated to his literary reputation", "Exclusively comedic, exaggerated narrative voice"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The story's title, 'Neighbors', suggests it centrally explores which kind of relationship or setting?", "options": [
            "The dynamic between people living close to one another, such as in adjoining apartments or houses", "A purely historical account of urban planning",
            "An unrelated legal dispute over property lines", "A description of a natural wilderness setting"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What literary quality is minimalist short fiction, the style broadly associated with Carver, generally known for?", "options": [
            "Suggesting deeper meaning through what is left unsaid, rather than explicit explanation", "Explaining every character's motivation in extensive detail",
            "A term unrelated to short story technique", "Avoiding any subtlety or implication whatsoever"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story about neighbours explore themes of curiosity or voyeurism regarding another person's life?", "options": [
            "Close physical proximity can create opportunities for characters to become curious about others' private lives", "Curiosity about others has no connection to stories about neighbours",
            "This thematic focus is unrelated to short fiction", "Neighbours in fiction never take an interest in each other's lives"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'subtext' mean, a concept especially relevant to minimalist fiction where meaning is often implied?", "options": [
            "Meaning conveyed beneath the surface of what is explicitly stated in dialogue or narration", "A term unrelated to literary analysis",
            "A synonym for a story's literal plot summary", "A purely grammatical concept with no connection to meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might Carver's fiction often focus on ordinary, everyday domestic settings and situations?", "options": [
            "His work is widely recognised for finding significance and tension within seemingly mundane, everyday life", "His fiction is known for avoiding any domestic or everyday settings",
            "This focus is unrelated to his body of work", "Ordinary settings are never used meaningfully in his fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'restrained narration' mean as a technique associated with minimalist short fiction?", "options": [
            "A narrative voice that avoids excessive emotional commentary, letting actions and dialogue speak for themselves", "A narrative voice that explains every character's feeling explicitly",
            "A term unrelated to narrative technique", "A style used only in highly emotional, expressive fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is Carver often credited as an influential figure in the development of the modern American short story?", "options": [
            "His minimalist technique significantly influenced later short story writers and the genre's direction", "Carver had no significant influence on short fiction as a genre",
            "This reputation is unrelated to literary history", "The modern short story developed with no connection to his work"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a writing style using very few words to convey meaning?", "options": [
            "'Minimalist'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a minimalist story about neighbours leave certain character motivations ambiguous or unexplained?", "options": [
            "Ambiguity can invite the reader's own interpretation and reflect the uncertainty of real-life understanding of others", "Ambiguity is never used deliberately in short fiction",
            "This technique is unrelated to minimalist style", "Minimalist fiction always explains every motivation explicitly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the effect of using plain, everyday dialogue in a story exploring domestic relationships?", "options": [
            "It can make the characters and their situation feel authentic and relatable", "Plain dialogue always makes a story less effective",
            "This technique is unrelated to Carver's narrative style", "Everyday dialogue is never used meaningfully in serious fiction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this story ask readers to infer what a character is feeling, since it may not be stated directly?", "options": [
            "Minimalist fiction often requires readers to infer emotion and meaning from action and implication", "Inference has no relevance to reading minimalist fiction",
            "This question type is unrelated to studying this story", "Characters' feelings are always explicitly stated in this style of fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'characterisation through action' mean, a technique especially relevant to minimalist short fiction?", "options": [
            "Revealing a character's personality primarily through what they do rather than lengthy description", "A term unrelated to narrative technique",
            "A synonym for revealing character only through direct authorial statement", "Ignoring character development in favour of plot alone"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story titled 'Neighbors' explore boundaries - physical, social, or ethical - between people?", "options": [
            "The theme of neighbours naturally invites reflection on where personal boundaries lie between close but separate lives", "Boundaries have no thematic connection to a story about neighbours",
            "This thematic reading is unrelated to literary analysis", "Stories about neighbours never explore any sense of boundary or separation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying minimalist fiction like Carver's valuable for developing close-reading skills?", "options": [
            "It requires careful attention to implication and subtext rather than relying on explicit statement", "Minimalist fiction requires no particular close-reading skill",
            "This value is unrelated to studying short fiction", "Only elaborate, highly descriptive fiction rewards close reading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'irony' mean, a device potentially relevant to a story exploring the gap between how neighbours appear and their private realities?", "options": [
            "A contrast between appearance and underlying reality", "A term unrelated to this story's themes",
            "A synonym for a story with no unexpected element", "A purely comedic device with no serious application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why has Carver's short fiction remained widely studied and anthologised internationally?", "options": [
            "His distinctive style and influence on the short story form are broadly recognised in literary study", "Carver's work has no lasting literary reputation",
            "This recognition is unrelated to literary study", "He is studied only for biographical, not literary, reasons"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'Neighbors' in an English course is to:", "options": [
            "Develop close-reading skills around subtext and minimalist narrative technique", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with stories exploring domestic or everyday themes", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37566: [  # A Respectable Woman
        {"q": "'A Respectable Woman' is best classified as which literary genre?", "options": [
            "A short story", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'A Respectable Woman' is widely attributed to Kate Chopin, a writer associated with which literary tradition?", "options": [
            "Late 19th-century American literature", "Ancient Greek epic poetry",
            "Contemporary Nepali fiction", "Medieval Japanese drama"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Kate Chopin is broadly recognised in literary history for exploring which recurring theme in much of her fiction?", "options": [
            "Women's inner lives, desires, and constraints within societal expectations of the period", "Purely technical scientific subjects with no social dimension",
            "A term unrelated to her literary reputation", "Exclusively comedic, lighthearted subjects with no deeper meaning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The story's title, 'A Respectable Woman', invites the reader to consider which broader social concept?", "options": [
            "Social expectations and norms placed on women's behaviour, particularly regarding 'respectability'", "A purely legal definition of citizenship",
            "An unrelated discussion of financial management", "A description of a fictional adventure across continents"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What literary technique might a story with an ironic or pointed title (like 'A Respectable Woman') use to invite deeper reflection?", "options": [
            "Irony, prompting the reader to question or reconsider the surface meaning of the title", "A purely literal title with no invitation to interpretation",
            "A term unrelated to literary titling", "Titles in this period never carried any interpretive weight"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story exploring a woman's internal conflict use close attention to her private thoughts and feelings?", "options": [
            "It can reveal the tension between social expectation and personal desire or perspective", "Internal thought has no role in exploring social themes",
            "This technique is unrelated to Chopin's narrative style", "Such stories never explore any internal psychological dimension"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social constraint' mean as a theme potentially relevant to this story?", "options": [
            "Limitations placed on individual behaviour or choice by societal norms and expectations", "A term unrelated to literary themes",
            "A synonym for complete personal freedom with no social limitation", "A purely legal, not social, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is Chopin often studied as a significant figure in the development of American literature exploring women's experience?", "options": [
            "Her work is widely recognised for nuanced portrayals of women's inner lives within their social context", "Chopin had no significant literary influence",
            "This reputation is unrelated to literary history", "Chopin is studied only for biographical, not literary, reasons"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'psychological realism' mean as a literary approach, relevant to Chopin's attention to characters' inner experience?", "options": [
            "A style depicting characters' inner thoughts and emotions with careful, realistic detail", "A term unrelated to Chopin's literary style",
            "A synonym for pure fantasy with no connection to real psychology", "A purely scientific method with no literary application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a contrast between what is stated or expected and the underlying reality?", "options": [
            "'Irony'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story from this literary period explore a woman navigating desire against social expectation?", "options": [
            "It reflects broader historical conversations about women's roles and personal autonomy during that era", "Such themes have no connection to literature from this period",
            "This thematic focus is unrelated to Chopin's body of work", "Desire and social expectation are never explored together in this era's fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What is the effect of an ambiguous or open-ended conclusion, a technique sometimes used in short fiction exploring internal conflict?", "options": [
            "It can leave the reader to reflect on the character's unresolved tension rather than providing a tidy resolution", "Open endings always weaken a story exploring internal conflict",
            "This technique is unrelated to short fiction structure", "Stories exploring inner conflict must always resolve every tension explicitly"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this story ask readers to consider the significance of its title in relation to the plot?", "options": [
            "Understanding how the title relates ironically or thematically to events is often key to interpreting the story", "The title has no relevance to comprehension of the story",
            "This question type is unrelated to studying short fiction", "Titles in this period of literature never carry thematic significance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might Chopin's work be considered ahead of its time in exploring women's inner experience?", "options": [
            "Her nuanced attention to women's psychology was notable within the literary conventions of her era", "Her work is considered entirely conventional for its time with no notable distinction",
            "This reading is unrelated to literary history", "Chopin's work avoided any exploration of women's inner lives"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'autonomy' mean, a concept potentially relevant to a story examining a woman's personal choices against social expectation?", "options": [
            "The capacity for self-governance and independent decision-making", "A term unrelated to literary themes of this period",
            "A synonym for complete dependence on others' decisions", "A purely legal, not personal, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is close reading of a character's internal reflection especially important in a psychologically focused short story like this one?", "options": [
            "Much of the story's meaning may reside in subtle shifts in the character's private thoughts rather than external action", "Internal reflection carries no particular weight in this kind of story",
            "This analytical approach is unrelated to studying short fiction", "External action always matters more than internal reflection in every story"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this story remain relevant to modern readers despite being written well over a century ago?", "options": [
            "Its exploration of personal desire versus social expectation retains broad, timeless relevance", "The story has no relevance to readers today",
            "This appeal is unrelated to literary study", "Only very recently written fiction can be considered relevant to modern readers"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social norm' mean as a concept relevant to the pressures a character in this story might navigate?", "options": [
            "An accepted standard of behaviour expected within a particular society", "A term unrelated to literary themes",
            "A purely legal requirement with no social dimension", "A synonym for complete individual freedom with no external expectation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is studying 19th-century American short fiction exploring women's experience valuable within a broader English curriculum?", "options": [
            "It broadens students' exposure to diverse literary perspectives and historical social contexts", "Such fiction has no place in an English curriculum",
            "This topic is unrelated to English language and literature study", "Only contemporary fiction is considered worth studying in an English course"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'A Respectable Woman' in an English course is to:", "options": [
            "Develop analytical skills around irony and psychological nuance in classic short fiction", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with fiction exploring social expectation or gender", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37567: [  # A Devoted Son
        {"q": "'A Devoted Son' is best classified as which literary genre?", "options": [
            "A short story", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'A Devoted Son' is widely attributed to Anita Desai, a writer associated with which literary tradition?", "options": [
            "Modern Indian literature written in English", "Ancient Roman epic poetry",
            "Contemporary Nepali drama", "Medieval European romance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The story's title, 'A Devoted Son', suggests it centrally explores which kind of relationship?", "options": [
            "The relationship and sense of duty between a son and his parents", "A purely historical account of an unrelated political event",
            "An unrelated legal dispute over inheritance law", "A description of a fictional adventure across continents"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story about filial devotion explore tension between duty and personal autonomy?", "options": [
            "Family obligation and individual identity can create meaningful narrative and thematic tension", "Duty and autonomy are never explored together in family-focused fiction",
            "This thematic focus is unrelated to short fiction", "Such tension has no connection to stories about filial relationships"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'filial piety' mean, a concept potentially central to a story about a devoted son's relationship with his parents?", "options": [
            "A sense of respect, duty, and care owed by children toward their parents", "A term unrelated to family-themed literature",
            "A synonym for complete independence from family obligation", "A purely legal, not cultural or ethical, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might Desai's fiction often explore family dynamics within an Indian social and cultural context?", "options": [
            "Her work is widely recognised for nuanced portrayals of Indian family life and its psychological complexity", "Her fiction is known for avoiding any exploration of family relationships",
            "This focus is unrelated to her body of work", "Family dynamics are never a subject of her fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story ironically titled 'A Devoted Son' explore complications beneath a seemingly straightforward, admirable relationship?", "options": [
            "Irony can reveal that devotion and care can also carry unexpected tension, resentment, or complexity", "Irony is never used in stories exploring family relationships",
            "This technique is unrelated to Desai's narrative style", "The story's title necessarily indicates an entirely simple, uncomplicated relationship"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'generational conflict' mean as a theme potentially relevant to this story?", "options": [
            "Tension or differing perspectives arising between older and younger generations within a family", "A term unrelated to family-themed literature",
            "A synonym for complete agreement between generations with no tension", "A purely legal, not interpersonal, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is Desai often credited as a significant figure in modern Indian English literature?", "options": [
            "Her psychologically nuanced fiction is widely recognised as influential within the tradition", "Desai had no significant role in Indian English literature",
            "This reputation is unrelated to literary history", "Desai wrote exclusively in a language other than English"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a story's central theme or underlying message?", "options": [
            "'Theme'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a story about a son's success (e.g. professional achievement) also explore strain within the family relationship?", "options": [
            "Achievement can sometimes create distance or altered dynamics within close family relationships", "Success and family strain are never connected in fiction exploring this theme",
            "This thematic connection is unrelated to the story's likely content", "Professional achievement always simplifies, never complicates, family relationships in fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'characterisation' mean, relevant to how the son and his parents might be portrayed through their interactions?", "options": [
            "The way a writer develops and reveals a character's personality and values", "A term unrelated to literary analysis",
            "A purely physical description with no personality dimension", "A synonym for plot summary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this story ask readers to consider whether the title's description of the son is entirely accurate?", "options": [
            "Questioning a title's literal claim can develop critical interpretation of irony and complexity in the story", "Titles should never be questioned or analysed critically",
            "This question type is unrelated to studying short fiction", "The story's title is necessarily meant with no ironic dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story about caring for ageing parents explore themes of burden alongside love and duty?", "options": [
            "Realistic portrayals of caregiving often acknowledge both its emotional rewards and its genuine difficulties", "Caregiving is always portrayed as either purely burdensome or purely rewarding, never both",
            "This thematic complexity is unrelated to literary analysis", "Burden and love are never explored together in stories about family caregiving"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'psychological complexity' mean as a quality potentially relevant to Desai's portrayal of family relationships in this story?", "options": [
            "A nuanced, layered portrayal of characters' inner motivations and emotions", "A term unrelated to character analysis",
            "A purely surface-level description with no inner complexity", "A synonym for a character with no emotional dimension"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might this story be considered relevant to readers navigating their own relationships with family and duty?", "options": [
            "Its themes of obligation, care, and generational tension resonate with widely shared family experience", "This story has no relevance to readers' own lives",
            "This connection is unrelated to studying the story", "Family relationships are considered irrelevant to literary study"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What does 'irony' mean, especially relevant to interpreting a title that may not fully match the story's more complex reality?", "options": [
            "A contrast between what is stated or expected and the underlying, more complex reality", "A term unrelated to this story's themes",
            "A synonym for a story with an entirely literal, unambiguous title", "A purely comedic device with no serious application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying modern Indian English literature valuable within a broader English curriculum?", "options": [
            "It broadens students' exposure to diverse voices and cultural perspectives within English-language literature", "Modern Indian English literature has no place in an English course",
            "This topic is unrelated to English language study", "Only British or American literature should be studied in English courses"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this story's exploration of family duty be considered especially relevant within a South Asian cultural context, including Nepal?", "options": [
            "Themes of filial responsibility and caring for ageing parents resonate broadly within South Asian family structures", "This story has no relevance to a South Asian cultural context",
            "Family duty is considered an entirely foreign concept within Nepali society", "This connection is unrelated to studying the story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'A Devoted Son' in an English course is to:", "options": [
            "Develop analytical skills around irony and family dynamics through nuanced modern short fiction", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with fiction exploring family duty or generational relationships", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37568: [  # The Treasure in the Forest
        {"q": "'The Treasure in the Forest' is best classified as which literary genre?", "options": [
            "A short story", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'The Treasure in the Forest' is widely attributed to H. G. Wells, a writer associated with which literary tradition?", "options": [
            "Late 19th/early 20th-century British literature, particularly known for speculative and adventure fiction", "Ancient Roman epic poetry",
            "Contemporary Nepali drama", "Medieval Japanese theatre"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The story's title, involving a search for treasure in a forest, suggests it belongs to which broad narrative tradition?", "options": [
            "Adventure fiction, often involving quest, discovery, and risk", "A purely factual scientific report",
            "A term unrelated to narrative genre", "A formal academic essay with no narrative element"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might an adventure story centred on a treasure hunt explore themes of greed or moral consequence?", "options": [
            "The pursuit of wealth is a common narrative device for examining characters' ethics and choices under pressure", "Greed is never explored as a theme in treasure-hunt narratives",
            "This thematic focus is unrelated to adventure fiction", "Moral consequence has no connection to stories about seeking treasure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What literary device might be used to build suspense in a story about characters seeking a hidden treasure?", "options": [
            "Withholding information and building anticipation before a climactic revelation", "Revealing all information about the treasure at the very beginning",
            "A term unrelated to adventure narrative technique", "Avoiding any element of suspense throughout the story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is H. G. Wells often studied as a significant figure in the history of speculative and adventure fiction?", "options": [
            "His work is widely recognised as influential within these genres in English literature", "Wells had no significant literary influence",
            "This reputation is unrelated to literary history", "Wells wrote exclusively non-fiction with no narrative fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'irony' mean, a device potentially relevant to a story where a search for treasure leads to unexpected consequence?", "options": [
            "A contrast between what characters expect or desire and what actually occurs", "A term unrelated to this story's likely structure",
            "A synonym for a story with an entirely predictable, straightforward outcome", "A purely comedic device with no serious application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story about a treasure hunt use a remote or isolated setting (like a forest)?", "options": [
            "Isolation can heighten tension and remove characters from ordinary social constraints, intensifying the narrative", "Setting has no bearing on the story's tension or themes",
            "This technique is unrelated to adventure narrative", "Isolated settings are never used meaningfully in adventure fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'foreshadowing' mean as a literary technique potentially relevant to building suspense toward the story's outcome?", "options": [
            "Hints or clues given early in a narrative about events that will occur later", "A term unrelated to narrative technique",
            "A synonym for a story's conclusion only", "A device that removes all suspense from a narrative"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a story built around a search, journey, or pursuit of a specific goal?", "options": [
            "'Quest' narrative", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might a treasure-hunt narrative explore the theme of trust or betrayal between characters pursuing the same goal?", "options": [
            "Competing self-interest around a shared goal can create meaningful conflict and tension between characters", "Trust and betrayal are never explored in adventure fiction",
            "This thematic focus is unrelated to the genre", "Characters pursuing a shared goal in fiction always cooperate with no conflict"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'moral consequence' mean, relevant to a story where the pursuit of treasure might lead to an ironic or cautionary outcome?", "options": [
            "The ethical result or lesson stemming from a character's choices or actions", "A term unrelated to narrative themes",
            "A synonym for an outcome entirely disconnected from a character's choices", "A purely legal, not ethical or narrative, concept"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this story ask readers to trace the sequence of events leading to its conclusion?", "options": [
            "Tracing plot sequence tests understanding of how cause and effect build toward the story's resolution", "Plot sequence has no relevance to comprehension of adventure fiction",
            "This question type is unrelated to studying short fiction", "Adventure stories never follow any clear sequence of events"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might early 20th-century adventure fiction, the era associated with Wells, often reflect broader contemporary interests in exploration and discovery?", "options": [
            "Fiction from this period often engaged with widespread public fascination with exploration and the unknown", "This era of fiction never engaged with themes of exploration",
            "This connection is unrelated to literary and historical context", "Adventure fiction from this period focused exclusively on domestic, non-adventurous settings"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'plot twist' mean as a narrative device potentially relevant to a treasure-hunt story with an unexpected outcome?", "options": [
            "An unexpected turn or revelation that changes the direction or understanding of a story", "A term unrelated to narrative technique",
            "A synonym for a completely predictable, expected story development", "A device used only in comedic writing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is studying classic adventure fiction like this valuable for understanding narrative suspense techniques?", "options": [
            "It demonstrates how writers build and sustain tension toward a climactic resolution", "Adventure fiction has no value for studying narrative technique",
            "This value is unrelated to studying short fiction", "Suspense techniques are unique to modern fiction and absent from classic works"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story combining adventure with moral reflection be considered more than simple entertainment?", "options": [
            "It can use an engaging plot to explore deeper questions about human motivation and consequence", "Adventure stories never contain any deeper thematic reflection",
            "This combination is unrelated to literary analysis", "Entertainment and moral reflection are always entirely separate in fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'setting' contribute to a story centred on a forest search for treasure?", "options": [
            "It establishes atmosphere and can heighten tension through isolation or unfamiliarity", "Setting has no effect on a story's tone or tension",
            "This element is unrelated to the story's structure", "Setting is only ever mentioned in passing with no narrative purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why has classic adventure short fiction from this era remained a common subject of literary study?", "options": [
            "Such stories often combine accessible plot with lasting thematic and stylistic interest", "This kind of fiction has no lasting literary reputation",
            "This continued study is unrelated to literary or educational value", "Adventure fiction is studied only for historical, not literary, reasons"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'The Treasure in the Forest' in an English course is to:", "options": [
            "Develop skills in analysing suspense, irony, and moral theme in classic adventure fiction", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with adventure or suspense-driven fiction", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37569: [  # My Old Home
        {"q": "'My Old Home' is best classified as which literary genre?", "options": [
            "A short story", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'My Old Home' is widely attributed to Lu Xun, a writer associated with which literary tradition?", "options": [
            "Modern Chinese literature", "Ancient Roman epic poetry",
            "Contemporary Nepali drama", "Medieval European romance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The story's title, 'My Old Home', suggests it centrally explores which broad theme?", "options": [
            "Return to one's childhood home and reflection on change over time", "A purely technical description of architecture",
            "An unrelated discussion of international trade", "A description of a fictional battle scene"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a story about returning to one's hometown explore themes of nostalgia alongside disillusionment?", "options": [
            "Revisiting the past can reveal both fond memory and the often unsettling reality of change over time", "Nostalgia and disillusionment are never explored together in fiction",
            "This thematic focus is unrelated to short fiction", "Return-home narratives never involve any sense of altered perception"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Lu Xun is broadly recognised as a major and influential figure in which period of literary history?", "options": [
            "Early 20th-century modern Chinese literature", "Ancient classical literature",
            "Contemporary 21st-century digital fiction", "Medieval European literature"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might Lu Xun's fiction often engage with social change and its impact on ordinary individuals and communities?", "options": [
            "His work is widely recognised for critically examining Chinese society during a period of significant transformation", "His fiction is known for avoiding any engagement with social change",
            "This focus is unrelated to his body of work", "Social change is never a subject of his fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social realism' mean as a literary approach, relevant to Lu Xun's broader reputation?", "options": [
            "A style depicting everyday life and social conditions with a focus on realistic, often critical detail", "A term unrelated to his literary style",
            "A synonym for pure fantasy with no connection to real social conditions", "A purely scientific method with no literary application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story reflecting on childhood memory use a contrast between past and present perception of a place or person?", "options": [
            "Contrasting memory with present reality can highlight how time, distance, or social change alters understanding", "Such contrast has no thematic function in this kind of story",
            "This technique is unrelated to reflective/narrative fiction", "Memory and present reality are never contrasted meaningfully in fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'characterisation' mean, relevant to how a childhood friend or figure might be portrayed differently upon the narrator's return?", "options": [
            "The way a writer develops and reveals a character's personality, potentially showing change over time", "A term unrelated to literary analysis",
            "A purely physical description with no personality dimension", "A synonym for plot summary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What vocabulary term describes a sentimental longing or affection for the past?", "options": [
            "'Nostalgia'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might this story explore social or class distinctions that have grown between the narrator and figures from their past?", "options": [
            "Time and changing circumstance can alter relationships in ways connected to broader social structures", "Class or social distinction is never explored in stories about returning home",
            "This thematic focus is unrelated to the story's likely content", "Social structure has no connection to personal relationships in fiction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is Lu Xun often credited as a foundational figure in modern Chinese literature?", "options": [
            "His work is widely recognised as significantly shaping the development of modern Chinese fiction", "Lu Xun had no significant role in Chinese literary history",
            "This reputation is unrelated to literary history", "Lu Xun wrote exclusively in a language other than Chinese"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a story about returning to one's hometown be structured around a journey (arrival, stay, departure)?", "options": [
            "This structure naturally frames the narrator's reflection and the changes they observe", "Journey structure has no connection to a story about a homecoming",
            "This technique is unrelated to narrative structure", "Such stories never follow any structured journey framework"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'social critique' mean, a quality potentially present in this story's exploration of change over time?", "options": [
            "A thoughtful examination or criticism of aspects of society through the text", "A term unrelated to Lu Xun's literary reputation",
            "A synonym for uncritical praise of existing social conditions", "A purely legal, not literary, form of analysis"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this story ask readers to compare the narrator's childhood memory with their present-day observation?", "options": [
            "Comparing past and present perception is often central to understanding the story's reflective theme", "Such comparison has no relevance to comprehension of this story",
            "This question type is unrelated to studying reflective short fiction", "The story contains no meaningful contrast between past and present"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this story be considered relevant beyond its original Chinese social context?", "options": [
            "Its themes of memory, change, and returning home resonate broadly across many cultures", "The story has no relevance outside its original specific context",
            "This appeal is unrelated to literary interpretation", "Themes of homecoming and change are unique to only one specific culture"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'universal theme' mean, relevant to why this story's exploration of home and change might resonate broadly?", "options": [
            "An idea broadly relatable to human experience regardless of background", "A term unrelated to literary analysis",
            "A synonym for an idea relevant to only one narrow group", "A purely local, culturally specific concept with no wider relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying a translated Chinese literary classic (originally written in Chinese) valuable in an English course?", "options": [
            "It exposes students to literary perspectives and traditions beyond English-language literature", "Translated classics have no educational value",
            "Only originally English-language texts should be studied", "Translation removes all meaningful content from a story"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this story's theme of encountering a changed hometown resonate with readers who have experienced migration or return, including in Nepal?", "options": [
            "Many readers, including in contexts with significant migration for work or study, may relate to the experience of a transformed 'home'", "This theme has no relevance to readers with migration experience",
            "This connection is unrelated to studying the story", "Migration and homecoming are never connected to this story's themes"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The general educational value of studying 'My Old Home' in an English course is to:", "options": [
            "Develop analytical skills around memory, change, and social reflection in a modern literary classic", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with fiction exploring nostalgia or social change", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37570: [  # The Half-closed Eyes of the Buddha and the Slowly Sinking Sun
        {"q": "'The Half-closed Eyes of the Buddha and the Slowly Sinking Sun' is best classified, given its title, as most likely which literary form?", "options": [
            "A short story or descriptive/reflective narrative piece", "A formal legal contract", "A scientific lab manual", "A business invoice"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "What does the title's imagery (a Buddha statue, a setting sun) suggest about the piece's likely tone and setting?", "options": [
            "A contemplative, serene atmosphere, possibly set in or evoking a Himalayan/South Asian Buddhist context", "A fast-paced, purely technical narrative with no atmospheric description",
            "An unrelated discussion of modern industrial technology", "A purely comedic, lighthearted subject with no reflective tone"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What literary device is at work when 'half-closed eyes' of a statue are described as though gazing or perceiving?", "options": [
            "Personification (attributing living, perceptive qualities to a non-living object)", "A purely literal, non-figurative description",
            "A term unrelated to literary analysis", "Onomatopoeia exclusively"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might a piece use the image of a 'slowly sinking sun' alongside a serene religious image?", "options": [
            "The passage of a day (sunset) alongside a symbol of peace or transcendence can evoke themes of time, impermanence, or stillness", "Sunset imagery has no connection to themes of time or reflection",
            "This technique is unrelated to descriptive/reflective writing", "Combining these images always produces a purely negative or ominous tone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'imagery' mean as a literary technique likely central to this piece's title and content?", "options": [
            "Descriptive language appealing to the senses to create a vivid impression", "A term unrelated to literary analysis",
            "A purely factual, non-descriptive style of writing", "A synonym for the piece's rhyme scheme only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a piece set around a Buddhist religious site explore themes of peace, impermanence, or spiritual reflection?", "options": [
            "Such settings are often associated culturally and symbolically with these themes", "Religious settings have no thematic connection to reflective writing",
            "This thematic reading is unrelated to literary analysis", "Peace and impermanence are never explored through religious imagery in literature"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'atmosphere' mean as a literary element likely central to this evocatively-titled piece?", "options": [
            "The overall mood or feeling created through setting, description, and tone", "A term unrelated to literary analysis",
            "A purely technical meteorological term with no literary use", "A synonym for plot summary"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a writer use a long, evocative, image-rich title (rather than a short, plain one) for a reflective piece like this?", "options": [
            "An elaborate, sensory title can immediately immerse the reader in the piece's atmosphere and themes before it even begins", "Long titles have no effect on how a reader approaches a text",
            "This technique is unrelated to literary titling", "Elaborate titles are always considered a weakness in reflective writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'impermanence' mean as a theme potentially relevant to a piece juxtaposing a setting sun with a serene, ancient statue?", "options": [
            "The idea that all things are transient and subject to change over time", "A term unrelated to reflective or spiritual writing",
            "A synonym for permanence and unchanging stability", "A purely scientific concept with no reflective or spiritual application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes writing that vividly describes a scene, mood, or setting?", "options": [
            "'Descriptive'", "'Trigonometry'", "'Photosynthesis'", "'Jurisdiction'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might such a piece be relevant reading within a Nepali English curriculum, given Nepal's Buddhist heritage sites (e.g. Swayambhunath, Boudhanath)?", "options": [
            "It can connect students to culturally resonant imagery and themes present within their own regional heritage", "This piece has no relevance to Nepali students",
            "Nepal has no connection to Buddhist cultural or religious heritage", "This connection is unrelated to studying the piece"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a reflective piece use a slow, unhurried pace in its prose to match its contemplative subject matter?", "options": [
            "Pacing can mirror and reinforce the calm, reflective mood the piece seeks to evoke", "Pacing has no connection to a piece's tone or mood",
            "This technique is unrelated to descriptive/reflective writing", "A slow pace always weakens a reflective piece's impact"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'symbolism' mean, a technique likely central to this piece's use of a Buddha statue and setting sun as central images?", "options": [
            "The use of an object, image, or event to represent a deeper meaning", "A term unrelated to literary analysis",
            "A purely decorative element with no meaning", "A synonym for literal, non-figurative description"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might comprehension questions on this piece ask readers to interpret what the closing/opening imagery (sunset, statue) might represent?", "options": [
            "Interpreting central symbolic imagery is often key to understanding a reflective piece's deeper meaning", "Symbolic imagery carries no particular significance for comprehension",
            "This question type is unrelated to studying reflective writing", "This piece contains no interpretable symbolic imagery"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might a piece exploring stillness and quiet observation avoid a fast-moving, action-driven plot?", "options": [
            "A contemplative piece often prioritises mood and reflection over dramatic plot events", "Reflective writing must always include a fast-moving, dramatic plot",
            "This choice is unrelated to the piece's likely purpose", "Stillness and quiet observation are never explored in literary writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'sensory detail' mean, relevant to how this piece likely evokes its visual and atmospheric imagery?", "options": [
            "Description that appeals to sight, sound, or other senses to create a vivid impression", "A term unrelated to descriptive writing",
            "A purely factual, non-sensory style of description", "A synonym for a piece's grammatical structure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this piece be considered a good example for teaching students about evocative, atmospheric descriptive writing?", "options": [
            "Its rich, sensory title suggests a piece well suited to studying how imagery builds mood and meaning", "This piece has no useful connection to teaching descriptive technique",
            "This educational use is unrelated to literary study", "Atmospheric writing is never usefully illustrated through such a title"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is close reading of imagery especially important in a piece whose entire title is built from vivid sensory description?", "options": [
            "The title signals that visual and atmospheric detail likely carries central importance to the piece's meaning", "Imagery has no particular significance in this kind of piece",
            "This analytical approach is unrelated to studying reflective writing", "Close reading of imagery is unnecessary when a title is already descriptive"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might reading reflective, atmospheric writing rooted in regional cultural and religious imagery be valuable for students?", "options": [
            "It can build both literary appreciation and connection to culturally resonant themes and settings", "Such writing has no educational value",
            "This topic is unrelated to studying literature", "Only writing entirely disconnected from any cultural or regional context is worth studying"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying this piece in an English course is to:", "options": [
            "Develop close-reading and imagery-analysis skills through a richly atmospheric, reflective text", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with reflective or atmospheric writing", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37571: [  # A Very Old Man with Enormous Wings
        {"q": "'A Very Old Man with Enormous Wings' is best classified as which literary genre?", "options": [
            "A short story, widely associated with magical realism", "A formal scientific essay", "A one-act comic play", "A motivational speech"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'A Very Old Man with Enormous Wings' is widely attributed to Gabriel García Márquez, a writer associated with which literary tradition?", "options": [
            "Latin American literature, particularly known for magical realism", "Ancient Roman epic poetry",
            "Contemporary Nepali drama", "Medieval English romance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "What is 'magical realism' as a literary genre, closely associated with García Márquez's work?", "options": [
            "A genre blending realistic, everyday settings with magical or fantastical elements treated as ordinary", "A genre depicting purely realistic events with no fantastical elements whatsoever",
            "A term unrelated to García Márquez's literary reputation", "A genre set exclusively in entirely invented fantasy worlds with no realistic grounding"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The story is widely known for centring on the appearance of which extraordinary figure in an ordinary village setting?", "options": [
            "A very old man with enormous wings, treated by the community with a mix of curiosity and mundane reaction", "A purely scientific alien visitor treated with panic and terror",
            "A famous historical king arriving to reclaim the village", "A modern technological robot"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why is the villagers' relatively mundane, even exploitative reaction to an extraordinary winged figure often highlighted as significant in discussions of this story?", "options": [
            "It reflects the story's characteristic magical realist blending of the miraculous with ordinary, sometimes cynical human behaviour", "Villagers in the story are widely noted for reacting with awe and immediate reverence with no ordinary human response",
            "This reaction has no thematic significance in the story", "The story avoids depicting any human reaction to the winged figure at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What literary effect does treating a fantastical element (like a winged old man) as mundane or ordinary typically create in magical realist fiction?", "options": [
            "It can blur the line between the miraculous and the everyday, prompting reflection on how people respond to the extraordinary", "This treatment has no particular literary effect",
            "This technique is unrelated to magical realism", "Treating fantastical elements as ordinary always removes any thematic depth from a story"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is García Márquez widely regarded as one of the most significant writers associated with 20th-century Latin American literature?", "options": [
            "His work, especially his pioneering of magical realism, is widely recognised as highly influential internationally", "García Márquez had no significant lasting literary influence",
            "This reputation is unrelated to literary history", "García Márquez is studied only for biographical, not literary, reasons"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'satire' mean, a quality sometimes discussed in relation to this story's portrayal of how the community treats the winged man?", "options": [
            "Using irony or exaggeration to critique human behaviour or society", "A term unrelated to this story's likely themes",
            "A synonym for a purely earnest, uncritical portrayal with no irony", "A device used only in purely comedic writing with no serious critique"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might magical realist fiction be considered a distinctive way of exploring social or human themes compared to purely realistic fiction?", "options": [
            "Blending the fantastical with the ordinary can create fresh perspective on familiar human behaviours and social dynamics", "Magical realism is considered to have no thematic advantage over purely realistic fiction",
            "This distinction is unrelated to literary genre study", "Fantastical elements always remove any meaningful social commentary from a story"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What vocabulary term describes a genre blending the fantastical with the everyday, treated as normal within the narrative?", "options": [
            "'Magical realism'", "'Trigonometry'", "'Photosynthesis'", "'Depreciation'"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Why might the story explore themes of exploitation or spectacle, given a community's reaction to an extraordinary visitor?", "options": [
            "It can critique how the miraculous or unusual might be commodified or treated as curiosity rather than something sacred", "Exploitation and spectacle are never explored themes in this story",
            "This thematic focus is unrelated to the story's likely content", "The community in the story is widely noted for showing no interest whatsoever in the winged man"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'ambiguity' mean, a quality often associated with magical realist fiction like this story?", "options": [
            "Openness to multiple possible interpretations, often left deliberately unresolved", "A term unrelated to this genre",
            "A synonym for a story with only one single, obvious meaning", "A purely negative quality indicating a story has failed"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why might comprehension questions on this story ask readers to consider what the winged man might symbolically represent?", "options": [
            "Interpreting the story's central fantastical figure is often key to understanding its broader thematic meaning", "Symbolic interpretation has no relevance to comprehension of this story",
            "This question type is unrelated to studying magical realist fiction", "The winged man is widely understood to carry no symbolic significance at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might this story be read as commentary on how society treats those who are different or extraordinary?", "options": [
            "The community's varied reactions to the winged man can reflect broader patterns in how societies respond to the unfamiliar", "This story has no connection to themes of difference or social response",
            "This reading is unrelated to literary interpretation", "Themes of social response to the unusual are never explored in this story"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'irony' mean, a device widely noted as present in how ordinary, sometimes petty human behaviour surrounds an extraordinary, almost sacred figure in this story?", "options": [
            "A contrast between the expected reverence for something miraculous and the actual mundane or self-interested human response", "A term unrelated to this story's themes",
            "A synonym for a story with an entirely predictable, reverent human response", "A purely comedic device with no serious application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why is studying Latin American magical realist fiction valuable within a broader English curriculum?", "options": [
            "It exposes students to an influential literary tradition and mode of storytelling distinct from purely realistic fiction", "Magical realist fiction has no place in an English course",
            "This topic is unrelated to English language and literature study", "Only strictly realistic fiction should be studied in an English course"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Why might the story's ending (regardless of specific plot detail) be considered significant for interpreting its overall meaning?", "options": [
            "As with much short fiction, the conclusion often reframes or crystallises the story's central thematic concerns", "A story's ending never carries any particular interpretive weight",
            "This analytical approach is unrelated to studying short fiction", "Endings in magical realist fiction are widely understood to carry no significance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "What does 'the fantastic treated as mundane' mean as a defining technique of magical realism relevant to this story?", "options": [
            "Extraordinary or supernatural elements are presented within the narrative as unremarkable, ordinary occurrences", "Extraordinary elements are always treated with intense shock and disbelief in this genre",
            "This technique is unrelated to defining magical realism", "Magical realism avoids including any fantastical elements at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Why has this story remained widely studied and anthologised internationally?", "options": [
            "Its inventive blending of the fantastical and the everyday is broadly recognised as a landmark example of magical realism", "The story has no lasting literary reputation",
            "This appeal is unrelated to literary study", "It is studied only for historical, not thematic or stylistic, reasons"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The general educational value of studying 'A Very Old Man with Enormous Wings' in an English course is to:", "options": [
            "Develop appreciation for magical realism and its use to explore human and social themes", "Memorise unrelated vocabulary with no thematic connection",
            "Avoid engaging with fantastical or non-realistic literary genres", "Focus exclusively on unrelated grammar drills"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
