def filter_user(user, reject_him=False):
    def decorator(func):
        async def wrapper(ctx, *args, **kwargs):
            if user.isdigit():
                if ctx.author.id != int(user) and reject_him == False:
                    return await ctx.send("You do not have permission to use this command.")
                elif reject_him == True and ctx.author.id == int(user):
                    return await ctx.send("You do not have permission to use this command.")
            else:
                if ctx.author.name != user and reject_him == False:
                    return await ctx.send("You do not have permission to use this command.")
                elif reject_him == True and ctx.author.name == user:
                    return await ctx.send("You do not have permission to use this command.")
            return await func(ctx, *args, **kwargs)
        return wrapper
    return decorator
