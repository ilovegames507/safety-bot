import discord
import datetime

users = {} 
# Dictionary to store user IDs and their birth dates

def get_user_age(birth_date):
    DOB = input("Enter your date of birth (YYYY-MM-DD): ")
    birth_date = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

DOB = input("Enter your date of birth (YYYY-MM-DD): ")
birth_date = datetime.datetime.strptime(DOB, "%Y-%m-%d").date()
age = get_user_age(birth_date)

if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Function to calculate age from birth date
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
def get_user_ID():
    # Ask the user to submit identification
    question = input("To prove you are an adult, submit an image of any identification proving your age, for example: passport, ID card, etc. ")

    # Ask if the user wants to submit an ID
    response = input("Do you want to submit any identification proving your age? (yes/no): ")

    # Check if the user responds positively
    if response.lower() == "yes":
        print("To protect your privacy, you may obscure your name, photo, and any other sensitive details. Only your date of birth needs to remain visible for age verification purposes. Please also include a handwritten note in the photo with your Discord username and today’s date.")
    else:
        print("You chose not to submit an identification.")

    async def send_image(ctx):
        await ctx.send(file=discord.File("path/to/your/image.png"))
        return "Image sent successfully please wait to staff review your post."
    
    failed = False  # Set to True if the image-sending operation fails
    if failed:
        print("Failed to send image. Please try again.")
    else:
        print("Image sent successfully. Please wait for staff review.")
    
    async def image(ctx):
        channel = ctx.bot.get_channel(1234567890)  
        if ctx.message.attachments:
            attachment = ctx.message.attachments[0]
            file = await attachment.to_file()
        else:
            return "No attachment found. Please attach an image."
        await channel.send(file=file)
        return "Image sent successfully please wait to staff review your post."
    
from discord.ext import commands

bot = commands.Bot(command_prefix="!")  # Initialize the bot with a command prefix

@bot.command()
async def failed_image(ctx):
    channel = ctx.bot.get_channel(1234567890)  # Replace with your staff/review channel ID

    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        file = await attachment.to_file()
        await channel.send(
            f"🚫 Re-submission from {ctx.author.mention} (ID: {ctx.author.id}):",
            file=file
        )
        await ctx.send(
            "📩 Your image has been re-submitted. Please wait while staff reviews it.\n\n"
            "✅ Make sure your **date of birth is clearly visible** and that you include a **handwritten note** stating:\n"
            "> *For verification purposes by [Your Server Name]. I confirm this is my ID and I'm over 18.*"
        )
    else:
        await ctx.send(" No attachment found. Please attach an image with your ID and the required note.")

        @bot.listener()
        async def image_verify():
           user =ctx.author
           channel = ctx.bot.get_channel(1234567890)  # Replace with your staff/review channel ID
           channel_id = 1234567890  # Replace with your staff/review channel ID
           print(f"Image sent successfully to {channel.name} channel.")

log_channel = bot.get_channel(1234567890)  # Replace 1234567890 with your log channel ID

if log_channel:
    async def log_verification(ctx, user):
        await log_channel.send(f"🔍 {user.mention} tried to verify with age `{age}`")
        if age >= 18:
            await ctx.send(f"{user.mention}, you're verified as 18 or older.")
        else:
            await ctx.send(f"{user.mention}, you must be at least 18 to verify.")
    
    # Wrap the call to log_verification in an async function
    async def execute_verification(ctx):
        user = ctx.author  # Define the user as the author of the context
        await log_verification(ctx, user)
    
    # Schedule the async function to run
    @bot.command()
    async def verify(ctx):
        await execute_verification(ctx)
    

    
