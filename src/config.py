import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Discord bot."""
    
    # Bot Configuration
    TOKEN = os.getenv('DISCORD_TOKEN')
    PREFIX = os.getenv('PREFIX', '!')
    
    # Lavalink Configuration
    LAVALINK_URI = os.getenv('LAVALINK_URI', 'http://localhost:2333')
    LAVALINK_PASSWORD = os.getenv('LAVALINK_PASSWORD', 'youshallnotpass')
    
    # Database Configuration (if needed)
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    # API Keys (if needed)
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    # Bot Settings
    MAX_QUEUE_SIZE = int(os.getenv('MAX_QUEUE_SIZE', '100'))
    DEFAULT_VOLUME = int(os.getenv('DEFAULT_VOLUME', '50'))
    
    @classmethod
    def validate(cls):
        """Validate required configuration."""
        if not cls.TOKEN:
            raise ValueError("DISCORD_TOKEN is required!")
        
        return True
