# Google Cloud Tech Summit 2026 - Conference Website

A modern, responsive 1-day technical conference website built with Python Flask, featuring a beautiful dark theme, real-time search functionality, and comprehensive schedule management.

## 🌟 Features

- **Modern Dark Theme**: Beautiful gradient-based design with smooth animations
- **Real-time Search**: Search talks by title, speaker name, or category
- **Category Filtering**: Filter sessions by Infrastructure & Development or Data & AI categories
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Speaker Profiles**: Each speaker includes LinkedIn integration
- **8 Technical Talks**: Full-day schedule with 60-minute lunch break
- **Google Cloud Focus**: All talks centered around Google Cloud Technologies

## 📋 Conference Details

- **Event**: Google Cloud Tech Summit 2026
- **Date**: March 15, 2026
- **Location**: San Francisco Convention Center, CA
- **Duration**: 9:00 AM - 6:15 PM (with 60-minute lunch break)
- **Total Talks**: 8 sessions
- **Total Speakers**: 10 industry experts

## 🏗️ Project Structure

```
Conference/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── templates/
│   └── index.html             # Main HTML template
└── static/
    ├── css/
    │   └── style.css          # Stylesheet with modern design
    └── js/
        └── script.js          # JavaScript for search & interactivity
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Navigate to the project directory**:
   ```bash
   cd C:\Users\Alex\Documents\ProyectosAnt\Conference
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Running the Application

1. **Start the Flask development server**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **To stop the server**, press `Ctrl+C` in the terminal.

## 🔍 Using the Website

### Viewing the Schedule
- The home page displays all 8 talks in chronological order
- Each talk card shows:
  - Time slot
  - Title
  - Category badge
  - Description
  - Speaker information with LinkedIn links

### Searching for Sessions

1. **Search by Title or Speaker**:
   - Type keywords in the search box
   - Results update automatically after 300ms (debounced)
   - Example: "Machine Learning" or "Sarah Chen"

2. **Filter by Category**:
   - Use the dropdown to select:
     - Category 1: Infrastructure & Development
     - Category 2: Data & AI
   - Select "All Categories" to clear the filter

3. **Combined Search**:
   - Use both search box and category filter together
   - Results will match both criteria

### Speaker Information
- Click on any LinkedIn link to view speaker profiles
- Each speaker has a unique avatar with their initials

## 📊 Conference Schedule

| Time | Talk | Category | Speakers |
|------|------|----------|----------|
| 09:00 - 10:00 | Keynote: The Future of Cloud Computing | 1 | Sarah Chen |
| 10:15 - 11:15 | Building Scalable Applications with GKE | 1 | Michael Rodriguez, Emily Johnson |
| 11:30 - 12:30 | Machine Learning on Google Cloud Platform | 2 | David Kim |
| 12:30 - 01:30 | **Lunch Break** | - | - |
| 01:30 - 02:30 | Serverless Architecture with Cloud Functions | 1 | Jessica Martinez, Robert Thompson |
| 02:45 - 03:45 | Data Analytics with BigQuery and Looker | 2 | Amanda Lee |
| 04:00 - 05:00 | Security Best Practices for Google Cloud | 1 | James Wilson, Lisa Anderson |
| 05:15 - 06:15 | Cloud Migration Strategies | 2 | Daniel Brown |

## 🛠️ Making Changes

### Adding New Talks

Edit `app.py` and add a new entry to the `TALKS` list:

```python
{
    'id': 9,  # Increment the ID
    'title': 'Your Talk Title',
    'speaker_ids': [1, 2],  # Reference speaker IDs
    'category': 1,  # 1 or 2
    'description': 'Talk description',
    'time': '06:30 PM - 07:30 PM'
}
```

### Adding New Speakers

Edit `app.py` and add a new entry to the `SPEAKERS` list:

```python
{
    'id': 11,  # Increment the ID
    'first_name': 'John',
    'last_name': 'Doe',
    'linkedin': 'https://www.linkedin.com/in/johndoe'
}
```

### Modifying Conference Details

Edit the `CONFERENCE_DATA` dictionary in `app.py`:

```python
CONFERENCE_DATA = {
    'name': 'Your Conference Name',
    'date': 'Your Date',
    'location': 'Your Location',
    'description': 'Your Description'
}
```

### Customizing Styles

Edit `static/css/style.css`:

- **Colors**: Modify CSS variables in the `:root` section
- **Fonts**: Change the Google Fonts import and font-family
- **Animations**: Adjust keyframes and transition properties
- **Layout**: Modify grid, flexbox, and spacing properties

### Modifying Search Behavior

Edit `static/js/script.js`:

- **Debounce Delay**: Change the timeout value (default: 300ms)
- **Search Logic**: Modify the `performSearch()` function
- **Display Format**: Update the `createTalkCard()` function

## 🎨 Design Features

- **Color Scheme**: Google-inspired colors (Blue, Green, Yellow, Red)
- **Typography**: Inter font family for modern, clean look
- **Animations**: Fade-in-up animations with stagger effect
- **Glassmorphism**: Semi-transparent cards with backdrop blur
- **Gradients**: Smooth color transitions throughout
- **Hover Effects**: Interactive elements with smooth transitions
- **Responsive**: Mobile-first design with breakpoints at 768px and 480px

## 🔧 API Endpoints

The application provides the following REST API endpoints:

- `GET /` - Main page (renders HTML)
- `GET /api/talks` - Returns all talks as JSON
- `GET /api/speakers` - Returns all speakers as JSON
- `GET /api/search?q=query&category=1` - Search talks by query and/or category

### Example API Usage

```bash
# Get all talks
curl http://localhost:5000/api/talks

# Search by keyword
curl http://localhost:5000/api/search?q=machine

# Filter by category
curl http://localhost:5000/api/search?category=1

# Combined search
curl http://localhost:5000/api/search?q=cloud&category=2
```

## 🧪 Testing

### Manual Testing Checklist

- [ ] Home page loads correctly
- [ ] All 8 talks are displayed
- [ ] Lunch break is visually distinct
- [ ] Search by title works (e.g., "Machine Learning")
- [ ] Search by speaker works (e.g., "Sarah Chen")
- [ ] Category filter works (Category 1 and 2)
- [ ] Combined search and filter works
- [ ] LinkedIn links open correctly
- [ ] Responsive design works on mobile
- [ ] Animations play smoothly
- [ ] No console errors in browser

### Browser Compatibility

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📝 Technologies Used

### Backend
- **Python 3.x**: Programming language
- **Flask 3.0.0**: Web framework
- **Werkzeug 3.0.1**: WSGI utility library

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with variables, gradients, and animations
- **JavaScript (ES6+)**: Interactive functionality
- **Google Fonts**: Inter font family

## 🐛 Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
app.run(debug=True, port=5001)  # Change to any available port
```

### Module Not Found Error
Ensure you've activated the virtual environment and installed dependencies:
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Static Files Not Loading
Make sure the directory structure is correct:
- `static/css/style.css`
- `static/js/script.js`

### Search Not Working
Check browser console for JavaScript errors. Ensure the Flask server is running.

## 🚀 Deployment Options

### Option 1: Heroku
1. Create a `Procfile`:
   ```
   web: python app.py
   ```
2. Update `app.py` to use environment port:
   ```python
   import os
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
   ```

### Option 2: PythonAnywhere
1. Upload files to PythonAnywhere
2. Configure WSGI file to point to `app.py`
3. Set static files mapping

### Option 3: Docker
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 📄 License

This project is open source and available for educational purposes.

## 👥 Contributors

- Conference website developed for Google Cloud Tech Summit 2026
- Built with Flask and modern web technologies

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the API endpoints documentation
3. Inspect browser console for errors
4. Verify Flask server is running

---

**Enjoy the Google Cloud Tech Summit 2026!** 🎉
