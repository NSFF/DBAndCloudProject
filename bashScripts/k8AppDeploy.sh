#!/usr/bin/env bash
minikube image pull nsff/dbandcloud:main
kubectl create deployment dbandcloud --image=nsff/dbandcloud:main
kubectl expose deployment dbandcloud --type=NodePort --port=8080

# after startup is done, we can launch the application with minikube service, but the output can also
# be checked in the minikube dashboard => pods => click on the 3 dots next to the pod => logs
#minikube service dbandcloud