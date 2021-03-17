FROM gcr.io/kubeflow-images-public/tensorflow-2.1.0-notebook-cpu:1.0.0

COPY requirements.txt /tmp

USER root

# RUN pip3 install --upgrade pip

RUN pip3 install -r /tmp/requirements.txt

RUN pip uninstall -y enum34

RUN pip3 install kfp --upgrade

USER ${NB_USER}
    
ENV NB_PREFIX /

CMD ["sh","-c", "jupyter notebook --notebook-dir=/home/${NB_USER} --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
