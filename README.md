# DBAndCloudProject

# Software used

* docker v24.0.4([install](https://docs.docker.com/engine/install/ubuntu/))
* Kubernetes v1.27.4 ([install](https://minikube.sigs.k8s.io/docs/drivers/docker/))

# Environment setup

Use the [``requirements.txt``](requirements.txt) or [``environment.yml``](environment.yml) to install your local python env.


# References

Here is a list of references I used to fix bugs and implement the project:

* Fix docker install and run bug: https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate
* Fix minikube not using docker driver by default: https://minikube.sigs.k8s.io/docs/drivers/docker/