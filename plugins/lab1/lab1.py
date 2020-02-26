from cloudify.decorators import operation


@operation(resumable=True)
def start(ctx):
    ctx.logger.info("Starting lab1")
