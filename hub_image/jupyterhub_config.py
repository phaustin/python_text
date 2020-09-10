# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image_whitelist = {'scipy':'jupyter/scipy-notebook:latest',
                                   'pangeo':'phaustin/notebook:textbook'}
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'textbook_network'

# delete containers when the stop
c.DockerSpawner.remove = True

# explicitly set cmd, so we start jupyterhub-singleuser rather than jupyter notebook
# This is useful when running docker images that aren't built specifically for JupyterHub
c.DockerSpawner.cmd = 'jupyterhub-singleuser'
