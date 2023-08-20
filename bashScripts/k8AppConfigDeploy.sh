#!/usr/bin/env bash
minikube image pull nsff/dbandcloud:main
kubectl apply -f ./../configs/k8-deployment-config.yml

# after startup is done, we can launch the application with minikube service, but the output can also
# be checked in the minikube dashboard => pods => click on the 3 dots next to the pod => logs
#minikube service dbandcloud