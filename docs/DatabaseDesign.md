# Database Design

[![UML](https://github.com/rahuluniv/EduBest/blob/main/images/UML.png)
[![UML](https://github.com/rahuluniv/EduBest/blob/main/images/database_walk.png)


### Database Schema Overview

The proposed database schema is designed to support the RCAT platform's core functionalities, including managing schools, districts, users (administrators, district administrators, educators, and students), tests, skills, and user progress tracking. The database will be built using PostgreSQL, considering its robustness, scalability, and compatibility with Django.

### Entities and Relationships

1. **Users**
    - Attributes: UserID, FirstName, LastName, Email, Role (Enum: Admin, DistrictAdmin, Educator, Student), PasswordHash, LastLogin, IsActive
    - Relationships: One-to-many with Schools (for DistrictAdmin and Educator), one-to-many with Tests (for Educator)

2. **Schools**
    - Attributes: SchoolID, Name, Domain, DistrictID, Region
    - Relationships: Many-to-one with Districts, one-to-many with Users

3. **Districts**
    - Attributes: DistrictID, Name, RegionID
    - Relationships: Many-to-one with Regions, one-to-many with Schools

4. **Regions**
    - Attributes: RegionID, Name
    - Relationships: One-to-many with Districts

5. **Tests**
    - Attributes: TestID, Title, Description, CreatedBy (UserID), CreationDate, IsActive
    - Relationships: Many-to-one with Users (CreatedBy), many-to-many with Skills, one-to-many with Questions

6. **Skills**
    - Attributes: SkillID, Name, Description, Category (Enum: ReadingComprehension, Vocabulary)
    - Relationships: Many-to-many with Tests

7. **Questions**
    - Attributes: QuestionID, TestID, Text, Type (Enum: MultipleChoice, FillInTheBlanks, MathProblem), CorrectAnswer, SkillID
    - Relationships: Many-to-one with Tests, many-to-one with Skills

8. **StudentTestResults**
    - Attributes: ResultID, StudentID (UserID), TestID, Score, CompletionDate
    - Relationships: Many-to-one with Users (StudentID), many-to-one with Tests

9. **StudentSkillProgress**
    - Attributes: ProgressID, StudentID (UserID), SkillID, Level, LastUpdated
    - Relationships: Many-to-one with Users (StudentID), many-to-one with Skills

### Security and Authentication

- **User Authentication**: Utilize Django Rest Framework SimpleJWT for handling user authentication and authorization. JWT tokens will be used to securely manage user sessions and API access.
- **Domain Whitelisting**: Implement domain whitelisting at the application level to ensure that only authorized domains (schools) can access the platform.

### Role Management

- Utilize Django's built-in user management system to define custom user roles (Admin, DistrictAdmin, Educator, Student) and permissions. This setup will facilitate secure and role-appropriate access to various platform features.

### Additional Considerations

- **Indexes**: Create indexes on frequently queried fields (e.g., UserID, SchoolID, TestID) to enhance query performance.
- **Normalization**: Ensure the database schema is normalized to at least the third normal form (3NF) to reduce redundancy and improve data integrity.
- **Backup and Restoration**: Implement regular database backups and test restoration procedures to safeguard against data loss.
To develop a detailed database design document for the RCAT Migration project described, which encompasses Django for backend and Next.js for frontend, we'll outline the essential components required for the database schema. This will include tables, relationships, key features, and considerations necessary to support the functionalities and user stories outlined in your project requirements.

