## Flask Application Design

### HTML Files

#### `index.html`

- Purpose: Serves as the homepage of the portfolio.
- Content:
  - Elegant header section introducing the college and its design portfolio.
  - Sections showcasing various design projects created by college students, including images, descriptions, and brief explanations.
  - An elegant footer section providing contact information and social media links.

#### `about.html`

- Purpose: Provides information about the college and its commitment to design education.
- Content:
  - A detailed overview of the college's design curriculum, highlighting the programs, specializations, and faculty members.
  - Compelling testimonials from design professionals who graduated from the college.
  - A dynamic image gallery showcasing the college's facilities, such as studios, labs, and workshops.

#### `projects.html`

- Purpose: Displays a comprehensive collection of design projects from students and alumni.
- Content:
  - An extensive gallery featuring diverse design projects, including illustrations, graphics, websites, and product designs.
  - Interactive filtering and sorting options to help visitors easily find projects of interest.
  - Brief descriptions and project credits for each displayed work.

#### `contact.html`

- Purpose: Facilitates communication between prospective students, parents, and the college's admissions department.
- Content:
  - A well-structured form for visitors to submit inquiries or schedule a campus visit.
  - Contact information, including email addresses and phone numbers, for various departments and offices.
  - An interactive map providing clear directions to the college campus.

### Routes

#### `@app.route("/")`

- Purpose: Directs users to the homepage of the portfolio (`index.html`).

#### `@app.route("/about")`

- Purpose: Directs users to the page providing information about the college and its design education programs (`about.html`).

#### `@app.route("/projects")`

- Purpose: Directs users to the gallery showcasing student design projects (`projects.html`).

#### `@app.route("/contact")`

- Purpose: Directs users to the contact page for inquiries and campus visits (`contact.html`).

#### `@app.route("/submit-inquiry")`

- Purpose: Handles form submissions from the contact page, sending inquiries to the admissions department via email.

#### `@app.route("/error")`

- Purpose: Displays a generic error message if any unforeseen errors occur during the application's operation.