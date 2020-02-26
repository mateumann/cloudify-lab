from cloudify.decorators import operation


@operation(resumable=True)
def configure(ctx, **kwargs):
    ctx.logger.info("Training configure ctx=%s kwargs=%s", ctx, kwargs)


@operation(resumable=True)
def rel_postconfigure(ctx, **kwargs):
    if 'instance' in ctx:
        ctx.logger.info("Post configure (training) for instance id=%s, runtime_properties=%s, " +
                        "host_ip=%s, relationships=%s, kwargs=%s",
                        ctx.instance.id, ctx.instance.runtime_properties, ctx.instance.host_ip,
                        ctx.instance.relationships, kwargs)
    elif 'node' in ctx:
        ctx.logger.info("Post configure (training) for node id=%s, type_hierarchy=%s, " +
                        "properties=%s, type=%s, kwargs=%s",
                        ctx.node.id, ctx.node.type_hierarchy, ctx.node.properties, ctx.node.type,
                        kwargs)
    else:
        ctx.logger.info("Post configure (training) for ctx=%s, kwargs=%s",
                        ctx.__dict__, kwargs)
