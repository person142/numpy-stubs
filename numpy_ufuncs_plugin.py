from mypy.nodes import ARG_POS
from mypy.plugin import Plugin
from mypy.types import CallableType
import numpy as np


def ufunc_call_hook(ctx):
    ufunc_name = ctx.context.callee.name
    ufunc = getattr(np, ufunc_name, None)
    if ufunc is None:
        # No extra information; return the signature unmodified.
        return ctx.default_signature

    # Strip off the *args and replace it with the correct number of
    # positional arguments.
    arg_kinds = [ARG_POS] * ufunc.nin + ctx.default_signature.arg_kinds[1:]
    arg_names = (
        [f'x{i}' for i in range(ufunc.nin)] +
        ctx.default_signature.arg_names[1:]
    )
    arg_types = (
        [ctx.default_signature.arg_types[0]] * ufunc.nin +
        ctx.default_signature.arg_types[1:]
    )
    return ctx.default_signature.copy_modified(
        arg_kinds=arg_kinds,
        arg_names=arg_names,
        arg_types=arg_types,
    )


class UFuncPlugin(Plugin):
    def get_method_signature_hook(self, method):
        if method == 'numpy.ufunc.__call__':
            return ufunc_call_hook


def plugin(version):
    return UFuncPlugin
