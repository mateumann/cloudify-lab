from cloudify.decorators import operation
from cloudify.constants import NODE_INSTANCE, RELATIONSHIP_INSTANCE


@operation(resumable=True)
def configure(ctx, **kwargs):
    ctx.logger.info("Training configure ctx=%s kwargs=%s", ctx, kwargs)


@operation(resumable=True)
def rel_postconfigure(ctx, **kwargs):
    if ctx.type == NODE_INSTANCE:
        ctx.logger.info("Post configure (training) for instance id=%s, runtime_properties=%s, " +
                        "host_ip=%s, relationships=%s, kwargs=%s",
                        ctx.instance.id, ctx.instance.runtime_properties, ctx.instance.host_ip,
                        ctx.instance.relationships, kwargs)
    elif ctx.type == RELATIONSHIP_INSTANCE:
        ctx.logger.info("Post configure (training) for relationship source.id=%s (%s), " +
                        "target.id=%s (%s), kwargs = %s",
                        ctx.source.instance.id, ctx.source.instance.host_ip, ctx.target.instance.id,
                        ctx.target.instance.host_ip, kwargs)
    else:
        ctx.logger.info("Post configure (training) for ctx=%s, kwargs=%s",
                        ctx.__dict__, kwargs)
