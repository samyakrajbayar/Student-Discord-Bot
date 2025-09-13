# 🎓 StudyMentor Discord Bot

**An AI-powered Discord bot that transforms student productivity through smart academic planning, peer mentorship, and personalized tutoring.**

## 🌟 Overview

StudyMentor is a comprehensive Discord bot designed to help high school and college students excel academically while building meaningful peer connections. It combines cutting-edge AI tutoring, smart scheduling, and community-driven mentorship in one powerful platform.

### 🎯 **Perfect for College Applications**
This project demonstrates technical excellence, social impact, and leadership—key qualities that Ivy League and MIT admissions look for. The bot generates measurable impact data that strengthens your application portfolio.

---

## ✨ Features

### 🤖 **AI-Powered Tutoring**
- Step-by-step problem solving across all subjects
- Personalized quiz generation (SAT, AP, Subject-specific)
- Adaptive difficulty based on student level
- Instant feedback and explanations

### 📅 **Smart Academic Planner**
- Integrated task management with priority levels
- Google Calendar synchronization
- Automated deadline reminders
- Study session tracking and analytics

### 🎤 **Interview Preparation**
- Mock college admission interviews
- AI-driven feedback on responses
- Progress tracking and improvement metrics
- Real-time confidence building

### 🤝 **Peer Mentorship Network**
- Anonymous help request system
- Skill-based mentor matching
- Gamified point system for helpers
- Community achievement badges

### 📊 **Progress Analytics**
- Comprehensive user profiles with leveling
- Study time tracking and visualization
- Performance metrics across subjects
- Exportable reports for applications

### 🏆 **Community Features**
- Subject-specific study groups
- Leaderboards and competitions
- Daily motivational content
- Peer recognition system

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Discord Bot Token
- Replit Account (recommended) or local environment

### 1. **Replit Deployment** (Recommended)
```bash
# 1. Fork this repository to Replit
# 2. Install dependencies (automatic)
# 3. Set environment variables in Secrets tab
# 4. Click Run!
```

### 2. **Local Development**
```bash
# Clone the repository
git clone https://github.com/yourusername/studymentor-bot.git
cd studymentor-bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export DISCORD_BOT_TOKEN=your_token_here
export OPENAI_API_KEY=your_openai_key_here  # Optional

# Run the bot
python main.py
```

### 3. **Environment Variables**

**Required:**
```env
DISCORD_BOT_TOKEN=your_discord_bot_token
```

**Optional (Enhanced Features):**
```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_notion_db_id
```

---

## 📖 Usage Guide

### **Getting Started Commands**
```bash
!study register junior Harvard, MIT, Stanford    # Set up your profile
!study help                                      # View all commands
!study profile                                   # Check your progress
```

### **Core Features**
```bash
# AI Tutoring
!study tutor How do I solve quadratic equations?
!study quiz math medium

# Task Management  
!study plan add Math Homework | Complete Chapter 5 | 2024-01-15
!study plan list

# Study Tracking
!study study 60 calculus                        # Log 60 minutes of calculus

# Interview Practice
!study interview                                 # Get a practice question

# Mentorship
!study mentor request physics Need help with momentum problems
```

### **Analytics & Progress**
```bash
!study stats           # View server-wide impact metrics
!study leaderboard     # See top performers
!study profile @user   # Check someone's progress
```

---

## 🏗️ Architecture

### **Tech Stack**
- **Backend:** Python 3.8+ with discord.py
- **Database:** SQLite (production-ready, no setup required)
- **AI Integration:** OpenAI GPT-3.5-turbo
- **APIs:** Google Calendar, Notion, Discord
- **Hosting:** Replit (recommended) or any Python environment

### **Core Components**
```
studymentor-bot/
├── main.py                     # Main bot file with all commands
├── google_calendar.py          # Google Calendar integration
├── notion_integration.py       # Notion API integration
├── requirements.txt            # Python dependencies
├── .replit                     # Replit configuration
├── SETUP_GUIDE.md             # Detailed setup instructions
└── README.md                  # This file
```

### **Database Schema**
- **users:** Profile data, progress tracking, preferences
- **study_sessions:** Time tracking, subject analytics
- **tasks:** Assignment management, deadlines
- **mentorship_requests:** Peer help system
- **interview_practice:** Mock interview history

---

## 🔧 Advanced Configuration

### **Google Calendar Integration**
1. Enable Google Calendar API in Google Cloud Console
2. Create service account credentials
3. Add `GOOGLE_API_KEY` to environment variables
4. Bot automatically syncs study sessions and deadlines

### **Notion Integration**
1. Create Notion integration at notion.so/my-integrations
2. Set up a database for task management
3. Add `NOTION_TOKEN` and `NOTION_DATABASE_ID`
4. Enable automatic task syncing

### **OpenAI Enhancement**
1. Get API key from platform.openai.com
2. Add `OPENAI_API_KEY` to environment
3. Unlock advanced AI tutoring capabilities

---

## 🎯 College Application Integration

### **Building Your Portfolio**
1. **Technical Skills:** Python, APIs, Database Design, AI Integration
2. **Leadership:** Community building, student mentorship
3. **Impact:** Quantifiable improvements in student outcomes
4. **Innovation:** Novel approach to educational technology

### **Documentation for Applications**
- Export usage statistics with `!study stats`
- Screenshot community engagement
- Document technical challenges overcome
- Gather testimonials from helped students

### **Scaling Strategy**
1. **Phase 1:** Deploy in your school's Discord (10-50 users)
2. **Phase 2:** Expand to neighboring schools (100-500 users)
3. **Phase 3:** Launch on educational Discord servers (1000+ users)
4. **Phase 4:** Partner with educational organizations

---

### **For Developers**
```bash
# Fork the repository
git fork https://github.com/yourusername/studymentor-bot

# Create feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m 'Add amazing feature'

# Push to branch
git push origin feature/amazing-feature

# Open a Pull Request
```

### **Development Priorities**
- [ ] Mobile app companion
- [ ] Advanced AI tutoring models
- [ ] Real-time collaboration features
- [ ] Integration with learning management systems
- [ ] Multi-language support

---

## If you cant tell, I used Chatgpt for the readme File lol
