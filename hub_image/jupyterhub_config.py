# dummy for testing. Don't use this in production!
# environmental variables set in ../run_docker.sh
import sys
import os

c = get_config()  # noqa
c.JupyterHub.authenticator_class = "dummyauthenticator.DummyAuthenticator"

# launch with docker
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = "0.0.0.0"
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = f"{os.environ['HUB_CONTAINER_NAME']}"

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
# c.DockerSpawner.image_whitelist = {'scipy':'phaustin/notebook:textbook',
#                                    'pangeo':'phaustin/notebook:textbook'}
c.DockerSpawner.image = "phaustin/notebook:textbook"
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = f"{os.environ['NETWORK_NAME']}"

# delete containers when the stop
c.DockerSpawner.remove = True

# explicitly set cmd, so we start jupyterhub-singleuser rather than jupyter notebook
# This is useful when running docker images that aren't built specifically for JupyterHub
c.DockerSpawner.cmd = "jupyterhub-singleuser"
# c.DockerSpawner.notebook_dir = '/'
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir
# https://jupyterhub-dockerspawner.readthedocs.io/en/latest/api/index.html
# c.DockerSpawner.default_url='/tree/home/{username}'
#
# jupyter needs f-string-like syntax in template for user name
#
user_string = r"jupyterhub-user-{username}"
c.DockerSpawner.volumes = {
    f"{os.environ['HOST_HUB_HOMEDIRS']}/{user_string}": notebook_dir
}

## Services
c.JupyterHub.services = [
    {
        "name": "idle-culler",
        "admin": True,
        "command": [sys.executable, "-m", "jupyterhub_idle_culler", "--timeout=3600"],
    }
]
