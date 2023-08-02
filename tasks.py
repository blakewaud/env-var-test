import os
from robocorp.tasks import task
from robocorp import log


@task
def expose_env_vars():
    """Logs all environment variables available in the context."""
    env_vars = os.environ
    log.info(f"Environment variables: {env_vars!r}")
