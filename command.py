import discord
from discord.ext import commands

# Create an instance of commands.Bot
intents = discord.Intents.default()
intents.members = True  # Enable the members intent if required
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
@commands.has_permissions(administrator=True)  # Only allow admins to use this command
async def age(ctx, action: str, member: discord.Member):
    # Check if the action is "verify"
    if action.lower() == "verify":
        # Get the "Verified" role (replace with the actual role name)
        role = discord.utils.get(ctx.guild.roles, name="Verified")
        
        if role:
            # Add the role to the user
            await member.add_roles(role)
            await ctx.send(f"✅ {member.mention} has been verified and given the 'Verified' role.")
        else:
            await ctx.send("❌ The 'Verified' role doesn't exist. Please contact an admin to create it.")
    else:
        await ctx.send("❌ Invalid action. Use '!age verify @user' to verify a user.")

