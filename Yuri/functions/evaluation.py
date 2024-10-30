from Yuri import Yuri
from discord.ext import commands
from discord import *

@Yuri.command("eval")
async def eval(ctx):
    if len(ctx.message.content.split()) < 2:
        return await ctx.send("Please enter code to run it!")
    stats = await ctx.send("Loading...")
    
    cmd = ctx.message.content.split(None, 1)[1]

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = io.StringIO()
    redirected_error = io.StringIO()
    sys.stdout = redirected_output
    sys.stderr = redirected_error
    exc = None

    try:
        exec(f"async def __aexec(ctx):\n" + "".join(f"    {line}\n" for line in cmd.splitlines()))
        await locals()["__aexec"](ctx)
    except Exception:
        exc = traceback.format_exc()
    stdout, stderr = redirected_output.getvalue(), redirected_error.getvalue()
    sys.stdout, sys.stderr = old_stdout, old_stderr
    evaluation = exc if exc else stderr if stderr else stdout if stdout else "Success"
    output_code = f"{evaluation.strip()}"
    if len(output_code) > 3500:
        with io.BytesIO(evaluation.encode()) as out_file:
            out_file.name = "eval_output.txt"
            await ctx.send("Output too big, sending as file:", file=File(out_file))
    else:
        await ctx.send(f"```python\n{output_code}```")
    await stats.delete()      
