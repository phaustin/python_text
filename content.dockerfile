FROM busybox

RUN mkdir -p /srv/problem_solving_notebooks
COPY ./notebooks_source/ /srv/problem_solving_notebooks

CMD tail -f /dev/null


