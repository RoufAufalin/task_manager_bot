from discord.ext import commands
import database
import discord

class TaskManagerCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(
            f"Hallo {ctx.author.mention}, butuh bantuan apa?"
        )
    
    @commands.command()
    async def add_task(self, ctx, *, description):
        
        description = description.strip()
        
        if not description:
            await ctx.send(f"Masukkan tugas yang ingin dikerjakan!")
        else:    
            task_id =  database.add_task(description)
            
            await ctx.send(
                f"Tugas #{task_id}: {description} telah ditambahkan! "
            )
    
    @commands.command()
    async def show_tasks(self, ctx):
        tasks = database.show_tasks()
        
        if tasks == []:
            await ctx.send(
                f"Tidak ada tugas"
            )
            return
        
        all_task = discord.Embed(title = "Daftar Tugas", description = "Berikut daftar tugas kamu", colour=discord.Color.blue())
        
        for task in tasks:
            task_id = task[0]
            description = task[1]
            status = "Belum Selesai" if task[2] == 0 else "Selesai"
            
            all_task.add_field(
                name = f"Tugas #{task_id}",
                value = f"{description} \n Status: {status}",
                inline = False
            )
                
        await ctx.send(embed=all_task)
    
    @commands.command()
    async def delete_task(self, ctx, task_id: int):
        result = database.delete_task(task_id)
        
        if result:
            await ctx.send(f"Tugas {task_id} berhasil dihapus")
        else:
            await ctx.send(f"Tugas {task_id} tidak ditemukan")
            
    @commands.command()
    async def complete_task(self, ctx, task_id: int):
        result = database.complete_task(task_id)
        if result:
            await ctx.send(f"Tugas {task_id} berhasil diselesaikan")
        else:
            await ctx.send(f"Tugas {task_id} tidak ditemukan")
    
async def setup(bot):
    await bot.add_cog(TaskManagerCommands(bot))
    