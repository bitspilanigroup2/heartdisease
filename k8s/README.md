## Godaddy
  https://account.godaddy.com/
  https://dcc.godaddy.com/manage/nithin.net.in/dns


## Delete kubeconfig
  kubectl config delete-cluster aiplatform.us-east-1.eksctl.io
  kubectl config delete-context nithin@aiplatform.us-east-1.eksctl.io
  kubectl config unset users.nithin@aiplatform.us-east-1.eksctl.io
  kubectl config unset current-contexts.nithin@aiplatform.us-east-1.eksctl.io
  kubectl config unset current-context

## Entries
  Callback URL(s)
    https://kubeflow.bitspilanigroup2.com/oauth2/idpresponse
  Domain Name
    auth.platform.nithin.net.in

## Usage - https://www.kubeflow.org/docs/aws/deploy/install-kubeflow/

  # 1. Create EKS Cluster
      eksctl create cluster -f cluster.yaml

  # 2. Variables
      export PATH=$PATH:"/home/user/Documents/Learnings/BITS/BITS - AI & ML/Comprehensive/Project/heartdisease/k8s"
      export AWS_CLUSTER_NAME=aiplatform
      export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_aws_cognito.v1.2.0.yaml"
      mkdir ${AWS_CLUSTER_NAME} && cd ${AWS_CLUSTER_NAME}
      wget -O kfctl_aws.yaml $CONFIG_URI
  
  # 3. Use Node Group Role
      aws iam list-roles \
      | jq -r ".Roles[] \
      | select(.RoleName \
      | startswith(\"eksctl-$AWS_CLUSTER_NAME\") and contains(\"NodeInstanceRole\")) \
      .RoleName"
  
  # 4. Updates Roles, region & comment enablepodiampolicy

  # 5. Deploy Kubeflow
      kfctl apply -V -f kfctl_aws.yaml
      kubectl -n kubeflow get all
      kubectl get ingress -n istio-system

  # 6. Delete kubeflow
      kfctl delete -V -f kfctl_aws.yaml

  # 7. Delete EKS
      eksctl delete cluster --name aiplatform

  

## Trouble Shooting
  
  https://www.kubeflow.org/docs/aws/troubleshooting-aws/

  kubectl get configmaps aws-alb-ingress-controller-config -n kubeflow -o yaml > ex-config.yaml
  kubectl replace -f ex-config.yaml

  kubectl -n kubeflow get all
  kubectl get ingress -n istio-system
  kubectl get ing istio-ingress -n istio-system -o yaml

  kubectl get ing istio-ingress -n istio-system -o yaml > ex-ingress.yaml
  kubectl replace -f ex-ingress.yaml

  kubectl get svc istio-ingressgateway -n istio-system -o yaml
  KUBE_EDITOR="nano" kubectl edit svc istio-ingressgateway -n istio-system



## EKS Ingress Sample
  kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/2048/2048-namespace.yaml
  kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/2048/2048-deployment.yaml
  kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/2048/2048-service.yaml
  kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/v1.1.4/docs/examples/2048/2048-ingress.yaml


## Home Page
  https://kubeflow.platform.nithin.net.in
  