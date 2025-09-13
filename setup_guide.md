# StudyMentor Discord Bot - Complete Setup Guide 🎓

## 🚀 Quick Start for Replit

### 1. Create Your Replit Project
1. Go to [Replit.com](https://replit.com)
2. Click "Create Repl"
3. Choose "Python" template
4. Name it "StudyMentor-Bot"
5. Upload all the provided files to your Repl

### 2. Set Up Discord Bot
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" → Name it "StudyMentor"
3. Go to "Bot" tab → Click "Add Bot"
4. Under "Token" → Click "Copy" (save this token!)
5. Enable these permissions:
   - Send Messages
   - Read Message History
   - Use Slash Commands
   - Add Reactions
   - Embed Links
   - Manage Messages

### 3. Configure Environment Variables in Replit
Go to the 🔒 **Secrets** tab in Replit and add:

**Required:**
```
DISCORD_BOT_TOKEN = your_discord_bot_token_here
```

**Optional (for enhanced features):**
```
OPENAI_API_KEY = your_openai_api_key_here
GOOGLE_API_KEY = your_google_api_key_here
NOTION_TOKEN = your_notion_integration_token_here
NOTION_DATABASE_ID = your_notion_database_id_here
```

### 4. Install Dependencies
In the Replit Shell, run:
```bash
pip install -r requirements.txt
```

### 5. Run Your Bot
Click the green "▶ Run" button in Replit!

### 6. Invite Bot to Your Server
1. In Discord Developer Portal → "OAuth2" → "URL Generator"
2. Select scopes: `bot`, `applications.commands`
3. Select permissions: `Send Messages`, `Read Message History`, `Use Slash Commands`, `Add Reactions`, `Embed Links`
4. Copy the generated URL and open it
5. Select your server and authorize!

## 🔧 Optional Integrations

### Google Calendar Integration
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create new project → Enable Calendar API
3. Create credentials (Service Account or OAuth 2.0)
4. Add your credentials to Replit Secrets
5. The bot will automatically sync study sessions and deadlines!

### OpenAI Integration (AI Tutoring)
1. Get API key from [OpenAI](https://platform.openai.com/api-keys)
2. Add `OPENAI_API_KEY` to Replit Secrets
3. Users can now get AI tutoring with `!study tutor <question>`

### Notion Integration
1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Create new integration → Copy Internal Integration Token
3. Create a database in Notion for tasks
4. Share the database with your integration
5. Add `NOTION_TOKEN` and `NOTION_DATABASE_ID` to Secrets

## 📊 Bot Commands Overview

### 👤 Profile & Setup
- `!study register [grade] [colleges]` - Set up profile
- `!study profile [@user]` - View study profile

### 🤖 AI Tutoring
- `!study tutor <question>` - Get AI tutoring help
- `!study quiz <subject>` - Practice quizzes

### 📅 Planning & Tracking
- `!study plan add <task> | <description> | <due_date>`
- `!study plan list` - View tasks
- `!study study <minutes> <subject>` - Log study time

### 🎤 Interview & Mentorship
- `!study interview` - Practice interviews
- `!study mentor request <subject> <description>`

### 📊 Analytics
- `!study stats` - Server statistics
- `!study leaderboard [category]` - View leaderboards

## 🎯 Impact Measurement Features

### For Your College Applications
The bot automatically tracks:
- **Total study hours logged by users**
- **Number of active student users**
- **Quiz attempts and improvements**
- **Mentorship connections facilitated**
- **Interview practice sessions completed**

Use `!study stats` to generate impact reports showing:
- Students helped
- Total study time facilitated
- Academic improvements
- Community engagement metrics

## 🚀 Scaling & Community Building

### Growing Your User Base
1. **Start with your school's Discord server**
2. **Share in study groups and academic communities**
3. **Create dedicated channels for different subjects**
4. **Host study sessions and use the bot to track progress**

### Advanced Features to Add Later
- **SAT/ACT practice tests with scoring**
- **College application deadline tracking**
- **Peer matching algorithm for study buddies**
- **Achievement badges and gamification**
- **Export data for college applications**

## 🛠️ Troubleshooting

### Common Issues:

**Bot not responding:**
- Check that DISCORD_BOT_TOKEN is set correctly
- Ensure bot has proper permissions in your server
- Check Replit logs for error messages

**AI features not working:**
- Verify OPENAI_API_KEY is valid
- Check your OpenAI account has credits
- Bot will fall back to rule-based responses

**Database errors:**
- The bot creates SQLite database automatically
- If issues persist, delete `studymentor.db` file and restart

### Getting Help:
1. Check Replit console for error messages
2. Verify all environment variables are set
3. Test bot commands in a private server first
4. Make sure bot has administrator permissions initially

## 📈 Measuring Success for College Apps

### Key Metrics to Track:
1. **User Engagement**: Active daily/weekly users
2. **Academic Impact**: Study hours logged, quiz scores
3. **Community Building**: Mentorship connections made
4. **Technical Growth**: Features added, uptime maintained
5. **Leadership**: How you grew and managed the community

### Creating Impact Reports:
Use the `!study stats` command regularly to document:
- Growth in user base over time
- Total study hours facilitated
- Success stories from users
- Technical challenges overcome

This data becomes powerful evidence of your leadership, technical skills, and positive impact for college applications!

## 🌟 Next Steps

1. **Deploy and test all basic features**
2. **Invite 10-20 initial users from your school**
3. **Gather feedback and iterate**
4. **Add advanced features based on user needs**
5. **Document your impact for college applications**
6. **Scale to other schools and communities**

**Good luck building the future of student productivity! 🚀📚**