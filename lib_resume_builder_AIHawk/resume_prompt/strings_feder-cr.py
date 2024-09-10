from lib_resume_builder_AIHawk.template_base import *

prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, LinkedIn profile, and GitHub profile. Exclude any information that is not provided.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}
""" + prompt_header_template


prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
3. **Grade**: Include your Grade if it is strong and relevant.
4. **Relevant Coursework**: List key courses with their grades to showcase your academic strengths.

- **My information:**  
  {education_details}
"""+ prompt_education_template


prompt_working_experience = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to detail the work experience for a resume. For each job entry, ensure you include:

1. **Company Name and Location**: Provide the name of the company and its location.
2. **Job Title**: Clearly state your job title.
3. **Dates of Employment**: Include the start and end dates of your employment.
4. **Responsibilities and Achievements**: Describe your key responsibilities and notable achievements, emphasizing measurable results and specific contributions.

- **My information:**  
  {experience_details}
"""+ prompt_working_experience_template

- **Template to Use**
```
<section id="work-experience">
    <h2>Work Experience</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name">[Company Name]</span>
          <span class="entry-location"> — [Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date]</span>
      </div>
      <ul class="compact-list">
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe any key projects or technologies you worked with]  </li>
          <li>[Describe any key projects or technologies you worked with]  </li>
          <li>[Mention any notable accomplishments or results]</li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name">[Company Name]</span>
          <span class="entry-location"> — [Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date]</span>
      </div>
      <ul class="compact-list">
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe your responsibilities and achievements in this role] </li>
          <li>[Describe any key projects or technologies you worked with]  </li>
          <li>[Describe any key projects or technologies you worked with]  </li>
          <li>[Mention any notable accomplishments or results]</li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name">[Company Name]</span>
          <span class="entry-location"> — [Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date]</span>
      </div>
      <ul class="compact-list">
          <li>[Describe your responsibilities and achievements in this role]</li>
          <li>[Describe any key projects or technologies you worked with]</li>
          <li>[Mention any notable accomplishments or results]</li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_side_projects = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to highlight notable side projects. For each project, ensure you include:

1. **Project Name and Link**: Provide the name of the project and include a link to the GitHub repository or project page.
2. **Project Details**: Describe any notable recognition or achievements related to the project, such as GitHub stars or community feedback.
3. **Technical Contributions**: Highlight your specific contributions and the technologies used in the project.

- **My information:**  
  {projects}
"""+ prompt_side_projects_template



prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution’s name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
3. **GPA**: Include your GPA if it is strong and relevant.
4. **Relevant Coursework**: List key courses with their grades to showcase your academic strengths but make sure you only list the course you have. You may leave it as empty if there is none. 

- **My information:**  
  {education_details}

- **Template to Use**
```
<section id="education">
    <h2>Education</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name">[University Name]</span>
          <span class="entry-location">[Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Degree] in [Field of Study] | GPA: [Your GPA]/4.0</span>
          <span class="entry-year">[Start Year] – [End Year]</span>
      </div>
      <ul class="compact-list">
          <li>[Course Name] → GPA: [Grade]/4.0</li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_achievements = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant achievements. For each achievement, ensure you include:

1. **Award or Recognition**: Clearly state the name of the award, recognition, scholarship, or honor.
2. **Description**: Provide a brief description of the achievement and its relevance to your career or academic journey.

- **My information:**  
  {achievements}
"""+ prompt_achievements_template


prompt_certifications = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant certifications based on the provided details. For each certification, ensure you include:

1. Certification Name: Clearly state the name of the certification.
2. Description: Provide a brief description of the certification and its relevance to your professional or academic career.

Ensure that the certifications are clearly presented and effectively highlight your qualifications.

To implement this:

If any of the certification details (e.g., descriptions) are not provided (i.e., None), omit those sections when filling out the template.

- **My information:**  
  {certifications}

- **Job Description:**  
  {job_description}
"""+ prompt_certifications_template


prompt_additional_skills = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list additional skills relevant to the job. For each skill, ensure you include:

1. **Skill Category**: Clearly state the category or type of skill.
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Proficiency and Experience**: Briefly describe your experience and proficiency level.

- **My information:**  
  {languages}
  {interests}
  {skills}
"""+ prompt_additional_skills_template
