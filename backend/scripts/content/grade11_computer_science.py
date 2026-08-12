# -*- coding: utf-8 -*-
"""
NEB Grade 11 Management - Computer Science question bank (course 209,
subject 37572, created this session via scripts/link_common_subjects.py's
create_and_link() using course 91's real Computer Science chapter names).

Authored content (not content partner data - loaded with source='synthetic'
via scripts/load_by_chapter_id.py). The original plan was to LINK this
shell to course 91's Computer Science questions (since the chapter names
were copied verbatim from 91), but an audit found that ALL of 91's
Computer Science content is old generic "[SYNTHETIC PLACEHOLDER]" filler
from the original clean_and_fill.py pipeline, not real content partner
content - so linking would have surfaced low-quality placeholder text to
students. That link was created and then reverted (QuestionChapter rows
removed) before this fresh content was authored. This is an introductory
computer/ICT syllabus, distinct from course 210's advanced Programming
in C / OOP / DBMS syllabus - both are legitimate, just pitched at
different depth for their respective real-world course contexts.

Chapter mapping (verified live, chapter names copied from course 91):
  37582 - Introduction of computer
  37581 - Number System and Conversion
  37583 - Computer system and I/O devices
  37580 - Concept of Software
  37578 - C Programming Languages
  37577 - Programming Concept
  37579 - Introduction to Office Package
  37575 - Introduction to Web development
  37576 - Web browsers and search Engines
  37574 - Introduction to Multimedia
  37573 - Digital society and computer ethics

Each entry: {"q": stem, "options": [4 strings], "correct": 0-based index,
"difficulty": "Easy"|"Medium"|"Hard"}. Never presented as content partner
content or as evidence about real students.
"""

QUESTIONS = {
    37582: [  # Introduction of computer
        {"q": "A 'computer' is best defined as an electronic device that:", "options": [
            "Accepts input, processes data according to instructions, and produces output", "Only displays images with no data processing capability",
            "A concept unrelated to processing data", "Only stores electricity with no computational function"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The basic functional units of a computer include:", "options": [
            "Input unit, processing unit (CPU), memory, and output unit", "Only a keyboard, with no other component",
            "A concept unrelated to a computer's basic structure", "Only a monitor, with no processing component"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'Central Processing Unit (CPU)' is often called the 'brain' of the computer because it:", "options": [
            "Carries out instructions and performs calculations/processing", "Only displays visual output with no processing role",
            "A concept unrelated to executing instructions", "Only stores data permanently with no processing capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Input devices' allow a user to:", "options": [
            "Enter data or commands into a computer", "Only display processed results with no data entry capability",
            "A concept unrelated to providing data to a computer", "Only store data permanently with no input function"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is an example of an input device?", "options": [
            "Keyboard", "Monitor", "Printer", "Speaker"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is an example of an output device?", "options": [
            "Monitor", "Keyboard", "Mouse", "Scanner"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Memory' in a computer system is used to:", "options": [
            "Store data and instructions, either temporarily or permanently", "Only display output with no storage capability",
            "A concept unrelated to storing data", "Only convert electrical signals with no storage function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'RAM (Random Access Memory)' is a type of memory that is:", "options": [
            "Volatile, meaning its contents are lost when the computer is powered off", "Permanently retained even after the computer is powered off, identical to a hard disk",
            "A concept unrelated to how memory retains data", "Only used for permanent long-term storage, never for temporary storage"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'ROM (Read-Only Memory)' typically stores:", "options": [
            "Permanent instructions, such as those needed to start up the computer", "Data that changes every second during normal computer use",
            "A concept unrelated to storing startup instructions", "Only user-created documents, never system instructions"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The generation of computers is often classified based on the underlying technology, such as the shift from:", "options": [
            "Vacuum tubes, to transistors, to integrated circuits, to microprocessors", "A single unchanging technology throughout history with no generational shift",
            "A concept unrelated to computing hardware evolution", "Only mechanical gears, with no electronic technology ever introduced"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'personal computer (PC)' is generally designed for:", "options": [
            "Use by a single individual for general-purpose tasks", "Exclusive use by large organisations with thousands of simultaneous users",
            "A concept unrelated to individual computing needs", "Only industrial manufacturing with no general-purpose capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'laptop computer' differs from a desktop computer mainly in its:", "options": [
            "Portability, being designed for easy movement and use in different locations", "Complete inability to perform any computing task",
            "A concept unrelated to a computer's physical design", "Guaranteed lack of any input or output device"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Data' and 'information' differ in that:", "options": [
            "Data refers to raw, unprocessed facts, while information is data that has been processed to be meaningful", "Data and information are always exactly identical concepts",
            "Information always exists before any data is collected", "Data is always more meaningful and useful than information"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Hardware' refers to:", "options": [
            "The physical, tangible components of a computer system", "Only the software programs installed on a computer",
            "A concept unrelated to a computer's physical parts", "Only the electricity powering a computer, with no physical component"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Software' refers to:", "options": [
            "The set of instructions/programs that tell a computer what to do", "Only the physical, tangible components of a computer",
            "A concept unrelated to computer instructions", "Only the computer's power supply unit"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'motherboard' in a computer serves as:", "options": [
            "The main circuit board connecting and allowing communication between key hardware components", "A type of output device with no connective function",
            "A concept unrelated to a computer's internal structure", "Only a decorative panel with no functional role"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'secondary storage device', such as a hard disk, is used to:", "options": [
            "Store data permanently, even when the computer is powered off", "Only store data temporarily while the computer is powered on, identical to RAM",
            "A concept unrelated to long-term data storage", "Process instructions, replacing the role of the CPU"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why computers are considered valuable tools across nearly every modern profession?", "options": [
            "Their ability to process, store, and communicate information efficiently supports a wide range of tasks across different fields", "Computers have no practical use outside of a single, narrow technical profession",
            "Computers can only perform a single fixed task with no broader applicability", "Modern professions have no reliance on computing technology of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the practical difference between RAM and a hard disk for everyday computer use?", "options": [
            "RAM temporarily holds data the CPU is actively using for fast access, while the hard disk stores data permanently for long-term retrieval", "RAM and a hard disk serve exactly the same function with no meaningful difference",
            "A hard disk loses all its data the moment the computer is powered off, exactly like RAM", "RAM is used only for permanent storage, with the hard disk used only temporarily"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of this introductory unit on computers?", "options": [
            "To build foundational understanding of what a computer is, its basic components, and how it processes information", "To provide unrelated trivia with no connection to how computers function",
            "To focus exclusively on a single obsolete computing technology with no broader relevance", "To replace the need for any further study of computer science topics"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37581: [  # Number System and Conversion
        {"q": "The 'decimal number system' (base-10) uses digits ranging from:", "options": [
            "0 to 9", "0 to 1", "0 to 7", "0 to 15"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The 'binary number system' (base-2), fundamental to computing, uses digits limited to:", "options": [
            "0 and 1", "0 to 9", "0 to 7", "A to F"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Computers fundamentally operate using the binary number system mainly because:", "options": [
            "Digital circuits can reliably represent two distinct electrical states (on/off)", "Binary is simply easier for humans to read than decimal",
            "A concept unrelated to how digital electronic circuits function", "Computers cannot process any other number system under any circumstance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'octal number system' uses a base of:", "options": [
            "8", "2", "10", "16"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'hexadecimal number system' uses a base of:", "options": [
            "16", "8", "10", "2"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In hexadecimal notation, the digits A through F represent decimal values:", "options": [
            "10 through 15", "1 through 6", "0 through 5", "16 through 21"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Converting the binary number 1010 to decimal gives:", "options": [
            "10", "8", "12", "5"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Converting the decimal number 9 to binary gives:", "options": [
            "1001", "1010", "1100", "0110"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Each binary digit (0 or 1) is commonly referred to as a:", "options": [
            "Bit", "Byte", "Nibble", "Word"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A group of 8 bits is commonly referred to as a:", "options": [
            "Byte", "Nibble", "Word", "Character"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'nibble' refers to a group of:", "options": [
            "4 bits", "8 bits", "16 bits", "2 bits"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'ASCII (American Standard Code for Information Interchange)' is a coding scheme used to represent:", "options": [
            "Characters (letters, digits, symbols) as numerical codes for computer processing", "Only images, with no relevance to text",
            "A concept unrelated to representing text digitally", "Only audio signals, with no relevance to text characters"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Converting the hexadecimal number 'A' to decimal gives:", "options": [
            "10", "16", "1", "11"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Binary-Coded Decimal (BCD) is a coding method that represents each decimal digit using:", "options": [
            "A separate 4-bit binary code", "A single bit with no further encoding",
            "A concept unrelated to representing decimal digits", "Only hexadecimal notation, never binary"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Understanding number system conversion is important in computer science mainly because it:", "options": [
            "Underlies how data is represented and processed internally by digital computer systems", "Has no practical relevance to how computers function internally",
            "Applies only to advanced theoretical mathematics with no computing relevance", "Is relevant only to designing physical computer casings"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Hexadecimal notation is often used by programmers as a convenient shorthand mainly because:", "options": [
            "Each hexadecimal digit corresponds neatly to exactly 4 binary bits, making conversion straightforward", "Hexadecimal has no relationship to binary representation",
            "Hexadecimal numbers are always identical in value to decimal numbers with no conversion needed", "Computers cannot process hexadecimal values at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why binary is the foundational number system for digital computing, despite being less intuitive for humans than decimal?", "options": [
            "Digital hardware most naturally represents two distinct states (like voltage on/off), making binary a direct match for how circuits operate", "Binary was chosen purely by historical accident with no technical basis",
            "Decimal is actually easier for computer hardware to represent directly than binary", "Binary has no practical advantage over decimal for digital circuits"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the practical value of ASCII encoding for computer systems?", "options": [
            "It provides a standardised way to represent text characters numerically, enabling consistent text processing and exchange across different systems", "ASCII has no practical role in how computers handle text",
            "ASCII is used exclusively for image data, never for text", "Text can be processed by computers with no need for any character encoding scheme"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates why understanding octal and hexadecimal systems remains useful even though computers fundamentally use binary?", "options": [
            "They provide a more compact, human-readable shorthand for binary values, since both convert cleanly to and from binary", "Octal and hexadecimal have no mathematical relationship to binary values",
            "Computers process octal and hexadecimal directly with no underlying binary representation", "These systems are used only in contexts entirely unrelated to computing"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of studying number systems and conversion in an introductory Computer Science course?", "options": [
            "To build foundational understanding of how computers internally represent and process data using binary and related number systems", "Number systems have no relevance to understanding how computers function",
            "This topic is relevant only to advanced computer engineering, not introductory study", "Studying number systems replaces the need to understand any other computing concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37583: [  # Computer system and I/O devices
        {"q": "A 'computer system' broadly consists of:", "options": [
            "Hardware, software, data, and the people who use it, working together", "Only physical hardware with no other component",
            "A concept unrelated to how computing components work together", "Only a single component with no interaction between parts"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'I/O devices' (Input/Output devices) allow a computer system to:", "options": [
            "Receive data from, and send results to, the outside world (including users)", "Only process data internally with no external interaction",
            "A concept unrelated to how a computer interacts with its environment", "Only store data permanently with no interaction capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'scanner' is an input device used to:", "options": [
            "Convert a physical document or image into digital form", "Only print digital documents onto physical paper",
            "A concept unrelated to converting physical documents to digital form", "Only play back audio, with no scanning capability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'printer' is an output device used to:", "options": [
            "Produce a physical, printed copy of digital content", "Only convert physical documents into digital form",
            "A concept unrelated to producing physical output", "Only display content on a screen, with no printing function"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'mouse' is an input device primarily used to:", "options": [
            "Control the position of an on-screen pointer and interact with graphical interface elements", "Only display visual output with no interaction capability",
            "A concept unrelated to interacting with a graphical interface", "Only process instructions, replacing the CPU's role"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'microphone' is an input device that captures:", "options": [
            "Audio/sound and converts it into digital data", "Only visual images, with no relevance to audio",
            "A concept unrelated to capturing sound", "Only text typed by a user, with no audio capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'speaker' is an output device used to:", "options": [
            "Produce audible sound output from a computer system", "Only capture sound, identical to a microphone",
            "A concept unrelated to producing audio output", "Only display visual images, with no audio capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'monitor' (display screen) is classified as a(n):", "options": [
            "Output device", "Input device only, with no output capability", "Storage device only, with no display capability",
            "A device unrelated to displaying computer output"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'touchscreen' is notable among I/O devices because it can function as:", "options": [
            "Both an input device (via touch) and an output device (via display) simultaneously", "Only an output device, with no input capability whatsoever",
            "A concept unrelated to combining input and output functions", "Only an input device, with no display/output capability at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'webcam' is an input device commonly used for:", "options": [
            "Capturing live video, often for video calls or recording", "Only printing physical documents",
            "A concept unrelated to capturing visual/video data", "Only producing audio output"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Ports' on a computer (such as USB ports) serve to:", "options": [
            "Provide physical connection points for attaching external I/O devices", "Only supply electrical power with no data connection capability",
            "A concept unrelated to connecting external devices", "Only display visual output, replacing the monitor's role"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'joystick' is primarily used as an input device for:", "options": [
            "Gaming and simulation control", "Printing physical documents",
            "A concept unrelated to controlling on-screen actions", "Producing audio output exclusively"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'barcode reader', commonly used in retail, functions as an input device that:", "options": [
            "Scans and converts barcode patterns into digital data for a computer system", "Only prints barcodes onto physical labels with no scanning capability",
            "A concept unrelated to reading coded data from physical items", "Only displays visual output, with no data-capture capability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'projector', used to display computer output on a large screen, is classified as a(n):", "options": [
            "Output device", "Input device only, with no display capability", "Storage device, with no display function",
            "A device unrelated to displaying visual content"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The choice of I/O devices for a particular computer system typically depends on:", "options": [
            "The intended use case and the type of interaction required by the user", "A completely random selection process with no relationship to intended use",
            "A concept unrelated to how a system's purpose shapes its hardware", "Only the manufacturer's brand name, with no reference to functionality"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why a touchscreen device is considered both an input and output device?", "options": [
            "It displays visual content (output) while also detecting and responding to a user's physical touch (input) on the same surface", "A touchscreen only ever performs a single function, either input or output, never both",
            "A touchscreen has no relationship to either input or output device categories", "Touchscreens can only display content with no touch-detection capability whatsoever"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why businesses like retail stores commonly use barcode readers as input devices?", "options": [
            "They allow fast, accurate data entry of product information, reducing manual entry errors and speeding up transactions", "Barcode readers provide no practical benefit over manually typing every product's information",
            "Barcode readers are used exclusively for printing, not for reading any data", "Retail businesses have no practical use for input devices of any kind"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the difference between an input device and an output device using a real classroom scenario?", "options": [
            "A student using a microphone to record their voice (input) and a speaker to play it back (output)", "A keyboard functioning identically to a speaker, with no functional distinction",
            "A monitor being used exclusively to type in new data with no ability to display anything", "A scenario where no distinction exists between input and output devices"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why selecting appropriate I/O devices matters for a computer system's intended use, such as a system used for video conferencing versus one used for document printing?", "options": [
            "Different tasks require different I/O capabilities (e.g. webcam/microphone for conferencing, a printer for hard-copy documents) to function effectively", "Every computer system requires an absolutely identical set of I/O devices regardless of its intended use",
            "I/O device selection has no bearing on how well a system supports its intended task", "A single I/O device can always perform every possible input and output function equally well"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall role of I/O devices within a complete computer system?", "options": [
            "They enable the computer to interact with the external world by receiving data and delivering processed results to users", "I/O devices play no meaningful role in how a computer system functions",
            "I/O devices are relevant only to specialised industrial computing, not general use", "A computer system can function fully without any input or output device"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37580: [  # Concept of Software
        {"q": "'Software' refers to:", "options": [
            "A set of instructions (programs) that direct a computer's hardware to perform specific tasks", "Only the physical, tangible components of a computer",
            "A concept unrelated to instructing computer hardware", "Only the electrical power supplied to a computer"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'System software' is software designed primarily to:", "options": [
            "Manage and control a computer's hardware and provide a platform for other software to run", "Only allow users to create documents, with no relation to managing hardware",
            "A concept unrelated to managing a computer's underlying operations", "Only play multimedia files, with no system management role"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'Operating System (OS)', an example of system software, is responsible for:", "options": [
            "Managing hardware resources and providing a platform for running application programs", "Only displaying decorative wallpaper images with no functional role",
            "A concept unrelated to managing a computer's resources", "Only connecting a computer to the internet, with no other function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Application software' is designed primarily to:", "options": [
            "Help users perform specific tasks, such as word processing or spreadsheet calculations", "Only manage a computer's internal hardware resources, identical to an operating system",
            "A concept unrelated to performing user-facing tasks", "Only control a computer's power supply"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following is an example of application software?", "options": [
            "A word processor (e.g. Microsoft Word)", "The operating system's kernel", "A device driver", "The computer's BIOS"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'device driver' is a type of system software that:", "options": [
            "Allows the operating system to communicate with a specific hardware device", "Only allows users to create text documents, with no relation to hardware",
            "A concept unrelated to hardware-software communication", "Only manages a company's financial accounts"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Utility software' typically performs tasks such as:", "options": [
            "Disk cleanup, antivirus protection, or file compression", "Only word processing, identical to typical application software",
            "A concept unrelated to maintaining or optimising a computer system", "Only playing video games, with no maintenance function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Proprietary software' refers to software that is:", "options": [
            "Owned and controlled by a company or individual, typically with restrictions on use, modification, or distribution", "Freely available for anyone to modify and redistribute with no restriction",
            "A concept unrelated to software ownership or licensing", "Always provided completely free of charge with no licensing terms"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Open-source software' refers to software whose:", "options": [
            "Source code is made publicly available, allowing users to view, modify, and often redistribute it", "Source code is always kept entirely secret with no public access",
            "A concept unrelated to how source code is shared", "Use is restricted exclusively to the original author, with no distribution allowed"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Freeware' refers to software that is:", "options": [
            "Available to use at no monetary cost, though not necessarily open-source", "Always open-source, with the two terms being identical",
            "A concept unrelated to a software's cost or price", "Always more expensive than proprietary software"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'compiler', a type of system software, is used to:", "options": [
            "Translate source code written in a programming language into machine code", "Only display images on screen, with no relation to code translation",
            "A concept unrelated to converting programming code", "Only print documents, with no software translation role"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Software 'installation' refers to the process of:", "options": [
            "Setting up a program on a computer system so it can be used", "Permanently and completely deleting a program from a computer",
            "A concept unrelated to preparing software for use", "Only updating an already-installed program, with no initial setup involved"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Software updates' are typically released to:", "options": [
            "Fix bugs, improve performance, or add new features to existing software", "Deliberately introduce new errors into previously working software",
            "A concept unrelated to maintaining or improving software over time", "Only change a program's name, with no functional improvement"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'firmware' is a specific type of software that is:", "options": [
            "Embedded directly into a hardware device to control its basic functions", "Only used for word processing, with no relation to hardware control",
            "A concept unrelated to controlling hardware operations", "Only found in application software, never in hardware devices"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "The relationship between system software and application software can be described as:", "options": [
            "System software manages the underlying hardware, providing a foundation on which application software runs", "System software and application software perform exactly identical functions with no distinction",
            "Application software manages hardware directly, with no need for system software", "A concept unrelated to how different software categories interact"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why an operating system is considered essential for a computer to function usefully?", "options": [
            "It manages hardware resources and provides the platform that allows application software to run and interact with the user", "An operating system serves no functional purpose and could be removed with no effect on the computer",
            "Application software can run directly on hardware with no need for any operating system", "An operating system's only role is to display a decorative background image"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the key difference between proprietary and open-source software licensing models?", "options": [
            "Proprietary software restricts access to and modification of its source code, while open-source software makes its source code publicly available for viewing and modification", "Proprietary and open-source software are always identical in terms of licensing restrictions",
            "Open-source software is always more expensive to obtain than proprietary software", "Proprietary software is always distributed completely free of charge, identical to freeware"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates why regular software updates are important for maintaining a secure and well-functioning computer system?", "options": [
            "Updates often patch security vulnerabilities and fix bugs that could otherwise be exploited or cause malfunctions", "Software updates never provide any benefit and should always be avoided",
            "Updates always introduce more problems than they solve, with no benefit whatsoever", "A concept with no relevance to a computer system's security or performance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best distinguishes a compiler's role from that of typical application software like a word processor?", "options": [
            "A compiler translates programming code into a form the computer can execute, while a word processor helps users create and edit documents", "A compiler and a word processor perform exactly the same underlying function",
            "A compiler is used only to display documents, identical to a word processor", "A word processor is responsible for translating source code, not the compiler"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of studying the concept of software within an introductory Computer Science course?", "options": [
            "To build foundational understanding of the different categories of software and how they enable a computer system to function and be used", "Software concepts have no relevance to understanding how computers are actually used",
            "This topic is relevant only to professional software developers, not general students", "Studying software concepts replaces the need to understand computer hardware at all"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37578: [  # C Programming Languages
        {"q": "'C' is a widely used programming language often described as a:", "options": [
            "General-purpose, procedural programming language", "A language used exclusively for designing website visual layouts, with no general programming capability",
            "A concept unrelated to writing computer instructions", "A purely graphical, non-textual programming tool"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Every C program must contain at least one function named:", "options": [
            "main()", "start()", "run()", "execute()"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, a 'variable' is used to:", "options": [
            "Store a value that can be used and modified during program execution", "Only display fixed text with no ability to store or change any value",
            "A concept unrelated to storing data during a program's execution", "Only represent a mathematical constant that can never be assigned a value"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, 'int' is a data type used to declare variables that store:", "options": [
            "Whole numbers (integers)", "Only single characters", "Only decimal/floating-point numbers", "Only true/false values"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, 'float' is a data type used to declare variables that store:", "options": [
            "Decimal (floating-point) numbers", "Only whole numbers with no decimal component", "Only single characters",
            "Only text strings"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, 'char' is a data type used to declare variables that store:", "options": [
            "A single character", "An entire paragraph of text with no character limit", "Only whole numbers",
            "Only decimal numbers"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The printf() function in C is primarily used to:", "options": [
            "Display output to the screen", "Accept input from the user, identical to scanf()",
            "A concept unrelated to displaying program output", "Only perform mathematical calculations with no output capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "The scanf() function in C is primarily used to:", "options": [
            "Accept input from the user", "Display output to the screen, identical to printf()",
            "A concept unrelated to receiving user input", "Only perform file operations with no input capability"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In C, an 'if statement' allows a program to:", "options": [
            "Execute a block of code conditionally, based on whether a specified condition is true", "Always execute every block of code regardless of any condition",
            "A concept unrelated to conditional execution", "Only define a new variable, with no conditional execution capability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'for loop' in C is commonly used when a programmer needs to:", "options": [
            "Repeat a block of code a specific, known number of times", "Prevent any block of code from ever executing",
            "A concept unrelated to repeating code", "Only define a function, with no looping capability"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In C, the ';' (semicolon) character is used to:", "options": [
            "Terminate a statement", "Begin a new function definition, identical to the keyword 'int'",
            "A concept unrelated to structuring C code", "Add a comment to the code, with no other purpose"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Comments' in a C program, marked with // or /* */, are used to:", "options": [
            "Add explanatory notes to the code that are ignored by the compiler when the program runs", "Add executable instructions that the compiler actively runs as part of the program",
            "A concept unrelated to documenting code for readability", "Only display error messages to the user"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "An 'operator' in C, such as '+' or '-', is used to:", "options": [
            "Perform an operation (e.g. arithmetic) on one or more values", "Only define a new data type, with no operation performed",
            "A concept unrelated to performing calculations or operations", "Only terminate a program, with no operational purpose"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In C, 'void' is commonly used to indicate that a function:", "options": [
            "Does not return any value", "Always returns an integer value, with no exception",
            "A concept unrelated to a function's return behaviour", "Can only be called a single time throughout the entire program"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'syntax error' in a C program refers to:", "options": [
            "A violation of the language's grammatical rules, preventing successful compilation", "A logically correct program that nonetheless produces an unexpected result",
            "A concept unrelated to how code is structured according to language rules", "An error that occurs only after a program has successfully run, never before"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why C is often taught as a foundational programming language in introductory computer science education?", "options": [
            "Its relatively simple, structured syntax helps build core programming concepts (variables, control flow, functions) that transfer to many other languages", "C has no relevance to understanding fundamental programming concepts",
            "C is used exclusively for a single, narrow application with no broader educational value", "Learning C provides no transferable understanding applicable to other programming languages"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the difference in purpose between printf() and scanf() in a C program?", "options": [
            "printf() sends output to the screen for the user to see, while scanf() reads input provided by the user", "printf() and scanf() perform exactly the same function with no meaningful distinction",
            "scanf() is used only to display output, identical to printf()", "printf() is used only to accept input, identical to scanf()"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best illustrates why choosing the correct data type (e.g. int vs float) matters when writing a C program?", "options": [
            "Using the wrong data type (e.g. int instead of float) can lead to loss of precision or incorrect results, such as truncating decimal values", "Data type choice has no effect whatsoever on how a program stores or processes a value",
            "Every data type in C stores and processes values in an identical way with no distinction", "Choosing a data type only affects how a program looks visually, not its actual behaviour"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'comments' are considered good programming practice, even though they don't affect a program's execution?", "options": [
            "They improve code readability and help other programmers (or the original author later) understand the code's purpose and logic", "Comments always change a program's actual behaviour when it runs",
            "Comments have no practical benefit for anyone reading or maintaining the code", "Comments are required by the C compiler in order for a program to run at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of introducing students to the C programming language in this course?", "options": [
            "To build foundational programming skills and logical thinking applicable broadly across computing tasks", "C programming has no practical relevance to a Management-stream student's broader computer literacy",
            "This topic is relevant only to advanced software engineers, not introductory learners", "Learning C replaces the need to understand any other computer science concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37577: [  # Programming Concept
        {"q": "A 'program', in computing terms, refers to:", "options": [
            "A set of step-by-step instructions written to perform a specific task", "A single, isolated hardware component with no instructions involved",
            "A concept unrelated to giving a computer a task to perform", "Only a decorative graphic displayed on screen"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Programming' is the process of:", "options": [
            "Writing instructions (code) that a computer can execute to perform a task", "Only physically assembling computer hardware components",
            "A concept unrelated to writing computer instructions", "Only browsing the internet, with no code creation involved"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "An 'algorithm' refers to:", "options": [
            "A step-by-step procedure or set of rules for solving a problem", "A single, unstructured line of code with no defined steps",
            "A concept unrelated to solving problems systematically", "Only a type of computer hardware component"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'flowchart' is a diagrammatic representation used to:", "options": [
            "Visually represent the steps and logic of an algorithm or process", "Only display a program's final output text with no reference to logic or steps",
            "A concept unrelated to representing program logic visually", "Only list a program's variable names, with no logical structure shown"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Pseudocode' refers to:", "options": [
            "An informal, high-level description of a program's logic, written in plain language rather than strict programming syntax", "Actual, fully executable code written in a specific programming language",
            "A concept unrelated to describing program logic", "Only a type of computer hardware error message"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Sequence', one of the three fundamental programming control structures, refers to:", "options": [
            "Executing instructions one after another, in the order they are written", "Repeating a set of instructions indefinitely with no termination",
            "A concept unrelated to how instructions are ordered and executed", "Executing instructions only if a specific condition is true"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Selection' (decision-making), another fundamental control structure, refers to:", "options": [
            "Choosing between different paths of execution based on a condition", "Executing every instruction in strict sequential order with no branching",
            "A concept unrelated to conditional branching in a program", "Repeating a set of instructions a fixed number of times, with no branching"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Iteration' (looping), the third fundamental control structure, refers to:", "options": [
            "Repeating a set of instructions multiple times, often until a condition is met", "Executing an instruction exactly once, with no possibility of repetition",
            "A concept unrelated to repeating code", "Only choosing between two alternative paths, with no repetition involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Debugging' refers to the process of:", "options": [
            "Identifying and fixing errors in a program's code", "Deliberately introducing new errors into a working program",
            "A concept unrelated to correcting problems in code", "Only compiling a program, with no error correction involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'logical error' in a program refers to a mistake where the program:", "options": [
            "Runs without crashing but produces an incorrect result due to flawed logic", "Fails to compile at all due to a grammatical/syntax mistake",
            "A concept unrelated to a program's actual runtime behaviour", "Always crashes immediately with no output whatsoever"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'variable' in programming serves to:", "options": [
            "Hold a value that can change during a program's execution", "Only represent a value that can never be modified once set",
            "A concept unrelated to storing changeable data during execution", "Only display a program's final output text"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'constant' in programming, unlike a variable, is a value that:", "options": [
            "Remains fixed and unchanged throughout a program's execution", "Constantly changes with every single line of code executed",
            "A concept unrelated to fixed, unchanging values", "Only exists temporarily and is deleted after each use"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Top-down design', a programming approach, involves:", "options": [
            "Breaking a complex problem into smaller, more manageable sub-problems", "Writing an entire program's code in a single, unbroken block with no sub-division",
            "A concept unrelated to structuring how a program is designed", "Beginning coding without any prior planning of the problem's structure"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A 'compiler' translates source code into machine code, while an 'interpreter' typically:", "options": [
            "Executes source code line-by-line, translating and running each line without producing a separate compiled file", "Performs exactly the same process as a compiler with no meaningful difference",
            "A concept unrelated to how programming languages are executed", "Only displays a program's output, with no translation of code involved"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Program testing', a key step in software development, aims to:", "options": [
            "Verify that a program behaves correctly and produces expected results", "Guarantee a program is entirely free of any possible defect with no verification needed",
            "A concept unrelated to checking a program's correctness", "Only occur before any code has actually been written"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why algorithms are typically designed and reviewed (e.g. via flowcharts or pseudocode) before actual code is written?", "options": [
            "Planning the logic first helps catch errors in the approach early, before investing time in writing and debugging actual code", "Planning has no benefit and always wastes time compared to writing code immediately",
            "Algorithms and code writing are always done in exactly the same step with no separation", "Flowcharts and pseudocode are only used after a program has already been fully written and tested"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the relationship between the three fundamental control structures (sequence, selection, iteration)?", "options": [
            "Together they provide the essential building blocks for expressing any program's logic, regardless of programming language", "The three structures are entirely unrelated to each other with no combined purpose",
            "Only one of the three structures is ever actually needed to write any program", "These structures apply only to a single specific programming language, not universally"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the difference between a 'syntax error' and a 'logical error' in a program?", "options": [
            "A syntax error prevents the program from compiling at all, while a logical error allows the program to run but produce an incorrect result", "Syntax errors and logical errors are always exactly identical with no meaningful distinction",
            "A logical error always prevents a program from compiling, identical to a syntax error", "A syntax error only ever occurs after a program has successfully executed"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'top-down design' (breaking a problem into smaller sub-problems) is a valuable programming practice for larger projects?", "options": [
            "It makes complex problems more manageable by allowing each smaller part to be designed, coded, and tested somewhat independently", "Breaking a problem into smaller parts always makes a project significantly harder to manage",
            "Top-down design has no practical benefit for programming projects of any size", "This approach applies only to very small, trivial programs with no benefit for larger ones"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of studying fundamental programming concepts (algorithms, control structures, debugging) in this course?", "options": [
            "To build the foundational logical thinking and problem-solving skills that underlie writing and understanding any computer program", "Programming concepts have no relevance to understanding how software is actually built",
            "This topic is relevant only to students planning a career exclusively in software development", "Studying programming concepts replaces the need to learn any specific programming language"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37579: [  # Introduction to Office Package
        {"q": "An 'office package' (office suite) typically bundles together applications for tasks such as:", "options": [
            "Word processing, spreadsheets, and presentations", "Only playing video games, with no productivity application included",
            "A concept unrelated to everyday productivity tasks", "Only editing photographs, with no document or spreadsheet application"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'word processor', such as Microsoft Word, is primarily used to:", "options": [
            "Create, edit, and format text documents", "Only perform numerical calculations, identical to a spreadsheet program",
            "A concept unrelated to creating written documents", "Only play audio/video files"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'spreadsheet' application, such as Microsoft Excel, is primarily used for:", "options": [
            "Organising data in rows/columns and performing calculations", "Only creating text documents, identical to a word processor",
            "A concept unrelated to organising or calculating numerical data", "Only designing website layouts"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'presentation' application, such as Microsoft PowerPoint, is primarily used to:", "options": [
            "Create slideshows for presenting information visually to an audience", "Only perform complex numerical calculations, identical to a spreadsheet",
            "A concept unrelated to presenting information to an audience", "Only manage a database's internal storage"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "In a spreadsheet, a 'cell' refers to:", "options": [
            "The intersection of a row and a column, used to store a single piece of data", "An entire spreadsheet file, with no reference to a specific row/column intersection",
            "A concept unrelated to how data is organised in a spreadsheet", "Only a formula, with no relation to a specific data location"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A spreadsheet 'formula' allows a user to:", "options": [
            "Perform automatic calculations based on the values in specified cells", "Only format text with bold or italic styling, with no calculation capability",
            "A concept unrelated to performing calculations within a spreadsheet", "Only insert an image into a document"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The SUM function in a spreadsheet is used to:", "options": [
            "Add together the values in a specified range of cells", "Only display the largest value in a range, with no addition performed",
            "A concept unrelated to performing arithmetic on cell values", "Only sort a range of cells alphabetically"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In a word processor, 'formatting' options (such as bold, italics, font size) allow a user to:", "options": [
            "Adjust the visual appearance of text within a document", "Only perform numerical calculations, with no visual adjustment capability",
            "A concept unrelated to adjusting a document's visual presentation", "Only save a document in a different file format"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Mail merge', a word processing feature, allows a user to:", "options": [
            "Automatically generate multiple personalised documents (e.g. letters) from a single template and a data source", "Only send a single, identical email with no personalisation capability",
            "A concept unrelated to generating personalised documents", "Only format a spreadsheet's numerical values"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "In a presentation application, a 'slide transition' refers to:", "options": [
            "A visual effect applied when moving from one slide to the next", "A concept unrelated to how slides are displayed in sequence",
            "Only the text content typed onto a single slide", "Only a spreadsheet formula used within a presentation file"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A spreadsheet 'chart' or 'graph' is used to:", "options": [
            "Visually represent numerical data for easier interpretation", "Only store raw numerical data with no visual representation",
            "A concept unrelated to visualising data", "Only format text within a word processing document"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Saving a document in 'PDF' format is often preferred when sharing a finished document because PDF:", "options": [
            "Preserves consistent formatting and appearance across different devices and software", "Always allows the recipient to freely edit every part of the document with no restriction",
            "A concept unrelated to preserving a document's appearance when shared", "Can only be opened using a spreadsheet application, never a document viewer"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Templates' in office applications provide users with:", "options": [
            "A pre-designed starting structure/format that can be customised for a specific document, spreadsheet, or presentation", "A concept unrelated to speeding up document creation",
            "Only a blank, entirely unformatted file with no pre-designed structure", "Only a printed, non-digital reference sheet"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Using absolute cell references (e.g. $A$1) in a spreadsheet formula, as opposed to relative references, ensures that:", "options": [
            "The referenced cell does not change when the formula is copied to other cells", "The referenced cell always changes unpredictably every time the formula is copied",
            "A concept unrelated to how references behave when a formula is copied", "The formula can no longer perform any calculation at all"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Collaborative editing', a feature in modern office packages, allows:", "options": [
            "Multiple users to work on the same document simultaneously, often via cloud-based tools", "Only a single user to ever access a document, with no possibility of shared editing",
            "A concept unrelated to enabling teamwork on shared documents", "Only printing a document, with no editing capability of any kind"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why office package proficiency is considered a valuable general workplace skill, including for Management-stream students?", "options": [
            "Word processing, spreadsheet, and presentation skills are widely used across nearly all professional and administrative tasks", "Office package skills have no practical relevance to any workplace task",
            "These skills are relevant only to specialised computer science professionals, not general business tasks", "Office packages are used exclusively for personal entertainment, with no professional application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains the practical benefit of using spreadsheet formulas rather than manually calculating and typing in values?", "options": [
            "Formulas automatically recalculate when underlying data changes, reducing manual effort and the risk of calculation errors", "Formulas provide no benefit over manually recalculating and retyping every value by hand",
            "Formulas can only be used once and must be manually reset for every new calculation", "Manual calculation is always faster and more accurate than using a spreadsheet formula"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a practical business use of 'mail merge'?", "options": [
            "Generating personalised invitation letters for hundreds of clients from a single template and a client list", "Sending the exact same unpersonalised message to a single recipient with no data source involved",
            "A feature with no practical business application", "Formatting a single spreadsheet's numerical values with no letter-writing involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why choosing to save a finished document as a PDF (rather than an editable file format) is often recommended before sharing it externally?", "options": [
            "It helps ensure the document's formatting and appearance remain consistent and are not accidentally altered by the recipient", "PDF format always makes a document significantly larger with no other benefit",
            "PDF format has no practical advantage over any other file format when sharing documents", "Saving as PDF prevents the document from ever being viewed by anyone"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall value of learning an office package within an introductory Computer Science course for Management students?", "options": [
            "It builds practical digital literacy directly applicable to common workplace document, data, and presentation tasks", "Office package skills have no connection to real workplace needs",
            "This topic is relevant only to dedicated IT professionals, not Management-stream students", "Learning an office package replaces the need to understand any other computing concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37575: [  # Introduction to Web development
        {"q": "'Web development' broadly refers to the process of:", "options": [
            "Building and maintaining websites and web applications", "Only manufacturing physical computer hardware",
            "A concept unrelated to creating web-based content", "Only managing a company's internal accounting records"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'HTML' is a fundamental language used in web development primarily to:", "options": [
            "Define the structure and content of a web page", "Only style the visual appearance of a web page, with no structural role",
            "A concept unrelated to building web page content", "Only add interactivity, with no structural role"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'CSS' is used in web development primarily to:", "options": [
            "Style and visually format a web page's appearance", "Only define a webpage's raw text content, with no styling capability",
            "A concept unrelated to a webpage's visual presentation", "Only manage a website's database"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'web browser' (e.g. Chrome, Firefox) is software used to:", "options": [
            "Access and display web pages and websites", "Only write website code, with no display capability",
            "A concept unrelated to viewing web content", "Only manage a computer's local files, with no internet connectivity"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'web page' is best described as:", "options": [
            "A single document accessible via a web browser, typically part of a larger website", "An entire physical computer, with no relation to a browsable document",
            "A concept unrelated to viewable online content", "Only a printed document with no digital or online form"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'website' refers to:", "options": [
            "A collection of related web pages, typically hosted under a single domain", "A single isolated web page with no relationship to any other page",
            "A concept unrelated to organising multiple web pages together", "Only a single image file, with no textual content"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Frontend web development' focuses primarily on:", "options": [
            "The parts of a website users directly see and interact with in their browser", "Only the server-side database, with no visible user interface",
            "A concept unrelated to what users see and interact with", "Only a company's internal accounting software"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Backend web development' focuses primarily on:", "options": [
            "Server-side logic, databases, and behind-the-scenes functionality that supports a website", "Only the visual design elements a user directly sees, identical to frontend development",
            "A concept unrelated to server-side website functionality", "Only a webpage's font choice, with no server-side logic involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'hyperlink' on a web page allows a user to:", "options": [
            "Navigate to another web page or resource by clicking on it", "Only change a webpage's background colour with no navigation capability",
            "A concept unrelated to navigating between web pages", "Only print the current web page"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'web server' is responsible for:", "options": [
            "Storing website files and delivering them to a user's browser upon request", "Only displaying a website's content locally with no request/response interaction",
            "A concept unrelated to hosting and delivering website content", "Only managing a company's physical office space"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'URL (Uniform Resource Locator)' serves to:", "options": [
            "Specify the address of a specific resource (e.g. a web page) on the internet", "Only encrypt data transmitted between a browser and server, with no addressing role",
            "A concept unrelated to locating web resources", "Only refer to a computer's internal file storage path, with no online relevance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'text editor' or 'code editor' used in web development allows a developer to:", "options": [
            "Write and edit the HTML/CSS/other code that makes up a website", "Only view finished websites, with no code-writing capability",
            "A concept unrelated to creating website code", "Only manage a computer's power settings"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Responsive web design' aims to ensure a website:", "options": [
            "Displays and functions well across a range of different screen sizes and devices", "Functions correctly only on a single, specific screen size with no adaptability",
            "A concept unrelated to how a website adapts across devices", "Cannot be accessed from a mobile phone under any circumstance"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A basic HTML document typically begins with a declaration such as:", "options": [
            "<!DOCTYPE html>", "<start>", "<begin_html>", "#include <html>"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "In HTML, tags such as `<p>` and `</p>` are used to:", "options": [
            "Define a paragraph element, with the opening and closing tag marking its start and end", "Only define a hyperlink, with no relation to paragraph text",
            "A concept unrelated to structuring text content on a webpage", "Only apply colour styling, with no structural role"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why HTML and CSS are typically taught together as complementary skills in introductory web development?", "options": [
            "HTML provides the structural content of a page, while CSS controls its visual styling - together they build a complete, well-presented web page", "HTML and CSS perform exactly the same function with no meaningful distinction",
            "CSS is responsible for structuring content, while HTML handles all visual styling", "Learning only one of the two languages is always sufficient to build any complete webpage"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the difference between frontend and backend web development?", "options": [
            "Frontend development focuses on the user-facing interface, while backend development handles server-side logic and data management behind the scenes", "Frontend and backend development are always performed by exactly the same code with no distinction",
            "Backend development is responsible only for a website's visual design, identical to frontend development", "Frontend development handles server-side databases exclusively, with no visible interface role"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates why 'responsive web design' has become increasingly important for websites built today?", "options": [
            "Users access websites from many different devices with varying screen sizes, so responsive design helps ensure a usable experience across all of them", "All users view websites using an identical screen size, making responsive design unnecessary",
            "Responsive design has no bearing on how usable a website is on different devices", "Responsive design is relevant only for websites accessed exclusively on desktop computers"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the practical role of a URL in navigating the web?", "options": [
            "It provides a specific, structured address that tells a browser exactly which resource to request and display", "A URL has no functional role in how a browser locates or displays web content",
            "URLs are used exclusively for internal file storage, with no connection to the internet", "Every website shares an identical URL with no unique addressing"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall purpose of this introductory unit on web development?", "options": [
            "To build foundational understanding of how websites are structured, styled, and made accessible via the web", "Web development concepts have no relevance to understanding how the modern internet functions",
            "This topic is relevant only to professional web developers, not introductory students", "Studying web development replaces the need to understand any other computer science topic"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37576: [  # Web browsers and search Engines
        {"q": "A 'web browser' is software that allows a user to:", "options": [
            "Access, view, and interact with websites and web content", "Only write website code, with no capability to display web content",
            "A concept unrelated to viewing online content", "Only manage a computer's local files with no internet access"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is an example of a widely used web browser?", "options": [
            "Google Chrome", "Microsoft Excel", "Adobe Photoshop", "Windows Media Player"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'search engine' is a tool designed to:", "options": [
            "Help users find relevant information or web pages based on a search query", "Only display a single, fixed web page with no search capability",
            "A concept unrelated to finding information online", "Only manage a computer's local hardware settings"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "Which of the following is an example of a widely used search engine?", "options": [
            "Google", "Microsoft Word", "Adobe Reader", "VLC Media Player"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A browser's 'bookmark' (or favourite) feature allows a user to:", "options": [
            "Save a web page's address for quick access later", "Only permanently delete a web page from the internet",
            "A concept unrelated to saving frequently visited pages", "Only change a webpage's text colour"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A browser's 'history' feature keeps a record of:", "options": [
            "Previously visited web pages", "Only bookmarked pages, with no record of general browsing",
            "A concept unrelated to tracking previously visited pages", "Only a user's saved passwords, with no relation to visited pages"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Private/incognito browsing mode' in a browser is designed to:", "options": [
            "Avoid saving browsing history, cookies, and site data locally after the session ends", "Guarantee complete anonymity from every website and network visible to that browsing session",
            "A concept unrelated to how browsing data is saved locally", "Permanently block access to every website with no exception"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A search engine's 'search results ranking' is typically determined by factors such as:", "options": [
            "Relevance to the search query and the perceived quality/authority of a page", "A purely random selection process with no reference to relevance or quality",
            "A concept unrelated to how search results are ordered", "Only the exact alphabetical order of website names"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Search engine optimisation (SEO)' refers to techniques used to:", "options": [
            "Improve a website's visibility and ranking in search engine results", "Deliberately reduce a website's visibility in search engine results",
            "A concept unrelated to a website's search ranking", "Only change a website's server hosting location"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A browser 'extension' or 'add-on' is used to:", "options": [
            "Add extra features or functionality to a web browser", "Only permanently disable a browser's core functionality",
            "A concept unrelated to customising a browser's capabilities", "Only change a computer's operating system entirely"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cookies', small files stored by websites in a browser, are commonly used to:", "options": [
            "Remember user preferences and session information across visits to a website", "Physically damage a user's computer hardware",
            "A concept unrelated to remembering website-related information", "Only display advertisements with no other function"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Using specific, well-chosen 'keywords' in a search query helps to:", "options": [
            "Narrow search results toward more relevant, useful information", "Guarantee that only false or incorrect information will ever appear",
            "A concept unrelated to the relevance of search results", "Prevent any search results from appearing at all"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Evaluating a search result's 'credibility' before relying on it involves checking factors such as:", "options": [
            "The source's authority, the author's expertise, and supporting evidence", "Only the visual design of the resulting webpage",
            "A concept unrelated to assessing the trustworthiness of information", "Only the length of the webpage's URL"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "A browser's 'tabs' feature allows a user to:", "options": [
            "Open and switch between multiple web pages within a single browser window", "Only view a single web page at a time, with no ability to open additional pages",
            "A concept unrelated to managing multiple open web pages", "Only save a webpage permanently to the computer's hard disk"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "A 'pop-up blocker', a common browser feature, is used to:", "options": [
            "Prevent unwanted pop-up windows/advertisements from automatically appearing while browsing", "Guarantee every advertisement will always be displayed with no blocking capability",
            "A concept unrelated to controlling unwanted browser content", "Only block a user's own bookmarked pages from loading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why evaluating the credibility of search results matters, given that a search engine returns many possible sources?", "options": [
            "Not every indexed web page is accurate or reliable, so critically assessing sources helps avoid relying on misleading or false information", "Every result returned by a search engine is guaranteed to be completely accurate with no need for evaluation",
            "Search engines only ever return a single, always-correct result with no other option", "Evaluating credibility has no practical relevance to using search engines effectively"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains the practical benefit of using well-chosen keywords rather than a vague, general query when searching?", "options": [
            "Specific, relevant keywords help the search engine return more targeted, useful results rather than overly broad ones", "Keyword choice has no effect whatsoever on the relevance of search results returned",
            "Vague queries always return more useful results than specific, well-chosen keywords", "Search engines ignore search query wording entirely and return identical results regardless"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'private/incognito browsing mode' does not guarantee complete anonymity online?", "options": [
            "While it avoids saving local browsing data, a user's activity can still potentially be visible to the website visited, the network, or the internet service provider", "Private browsing mode guarantees complete anonymity from absolutely every party under all circumstances",
            "Private browsing mode has no relationship to how browsing data is saved or visible", "Private browsing mode blocks all internet access entirely, preventing any browsing activity"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a responsible use of browser 'cookies' from a website's perspective?", "options": [
            "Using cookies to remember a user's login session so they don't need to re-enter their password on every page", "Using cookies to physically damage a visitor's computer hardware",
            "A use case with no practical, legitimate application for cookies", "Cookies being used exclusively to block a website's own content from loading"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall importance of understanding how web browsers and search engines work within a general computer literacy course?", "options": [
            "It equips students with practical skills for efficiently and safely finding and accessing information online, a core part of everyday digital life", "Understanding browsers and search engines has no practical relevance to everyday computer use",
            "This topic is relevant only to professional web developers, never to general users", "Studying this topic replaces the need to understand any other computer science concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37574: [  # Introduction to Multimedia
        {"q": "'Multimedia' refers to content that combines multiple forms of media, such as:", "options": [
            "Text, images, audio, video, and animation", "Only plain, unformatted text with no other media type",
            "A concept unrelated to combining different media formats", "Only a single static image with no other content type"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Digital image' formats, such as JPEG and PNG, are used to:", "options": [
            "Store and represent visual images in a digital, computer-readable form", "Only store audio content, with no relevance to visual images",
            "A concept unrelated to representing visual content digitally", "Only store spreadsheet numerical data"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Audio' files, in formats such as MP3, are used to store:", "options": [
            "Sound content in a digital, computer-readable format", "Only visual image content, with no relevance to sound",
            "A concept unrelated to representing sound digitally", "Only text documents"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Video' files, such as MP4 format, typically combine:", "options": [
            "A sequence of moving images with accompanying audio", "Only static, unmoving images with no sequence involved",
            "A concept unrelated to representing moving visual/audio content", "Only spreadsheet numerical data, with no visual or audio component"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Animation' refers to the technique of:", "options": [
            "Creating an illusion of movement by displaying a rapid sequence of images", "Only displaying a single, completely static image with no illusion of movement",
            "A concept unrelated to creating a sense of visual movement", "Only recording live-action video footage, with no illusion of movement created"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Image compression' is used to:", "options": [
            "Reduce an image file's size while attempting to preserve acceptable visual quality", "Deliberately increase an image's file size with no other purpose",
            "A concept unrelated to managing digital image file size", "Only convert an image into audio format"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Lossy compression', a type of file compression, results in:", "options": [
            "Some loss of original data/quality in exchange for a significantly smaller file size", "No loss of any original data or quality whatsoever, identical to lossless compression",
            "A concept unrelated to trading off quality for smaller file size", "An increase in the file's original quality with no reduction in size"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Lossless compression', in contrast to lossy compression, preserves:", "options": [
            "All of the original data with no loss in quality, though typically with less size reduction", "None of the original data, resulting in significant loss of quality",
            "A concept unrelated to how compression affects data quality", "Only audio data, with no application to images or video"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Resolution', in the context of digital images, refers to:", "options": [
            "The amount of detail an image holds, often measured in pixels", "A measure of an image's file format only, with no relation to detail",
            "A concept unrelated to an image's level of visual detail", "Only the colour of an image, with no relation to detail level"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Multimedia software', such as video editors, allows users to:", "options": [
            "Create, edit, and combine multimedia elements such as video, audio, and images", "Only perform spreadsheet calculations, with no multimedia editing capability",
            "A concept unrelated to producing or editing multimedia content", "Only manage a computer's internal hardware settings"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Multimedia content is widely used in fields such as education and marketing mainly because it:", "options": [
            "Can engage audiences more effectively than text alone by combining multiple sensory formats", "Has no practical benefit over plain text in any context",
            "A concept unrelated to how content engages or informs an audience", "Always makes information significantly harder to understand than plain text alone"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Streaming', as used for online video/audio content, refers to:", "options": [
            "Delivering multimedia content continuously over the internet without requiring a full download before playback", "Requiring a user to fully download an entire file before any playback can begin, with no continuous delivery",
            "A concept unrelated to delivering multimedia content over the internet", "Only applicable to text documents, with no relevance to audio or video"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Frame rate', relevant to video and animation, refers to:", "options": [
            "The number of individual images (frames) displayed per second", "A measure of an image's file size only, with no relation to displayed frames",
            "A concept unrelated to how smoothly video or animation appears to move", "Only the audio quality of a video file"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Choosing an appropriate file format for a multimedia project (e.g. JPEG vs PNG for an image) often depends on factors such as:", "options": [
            "The need for compression, transparency support, or preserving image quality", "A completely random choice with no relevant technical consideration",
            "A concept unrelated to the practical requirements of a multimedia project", "Only the file's creation date, with no reference to technical requirements"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Digital storytelling', using multimedia tools, combines elements such as:", "options": [
            "Narrative text, images, audio, and sometimes video to convey a story or message", "Only plain, unformatted numerical spreadsheet data with no narrative element",
            "A concept unrelated to combining multiple media types to communicate", "Only a single static image with no narrative or additional media involved"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why 'lossy compression' is commonly used for web images and streaming video despite some quality loss?", "options": [
            "It significantly reduces file size, improving loading speed and reducing bandwidth/storage needs, which is often an acceptable trade-off for many uses", "Lossy compression always produces a better-quality result than the original uncompressed file",
            "Lossy compression has no practical benefit over lossless compression in any context", "File size has no relevance to how quickly web content loads or streams"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'streaming' has become the dominant way people consume online video and audio content, rather than downloading full files first?", "options": [
            "Streaming allows playback to begin almost immediately without waiting for an entire large file to download first", "Streaming always requires a much larger complete download before any playback can begin, identical to a full download",
            "Streaming has no practical advantage over requiring a full file download before playback", "Streaming is relevant only to text-based content, not audio or video"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why multimedia content (combining text, images, audio, video) is often considered more engaging for an audience than text alone?", "options": [
            "Combining multiple sensory formats can capture attention and communicate information through more than one channel simultaneously", "Multimedia content is always less effective at engaging an audience than plain text alone",
            "There is no meaningful difference in audience engagement between multimedia and plain text content", "Multimedia content is relevant only to entertainment, with no practical application in education or business"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates the trade-off involved in choosing a higher image 'resolution' for a website's images?", "options": [
            "Higher resolution provides more visual detail but results in a larger file size, which can slow down a webpage's loading time", "Higher resolution always results in a smaller file size with no trade-off whatsoever",
            "Resolution has no relationship to a digital image's file size", "Choosing image resolution has no effect on a webpage's loading performance"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best summarises the overall purpose of this introductory unit on multimedia?", "options": [
            "To build foundational understanding of different multimedia formats and how they are used, compressed, and combined to communicate effectively", "Multimedia concepts have no relevance to modern digital communication",
            "This topic is relevant only to professional video editors, never to general computer literacy", "Studying multimedia replaces the need to understand any other computer science topic"],
         "correct": 0, "difficulty": "Medium"},
    ],
    37573: [  # Digital society and computer ethics
        {"q": "'Digital society' refers to a society in which:", "options": [
            "Digital technology plays a significant role in communication, work, and daily life", "Digital technology has no meaningful role in daily life or communication",
            "A concept unrelated to the role of technology in modern life", "Only a small, isolated group uses any form of digital technology"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Computer ethics' concerns the study of:", "options": [
            "Moral principles guiding the appropriate and responsible use of computers and technology", "A concept entirely unrelated to how technology should be used responsibly",
            "Only the physical safety procedures for handling computer hardware", "Only a computer's technical specifications, with no reference to responsible use"],
         "correct": 0, "difficulty": "Easy"},
        {"q": "'Software piracy' refers to:", "options": [
            "The unauthorised copying, distribution, or use of copyrighted software", "The legal, authorised purchase and use of licensed software",
            "A concept unrelated to software copyright or licensing", "Only a technical term for a type of computer virus"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Plagiarism', an ethical concern amplified by easy digital copying, refers to:", "options": [
            "Presenting someone else's work or ideas as one's own without proper credit", "Properly citing and crediting another person's original work",
            "A concept unrelated to academic or intellectual honesty", "A term relevant only to physical, printed books, with no digital application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Cyberbullying' refers to:", "options": [
            "Using digital technology to harass, intimidate, or harm another person", "Respectful, constructive online communication with no harmful intent",
            "A concept unrelated to online behaviour or interaction", "Only a term describing legitimate business competition online"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Data privacy' concerns relate to:", "options": [
            "How personal information is collected, stored, and used, and an individual's control over it", "A concept unrelated to how personal data is handled by others",
            "Only a company's physical office security measures", "Only a computer's hardware maintenance schedule"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Hacking' typically refers to:", "options": [
            "Gaining unauthorised access to a computer system or network", "Legitimate, authorised access to one's own computer system with proper credentials",
            "A concept unrelated to unauthorised computer access", "Only a technical term for installing new software with proper authorisation"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "A 'computer virus' refers to a type of malicious program that:", "options": [
            "Can replicate itself and spread to other files/systems, often causing harm", "Always improves a computer's performance with no harmful effect",
            "A concept unrelated to malicious software", "Only refers to a legitimate software update"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Netiquette' refers to:", "options": [
            "A set of guidelines for polite, respectful, and appropriate behaviour when communicating online", "A term unrelated to online communication behaviour",
            "Only the technical rules governing internet network protocols", "Only a company's internal HR policy with no relation to online conduct"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Intellectual property rights' in the digital context aim to protect:", "options": [
            "Creators' rights over their original digital work, such as software, music, or written content", "No rights whatsoever regarding digital creative work",
            "A concept unrelated to protecting creative or original work", "Only physical, non-digital property, with no relevance to digital content"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "The 'digital divide' refers to the gap between:", "options": [
            "Those who have access to modern digital technology/internet and those who do not", "A concept unrelated to unequal access to technology",
            "Only a gap in computer processing speed between two specific devices", "A term describing the physical distance between two computer devices"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Responsible digital citizenship' involves using technology in ways that are:", "options": [
            "Ethical, respectful of others, and mindful of legal and social norms", "Entirely careless, with no consideration of ethics or impact on others",
            "A concept unrelated to how one behaves while using digital technology", "Relevant only to businesses, never to individual users"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "'Phishing', a common cybersecurity threat, involves attempting to:", "options": [
            "Deceive individuals into revealing sensitive information (like passwords) by posing as a trustworthy source", "Legitimately request information with full transparency about the requester's identity",
            "A concept unrelated to online deception or fraud", "Only refer to a type of authorised software update process"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Ethical use of AI and automation technologies is an emerging concern partly because of issues such as:", "options": [
            "Algorithmic bias and the potential displacement of certain jobs", "A complete absence of any ethical consideration relevant to AI technology",
            "A concept unrelated to the societal impact of new technology", "Concerns limited exclusively to AI's physical hardware requirements"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "'Digital literacy education', which includes ethics, aims to help individuals:", "options": [
            "Use technology safely, effectively, and responsibly", "Avoid any use of technology whatsoever",
            "A concept unrelated to safe and effective use of technology", "Only learn technical hardware repair skills, with no ethical component"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best explains why software piracy is considered an ethical (and often legal) concern, not merely a technical one?", "options": [
            "It deprives creators and companies of rightful compensation for their work, undermining the incentive to create software", "Software piracy has no negative impact on software creators or companies of any kind",
            "Software piracy is always fully legal in every country with no restriction whatsoever", "This concept applies only to physical goods, not to digital software"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why data privacy has become an increasingly significant ethical concern in a digital society?", "options": [
            "Growing digital data collection by companies and platforms raises questions about consent, control, and potential misuse of personal information", "Data privacy has no relevance to how modern digital platforms operate",
            "No personal data is ever collected by any digital platform or service", "Data privacy concerns are relevant only to government agencies, never to private companies"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best explains why 'netiquette' guidelines are considered important for maintaining a healthy online community?", "options": [
            "They help promote respectful, constructive communication, reducing conflict and harmful behaviour in digital spaces", "Netiquette guidelines have no bearing on the quality of online interactions",
            "Online communication requires no consideration of politeness or respect, unlike face-to-face communication", "Netiquette applies only to professional workplace email, with no relevance to general online communication"],
         "correct": 0, "difficulty": "Hard"},
        {"q": "Which of the following best illustrates a responsible response to encountering a suspicious 'phishing' email requesting personal information?", "options": [
            "Not clicking any links or providing information, and verifying the sender's legitimacy through an independent, trusted channel", "Immediately providing all requested personal and financial information without any verification",
            "Forwarding the email to as many contacts as possible with no warning about its suspicious nature", "A concept with no practical real-world application"],
         "correct": 0, "difficulty": "Medium"},
        {"q": "Which of the following best summarises the overall importance of studying digital society and computer ethics within an introductory Computer Science course?", "options": [
            "It helps students understand the social responsibilities and ethical considerations that come with using and being affected by digital technology", "This topic has no practical relevance to how students use technology in their own lives",
            "Ethics is relevant only to computer science professionals, never to general technology users", "Studying digital ethics replaces the need to understand any technical computing concept"],
         "correct": 0, "difficulty": "Medium"},
    ],
}
