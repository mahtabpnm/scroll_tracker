# 📊 Scroll Tracker Web App

A Flask-based web application that visually tracks how much of a webpage a user has scrolled and offers motivational tips based on progress. Great for blogs, readers, or educational pages.

---

## 🎯 Purpose

This app helps users stay engaged by showing a live progress percentage while scrolling through long content and displaying dynamic motivational messages based on how far they’ve read.

It mimics user behavior tracking like modern analytics tools, while being lightweight and educational.

---

## 🚀 Features

- Real-time scroll percentage display
- Dynamic tips based on scroll progress
- Colorful UI with CSS styling
- Simple Flask backend + frontend communication
- Includes basic DSA elements (Array + String)

---

## 🧠 Algorithm & Data Structures Used

### Frontend (JavaScript)
- Calculates scroll percentage using:
  ```js
  percent = (scrollTop / (documentHeight - windowHeight)) * 100
  ```
- Sends data to the backend using `fetch()`.

### Backend (Python + Flask)
- Uses a **list (array)** to store pre-defined motivational messages:
  ```python
  tips = ["Keep going!", "You're halfway there!", "Almost done!", "You made it to the end!"]
  ```
- Uses **conditional logic** to select a tip based on scroll percentage:
  ```python
  if percent < 25:
      return tips[0]
  elif percent < 50:
      return tips[1]
  elif percent < 75:
      return tips[2]
  else:
      return tips[3]
  ```

This is a **constant-time (O(1))** operation using array indexing and control flow logic.

---

## 🛠️ Tech Stack

- **Python** + **Flask**
- **HTML/CSS/JavaScript**
- Local API with `fetch()`
- Optional: Jinja2 templating

---

## ⚙️ How to Run the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/mahtabpnm/scroll_tracker.git
   cd scroll_tracker
   ```

2. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install Flask:
   ```bash
   pip install flask
   ```

4. Run the Flask app:
   ```bash
   python scroll_tracker.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

---

## 🌟 Future Ideas

- Save user scroll history per session
- Add charts or graphs to track user behavior
- Support multiple pages with different tip sets
- Host it online using Render or PythonAnywhere

---

## 📸 Screenshot

*You can insert a screenshot here once your app is running!*

---

## 👩‍💻 Author

**Mahtab P.**  
Made with 💙 using Python + Flask  
[GitHub Profile](https://github.com/mahtabpnm)
