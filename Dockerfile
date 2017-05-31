FROM jupyter/datascience-notebook
WORKDIR /app
ADD . /app
USER root
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.notebook_dir=/app"]
