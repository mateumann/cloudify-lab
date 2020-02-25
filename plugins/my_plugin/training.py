
from cloudify.decorators import operation

@operation(resumable=True)
def configure(ctx, **kwargs):
    ctx.logger.info("Training configure ctx=%s kwargs=%s", ctx, kwargs)

@operation(resumable=True)
def rel_postconfigure(ctx, **kwargs):
    ctx.logger.info("Training rel_postconfigure ctx=%s kwargs=%s", ctx, kwargs)
