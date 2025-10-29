# Professional Discord Bot

A feature-rich Discord bot with music playback, interactive games, and utility commands.

## Features

### 🎵 Music System
- High-quality music playback using Lavalink
- Support for YouTube, Spotify, SoundCloud
- Queue management with shuffle and loop
- Interactive music controls with buttons
- Auto-updating now playing embeds
- Volume control and track seeking

### 🎮 Interactive Games
- Minesweeper with customizable difficulty
- Rock Paper Scissors
- Trivia questions
- More games coming soon!

### 🛠️ General Commands
- Server information and statistics
- User information and avatars
- Moderation tools
- Audit log viewing
- Ping and uptime monitoring

## Quick Start

### Prerequisites
- Python 3.8+
- Discord Bot Token
- Lavalink Server (for music features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kwgdbeksb/discord-bot-professional.git
cd discord-bot-professional
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your bot token and configuration
```

4. Start Lavalink server (for music features):
```bash
java -jar Lavalink.jar
```

5. Run the bot:
```bash
python bot.py
```

## Configuration

Create a `.env` file with the following variables:

```env
DISCORD_TOKEN=your_bot_token_here
PREFIX=!
LAVALINK_URI=http://localhost:2333
LAVALINK_PASSWORD=youshallnotpass
MAX_QUEUE_SIZE=100
DEFAULT_VOLUME=50
```

## Commands

### Music Commands
- `/play <song>` - Play a song or add to queue
- `/pause` - Pause current track
- `/resume` - Resume playback
- `/skip` - Skip current track
- `/stop` - Stop playback and clear queue
- `/queue` - View current queue
- `/nowplaying` - Show current track info
- `/volume <1-100>` - Set playback volume
- `/shuffle` - Shuffle the queue
- `/remove <position>` - Remove track from queue
- `/disconnect` - Disconnect from voice channel

### General Commands
- `/ping` - Check bot latency
- `/serverinfo` - Display server information
- `/userinfo [user]` - Display user information
- `/avatar [user]` - Show user's avatar
- `/minesweeper` - Play Minesweeper game
- `/rps <choice>` - Play Rock Paper Scissors
- `/auditlog` - View server audit logs (Admin only)

## Recent Updates

### Skip Command Fix
- Fixed the skip command functionality
- Improved error handling for music playback
- Enhanced queue management
- Better user feedback for music operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, join our Discord server or create an issue on GitHub.

## Links

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Wavelink Documentation](https://wavelink.dev/)
- [Lavalink](https://github.com/freyacodes/Lavalink)