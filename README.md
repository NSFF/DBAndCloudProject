# DBAndCloudProject

# Software used

* Docker v24.0.4([install](https://docs.docker.com/engine/install/ubuntu/))
* Kubernetes v1.27.4 ([install](https://minikube.sigs.k8s.io/docs/drivers/docker/))
* Python~=3.8.0

# Environment setup

Use the [``requirements.txt``](requirements.txt) or [``environment.yml``](environment.yml) to install your local python env.
(Add ``python~=3.8.0`` to the requirements.txt script if you also want to install the right version of python. It had to be deleted because of a dockerfile issue.)


# References

Here is a list of references I used to fix bugs and implement the project:

* Fix docker install and run bug: https://askubuntu.com/questions/1379425/system-has-not-been-booted-with-systemd-as-init-system-pid-1-cant-operate
* Fix minikube not using docker driver by default: https://minikube.sigs.k8s.io/docs/drivers/docker/
* Docker make dockerfile tutorial: https://www.youtube.com/watch?v=LQjaJINkQXY
* Docker push to docker hub: https://www.youtube.com/watch?v=EIHY_CY5J0k
* Use image in minikube: https://minikube.sigs.k8s.io/docs/handbook/pushing/
* Docker install additional python libraries: https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file
* Helped in debugging/testing minikube pod: https://www.youtube.com/watch?v=wQRqTAW27oQ
* Use local docker image in minikube: https://stackoverflow.com/questions/42564058/how-to-use-local-docker-images-with-minikube
* Github actions only execute on folder specific changes: https://stackoverflow.com/questions/63822219/how-to-run-github-actions-workflow-only-if-the-pushed-files-are-in-a-specific-fo
* Github actions build docker and push to hub: https://docs.github.com/en/actions/publishing-packages/publishing-docker-images
* Github actions basics: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
* Github actions, dockerfile should not use workdir: https://docs.github.com/en/actions/creating-actions/dockerfile-support-for-github-actions