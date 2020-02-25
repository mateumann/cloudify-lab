
from cloudify.decorators import operation

@operation(resumable=True)
def start(ctx, **kwargs):
    ctx.logger.info("Starting lab1")
