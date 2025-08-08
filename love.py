import discord
from discord.ext import commands
import random
import os
from keep_alive import keep_alive
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập dưới tên {bot.user}")


# Gửi tin nhắn ẩn danh
@bot.command()
async def guiandanh(ctx, member: discord.Member, *, message):
    try:
        await member.send(f"📩 Bạn nhận được một tin nhắn ẩn danh:\n\n{message}")
        await ctx.message.delete()
        await ctx.send("✅ Tin nhắn ẩn danh đã được gửi!", delete_after=3)
    except:
        await ctx.send("❌ Không thể gửi tin nhắn (có thể họ tắt DM).", delete_after=3)

# Hôn
@bot.command()
async def hon(ctx, member: discord.Member):
    gifs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/G3va31oEEnIkM/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/zkppEMFvRX5FC/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/MQVpBqASxSlFu/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wOtkVwroA6yzK/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QGc8RgRvMonFm/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/iseq9MQgxo4aQ/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bm2O3nXTcKJeU/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTc2d2RpOTBsMWFucWUwMGRwaXVvNTU3ZnEydDcyOXhvcnk5dGV6ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XZYxeRlIEdmKI/giphy.gif",
    ]
    embed = discord.Embed(description=f"💋 {ctx.author.mention} vừa hôn {member.mention} thật nồng nhiệt!", color=0xFF69B4)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

# Ôm
@bot.command()
async def om(ctx, member: discord.Member):
    gifs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3o3dGxzaXI0aDJlMTV1aGQyYndpeHIzM2JhajJsaWd6YzJhd3NhdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QFPoctlgZ5s0E/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3o3dGxzaXI0aDJlMTV1aGQyYndpeHIzM2JhajJsaWd6YzJhd3NhdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QFPoctlgZ5s0E/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3o3dGxzaXI0aDJlMTV1aGQyYndpeHIzM2JhajJsaWd6YzJhd3NhdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IRUb7GTCaPU8E/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3o3dGxzaXI0aDJlMTV1aGQyYndpeHIzM2JhajJsaWd6YzJhd3NhdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/49mdjsMrH7oze/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3o3dGxzaXI0aDJlMTV1aGQyYndpeHIzM2JhajJsaWd6YzJhd3NhdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/JUwliZWcyDmTQZ7m9L/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dHF6eXFjZjlyeDg1c3hhODMzdWJsNTBpMjlxYjd1cWJma3hhYXptNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/NgA5xoalnq0RlBLAnq/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Yjc1ZzJnMDhhcG0zeWNvbDNxc3lkYm4wbjBvZ2x4d2VwaXh6bnludyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ZnBrkqoaI2hq/giphy.gif",
    ]
    embed = discord.Embed(description=f"🤗 {ctx.author.mention} ôm chặt {member.mention} đầy yêu thương!", color=0xFFB6C1)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

# Thích
@bot.command()
async def thich(ctx, member: discord.Member):
    gifs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjFlb2FvbDBtcHVwN2U3OTdyN2o3cXlsNTZqbGtxaXI2cHlpNzhqNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/klmpEcFgXzrYQ/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjFlb2FvbDBtcHVwN2U3OTdyN2o3cXlsNTZqbGtxaXI2cHlpNzhqNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/HPI9m7McNPGN2/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjFlb2FvbDBtcHVwN2U3OTdyN2o3cXlsNTZqbGtxaXI2cHlpNzhqNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/XTK2z2iSD3tmw/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGl0d3F6NXhhbzZxajRvcXdrYzhnZGNiOXFvMXlnODQ2dGdzbGp6diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/obkyxZcD6mDSt01QjQ/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjFlb2FvbDBtcHVwN2U3OTdyN2o3cXlsNTZqbGtxaXI2cHlpNzhqNiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nmSUITmMlQvII/giphy.gif",
    ]
    embed = discord.Embed(description=f"😍 {ctx.author.mention} thích {member.mention} lắm luôn!", color=0xFFD700)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

# Tặng hoa
@bot.command()
async def tanghoa(ctx, member: discord.Member):
    gifs = [
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjFzaWw0YXJsdW1xeHplb241NWsyMG9nMmo5bHhnb2hwcWZuMnluNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PY3jUxrRsQVdx9CyFC/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjFzaWw0YXJsdW1xeHplb241NWsyMG9nMmo5bHhnb2hwcWZuMnluNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9orhOjh6QOD2BY6ZPi/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjFzaWw0YXJsdW1xeHplb241NWsyMG9nMmo5bHhnb2hwcWZuMnluNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/138Vem0XgW0Yzxm5QA/giphy.gif",
    ]
    embed = discord.Embed(description=f"💐 {ctx.author.mention} gửi tặng {member.mention} một bó hoa xinh đẹp!", color=0xFF69B4)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

# Thính ngẫu nhiên 20 câu
@bot.command()
async def thinh(ctx):
    list_thinh = [
        "Em có biết tại sao trời mưa không? Vì anh đang nhớ em.",
        "Nếu nụ cười của em là nắng, thì anh muốn làm bầu trời.",
        "Anh không giỏi toán, nhưng anh biết chúng ta = perfect.",
        "Nhà em có bán rượu không? Sao em nhìn anh say quá vậy.",
        "Trời hôm nay đẹp thế, nhưng không đẹp bằng em.",
        "Nếu em là trà sữa, anh sẽ là ống hút để ở bên em mãi.",
        "Anh muốn làm Google, vì em tìm gì anh cũng có.",
        "Em ơi, anh bị bệnh rồi... bệnh tương tư.",
        "Em có biết vì sao anh thích mưa không? Vì mỗi lần mưa em lại ở gần anh.",
        "Nếu anh là nhạc, em sẽ là lời, để ta mãi bên nhau.",
        "Trái đất tròn, nên kiểu gì anh cũng gặp được em.",
        "Nhìn em, anh thấy ngày mai đáng sống hơn.",
        "Anh muốn làm ly cà phê sáng, để em nhớ đến mỗi ngày.",
        "Nếu anh là gió, em có cho anh được ôm trọn em không?",
        "Em như ánh trăng, dịu dàng mà sáng mãi trong anh.",
        "Tim anh hôm nay như biển lớn, chỉ chờ em thả neo.",
        "Nếu anh là hoa, em chính là ánh nắng.",
        "Em làm anh quên mất cả mật khẩu WiFi.",
        "Anh không cần bản đồ, vì đã lạc vào tim em.",
        "Nếu yêu em là sai, anh không muốn đúng."
    ]
    gifs = [
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzgxbm5oNDU3N3YwcWNzOXAxb2JrNmdvY3FuNmQ4MGp1dnVzcXAwdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bqSkJ4IwNcoZG/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3BxcXR2dWNtMjBjcXNlc2s5dXhwbGhtMjd3YTlqdnp6bTl3MDQxayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bfEOX1UuyCqVq/giphy.gif",
        "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3gzMno2aGc3b3Zoamd0ZnlnZzB5M295bXFtdGdhamF2bXhxeWdzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wkW0maGDN1eSc/giphy.gif",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2s0bGdxNmducGtrMW14amdwajNwMTBsNHR5NnQ4NmR6anVoNG81eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VpcYdQpElriNy/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3dXd3bXd0cnhhczFmajVjbWlnOG5mNHJib2oybXA0cmdweDluZHMydyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/UrPxdGW62TDtS/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3azdxZ2YwY2R3cmJpaTd3NTVibzNrbmFwcTNxM3M3Z3FxaHZsZHdjdSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/BkqSYWqv8Zfva/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NmJ1bHJ3ZWgzeXp6cGNxaHY0bWdhZGZnemJmaWpyNjdlbGpyNHM5aiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/68MmLuvSQ60Vy/giphy.gif",
        "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bGk0b2pzbnkwdDgwbjZid3h2eXV0NnQ3enQweGplNHJueWM1aXRqbSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/iiahzvZJk2sPYbSbuy/giphy.gif",
    ]
    embed = discord.Embed(description=random.choice(list_thinh), color=0xFF1493)
    embed.set_image(url=random.choice(gifs))
    await ctx.send(embed=embed)

# ======================== CHẠY BOT ========================
keep_alive()
bot.run(TOKEN)
