# UniApps Planning

### Project idea 
>Web application tool for Higher Education admissions staff. This interactive application will allow counselors, (typically the first point of contact for prospective applicants) to keep track of applicant status as well as the application status throughout the enrollments process. With the option to sign up/log in, counselors will have full access to maintain and manage applicant records. Additionally, counselors will have a graphical overview of applicant and application data to maximize efficiency in analysis. 

### Tech stack (frontend, backend, database)
- Frontend - React
- Backend - Django 
- Database - PostgreSQL

### List of backend models and their properties
- Counselor
    - name
    - email
    - password
    - university
    
- Applicant
    - name
    - email
    - phone-number
    - major
    - enrollment status
        - inquiry
        - enrolled
        - deferred
       
- Application
    - academic year
    - start term/semester
    - intended-major
    - status
        - in progress
        - applied
        - processed
        - accepted
        - deposited
        - denied
        - waitlisted
    - last updated
    - recent school
    - GPA
    - applicant (Foreign Key)
    
### React component hierarchy (if applicable)
- Counselor
    - Applicants
        - Applicant
            - Application
            
### User stories
- [ ] As a user (counselor), I would like to have the option to register/log in.
- [ ] As a logged in user, I would like to view applicant information and enrollment status.
- [ ] As a logged in user, I would like to create a new applicant record.
- [ ] As a logged in user, I would like to edit applicant information and update enrollment status.
- [ ] As a logged in user, I would like to delete applicant records.
- [ ] As a logged in user, I would like to add new applications to applicant records.
- [ ] As a logged in user, I would like to edit application information and status.
- [ ] As a logged in user, I would like to delete applications.
- [ ] As a logged in user, I would like to view the overall status of applicants and applications.
- [ ] As a logged in user, I would like a quick way to email applicants.

#### Stretch Goals

- [ ] As a logged in user, I would like to see visual charts showing the overall analysis of applicants and applications.
- [ ] As a logged in user, I would like to have a search functionality to search applicants and applications. 
- [ ] As a logged in user, I would like to have a text feature to send and receive messages from applicants.
- [ ] As a logged in user, I would like to be able to have live chat functionality.

### Wireframes

Landing Page
![Screen Shot 2022-09-01 at 23 12 35](https://media.git.generalassemb.ly/user/41660/files/662d5f12-2aa0-43ac-82da-ed97e9a42f74)

Counselor Dashboard 
![Screen Shot 2022-09-01 at 23 37 48](https://media.git.generalassemb.ly/user/41660/files/2e624e1c-ab5c-43e7-aa60-797509851f61)
