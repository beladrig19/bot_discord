import discord
from discord.ext import commands

# Définir les intents nécessaires
intents = discord.Intents.default()

# Activer les intents pour les membres et les messages
intents.members = True
intents.messages = True

# Initialise le bot
bot = commands.Bot(command_prefix='!', description='bot pour 14443b tags', intents=intents)



# Fonction pour simuler une utilisation des blocs 5 et 6
def simulate_utilisation(block5, block6, utilisations):
    # On ajuste le nombre d'itérations en fonction du nombre d'utilisations moins 1
    for _ in range(utilisations - 1):
        # Swap endianness pour les blocs 5 et 6
        block5_swapped = block5[6:] + block5[4:6] + block5[2:4] + block5[:2]
        block6_swapped = block6[6:] + block6[4:6] + block6[2:4] + block6[:2]
        
        # Décrémenter le bloc 5 de 2
        block5_swapped = hex(int(block5_swapped, 16) - 2)[2:].upper().zfill(8)
        # Décrémenter le bloc 6 de 2
        block6_swapped = hex(int(block6_swapped, 16) - 2)[2:].upper().zfill(8)
        
        # Re-swap endianness pour les blocs 5 et 6
        block5 = block5_swapped[6:] + block5_swapped[4:6] + block5_swapped[2:4] + block5_swapped[:2]
        block6 = block6_swapped[6:] + block6_swapped[4:6] + block6_swapped[2:4] + block6_swapped[:2]
    return block5, block6


# Commande pour demander le nombre d'utilisations et afficher les valeurs mises à jour
@bot.command()
async def update_blocks(ctx):
    # Demander le nombre d'utilisations à l'utilisateur
    await ctx.send("Combien de fois avez-vous utilisé la carte ?")
    utilisations_response = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    utilisations = int(utilisations_response.content)

    # Demander les valeurs des blocs 5 et 6 à l'utilisateur
    await ctx.send("Entrez la valeur du bloc 5 :")
    block5_response = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    block5_value = block5_response.content

    await ctx.send("Entrez la valeur du bloc 6 :")
    block6_response = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
    block6_value = block6_response.content

    # Appeler la fonction pour simuler une utilisation des blocs 5 et 6
    block5_updated, block6_updated = simulate_utilisation(block5_value, block6_value, utilisations)

    # Afficher les valeurs mises à jour
    await ctx.send(f"Valeur du bloc 5 après {utilisations} utilisation(s) : {block5_updated}")
    await ctx.send(f"Valeur du bloc 6 après {utilisations} utilisation(s) : {block6_updated}")




# Lancement du bot
bot.run('MTIxMTIxNjkzNzEzNzM0MDQ0Ng.G3W44Q.OHiqDItrngL_DMUd17L1Xuqn_Ah9niLpsiO92w')
