# Flashcard App

This is a simple full-stack Flashcard application built using Vue.js for the frontend and Django for the backend. The app allows users to:

- Add new flashcards
- Flip flashcards to see the answer
- Delete existing flashcards

## Demo

Watch the working demo on YouTube:  
**[Click here to watch the video](https://youtu.be/g7fgZ9vKAbU?si=7Qpuq4MLwdtpfdpB)**  
---

## Features

- Create new flashcards using a form or add button
- Flip each card to reveal the answer
- Delete cards when no longer needed
- Smooth UI animations using Tailwind CSS
- Built using Vue.js (frontend) and Django REST Framework (backend)

---

## Technologies Used

- **Frontend**: Vue.js, Tailwind CSS
- **Backend**: Django, Django REST Framework
- **Others**: Axios (for API requests), CORS Headers

---

## Getting Started

Follow the instructions below to run the app locally on your system.

---

### Backend Setup (Django)

1. Clone the repository and navigate to the backend directory:
   ```bash
   git clone <your-repo-url>
   cd backend
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the backend server:

   ```bash
   python manage.py runserver
   ```

---

### Frontend Setup (Vue.js)

1. Open a new terminal and navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the frontend development server:

   ```bash
   npm run dev
   ```

---

### Usage

* Open the app in your browser at: `http://localhost:5173` (or the port shown in terminal)
* Click the **plus** flashcard to create a new flashcard.
* Click any flashcard to flip and see the answer.
* Use the delete button to remove any flashcard.

---

## Project Structure

```
flashcard-app/
│
├── backend/
│   ├── manage.py
│   ├── flashcards/ (Django app)
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── ...
│
├── requirements.txt
└── README.md
```

---

## Notes

* CORS is enabled for local frontend-backend communication.
* The backend API is available at: `http://localhost:8000/api/flashcards/`
* Flashcards are persisted using Django’s default SQLite database.
