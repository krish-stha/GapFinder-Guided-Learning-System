# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Social Studies and Life Skills Education
question bank (course 210, subject 34299 "सामाजिक अध्ययन तथा जीवनोउपायोगी
शिक्षा", which already existed as an empty 11-chapter shell before this
session).

Authored content (not content partner data - loaded with source='synthetic'
via scripts/load_by_chapter_id.py, NOT load_question_bank.py). This
subject's chapter names are exact-verified-mismatched against course 38's
Social Studies content (same "एकाइ N" unit numbering, differing exact
wording per unit - confirmed via a live query, not assumed), so linking
real content the way नेपाली/English were handled is not possible here;
this is fresh content instead. Keyed by the verified integer chapter_id
(not the Devanagari chapter name) to avoid any transcription risk -
several of these titles have real double-space/formatting quirks in the
source data.

Chapter mapping (verified live, NEB Grade 12 Social Studies & Life Skills
Education unit list):
  34699 - Unit 1: Concept of Social and Life Skills Education
  34704 - Unit 2: Digital Skills and General Research Skills as Life Skills
  34706 - Unit 3: Life Skills
  34720 - Unit 4: Development of Society and Philosophy
  34736 - Unit 5: Geography and Social Life
  34738 - Unit 6: History of Nepal
  34734 - Unit 7: Social Identity and Diversity
  34702 - Unit 8: Constitution and Civic Consciousness
  34740 - Unit 9: Urbanization and Migration
  34744 - Unit 10: Economy and Development
  34742 - Unit 11: Education and Social Development

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}. Never presented as content partner
content or as evidence about real students.
"""

QUESTIONS = {
    34699: [  # Unit 1: Concept of Social and Life Skills Education
        {"q": "At Grade 12 level, 'Social and Life Skills Education' builds on the Grade 11 foundation by:", "options": [
            "Deepening students' understanding of society while further developing applicable life competencies", "Discarding everything covered in Grade 11 with no continuity",
            "Focusing exclusively on unrelated laboratory science content", "Removing any connection to civic or social understanding"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The subject's dual focus on 'social' and 'life skills' education reflects the goal of preparing students to be:", "options": [
            "Both socially aware citizens and practically capable individuals", "Neither socially aware nor practically capable",
            "Experts in an entirely unrelated technical field", "Isolated from both society and practical life demands"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key aim of this subject at the +2 level is to prepare students for:", "options": [
            "Active, informed participation in society, further education, and working life", "A future entirely disconnected from society",
            "Passive, uninformed engagement with civic matters", "A single narrow occupation with no broader applicability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "This subject's 'integrated' nature means it draws content and methods from disciplines including:", "options": [
            "History, geography, economics, civics, and applied life-skills training", "Only advanced pure mathematics",
            "Only foreign language literature", "No recognisable academic discipline"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "At Grade 12, students are expected to apply Social Studies concepts with:", "options": [
            "Greater analytical depth and independence than at earlier grades", "Less understanding than they had in earlier grades",
            "No reference at all to previously learned content", "Complete reliance on rote memorisation with no analysis"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Lifelong learning', a value underlying this subject, refers to the idea that learning:", "options": [
            "Continues beyond formal schooling, throughout an individual's life", "Ends completely upon finishing +2 education",
            "Is relevant only during a person's childhood", "Has no relevance beyond the classroom"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Global citizenship', an increasingly emphasised concept, refers to an individual's:", "options": [
            "Awareness of and engagement with issues beyond their own national borders", "Complete disregard for any issue outside their own household",
            "Legal citizenship status only, with no broader awareness", "A concept unrelated to social studies education"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "This subject's applied focus (through 'life skills') distinguishes it from a purely theoretical subject by emphasising:", "options": [
            "Practical application of knowledge to real situations, not just theoretical understanding", "Exclusively abstract theory with no practical relevance",
            "Memorisation with no application of any kind", "A focus entirely unrelated to real-life situations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Value education', often woven into this subject, aims to help students develop:", "options": [
            "Ethical principles and social values such as honesty, respect, and responsibility", "No ethical framework of any kind",
            "Values relevant only to a single religious tradition", "A concept unrelated to civic or personal development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Grade 12 students are expected to connect Social Studies concepts to:", "options": [
            "Current national and global events and issues", "Only historical events with no reference to the present",
            "No real-world events of any kind", "Exclusively fictional scenarios with no basis in reality"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Interdependence', a concept relevant to this subject, highlights that individuals and societies:", "options": [
            "Rely on one another and on broader systems for wellbeing and functioning", "Operate in complete isolation with no reliance on others",
            "Have no meaningful connection to broader social or economic systems", "Are entirely self-sufficient with no external relationships"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "This subject encourages students to apply 'critical thinking' to social issues by:", "options": [
            "Analysing evidence and multiple perspectives before forming a judgment", "Accepting the first opinion presented with no further analysis",
            "Avoiding any independent judgment on social issues", "Relying solely on unverified rumours"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Civic engagement' at the student level might include activities such as:", "options": [
            "Participating in community service or school-level decision-making bodies", "Complete avoidance of any community or school-related activity",
            "A concept irrelevant to a +2 level student", "Only activities conducted entirely outside of Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Grade 12's Social Studies curriculum places emphasis on preparing students for the transition to:", "options": [
            "Higher education, employment, and fuller civic responsibility as young adults", "A life entirely disconnected from further education or work",
            "No transition of any kind beyond secondary school", "Exclusively technical vocational training with no civic component"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital citizenship', increasingly relevant to this subject, refers to responsible and informed:", "options": [
            "Use of digital technology and online platforms", "Complete avoidance of any digital technology",
            "A concept unrelated to social studies", "Use of technology with no reference to responsibility"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "This unit's introductory content is intended to set the stage for the rest of the Grade 12 syllabus by:", "options": [
            "Framing the subject's integrated scope of social understanding and applied life skills", "Providing entirely unrelated content with no connection to later units",
            "Focusing exclusively on a single isolated historical fact", "Replacing the need to study any further unit"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why this subject continues into Grade 12 rather than ending after Grade 11?", "options": [
            "Social understanding and life skills develop progressively, and Grade 12 deepens and extends what was introduced earlier", "There is no pedagogical reason for the subject to continue",
            "Grade 12 content is entirely unrelated to what was covered in Grade 11", "The subject exists in Grade 12 purely by administrative accident"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates 'global citizenship' in a Nepali +2 student's daily life?", "options": [
            "Following international news and understanding how global issues like climate change might affect Nepal", "Complete disinterest in any event or issue beyond the student's own household",
            "Rejecting any connection between Nepal and the rest of the world", "A concept with no practical relevance to a student's life"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the practical value of combining 'social knowledge' with 'life skills' for a student about to enter higher education or the workforce?", "options": [
            "Social knowledge provides context for informed decisions, while life skills provide the practical tools to act on them effectively", "Social knowledge and life skills serve entirely unrelated purposes with no combined benefit",
            "Only life skills matter for a student's future; social knowledge is irrelevant", "Only social knowledge matters; practical skills have no bearing on future success"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of this introductory Grade 12 unit?", "options": [
            "To establish the subject's continued integrated focus on deeper social understanding and advanced applied life skills", "To provide isolated trivia unrelated to the rest of the syllabus",
            "To discourage further study of the subject", "To focus exclusively on a single narrow historical event with no broader framing"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34704: [  # Unit 2: Digital Skills and General Research Skills as Life Skills
        {"q": "'Digital skills', as covered in this unit, refer to the ability to:", "options": [
            "Effectively and responsibly use computers, the internet, and digital tools", "Avoid using any digital device entirely",
            "Only operate outdated, non-digital equipment", "A concept unrelated to modern communication or research"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Online research skill' involves the ability to:", "options": [
            "Search for, evaluate, and use credible information found on the internet", "Accept all online information as automatically true with no evaluation",
            "Avoid using the internet for any research purpose", "A skill unrelated to gathering information"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Evaluating the 'credibility' of an online source involves checking factors such as:", "options": [
            "The author's expertise, the publisher's reputation, and supporting evidence", "Only the visual design of the webpage",
            "The number of unrelated advertisements on the page", "A factor unrelated to trustworthiness of information"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Digital literacy' includes understanding how to protect oneself from online risks such as:", "options": [
            "Misinformation, scams, and privacy breaches", "No risks exist online whatsoever",
            "Risks that apply only to offline activities", "A concept unrelated to internet use"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'General research skills' taught in this unit include the ability to:", "options": [
            "Formulate a research question, gather relevant data, and draw evidence-based conclusions", "Draw conclusions with no reference to any evidence",
            "Avoid ever forming a specific research question", "A skill unrelated to investigating any topic"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Data privacy awareness', a component of digital skills, refers to understanding how to:", "options": [
            "Protect personal information shared online", "Share all personal information publicly with no restriction",
            "A concept unrelated to online activity", "Avoid using any online service permanently"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital communication tools' such as email and messaging apps are useful life skills because they enable:", "options": [
            "Efficient, widespread communication for both personal and professional purposes", "No practical benefit for communication of any kind",
            "Communication only within a single physical room", "A concept unrelated to modern life"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Search engine literacy', part of digital research skills, involves the ability to:", "options": [
            "Use effective search strategies and keywords to find relevant, reliable information", "Only accept the very first search result with no further evaluation",
            "Avoid using any search engine entirely", "A skill unrelated to finding information online"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Misinformation', a growing digital-era concern, refers to:", "options": [
            "False or inaccurate information, whether spread intentionally or unintentionally", "Only information that is completely accurate and verified",
            "A concept unrelated to online content", "Information found exclusively in printed books"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital footprint' refers to:", "options": [
            "The trail of data a person leaves behind through their online activity", "A physical footprint left on a computer's keyboard",
            "A concept unrelated to online behaviour", "Only a company's official website content"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Citing sources properly when using online research is important primarily because it:", "options": [
            "Gives credit to original authors and helps readers verify the information's origin", "Has no relevance to academic or research integrity",
            "Is required only for printed sources, never for online sources", "Automatically improves a source's accuracy regardless of citation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Cross-checking information' across multiple credible sources helps a researcher to:", "options": [
            "Verify accuracy and reduce the risk of relying on false or biased information", "Guarantee that information is entirely accurate with a single source alone",
            "Avoid the need to consult more than one source ever", "A step unrelated to research quality"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Digital skills' are considered essential life skills in the present day largely because:", "options": [
            "A significant share of communication, education, and work now depends on digital technology", "Digital technology plays no role in modern communication or work",
            "Digital skills are relevant only to computer science professionals", "Digital technology has had no impact on how research or communication is conducted"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Using proper 'keywords' when conducting an online search helps to:", "options": [
            "Narrow results toward relevant, useful information rather than irrelevant content", "Guarantee that only false information will appear",
            "Have no effect on the relevance of search results", "Prevent any search results from appearing at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A student comparing information from a government statistics website against a random unverified social media post is practising:", "options": [
            "Evaluating source credibility as part of digital research skills", "A skill entirely unrelated to research or credibility",
            "An activity with no connection to digital literacy", "A practice that guarantees the social media post is more accurate"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Ethical use of digital information' includes avoiding practices such as:", "options": [
            "Plagiarism and spreading unverified information", "Always properly citing every source used",
            "A concept unrelated to research ethics", "Verifying information before sharing it"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'digital skills' are grouped together with 'general research skills' as life skills in this unit?", "options": [
            "In practice, most modern research now involves using digital tools responsibly to find and evaluate information", "Digital skills and research skills are entirely unrelated to one another",
            "Research skills have no application to digital environments", "This grouping serves no pedagogical purpose"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the risk of relying on a single, unverified online source for an important decision?", "options": [
            "A single unverified source may be inaccurate or biased, leading to poorly informed decisions", "A single online source is always guaranteed to be fully accurate",
            "There is no risk whatsoever in relying on any single source", "Verification of sources is relevant only for print media, not digital media"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates responsible digital citizenship in an online research context?", "options": [
            "Verifying a claim across multiple credible sources before sharing it further", "Sharing any information found online immediately without any verification",
            "Ignoring the source's credibility entirely when using information", "Avoiding the use of the internet for research under any circumstance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on digital and general research skills?", "options": [
            "Building the practical ability to find, evaluate, and responsibly use information and digital tools", "A focus exclusively on hardware repair with no reference to research or information",
            "A topic with no relevance to a student's academic or civic life", "A purely historical account of the invention of computers"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34706: [  # Unit 3: Life Skills
        {"q": "'Career planning skill', relevant at the +2 level, involves the ability to:", "options": [
            "Identify personal interests and strengths to make informed decisions about future education or career paths", "Choose a career at random with no consideration of interests or strengths",
            "A skill unrelated to a student's future path", "Avoid any planning for the future entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Financial planning skill', an important life skill, includes the ability to:", "options": [
            "Budget, save, and make informed decisions about personal finances", "Spend all available money immediately with no planning",
            "A skill unrelated to personal financial wellbeing", "Avoid any consideration of income or expenses"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Public speaking skill' involves the ability to:", "options": [
            "Communicate ideas confidently and clearly to an audience", "Avoid speaking in front of any group under any circumstance",
            "A skill unrelated to communication", "Only communicate through written text, never verbally"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Workplace readiness skills' include competencies such as:", "options": [
            "Punctuality, teamwork, and professional communication", "Skills entirely unrelated to any work environment",
            "Only technical skills specific to a single narrow job", "A complete absence of any interpersonal competency"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Critical self-reflection', a life skill for personal growth, involves:", "options": [
            "Evaluating one's own thoughts, actions, and progress to identify areas for improvement", "Avoiding any evaluation of one's own behaviour",
            "Assuming one's own actions are always perfect with no room for improvement", "A skill unrelated to personal development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Time management skill', applied to exam preparation, helps a student to:", "options": [
            "Allocate sufficient, well-organised study time across different subjects", "Study only one subject while ignoring all others entirely",
            "Avoid any planning for exam preparation", "A skill unrelated to academic performance"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Networking and relationship-building skill' can benefit a student's future career by:", "options": [
            "Creating professional connections that may lead to opportunities and support", "Isolating the student from any professional contact",
            "A skill unrelated to career development", "Guaranteeing employment with no further effort"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Adaptability to technology', an increasingly relevant life skill, involves the ability to:", "options": [
            "Learn and effectively use new digital tools as they emerge", "Refuse to learn or use any new technology",
            "A skill unrelated to career or personal development", "Rely exclusively on outdated tools with no adaptation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Constructive feedback skill' involves both giving and receiving feedback in a way that:", "options": [
            "Helps improve performance while maintaining respect and positive relationships", "Focuses only on criticism with no constructive element",
            "Avoids any feedback exchange entirely", "A skill unrelated to personal or professional growth"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Resource management skill' involves the ability to:", "options": [
            "Use available resources (time, money, materials) efficiently to achieve a goal", "Waste all available resources with no planning",
            "A skill unrelated to achieving any goal", "Ignore resource constraints entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A student practising 'career planning skill' by researching different university programs and their requirements is:", "options": [
            "Making an informed decision about their future education path", "Choosing a path entirely at random with no research",
            "Engaging in an activity unrelated to career planning", "Avoiding any consideration of their future"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Ethical leadership', an advanced life skill relevant to future roles, involves:", "options": [
            "Guiding others while upholding honesty, fairness, and accountability", "Guiding others with no regard for honesty or fairness",
            "A concept unrelated to leadership", "Avoiding any leadership role or responsibility"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Budgeting skill', part of financial planning, involves:", "options": [
            "Tracking income and expenses to plan spending within available resources", "Spending without any reference to income",
            "A skill unrelated to personal finance", "Avoiding any awareness of one's own expenses"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Interview skill', relevant for future job or university admission processes, includes the ability to:", "options": [
            "Present oneself, one's experience, and one's goals clearly and confidently", "Avoid preparing for any interview situation",
            "A skill unrelated to future opportunities", "Answer questions with no reference to the question asked"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital professionalism', an emerging life skill, involves maintaining appropriate conduct:", "options": [
            "On professional and social media platforms, being mindful of one's online presence", "With no consideration of how online behaviour might be perceived",
            "A concept unrelated to career development", "Only in offline settings, with no reference to online behaviour"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Applying 'resource management skill' to a group project would involve:", "options": [
            "Allocating time, effort, and available materials efficiently among group members to meet the project's goals", "Ignoring all resource constraints and deadlines",
            "Assigning all responsibility to a single group member with no coordination", "A concept unrelated to completing a group project effectively"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why this Grade 12 unit revisits 'life skills' with a stronger focus on career and workplace readiness compared to Grade 11?", "options": [
            "As students approach the end of secondary education, skills directly relevant to further study or employment become increasingly important", "There is no meaningful difference in focus between the Grade 11 and Grade 12 life skills units",
            "Career and workplace readiness have no relevance to a graduating +2 student", "This unit exists purely to repeat Grade 11 content with no added depth"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a student successfully applying both 'time management' and 'resource management' skills together?", "options": [
            "Planning a study schedule that allocates sufficient time to each subject while making efficient use of available study materials", "Studying at random with no schedule and no consideration of available materials",
            "Ignoring all deadlines and available resources entirely", "A scenario where neither skill has any practical relevance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'ethical leadership' is emphasised as distinct from leadership skill alone?", "options": [
            "Leadership without an ethical foundation can result in guiding others toward outcomes that are effective but unfair or dishonest", "Ethics has no relevance to how a leader guides others",
            "Ethical leadership and leadership skill are always exactly identical concepts", "Ethical considerations apply only outside of any leadership context"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this Grade 12 'Life Skills' unit?", "options": [
            "Building advanced, practically applicable competencies relevant to a student's transition to further education, career, and adult responsibilities", "A focus exclusively on unrelated recreational activities",
            "A topic with no connection to a student's future life or career", "A purely theoretical topic with no practical application"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34720: [  # Unit 4: Development of Society and Philosophy
        {"q": "'Social philosophy' broadly examines questions related to:", "options": [
            "The nature of society, justice, and how individuals ought to live together", "Only questions of pure mathematics with no social relevance",
            "A field entirely unrelated to human society", "Only questions about physical, non-social phenomena"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'evolution of human society' is often studied by examining the progression from:", "options": [
            "Hunter-gatherer societies to agricultural, industrial, and modern information-based societies", "A single, permanently unchanging form of society throughout history",
            "Modern society directly to hunter-gatherer society with no intermediate stages", "A concept unrelated to historical social change"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social contract theory', a concept in social philosophy, proposes that:", "options": [
            "Individuals consent, explicitly or implicitly, to form societies and abide by shared rules for mutual benefit", "Society exists with absolutely no basis in individual consent or agreement",
            "A concept unrelated to the formation of society", "Individuals are legally forbidden from ever forming any society"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social norms' refer to:", "options": [
            "Shared expectations and rules that guide behaviour within a society", "A concept unrelated to social behaviour",
            "Rules that apply only to a single individual in isolation", "Laws that have no connection to social expectations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social institutions', such as family, education, and religion, function to:", "options": [
            "Organise and structure important aspects of social life and meet societal needs", "Have no role in structuring any aspect of society",
            "Exist entirely independent of any social function", "Apply only to a single isolated individual, not broader society"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Modernization', a concept in the development of society, refers to the process by which societies:", "options": [
            "Transition toward more industrialized, technologically advanced, and often urbanized forms", "Revert to entirely pre-industrial forms with no technological change",
            "Remain permanently unchanged despite technological advances", "A concept unrelated to social or technological change"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cultural change' within a society can occur due to factors such as:", "options": [
            "Technological innovation, contact with other cultures, and evolving social values", "A society existing in complete isolation with no external influence of any kind",
            "A concept unrelated to any external or internal influence", "Cultural change never occurring under any circumstance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social philosophy' differs from 'sociology' primarily in that philosophy tends to focus more on:", "options": [
            "Normative questions - what ought to be - rather than purely empirical description of what is", "Only empirical, statistical data with no normative questions",
            "A field with no meaningful distinction from sociology", "Only questions unrelated to human society"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Individualism' and 'collectivism' represent contrasting social philosophies regarding:", "options": [
            "The relative importance placed on individual autonomy versus group/community interests", "A concept unrelated to social organisation",
            "Only differences in a society's climate", "A distinction relevant only to economics, not social philosophy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social change theories' attempt to explain:", "options": [
            "How and why societies transform over time", "Why societies never change under any circumstance",
            "A concept unrelated to the study of society", "Only changes in a country's physical geography"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Utilitarianism', a philosophical approach relevant to social ethics, evaluates actions based on:", "options": [
            "Whether they maximise overall wellbeing or happiness for the greatest number of people", "Whether they benefit a single individual with no reference to broader wellbeing",
            "A concept unrelated to ethical evaluation", "Random chance, with no ethical basis at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social justice', a key concept in social philosophy, concerns:", "options": [
            "Fair distribution of rights, opportunities, and resources within society", "A concept unrelated to fairness or equity",
            "Only the punishment of crimes, with no reference to distribution of resources", "The complete absence of any fairness consideration in a society"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Traditional societies', as often discussed in this context, are typically characterised by:", "options": [
            "Strong reliance on custom, established social roles, and less technological change", "Complete absence of any social structure or custom",
            "Exclusively urban, highly industrialised structures", "A concept unrelated to social organisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The tension between 'tradition' and 'modernity' in developing societies like Nepal often centres on balancing:", "options": [
            "Preserving valued cultural practices while adapting to social/economic changes and opportunities", "Complete rejection of all tradition with no consideration of cultural value",
            "Complete rejection of any modern change with no adaptation whatsoever", "A concept with no relevance to Nepal's social development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Socialization' refers to the process through which individuals:", "options": [
            "Learn the norms, values, and behaviours of their society, typically starting in childhood", "Are born with complete knowledge of all social norms, with no learning process",
            "A concept unrelated to how individuals learn social behaviour", "Learn only technical skills, with no social learning involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Studying 'philosophy of society' helps students to:", "options": [
            "Critically reflect on the values and structures underlying their own society", "Avoid any reflection on their own society's values or structures",
            "Accept every social norm uncritically with no reflection", "A concept unrelated to understanding one's own society"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'social contract theory' remains relevant to discussions of modern governance?", "options": [
            "It provides a philosophical basis for understanding the legitimacy of laws and government authority as resting on the consent of the governed", "It has no relevance to how modern governments are understood or legitimised",
            "It applies only to ancient societies with no relevance to present-day governance", "It rejects entirely the idea that government authority requires any basis in consent"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates 'modernization' occurring within Nepali society?", "options": [
            "Increasing use of digital technology and urban infrastructure alongside traditional agricultural practices", "A complete absence of any technological or infrastructural change over time",
            "A society reverting entirely to pre-industrial practices with no modern influence", "A concept with no observable manifestation in Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the ongoing debate between individualism and collectivism as applied to social policy?", "options": [
            "It reflects differing views on how much weight should be given to individual freedom versus collective/community welfare in shaping policy", "This debate has no bearing on real social or economic policy decisions",
            "Individualism and collectivism are always in complete agreement with no tension", "This debate is relevant only to ancient philosophy with no modern application"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Development of Society and Philosophy'?", "options": [
            "Understanding how societies evolve over time and the philosophical questions underlying social organisation and values", "A focus exclusively on unrelated mathematical formulas",
            "A topic with no relevance to understanding real societies", "A purely biographical account of a single philosopher with no broader concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34736: [  # Unit 5: Geography and Social Life
        {"q": "This unit examines how Nepal's physical geography continues to shape:", "options": [
            "Settlement patterns, livelihoods, and regional social/economic differences", "Nothing at all related to social or economic life",
            "Only a country's flag design", "A concept entirely unrelated to livelihoods"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Ecological zones' in Nepal, from lowland Terai to high Himalaya, support different:", "options": [
            "Agricultural practices, vegetation, and patterns of human settlement", "An identical set of agricultural practices with no variation",
            "No form of human settlement whatsoever", "A concept unrelated to agriculture or settlement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Climate change', a growing concern in Nepal's Himalayan region, poses risks such as:", "options": [
            "Glacial melt, altered rainfall patterns, and increased risk of natural disasters", "No measurable risk to Nepal's environment or society",
            "Guaranteed improvement in agricultural yields with no downside", "A concept unrelated to Nepal's geography"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Natural disaster vulnerability' in Nepal is heightened in certain areas due to factors such as:", "options": [
            "Steep terrain, seismic activity, and monsoon-related flooding/landslides", "A complete absence of any natural hazard in Nepal",
            "A concept unrelated to Nepal's physical geography", "Guaranteed immunity from any natural disaster due to geography"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Land use patterns' in Nepal vary significantly between regions due to differences in:", "options": [
            "Terrain, climate, soil fertility, and accessibility", "A single uniform pattern applied identically everywhere in Nepal",
            "A factor entirely unrelated to geography", "Only differences in a region's political party affiliation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Trans-Himalayan trade routes', historically significant to Nepal's geography and society, connected:", "options": [
            "Nepal with Tibet and other regions, facilitating cultural and economic exchange", "Nepal exclusively with countries outside of Asia",
            "No external regions whatsoever", "A concept unrelated to historical trade"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Environmental conservation efforts' in Nepal, such as protected areas and national parks, aim to:", "options": [
            "Preserve biodiversity and natural resources for ecological and social benefit", "Actively destroy natural habitats with no conservation goal",
            "A concept unrelated to Nepal's environmental policy", "Focus exclusively on urban areas with no rural conservation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Tourism', closely tied to Nepal's geography, contributes to social life by:", "options": [
            "Generating income and employment in areas with notable natural or cultural attractions", "Having no economic or social impact on local communities",
            "A concept unrelated to Nepal's mountainous or cultural geography", "Discouraging any economic activity in tourist areas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Water resources', abundant in Nepal's rivers, are socially and economically significant for:", "options": [
            "Irrigation, drinking water, and hydropower generation", "No practical use of any kind",
            "A concept unrelated to Nepal's economy or livelihoods", "Only recreational boating with no other use"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Geographic accessibility' affects social development by influencing a community's access to:", "options": [
            "Markets, education, healthcare, and government services", "No aspect of a community's social or economic life",
            "Only a community's choice of local language", "A factor entirely unrelated to community wellbeing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Climate-induced migration', an emerging concern, refers to:", "options": [
            "Population movement driven partly by environmental changes such as changing agricultural viability or disaster risk", "Migration entirely unrelated to environmental factors",
            "A concept with no relevance to Nepal's mountain communities", "Migration that occurs only for tourism-related reasons"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Hydropower potential', significant to Nepal given its river systems, represents an opportunity for:", "options": [
            "Domestic energy generation and potential energy exports", "A resource with no economic potential whatsoever",
            "A concept unrelated to Nepal's geography", "Only recreational use, with no energy generation potential"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Environmental degradation', such as deforestation or river pollution, can undermine social wellbeing by:", "options": [
            "Threatening livelihoods, health, and long-term resource availability for communities", "Automatically improving a community's health and livelihoods",
            "Having no connection to a community's economic or social wellbeing", "A concept unrelated to environmental policy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Disaster risk reduction (DRR)' strategies in geographically vulnerable areas of Nepal focus on:", "options": [
            "Minimising the impact of natural hazards through preparedness, early warning, and resilient infrastructure", "Ignoring natural hazards entirely with no preparedness",
            "A concept unrelated to Nepal's geography or social planning", "Guaranteeing complete elimination of all natural hazards"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The relationship between geography and social life illustrates how physical environment and human society are:", "options": [
            "Interconnected, with each influencing the other over time", "Entirely separate, with no meaningful interaction",
            "Unrelated fields of study with no overlap", "A relationship that exists only in theory, never in practice"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why climate change poses a particular concern for Nepal's mountain communities?", "options": [
            "Glacial melt and changing weather patterns can directly threaten water sources, agriculture, and increase disaster risk in these areas", "Climate change has no measurable effect on mountainous regions",
            "Mountain communities in Nepal are entirely unaffected by any environmental change", "This concern applies only to coastal, not mountainous, regions"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why hydropower is often highlighted as a major economic opportunity tied to Nepal's geography?", "options": [
            "Nepal's mountainous terrain and abundant rivers provide substantial potential for generating and potentially exporting electricity", "Nepal's geography provides no advantage for any form of energy generation",
            "Hydropower is entirely unrelated to a country's physical geography", "Nepal has no rivers or elevation change suitable for hydropower"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the concept of 'geographic accessibility' affecting social development?", "options": [
            "A remote mountain village with limited road access having reduced access to healthcare and education services compared to an urban area", "A scenario where geographic location has no bearing on access to any service",
            "All areas of Nepal having identical, unrestricted access to every service regardless of terrain", "A concept relevant only to countries other than Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Geography and Social Life'?", "options": [
            "Examining how Nepal's physical environment continues to shape livelihoods, settlement, vulnerability, and social/economic opportunity", "A focus exclusively on unrelated foreign geography with no reference to Nepal",
            "A purely historical topic with no connection to present-day social or economic conditions", "A topic with no relevance to development planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A village relocating its main road route to avoid a known landslide-prone slope illustrates:", "options": [
            "Adapting settlement and infrastructure planning to geographic risk factors", "A decision entirely unrelated to geography or risk",
            "A guaranteed elimination of all future landslide risk", "A practice with no real-world planning application"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34738: [  # Unit 6: History of Nepal
        {"q": "The unification of Nepal is generally credited to the leadership of:", "options": [
            "Prithvi Narayan Shah", "Bhimsen Thapa", "Jung Bahadur Rana", "Tribhuvan Shah"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Rana regime' in Nepal refers to a period of:", "options": [
            "Hereditary prime ministerial rule that significantly limited the monarch's actual power", "Direct rule by the monarch with no prime ministerial authority",
            "A period with no centralised governmental authority at all", "A period of foreign colonial administration"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Rana regime in Nepal came to an end in the year:", "options": [
            "1951", "1990", "2006", "1962"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 1990 People's Movement (Jana Andolan) in Nepal led to the establishment of:", "options": [
            "A multi-party democratic system under a constitutional monarchy", "A return to absolute monarchy with no democratic participation",
            "No change to Nepal's political system whatsoever", "Direct foreign administration of Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Nepali Civil War (Maoist insurgency), which significantly affected Nepal's history, lasted roughly from:", "options": [
            "1996 to 2006", "1950 to 1960", "1846 to 1856", "2010 to 2020"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The Comprehensive Peace Accord, ending the Maoist insurgency, was signed in the year:", "options": [
            "2006", "1990", "1951", "2015"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal was formally declared a republic, ending its monarchy, in the year:", "options": [
            "2008", "1990", "1951", "2015"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Sugauli Treaty' (1816), significant in Nepal's history, was signed following conflict with:", "options": [
            "The British East India Company", "China", "Tibet", "The Soviet Union"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "King Tribhuvan's role in Nepal's 1951 political change is significant because he:", "options": [
            "Aligned with democratic forces against Rana rule, contributing to the end of the Rana regime", "Actively supported the continuation of Rana rule with no opposition",
            "Had no involvement in Nepal's political developments of that era", "Led Nepal into an extended period of foreign colonisation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 2015 (2072 BS) earthquake was significant in Nepal's recent history primarily due to its:", "options": [
            "Devastating human and infrastructural toll, prompting major reconstruction efforts", "Complete absence of any impact on Nepal",
            "Occurrence in a year with no other significant national events", "A purely economic event with no humanitarian dimension"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's 2015 constitution, a major historical/political milestone, was promulgated following:", "options": [
            "An extended constitutional drafting process involving elected Constituent Assemblies", "A single unilateral royal decree with no assembly involvement",
            "No formal drafting process of any kind", "A process conducted entirely by a foreign government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Understanding Nepal's political transitions - from monarchy to democracy to federal republic - helps students appreciate:", "options": [
            "How Nepal's governance system evolved in response to historical social and political movements", "That Nepal's political system has remained completely unchanged throughout its history",
            "A topic with no relevance to understanding present-day Nepal", "That political change in Nepal occurred with no connection to social movements"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The first democratic elections in Nepal were held in the year:", "options": [
            "1959", "1951", "1990", "2008"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the historical significance of the 1990 People's Movement in Nepal?", "options": [
            "It ended the Panchayat system and restored multi-party democracy under a constitutional monarchy", "It had no effect on Nepal's political structure",
            "It resulted in the immediate abolition of the monarchy", "It marked the beginning of the Rana regime"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why the Maoist insurgency (1996-2006) is considered a major turning point in Nepal's modern political history?", "options": [
            "It significantly reshaped Nepal's political landscape, ultimately contributing to the end of the monarchy and the drafting of a new constitution", "It had no lasting impact on Nepal's political trajectory",
            "It occurred entirely without any connection to Nepal's later political changes", "It strengthened the monarchy's authority with no political transformation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the sequence of major political transitions in Nepal covered in this unit?", "options": [
            "From unification under monarchy, through Rana rule, to multi-party democracy, and ultimately to a federal democratic republic", "Nepal transitioned directly from Rana rule to its present system with no intermediate stages",
            "Nepal's political system has remained a monarchy throughout its entire modern history", "Nepal's history includes no significant political transitions at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why the Sugauli Treaty (1816) is considered historically significant for Nepal?", "options": [
            "It defined Nepal's boundaries following conflict with the British and shaped Nepal's subsequent foreign relations", "It had no lasting effect on Nepal's territory or foreign relations",
            "It was an internal agreement with no foreign party involved", "It marked the beginning of Nepal's unification process"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates why studying Nepal's own history is emphasised alongside World History in this Social Studies curriculum?", "options": [
            "It helps students understand the specific historical roots of Nepal's present-day political and social institutions", "Nepal's own history has no bearing on understanding its present-day institutions",
            "World History alone is sufficient to understand Nepal's present-day context", "Nepal's history is entirely disconnected from broader global historical trends"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall value of studying the 'History of Nepal' unit within Social Studies?", "options": [
            "It builds an understanding of how Nepal's political and social systems developed into their present form", "It focuses exclusively on unrelated foreign historical events",
            "It has no connection to Nepal's current governance or society", "It is relevant only to specialised history students, not general Social Studies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The promulgation of Nepal's 2015 constitution is generally regarded as the culmination of a political process that began with:", "options": [
            "The end of the decade-long Maoist insurgency and the subsequent Constituent Assembly process", "A single royal decree issued with no prior political process",
            "An entirely foreign-led drafting process with no domestic involvement", "A process unrelated to any of Nepal's earlier political transitions"],
         "correct": 0, "difficulty": "Hard"},
    ],
    34734: [  # Unit 7: Social Identity and Diversity
        {"q": "At Grade 12, the study of 'social identity and diversity' builds on Grade 11 by examining these concepts with:", "options": [
            "Greater analytical depth, including their relationship to policy and governance", "No connection whatsoever to Grade 11 content",
            "Exclusively unrelated content with no reference to identity or diversity", "Less depth than covered in Grade 11"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Intersectionality', an advanced concept relevant to social identity, refers to how:", "options": [
            "Multiple aspects of a person's identity (e.g. gender, ethnicity, class) can combine to shape their experiences", "A person's identity consists of only a single, isolated characteristic",
            "A concept unrelated to how social identities interact", "Every individual experiences identity in an identical, uniform way"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Nepal's federal constitution addresses ethnic and social diversity partly through provisions for:", "options": [
            "Inclusive representation and proportional participation of diverse groups in governance", "The complete exclusion of diverse groups from any governmental role",
            "A single uniform identity imposed on the entire population", "No reference to diversity within the constitution at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social cohesion' refers to the degree to which members of a society:", "options": [
            "Feel connected, cooperate, and trust one another despite differences", "Are completely isolated from one another with no cooperation",
            "A concept unrelated to social relationships", "Actively work against each other with no shared trust"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Identity-based conflict' can arise when different social groups experience:", "options": [
            "Unequal access to power, resources, or recognition based on their identity", "Perfectly equal treatment with no disparity of any kind",
            "A concept entirely unrelated to social group dynamics", "Complete isolation with no interaction between groups"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Positive discrimination' or affirmative action policies aim to address disadvantage historically faced by:", "options": [
            "Marginalised social groups, by improving their access to opportunities", "Already-privileged groups exclusively",
            "No specific group in particular", "A concept unrelated to addressing social inequality"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Inclusive governance' aims to ensure that decision-making processes:", "options": [
            "Represent and consider the perspectives of diverse social groups", "Exclude the perspectives of all but a single dominant group",
            "A concept unrelated to how governments make decisions", "Apply only to a single, homogeneous population"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cultural preservation' efforts aim to protect elements such as:", "options": [
            "Languages, traditions, and customs of diverse communities", "The complete elimination of any minority culture",
            "A concept unrelated to community heritage", "Only the culture of a single dominant group"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Social exclusion', a challenge related to diversity, refers to:", "options": [
            "The process by which certain individuals or groups are systematically denied full participation in society", "A process that guarantees full participation for every individual regardless of background",
            "A concept unrelated to access or participation in society", "A process that applies only to already-privileged groups"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Diversity management' in institutions (e.g. workplaces, schools) involves policies that:", "options": [
            "Promote fair treatment and inclusion of individuals from different backgrounds", "Actively discriminate against individuals from certain backgrounds",
            "A concept unrelated to institutional policy", "Apply identical treatment while ignoring any relevant need or context"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's proportional representation electoral provisions aim to ensure:", "options": [
            "Fairer representation of historically underrepresented groups in elected bodies", "The complete exclusion of underrepresented groups from elected bodies",
            "Representation determined entirely by a single dominant group", "A concept unrelated to Nepal's electoral system"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Identity politics' refers to political approaches or movements organised around the interests of:", "options": [
            "Specific social identity groups, such as ethnic, gender, or religious communities", "No specific group interest whatsoever",
            "Only a single dominant group, with no reference to others", "A concept entirely unrelated to political organisation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social capital', relevant to diverse communities, refers to:", "options": [
            "The networks, trust, and relationships that enable cooperation within and between communities", "A purely financial asset with no social dimension",
            "A concept unrelated to community relationships", "Only the physical infrastructure present within a community"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'intersectionality' is a useful concept for understanding social inequality?", "options": [
            "It recognises that combined aspects of identity (e.g. gender and ethnicity together) can shape a person's experience of disadvantage differently than either alone", "It assumes every individual's identity consists of only a single, isolated trait",
            "It has no relevance to understanding patterns of social inequality", "It applies only to countries with no ethnic or gender diversity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the purpose of proportional representation provisions in Nepal's electoral system?", "options": [
            "To help ensure historically underrepresented and marginalised groups have a fairer voice in elected government bodies", "To exclude marginalised groups entirely from any representation",
            "To guarantee representation only for a single dominant political party", "This provision has no connection to social inclusion goals"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a policy addressing 'social exclusion' in practice?", "options": [
            "A scholarship program specifically supporting students from historically marginalised communities to access higher education", "A policy that restricts higher education access exclusively to already-privileged groups",
            "A policy with no connection to educational access or marginalisation", "A policy that has no measurable effect on social participation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'social cohesion' is considered important in a highly diverse country like Nepal?", "options": [
            "Strong social cohesion helps diverse groups cooperate and coexist peacefully despite differing identities and interests", "Social cohesion has no relevance to a country's stability or cooperation",
            "Diversity automatically guarantees social cohesion with no further effort required", "Social cohesion is relevant only to countries with no ethnic or cultural diversity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises how this Grade 12 unit extends the Grade 11 treatment of social identity and diversity?", "options": [
            "It applies these concepts with greater analytical depth to governance, policy, and real-world social outcomes", "It repeats Grade 11 content with no additional depth or application",
            "It removes any connection to governance or policy", "It focuses exclusively on unrelated content with no connection to identity or diversity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Social Identity and Diversity'?", "options": [
            "Understanding how identity and diversity shape social relationships, governance, and policy in a country like Nepal", "A focus exclusively on unrelated economic statistics",
            "A topic with no relevance to Nepal's constitution or governance", "A purely theoretical topic with no real-world application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A local government reserving a share of elected seats for women and marginalised groups is an example of applying which concept from this unit?", "options": [
            "Inclusive governance and positive/affirmative representation", "A policy that deliberately excludes marginalised groups from representation",
            "A concept unrelated to governance or representation", "A practice discouraged under Nepal's constitution"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34702: [  # Unit 8: Constitution and Civic Consciousness
        {"q": "'Civic consciousness' refers to a citizen's:", "options": [
            "Awareness of, and active engagement with, their rights, duties, and role in society", "Complete unawareness of their rights or societal role",
            "Awareness limited exclusively to their personal finances", "A concept unrelated to civic participation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "At Grade 12, the study of the constitution extends beyond basic structure to examine:", "options": [
            "How constitutional principles are applied and function in practice", "No further depth beyond what was studied in Grade 11",
            "A completely unrelated legal system from another country", "Only the physical printing and formatting of the constitution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Judicial review', a constitutional mechanism, allows courts to:", "options": [
            "Examine whether laws or government actions are consistent with the constitution", "Draft new laws directly, bypassing parliament entirely",
            "Set the national budget without any parliamentary involvement", "A mechanism unrelated to constitutional governance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Constitutional supremacy' means that:", "options": [
            "The constitution is the highest law, and other laws must be consistent with it", "The constitution has no binding legal authority",
            "Ordinary laws always override the constitution", "A concept unrelated to a country's legal hierarchy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Accountability' in governance refers to the principle that public officials should be:", "options": [
            "Answerable for their actions and decisions to the public and relevant institutions", "Entirely exempt from any scrutiny of their actions",
            "Accountable only to themselves, with no external oversight", "A concept unrelated to democratic governance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Transparency in governance' refers to the principle of:", "options": [
            "Making government processes and decisions open and accessible to public scrutiny", "Deliberately concealing all government decisions from the public",
            "A concept unrelated to democratic accountability", "Applying only to private businesses, not government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's constitutional bodies, such as the Election Commission, function to:", "options": [
            "Perform specific independent oversight roles, such as conducting fair elections", "Have no defined role within Nepal's governance system",
            "Report directly and exclusively to a single political party", "Replace the need for any elected government"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Constitutional amendment', the formal process for changing a constitution, typically requires:", "options": [
            "A defined special procedure, often more demanding than passing ordinary legislation", "No formal process whatsoever",
            "Amendment by a single individual with no institutional involvement", "A process entirely identical to enacting an ordinary law"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Active citizenship' can manifest through actions such as:", "options": [
            "Voting, participating in public consultations, and engaging in community initiatives", "Complete disengagement from any public or community matter",
            "A concept unrelated to a citizen's daily life", "Actions limited exclusively to elected officials"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human rights protections' embedded in Nepal's constitution aim to:", "options": [
            "Safeguard the fundamental freedoms and dignity of individuals", "Deliberately restrict the freedoms of all citizens with no protection",
            "Apply exclusively to government officials, not ordinary citizens", "A concept unrelated to constitutional governance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Checks and balances' among branches of government aim to:", "options": [
            "Prevent any single branch from exercising unchecked power", "Concentrate all governmental power within a single branch",
            "A concept unrelated to preventing abuse of power", "Eliminate the need for multiple branches of government"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Devolution of power' under Nepal's federal structure refers to:", "options": [
            "The transfer of certain governmental authorities from the federal level to provincial and local levels", "The complete concentration of all authority at the federal level with no transfer",
            "A concept unrelated to Nepal's governance structure", "The elimination of provincial and local government entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Constitutional literacy', an aspect of civic consciousness, refers to a citizen's understanding of:", "options": [
            "The basic structure, principles, and provisions of their country's constitution", "A concept unrelated to a citizen's understanding of governance",
            "Only a country's economic statistics, not its legal structure", "A concept relevant only to legal professionals, never ordinary citizens"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Public participation in local government decision-making, such as ward-level consultations, exemplifies:", "options": [
            "Active civic consciousness and grassroots democratic engagement", "Complete civic disengagement from local governance",
            "A concept unrelated to Nepal's local governance structure", "A practice discouraged under Nepal's constitution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'judicial review' is considered an important safeguard within a constitutional democracy?", "options": [
            "It allows courts to check whether laws and government actions comply with the constitution, helping prevent government overreach", "It has no relevance to maintaining constitutional governance",
            "It allows courts to bypass parliament entirely in the ordinary law-making process", "It applies only to countries without a written constitution"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the relationship between 'civic consciousness' and effective democratic governance?", "options": [
            "Informed and engaged citizens are better able to hold government accountable and participate meaningfully in decision-making", "Civic consciousness has no bearing on how effectively a democracy functions",
            "Democratic governance functions equally well regardless of citizen awareness or engagement", "Civic consciousness is relevant only to elected officials, not ordinary citizens"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates 'transparency in governance' in practice?", "options": [
            "A local government publicly publishing its annual budget and expenditure reports", "A government deliberately withholding all information about its budget from the public",
            "A concept with no practical real-world application", "A practice that applies only to private companies, not government bodies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'devolution of power' to provincial and local governments is intended to strengthen civic consciousness and participation?", "options": [
            "Decisions made closer to citizens' daily lives can make government more responsive and accessible, encouraging greater civic engagement", "Devolution of power has no effect on citizens' engagement with governance",
            "Devolved power always reduces citizen engagement with government", "This concept applies only to unitary states, not federal ones like Nepal"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises how this Grade 12 unit builds on the Grade 11 study of the constitution?", "options": [
            "It extends the earlier foundational understanding to examine how constitutional principles operate in practice and shape active citizenship", "It discards all Grade 11 content with no continuity",
            "It focuses exclusively on unrelated legal systems from other countries", "It provides no additional depth beyond the Grade 11 treatment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Constitution and Civic Consciousness'?", "options": [
            "Understanding how constitutional principles function in practice and how informed citizens can engage meaningfully with governance", "A focus exclusively on unrelated historical trivia",
            "A topic with no connection to real governance or citizenship", "A purely theoretical topic with no practical relevance"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34740: [  # Unit 9: Urbanization and Migration
        {"q": "'Urbanization' refers to the process by which an increasing share of a population:", "options": [
            "Comes to live in urban (city/town) areas rather than rural areas", "Moves exclusively toward rural areas with no urban growth",
            "Remains permanently in a single fixed location with no movement", "A concept unrelated to where people live"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Kathmandu Valley has experienced significant urbanization largely driven by:", "options": [
            "Concentration of economic opportunity, education, and administrative functions", "A complete absence of any economic or administrative activity",
            "A deliberate government policy to discourage all urban growth", "A concept unrelated to migration or economic opportunity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Rural-to-urban migration' is often driven by 'push factors' such as:", "options": [
            "Limited rural employment opportunities and lower access to services", "An abundance of rural employment with no reason to migrate",
            "A concept unrelated to why people move to cities", "Superior services and infrastructure exclusively in rural areas"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Pull factors' that attract migrants to urban areas include:", "options": [
            "Better employment opportunities, education, and healthcare access", "A complete absence of any opportunity in urban areas",
            "A concept unrelated to urban migration", "Only unfavourable conditions found exclusively in cities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'International labour migration' from Nepal, distinct from internal rural-urban migration, involves:", "options": [
            "Nepali citizens moving abroad, often to Gulf countries or Malaysia, for employment", "Migration that occurs exclusively within Nepal's own borders",
            "A concept unrelated to Nepal's labour market", "Migration limited only to short-distance travel"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Urban sprawl', a challenge associated with rapid urbanization, refers to:", "options": [
            "Often unplanned, outward expansion of a city's built-up area", "A carefully controlled and fully planned contraction of a city",
            "A term unrelated to city growth patterns", "A decline in a city's population with no expansion"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Rapid, unplanned urbanization can strain city infrastructure such as:", "options": [
            "Housing, water supply, waste management, and transportation systems", "A country's foreign embassies exclusively",
            "A factor entirely unrelated to city planning", "Only a city's tourism marketing budget"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Informal settlements', sometimes arising in rapidly urbanizing areas, are characterised by:", "options": [
            "Housing developed outside formal planning and legal land-tenure systems, often lacking full access to services", "Fully planned, government-approved housing with complete service access",
            "A concept unrelated to urban growth challenges", "Housing found exclusively in rural, non-urban settings"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Remittances' sent home by internationally migrated workers contribute to Nepal's economy by:", "options": [
            "Supporting household consumption, investment, and national foreign exchange reserves", "Having no measurable economic effect whatsoever",
            "Draining Nepal's foreign exchange reserves entirely", "A concept unrelated to Nepal's balance of payments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Urban planning' aims to manage city growth by addressing issues such as:", "options": [
            "Zoning, infrastructure development, and sustainable resource management", "A complete absence of any organised approach to city development",
            "A concept unrelated to managing urban growth", "Ignoring infrastructure needs entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Circular migration' refers to a pattern in which migrants:", "options": [
            "Move back and forth between their place of origin and destination, rather than relocating permanently", "Never return to their place of origin under any circumstance",
            "Remain permanently and exclusively in a single location with no movement", "A concept unrelated to migration patterns"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Brain drain', a concern related to international migration, refers to:", "options": [
            "The emigration of highly skilled individuals, potentially reducing a country's skilled workforce", "An increase in a country's skilled workforce due to migration",
            "A concept unrelated to labour migration", "A phenomenon limited exclusively to unskilled workers"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Social impact of migration' on families left behind can include:", "options": [
            "Changes in household structure and responsibilities, alongside potential economic benefits from remittances", "No social impact of any kind on the family",
            "A concept unrelated to labour migration", "Guaranteed improvement in every aspect of family life with no challenge"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Balanced regional development is often proposed as a strategy to reduce excessive urban migration by:", "options": [
            "Creating economic opportunities in currently underdeveloped regions, reducing the pressure to migrate to major cities", "Concentrating all development exclusively in a single major city",
            "A concept unrelated to managing internal migration patterns", "Actively discouraging any development outside the capital"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why Kathmandu Valley has experienced disproportionately high urbanization compared to many other parts of Nepal?", "options": [
            "It concentrates economic, educational, and administrative opportunities, drawing migrants from across the country", "Kathmandu Valley has experienced no urbanization at all",
            "Urbanization in Nepal is evenly distributed across all regions with no concentration", "Kathmandu Valley has actively discouraged any migration into the area"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the connection between 'push factors' and 'pull factors' in understanding migration decisions?", "options": [
            "Push factors (like limited rural opportunity) and pull factors (like urban opportunity) together explain why individuals choose to migrate", "Only push factors ever influence a migration decision, with pull factors playing no role",
            "Push and pull factors are unrelated concepts with no connection to migration", "Migration decisions occur entirely independently of any economic or social factor"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a policy response aimed at managing the challenges of rapid urbanization?", "options": [
            "A city government implementing zoning regulations and expanding water/sanitation infrastructure to keep pace with growth", "A city government ignoring infrastructure needs entirely despite rapid population growth",
            "A policy that actively worsens housing and service shortages with no planning", "A concept with no practical application to real cities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'brain drain' is considered a potential concern for Nepal's long-term development?", "options": [
            "The emigration of highly skilled workers can reduce the domestic pool of expertise needed to support various sectors' development", "Brain drain always benefits Nepal's domestic sectors with no downside",
            "Brain drain has no connection to Nepal's skilled workforce or development", "This concept applies only to unskilled labour migration"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Urbanization and Migration'?", "options": [
            "Understanding the causes, patterns, and social/economic consequences of both internal urban migration and international labour migration", "A focus exclusively on unrelated foreign case studies with no reference to Nepal",
            "A topic with no relevance to Nepal's current social and economic development", "A purely historical topic with no connection to present-day migration patterns"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A local government building affordable housing and expanding public transit in response to rapid population inflow is an example of:", "options": [
            "A planned policy response to challenges created by urbanization", "A policy that actively discourages any urban infrastructure development",
            "A concept unrelated to managing urban growth", "A response applicable only to rural, non-urban settings"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34744: [  # Unit 10: Economy and Development
        {"q": "At Grade 12, the study of Nepal's economy and development builds on earlier content by examining:", "options": [
            "More advanced analysis of economic structure, policy, and development strategy", "No additional depth compared to earlier grades",
            "A completely unrelated country's economy with no reference to Nepal", "Only the physical geography of Nepal with no economic content"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Nepal's 'Fifteenth Plan' and successive periodic development plans are coordinated by the:", "options": [
            "National Planning Commission", "World Trade Organization", "A private multinational corporation",
            "The United Nations Security Council"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Structural transformation' of an economy typically refers to a shift in the relative importance of:", "options": [
            "Agriculture, industry, and services sectors as an economy develops", "A single, permanently fixed economic sector with no change over time",
            "A concept unrelated to how economies evolve", "Only a country's foreign exchange rate"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Nepal's economy is often described as still being in transition from a predominantly:", "options": [
            "Agriculture-based economy toward greater industrial/service-sector activity", "Fully industrialised economy back toward a purely agricultural one",
            "A concept unrelated to Nepal's economic structure", "An economy with no agricultural sector at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Public-Private Partnership (PPP)' models are increasingly used in Nepal's development strategy to:", "options": [
            "Combine government and private-sector resources/expertise for infrastructure and development projects", "Completely exclude the private sector from any development project",
            "A concept unrelated to Nepal's development financing", "Replace the need for any government involvement in infrastructure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Foreign aid and development assistance' have historically contributed to Nepal's development by:", "options": [
            "Supplementing domestic resources for infrastructure and social programs", "Completely replacing the need for any domestic revenue or planning",
            "A concept unrelated to Nepal's development financing", "Being legally prohibited under Nepal's constitution"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Graduation from Least Developed Country (LDC) status', a goal for Nepal, reflects improvements in indicators such as:", "options": [
            "Income, human assets, and economic vulnerability", "A country's total land area alone",
            "A purely symbolic label with no basis in measurable indicators", "A concept unrelated to Nepal's development planning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Economic diversification', often recommended for Nepal, involves:", "options": [
            "Reducing reliance on a narrow set of economic activities (like remittances) by developing multiple sectors", "Increasing dependence on a single economic sector",
            "A concept unrelated to reducing economic vulnerability", "Eliminating the need for any economic planning"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Sustainable Development Goals (SDGs)' commitments shape Nepal's development planning by setting targets related to:", "options": [
            "Poverty reduction, education, health, and environmentally sustainable growth", "Exclusively military expenditure with no other target",
            "No development-related target of any kind", "Targets relevant only to already-developed nations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Fiscal federalism', relevant to Nepal's post-2015 governance structure, concerns how:", "options": [
            "Revenue and expenditure responsibilities are distributed across federal, provincial, and local governments", "All fiscal authority remains concentrated exclusively at the federal level",
            "A concept unrelated to Nepal's federal restructuring", "Provincial and local governments are given no fiscal authority whatsoever"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Inclusive growth', a development policy goal, emphasises that economic growth should:", "options": [
            "Benefit a broad cross-section of society, not just a small privileged group", "Benefit only a small, already-wealthy segment of the population",
            "A concept unrelated to how growth is distributed", "Occur with no consideration of who benefits from it"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human capital investment', such as in education and health, supports long-term development mainly by:", "options": [
            "Building a more skilled, healthy, and productive population", "Having no bearing on a country's long-term productivity",
            "A concept unrelated to development strategy", "Reducing a population's overall productivity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Balanced regional development' remains a policy priority for Nepal mainly to:", "options": [
            "Reduce disparities in development between Kathmandu Valley and other regions of the country", "Concentrate all development exclusively within Kathmandu Valley",
            "A concept unrelated to regional development planning", "Ignore any disparity between regions entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Private sector development' is important to Nepal's economic growth strategy because private enterprises:", "options": [
            "Contribute significantly to employment generation and economic output", "Have no role in generating employment or economic output",
            "A concept unrelated to Nepal's economic development", "Are legally prohibited from operating in Nepal"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'economic diversification' is often recommended for Nepal given its historical reliance on remittances?", "options": [
            "Heavy reliance on a single income source like remittances leaves the economy vulnerable to external shocks affecting that source", "Diversification would make Nepal's economy more vulnerable, not less",
            "Nepal's economy faces no vulnerability regardless of its reliance on any single sector", "Diversification has no relevance to reducing economic risk"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the purpose of 'fiscal federalism' in Nepal's post-2015 governance structure?", "options": [
            "It distributes revenue and spending authority across government levels, aiming to support more locally responsive development", "It concentrates all fiscal authority exclusively at the federal level with no distribution",
            "It has no connection to how development resources are allocated across Nepal", "It eliminates the need for any government revenue collection"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'inclusive growth' is emphasised as a policy goal rather than economic growth alone?", "options": [
            "Growth that benefits only a small segment of society can worsen inequality even while GDP rises", "Inclusive growth and economic growth are always identical, with no distinction",
            "GDP growth automatically ensures benefits are shared broadly across society with no further effort needed", "Inclusive growth has no relevance to development policy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a 'Public-Private Partnership' approach to development in Nepal?", "options": [
            "A hydropower project jointly financed and operated by a government agency and a private company", "A project financed and operated exclusively by the government with no private involvement",
            "A project that excludes any form of government involvement whatsoever", "A concept unrelated to infrastructure development"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises how this Grade 12 unit extends the Grade 11 treatment of 'Economy and Development'?", "options": [
            "It applies more advanced analysis to Nepal's economic structure, federal fiscal arrangements, and development strategy", "It repeats Grade 11 content with no additional depth",
            "It focuses exclusively on an unrelated foreign economy", "It removes any connection to development policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall focus of this unit on 'Economy and Development'?", "options": [
            "Understanding Nepal's evolving economic structure and the strategies used to pursue inclusive, sustainable development", "A focus exclusively on unrelated foreign economic history",
            "A topic with no relevance to Nepal's current development policy", "A purely theoretical topic with no practical application"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34742: [  # Unit 11: Education and Social Development
        {"q": "Education is widely regarded as a driver of social development mainly because it:", "options": [
            "Builds knowledge, skills, and human capital that support broader societal progress", "Has no measurable relationship to a society's development",
            "A concept unrelated to social or economic outcomes", "Actively reduces a society's overall productivity"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Universal access to education', a policy goal in Nepal, aims to ensure that:", "options": [
            "All children, regardless of background, have the opportunity to receive an education", "Education is restricted exclusively to a small privileged group",
            "A concept unrelated to Nepal's education policy", "Access to education is granted only to a single specific region"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Literacy rate', an important education-related indicator, measures:", "options": [
            "The proportion of a population able to read and write", "A country's total population size with no reference to literacy",
            "Only the number of schools in a country", "A measure unrelated to education outcomes"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Gender parity in education' refers to ensuring that:", "options": [
            "Both boys and girls have equal access to and participation in education", "Only boys are granted access to formal education",
            "A concept unrelated to educational access", "Only girls are granted access to formal education"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Quality of education', beyond simple access, concerns factors such as:", "options": [
            "Curriculum relevance, teacher competency, and learning outcomes", "Only the physical size of a school building",
            "A concept unrelated to actual learning outcomes", "Only the number of students enrolled, regardless of what they learn"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Technical and vocational education and training (TVET)' aims to:", "options": [
            "Equip students with practical, employable skills for specific trades or occupations", "Focus exclusively on theoretical academic knowledge with no practical skill",
            "A concept unrelated to preparing students for employment", "Replace the need for any general academic education"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Higher education', including universities, contributes to social development by:", "options": [
            "Producing skilled professionals and advancing research and knowledge", "Having no connection to a country's skilled workforce",
            "A concept unrelated to national development", "Focusing exclusively on unrelated recreational activities"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Education for marginalised communities' is emphasised in Nepal's policy partly to:", "options": [
            "Address historical disparities in access to schooling faced by disadvantaged groups", "Further restrict access to education for disadvantaged groups",
            "A concept unrelated to educational equity", "Apply exclusively to already well-resourced communities"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'School dropout', a challenge in Nepal's education system, can be influenced by factors such as:", "options": [
            "Poverty, distance to school, and social/cultural barriers", "A complete absence of any barrier to continuing education",
            "A concept unrelated to why students leave school early", "Only a student's personal preference, with no external factor involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Education and economic development' are closely linked because a more educated workforce tends to be:", "options": [
            "More productive and better able to contribute to economic growth", "Less productive than an entirely uneducated workforce",
            "A concept unrelated to economic productivity", "Relevant only to non-economic aspects of society"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital access in education', an increasingly important issue, concerns whether students have:", "options": [
            "Access to computers, the internet, and digital learning resources", "No relevance to modern education systems",
            "Access limited exclusively to printed textbooks with no digital resource", "A concept unrelated to educational equity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Community participation in education', such as through school management committees, aims to:", "options": [
            "Strengthen local accountability and engagement in the functioning of schools", "Exclude the local community entirely from any involvement in schools",
            "A concept unrelated to how schools are managed", "Replace the need for any professional teaching staff"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Skill mismatch', a labour market challenge, refers to a situation where:", "options": [
            "The skills produced by the education system do not align well with the skills demanded by employers", "Education perfectly and automatically matches every job requirement with no mismatch",
            "A concept unrelated to education or the labour market", "Employers require no specific skills of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Investment in early childhood education is often highlighted as particularly valuable because it:", "options": [
            "Lays a foundational basis for a child's later cognitive and social development", "Has no measurable effect on a child's later development",
            "A concept unrelated to long-term educational outcomes", "Is relevant only to a child's physical growth, not cognitive development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'quality of education', not just access, is emphasised as a policy concern in Nepal?", "options": [
            "Enrolling students in school does not guarantee meaningful learning if curriculum, teaching, and resources are inadequate", "Access alone always guarantees high-quality learning outcomes with no further consideration needed",
            "Quality of education has no bearing on a student's actual learning outcomes", "Quality is relevant only to higher education, not schooling"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the connection between 'technical and vocational education' and Nepal's broader development goals?", "options": [
            "TVET can equip a segment of the workforce with practical skills that support employment and reduce skill mismatches in the labour market", "TVET has no relevance to Nepal's labour market or development goals",
            "TVET exists entirely separately from any broader development strategy", "TVET is relevant only to countries with no general academic education system"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a policy response to address school dropout linked to poverty?", "options": [
            "A scholarship or stipend program that reduces the financial burden of schooling for low-income families", "A policy that increases school fees for all students regardless of income",
            "A policy with no connection to reducing financial barriers to education", "A policy that discourages any low-income student from attending school"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'gender parity in education' remains an important policy focus in some parts of Nepal?", "options": [
            "Social and cultural factors have historically limited girls' access to schooling in certain communities, requiring targeted policy attention", "Gender has never had any bearing on educational access in Nepal's history",
            "Gender parity is relevant only to countries other than Nepal", "This concept has no connection to Nepal's education policy goals"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall relationship examined in this unit between education and social development?", "options": [
            "Education builds human capital and opportunity, serving as a key driver of broader social and economic development", "Education and social development are entirely unrelated fields",
            "Social development occurs independently of a population's educational access or quality", "Education is relevant only to an individual's private life, with no broader social effect"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of concluding the Grade 12 Social Studies syllabus with a unit on 'Education and Social Development'?", "options": [
            "It ties together the course's themes by showing how education, as both an outcome and driver of development, connects individual opportunity to societal progress", "It is an arbitrary, unrelated final topic with no connection to the rest of the course",
            "It has no thematic connection to earlier units on economy, governance, or society", "It focuses exclusively on unrelated content with no relevance to social development"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
