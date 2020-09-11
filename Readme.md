# python text using an internal git repo

This is a sample jupyterhub setup for a jupyterbook.  Basic approach:

1) bind mount two directories -- a github repository for the notebooks (read-only) and
   a home_dirs repository for persisting user notebooks spawned by docker spawner.

2) To try this out on localhost:

   ```
   cp -a notebooks_source git_repo
   cd git_repo
   git init
   git add -f *
   git commit -m 'init'
   ```

   Then:

   a) docker-compose build content  
   b) docker-compose build jupyterhub  
   c) docker-compose build notebook
   d) docker-compose up

   server should be running on localhost:8500 with dummyAuthenticator

## next steps

Add apache webserver to serve `_build/html/` files that pull individual notebooks from the
bind mounted git repo
