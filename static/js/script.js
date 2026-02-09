// Search and filter functionality
let allTalks = [];
let searchTimeout = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');

    // Load all talks initially
    loadTalks();

    // Add event listeners
    searchInput.addEventListener('input', handleSearch);
    categoryFilter.addEventListener('change', handleSearch);

    // Add stagger animation to talk cards
    animateTalkCards();
});

// Load all talks from the API
function loadTalks() {
    fetch('/api/talks')
        .then(response => response.json())
        .then(data => {
            allTalks = data;
        })
        .catch(error => {
            console.error('Error loading talks:', error);
        });
}

// Handle search with debouncing
function handleSearch() {
    clearTimeout(searchTimeout);

    searchTimeout = setTimeout(() => {
        const searchQuery = document.getElementById('searchInput').value.trim();
        const category = document.getElementById('categoryFilter').value;

        performSearch(searchQuery, category);
    }, 300);
}

// Perform the search
function performSearch(query, category) {
    const params = new URLSearchParams();

    if (query) {
        params.append('q', query);
    }

    if (category) {
        params.append('category', category);
    }

    // If no search criteria, show all talks
    if (!query && !category) {
        displayTalks(allTalks);
        return;
    }

    fetch(`/api/search?${params.toString()}`)
        .then(response => response.json())
        .then(data => {
            displayTalks(data);
        })
        .catch(error => {
            console.error('Error searching talks:', error);
        });
}

// Display talks in the schedule
function displayTalks(talks) {
    const scheduleContainer = document.getElementById('scheduleContainer');

    if (talks.length === 0) {
        scheduleContainer.innerHTML = `
            <div class="no-results">
                <h3>No sessions found</h3>
                <p>Try adjusting your search criteria</p>
            </div>
        `;
        return;
    }

    scheduleContainer.innerHTML = talks.map(talk => createTalkCard(talk)).join('');
    animateTalkCards();
}

// Create HTML for a talk card
function createTalkCard(talk) {
    const isLunchBreak = talk.id === 4;
    const categoryClass = talk.category ? `category-${talk.category}` : '';

    let speakersHTML = '';
    if (talk.speakers && talk.speakers.length > 0) {
        speakersHTML = `
            <div class="speakers">
                ${talk.speakers.map(speaker => `
                    <div class="speaker">
                        <div class="speaker-avatar">
                            ${speaker.first_name[0]}${speaker.last_name[0]}
                        </div>
                        <div class="speaker-info">
                            <div class="speaker-name">${speaker.first_name} ${speaker.last_name}</div>
                            <a href="${speaker.linkedin}" target="_blank" class="speaker-linkedin">
                                <svg class="linkedin-icon" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                                </svg>
                                LinkedIn
                            </a>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    let categoryHTML = '';
    if (talk.category) {
        categoryHTML = `<div class="talk-category ${categoryClass}">Category ${talk.category}</div>`;
    }

    return `
        <div class="talk-card ${isLunchBreak ? 'lunch-break' : ''}" data-talk-id="${talk.id}">
            <div class="talk-time">${talk.time}</div>
            <div class="talk-content">
                <h3 class="talk-title">${talk.title}</h3>
                ${categoryHTML}
                <p class="talk-description">${talk.description}</p>
                ${speakersHTML}
            </div>
        </div>
    `;
}

// Animate talk cards with stagger effect
function animateTalkCards() {
    const cards = document.querySelectorAll('.talk-card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });
}

// Smooth scroll to top
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Add scroll to top button functionality
window.addEventListener('scroll', function () {
    const scrollButton = document.getElementById('scrollToTop');
    if (scrollButton) {
        if (window.pageYOffset > 300) {
            scrollButton.style.display = 'block';
        } else {
            scrollButton.style.display = 'none';
        }
    }
});
