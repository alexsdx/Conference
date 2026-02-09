from flask import Flask, render_template, jsonify, request
from datetime import datetime, time
import json

app = Flask(__name__)

# Conference data
CONFERENCE_DATA = {
    'name': 'Google Cloud Tech Summit 2026',
    'date': 'March 15, 2026',
    'location': 'San Francisco Convention Center, CA',
    'description': 'A one-day technical conference exploring the latest in Google Cloud Technologies'
}

# Speakers data
SPEAKERS = [
    {
        'id': 1,
        'first_name': 'Sarah',
        'last_name': 'Chen',
        'linkedin': 'https://www.linkedin.com/in/sarahchen'
    },
    {
        'id': 2,
        'first_name': 'Michael',
        'last_name': 'Rodriguez',
        'linkedin': 'https://www.linkedin.com/in/michaelrodriguez'
    },
    {
        'id': 3,
        'first_name': 'Emily',
        'last_name': 'Johnson',
        'linkedin': 'https://www.linkedin.com/in/emilyjohnson'
    },
    {
        'id': 4,
        'first_name': 'David',
        'last_name': 'Kim',
        'linkedin': 'https://www.linkedin.com/in/davidkim'
    },
    {
        'id': 5,
        'first_name': 'Jessica',
        'last_name': 'Martinez',
        'linkedin': 'https://www.linkedin.com/in/jessicamartinez'
    },
    {
        'id': 6,
        'first_name': 'Robert',
        'last_name': 'Thompson',
        'linkedin': 'https://www.linkedin.com/in/robertthompson'
    },
    {
        'id': 7,
        'first_name': 'Amanda',
        'last_name': 'Lee',
        'linkedin': 'https://www.linkedin.com/in/amandalee'
    },
    {
        'id': 8,
        'first_name': 'James',
        'last_name': 'Wilson',
        'linkedin': 'https://www.linkedin.com/in/jameswilson'
    },
    {
        'id': 9,
        'first_name': 'Lisa',
        'last_name': 'Anderson',
        'linkedin': 'https://www.linkedin.com/in/lisaanderson'
    },
    {
        'id': 10,
        'first_name': 'Daniel',
        'last_name': 'Brown',
        'linkedin': 'https://www.linkedin.com/in/danielbrown'
    },
    {
        'id': 11,
        'first_name': 'Rachel',
        'last_name': 'Foster',
        'linkedin': 'https://www.linkedin.com/in/rachelfoster'
    },
    {
        'id': 12,
        'first_name': 'Kevin',
        'last_name': 'Zhang',
        'linkedin': 'https://www.linkedin.com/in/kevinzhang'
    }
]

# Talks data
TALKS = [
    {
        'id': 1,
        'title': 'Keynote: The Future of Cloud Computing',
        'speaker_ids': [1],
        'category': 1,
        'description': 'Explore the cutting-edge innovations in cloud computing and how Google Cloud is shaping the future of technology infrastructure.',
        'time': '09:00 AM - 10:00 AM'
    },
    {
        'id': 2,
        'title': 'Building Scalable Applications with Google Kubernetes Engine',
        'speaker_ids': [2, 3],
        'category': 1,
        'description': 'Learn best practices for deploying and managing containerized applications at scale using GKE.',
        'time': '10:15 AM - 11:15 AM'
    },
    {
        'id': 3,
        'title': 'Machine Learning on Google Cloud Platform',
        'speaker_ids': [4],
        'category': 2,
        'description': 'Discover how to leverage Google Cloud\'s ML tools including Vertex AI, AutoML, and TensorFlow for your AI projects.',
        'time': '11:30 AM - 12:30 PM'
    },
    {
        'id': 4,
        'title': 'Lunch Break',
        'speaker_ids': [],
        'category': None,
        'description': 'Networking lunch with fellow attendees',
        'time': '12:30 PM - 01:30 PM'
    },
    {
        'id': 5,
        'title': 'Serverless Architecture with Cloud Functions and Cloud Run',
        'speaker_ids': [5, 6],
        'category': 1,
        'description': 'Deep dive into building event-driven, serverless applications that scale automatically.',
        'time': '01:30 PM - 02:30 PM'
    },
    {
        'id': 6,
        'title': 'Data Analytics with BigQuery and Looker',
        'speaker_ids': [7],
        'category': 2,
        'description': 'Transform your data into actionable insights using Google Cloud\'s powerful analytics platform.',
        'time': '02:45 PM - 03:45 PM'
    },
    {
        'id': 7,
        'title': 'Security Best Practices for Google Cloud',
        'speaker_ids': [8, 9],
        'category': 1,
        'description': 'Learn how to implement robust security measures and compliance frameworks in your cloud infrastructure.',
        'time': '04:00 PM - 05:00 PM'
    },
    {
        'id': 8,
        'title': 'Cloud Migration Strategies and Success Stories',
        'speaker_ids': [10],
        'category': 2,
        'description': 'Real-world case studies and proven strategies for successful cloud migration projects.',
        'time': '05:15 PM - 06:15 PM'
    }
]

def get_speaker_by_id(speaker_id):
    """Get speaker details by ID"""
    return next((s for s in SPEAKERS if s['id'] == speaker_id), None)

def format_talk(talk):
    """Format talk with speaker details"""
    formatted_talk = talk.copy()
    formatted_talk['speakers'] = [get_speaker_by_id(sid) for sid in talk['speaker_ids']]
    return formatted_talk

@app.route('/')
def index():
    """Render the home page"""
    talks = [format_talk(talk) for talk in TALKS]
    return render_template('index.html', 
                         conference=CONFERENCE_DATA, 
                         talks=talks)

@app.route('/api/search')
def search():
    """Search talks by category, speaker, or title"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', '')
    
    results = []
    
    for talk in TALKS:
        # Skip lunch break from search results
        if talk['id'] == 4:
            continue
            
        match = False
        
        # Search by category
        if category and talk['category'] == int(category):
            match = True
        
        # Search by title
        if query and query in talk['title'].lower():
            match = True
        
        # Search by speaker name
        if query:
            for speaker_id in talk['speaker_ids']:
                speaker = get_speaker_by_id(speaker_id)
                if speaker:
                    full_name = f"{speaker['first_name']} {speaker['last_name']}".lower()
                    if query in full_name:
                        match = True
                        break
        
        if match or (not query and not category):
            results.append(format_talk(talk))
    
    return jsonify(results)

@app.route('/api/talks')
def get_talks():
    """Get all talks"""
    talks = [format_talk(talk) for talk in TALKS]
    return jsonify(talks)

@app.route('/api/speakers')
def get_speakers():
    """Get all speakers"""
    return jsonify(SPEAKERS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
