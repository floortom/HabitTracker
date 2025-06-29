## 🧾 Flask Habit Tracker

This is a simple yet powerful web application I built using **Flask** and **MongoDB** to help track daily habits over time. The app allows users to create habits (like “Read a book” or “Exercise”), mark them as completed on specific dates, and view progress day by day.

### 🔍 Features
- ✅ Add and manage daily habits
- 📅 Navigate between dates (past and future) using a dynamic date picker
- 📌 Automatically hide habits on dates before they were created
- 🗃️ Two MongoDB collections:
  - One for habit definitions
  - One for individual habit completions
- ✍️ Form handling with hidden fields to pass necessary metadata
- 🎨 Custom form styling for a clean and user-friendly UI

### 🧠 What I Learned
- How to build a focused, single-purpose Flask app from scratch  
- How to implement **date-based filtering** using query string arguments  
- How to manage form submissions with hidden fields and dynamic values  
- How to structure and save data in **MongoDB** collections  
- How to dynamically render the UI based on the habit creation date  
- How to separate the logic for creating habits vs. marking them completed  

### 📦 Tech Stack
- **Flask** – Web framework for Python  
- **MongoDB Atlas** – Cloud-based NoSQL database  
- **Jinja2** – Templating for dynamic HTML  
- **Bootstrap (or custom CSS)** – For UI styling

### 🚀 Running the App Locally
Make sure your virtual environment is activated, then run:

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_DEBUG = 1
flask run
