import os
import json
from robocorp.tasks import task
from robocorp import log

log.add_sensitive_variable_name("SECRET")


@task
def expose_env_vars():
    """Logs all environment variables available in the context."""
    env_vars = {key: value for key, value in os.environ.items()}
    log.info(f"Environment variables: {json.dumps(env_vars, indent=4, sort_keys=True)}")
