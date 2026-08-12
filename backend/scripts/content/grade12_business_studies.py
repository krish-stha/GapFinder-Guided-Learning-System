# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Business Studies (Principles of Management)
question bank.

Authored content (not content partner data - loaded with source='synthetic'
by scripts/load_question_bank.py). Topically accurate, written to read
like genuine exam questions per explicit user instruction. Chapter names
match, exactly, the Section rows already sitting under course 210 ("NEB
Grade 12 Management") Business Studies subject (subject_id=34300) - see
scripts/reports/phase1_verify.json for the source list. Note this Grade
12 "Business Studies" subject is curricularly a Principles of Management
course (Nature of Management, POLC framework, etc.) - genuinely distinct
from Grade 11's business-forms-focused Business Studies subject, not a
duplicate of it. Never presented as content partner content or as evidence
about real students.

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}.
"""

QUESTIONS = {
    "Nature of Management": [
        {"q": "'Management' is best defined as:", "options": [
            "The process of planning, organising, leading and controlling resources to achieve organisational goals efficiently and effectively",
            "Only the act of supervising factory workers", "Only the process of hiring employees", "Only the act of recording financial transactions"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Management is considered both an art and a science because it:", "options": [
            "Involves systematic, tested principles (science) as well as creative, situational judgement in application (art)",
            "Is purely a natural talent with no learnable principles at all", "Involves no decision-making of any kind",
            "Applies identically to every situation with no need for judgement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Efficiency' in management refers to:", "options": [
            "Doing things right - using resources with minimum waste", "Doing the right things regardless of resource use",
            "Ignoring resource costs entirely", "Achieving goals with unlimited resources"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Effectiveness' in management refers to:", "options": [
            "Doing the right things - achieving the intended organisational goals", "Using the fewest possible resources regardless of outcome",
            "Working the longest hours possible", "Avoiding all forms of goal-setting"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a widely recognised function of management?", "options": [
            "Planning, Organising, Leading and Controlling", "Only manufacturing products",
            "Only advertising products", "Only collecting government taxes"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Management is considered a distinct 'process' mainly because it involves:", "options": [
            "A continuous series of interrelated functions performed to achieve goals", "A single one-time act with no repetition",
            "Only physical labour with no mental activity", "An activity performed only once when a business starts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Management is described as a 'universal' activity because it:", "options": [
            "Is applicable to all types of organisations - business, government, non-profit, etc.", "Applies only to large multinational corporations",
            "Applies only to government offices", "Applies only to sole proprietorships"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a key reason management is important to any organisation?", "options": [
            "It coordinates resources and efforts to achieve goals effectively", "It has no measurable impact on organisational performance",
            "It exists only to increase paperwork", "It eliminates the need for any goal-setting"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Managers at different organisational levels (top, middle, first-line) typically differ mainly in their:", "options": [
            "Emphasis on strategic versus operational responsibilities", "Access to a company car",
            "Personal salary alone, with identical responsibilities", "Working hours only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Top-level management' is primarily responsible for:", "options": [
            "Setting overall organisational goals and strategic direction", "Directly supervising day-to-day shop floor operations",
            "Only performing clerical tasks", "Only responding to customer complaints"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'First-line (supervisory) management' is primarily responsible for:", "options": [
            "Directly overseeing the work of operational/non-managerial employees", "Setting the organisation's long-term strategic vision",
            "Negotiating with the government on national policy", "Deciding shareholder dividend policy"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes a manager's 'conceptual skill'?", "options": [
            "The ability to see the organisation as a whole and understand how its parts relate", "The ability to operate a single specific machine",
            "The ability to type quickly", "The ability to drive a company vehicle"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Technical skill' in management refers to:", "options": [
            "Proficiency in a specific specialised activity or field of work", "The ability to motivate an entire organisation",
            "The ability to set national economic policy", "A skill relevant only to top management"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Human (interpersonal) skill' in management refers to:", "options": [
            "The ability to work effectively with and through other people", "The ability to operate machinery only",
            "The ability to perform accounting calculations only", "A skill irrelevant to team-based work"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to common management theory, which skill becomes relatively MORE important as a manager rises to top-level positions?", "options": [
            "Conceptual skill", "Technical skill only", "Only physical strength", "Only clerical/typing skill"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why management is considered necessary in EVERY organised group effort?", "options": [
            "Without coordination and direction, individual efforts may not align with the group's overall goal", "Groups always naturally coordinate themselves with no guidance needed",
            "Organised effort never requires any planning", "Management is only relevant to for-profit businesses"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'manager' differs from a non-managerial employee mainly in that a manager:", "options": [
            "Is responsible for directing and coordinating the work of others toward organisational goals", "Never performs any task personally",
            "Has no accountability of any kind", "Works exclusively alone with no team"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following best reflects management's role as a 'coordinating' force?", "options": [
            "Integrating the efforts of different individuals and departments toward common goals", "Keeping every department working in complete isolation with no communication",
            "Eliminating the need for teamwork entirely", "Preventing any interaction between departments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the statement 'management is goal-oriented'?", "options": [
            "All managerial activities are ultimately directed toward achieving specific organisational objectives", "Managers work without any defined objective",
            "Goals are irrelevant to the management process", "Management activities have no defined purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of a 'non-profit' organisation that still requires management?", "options": [
            "A charitable NGO providing community services", "A privately owned retail shop seeking profit",
            "A publicly traded manufacturing company", "A government-owned commercial enterprise selling goods for profit"],
         "correct": 0, "difficulty": "Easy"},
    ],
    "Classical  Management Perspectives": [  # NOTE: real chapter name has a double space between "Classical" and "Management" - exact match required
        {"q": "The 'Classical Management' perspective broadly emphasises:", "options": [
            "Formal structure, efficiency, and systematic principles of organisation and work", "Employee emotions and informal social relationships as the primary focus",
            "Ignoring structure entirely in favour of complete employee autonomy", "Only modern digital technology in management"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Frederick W. Taylor is most closely associated with the theory of:", "options": [
            "Scientific Management", "Human Relations", "Systems Theory", "Contingency Theory"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Taylor's Scientific Management emphasised finding the:", "options": [
            "'One best way' to perform a task through scientific study and standardisation", "Best way based purely on worker intuition with no study",
            "Best way based solely on employee seniority", "Best way based only on random trial and error with no measurement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a core principle of Taylor's Scientific Management?", "options": [
            "Scientific selection and training of workers for their specific roles", "Complete elimination of any worker training",
            "Paying all workers an identical wage regardless of output", "Avoiding any standardisation of work methods"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Henri Fayol is most closely associated with:", "options": [
            "General/Administrative Management theory and 14 Principles of Management", "Scientific Management and time-motion studies",
            "The Hawthorne Studies on human relations", "Modern digital transformation theory"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Fayol identified management functions that broadly evolved into what is now commonly summarised as:", "options": [
            "Planning, Organising, Leading (Commanding/Coordinating) and Controlling", "Only manufacturing and selling",
            "Only accounting and taxation", "Only hiring and firing employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Fayol's principle of 'Unity of Command' states that:", "options": [
            "An employee should receive orders/instructions from only one superior", "An employee should report to as many superiors as possible",
            "No employee should ever receive any instruction", "Only top management should ever give orders"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Fayol's principle of 'Division of Work' suggests that:", "options": [
            "Specialisation of tasks increases efficiency and expertise", "All employees should perform identical, unspecialised tasks",
            "Work should never be divided among employees", "Only managers should ever perform any work"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Fayol's principle of 'Scalar Chain' refers to:", "options": [
            "The formal line of authority/communication running from top to bottom of the organisation", "A method for calculating employee wages",
            "A financial ratio used in accounting", "A marketing pricing strategy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Max Weber is most closely associated with the theory of:", "options": [
            "Bureaucracy", "Scientific Management", "Human Relations", "Contingency Management"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Weber's Bureaucratic theory emphasises organisational structure characterised by:", "options": [
            "Clear hierarchy, formal rules, division of labour, and impersonal relationships", "Complete absence of any rules or hierarchy",
            "Decisions made purely on personal favouritism", "No division of labour whatsoever"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key criticism of classical management theories is that they:", "options": [
            "Tend to underemphasise the human/social and psychological needs of workers", "Focus excessively on employee emotions and ignore structure entirely",
            "Have never influenced any modern management practice", "Apply only to non-profit organisations"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Time and motion studies, associated with Scientific Management, were used to:", "options": [
            "Analyse and improve the efficiency of specific work tasks", "Measure employee personal satisfaction only",
            "Calculate a company's total tax liability", "Design a company's advertising campaign"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Fayol's principle of 'Equity' in management suggests that managers should treat employees with:", "options": [
            "Kindness, fairness and justice", "Strict favouritism toward senior staff only", "Complete indifference to fairness",
            "Harshness at all times"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best distinguishes Fayol's approach from Taylor's?", "options": [
            "Fayol focused on overall administrative/managerial principles for the whole organisation, while Taylor focused on shop-floor task efficiency",
            "Fayol and Taylor developed identical theories with no distinction", "Taylor focused only on top-level administration",
            "Fayol focused only on individual worker task timing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Under Weber's bureaucratic model, employee selection and promotion are ideally based on:", "options": [
            "Technical competence and qualifications", "Personal friendship with the manager",
            "Family relationship to the owner", "Random selection with no criteria"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a strength commonly attributed to classical management theories?", "options": [
            "They provided systematic, foundational principles that improved organisational efficiency", "They completely eliminated the need for any management structure",
            "They focused exclusively on employee happiness with no attention to productivity", "They rejected the idea of any formal organisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Fayol's principle of 'Remuneration' states that employee compensation should be:", "options": [
            "Fair and satisfactory to both employees and the organisation", "As low as legally possible regardless of fairness",
            "Determined solely by random chance", "Identical for every employee regardless of role or effort"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'piece-rate' wage system, associated with Scientific Management, pays workers based on:", "options": [
            "The quantity of output produced", "A fixed salary regardless of output", "Seniority alone", "Random assignment with no clear rule"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the enduring relevance of classical management principles today?", "options": [
            "Many organisations still rely on structured hierarchies, defined roles, and efficiency-focused processes rooted in these ideas",
            "Classical principles have been completely abandoned in all modern organisations", "They are relevant only to non-business organisations",
            "They have no connection to how modern companies are structured"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Planning and Decision Making": [
        {"q": "'Planning', as a management function, refers to:", "options": [
            "Setting objectives and determining the best course of action to achieve them", "Only recording past financial transactions",
            "Only supervising employees on the shop floor", "An activity performed only after all work is completed"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Planning is generally considered the FIRST function of management because:", "options": [
            "It provides the direction and basis on which other management functions (organising, leading, controlling) are carried out",
            "It is legally required to be performed last", "It has no connection to other management functions",
            "It is the least important management function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Mission Statement' of an organisation broadly describes:", "options": [
            "The organisation's fundamental purpose and reason for existence", "A single day's task list for employees",
            "The organisation's annual tax return", "A specific employee's job description only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Strategic planning' typically covers:", "options": [
            "Long-term, organisation-wide goals and direction, usually set by top management", "Only a single day's routine task scheduling",
            "Only clerical filing procedures", "Only the choice of office furniture"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Operational planning' typically covers:", "options": [
            "Short-term, detailed plans for specific day-to-day activities", "Only the organisation's 20-year vision",
            "Only shareholder dividend policy", "The organisation's fundamental mission statement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'policy' in management is best described as:", "options": [
            "A general guideline that channels thinking and decision-making within an organisation", "A single, one-time, specific decision",
            "A financial statement", "An employee's personal opinion with no organisational standing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'procedure' in management is best described as:", "options": [
            "A series of specific steps to be followed to carry out a particular activity", "A broad, general organisational goal",
            "A financial ratio", "An informal rumour within the organisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Decision-making' in management refers to:", "options": [
            "The process of selecting the best course of action among available alternatives", "Only recording a decision after it has already been made by someone else",
            "Avoiding the need to choose between any alternatives", "An activity performed only by non-managerial employees"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The FIRST step in a rational decision-making process is typically to:", "options": [
            "Identify and define the problem", "Immediately implement a random solution",
            "Evaluate the outcome, before any decision is made", "Ignore the situation entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Programmed decisions' refer to decisions that are:", "options": [
            "Routine and repetitive, made according to established rules or procedures", "Completely unique and made only once in an organisation's history",
            "Made without any prior guideline whatsoever", "Only made by the most junior employee"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Non-programmed decisions' refer to decisions that are:", "options": [
            "Novel, unstructured, and typically require significant managerial judgement", "Highly routine and repetitive",
            "Made using a fixed checklist with no judgement required", "Always made by machines with no human input"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Decision-making under risk' refers to a situation where:", "options": [
            "The outcomes of alternatives are not certain, but their probabilities can be estimated", "All outcomes are known with complete certainty",
            "No information whatsoever is available about outcomes", "There is only ever one possible outcome"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Decision-making under uncertainty' refers to a situation where:", "options": [
            "Neither the outcomes nor their probabilities can be reliably estimated", "All outcomes and their exact probabilities are perfectly known",
            "Only one alternative exists with a guaranteed result", "The decision has already been made by someone else"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A SWOT analysis used in strategic planning stands for:", "options": [
            "Strengths, Weaknesses, Opportunities, Threats", "Sales, Wages, Output, Tax", "Supply, Work, Ownership, Trade",
            "Strategy, Wealth, Objectives, Time"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Contingency planning' refers to preparing:", "options": [
            "Alternative plans in case the original plan fails or unexpected events occur", "A plan that never needs to change under any circumstance",
            "A plan applicable only to a single employee", "A plan with no reference to any potential risk"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an advantage of formal planning in an organisation?", "options": [
            "It provides direction, reduces uncertainty, and helps coordinate efforts", "It guarantees that no problems will ever arise",
            "It eliminates the need for any future decision-making", "It has no effect on organisational coordination"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'budget' is a type of plan that expresses:", "options": [
            "Expected results in numerical/financial terms", "Only a verbal description with no numbers",
            "An employee's personal opinion", "A plan with no time frame at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Management by Objectives (MBO)' is an approach where:", "options": [
            "Managers and employees jointly set specific, measurable objectives and review progress toward them", "Objectives are set solely by employees with no managerial input",
            "No objectives are ever formally defined", "Objectives are decided randomly with no review"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes a limitation of planning?", "options": [
            "Plans can become outdated or inaccurate due to unpredictable changes in the environment", "Planning guarantees a perfectly accurate prediction of the future in all cases",
            "Planning has no cost or time investment required", "Planning eliminates the need for any monitoring afterward"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why generating multiple alternatives is an important step in decision-making?", "options": [
            "It increases the likelihood of identifying the best possible course of action", "It guarantees the decision will always be free of any risk",
            "It is legally required to consider at least one hundred alternatives", "It eliminates the need to evaluate any alternative afterward"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Organizing": [
        {"q": "'Organising', as a management function, refers to:", "options": [
            "Arranging and structuring resources and tasks to implement plans effectively", "Only the process of setting long-term goals",
            "Only the act of monitoring completed work", "An activity unrelated to task or resource arrangement"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Organisational structure' refers to:", "options": [
            "The formal arrangement of jobs, reporting relationships, and authority within an organisation", "A single employee's personal daily schedule",
            "The organisation's annual profit figure", "A type of marketing strategy"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Departmentalisation' refers to the process of:", "options": [
            "Grouping jobs and activities into logical units or departments", "Eliminating all departments within an organisation",
            "Hiring only a single employee for the entire organisation", "Calculating a company's tax obligations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Functional departmentalisation' groups jobs based on:", "options": [
            "Similar functions or activities, such as marketing, finance, and production", "Random employee names in alphabetical order",
            "Geographic location only, with no reference to function", "Employee age only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Chain of Command' refers to:", "options": [
            "The unbroken line of authority extending from the top to the bottom of an organisation", "A method of calculating employee salaries",
            "A financial ratio used in accounting", "A type of marketing channel"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Span of Control' refers to:", "options": [
            "The number of subordinates a manager can effectively supervise", "The total number of departments in an organisation",
            "The geographic distance between two offices", "The number of years a manager has worked"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'narrow span of control' typically results in an organisational structure that is:", "options": [
            "Tall, with many levels of hierarchy", "Flat, with very few levels of hierarchy",
            "Entirely without any hierarchy", "Identical to a wide span of control in every respect"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'wide span of control' typically results in an organisational structure that is:", "options": [
            "Flat, with fewer levels of hierarchy", "Tall, with many levels of hierarchy",
            "Impossible to implement in practice", "Unrelated to the number of hierarchy levels"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Delegation of authority' refers to:", "options": [
            "A manager assigning part of their authority and responsibility to a subordinate", "A manager performing every task personally with no assistance",
            "The complete removal of all authority from an organisation", "An employee assigning tasks to their own manager"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Centralisation' in an organisational structure means that decision-making authority is:", "options": [
            "Concentrated mainly at the top levels of management", "Spread widely and equally among all employees",
            "Held only by customers", "Absent entirely from the organisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Decentralisation' in an organisational structure means that decision-making authority is:", "options": [
            "Distributed to lower levels of management throughout the organisation", "Concentrated entirely with a single top executive",
            "Given only to external consultants", "Removed from the organisation entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Line authority' in an organisation refers to authority that:", "options": [
            "Flows directly down the chain of command, giving a superior direct control over subordinates", "Exists only in an advisory capacity with no direct control",
            "Applies only to external contractors", "Has no relationship to the chain of command"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Staff authority' in an organisation refers to authority that is primarily:", "options": [
            "Advisory/support in nature, assisting line managers without direct command over them", "The highest form of direct command authority in the organisation",
            "Applicable only to the CEO", "Identical in every way to line authority"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'matrix organisational structure' combines:", "options": [
            "Functional and project/product-based reporting relationships simultaneously", "Only a single reporting relationship with no overlap",
            "No formal structure whatsoever", "Only geographic departmentalisation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "An 'organisation chart' is a visual tool used to show:", "options": [
            "The formal structure, reporting relationships, and hierarchy of an organisation", "The organisation's total annual sales figures",
            "A single employee's personal résumé", "A marketing advertisement"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Job design' in the organising function refers to:", "options": [
            "Determining the specific tasks, duties, and responsibilities of a given job", "Only setting an employee's salary",
            "Only choosing an employee's uniform colour", "An activity unrelated to any job's actual content"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a benefit of effective delegation?", "options": [
            "It frees up managerial time for higher-level tasks while developing subordinates' skills", "It guarantees subordinates will never make any mistake",
            "It eliminates the need for any managerial oversight", "It removes all responsibility from the manager permanently"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Unity of Direction' as an organising principle means that:", "options": [
            "Activities with the same objective should be directed by one manager using one plan", "Every employee should have a completely different, unrelated objective",
            "Multiple unrelated plans should always be used for a single objective", "Direction should change randomly every day"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Geographic departmentalisation is most suitable for organisations that:", "options": [
            "Operate across multiple distinct regions with different local needs", "Operate in only a single, small local market",
            "Have no physical location at all", "Sell only one single product with no regional variation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why organising is considered essential after planning?", "options": [
            "It translates plans into an actionable structure by assigning resources, tasks and authority", "Organising has no connection to previously made plans",
            "Organising always occurs before any planning takes place", "Organising eliminates the need for any further management function"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Leading": [
        {"q": "'Leading', as a management function, primarily involves:", "options": [
            "Motivating, directing, and influencing employees to work toward organisational goals", "Only recording financial transactions",
            "Only designing the organisational chart", "An activity with no connection to employee motivation"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Leadership' is best defined as:", "options": [
            "The ability to influence and guide others toward achieving a goal", "The act of performing every task alone with no team involvement",
            "A title given automatically to the most senior employee with no reference to influence", "An activity unrelated to motivating others"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'autocratic' leadership style is characterised by:", "options": [
            "The leader making decisions unilaterally with little input from subordinates", "The leader always involving the entire team in every decision",
            "The complete absence of any leader", "Decisions made entirely by subordinates with no leader involvement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'democratic' (participative) leadership style is characterised by:", "options": [
            "The leader involving subordinates in the decision-making process", "The leader making all decisions alone with zero input from others",
            "The complete absence of any decision-making process", "A style used only in government organisations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'laissez-faire' (free-rein) leadership style is characterised by:", "options": [
            "The leader giving subordinates significant freedom and minimal direct supervision", "The leader controlling every single detail of subordinates' work",
            "The complete absence of any subordinates", "A style that eliminates all employee freedom"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Maslow's Hierarchy of Needs theory proposes that human needs are arranged in order from:", "options": [
            "Basic physiological needs up to self-actualisation needs", "Only financial needs, with no other category",
            "Random, unordered needs with no hierarchy", "Only social needs, with no physical needs included"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "According to Maslow, once a lower-level need (e.g. physiological) is satisfied, an individual is typically motivated by:", "options": [
            "The next higher-level need in the hierarchy", "No further needs of any kind", "The exact same lower-level need repeatedly with no progression",
            "A need entirely unrelated to the hierarchy"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Herzberg's Two-Factor Theory distinguishes between:", "options": [
            "'Hygiene factors' (which prevent dissatisfaction) and 'motivators' (which create satisfaction)", "Only financial factors, with no other category",
            "Only physical working conditions, with no reference to psychological factors", "A single unified factor with no distinction at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "According to Herzberg, which of the following is typically classified as a 'hygiene factor'?", "options": [
            "Salary and working conditions", "Recognition for achievement", "Opportunity for personal growth",
            "The sense of responsibility given to an employee"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Motivation' in a workplace context refers to:", "options": [
            "The internal drive that energises and directs an employee's behaviour toward achieving goals", "A financial statement prepared at year-end",
            "A type of organisational chart", "An activity unrelated to employee behaviour"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Communication' in the leading function refers to:", "options": [
            "The process of exchanging information and understanding between individuals in an organisation", "Only the act of writing a memo with no exchange of understanding",
            "An activity performed only by top management", "A process irrelevant to leadership effectiveness"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Formal communication' within an organisation follows:", "options": [
            "The official organisational structure and designated channels", "No structure at all, occurring entirely at random",
            "Only informal social gatherings outside of work", "A channel used exclusively by customers"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Informal communication' (the 'grapevine') within an organisation refers to:", "options": [
            "Unofficial communication that flows outside formal organisational channels", "Only official memos issued by top management",
            "A communication method that is always completely accurate", "A channel used only for legal contracts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Team building' as a leadership activity primarily aims to:", "options": [
            "Improve cooperation, trust, and performance among group members", "Increase conflict and division among employees",
            "Eliminate the need for any teamwork", "Reduce communication between team members"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which leadership style is generally considered most effective in a crisis requiring quick, decisive action?", "options": [
            "Autocratic leadership, due to the need for rapid decision-making", "Laissez-faire leadership, allowing complete freedom with no direction",
            "A style with absolutely no leader present", "A style that requires lengthy group consensus before any action"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Trait theory' of leadership suggests that effective leaders:", "options": [
            "Possess certain inherent personal characteristics that distinguish them from non-leaders", "Are created entirely by random chance with no identifiable characteristics",
            "Have no distinguishing characteristics whatsoever", "Are determined solely by their job title"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Situational leadership' theory suggests that:", "options": [
            "The most effective leadership style depends on the specific situation and the followers involved", "A single leadership style is always effective in every situation",
            "Leadership style has no connection to the situation at all", "Only autocratic leadership can ever be effective"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why effective leading is essential even after good planning and organising?", "options": [
            "Plans and structures alone do not guarantee action - people must be motivated and directed to actually carry them out",
            "Leading has no effect on whether plans are actually executed", "Once a plan exists, no further employee motivation is ever needed",
            "Leading is only relevant to non-business organisations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Empowerment' of employees in a leadership context refers to:", "options": [
            "Giving employees greater authority and responsibility to make decisions in their own area of work", "Removing all authority and responsibility from employees",
            "A concept applicable only to top management", "An approach that eliminates all employee decision-making"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a common barrier to effective communication in an organisation?", "options": [
            "Use of unclear or overly technical language between sender and receiver", "Perfectly clear language understood identically by everyone involved",
            "Complete absence of any message being sent", "A message sent with no sender or receiver at all"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Controlling": [
        {"q": "'Controlling', as a management function, refers to:", "options": [
            "Monitoring performance, comparing it to standards, and taking corrective action as needed", "Only the initial process of setting goals",
            "Only the act of hiring new employees", "An activity unrelated to performance monitoring"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The controlling function is closely linked to planning because:", "options": [
            "Plans provide the standards against which actual performance is measured during controlling", "Controlling has no relationship to planning whatsoever",
            "Controlling always occurs before any planning takes place", "Plans are created only after controlling is complete"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The basic control process typically involves the steps:", "options": [
            "Setting standards, measuring performance, comparing performance to standards, and taking corrective action",
            "Only measuring performance with no standard-setting", "Only taking corrective action with no prior measurement",
            "Ignoring performance entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Standards' in the control process refer to:", "options": [
            "Predetermined criteria or benchmarks used to evaluate performance", "A type of financial statement",
            "An employee's personal name tag", "A random number with no relationship to performance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Feedback control' involves evaluating performance:", "options": [
            "After an activity has been completed, to inform future actions", "Only before an activity begins",
            "Only while an activity is happening, never after", "Without any reference to the activity's outcome"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Concurrent control' involves monitoring and adjusting activities:", "options": [
            "While they are actually occurring, in real time", "Only after the activity is fully completed",
            "Only before the activity begins", "Without any reference to ongoing activities"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Feedforward (preliminary) control' focuses on:", "options": [
            "Preventing problems before an activity begins, through proactive measures", "Only correcting problems long after they have occurred",
            "Ignoring potential problems entirely", "Controlling activities only after they are finished"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'budgetary control' system uses budgets primarily to:", "options": [
            "Compare actual financial performance against planned financial targets", "Only record employee attendance",
            "Only design the company's advertising", "Determine an employee's personal opinions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Variance analysis' in budgetary control refers to:", "options": [
            "Examining the difference between actual and budgeted figures to identify causes", "Ignoring any difference between actual and budgeted figures",
            "A method used only in marketing, not finance", "A process unrelated to budgets"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of a non-financial control tool?", "options": [
            "Quality control inspection of finished products", "A cash flow budget",
            "A profit and loss statement", "A balance sheet"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Corrective action' in the control process is taken when:", "options": [
            "Actual performance deviates significantly from the established standard", "Actual performance exactly matches the standard, requiring no change",
            "No standard has ever been set", "Performance has not yet been measured at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Effective control systems are generally characterised by being:", "options": [
            "Accurate, timely, and relevant to the activity being controlled", "Deliberately vague and delayed to avoid influencing behaviour",
            "Completely unrelated to the organisation's actual goals", "Applied only once a year regardless of the activity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Management by Exception' is a control principle where managers focus their attention primarily on:", "options": [
            "Significant deviations from standards, rather than every routine detail", "Every single minor detail regardless of significance",
            "Activities that have no deviation from standard at all", "Random activities chosen without reference to performance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why controlling is often called the 'final' link in the management process, while also feeding back into planning?", "options": [
            "It evaluates whether objectives were met and provides information used to adjust future plans", "It has no connection to any other management function",
            "It always occurs before planning, never after", "It is entirely unrelated to organisational objectives"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A performance appraisal system used to evaluate individual employees is a form of:", "options": [
            "Control focused on human resources/personnel performance", "A financial statement only",
            "A marketing strategy", "A type of organisational chart"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a common challenge in implementing an effective control system?", "options": [
            "Setting standards that are realistic yet challenging, and gathering accurate, timely performance data", "Control systems never face any practical challenge",
            "Standards are always perfectly accurate with no effort required", "Performance data is always instantly and perfectly available with no cost"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Inventory control techniques help an organisation primarily by:", "options": [
            "Ensuring optimal stock levels are maintained, avoiding both shortages and excess", "Eliminating the need to ever purchase any inventory",
            "Guaranteeing inventory theft never occurs", "Having no relationship to stock levels at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the relationship between controlling and employee morale if poorly implemented?", "options": [
            "Overly strict or punitive control systems can reduce employee morale and trust", "Control systems always improve morale no matter how they are implemented",
            "Controlling has no possible effect on employee morale", "Control systems are only ever viewed positively by employees"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Quality control in a manufacturing business primarily aims to:", "options": [
            "Ensure products meet defined quality standards before reaching customers", "Increase the number of defective products produced",
            "Eliminate the need for any product standards", "Have no relationship to customer satisfaction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of the controlling function in management?", "options": [
            "To ensure that actual organisational performance aligns with planned objectives, correcting deviations as needed", "To eliminate the need for any future planning",
            "To operate completely independently of any prior plan or standard", "To focus solely on punishing employees with no constructive purpose"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Others Management Function": [
        {"q": "'Staffing', often discussed alongside the core POLC functions, primarily involves:", "options": [
            "Recruiting, selecting, training and developing the right people for organisational roles", "Only calculating a company's tax liability",
            "Only designing product packaging", "An activity unrelated to human resources"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Coordinating', sometimes treated as a distinct management function, refers to:", "options": [
            "Synchronising the efforts of different individuals and departments to achieve unity of action", "Deliberately creating conflict between departments",
            "Isolating each department with no communication", "An activity irrelevant to achieving organisational goals"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Innovating', as a managerial function emphasised in some frameworks, refers to management's role in:", "options": [
            "Generating and implementing new ideas, products or processes", "Strictly repeating the exact same processes with no change",
            "Avoiding any form of change indefinitely", "An activity with no relevance to organisational growth"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Representing', as a managerial function, refers to a manager's role in:", "options": [
            "Representing the organisation to external stakeholders such as government, customers, and the public", "Only representing their own personal interests",
            "Avoiding any contact with external parties", "A function performed solely by non-managerial staff"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The staffing function typically includes which of the following activities?", "options": [
            "Recruitment, selection, and performance appraisal of employees", "Only bookkeeping and ledger posting",
            "Only advertising campaigns", "Only physical plant maintenance"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Human Resource Planning' involves forecasting an organisation's:", "options": [
            "Future workforce needs and how to meet them", "Future raw material needs only",
            "Future advertising budget only", "Future tax obligations only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a reason some management theorists treat 'staffing' as a function distinct from 'organising'?", "options": [
            "Staffing focuses specifically on people (recruitment, selection, development), while organising focuses on structural arrangement of jobs",
            "Staffing and organising are always considered completely identical with no distinction", "Staffing has no connection to human resources at all",
            "Organising only applies to non-human resources"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Coordination' is sometimes called the 'essence of management' because it:", "options": [
            "Is implicitly involved in every other management function, ensuring harmony of effort", "Is entirely unrelated to any other management function",
            "Applies only to the controlling function", "Is only relevant to very small organisations"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of external coordination a manager might perform?", "options": [
            "Liaising with suppliers, government bodies, or industry associations", "Only coordinating with the manager's own personal family",
            "An activity that never involves any external party", "Only coordinating tasks within a single individual's own work"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Innovation management in an organisation is important mainly because it helps the organisation:", "options": [
            "Adapt to changing markets and maintain competitiveness", "Avoid all forms of change permanently",
            "Eliminate the need for any future planning", "Guarantee immediate profit with no risk"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A manager acting as a company's spokesperson to the media is performing which type of role?", "options": [
            "A representational/representing role", "A purely technical/manufacturing role",
            "A purely clerical/filing role", "A role unrelated to management"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'training and development' within the staffing function?", "options": [
            "Improving employees' skills and knowledge to perform their roles effectively", "Reducing employee skills deliberately",
            "An activity performed only once, never repeated", "An activity unrelated to employee performance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Succession planning' within staffing refers to:", "options": [
            "Preparing employees to fill key organisational positions in the future", "Ignoring the need for future leadership entirely",
            "A plan relevant only to entry-level positions", "A process unrelated to organisational continuity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Coordinating the activities of the production, marketing, and finance departments toward a single company goal is an example of:", "options": [
            "Interdepartmental coordination", "Complete departmental isolation", "A financial control technique only",
            "A staffing activity only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'innovating' is increasingly emphasised as a management function in modern, competitive markets?", "options": [
            "Rapid technological and market change requires organisations to continuously adapt and improve", "Markets today change less than they did in the past, reducing the need for innovation",
            "Innovation has no bearing on organisational survival", "Only very large multinational firms benefit from innovation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A manager negotiating a contract with an external supplier is primarily exercising which function?", "options": [
            "Representing/external coordination", "Only internal controlling", "Only staffing", "Only technical production work"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'orientation' (induction) as part of staffing?", "options": [
            "Introducing a new employee to the organisation, its culture, and their specific role", "Terminating an employee's contract",
            "An activity performed only for the CEO", "An activity unrelated to new employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes why coordination becomes MORE challenging as an organisation grows larger?", "options": [
            "More departments, employees, and activities increase the complexity of aligning everyone toward common goals", "Larger organisations automatically coordinate themselves with no management effort",
            "Coordination challenges decrease as organisations grow", "Organisational size has no relationship to coordination difficulty"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an example of 'innovating' within an existing business?", "options": [
            "Introducing a new digital payment option for customers", "Repeating last year's exact strategy with zero change",
            "Ignoring customer feedback entirely", "Reducing product quality without any strategic reason"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises why frameworks beyond the basic POLC (Planning, Organising, Leading, Controlling) sometimes add functions like staffing, coordinating, and innovating?", "options": [
            "To capture important managerial activities that may not be fully addressed within the four core functions alone",
            "Because the POLC framework has been proven completely incorrect and unusable", "Because staffing, coordinating and innovating have no relevance to management",
            "Because modern organisations no longer perform planning, organising, leading or controlling at all"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Contemporary issue on Management": [
        {"q": "'Globalisation' as a contemporary management issue refers to:", "options": [
            "The increasing interconnectedness of economies, markets and organisations across national borders", "The complete isolation of a business from all foreign markets",
            "A concept relevant only to government policy with no business relevance", "The elimination of all international trade"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Corporate Social Responsibility (CSR)' as a contemporary management concern refers to:", "options": [
            "An organisation's obligation to contribute positively to society and the environment", "An organisation's obligation to maximise profit with no regard for society",
            "A legal requirement that applies only to government agencies", "A concept with no relevance to modern business management"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Workforce diversity' as a contemporary management issue refers to managing employees who differ in:", "options": [
            "Gender, age, ethnicity, culture and other characteristics", "Only their job title, with no other differences considered",
            "Nothing at all - all employees are assumed identical", "Only their physical office location"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital transformation' in management refers to:", "options": [
            "The integration of digital technology into all areas of business, changing how organisations operate", "The complete rejection of all technology in business",
            "A concept relevant only to the entertainment industry", "An issue unrelated to modern organisational operations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Work-life balance' as a contemporary management concern refers to:", "options": [
            "Helping employees balance their professional responsibilities with personal life needs", "Requiring employees to work exclusively, with no personal time permitted",
            "A concept with no impact on employee productivity or retention", "An issue relevant only to senior executives"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Ethical management' emphasises that managerial decisions should be guided by:", "options": [
            "Moral principles and integrity, not just profit maximisation", "Profit maximisation alone, with no other consideration",
            "Random decision-making with no guiding principle", "Only the personal preference of the manager, regardless of impact on others"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sustainability' as a contemporary management issue emphasises:", "options": [
            "Meeting present business needs without compromising the ability of future generations to meet their own needs", "Maximising short-term profit with no regard for long-term consequences",
            "Ignoring environmental impact entirely", "A concept relevant only to the government, not business"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Change management' refers to the structured approach organisations use to:", "options": [
            "Transition individuals, teams and the organisation from a current state to a desired future state", "Avoid all forms of organisational change permanently",
            "Fire all existing employees whenever change occurs", "Ignore the impact of change on employees"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Remote/flexible work' has become a contemporary management issue mainly due to:", "options": [
            "Advances in digital communication technology enabling employees to work outside traditional offices", "A complete absence of any technology enabling such work",
            "A universal legal ban on working from any location other than an office", "No relevance to modern organisational practices"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Knowledge management' in contemporary organisations refers to:", "options": [
            "Systematically capturing, sharing and effectively using organisational knowledge and expertise", "Deliberately discarding all organisational knowledge and expertise",
            "An activity relevant only to educational institutions", "A concept unrelated to organisational performance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Managing a diverse, multigenerational workforce is a contemporary challenge because it requires managers to:", "options": [
            "Adapt their leadership and communication approaches to different generational expectations and values", "Treat every employee identically regardless of background or preference",
            "Ignore generational differences entirely", "Exclude certain age groups from the workplace"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes why CSR has become increasingly important to modern businesses?", "options": [
            "Stakeholders, including customers and investors, increasingly expect businesses to act responsibly toward society and environment",
            "CSR has no impact on a company's reputation or customer trust", "CSR is legally banned in most countries",
            "CSR only applies to government-owned enterprises"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Artificial Intelligence (AI)' as a contemporary management issue is primarily relevant because it:", "options": [
            "Is changing how organisations make decisions, automate processes, and interact with customers", "Has no relevance to any modern business function",
            "Can only be used in scientific laboratories, never in business", "Eliminates the need for any human management entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Crisis management' refers to an organisation's approach to:", "options": [
            "Preparing for, responding to, and recovering from unexpected disruptive events", "Deliberately creating crises within the organisation",
            "Ignoring any potential disruptive event entirely", "A concept relevant only to government agencies"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Employee wellbeing' as a contemporary management focus includes attention to:", "options": [
            "Employees' physical, mental and emotional health in the workplace", "Only an employee's physical office equipment",
            "An area with no connection to organisational productivity", "A concern relevant only outside of working hours"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Data privacy and security' has become a contemporary management issue mainly due to:", "options": [
            "The increasing collection and digital storage of sensitive customer and business information", "A complete absence of any digital data in modern organisations",
            "No relevance to customer trust or legal compliance", "A concept relevant only to the banking sector"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'agility' (the ability to adapt quickly) is emphasised in contemporary management thinking?", "options": [
            "Rapidly changing markets and technology require organisations to respond and adapt quickly to remain competitive", "Modern markets change far less frequently than in the past",
            "Agility has no bearing on organisational competitiveness", "Only small businesses need to be agile, not larger ones"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best describes the relationship between technology and contemporary management practice?", "options": [
            "Technology increasingly shapes how managers plan, communicate, and make decisions", "Technology has no influence on management practice whatsoever",
            "Modern managers are legally prohibited from using technology", "Technology only affects manufacturing, never management decisions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes 'stakeholder management' as a contemporary concern?", "options": [
            "Balancing the interests of various groups affected by the organisation, such as employees, customers, investors and community",
            "Focusing exclusively on shareholders with no regard for any other party", "Ignoring all external parties entirely",
            "A concept relevant only to non-profit organisations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why contemporary management issues are typically studied alongside classical management principles?", "options": [
            "Classical principles provide a foundation, while contemporary issues show how management must adapt to a changing environment",
            "Contemporary issues have completely replaced the need to understand any classical principle", "Classical principles remain entirely unchanged and irrelevant to modern issues",
            "There is no meaningful relationship between the two"],
         "correct": 0, "difficulty": "Hard"},
    ],
    "Business Letter Writing": [
        {"q": "A 'business letter' is best described as:", "options": [
            "A formal written communication used for official business purposes", "An informal message sent only between close friends",
            "A verbal conversation with no written record", "A document with no defined structure or purpose"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is a standard component of a formal business letter?", "options": [
            "The heading/letterhead, date, inside address, salutation, body, and closing", "Only a single word with no further content",
            "Only an image with no text", "A document with no sender information at all"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'salutation' in a business letter refers to:", "options": [
            "The greeting used to address the recipient, such as 'Dear Sir/Madam'", "The sender's final signature",
            "The letter's overall subject line only", "The postal stamp on the envelope"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'complimentary close' of a business letter (e.g. 'Yours faithfully') is typically placed:", "options": [
            "At the end of the letter, just before the signature", "At the very beginning, before the date",
            "In the middle of the body paragraph", "On the envelope only, never in the letter itself"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'inquiry letter' is written primarily to:", "options": [
            "Request information about a product, service or business matter", "Formally terminate an employee's contract",
            "Record a company's annual financial results", "Announce a company's permanent closure"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'letter of complaint' is written primarily to:", "options": [
            "Formally express dissatisfaction about a product, service or situation", "Congratulate a business on a recent achievement",
            "Request a job interview", "Provide a positive product review with no issue raised"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'order letter' is written primarily to:", "options": [
            "Formally request the purchase of goods or services from a supplier", "Formally resign from a job position",
            "Request a salary increment", "Announce a company holiday schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'cover letter' accompanying a job application typically serves to:", "options": [
            "Introduce the applicant and highlight their suitability for the position", "Replace the need for a résumé/CV entirely",
            "Serve as a legal employment contract", "Record the applicant's salary history in full detail"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the appropriate tone for a formal business letter?", "options": [
            "Polite, clear, and professional", "Casual and full of slang expressions",
            "Deliberately vague and ambiguous", "Aggressive and confrontational"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'subject line' of a business letter serves to:", "options": [
            "Briefly indicate the main purpose or topic of the letter", "Replace the need for a salutation entirely",
            "Serve as the sender's personal signature", "Indicate the letter's exact word count"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'memorandum' (memo) differs from a formal business letter mainly in that a memo is typically:", "options": [
            "Used for internal communication within an organisation, often with a simpler format", "Used exclusively for external communication with customers",
            "Always longer and more formal than a letter", "Never used in any business setting"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an important principle of effective business writing?", "options": [
            "Clarity and conciseness, avoiding unnecessary jargon or complexity", "Maximum length regardless of relevance",
            "Deliberate ambiguity to avoid commitment", "Excessive use of technical jargon with no explanation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'circular letter' is typically used to:", "options": [
            "Communicate the same information to multiple recipients simultaneously, such as a price change announcement", "Communicate a private matter to a single specific individual only",
            "Serve as a binding legal contract only", "Replace the need for any other form of business communication"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Proofreading a business letter before sending is important mainly because it helps to:", "options": [
            "Catch errors in grammar, spelling, and factual accuracy that could harm the sender's professional image", "Increase the number of errors in the final document",
            "Guarantee the recipient will respond positively regardless of content", "Replace the need for a clear message entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the purpose of the 'inside address' in a formal business letter?", "options": [
            "It identifies the name and address of the recipient", "It identifies only the sender's personal home address",
            "It serves as the letter's title only", "It is optional and carries no informational purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'letter of credit' used in trade primarily serves to:", "options": [
            "Provide a guarantee of payment from a bank on behalf of a buyer to a seller", "Formally terminate a business relationship",
            "Request a product catalogue only", "Serve as an employee's resignation letter"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following is an appropriate closing salutation when the recipient's name is unknown (e.g. 'Dear Sir/Madam')?", "options": [
            "Yours faithfully", "Yours sincerely (used mainly when the recipient's name is known)", "Best wishes only, with no formal closing",
            "No closing is ever required in business writing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why maintaining a professional tone is especially important in written business communication (compared to casual conversation)?", "options": [
            "Written communication creates a lasting record and reflects on the sender's/organisation's professional reputation", "Written communication is always deleted immediately after being read",
            "Tone has no impact on how a written message is received", "Professional tone is only relevant in spoken communication"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'enclosure' notation at the end of a business letter indicates that:", "options": [
            "Additional documents are included along with the letter", "The letter has no further content beyond the notation",
            "The recipient must reply within 24 hours", "The letter is legally void"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the goal of a well-structured business letter?", "options": [
            "To clearly and professionally convey the intended message and achieve the desired response from the recipient", "To confuse the recipient as much as possible",
            "To avoid conveying any clear information", "To ensure the recipient never responds"],
         "correct": 0, "difficulty": "Medium"},
    ],
    "Business Plan": [
        {"q": "A 'business plan' is best defined as:", "options": [
            "A formal written document describing a business's goals, strategies, and how it intends to achieve them", "A single verbal conversation with no written record",
            "A document used only after a business has permanently closed", "A legal document with no connection to business strategy"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A key purpose of preparing a business plan is to:", "options": [
            "Guide business decision-making and attract potential investors or lenders", "Guarantee the business will never fail",
            "Replace the need for any future decision-making", "Serve no practical function once written"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Executive Summary' section of a business plan typically:", "options": [
            "Provides a concise overview of the entire business plan's key points", "Contains only the company's detailed financial statements",
            "Is placed only at the very end of the document", "Is the longest section of the entire plan"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Market Analysis' section of a business plan typically covers:", "options": [
            "Information about the target market, customers, and competitors", "Only the company's internal staff structure",
            "Only the company's tax obligations", "Only the founder's personal biography"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Marketing and Sales Strategy' section of a business plan describes:", "options": [
            "How the business intends to attract and retain customers and generate sales", "Only the company's office layout",
            "Only the company's employee benefits package", "Only the company's legal registration number"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Financial Plan' section of a business plan typically includes:", "options": [
            "Projected income statements, cash flow forecasts, and funding requirements", "Only the founder's personal opinions",
            "Only the company's marketing slogan", "Only a list of employee names"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Organisational and Management' section of a business plan describes:", "options": [
            "The business's ownership structure and the management team's roles and experience", "Only the company's product packaging design",
            "Only the company's chosen advertising jingle", "Only the exact office furniture layout"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A business plan is particularly important when seeking a bank loan or investor funding because it:", "options": [
            "Demonstrates the viability and potential profitability of the business to lenders/investors", "Is legally irrelevant to any funding decision",
            "Guarantees automatic loan approval regardless of content", "Has no influence on an investor's decision"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'SWOT analysis' included in a business plan helps identify the business's:", "options": [
            "Strengths, Weaknesses, Opportunities, and Threats", "Sales, Wages, Output, and Tax obligations only",
            "Suppliers, Warehouses, Outlets, and Transport routes only", "Staff, Working hours, Overtime, and Tenure only"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Product/Service Description' section of a business plan primarily explains:", "options": [
            "What the business will sell and the value it offers to customers", "Only the personal hobbies of the founder",
            "Only the company's chosen office location with no product detail", "Only unrelated historical background information"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'break-even analysis' commonly included in the financial section of a business plan helps determine:", "options": [
            "The sales volume at which total revenue equals total cost", "The exact resale value of the business's fixed assets",
            "The founder's personal net worth", "The number of employees required by law"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes why a business plan should include a clearly defined target market?", "options": [
            "It helps focus marketing efforts and resources on the customers most likely to buy the product/service", "A defined target market has no impact on marketing effectiveness",
            "All businesses should target every possible customer with no focus", "Target markets are irrelevant to financial planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'competitive analysis' within a business plan primarily examines:", "options": [
            "The strengths and weaknesses of existing competitors in the market", "Only the business's own internal staff performance",
            "Only the government's tax policy", "Only unrelated international news events"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is a common reason new businesses fail, as often addressed by careful business planning?", "options": [
            "Insufficient market research or inadequate financial planning", "Excessive attention to customer needs",
            "Too much detailed financial forecasting", "Too much focus on identifying competitors"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'startup business plan' differs from a plan for an established business mainly in that it typically places more emphasis on:", "options": [
            "Validating the business concept and securing initial funding", "Only reporting many years of historical financial performance",
            "Only describing an already well-known, established brand", "Only detailing employee retirement benefits"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why a business plan is often described as a 'living document'?", "options": [
            "It should be periodically reviewed and updated as the business and its environment change", "It must be written once and never changed under any circumstance",
            "It has no ongoing relevance after the business launches", "It is discarded immediately after being submitted to a bank"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'mission statement' within a business plan primarily communicates:", "options": [
            "The core purpose and values of the business", "Only the business's tax identification number",
            "Only a list of the business's physical assets", "Only the founder's personal contact details"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best describes the role of 'goals and objectives' within a business plan?", "options": [
            "They provide specific, measurable targets the business aims to achieve within a defined timeframe", "They are optional and carry no strategic importance",
            "They must always be identical for every business regardless of industry", "They replace the need for any financial planning"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why lenders and investors scrutinise the financial projections in a business plan carefully?", "options": [
            "To assess the realism of the plan and the likelihood of the business generating sufficient returns to repay funding", "Financial projections have no bearing on lending decisions",
            "Lenders are legally required to ignore financial information", "Financial projections are always guaranteed to be completely accurate"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall value of preparing a business plan, even for a small business with no external funding needs?", "options": [
            "It clarifies strategy, anticipates challenges, and provides a roadmap for decision-making", "It has no value whatsoever for a business not seeking external funding",
            "It is required only for businesses with over 1,000 employees", "It guarantees the business will never face any challenge"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
