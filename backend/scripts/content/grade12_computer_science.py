# -*- coding: utf-8 -*-
"""
NEB Grade 12 Management - Computer Science question bank (course 210,
subject 34301 "Computer Science", which already existed as an empty
7-chapter shell before this session).

Authored content (not content partner data - loaded with source='synthetic'
via scripts/load_by_chapter_id.py). This course's Computer Science shell
uses an advanced, programming/DBMS-focused chapter list, already
confirmed (earlier this session) to share zero exact chapter names with
course 38's real Computer Science content, which is an introductory/ICT
curriculum with entirely different topics ("3.1 Introduction" style
numbered sections). Different curricula, not a duplicate - so this is
fresh content rather than a link, matching this shell's own advanced
topic list. Keyed by verified integer chapter_id.

Chapter mapping (verified live):
  34532 - Programming in C
  34533 - Object-Oriented Programming (OOP)
  34529 - Database Management System (DBMS)
  34530 - Data communication and networking
  34531 - Web Technology II
  34534 - Software Process Model
  34535 - Recent Trends in Technology

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}. Never presented as content partner
content or as evidence about real students.
"""

QUESTIONS = {
    34532: [  # Programming in C
        {"q": "In the C programming language, every executable program must contain exactly one function named:", "options": [
            "main()", "start()", "begin()", "init()"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is the correct C syntax to declare an integer variable named 'x'?", "options": [
            "int x;", "integer x;", "x int;", "var x;"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, the '%d' format specifier used with printf()/scanf() is used for:", "options": [
            "Integers", "Floating-point numbers", "Single characters", "Strings only"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which header file must typically be included in a C program to use printf() and scanf()?", "options": [
            "stdio.h", "stdlib.h", "string.h", "math.h"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, the '=' operator is used for assignment, while '==' is used for:", "options": [
            "Equality comparison", "Addition", "Also assignment, with no functional difference from '='", "Division"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'for' loop in C is typically used when the programmer:", "options": [
            "Knows in advance how many times a block of code should repeat", "Never wants any code to repeat",
            "Wants a condition checked only after the loop body executes at least once, with no other option", "Wants to define a new function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'while' loop in C checks its condition:", "options": [
            "Before executing the loop body, so the body may never execute if the condition is false initially", "Only after the loop body has executed at least once, with no exception",
            "Exactly once and never again regardless of the condition", "At no point at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'do-while' loop in C differs from a 'while' loop mainly because it:", "options": [
            "Executes the loop body at least once before checking the condition", "Never checks any condition at all",
            "Checks the condition before every single iteration with no exception, identical to a while loop", "Cannot contain any statements inside its body"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In C, an 'array' is best described as:", "options": [
            "A collection of elements of the same data type stored in contiguous memory locations", "A single, standalone variable with no collection of elements",
            "A type that can only ever hold exactly one value", "A concept unrelated to storing multiple values"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'function' in C is used primarily to:", "options": [
            "Group a reusable block of code that performs a specific task", "Prevent any code from ever being reused",
            "Store a single constant value with no executable code", "A concept unrelated to organising code"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In C, a 'pointer' is a variable that:", "options": [
            "Stores the memory address of another variable", "Stores only integer values with no relation to memory addresses",
            "Cannot be used in any C program", "Is identical in every respect to a normal integer variable"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The '&' operator, when placed before a variable name in C, is used to:", "options": [
            "Obtain the memory address of that variable", "Perform a bitwise OR operation exclusively",
            "Convert the variable into a string", "A concept unrelated to memory addresses"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In C, 'recursion' refers to a function that:", "options": [
            "Calls itself, directly or indirectly, to solve a problem", "Can never call any other function, including itself",
            "Executes only once with no possibility of repeated execution", "Is unrelated to function calls of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'structure' (struct) in C allows a programmer to:", "options": [
            "Group variables of different data types under a single name", "Group variables only if they are of an identical data type",
            "Store only a single value with no grouping capability", "A concept unrelated to organising related data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In C, the 'if-else' statement is used to:", "options": [
            "Execute different blocks of code based on whether a condition is true or false", "Always execute every block of code regardless of any condition",
            "Repeat a block of code indefinitely with no condition", "Define a new variable"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, dividing an integer by zero (e.g. 5/0) typically results in:", "options": [
            "Undefined behaviour or a runtime error", "A guaranteed, well-defined result of exactly zero",
            "Automatic conversion of the divisor to 1", "A compile-time syntax error only, with no runtime consequence"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The scope of a 'local variable' declared inside a C function is limited to:", "options": [
            "That function only, unless explicitly passed elsewhere", "The entire program, accessible from any function with no restriction",
            "Only functions defined after it in the file", "No scope at all - it cannot be used anywhere"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'pointers' are considered a powerful but potentially risky feature of C?", "options": [
            "They allow direct memory manipulation, enabling efficient programs but also creating risk of errors like invalid memory access if misused", "Pointers have no practical use in C programming",
            "Pointers are always completely risk-free with no possibility of error", "Pointers can only be used for arithmetic operations, with no connection to memory"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the practical benefit of using functions to structure a C program rather than writing all code in a single main() block?", "options": [
            "Functions improve code organisation, reusability, and readability by breaking a program into manageable, purposeful units", "Functions make a program impossible to read or maintain",
            "Using functions has no benefit over writing all code in a single block", "Functions can only be used once and then must be deleted"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises why learning C is often considered foundational for computer science students, despite the availability of higher-level languages?", "options": [
            "C's close relationship to memory management and system-level operations builds a strong understanding of how programs actually execute", "C has no relevance to understanding programming concepts",
            "C is used exclusively for web design with no relevance to systems programming", "Learning C provides no transferable knowledge to other programming languages"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34533: [  # Object-Oriented Programming (OOP)
        {"q": "'Object-Oriented Programming (OOP)' is a programming paradigm centred around the concept of:", "options": [
            "Objects, which bundle together data and the functions (methods) that operate on that data", "Only sequential lines of code with no grouping of data and behaviour",
            "A paradigm unrelated to organising code around data", "Only mathematical formulas with no reference to code structure"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'class' in OOP is best described as:", "options": [
            "A blueprint or template used to create objects", "A single specific object instance with no template role",
            "A concept unrelated to object creation", "A type of loop structure"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'object' in OOP refers to:", "options": [
            "A specific instance created from a class", "A blueprint used to define a class",
            "A concept unrelated to classes", "A type of conditional statement"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Encapsulation', a core OOP principle, refers to:", "options": [
            "Bundling data and methods together while restricting direct access to some of an object's internal details", "Making all internal data of an object fully and directly accessible from anywhere with no restriction",
            "A concept unrelated to how objects manage their internal data", "Only applicable to functions, never to data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Inheritance', another core OOP principle, allows a new class to:", "options": [
            "Acquire properties and behaviours from an existing (parent) class", "Never share any property or behaviour with any other class",
            "A concept unrelated to relationships between classes", "Only be used with classes that have no other name"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Polymorphism' in OOP refers to the ability of:", "options": [
            "Different classes' objects to respond differently to the same method call or interface", "Every object to behave in an absolutely identical, uniform manner with no variation",
            "A concept unrelated to method behaviour across classes", "Preventing any two classes from ever sharing a method name"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Abstraction' in OOP involves:", "options": [
            "Hiding complex implementation details and exposing only essential features to the user", "Exposing every internal implementation detail with no simplification",
            "A concept unrelated to simplifying complex systems", "Only applicable to mathematical operations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'constructor' in OOP is a special method used to:", "options": [
            "Initialise a newly created object's data when it is instantiated", "Permanently delete an object from memory",
            "A concept unrelated to object creation", "Only print text to the screen with no other purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'destructor' in OOP is typically used to:", "options": [
            "Perform cleanup operations when an object is destroyed or goes out of scope", "Create a brand-new object from scratch",
            "A concept unrelated to object lifecycle", "Only initialise a class's static variables"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Access specifiers' such as 'private' and 'public' in OOP languages control:", "options": [
            "Which parts of a program can access a class's members (data/methods)", "The colour scheme of a program's output",
            "A concept unrelated to controlling access to class members", "Only the speed at which a program executes"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Method overloading', a form of polymorphism, allows a class to have:", "options": [
            "Multiple methods with the same name but different parameter lists", "Only a single method defined across the entire program, with no duplication of names",
            "A concept unrelated to defining multiple related methods", "Methods that can never take any parameters at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Method overriding' occurs when a subclass:", "options": [
            "Provides its own specific implementation of a method already defined in its parent class", "Deletes a method entirely from the parent class with no replacement",
            "A concept unrelated to inheritance", "Can only use the exact implementation defined in the parent class with no modification"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A key advantage of using 'inheritance' in software design is that it:", "options": [
            "Promotes code reuse by allowing new classes to build on existing ones", "Forces every class to be written entirely from scratch with no reuse",
            "Has no practical benefit for software design", "Only applies to mathematical calculations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In OOP, a 'parent class' (or base class) is a class from which:", "options": [
            "Other classes (child/derived classes) inherit properties and behaviours", "No other class can ever inherit anything",
            "Only a single object can ever be created, with no further classes derived", "A concept unrelated to inheritance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best illustrates 'encapsulation' in a real-world analogy?", "options": [
            "A car's engine internals being hidden from the driver, who interacts only with the accelerator and steering wheel", "A car with no separation between its internal mechanisms and the driver's controls",
            "A concept with no real-world analogy of any kind", "A car engine that exposes every internal component directly to the driver with no abstraction"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'polymorphism' is useful in software design?", "options": [
            "It allows a single interface to work with different underlying object types, making code more flexible and extensible", "It forces every object in a program to behave in exactly the same, rigid way",
            "It has no practical benefit for designing flexible software", "It applies only to a single specific class with no broader applicability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes a 'class' from an 'object' in OOP terminology?", "options": [
            "A class is the blueprint/definition, while an object is a specific instance created from that blueprint", "A class and an object are always exactly identical concepts with no distinction",
            "An object always exists before its class is ever defined", "A class can only ever produce a single object, with no possibility of multiple instances"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'access specifiers' like private/public matter for good software design?", "options": [
            "They help protect an object's internal state from unintended external modification, supporting encapsulation", "Access specifiers have no practical effect on how a program behaves",
            "They are used only to change a program's visual appearance", "They prevent a class from ever being used within a program"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why OOP is widely used for building large, complex software systems?", "options": [
            "Its principles (encapsulation, inheritance, polymorphism, abstraction) support modularity, reuse, and maintainability at scale", "OOP has no practical advantage over any other programming paradigm for large systems",
            "OOP can only be used for very small, simple programs", "OOP principles make large software systems harder to maintain"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the relationship between the four core OOP principles (encapsulation, inheritance, polymorphism, abstraction)?", "options": [
            "Together they support building modular, reusable, and maintainable software organised around real-world-like objects", "The four principles are entirely unrelated to each other with no shared purpose",
            "Only one of the four principles is ever actually used in real OOP languages", "These principles apply exclusively to non-programming contexts"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34529: [  # Database Management System (DBMS)
        {"q": "A 'Database Management System (DBMS)' is software designed to:", "options": [
            "Store, organise, retrieve, and manage data efficiently and securely", "Only display images with no data storage capability",
            "A concept unrelated to storing or organising data", "Only manage a computer's physical hardware components"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'table' in a relational database consists of:", "options": [
            "Rows (records) and columns (fields/attributes)", "Only a single unstructured block of text",
            "A concept unrelated to organising data", "Only images with no textual or numeric data"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'primary key' in a database table is used to:", "options": [
            "Uniquely identify each record in that table", "Store a table's largest possible value with no reference to uniqueness",
            "A concept unrelated to identifying records", "Automatically delete duplicate records"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'foreign key' in a relational database is used to:", "options": [
            "Establish a link between records in two related tables", "Uniquely identify a record within its own table only, with no reference to any other table",
            "A concept unrelated to relationships between tables", "Encrypt data stored in a table"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'SQL (Structured Query Language)' is primarily used to:", "options": [
            "Define, manipulate, and query data in a relational database", "Design a website's visual layout",
            "A concept unrelated to databases", "Only compile programs written in C"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The SQL command 'SELECT' is used to:", "options": [
            "Retrieve data from one or more database tables", "Permanently delete an entire database",
            "A concept unrelated to querying data", "Only create a new empty table with no data retrieval"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The SQL command 'INSERT' is used to:", "options": [
            "Add new records into a database table", "Permanently delete a table's structure",
            "A concept unrelated to adding data", "Only retrieve existing data with no addition of new data"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Normalization' in database design refers to the process of:", "options": [
            "Organising data to reduce redundancy and improve data integrity", "Deliberately duplicating data across as many tables as possible",
            "A concept unrelated to database structure", "Only formatting the visual display of query results"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A key benefit of using a DBMS over storing data in plain flat files is:", "options": [
            "Improved data integrity, security, and efficient querying capabilities", "A guaranteed increase in data redundancy with no other benefit",
            "No meaningful benefit over flat files in any respect", "A DBMS can only store a single record at a time"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'one-to-many relationship' between two database tables means that:", "options": [
            "One record in the first table can relate to multiple records in the second table", "Every record in both tables must always be identical",
            "A concept unrelated to relationships between tables", "Only a single record can ever exist across both tables combined"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Data integrity' in a database refers to:", "options": [
            "The accuracy and consistency of data stored within the database", "A concept unrelated to the accuracy of stored data",
            "Only the physical security of the server hardware", "The visual formatting of a database's output"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'ACID properties' (Atomicity, Consistency, Isolation, Durability) describe key guarantees for:", "options": [
            "Reliable database transactions", "A database's visual user interface design",
            "A concept unrelated to how transactions are processed", "Only the physical storage capacity of a hard drive"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'query' in the context of a database refers to:", "options": [
            "A request for specific data or an operation on the database", "A permanent physical backup of the entire database",
            "A concept unrelated to requesting or manipulating data", "Only the database's initial installation process"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The SQL 'WHERE' clause is used to:", "options": [
            "Filter records based on a specified condition", "Permanently delete an entire table with no condition",
            "A concept unrelated to filtering query results", "Only sort results alphabetically with no filtering"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Database security' measures aim to protect data from:", "options": [
            "Unauthorised access, modification, or loss", "Guaranteeing unrestricted access to all users with no protection",
            "A concept unrelated to protecting stored data", "Only protecting a database's visual formatting"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'normalization' is important in relational database design?", "options": [
            "It reduces data redundancy and helps prevent inconsistencies when data is updated", "It has no practical benefit for database design",
            "It always increases redundancy with no benefit to data consistency", "It applies only to non-relational databases"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the purpose of a 'foreign key' in linking two related tables, such as 'Students' and 'Courses'?", "options": [
            "It allows records in one table (e.g. a student's enrolment) to reference a specific record in another table (e.g. a course), maintaining relational integrity", "A foreign key has no functional purpose in a relational database",
            "A foreign key is used only to make a table's data harder to read", "A foreign key can only be used within a single table with no reference to any other table"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why businesses widely rely on DBMS software rather than simple spreadsheet files for managing large-scale data?", "options": [
            "A DBMS provides more robust data integrity, security, concurrent access handling, and efficient querying for large or complex datasets", "Spreadsheets are always superior to a DBMS for managing any scale of data",
            "There is no practical difference between a DBMS and a spreadsheet for large-scale data management", "DBMS software cannot handle structured data of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a practical use of the SQL 'WHERE' clause?", "options": [
            "Retrieving only the records of students who scored above a certain grade threshold", "Retrieving every single record in a table with no filtering criteria applied",
            "Permanently deleting an entire database table", "Changing a table's overall visual appearance with no data filtering"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of studying DBMS concepts within a Computer Science curriculum?", "options": [
            "To understand how structured data is efficiently and reliably stored, organised, retrieved, and secured in real-world systems", "DBMS concepts have no practical application in real-world software systems",
            "DBMS is relevant only to database administrators, never to general software development", "Studying DBMS replaces the need to understand any programming concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34530: [  # Data communication and networking
        {"q": "'Data communication' refers to the process of:", "options": [
            "Transmitting data between two or more devices over a communication medium", "Only storing data permanently with no transmission",
            "A concept unrelated to transmitting information", "Only printing data onto paper"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'computer network' refers to:", "options": [
            "A group of interconnected computers/devices that can communicate and share resources", "A single, standalone computer with no external connections",
            "A concept unrelated to connecting multiple devices", "Only a single physical cable with no connected devices"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'LAN (Local Area Network)' typically covers:", "options": [
            "A relatively small geographic area, such as a single building or campus", "The entire globe with no size limitation",
            "A concept unrelated to network coverage area", "Only a single computer with no networked connection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'WAN (Wide Area Network)' typically covers:", "options": [
            "A large geographic area, potentially spanning cities, countries, or continents", "Only a single room within a building",
            "A concept unrelated to network coverage area", "Exactly the same physical area as a LAN, with no distinction"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'internet' can be described as:", "options": [
            "A global network connecting millions of smaller networks and devices worldwide", "A single, isolated computer with no external connectivity",
            "A concept unrelated to networking", "Only a single company's private internal network"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'IP address' refers to:", "options": [
            "A unique numerical identifier assigned to a device on a network", "A physical cable used to connect two computers",
            "A concept unrelated to identifying devices on a network", "Only the brand name of a networking device"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'router' in a network functions primarily to:", "options": [
            "Direct data packets between different networks", "Permanently store all data transmitted across a network with no forwarding function",
            "A concept unrelated to directing network traffic", "Only display a network's data visually with no forwarding role"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'protocol' in networking refers to:", "options": [
            "A set of rules governing how data is formatted and transmitted between devices", "A physical piece of networking hardware",
            "A concept unrelated to communication rules", "Only the brand of a network cable"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'TCP/IP', a foundational networking protocol suite, is primarily responsible for:", "options": [
            "Governing how data is transmitted and routed reliably across networks including the internet", "Only formatting the visual display of a webpage",
            "A concept unrelated to network communication", "Only managing a computer's internal file storage"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Bandwidth' in networking refers to:", "options": [
            "The maximum rate of data transfer across a network connection", "The physical length of a network cable",
            "A concept unrelated to data transfer capacity", "Only the number of devices connected to a network"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Network topology' refers to:", "options": [
            "The physical or logical arrangement of devices and connections within a network", "A concept unrelated to how a network is structured",
            "Only the brand of networking equipment used", "The specific data being transmitted across a network"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a 'star topology' network, all devices are connected to:", "options": [
            "A central hub or switch", "Each other directly, with no central connection point",
            "A concept unrelated to network arrangement", "No connection point of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Wireless networking' (Wi-Fi) allows devices to connect to a network:", "options": [
            "Without a direct physical cable connection, using radio waves", "Only through a direct, mandatory physical cable with no wireless option",
            "A concept unrelated to wireless communication", "Only via a single, fixed wired connection"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'firewall' in networking serves to:", "options": [
            "Monitor and control incoming/outgoing network traffic based on security rules", "Permanently disable all network connectivity",
            "A concept unrelated to network security", "Only increase a network's physical cable length"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Network security' measures aim to protect data and systems from:", "options": [
            "Unauthorised access, attacks, and data breaches", "Guaranteeing unrestricted access to all users with no protection whatsoever",
            "A concept unrelated to protecting networked systems", "Only protecting the physical appearance of network cabling"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why the OSI/TCP-IP layered model is useful for understanding networking?", "options": [
            "It breaks down complex network communication into manageable layers, each handling a specific aspect of data transmission", "It has no practical use for understanding how networks function",
            "It applies only to a single, obsolete networking technology with no modern relevance", "It combines all networking functions into a single, undivided layer"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the difference between a LAN and a WAN?", "options": [
            "A LAN covers a smaller, localised area (e.g. one building), while a WAN spans much larger distances (e.g. across cities or countries)", "A LAN and a WAN are always exactly identical in size and scope",
            "A WAN is always physically smaller than any LAN", "There is no meaningful distinction between the two terms"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'protocols' are essential for network communication to function correctly?", "options": [
            "They establish common, agreed-upon rules so that different devices and systems can reliably exchange data", "Protocols have no bearing on whether devices can successfully communicate",
            "Each device can use entirely its own, unique rules with no need for any shared standard", "Protocols are relevant only to a single specific brand of networking hardware"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the practical role of a 'firewall' in a business network?", "options": [
            "Blocking unauthorised external attempts to access the company's internal network while allowing legitimate traffic", "Permanently disconnecting the company's network from any external communication",
            "A concept with no practical security application", "Increasing a network's physical bandwidth capacity"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall importance of studying data communication and networking within Computer Science?", "options": [
            "It provides the foundational understanding of how devices and systems exchange data reliably and securely, underlying most modern computing applications", "Networking concepts have no relevance to how modern software or the internet functions",
            "Data communication is relevant only to specialised network engineers, never to general computer science understanding", "Networking is a purely historical topic with no relevance to current technology"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34531: [  # Web Technology II
        {"q": "'HTML (HyperText Markup Language)' is primarily used to:", "options": [
            "Structure the content of a web page", "Compile a program's machine code",
            "A concept unrelated to web page structure", "Only manage a database's internal storage"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'CSS (Cascading Style Sheets)' is primarily used to:", "options": [
            "Style and visually format the presentation of a web page", "Structure a web page's raw content with no styling capability",
            "A concept unrelated to a webpage's visual appearance", "Only manage a server's internal file storage"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'JavaScript' is commonly used in web development to:", "options": [
            "Add interactivity and dynamic behaviour to a web page", "Only define a webpage's static structure with no interactivity",
            "A concept unrelated to enhancing web pages", "Only style a webpage's colours with no scripting capability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'client-server model' in web technology describes how:", "options": [
            "A client (e.g. browser) requests resources or services from a server, which responds accordingly", "A server and client are always the exact same single machine with no distinction",
            "A concept unrelated to how web requests are processed", "Only servers exist, with no client ever making any request"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'HTTP (HyperText Transfer Protocol)' is the protocol primarily used for:", "options": [
            "Transferring web page data between a client (browser) and a web server", "Only sending emails between two mail servers",
            "A concept unrelated to transferring web content", "Only managing a database's internal indexing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'HTTPS' differs from HTTP mainly in that HTTPS:", "options": [
            "Encrypts the data transferred between client and server for greater security", "Provides no security or encryption whatsoever, identical to HTTP",
            "A concept unrelated to secure data transfer", "Is used only for offline, non-networked file transfer"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Server-side scripting' (e.g. PHP, Node.js) refers to code that executes:", "options": [
            "On the web server, before the resulting content is sent to the client", "Only within the client's browser with no server involvement",
            "A concept unrelated to how dynamic web content is generated", "Only on a completely offline, disconnected machine"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Client-side scripting' (e.g. JavaScript running in a browser) refers to code that executes:", "options": [
            "Within the user's web browser", "Only on the web server, never within the browser",
            "A concept unrelated to browser-based execution", "Only during the server's initial installation process"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'responsive web design' aims to ensure a website:", "options": [
            "Displays and functions well across different screen sizes and devices", "Functions correctly only on a single specific screen size with no adaptability",
            "A concept unrelated to how a website adapts to devices", "Cannot be viewed on any device other than a desktop computer"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'web framework' (e.g. for building websites more efficiently) provides developers with:", "options": [
            "Pre-built tools, libraries, and structure to speed up and standardise web development", "No practical benefit over writing every single line of code entirely from scratch",
            "A concept unrelated to building websites more efficiently", "Only a visual theme with no underlying code structure"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Content Management System (CMS)' software, such as WordPress, allows users to:", "options": [
            "Create and manage website content without necessarily writing code directly", "Only write raw machine code with no content management capability",
            "A concept unrelated to managing website content", "Exclusively manage a network's physical hardware"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'API (Application Programming Interface)', relevant to modern web applications, allows:", "options": [
            "Different software systems to communicate and exchange data with one another", "Only a single program to run in complete isolation with no external communication",
            "A concept unrelated to software communication", "Only a webpage's visual styling, with no data exchange capability"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Web hosting' refers to the service that:", "options": [
            "Stores and makes a website's files accessible on the internet via a server", "Only designs a website's visual layout with no storage or server role",
            "A concept unrelated to making a website accessible online", "Only manages a company's internal accounting records"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'domain name' (e.g. example.com) serves to:", "options": [
            "Provide a human-readable address for a website, mapped to a numerical IP address", "Replace the need for any web server entirely",
            "A concept unrelated to website addressing", "Only refer to a company's internal accounting code"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Web security' concerns for modern web applications include protecting against threats such as:", "options": [
            "SQL injection and cross-site scripting (XSS) attacks", "Threats that do not exist in any web application context",
            "A concept unrelated to protecting a website's users or data", "Only threats related to physical hardware theft"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the difference between 'client-side' and 'server-side' scripting?", "options": [
            "Client-side scripts run in the user's browser, while server-side scripts run on the web server before content reaches the browser", "Client-side and server-side scripting always execute in exactly the same location",
            "There is no meaningful technical distinction between the two approaches", "Server-side scripting can only ever run within a user's browser"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'responsive web design' has become increasingly important for modern websites?", "options": [
            "Users access websites from a wide variety of devices with different screen sizes, so adaptable layouts improve usability across all of them", "All users access websites using an identical screen size, so responsiveness provides no benefit",
            "Responsive design has no bearing on how usable a website is across devices", "Responsive design is relevant only to desktop computers, not to any other device"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the security benefit of using HTTPS rather than plain HTTP for a website handling sensitive user data?", "options": [
            "HTTPS encrypts data in transit, making it much harder for an attacker to intercept and read sensitive information", "HTTPS provides no additional security benefit over plain HTTP",
            "HTTPS only affects a website's visual appearance, not its security", "Plain HTTP already fully encrypts all transmitted data by default"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the practical use of an API in a modern web application?", "options": [
            "A weather app on a website retrieving live weather data from a separate weather service's API", "A webpage displaying only static, permanently fixed text with no external data of any kind",
            "A concept with no practical real-world web application", "An API used exclusively to change a webpage's font style"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall relationship between HTML, CSS, and JavaScript in building a modern website?", "options": [
            "HTML structures the content, CSS styles its presentation, and JavaScript adds interactivity and dynamic behaviour", "The three technologies are functionally identical with no distinct roles",
            "Only one of the three technologies is ever actually needed to build any website", "CSS is responsible for structuring content, while HTML handles visual styling"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34534: [  # Software Process Model
        {"q": "A 'Software Process Model' provides a structured approach to guide:", "options": [
            "The stages and activities involved in developing software, from planning through deployment", "Only the final marketing of a completed software product",
            "A concept unrelated to organising software development activities", "Only the physical manufacturing of computer hardware"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Waterfall model' of software development is characterised by:", "options": [
            "A sequential, linear progression through defined phases such as requirements, design, implementation, and testing", "A highly iterative, non-sequential approach with no defined phase order",
            "A concept unrelated to structuring the development process", "The complete absence of any distinct development phase"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A key limitation of the Waterfall model is that it:", "options": [
            "Makes it difficult to accommodate changes once a phase is completed and the project has moved forward", "Allows unlimited, cost-free changes at any stage with no consequence",
            "Has no defined phases at all, making it impossible to limit in any way", "Is always faster than every other software process model in every situation"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The 'Agile' software development approach emphasises:", "options": [
            "Iterative development, flexibility, and close collaboration with stakeholders throughout the project", "A rigid, entirely fixed plan with zero flexibility once started",
            "A concept unrelated to how development activities are organised", "The complete absence of any collaboration with stakeholders"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Scrum', a popular Agile framework, organises work into fixed time periods called:", "options": [
            "Sprints", "Waterfalls", "Cascades", "Deployments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Spiral model' of software development combines elements of iterative development with a strong emphasis on:", "options": [
            "Risk analysis and management at each cycle", "Complete avoidance of any risk assessment",
            "A concept unrelated to managing project risk", "A strictly single-pass, non-iterative approach"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Requirements analysis', typically an early phase in a software process model, involves:", "options": [
            "Gathering and defining what the software system needs to accomplish", "Only writing the final user documentation after the software is complete",
            "A concept unrelated to understanding a project's goals", "Only compiling the source code with no analysis involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Software testing', a critical phase in the development process, aims to:", "options": [
            "Identify defects and verify that software meets its intended requirements", "Guarantee a program has zero possible defects with no verification needed",
            "A concept unrelated to verifying software quality", "Only occur before any code has been written"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Software maintenance', occurring after deployment, involves:", "options": [
            "Fixing defects, and updating or improving software after it has been released", "A phase that never occurs once software is deployed",
            "A concept unrelated to a software product's lifecycle after release", "Only the process of initially writing the very first version of the code"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Iterative development' involves:", "options": [
            "Repeating cycles of development, allowing refinement based on feedback over time", "A strictly single-pass process with absolutely no repetition",
            "A concept unrelated to refining software over time", "The complete absence of any feedback incorporation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'Software Requirements Specification (SRS)' document serves to:", "options": [
            "Formally document what a software system is expected to do", "Only describe the source code's internal syntax with no functional description",
            "A concept unrelated to defining a project's requirements", "Only serve as marketing material for the finished product"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Version control systems' (e.g. Git), used throughout modern software development, help teams to:", "options": [
            "Track changes to source code and collaborate effectively across a project", "Prevent any collaboration between multiple developers",
            "A concept unrelated to managing changes in a codebase", "Only manage a project's marketing materials"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Choosing an appropriate software process model for a project often depends on factors such as:", "options": [
            "Project size, requirement stability, and the level of stakeholder involvement needed", "A completely random choice with no relevant project factors",
            "A concept unrelated to project characteristics", "Only the personal preference of a single, uninvolved individual"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Continuous Integration (CI)', a modern software development practice, involves:", "options": [
            "Frequently merging and testing code changes to detect issues early", "Merging code changes only once, at the very end of a project, with no earlier testing",
            "A concept unrelated to managing code changes throughout a project", "Avoiding any testing of code changes entirely"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A key advantage of Agile methodologies over the traditional Waterfall model is Agile's greater:", "options": [
            "Ability to accommodate changing requirements throughout the development process", "Rigid inflexibility once a project begins, with no possibility of change",
            "A concept unrelated to how each model handles changing requirements", "Complete avoidance of any stakeholder feedback throughout development"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why the Waterfall model may be poorly suited to a project where requirements are expected to evolve significantly?", "options": [
            "Its sequential, linear structure makes it costly and difficult to revisit earlier phases once the project has progressed", "The Waterfall model is always the best choice for any project regardless of how requirements might change",
            "The Waterfall model has no defined phases, making it inherently as flexible as Agile", "Changing requirements have no bearing on how well a chosen process model performs"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why Agile's iterative 'sprints' can help reduce project risk compared to a single, long, uninterrupted development phase?", "options": [
            "Frequent short cycles allow for regular feedback and course-correction, catching problems earlier rather than at the very end of a long single phase", "Sprints have no relationship to how a project's risk is managed",
            "A single, long uninterrupted phase always reduces risk more effectively than iterative cycles", "Iterative development eliminates the need for any testing throughout the project"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the purpose of the 'Spiral model's emphasis on risk analysis at each iteration?", "options": [
            "It allows the project team to identify and address potential risks early and repeatedly throughout development, rather than only once", "Risk analysis has no bearing on how the Spiral model structures development",
            "The Spiral model performs risk analysis only once, at the very end of the project", "The Spiral model explicitly avoids any consideration of project risk"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates why 'software maintenance' is considered an ongoing phase rather than a one-time event?", "options": [
            "Software often requires bug fixes, security updates, and feature improvements throughout its operational life after initial release", "Software never requires any change or fix once it has been initially released",
            "Maintenance occurs only once, immediately before the software's initial release", "Maintenance has no connection to a software product's lifecycle after deployment"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of studying software process models within Computer Science?", "options": [
            "To understand structured approaches for managing the software development lifecycle effectively, from planning through maintenance", "Software process models have no practical relevance to how real software projects are managed",
            "This topic is relevant only to project managers, never to programmers", "Process models are relevant only to very large multinational companies, never smaller projects"],
         "correct": 0, "difficulty": "Medium"},
    ],
    34535: [  # Recent Trends in Technology
        {"q": "'Artificial Intelligence (AI)' broadly refers to:", "options": [
            "The capability of computer systems to perform tasks that typically require human intelligence", "A concept limited exclusively to physical robots with no software component",
            "A field with no relevance to modern computing", "Only a type of computer hardware component"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Machine Learning', a subset of AI, refers to systems that:", "options": [
            "Improve their performance on a task through experience/data, without being explicitly reprogrammed for every scenario", "Can never learn or improve from any data",
            "A concept unrelated to using data to improve performance", "Only apply to purely hardware-based systems with no software element"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cloud computing' allows users to access computing resources (storage, processing power, applications) primarily:", "options": [
            "Over the internet, from remote servers, rather than only from local hardware", "Only from a single physical device with no remote access",
            "A concept unrelated to internet-based resource access", "Only through a fully offline, disconnected network"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'Internet of Things (IoT)' refers to a network of:", "options": [
            "Everyday physical devices embedded with sensors/software that connect and exchange data over the internet", "Only traditional desktop computers with no other connected device type",
            "A concept unrelated to connected devices", "Devices that are permanently and completely disconnected from any network"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Big Data' refers to:", "options": [
            "Extremely large and complex datasets that traditional data-processing tools may struggle to handle effectively", "Only a small, simple dataset that fits easily on a single floppy disk",
            "A concept unrelated to the scale of modern data", "Data that is guaranteed to always be extremely easy to process with basic tools"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Blockchain technology' is fundamentally based on maintaining:", "options": [
            "A distributed, tamper-resistant digital ledger of transactions across multiple participants", "A single, centrally controlled database with no distribution across participants",
            "A concept unrelated to recording transactions", "Only a physical paper ledger with no digital component"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Cybersecurity', an increasingly critical field given recent technology trends, focuses on:", "options": [
            "Protecting systems, networks, and data from digital attacks and unauthorized access", "Guaranteeing systems are always completely open and accessible to anyone with no protection",
            "A concept unrelated to protecting digital systems", "Only the physical security of a building's entrance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Virtual Reality (VR)' technology creates:", "options": [
            "An immersive, simulated digital environment that a user can interact with", "Only a static, unchanging 2D image with no interactivity",
            "A concept unrelated to simulated digital environments", "Only physical, non-digital environments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Augmented Reality (AR)' differs from Virtual Reality mainly in that AR:", "options": [
            "Overlays digital elements onto the real-world environment, rather than fully replacing it", "Completely replaces the real world with an entirely simulated environment, identical to VR with no distinction",
            "A concept unrelated to enhancing real-world perception", "Has no relationship to digital overlays of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Automation', increasingly enabled by recent technology trends, refers to:", "options": [
            "Using technology to perform tasks with minimal human intervention", "A concept requiring maximum human intervention with no technological assistance",
            "A concept unrelated to reducing manual effort in tasks", "Only applicable to physical manufacturing, with no software application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Data privacy' concerns have grown alongside recent technology trends mainly due to:", "options": [
            "The increasing collection and use of personal data by digital platforms and services", "A complete absence of any data collection by modern digital platforms",
            "A concept unrelated to how personal data is used online", "Data privacy having no relevance to recent technological developments"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'5G technology' refers to a generation of mobile network technology offering:", "options": [
            "Significantly faster data speeds and lower latency compared to earlier generations", "Slower data speeds than all previous mobile network generations",
            "A concept unrelated to mobile network performance", "No improvement whatsoever over earlier mobile network generations"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Digital transformation' in businesses refers to the process of:", "options": [
            "Integrating digital technology into various areas of a business to improve operations and value delivery", "Businesses actively avoiding any use of digital technology",
            "A concept unrelated to how businesses adopt new technology", "Only relevant to businesses in a single specific industry, with no broader applicability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Ethical concerns around AI' commonly discussed in recent technology trends include issues such as:", "options": [
            "Bias in algorithms, job displacement, and data privacy", "A complete absence of any ethical consideration relevant to AI",
            "A concept unrelated to the societal impact of AI", "Concerns limited exclusively to AI's physical hardware requirements"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Remote work technology', accelerated by recent global trends, relies heavily on:", "options": [
            "Cloud computing, video conferencing, and collaborative digital tools", "A complete absence of any internet connectivity",
            "A concept unrelated to enabling work outside a traditional office", "Only physical paper documents with no digital tool involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'cloud computing' has become increasingly popular for businesses in recent years?", "options": [
            "It allows businesses to access scalable computing resources without the upfront cost of maintaining extensive physical infrastructure", "Cloud computing always costs significantly more than maintaining all infrastructure physically on-site with no exception",
            "Cloud computing provides no practical advantage over traditional in-house-only computing resources", "Businesses cannot access any computing resource through the cloud"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains a key ethical concern associated with the growing use of AI and machine learning systems?", "options": [
            "AI systems trained on biased data can produce biased or unfair outcomes, raising concerns about fairness and accountability", "AI systems are always completely free of any bias with no possible ethical concern",
            "Ethical concerns are entirely irrelevant to AI or machine learning technology", "AI systems have no impact on any decision that affects people"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'cybersecurity' has become an increasingly critical concern alongside other recent technology trends like IoT and cloud computing?", "options": [
            "The growing number of connected devices and cloud-based systems creates more potential entry points for cyberattacks, requiring stronger protection", "Increased connectivity has no relationship to a system's exposure to cyberattacks",
            "IoT and cloud computing have made cybersecurity entirely unnecessary", "Cybersecurity concerns apply only to isolated, non-networked systems"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a practical application of the 'Internet of Things (IoT)' in daily life?", "options": [
            "A smart home thermostat that adjusts temperature automatically based on sensor data and connects to a mobile app", "A traditional light switch with no sensors or network connectivity of any kind",
            "A concept with no practical, real-world application", "A device that is permanently disconnected from any network or sensor"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall importance of studying recent technology trends within a Computer Science curriculum?", "options": [
            "It helps students understand emerging technologies shaping industry practice and prepares them to engage thoughtfully with ongoing technological change", "Recent technology trends have no relevance to a student's future career or understanding of computer science",
            "This topic is purely speculative with no grounding in real, currently used technology", "Studying recent trends replaces the need to understand any foundational computer science concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
