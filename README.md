# Scroll Tracker with DSA Insights

This is a visually interactive web app built with **Flask**, **JavaScript**, and **CSS**, designed to show real-time scroll tracking and integrate core **Data Structures & Algorithms**.

## Purpose
Track how much of a page the user has scrolled and reveal algorithmic insights based on progress. This makes it both visually appealing and intellectually engaging—perfect for showcasing frontend skills and DSA knowledge.

## Technologies Used
- **Python (Flask)** – for backend routing and algorithm processing
- **HTML/CSS** – for structure and styling
- **JavaScript** – for dynamic scroll tracking and fetch API calls

## Algorithms Integrated
### 1. Longest Unique Substring (Sliding Window)
Detects the longest substring without repeating characters.
```python
Input: "abrkaabcdefghijjxxx"
Output: "abcdefghij"
```

### 2. Longest Palindromic Substring (Expand Around Center)
Finds the longest palindrome in a string.
```python
Input: "babad"
Output: "bab" or "aba"
```

## Features
- Scroll progress bar with percentage label
- Algorithm insights shown based on scroll percentage:
  - 0–24%: Longest Unique Substring
  - 25–49%: Longest Palindromic Substring
  - 50–74%: Motivational message
  - 75–100%: Completion message

## How to Run
```bash
pip install flask
python scroll_tracker.py
```
Then open [http://localhost:5000](http://localhost:5000) in your browser.

## File Structure
```
scroll_tracker/
├── static/
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html
├── scroll_tracker.py
└── README.md
```

## Note
Built in under 12 hours for a fast visual + DSA showcase.

## Author
[mahtabpnm](https://github.com/mahtabpnm)
