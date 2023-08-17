#!/usr/bin/env bash
kubectl create deployment dbandcloud --image=nsff/dbandcloud
kubectl expose deployment dbandcloud --type=NodePort --port=8080
minikube service dbandcloud