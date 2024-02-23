# Project Requirement
## Document for RCAT Migration to Django and Next.js
## Executive Summary

RCAT is transitioning its existing web application infrastructure to a more scalable and modern architecture using Django for the backend and Next.js for the frontend. This migration aims to enhance the platform's performance, improve user experience, and streamline the development process. RCAT provides a comprehensive suite of tools for schools to manage educational content, assessments, and track student progress across various grades and subjects, with a focus on reading comprehension and vocabulary skills.

## Project Glossary

- **Django**: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Next.js**: A React framework for production that provides server-side rendering, static site generation, and more, to ensure fast, scalable, and easy-to-deploy applications.
- **Administrator (RCAT Main Admin)**: Users responsible for overseeing and managing the RCAT platform, including schools, districts, regions, and system settings.
- **District Administrator**: Users with administrative rights over a specific district, responsible for managing schools and educators within their district.
- **Educator/Teacher**: Users who create, manage, and distribute assessments and educational content.
- **Student**: Users who participate in assessments and access educational content.
- **API**: Application Programming Interface, a set of protocols and tools for building software and applications.
- **JWT**: JSON Web Tokens, a method for securely transmitting information between parties as a JSON object.

## User Stories

### Administrator Portal (RCAT Main Admin)

#### Phase 1

##### User Story: School and District Management

> As the RCAT main admin, I want to add schools, whitelist domains, and manage regions and districts to ensure schools can access RCAT efficiently.

Acceptance Tests:

1. Admin can add and manage school profiles, including whitelisting domains.
2. Admin can create and organize districts and regions, linking schools appropriately.
3. System supports adding district administrators with specific management permissions.

##### User Story: Test and Skill Management

> As the RCAT main admin, I want to manage the skills and tests available on the platform to ensure they meet educational standards and requirements.

Acceptance Tests:

1. Admin can add, modify, or remove skills and categories related to reading comprehension and vocabulary.
2. The platform allows for categorization of questions in tests by genres, including informational, narrative, poetry, and tier 2 vocabulary.
3. Admin can create and manage a repository of tests, including the ability to add passages, questions, and math problems with a math editor.

### Educator Portal

#### Phase 1

##### User Story: Assessment Creation and Distribution

> As an educator, I want to create assessments from existing tests or create new ones to evaluate my students' progress in specific skills.

Acceptance Tests:

1. Educators can select from a pool of existing tests or create new tests tailored to their classroom needs.
2. The test creation interface supports adding various question types, including multiple-choice, fill-in-the-blanks, and math problems.
3. Educators can assign tests to students, schedule test availability, and track completion.

##### User Story: Student Progress Monitoring

> As an educator, I want to monitor my students' progress and performance on tests to provide targeted support and feedback.

Acceptance Tests:

1. Educators have access to detailed reports on student test performances, including scores and skill evaluations.
2. The platform provides analytics on class-wide performance trends and individual student progress.
3. Educators can identify areas of improvement and strengths, facilitating personalized feedback and support.

### Student Portal

#### Phase 1

##### User Story: Accessing and Completing Assessments

> As a student, I want to access and complete assessments assigned to me to demonstrate my understanding and skills.

Acceptance Tests:

1. Students can easily find and access assigned tests within their portal.
2. The testing interface is user-friendly, supporting various question types and including a math editor for relevant problems.
3. Students receive immediate feedback upon completion, including scores and correct answers for review.

##### User Story: Tracking Learning Progress

> As a student, I want to track my progress and performance over time to understand my learning growth and areas for improvement.

Acceptance Tests:

1. Students have access to a dashboard summarizing their performance on recent tests.
2. The platform tracks and displays progress in various skills over time, highlighting strengths and areas for improvement.
3. Students can set personal learning goals and monitor their advancement towards these goals.

## MoSCoW Prioritization

### Must Have

1. A Django-based backend with RESTful API endpoints for school, district, and test management.
2. A Next.js-based frontend with intuitive interfaces for administrators, educators

, and students.
3. Secure authentication and authorization processes, including JWT for API access and domain whitelisting for school access.
4. Comprehensive role management for administrators, district administrators, educators, and students.

### Should Have

1. Advanced analytics and reporting tools for tracking student progress and performance.
2. A math editor for creating and solving math problems within assessments.
3. Customizable test creation tools, allowing for a wide range of question types and content.

### Could Have

1. Integration with external educational resources and content providers.
2. Gamification elements for student engagement and motivation.
3. Personalized learning recommendations based on student performance and progress.

### Won't Have (at launch)

1. Real-time collaboration tools for students and educators.
2. Blockchain-based credentialing and record-keeping for educational achievements.
3. A mobile app version of the platform for enhanced accessibility and engagement.

## Technical Resources

### Backend Development

- **Framework**: Django
  - [Django Documentation](https://docs.djangoproject.com/en/3.2/)
- **Database**: PostgreSQL
  - [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- **Authentication**: Django Rest Framework SimpleJWT
  - [DRF SimpleJWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

### Frontend Development

- **Framework**: Next.js
  - [Next.js Documentation](https://nextjs.org/docs)
- **State Management**: Redux or Context API
  - [Redux Documentation](https://redux.js.org/introduction/getting-started)
  - [React Context Documentation](https://reactjs.org/docs/context.html)
- **Styling**: Tailwind CSS or Styled-Components
  - [Tailwind CSS Documentation](https://tailwindcss.com/docs)
  - [Styled-Components Documentation](https://styled-components.com/docs)

### Deployment and Operations

- **Cloud Hosting**: AWS or Vercel
  - [AWS Documentation](https://aws.amazon.com/documentation/)
  - [Vercel Documentation](https://vercel.com/docs)
- **CI/CD**: GitHub Actions
  - [GitHub Actions Documentation](https://docs.github.com/en/actions)


## Divided User Stories

Administrator Portal (RCAT Main Admin)
--------------------------------------

### School and District Management

1.  Add New School
    -   As an RCAT admin, I can add new schools to the platform to expand its reach and utility.
2.  Whitelist School Domains
    -   As an RCAT admin, I can whitelist school domains to ensure secure and exclusive access to the platform.
3.  Create Districts
    -   As an RCAT admin, I can create districts, organizing schools within specific geographical or administrative boundaries.
4.  Assign Schools to Districts
    -   As an RCAT admin, I can assign schools to their respective districts for better regional management.
5.  Add District Administrator
    -   As an RCAT admin, I can add district administrators to delegate management responsibilities within specific districts.

### Test and Skill Management

1.  Add Skills
    -   As an RCAT admin, I can add new skills to the test database to keep the curriculum up-to-date with educational standards.
2.  Edit Skills
    -   As an RCAT admin, I can edit existing skills to ensure accuracy and relevancy.
3.  Delete Skills
    -   As an RCAT admin, I can delete outdated or irrelevant skills from the platform.
4.  Create Test Templates
    -   As an RCAT admin, I can create test templates that educators can use or modify for their assessments.
5.  Categorize Test Questions
    -   As an RCAT admin, I can categorize test questions by genre (e.g., informational, narrative) to facilitate targeted assessments.

### Platform Configuration and Security

1.  Configure Test Settings
    -   As an RCAT admin, I can configure settings for tests, including time limits and availability windows.
2.  Manage User Roles and Permissions
    -   As an RCAT admin, I can manage user roles and permissions to ensure secure access to the platform's features.
3.  Monitor Platform Usage
    -   As an RCAT admin, I can monitor platform usage statistics to understand adoption rates and user engagement.
4.  Update Platform Security
    -   As an RCAT admin, I can update security protocols to protect user data and ensure compliance with privacy regulations.
5.  Backup and Restore Data
    -   As an RCAT admin, I can perform data backup and restoration to prevent data loss and maintain platform integrity.

Educator Portal
---------------

### Assessment Management

1.  Select Test Template
    -   As an educator, I can select from existing test templates to quickly create assessments.
2.  Customize Test Questions
    -   As an educator, I can customize test questions, adding or removing items based on my students' needs.
3.  Assign Tests to Students
    -   As an educator, I can assign tests to individual students or classes, scheduling them according to the lesson plan.
4.  Review Test Submissions
    -   As an educator, I can review test submissions, providing feedback and grades to students.
5.  Track Student Progress
    -   As an educator, I can track student progress on assessments over time to identify learning trends and areas for improvement.

Student Portal
--------------

### Engagement with Assessments

1.  Access Assigned Tests
    -   As a student, I can access tests assigned to me, viewing due dates and instructions.
2.  Complete Online Tests
    -   As a student, I can complete online tests, using tools like the math editor for specific questions.
3.  View Test Feedback
    -   As a student, I can view feedback and grades on completed tests to understand my performance.
4.  Track Personal Learning Progress
    -   As a student, I can track my learning progress through a dashboard, viewing my achievements and areas for growth.
5.  Set Personal Learning Goals
    -   As a student, I can set personal learning goals and monitor my progress toward achieving them.