# Recovery Inequity Dashboard

## Overview
Recovery Inequity Dashboard is a full-stack health analytics application built for the Dartmouth DALI Lab “Choose Your Own Adventure” Challenge.

The project explores how wearable-device health metrics can be visualized and analyzed to better understand recovery patterns, circadian rhythm consistency, and activity-health relationships over time.

The dashboard processes exported wearable-device data and presents interactive visualizations of:
- Heart rate trends
- Daily step counts
- Recovery and activity relationships
- Circadian rhythm patterns
- Longitudinal wellness metrics

This project was developed using Python and Streamlit, technologies that were new to me when starting the project.

---

## Live Application
[Insert Streamlit Deployment Link Here]

---

## Features
- Interactive health analytics dashboard
- Dynamic filtering and visualization
- XML and CSV data processing
- Time-series wellness analysis
- Responsive frontend using Streamlit
- Backend data processing using Python and Pandas

---

## Tech Stack

### Frontend
- Streamlit
- Plotly

### Backend
- Python
- Pandas
- XML parsing with ElementTree

### Data Sources
- Wearable-device export data
- CSV health datasets
- XML health export files

---

## Learning Journey

### Inspiration
I wanted to build a project that combined health analytics, data visualization, and software engineering. I was especially interested in how wearable-device data can reveal patterns in recovery, activity, and circadian rhythm consistency.

### Potential Impact
This type of dashboard could help users better understand how sleep, activity, and recovery interact over time. It could also support more accessible personal health tracking and encourage data-driven wellness habits.

### New Technologies Learned
For this project, I learned:
- Streamlit for building interactive web apps
- Plotly for dynamic visualizations
- GitHub deployment workflows
- Streamlit Cloud deployment

I chose Streamlit because it allowed rapid development of an interactive full-stack dashboard entirely in Python.

---

## Technical Rationale

### Architecture
The frontend and backend are integrated through Streamlit. The backend processes XML and CSV health data using Python and Pandas, while the frontend dynamically renders interactive visualizations.

### Technical Tradeoffs
One major tradeoff was choosing Streamlit instead of a more traditional React + Flask architecture. Streamlit simplified development and deployment, but it provides less frontend customization.

### Most Difficult Bug
One difficult issue involved deployment errors caused by missing files and ignored Git-tracked files. I debugged this by checking repository contents, updating `.gitignore`, and verifying deployment dependencies on Streamlit Cloud.

---

## AI Usage
I used ChatGPT during development to help debug GitHub deployment issues, Streamlit configuration problems, and repository setup.

Example prompt:
> “Why is Streamlit saying ModuleNotFoundError for Plotly even though it’s in requirements.txt?”

I still needed to manually debug dependency installation issues, correct file paths, and properly configure Git tracking for deployment.

---

## Setup Instructions

### Clone Repository
```bash
git clone https://github.com/pocketnuggets/recovery-inequity-dashboard.git
cd recovery-inequity-dashboard
