import discord
from discord.ext import commands
import asyncio
import logging
import os
from src.config import Config
from src.utils.logger import setup_logging
import wavelink

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

class DiscordBot(commands.Bot):
    """Main bot class with enhanced features."""
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.voice_states = True
        intents.guilds = True
        intents.members = True
        
        super().__init__(
            command_prefix=Config.PREFIX,
            intents=intents,
            help_command=None,
            case_insensitive=True,
            strip_after_prefix=True
        )
        
        self.config = Config()
        
    async def setup_hook(self):
        """Setup hook called when the bot is starting up."""
        logger.info("🤖 Setting up bot...")
        
        # Setup Wavelink nodes
        try:
            nodes = [
                wavelink.Node(
                    uri=self.config.LAVALINK_URI,
                    password=self.config.LAVALINK_PASSWORD,
                    identifier="main",
                    retries=3
                )
            ]
            await wavelink.Pool.connect(nodes=nodes, client=self, cache_capacity=100)
            logger.info("🎵 Wavelink connected successfully!")
        except Exception as e:
            logger.error(f"❌ Failed to connect to Lavalink: {e}")
            logger.warning("⚠️ Music features will be disabled")
        
        # Load cogs
        await self.load_cogs()
        
        # Sync commands
        try:
            synced = await self.tree.sync()
            logger.info(f"✅ Synced {len(synced)} command(s)")
        except Exception as e:
            logger.error(f"❌ Failed to sync commands: {e}")
    
    async def load_cogs(self):
        """Load all cogs."""
        cogs = [
            "src.cogs.music",
            "src.cogs.general",
        ]
        
        for cog in cogs:
            try:
                await self.load_extension(cog)
                logger.info(f"✅ Loaded cog: {cog}")
            except Exception as e:
                logger.error(f"❌ Failed to load cog {cog}: {e}")
    
    async def on_ready(self):
        """Called when the bot is ready."""
        logger.info(f"🚀 {self.user} is ready!")
        logger.info(f"📊 Connected to {len(self.guilds)} guilds")
        logger.info(f"👥 Serving {len(set(self.get_all_members()))} users")
        
        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.listening,
            name=f"{self.config.PREFIX}help | Music & Games"
        )
        await self.change_presence(activity=activity, status=discord.Status.online)
    
    async def on_command_error(self, ctx, error):
        """Global error handler."""
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("❌ You don't have permission to use this command!")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("❌ I don't have the required permissions!")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"⏰ Command is on cooldown. Try again in {error.retry_after:.2f} seconds.")
        else:
            logger.error(f"Unhandled error: {error}")
            await ctx.send("❌ An unexpected error occurred!")
    
    async def close(self):
        """Cleanup when bot is shutting down."""
        logger.info("🔄 Bot is shutting down...")
        
        # Disconnect from Wavelink
        try:
            await wavelink.Pool.close()
            logger.info("🎵 Wavelink disconnected")
        except Exception as e:
            logger.error(f"Error disconnecting Wavelink: {e}")
        
        await super().close()
        logger.info("👋 Bot shutdown complete")

def main():
    """Main function to run the bot."""
    bot = DiscordBot()
    
    try:
        bot.run(bot.config.TOKEN)
    except discord.LoginFailure:
        logger.error("❌ Invalid bot token!")
    except Exception as e:
        logger.error(f"❌ Failed to start bot: {e}")

if __name__ == "__main__":
    main()
