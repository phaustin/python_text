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
c.DockerSpawner.image_whitelist = {'scipy':'phaustin/notebook:textbook',
                                   'pangeo':'phaustin/notebook:textbook'}
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'textbook_network'

# delete containers when the stop
c.DockerSpawner.remove = True

# explicitly set cmd, so we start jupyterhub-singleuser rather than jupyter notebook
# This is useful when running docker images that aren't built specifically for JupyterHub
c.DockerSpawner.cmd = 'jupyterhub-singleuser'
#c.DockerSpawner.notebook_dir = '/'
notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
# https://jupyterhub-dockerspawner.readthedocs.io/en/latest/api/index.html
#c.DockerSpawner.default_url='/tree/home/{username}'
c.DockerSpawner.volumes = {'/Users/phil/repos/python_text/git_repo':
                           {'bind':'/srv/notebook_repo','mode':'ro'},
                           '/Users/phil/repos/python_text/home_dirs/jupyterhub-user-{username}':
                           notebook_dir}
