# A jupyerbook example served from localhost

## This is a sample jupyterhub setup for a jupyterbook.

Basic approach:

1) The docker-compose.yml file

- bind mounts `notebooks_source` in this repo to /srv/notebooks in the webserver
  and copies the book html files to /usr/local/apache2/htdocs

2) the `hub_image/jupyerhub_config.py` file

- bind mounts `home_dirs` in this repo to the notebook folder (default /home/joyvan/work)
  in the notebook container
  
- the `run_docker.sh` and .env files set parameters used in `jupyterhub_config.py` and 
  `docker-compose.yml`

3) Launching with:

- `./run_docker.sh`  will start the webserver on port ${TEXT_PORT} (default 8500) and the jupyterhub
  on ${HUB_PORT} (default 9500)

4) The github path for the notebooks in this repo needs to be specified in
   `notebooks_source/_config.yml`

5) so steps to build and deploy after cloning this repo:

   a) Create a local environment by executing:

     ```
      cd notebook_image
      conda env create -f environment.yml
      conda activate notebook
      pip install -r requirements.txt
      cd ..
      jb build notebooks_source
      ./run_docker.sh
     ```

  b) point your web browser at `localhost:8500` to see the book  
  c) right click on the rocketship on a page to get a launch jupyterhub and login  
  d) right click on the rocketship again to clone the repo and bring up that
     page in jupyter.


6) Next steps -- notebook and image testing, simplify the install process
