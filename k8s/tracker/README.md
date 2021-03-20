### Build and Push Image

```bash

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/c9b1h7x8

docker build -t tracker .

docker tag tracker:latest public.ecr.aws/c9b1h7x8/tracker:latest

docker push public.ecr.aws/c9b1h7x8/tracker:latest