import discord
from discord.ext import commands

class Buttons(discord.ui.View):
    def __intit__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Click me", style=discord.ButtonStyle.gray)
    async def buttonTest(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello!")

class ClickMe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Click me cog loaded")

    @commands.command()
    async def click(self, ctx):
        await ctx.send("Message with a button", view=Buttons())

async def setup(bot):
    await bot.add_cog(ClickMe(bot))