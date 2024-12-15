# Student Management System

This project is a **Student Management System** that allows users to perform CRUD (Create, Read, Update, Delete) operations on student data. It integrates a **Django REST Framework** backend with a **Vue.js** frontend and leverages Material Design Lite for UI styling.

---

## Features

1. **Backend**: Django REST Framework (DRF)
   - Student data model with fields: `Name`, `address`, and `fee`.
   - RESTful API endpoints for handling CRUD operations.
     - **GET**: Fetch all students.
     - **POST**: Add a new student.
     - **PUT**: Update existing student data.
     - **DELETE**: Remove a student record.

2. **Frontend**: Vue.js with Material Design Lite
   - User-friendly form for adding student details.
   - Dynamic data binding using Vue.js (`v-model`).
   - Fetch API integration to communicate with the backend.

---


## Installation and Setup

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/VasanthaKumar-20/student-management-system.git
   cd student-management-system
   ```

2. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate   # For Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. Migrate the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Add Vue.js to your project using the CDN (already included in this repository).

2. Ensure the form in the HTML communicates with the Django backend:
   - API URL: `http://127.0.0.1:8000/api/`

---

## Usage

1. Navigate to the form in your browser:
   ```
   http://127.0.0.1:8000
   ```

2. Enter student details (Name, Address, Fee) and click **Submit**.
3. The data will be sent to the backend and stored in the database.
4. Use API endpoints for additional CRUD operations.

---

## API Endpoints

- **GET**: `/api/` - Retrieve all students.
- **POST**: `/api/` - Add a new student.
- **PUT**: `/api/<id>` - Update student details.
- **DELETE**: `/api/<id>` - Delete a student record.

---

## Future Enhancements

- Add validation for form fields.
- Implement search and filtering features.
- Include pagination in the API.
- Enhance the frontend with Vue.js components.

---



## Contact

Created by **Vasanth**. For any inquiries, please reach out via [GitHub](https://github.com/VasanthaKumar-20).

