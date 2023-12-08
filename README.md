# HSRN Cluster (NYU's Kubernetes Cluster)

## First time using HSRN

When you log in for the first time, an HSRN staff member will have to add you to a Kubernetes namespace. Email hsrn-support@nyu.edu with your netID and the name you want for your namespace.

## Install the client

You need to download the [Kubectl client](https://kubernetes.io/docs/tasks/tools/#kubectl), and if you want to build new container images, you should also install [Docker](https://www.docker.com/get-started/).

```
# Install with Homebrew on macOS
brew install kubectl
```

Go to https://config.hsrn.nyu.edu/ and click on "get your config". You will be asked to log in using one of a long list of providers. Please select "New York University" if you have an NYU netID.

After you log in, you will be shown a YAML file. Put that file in .kube/config in your home directory

```
# go to home directory
cd ~
# You can create the .kube directory if it doesn't exist.
mkdir .kube
cd .kube/
# copy the YAML file generated online
# use ``wq`` to save and exit vim
vim config
# set the KUBECONFIG environment variable to its location
export KUBECONFIG=<home-directory>/.kube/config
```
For troubleshooting or details, please check the HSRN documentation available [here](https://k8s-docs.hsrn.nyu.edu/)
## Get access 
you can select your namespace by entering the following
```
kubectl config set-context --current --namespace ptgproject
```
Check your access by doing:
```
kubectl auth can-i create pods
```

## PTG members
Other team members will need to follow the same steps and download their own configuration file. Once this is done contact HSRN staff member (hsrn-support@nyu.edu) so they can add you to the ptg namespace.
