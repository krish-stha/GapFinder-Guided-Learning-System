# -*- coding: utf-8 -*-
"""
NEB Grade 11 Management - Social Studies and Life Skills Education
question bank (course 209, subject 34317 "सामाजिक अध्ययन", which already
existed as an empty 10-chapter shell before this session).

Authored content (not content partner data - loaded with source='synthetic'
via scripts/load_by_chapter_id.py, NOT load_question_bank.py). This
subject's chapter names are exact-verified-mismatched against course 91's
सामाजिक अध्ययन content (same "एकाइ N" unit numbering scheme, but differing
exact wording per unit - confirmed via a live query, not assumed), so
linking real content the way नेपाली/English/209-Computer-Science were
handled is not possible here; this is fresh content instead. Keyed by the
verified integer chapter_id (not the Devanagari chapter name) to avoid
any transcription risk with source data containing double-spaces and
other subtle whitespace quirks already seen elsewhere in this course.

Chapter mapping (verified live, NEB Grade 11 Social Studies & Life Skills
Education unit list - Unit 4 does not exist in this course's shell):
  34915 - Unit 1: Concept of Social Studies and Life Skills Education
  34913 - Unit 2: Skills of Social Studies and Life Skills
  35075 - Unit 3: Life Skills
  35065 - Unit 5: Geography and Social Relation
  35063 - Unit 6: World History
  35071 - Unit 7: Social Identity, Diversity and Class Division
  35073 - Unit 8: Constitution and Civic Awareness
  35079 - Unit 9: Settlement, Population and Development
  35081 - Unit 10: Economy and Development
  35077 - Unit 11: Health Service and Social Development

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}. Never presented as content partner
content or as evidence about real students.
"""

QUESTIONS = {
    34915: [  # Unit 1: Concept of Social Studies and Life Skills Education
        {"q": "'Social Studies' as a school subject is best described as the integrated study of:", "options": [
            "Human society, its history, geography, economy, and civic life", "Only pure mathematics with no social content",
            "Only natural sciences such as physics and chemistry", "A subject unrelated to human society"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Life Skills Education' primarily aims to develop learners':", "options": [
            "Practical abilities to handle everyday personal, social, and work-related challenges effectively", "Ability to memorise historical dates only",
            "Skills relevant only to laboratory science experiments", "Knowledge of foreign languages exclusively"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Social Studies is often described as an 'integrated' subject because it draws on:", "options": [
            "Multiple disciplines such as history, geography, economics, sociology, and civics together", "A single narrow discipline with no cross-disciplinary content",
            "Only mathematics and physics", "No academic disciplines at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key objective of teaching Social Studies at the +2 level in Nepal is to help students become:", "options": [
            "Informed, responsible citizens capable of participating meaningfully in society", "Isolated from society with no civic role",
            "Experts only in international relations with no domestic focus", "Unaware of Nepal's own social and historical context"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Life skills' commonly emphasised in this curriculum include:", "options": [
            "Communication, decision-making, critical thinking, and problem-solving", "Only advanced calculus techniques",
            "Only skills related to a single specific occupation", "Skills entirely unrelated to daily life"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Combining Social Studies with Life Skills Education in a single subject reflects the educational goal of:", "options": [
            "Preparing students with both social/civic knowledge and practical, applicable competencies", "Separating academic knowledge completely from any practical application",
            "Focusing exclusively on rote memorisation with no applied skill", "Removing any connection between knowledge and real life"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Civic sense', a concept often introduced early in Social Studies, refers to:", "options": [
            "An individual's awareness of their rights, duties, and responsibilities as a member of society", "A purely legal term with no relevance to ordinary citizens",
            "A concept used only in economics, not social studies", "An individual's private financial planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Social Studies helps students understand 'social change' by studying how societies:", "options": [
            "Evolve over time due to historical, economic, and cultural factors", "Remain permanently fixed with absolutely no change over time",
            "Change only due to natural disasters, with no other cause", "Have no relationship to historical or economic factors"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best illustrates the 'interdisciplinary' nature of Social Studies?", "options": [
            "Studying the economic impact of a historical event, which draws on both history and economics", "Studying only isolated historical dates with no other context",
            "Studying only mathematical formulas with no historical or economic reference", "Studying a topic using exactly one discipline at all times"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A core life skill relevant to workplace and community settings is 'interpersonal skill', which refers to the ability to:", "options": [
            "Communicate and interact effectively with other people", "Perform advanced mathematical calculations only",
            "Operate machinery with no reference to communication", "Memorise historical facts with no application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Critical thinking', as a life skill, involves the ability to:", "options": [
            "Analyse information objectively and make reasoned judgments", "Accept all information without question or analysis",
            "Avoid forming any opinion on any matter", "Rely solely on others' opinions with no independent analysis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Studying Social Studies and Life Skills Education together is intended to prepare students for:", "options": [
            "Both informed civic participation and practical, everyday life challenges", "Only theoretical academic examinations with no practical application",
            "A career limited exclusively to teaching", "A purely private, individual pursuit with no social relevance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Decision-making' as a life skill is important because it helps individuals:", "options": [
            "Evaluate options and choose a course of action appropriate to a situation", "Avoid making any choices in life",
            "Rely entirely on random chance for every decision", "Ignore the consequences of any choice made"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The scope of Social Studies at +2 level typically includes:", "options": [
            "Geography, history, economy, society, constitution, and civic awareness", "Only advanced physics equations",
            "Only foreign language grammar rules", "A single isolated topic with no broader scope"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Problem-solving skill' in the life skills framework refers to the ability to:", "options": [
            "Identify a problem and work through a systematic process to resolve it", "Ignore problems entirely without any response",
            "Rely exclusively on someone else to solve every problem", "Avoid ever encountering any problem in life"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Understanding one's own society through Social Studies helps a student to:", "options": [
            "Appreciate social diversity and engage constructively with different groups", "Remain completely indifferent to social diversity",
            "Reject engagement with any group different from their own", "Avoid any understanding of their own community"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Communication skill', a foundational life skill, includes the ability to:", "options": [
            "Express ideas clearly and listen effectively to others", "Perform complex mathematical proofs only",
            "Avoid speaking or listening in any social context", "Operate technical machinery with no reference to expression"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best explains why Nepal's +2 curriculum integrates Social Studies with Life Skills Education rather than teaching them as entirely separate, unrelated subjects?", "options": [
            "Social/civic knowledge and practical life competencies reinforce each other and both serve a student's readiness for adult and civic life", "The two areas have no meaningful connection to each other",
            "Combining them was done purely by administrative accident with no educational rationale", "Life skills have no relevance to a student's understanding of society"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A student applying 'critical thinking' learned in this subject to evaluate a news report would be:", "options": [
            "Assessing the report's evidence and reasoning rather than accepting it at face value", "Accepting the report's claims automatically with no evaluation",
            "Ignoring the report entirely without any engagement", "Applying a skill entirely unrelated to Social Studies"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of this introductory unit on the 'Concept of Social Studies and Life Skills Education'?", "options": [
            "To establish the subject's integrated scope and its goal of building both social understanding and practical life competencies", "To provide unrelated trivia with no connection to the rest of the course",
            "To focus exclusively on a single narrow historical event", "To replace the need for studying any further units in the subject"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34913: [  # Unit 2: Skills of Social Studies and Life Skills
        {"q": "'Research skill' within Social Studies refers to the ability to:", "options": [
            "Systematically gather, evaluate, and use information to answer a question", "Ignore all available information sources",
            "Rely only on personal opinion with no evidence gathering", "Avoid asking any research question at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Map-reading skill', a core Social Studies skill, involves the ability to:", "options": [
            "Interpret symbols, scale, and directions to understand geographic information on a map", "Perform advanced calculus operations",
            "Analyse a company's financial statements", "Memorise a list of unrelated historical dates"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Data interpretation skill' allows a student to:", "options": [
            "Draw meaningful conclusions from statistics, graphs, or tables presented in social/economic data", "Ignore any numerical or graphical information presented",
            "Rely solely on memorised facts with no reference to data", "Avoid engaging with any quantitative information"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Observation skill' in Social Studies fieldwork involves:", "options": [
            "Carefully watching and recording social, economic, or environmental phenomena", "Ignoring the surrounding environment entirely",
            "Relying exclusively on textbook descriptions with no direct observation", "A skill unrelated to fieldwork of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Time management', a key life skill, involves the ability to:", "options": [
            "Plan and prioritise tasks effectively within available time", "Ignore deadlines and schedules entirely",
            "Complete every task simultaneously with no prioritisation", "A skill with no relevance to academic or work life"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Teamwork skill' is valuable in both social studies fieldwork and daily life because it enables individuals to:", "options": [
            "Collaborate effectively with others to achieve a shared goal", "Work in complete isolation with no collaboration",
            "Ignore the contributions and perspectives of other people", "Avoid any group-based activity entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Interviewing skill', used in social research, involves:", "options": [
            "Asking structured questions to gather firsthand information from a respondent", "Only reading pre-published secondary sources with no direct interaction",
            "Avoiding any interaction with the subject of study", "A skill unrelated to gathering information"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Analytical skill' in Social Studies involves the ability to:", "options": [
            "Break down complex social or historical information into its underlying components to understand it better", "Accept complex information without any further examination",
            "Avoid engaging with complex information altogether", "A skill limited exclusively to mathematics"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Financial literacy', increasingly emphasised as a life skill, refers to:", "options": [
            "The ability to understand and manage personal financial matters such as budgeting and saving", "The ability to perform advanced corporate accounting only",
            "A skill unrelated to everyday personal decision-making", "The ability to print currency"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital literacy', a modern life skill, refers to the ability to:", "options": [
            "Effectively and safely use digital tools and information technology", "Avoid using any form of technology",
            "Only operate outdated, non-digital tools", "A skill unrelated to modern life"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Chart and graph construction skill' helps students to:", "options": [
            "Visually represent social or economic data in a clear, interpretable format", "Avoid ever representing data visually",
            "Only memorise numbers without any visual representation", "A skill with no application to Social Studies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Conflict resolution skill', a life skill relevant to social harmony, involves the ability to:", "options": [
            "Address disagreements constructively and reach a mutually acceptable solution", "Always avoid any disagreement by ignoring it entirely",
            "Escalate every disagreement without any resolution attempt", "A skill unrelated to interpersonal relationships"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Empathy', an important interpersonal life skill, refers to the ability to:", "options": [
            "Understand and share the feelings or perspective of another person", "Completely disregard other people's feelings",
            "Focus exclusively on one's own perspective with no consideration of others", "A skill unrelated to social interaction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Self-awareness', a foundational life skill, involves understanding one's own:", "options": [
            "Strengths, weaknesses, values, and emotions", "Only one's physical height and weight",
            "A concept unrelated to personal development", "Only one's academic exam scores"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Stress management skill' helps individuals to:", "options": [
            "Cope effectively with pressure and challenging situations", "Avoid ever experiencing any challenging situation",
            "Ignore stress entirely with no coping strategy", "A skill unrelated to personal wellbeing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Applying 'research skill' to a Social Studies project on local unemployment would involve:", "options": [
            "Collecting relevant local data and analysing it to draw evidence-based conclusions", "Guessing an answer with no data collection at all",
            "Ignoring the local context entirely", "A process unrelated to research skill"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Negotiation skill', useful in both civic and workplace contexts, involves the ability to:", "options": [
            "Reach a mutually acceptable agreement between parties with differing interests", "Impose one party's view with no consideration of the other",
            "Avoid any interaction between differing parties", "A skill unrelated to resolving differences"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'digital literacy' has become an increasingly emphasised life skill in recent Social Studies curricula?", "options": [
            "Technology plays a growing role in communication, research, and civic participation in modern society", "Digital tools have no relevance to modern civic or social life",
            "Digital literacy is relevant only to computer science students, not social studies", "Technology use has declined in relevance to everyday life"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why both 'analytical skill' and 'communication skill' are needed together when presenting Social Studies research findings?", "options": [
            "Analytical skill allows sound conclusions to be drawn, while communication skill allows those conclusions to be shared clearly with others", "Only analytical skill is ever needed, regardless of how findings are shared",
            "Only communication skill matters, regardless of whether the underlying analysis is sound", "The two skills are entirely unrelated to presenting research"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall value of combining social-studies-specific skills (research, map-reading, data interpretation) with broader life skills (communication, decision-making) in this unit?", "options": [
            "Together they equip students to investigate social phenomena rigorously and apply findings effectively in real life", "The two skill sets are entirely unrelated and provide no combined benefit",
            "Only broader life skills matter; discipline-specific skills are irrelevant", "This combination has no practical value for a +2 student"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35075: [  # Unit 3: Life Skills
        {"q": "'Adaptability', a valuable life skill, refers to the ability to:", "options": [
            "Adjust effectively to new conditions or changing circumstances", "Resist any form of change under all circumstances",
            "Remain identical in every situation regardless of context", "A skill unrelated to handling change"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Leadership skill' involves the ability to:", "options": [
            "Guide, motivate, and coordinate a group toward a common goal", "Work in complete isolation with no group interaction",
            "Avoid any responsibility for guiding others", "A skill unrelated to group activities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Goal-setting skill' helps an individual to:", "options": [
            "Define clear, achievable objectives and a plan to reach them", "Avoid ever defining any objective",
            "Pursue random, undefined outcomes with no planning", "A skill unrelated to personal or academic development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Resilience', as a life skill, refers to the ability to:", "options": [
            "Recover and adapt positively after facing setbacks or difficulties", "Give up entirely after any setback",
            "Avoid ever facing any challenge or difficulty", "A skill unrelated to overcoming adversity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Assertiveness', a communication-related life skill, involves the ability to:", "options": [
            "Express one's needs and opinions confidently while respecting others", "Aggressively dominate every conversation with no respect for others",
            "Remain silent and never express any opinion", "A skill unrelated to interpersonal communication"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Creative thinking', a valuable life skill, involves the ability to:", "options": [
            "Generate new ideas or novel approaches to a problem", "Rely exclusively on pre-existing, unchanged solutions",
            "Avoid any form of original thought", "A skill unrelated to problem-solving"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Coping skills' help individuals to:", "options": [
            "Manage difficult emotions and situations in a healthy way", "Ignore difficult emotions entirely with no management strategy",
            "Avoid ever experiencing any emotion", "A concept unrelated to personal wellbeing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Networking skill', relevant to career development, involves:", "options": [
            "Building and maintaining professional and social relationships that provide mutual support", "Avoiding all professional relationships entirely",
            "Relying solely on one's own resources with no external relationships", "A skill unrelated to career development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Entrepreneurial life skills' include qualities such as:", "options": [
            "Initiative, risk assessment, and innovative problem-solving", "Complete risk-avoidance with no initiative",
            "A total absence of problem-solving ability", "Skills unrelated to starting or managing an enterprise"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Practising 'active listening', part of communication life skills, involves:", "options": [
            "Fully concentrating on, understanding, and responding thoughtfully to a speaker", "Interrupting the speaker constantly with no attention to their message",
            "Ignoring the speaker entirely while they talk", "A skill unrelated to effective communication"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Ethical decision-making', a life skill relevant to civic life, involves considering:", "options": [
            "The moral implications and fairness of a choice, not just its personal benefit", "Only one's own personal benefit with no reference to fairness",
            "No ethical considerations of any kind", "A concept unrelated to decision-making"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Emotional regulation', part of emotional intelligence, refers to the ability to:", "options": [
            "Manage and appropriately express one's emotions in different situations", "Suppress all emotions permanently with no expression",
            "Express every emotion without any self-control", "A skill unrelated to interpersonal effectiveness"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Civic responsibility', a life skill relevant to community participation, involves:", "options": [
            "Actively contributing to the wellbeing of one's community and society", "Avoiding any involvement in community matters",
            "Focusing exclusively on personal interests with no community consideration", "A concept unrelated to social studies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Health and hygiene awareness', part of practical life skills, contributes to:", "options": [
            "Maintaining personal and community wellbeing through informed habits", "A concept entirely unrelated to daily life",
            "Ignoring basic health practices altogether", "A skill limited exclusively to medical professionals"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A student demonstrating 'adaptability' when moving to a new school environment would likely:", "options": [
            "Adjust their routines and approach to fit the new environment while maintaining their core goals", "Refuse to make any adjustment to the new environment",
            "Abandon all personal goals entirely upon any change", "Show a response entirely unrelated to adaptability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Life skills' as covered in this unit are considered valuable beyond the classroom mainly because they:", "options": [
            "Apply directly to everyday personal, social, and professional situations throughout life", "Apply only within a formal classroom examination setting",
            "Have no practical relevance once a student leaves school", "Are relevant only to a single, narrow profession"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best distinguishes 'assertiveness' from 'aggressiveness' as life skills?", "options": [
            "Assertiveness expresses one's own needs while still respecting others, while aggressiveness disregards others' needs entirely", "The two terms describe exactly the same behaviour",
            "Aggressiveness is always the more socially constructive approach", "Assertiveness always involves ignoring one's own needs entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'resilience' is considered a particularly important life skill for young people transitioning to adulthood?", "options": [
            "It equips them to handle setbacks constructively as they face increasing independence and responsibility", "Resilience has no relevance to the challenges of early adulthood",
            "Young people never encounter any setbacks requiring resilience", "Resilience is relevant only to professional athletes"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A workplace scenario requiring both 'teamwork' and 'conflict resolution' skills together would most likely involve:", "options": [
            "Collaborating with colleagues on a shared project while constructively managing any disagreements that arise", "Working entirely alone with no interaction with colleagues",
            "Avoiding any project that involves more than one person", "A scenario where neither skill has any relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises why this unit groups together skills like resilience, adaptability, leadership, and ethical decision-making under 'Life Skills'?", "options": [
            "They are all practical, transferable competencies that support effective personal, social, and professional functioning", "They share no common theme or purpose",
            "They are relevant only to Social Studies exams, not to real life", "They apply only to a single, narrow occupation"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35065: [  # Unit 5: Geography and Social Relation
        {"q": "'Human geography' focuses primarily on the study of:", "options": [
            "The relationship between people and their physical/social environment", "Only the physical structure of rocks and minerals",
            "Only outer space and astronomical phenomena", "A subject unrelated to people or environment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's geography is broadly divided into three major regions:", "options": [
            "Himalayan (mountain), Hilly, and Terai (plain) regions", "Desert, tundra, and rainforest regions",
            "Coastal, island, and volcanic regions", "Only a single uniform geographic region"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The relationship between geography and social life is evident in how physical terrain influences:", "options": [
            "Settlement patterns, livelihoods, and cultural practices of communities", "Nothing at all - geography has no social influence",
            "Only the colour of a region's flag", "Only a country's currency exchange rate"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Climate' significantly influences social life by shaping:", "options": [
            "Agricultural practices, clothing, housing styles, and economic activities of a region", "Only a country's political party system",
            "Only the stock market's daily performance", "A factor entirely unrelated to human activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Urbanization' refers to the process by which:", "options": [
            "An increasing proportion of a population comes to live in urban (city) areas", "A population moves exclusively toward rural areas with no urban growth",
            "Cities are physically relocated to entirely different regions", "A concept unrelated to population distribution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's Terai region is significant to the national economy mainly due to its:", "options": [
            "Fertile agricultural land supporting a large share of food production", "Complete absence of any agricultural activity",
            "Exclusively mountainous terrain with no plains", "Location entirely outside Nepal's borders"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Migration' as a geographic and social phenomenon refers to:", "options": [
            "The movement of people from one place to another, often for economic or social reasons", "A population that never moves from its original location",
            "A term unrelated to human movement", "A concept limited exclusively to animal movement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Natural resources' available in a region, such as water or forests, influence social life by shaping:", "options": [
            "Local livelihoods, industries, and patterns of resource-based economic activity", "A country's national anthem",
            "A concept unrelated to livelihoods or economy", "Only a country's diplomatic protocol"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's hilly region is characterised, among other things, by:", "options": [
            "Terraced farming adapted to sloped terrain", "Entirely flat land with no elevation change",
            "A complete absence of any agricultural activity", "Coastal fishing as the dominant economic activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Rural-urban migration' in Nepal has been driven partly by:", "options": [
            "The search for better employment, education, and services in urban areas", "A government requirement with no economic or social motive",
            "A decline in urban opportunities relative to rural areas", "Higher agricultural income than urban income in every case"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Deforestation' as an environmental-social issue can lead to social consequences such as:", "options": [
            "Loss of livelihoods dependent on forest resources and increased vulnerability to disasters like landslides", "An automatic increase in agricultural productivity with no downside",
            "No social consequence of any kind", "A guaranteed improvement in the local economy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Geographic isolation of remote mountain communities in Nepal has historically contributed to:", "options": [
            "Limited access to markets, education, and health services in those areas", "Immediate and equal access to all national services with no disparity",
            "No effect on access to services of any kind", "A guaranteed higher standard of living compared to urban areas"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Population density' refers to:", "options": [
            "The number of people living per unit of area (e.g. per square kilometre)", "The total land area of a country with no reference to population",
            "A measure entirely unrelated to population", "The total number of countries in a region"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Kathmandu Valley's high population density compared to many other parts of Nepal reflects its role as a centre of:", "options": [
            "Economic opportunity, education, and administrative activity", "Complete isolation with no economic or administrative role",
            "The country's least accessible and most remote terrain", "A region with no history of settlement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Environmental degradation' can affect social relations within a community by:", "options": [
            "Straining shared resources and potentially increasing competition or conflict over their use", "Automatically strengthening social bonds with no strain on resources",
            "Having no impact on community relationships whatsoever", "Guaranteeing an increase in the community's resource abundance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Regional disparity' in development across Nepal often reflects differences in:", "options": [
            "Geographic accessibility, infrastructure, and resource distribution across regions", "A uniform, identical level of development in every region",
            "A factor entirely unrelated to geography", "Only differences in regional flag design"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why Nepal's diverse geography (mountains, hills, plains) has led to significant cultural diversity across the country?", "options": [
            "Different terrains historically shaped distinct livelihoods, isolation levels, and cultural practices among communities", "Nepal's geography has had no influence on its cultural diversity",
            "Cultural diversity in Nepal exists entirely independent of geographic factors", "All regions of Nepal have identical geography with no variation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the social significance of studying the relationship between geography and settlement patterns?", "options": [
            "It helps explain why populations concentrate in certain areas and informs planning for infrastructure and services", "Settlement patterns have no relationship to geography whatsoever",
            "This relationship is relevant only to historical settlements, not present-day planning", "Geography has no bearing on where people choose to live"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A community heavily reliant on a single natural resource (e.g. a specific crop or forest product) faces particular social/economic vulnerability because:", "options": [
            "Depletion or price shocks affecting that resource can directly threaten the community's livelihood with few alternatives", "Such reliance guarantees permanent economic stability with no risk",
            "Natural resources have no bearing on a community's economic wellbeing", "Diversification of livelihoods would have no protective benefit in such a case"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall relationship examined in this unit between geography and social life?", "options": [
            "Physical geography shapes patterns of settlement, livelihood, culture, and social organisation across regions", "Geography and social life are entirely unrelated fields of study",
            "Social life is determined solely by government policy with no geographic influence", "Geography influences only weather patterns, not any aspect of society"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35063: [  # Unit 6: World History
        {"q": "The term 'World History' refers to the study of:", "options": [
            "Major historical developments and events across different civilizations and regions of the world", "Only the history of a single country, in isolation from the rest of the world",
            "Only recent events from the last five years", "A subject with no historical dimension"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Renaissance' in European history refers to a period marked by:", "options": [
            "A revival of art, learning, and culture, generally dated from the 14th to 17th centuries", "A period of complete cultural stagnation with no intellectual activity",
            "A modern 21st-century technological movement", "A period unrelated to art, culture or learning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Industrial Revolution', beginning in Britain in the 18th century, was primarily characterised by:", "options": [
            "A major shift from hand production to machine-based manufacturing", "A complete return to purely agricultural, pre-industrial society",
            "A political revolution with no economic or technological dimension", "A period with no lasting global impact"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'French Revolution' (beginning 1789) is significant in world history mainly for advancing ideas of:", "options": [
            "Liberty, equality, and fraternity, challenging traditional monarchical rule", "Strengthening absolute monarchy with no challenge to royal power",
            "A purely religious reform movement with no political dimension", "An event with no lasting historical significance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "World War I (1914-1918) is generally considered to have been triggered by a complex mix of factors including:", "options": [
            "Alliances, nationalism, imperialism, and a specific triggering assassination", "A single, isolated natural disaster with no political cause",
            "A dispute over a sporting competition", "An event with no identifiable cause"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "World War II (1939-1945) formally began with:", "options": [
            "Germany's invasion of Poland in 1939", "A peaceful diplomatic agreement with no military conflict",
            "An event confined only to Asia with no European involvement", "A conflict that had no international dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The United Nations (UN), established in 1945, was created primarily to:", "options": [
            "Promote international peace, security, and cooperation among nations", "Promote conflict and discourage cooperation between nations",
            "Serve as a purely ceremonial organisation with no functional role", "Replace all national governments worldwide"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Cold War' refers to the prolonged geopolitical tension primarily between:", "options": [
            "The United States and the Soviet Union (and their respective allies) after World War II", "Nepal and India during the same period",
            "Two European countries with no global significance", "A conflict involving direct large-scale military combat between the two superpowers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Decolonization', a major 20th-century global process, refers to:", "options": [
            "Former colonies gaining independence from colonial powers", "Countries voluntarily becoming colonies of other powers",
            "A process limited only to a single continent", "A concept unrelated to colonial history"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Russian Revolution' of 1917 led to:", "options": [
            "The overthrow of the Russian monarchy and the eventual establishment of a communist government", "The strengthening of the existing Russian monarchy with no change in government",
            "No significant change to Russia's political system", "An event confined entirely to economic matters with no political change"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Age of Exploration' (roughly 15th-17th centuries) was marked by European powers:", "options": [
            "Undertaking overseas voyages leading to new trade routes and colonization", "Withdrawing entirely from any overseas contact",
            "Focusing exclusively on internal European affairs with no exploration", "An era with no lasting global historical impact"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The League of Nations, formed after World War I, was ultimately considered to have failed largely because it:", "options": [
            "Lacked enforcement power and key major powers did not fully participate, failing to prevent further major conflict", "Successfully prevented all future international conflicts with no exceptions",
            "Was replaced immediately by the United Nations with no gap in time", "Had no relationship to preventing international conflict"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Globalization' as a historical process refers to the increasing:", "options": [
            "Interconnectedness of economies, cultures, and societies across the world", "Isolation of countries from any international interaction",
            "Uniformity of every country's government structure", "A concept unrelated to international connection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The end of the Cold War is commonly associated with:", "options": [
            "The dissolution of the Soviet Union in 1991", "The start of World War I", "The founding of the League of Nations",
            "The beginning of the Industrial Revolution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Universal Declaration of Human Rights (1948) established by the United Nations aimed to:", "options": [
            "Set out fundamental rights and freedoms to be universally protected", "Grant rights exclusively to citizens of a single specific country",
            "Have no binding moral or political significance internationally", "Focus exclusively on economic rights with no reference to civil or political rights"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Studying world history alongside Nepal's own history helps students to:", "options": [
            "Understand how global events and trends have influenced, and been influenced by, Nepal's own historical trajectory", "Study Nepal in complete isolation from any global context",
            "Ignore any connection between Nepal and world events", "Focus exclusively on unrelated foreign trivia with no connection to Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why the two World Wars are considered pivotal turning points in modern world history?", "options": [
            "They reshaped international borders, political systems, and led to the creation of new international institutions aimed at preventing future conflict", "They had no lasting impact on international politics or institutions",
            "They were minor, regional conflicts with no global significance", "They resulted in no political or institutional changes of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the historical significance of decolonization for countries in Asia and Africa during the 20th century?", "options": [
            "It allowed many nations to gain political independence and begin building their own governance and development paths", "It had no effect on the political status of these regions",
            "It resulted in these regions remaining permanently under colonial rule", "Decolonization is a concept relevant only to European history"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes the Cold War from a 'hot' (direct military) war between the two major powers involved?", "options": [
            "The Cold War was characterised primarily by political, ideological, and proxy conflict rather than direct large-scale combat between the US and USSR", "The Cold War involved direct, large-scale military combat between the United States and the Soviet Union",
            "There is no meaningful distinction between the two terms", "The Cold War refers only to a specific weather-related military campaign"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall value of studying World History within a Social Studies curriculum?", "options": [
            "It helps students understand global interconnections, the origins of current international institutions, and broader patterns shaping human societies", "World History has no relevance to understanding present-day society",
            "It focuses exclusively on isolated dates with no broader significance", "Studying world history replaces the need to understand one's own national history"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35071: [  # Unit 7: Social Identity, Diversity and Class Division
        {"q": "'Social identity' refers to the aspects of a person's identity that are derived from:", "options": [
            "Their membership in social groups such as ethnicity, religion, or community", "Only their individual physical height",
            "A concept unrelated to group membership", "Only their personal financial assets"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal is widely recognised for its significant:", "options": [
            "Ethnic, linguistic, and cultural diversity", "Complete cultural and linguistic uniformity with no diversity",
            "A single, unified ethnic identity with no variation", "An absence of any distinct cultural or linguistic groups"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Social class' generally refers to divisions within society based primarily on:", "options": [
            "Economic status, occupation, and access to resources", "A person's exact height and physical appearance",
            "A concept unrelated to economic or social position", "Only a person's astrological sign"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Caste system', historically significant in South Asian societies including Nepal, refers to a form of:", "options": [
            "Hereditary social stratification traditionally linked to occupation and social status", "A modern voluntary social club with no hereditary basis",
            "A system unrelated to social stratification", "A purely economic classification with no social/historical basis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social inclusion' as a policy goal aims to:", "options": [
            "Ensure marginalised or excluded groups have equal access to opportunities and participation in society", "Deliberately exclude marginalised groups from social participation",
            "Apply only to already-privileged groups in society", "A concept with no relevance to social policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Ethnic diversity' in Nepal is reflected in the presence of numerous distinct groups such as:", "options": [
            "Newar, Tamang, Gurung, Magar, Tharu, and many others, among Nepal's many recognised ethnic communities", "A country with only a single recognised ethnic group",
            "Groups found exclusively outside Nepal's borders", "A concept irrelevant to Nepal's demographic makeup"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Gender identity and equality' within social studies concerns issues such as:", "options": [
            "Equal rights, opportunities, and treatment regardless of gender", "A topic with no relevance to social studies",
            "Guaranteeing unequal treatment based on gender as an established norm", "A concept limited exclusively to legal studies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Marginalisation' refers to the process by which certain groups are:", "options": [
            "Pushed to the periphery of society, with limited access to resources, rights, or opportunities", "Given preferential treatment above all other groups in every respect",
            "Guaranteed the most resources and opportunities in society", "A term unrelated to social exclusion"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's 2015 constitution formally recognises the country's diversity by, among other things:", "options": [
            "Establishing a federal structure and provisions aimed at inclusion of diverse groups", "Declaring the country to have only a single, uniform culture with no diversity",
            "Eliminating any reference to social or ethnic diversity", "Removing federal structures entirely in favour of a fully unitary, undifferentiated state"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social stratification' refers to the hierarchical arrangement of individuals in society based on:", "options": [
            "Factors such as wealth, power, and social status", "A random and meaningless arrangement with no basis",
            "Only geographic location with no reference to wealth or status", "A concept unrelated to any societal hierarchy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Affirmative action' or reservation policies are sometimes implemented to:", "options": [
            "Address historical disadvantage faced by marginalised groups by improving their access to opportunities", "Further disadvantage marginalised groups intentionally",
            "Apply exclusively to already-privileged groups", "A concept with no connection to social equity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Multiculturalism' as a social value promotes:", "options": [
            "The coexistence and mutual respect of diverse cultural groups within a society", "The forced elimination of all cultural diversity within a society",
            "A policy of isolating cultural groups from one another entirely", "A concept irrelevant to socially diverse nations like Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Linguistic diversity' in Nepal is reflected in the country having:", "options": [
            "Well over a hundred distinct spoken languages recognised across different communities", "Only a single language spoken nationwide with no variation",
            "No officially recognised languages at all", "Languages found exclusively outside Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Class division' can influence access to education and healthcare because:", "options": [
            "Economic status often affects a family's ability to afford or access quality services", "Economic status has no bearing on access to education or healthcare in any society",
            "All social classes have identical access to services in every society", "This concept applies only to countries with no economic inequality"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social harmony' among Nepal's diverse groups is often promoted through policies emphasising:", "options": [
            "Mutual respect, inclusive governance, and equal rights across different communities", "Forced assimilation of all groups into a single identity with no diversity",
            "Systematic exclusion of specific ethnic or social groups", "A policy of ignoring diversity entirely with no active promotion of harmony"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why understanding social identity and diversity is important for civic life in Nepal specifically?", "options": [
            "Nepal's high ethnic, linguistic, and cultural diversity means inclusive, informed citizenship requires understanding and respecting these differences", "Nepal has no significant social or ethnic diversity to consider",
            "Civic life in Nepal requires ignoring all forms of social diversity", "This topic is relevant only to countries other than Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the relationship between historical caste-based stratification and present-day social inclusion policy in Nepal?", "options": [
            "Inclusion policies are partly designed to address disadvantages that trace back to historical caste-based social structures", "Caste-based stratification has no historical connection to any present-day social policy",
            "Social inclusion policy exists entirely independent of any historical context", "Caste-based stratification never existed in Nepal's history"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A policy promoting equal representation of historically marginalised ethnic groups in government positions is an example of addressing which concept covered in this unit?", "options": [
            "Social inclusion and reducing marginalisation", "Promoting deliberate exclusion of marginalised groups",
            "Eliminating ethnic diversity entirely", "A concept unrelated to social identity or class"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Social Identity, Diversity and Class Division'?", "options": [
            "Understanding how identity, diversity, and social stratification shape access to opportunity and social relationships in Nepal", "A focus exclusively on unrelated economic statistics with no reference to identity or class",
            "A topic with no relevance to Nepal's actual society", "A purely historical topic with no connection to present-day social issues"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A community celebrating multiple distinct festivals belonging to different ethnic groups within the same municipality illustrates:", "options": [
            "Nepal's social and cultural diversity coexisting within a shared civic space", "A society with a single, uniform culture and no diversity",
            "A concept unrelated to social identity or diversity", "A scenario impossible under Nepal's actual demographic makeup"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35073: [  # Unit 8: Constitution and Civic Awareness
        {"q": "A 'constitution' is best defined as:", "options": [
            "The fundamental legal document establishing a country's system of governance, rights, and duties", "A casual, informal set of unwritten social customs",
            "A document with no legal authority whatsoever", "A purely religious text with no governance role"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's current constitution was promulgated in the year:", "options": [
            "2015 (2072 BS)", "1990", "1962", "2006"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's 2015 constitution established the country as a:", "options": [
            "Federal Democratic Republic", "Absolute monarchy", "A unitary state with no federal structure",
            "A colony under foreign administration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Under Nepal's federal structure, government is organised into how many main tiers?", "options": [
            "Three - federal, provincial, and local", "One single tier only", "Five separate tiers",
            "Two tiers only, with no local government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Fundamental rights' guaranteed by a constitution typically include rights such as:", "options": [
            "Equality, freedom of expression, and freedom from discrimination", "Rights that apply only to government officials",
            "No rights of any kind for ordinary citizens", "Rights limited exclusively to property ownership"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Civic awareness' refers to a citizen's understanding of their:", "options": [
            "Rights, responsibilities, and role within the political and social system", "Personal financial investments only",
            "A concept unrelated to citizenship or governance", "Only their family's private history"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'separation of powers' principle divides government authority among:", "options": [
            "The legislative, executive, and judicial branches", "A single unified branch with no division of power",
            "Only religious institutions", "Only local governments, excluding any federal authority"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In Nepal's federal system, the 'legislative' branch at the federal level is represented by:", "options": [
            "The Federal Parliament (House of Representatives and National Assembly)", "The Supreme Court",
            "The Council of Ministers exclusively", "The local ward office only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'judiciary' in Nepal's constitutional system is primarily responsible for:", "options": [
            "Interpreting laws and administering justice, including reviewing the constitutionality of laws", "Passing new laws directly with no legislative role for parliament",
            "Managing the day-to-day administration of ministries", "Setting the country's annual national budget"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Voting rights' in Nepal's democratic system allow eligible citizens to:", "options": [
            "Participate in elections to choose their representatives at various levels of government", "Directly appoint judges to the Supreme Court",
            "Set the national budget without any parliamentary role", "A right that applies only to government employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Rule of law' as a constitutional principle means that:", "options": [
            "All individuals, including those in government, are subject to and accountable under the law", "Only ordinary citizens are subject to the law, while officials are exempt",
            "The law applies inconsistently based on a person's social status", "There is no need for laws to be consistently applied to anyone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Nepal's constitution includes provisions on 'directive principles' of the state, which:", "options": [
            "Provide guiding policy goals for the state, such as social justice and economic development", "Are strictly binding court orders with immediate legal enforcement",
            "Have no relevance to government policy direction", "Apply exclusively to private businesses, not government"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Civic duties' of a citizen, complementing their rights, typically include responsibilities such as:", "options": [
            "Obeying the law, paying taxes, and participating in civic life", "No responsibilities whatsoever, only rights",
            "Responsibilities that apply exclusively to elected officials", "A concept unrelated to citizenship"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'local government' tier in Nepal's federal structure is primarily responsible for services such as:", "options": [
            "Local infrastructure, basic services, and local-level administration", "Setting national foreign policy exclusively",
            "Managing the country's central bank", "Conducting national-level diplomatic negotiations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A constitutional amendment process typically requires:", "options": [
            "A specified special procedure, often involving a supermajority in parliament, to ensure changes are carefully deliberated", "No process at all - amendments can be made by any single individual instantly",
            "Amendments made exclusively through informal social consensus with no legal procedure", "A process identical to passing an ordinary law with no special requirement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Civic participation', such as voting or engaging in public consultations, strengthens democracy by:", "options": [
            "Ensuring government decisions reflect the input and interests of the citizens they affect", "Having no meaningful effect on government decision-making",
            "Undermining the legitimacy of elected government", "Applying only to citizens with a specific occupation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why Nepal's 2015 constitution establishing federalism was a significant governance change?", "options": [
            "It devolved power to newly created provincial and local governments, decentralising decision-making that was previously more centralised", "It had no effect on how government authority was distributed",
            "It eliminated all levels of government below the federal level", "It centralised all governmental authority exclusively at the federal level"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the constitutional principle of 'separation of powers' and its purpose?", "options": [
            "Dividing authority among branches of government helps prevent any single branch from becoming too powerful, supporting checks and balances", "It ensures a single branch of government controls all governmental functions without any check",
            "It has no relationship to preventing abuse of governmental power", "It applies only to countries without a constitution"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates active 'civic awareness' in practice?", "options": [
            "A citizen understanding their voting rights and participating in a local election", "A citizen who is entirely unaware of their basic legal rights and responsibilities",
            "A citizen who actively avoids any engagement with civic or political matters", "A concept with no practical, real-world application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of studying the Constitution and civic awareness within Social Studies?", "options": [
            "To help students understand their rights, responsibilities, and the structure of governance so they can participate meaningfully as informed citizens", "To memorise legal text with no practical understanding of governance",
            "To discourage any citizen participation in governance", "A topic with no relevance to a student's future civic life"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35079: [  # Unit 9: Settlement, Population and Development
        {"q": "A 'settlement' in geographic/social terms refers to:", "options": [
            "A place where people establish a permanent or semi-permanent community", "A legal document unrelated to population or place",
            "A term used only in financial/banking contexts", "A concept unrelated to where people live"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Rural settlements' are typically characterised by:", "options": [
            "Lower population density and reliance on agriculture-based livelihoods", "Extremely high population density with no agricultural activity",
            "A complete absence of any human population", "Exclusively industrial and financial economic activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Urban settlements' are typically characterised by:", "options": [
            "Higher population density and a concentration of commercial, industrial, and administrative activity", "Extremely low population density with no economic activity",
            "Exclusively agricultural livelihoods with no other economic activity", "A complete absence of any infrastructure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's national population census, conducted periodically, provides essential data on:", "options": [
            "The size, distribution, and demographic characteristics of the population", "Only the country's total land area with no population data",
            "Only the country's foreign trade statistics", "A concept unrelated to population planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Population growth rate' refers to the rate at which a population:", "options": [
            "Increases (or decreases) over a specific period of time", "Remains permanently and exactly fixed with no change",
            "Is measured only once in a country's entire history", "Has no relationship to birth or death rates"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Development' in a social studies context broadly refers to:", "options": [
            "Improvement in a society's economic, social, and human wellbeing over time", "A concept limited exclusively to building physical roads",
            "A decline in a country's overall standard of living", "A term unrelated to economic or social progress"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sustainable development' emphasises meeting present needs:", "options": [
            "Without compromising the ability of future generations to meet their own needs", "While completely ignoring any consideration for future generations",
            "By exhausting all available natural resources immediately", "With no reference to environmental or social factors"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human Development Index (HDI)' is a composite measure used to assess a country's development based on:", "options": [
            "Life expectancy, education, and standard of living (income)", "Only a country's total land area",
            "Only a country's military budget", "A measure unrelated to human wellbeing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Urban sprawl', a concern in rapidly growing cities like Kathmandu, refers to:", "options": [
            "The often unplanned, outward expansion of urban areas", "A planned and highly organised urban contraction",
            "A term unrelated to city growth patterns", "A decline in city population with no expansion"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Infrastructure development', such as roads and electricity, is important for settlement growth because it:", "options": [
            "Improves accessibility and living standards, encouraging further settlement and economic activity", "Has no relationship to where or how communities develop",
            "Actively discourages any settlement or economic growth", "Is relevant only to rural areas, never urban areas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Population pyramid' is a graphical tool used to represent:", "options": [
            "The age and sex distribution of a population", "A country's total government budget by year",
            "A tool unrelated to demographic data", "Only a country's export figures"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'youthful population structure', common in many developing countries, is characterised by:", "options": [
            "A relatively high proportion of children and young people compared to older age groups", "A population consisting almost entirely of elderly individuals",
            "An exactly equal number of people at every single age", "A population with no distinguishable age structure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Planned settlement development' aims to:", "options": [
            "Ensure organised growth of settlements with adequate infrastructure and services", "Encourage completely unregulated, chaotic settlement growth",
            "Prevent any settlement growth whatsoever", "A concept unrelated to urban or rural planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Migration from rural to urban areas can put pressure on urban infrastructure such as:", "options": [
            "Housing, water supply, and transportation systems", "A country's foreign embassies exclusively",
            "A factor entirely unrelated to city services", "Only a city's tourism promotion budget"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Balanced regional development' as a policy goal seeks to:", "options": [
            "Reduce disparities in development between different regions of a country", "Concentrate all development exclusively in a single region",
            "Ignore regional differences in development entirely", "Focus development efforts only on the capital city"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Demographic transition' describes the historical shift many countries experience from:", "options": [
            "High birth and death rates to lower birth and death rates as a society develops", "Low population growth directly to zero population with no other stages",
            "A process unrelated to birth or death rates", "A single unchanging population pattern with no transition"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why rapid, unplanned urban growth (like in parts of Kathmandu Valley) can create social and infrastructural challenges?", "options": [
            "Infrastructure and services may not expand fast enough to keep pace with population growth, straining housing, water, and transport systems", "Rapid urban growth always occurs with infrastructure automatically keeping pace, with no challenge",
            "Unplanned growth has no relationship to infrastructure or service provision", "Urban growth in Nepal has historically always been carefully planned with zero informal settlement"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why population data (such as from a national census) is essential for development planning?", "options": [
            "It allows planners to allocate resources like schools, hospitals, and infrastructure based on actual population size and distribution", "Population data has no relevance to how government resources are allocated",
            "Development planning can be done effectively with no reference to population figures", "Census data is relevant only to a country's tax department"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes 'development' from simple 'economic growth'?", "options": [
            "Development encompasses broader improvements in wellbeing (health, education, equity), not just an increase in economic output", "Development and economic growth are always exactly identical concepts",
            "Economic growth always guarantees improved wellbeing with no exception", "Development refers only to physical infrastructure with no social dimension"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this unit on settlement, population, and development?", "options": [
            "Understanding how population patterns and settlement growth relate to development challenges and planning needs", "A focus exclusively on unrelated historical trivia with no development relevance",
            "A topic with no connection to real policy or planning decisions", "A purely mathematical topic with no social studies relevance"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35081: [  # Unit 10: Economy and Development
        {"q": "A country's 'economy' broadly refers to the system through which:", "options": [
            "Goods and services are produced, distributed, and consumed within a society", "Only government ministries operate with no reference to production or consumption",
            "A single company's internal operations, unrelated to the broader society", "A concept unrelated to production or consumption"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's economy has historically relied significantly on:", "options": [
            "Agriculture, remittances, and tourism", "Large-scale oil exports", "Heavy industrial manufacturing as the dominant sector",
            "Deep-sea fishing as its primary economic activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Gross Domestic Product (GDP)' is commonly used to measure:", "options": [
            "The total value of goods and services produced within a country over a specific period", "A country's total population size",
            "A country's total land area", "A measure unrelated to economic output"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Remittance', a significant contributor to Nepal's economy, refers to:", "options": [
            "Money sent home by Nepali workers employed abroad", "A form of government tax collection",
            "A type of import tariff", "A concept unrelated to foreign employment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'informal economy', significant in many developing countries including Nepal, refers to economic activity that is:", "options": [
            "Not officially registered or regulated by the government", "Exclusively large-scale corporate activity",
            "Fully documented and taxed with no informal component", "A concept unrelated to economic activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Economic development' differs from simple economic growth in that development also considers:", "options": [
            "Improvements in living standards, equity, and overall wellbeing, not just output growth", "Only the total value of exports, with no reference to wellbeing",
            "A concept identical in every respect to economic growth", "Only a country's military expenditure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Poverty' in an economic and social context refers to a state where individuals or households:", "options": [
            "Lack sufficient income or resources to meet basic needs", "Have more than sufficient resources to meet every possible need",
            "Are guaranteed a fixed minimum income regardless of circumstances", "A concept unrelated to income or resources"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Unemployment' refers to a situation in which individuals who are:", "options": [
            "Willing and able to work cannot find suitable employment", "Retired and no longer seeking work of any kind",
            "Fully and satisfactorily employed in their preferred job", "Uninterested in ever working under any circumstance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's classification as a 'Least Developed Country (LDC)' historically reflected factors such as:", "options": [
            "Low income levels, weak human assets, and economic vulnerability", "An extremely high income level with no development challenges",
            "A classification unrelated to income or human development indicators", "A purely political label with no economic basis"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Foreign direct investment (FDI)' refers to investment made by:", "options": [
            "A foreign entity into productive assets or businesses within a country", "Only domestic citizens investing within their own country",
            "A government agency investing exclusively in foreign government bonds", "A concept unrelated to cross-border investment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Infrastructure development', such as roads, electricity, and telecommunications, supports economic development mainly by:", "options": [
            "Enabling more efficient production, trade, and access to markets and services", "Having no relationship to a country's economic activity",
            "Actively discouraging trade and economic activity", "Being relevant only to a country's foreign policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human capital', a key factor in economic development, refers to:", "options": [
            "The skills, education, and health of a population that contribute to productivity", "Only the physical currency circulating in an economy",
            "A concept unrelated to a country's workforce", "Only a country's natural mineral resources"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Income inequality' refers to:", "options": [
            "The uneven distribution of income among individuals or households within a society", "A situation where every individual earns an identical income",
            "A measure of a country's total government spending", "A concept unrelated to income distribution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's Sustainable Development Goals (SDG) commitments include targets related to:", "options": [
            "Poverty reduction, education, health, and sustainable economic growth", "Exclusively military expenditure targets",
            "No development-related targets whatsoever", "Targets relevant only to already fully-developed nations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Public investment' in sectors like education and health is often justified on the grounds that it:", "options": [
            "Builds human capital and long-term productive capacity for the economy", "Has no long-term benefit to a country's economy",
            "Should be avoided entirely in favour of private investment only", "Is relevant only to already wealthy countries"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Diversifying the economy' away from heavy reliance on a single sector (e.g. remittances) is often recommended to:", "options": [
            "Reduce economic vulnerability to shocks affecting that single sector", "Increase a country's dependence on a single economic sector",
            "Guarantee an immediate increase in national income with no further effort", "Eliminate the need for any economic planning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why remittances have played such a significant role in Nepal's economy in recent decades?", "options": [
            "Large-scale foreign labour migration has generated substantial inflows that support household consumption and foreign exchange reserves", "Remittances have had no measurable impact on Nepal's economy",
            "Nepal's economy has relied primarily on large-scale industrial exports rather than remittances", "Foreign labour migration from Nepal has been historically insignificant"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why economic development is considered a broader concept than GDP growth alone?", "options": [
            "GDP growth doesn't necessarily capture improvements in equity, health, education, or overall quality of life", "GDP growth and development are always identical, with no meaningful distinction",
            "Development is measured exclusively by a country's total exports", "GDP has no relevance to assessing an economy at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the concept of the 'informal economy' in the context of Nepal?", "options": [
            "A small, unregistered roadside vendor operating without formal business registration or tax reporting", "A large multinational corporation fully registered and paying all applicable taxes",
            "A government ministry's official budget allocation", "A publicly listed company's shares traded on the stock exchange"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Economy and Development'?", "options": [
            "Understanding the structure of Nepal's economy and the broader concept of development beyond simple economic growth", "A focus exclusively on unrelated foreign economic systems with no reference to Nepal",
            "A purely historical topic with no connection to present-day economic policy", "A topic with no relevance to a student's understanding of society"],
         "correct": 0, "difficulty": "Medium"},
    ],
    35077: [  # Unit 11: Health Service and Social Development
        {"q": "'Public health' refers to efforts organised to:", "options": [
            "Promote and protect the health of a population as a whole", "Focus exclusively on treating a single individual patient with no broader population focus",
            "A concept unrelated to community wellbeing", "Only address health issues in wealthy communities"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Nepal's health service system is generally organised across tiers including:", "options": [
            "Local health posts, district hospitals, and higher-level referral hospitals", "A single national hospital with no other facilities",
            "Exclusively private hospitals with no public health infrastructure", "No organised tiers of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Maternal and child health' services focus specifically on the health needs of:", "options": [
            "Mothers during pregnancy/childbirth and children in their early years", "Only elderly individuals with no reference to mothers or children",
            "A concept unrelated to family health", "Only adult male patients"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Immunization programs' aim to protect populations from disease primarily by:", "options": [
            "Providing vaccines that build immunity against specific infectious diseases", "Providing no medical intervention of any kind",
            "Treating diseases only after a severe outbreak has already occurred, with no prevention", "A concept unrelated to disease prevention"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Health and social development' are closely linked because improved health outcomes typically contribute to:", "options": [
            "Greater productivity, better education outcomes, and overall improved quality of life", "A decline in a population's overall productivity",
            "No measurable social or economic benefit", "A factor entirely unrelated to broader social development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Universal health coverage' as a policy goal aims to ensure that:", "options": [
            "All individuals have access to essential health services without financial hardship", "Only wealthy individuals have access to any health service",
            "Health services are provided exclusively to government employees", "A concept unrelated to healthcare access"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sanitation and hygiene' initiatives contribute to public health primarily by:", "options": [
            "Reducing the spread of infectious and waterborne diseases", "Having no relationship to disease prevention",
            "Increasing the spread of infectious disease", "A concept unrelated to community health"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Nutrition programs', particularly for children, aim to address issues such as:", "options": [
            "Malnutrition and stunted growth, supporting healthy physical and cognitive development", "A concept entirely unrelated to child development",
            "Only adult dietary preferences with no relevance to children", "Programs with no measurable health benefit"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Community health workers' play a role in Nepal's health system primarily by:", "options": [
            "Delivering basic health services and health education, especially in underserved/rural areas", "Performing complex surgical procedures exclusively in city hospitals",
            "Having no defined role within the health system", "Managing the national health budget independently"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Health awareness campaigns' aim to improve public health outcomes by:", "options": [
            "Educating the public about disease prevention, healthy practices, and available services", "Deliberately withholding health information from the public",
            "A concept unrelated to public health improvement", "Providing no useful information to the population"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Access to quality healthcare in remote/rural areas of Nepal has historically been challenged by factors such as:", "options": [
            "Geographic isolation, limited infrastructure, and a shortage of health workers in those areas", "Universally excellent healthcare access with no regional disparity",
            "No relationship between geography and access to health services", "An oversupply of health workers in every rural area"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Life expectancy', an indicator of a population's overall health, refers to:", "options": [
            "The average number of years a person is expected to live, based on current mortality patterns", "A country's total population count",
            "A measure entirely unrelated to health outcomes", "The number of hospitals in a given country"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Mental health awareness', increasingly emphasised in health and social development policy, addresses:", "options": [
            "Psychological wellbeing alongside physical health as an important component of overall health", "Only physical health, with no consideration of psychological wellbeing",
            "A concept irrelevant to overall social development", "A concept limited exclusively to medical professionals with no public relevance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Investment in health services is often considered a form of investment in 'human capital' because it:", "options": [
            "Supports a healthier, more productive population able to contribute more effectively to society and the economy", "Has no relationship to a population's productivity",
            "Only benefits the healthcare sector itself, with no broader economic effect", "A concept unrelated to economic development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Non-communicable diseases' (e.g. diabetes, heart disease), an increasing public health concern in Nepal, are diseases that:", "options": [
            "Are not spread through direct transmission between people, often linked to lifestyle and other long-term factors", "Are spread exclusively through direct person-to-person contact, like infectious disease",
            "Have no relevance to public health policy", "Occur exclusively in already-developed countries with no relevance to Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why access to healthcare is closely tied to broader social development outcomes?", "options": [
            "Better health enables people to study, work, and participate in society more fully, supporting overall development", "Health services have no bearing on education or workforce participation",
            "Social development occurs entirely independently of a population's health status", "Healthcare is relevant only to hospitals, with no wider societal effect"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the rationale behind Nepal's efforts to expand community health worker programs in rural areas?", "options": [
            "They extend basic health services and health education to underserved areas where formal hospital infrastructure is limited", "Community health workers are intended to fully replace hospitals in every context",
            "This program has no relevance to addressing rural health access", "Rural areas in Nepal already have equal or better hospital access than urban areas"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the link between 'nutrition' and 'social development' outcomes for children?", "options": [
            "Well-nourished children tend to have better cognitive development and educational outcomes, supporting long-term social development", "Nutrition has no measurable effect on a child's cognitive or educational outcomes",
            "Social development outcomes are entirely unrelated to childhood health and nutrition", "Only adult nutrition matters for a country's long-term social development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Health Service and Social Development'?", "options": [
            "Understanding how access to health services and public health outcomes are interconnected with broader social and economic development", "A focus exclusively on hospital architecture with no reference to social development",
            "A topic unrelated to Nepal's actual health system", "A purely historical topic with no relevance to present-day health policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A rural health post providing free basic checkups and vaccinations to a local community is an example of:", "options": [
            "Public health service delivery aimed at improving community wellbeing", "A purely private, for-profit medical enterprise",
            "A concept unrelated to health service provision", "An activity with no connection to social development"],
         "correct": 0, "difficulty": "Easy"},
    ],
}
