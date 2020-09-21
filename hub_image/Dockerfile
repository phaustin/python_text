FROM jupyterhub/jupyterhub:1.2
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache -r /tmp/requirements.txt
RUN mkdir -p /srv/jupyterhub/data
RUN chmod u+w,g+w,o+w /srv/jupyterhub/data
COPY jupyterhub_config.py /srv/jupyterhub/data/jupyterhub_config.py
RUN chmod u+w,g+w,o+w /srv/jupyterhub/data/*
WORKDIR /srv/jupyterhub/data
