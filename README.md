# happiness-project-impact-analysis
Analysis of Assignment Impact on Student Well-being (The Happiness Project)
This repository contains a comprehensive data analysis of the "Happiness Project," a course designed to improve student well-being through practical assignments. The project synthesizes quantitative performance data with qualitative feedback to provide data-driven insights into the course's effectiveness.

1. Business Problem & Objective
For any educational program, especially one focused on personal development, a critical question is: Which activities have the most meaningful and transformative impact on students, and why?

This project addresses that question by analyzing student data to identify the most impactful assignments. The primary objective is to provide actionable recommendations for curriculum development, ensuring the course prioritizes exercises that deliver the greatest value to student well-being and personal growth.

2. Data Sources
The analysis is built upon two distinct types of anonymized student data:

Quantitative Data: Sourced from course surveys and records (.xlsx files). This includes performance metrics such as:

Overall course grade    

Percentage of on-time assignment submissions    

Course engagement metrics (e.g., page views, participations)    

Qualitative Data: Sourced from the text of student assignment submissions (.pdf, .docx, .txt files). This unstructured data, particularly from midterm exam feedback, provides rich, detailed narratives about students' personal experiences, breakthroughs, and the emotional impact of each task.   

Note: All data was rigorously anonymized to protect student privacy before analysis. All personally identifiable information (PII) such as names and emails was removed.

3. Analysis Methodology
A dual approach was employed to gain a holistic understanding of the project's impact:

Quantitative Analysis:

Descriptive statistics were calculated using Python and the Pandas library to establish a baseline of student performance and engagement. This involved analyzing the distribution, mean, and median of grades and submission rates.   

Qualitative & Thematic Analysis:

Text from student reflections was systematically extracted and processed.

Using Natural Language Processing (NLP) principles, this qualitative data was analyzed to identify recurring themes, emotions, and key takeaways for each major assignment.

A frequency analysis of midterm feedback was conducted to rank assignments based on their reported impact.   

4. Key Findings & Insights
The analysis yielded clear and compelling insights into what makes an assignment effective. The central finding is that the most transformative assignments are those that combine practical, real-world application with deep self-reflection.

Ranking of Most Impactful Assignments
Based on student feedback, the top 5 most impactful assignments were :   

"Three Good Things" Assignment

Time Tracking Assignment

Gratitude Letter Assignment

Digital Detox Assignment

Get Some Sleep Assignment

Core Themes Driving Impact
Across the highest-rated assignments, three core themes emerged as drivers of positive change :   

Habit Formation & Practicality: Students placed high value on simple, actionable exercises (like "Three Good Things") that they could easily integrate into their daily routines and continue practicing long after the assignment was complete.

Data-Driven Self-Awareness: Assignments that provided students with objective data about their own behavior (e.g., the "Time Tracking Assignment") were profoundly empowering. This awareness served as a powerful catalyst for intentional change.

Strengthening Social Connections: Exercises that encouraged vulnerability and strengthened social bonds (e.g., the "Gratitude Letter") generated the most significant and lasting positive emotional impact, benefiting both the student and the recipient.

Actionable Recommendation
Based on these findings, it is recommended that the course curriculum prioritizes and expands upon these types of actionable, reflective, and socially-oriented exercises to maximize student well-being and long-term engagement with the material.

5. Tech Stack
Language: Python

Libraries for Analysis:

Pandas: For data manipulation, cleaning, and quantitative analysis.

Matplotlib / Seaborn: For data visualization (used in the analysis phase).

NLTK / spaCy: For qualitative text processing and thematic analysis.
