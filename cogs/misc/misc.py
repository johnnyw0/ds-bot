import discord
import random
import time
from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def alert(self, ctx, user: discord.User,*, content):
        print(f"Alert called by user {user} with content {content}")
        try:
            await user.send(content)
        except discord.HTTPException:
            await ctx.send("Você precisa especificar o destinatário da mensagem.")

            
    @commands.command()
    async def ban(self, ctx, qtd):
        await ctx.send("Escolhendo usuários que vão morrer...")
        time.sleep(1)


        ####### Instancia o servidor e escolhe aleatoriamente entre os membros quais poderão ser banidos
        guild = ctx.guild
        members = []
        for member in guild.members:
            print(member)
            members.append(member)
        qtd1 = int(qtd)
        ban = random.sample(members, qtd1)


        ###### Escolhe o membro que será banido
        await ctx.send(f"Um desses {qtd} membros será banido:")
        for member in ban:
            await ctx.send(member.global_name if member.global_name != None else member.name)

        usuario_escolhido = random.choice(ban)
        await ctx.send(f"Usuário escolhido: {usuario_escolhido.global_name if usuario_escolhido.global_name != None else usuario_escolhido.name}")
        #try:
        #    await guild.kick(usuario_escolhido)
        #except discord.Forbidden:
        #    await ctx.send("Não tenho permissão para banir esse usuário")




async def setup(bot):
    print("carregando cog no bot\n")
    await bot.add_cog(Misc(bot))
    print("cog carregada no bot\n")