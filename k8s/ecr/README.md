### Build and Push Image

```bash

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/c9b1h7x8

docker build -t heartdisease-nb .

docker tag heartdisease-nb:latest public.ecr.aws/c9b1h7x8/heartdisease-nb:latest

docker push public.ecr.aws/c9b1h7x8/heartdisease-nb:latest