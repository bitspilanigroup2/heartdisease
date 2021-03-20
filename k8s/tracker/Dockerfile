FROM python:3.8.0

COPY requirements.txt /

RUN pip install -r requirements.txt
    
RUN mkdir /mlflow/

EXPOSE 5000

## Environment variables made available through the Fargate task.
## Do not enter values
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    # --default-artifact-root ${BUCKET} \
    # --backend-store-uri mysql+pymysql://${USERNAME}:${PASSWORD}@${HOST}:${PORT}/${DATABASE}