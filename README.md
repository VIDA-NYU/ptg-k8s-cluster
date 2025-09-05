# HSRN Cluster (NYU's Kubernetes Cluster)

## First time using HSRN

When you log in for the first time, an HSRN staff member will have to add you to a Kubernetes namespace. Email hsrn-support@nyu.edu with your netID and the name you want for your namespace.

Before sending the email, follow the instructions to login and register with the HSRN system. They cannot add you until this step is done. Instructions here: https://k8s-docs.hsrn.nyu.edu/get-started/

## Install the client

You need to download the [Kubectl client](https://kubernetes.io/docs/tasks/tools/#kubectl), and if you want to build new container images, you should also install [Docker](https://www.docker.com/get-started/).

```
# Install with Homebrew on macOS
brew install kubectl
```
<details>
  <summary>kubelogin installation (v1.34.1) on macOS</summary>
  
Additionally, it is necessary to [download kubelogin](https://github.com/int128/kubelogin/releases/tag/v1.34.1), a plugin facilitating SSO authentication. Ensure the binary is placed in the PATH as ``kubectl-oidc_login``.
```
# 1. Download the release archive for macOS from GitHub:
#    kubelogin_darwin_amd64.zip (Intel) or kubelogin_darwin_arm64.zip (Apple Silicon)

# 2. Unzip the release archive
unzip kubelogin_darwin_amd64.zip -d ~/Downloads/kubelogin-darwin-amd64
cd ~/Downloads/kubelogin-darwin-amd64

# 3. Move binary to PATH as kubectl-oidc_login
sudo mv kubelogin /usr/local/bin/kubectl-oidc_login

# 4. Make it executable
sudo chmod +x /usr/local/bin/kubectl-oidc_login

# 5. Remove macOS quarantine attribute (Gatekeeper restriction)
sudo xattr -r -d com.apple.quarantine /usr/local/bin/kubectl-oidc_login

# 6. Verify installation
kubectl-oidc_login --version
```
</details>

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
# Check variable
echo $KUBECONFIG
export KUBECONFIG=<home-directory>/.kube/config
```
For troubleshooting or details, please check the HSRN documentation available [here](https://k8s-docs.hsrn.nyu.edu/)
## Get access 
you can select your namespace by entering the following
```
kubectl config set-context --current --namespace ptgproject
```
Verify in which namespace you are:
```
kubectl config view --minify | grep namespace:
```

Checks whether the current Kubernetes context has permission to create pods in the active namespace.
```
kubectl auth can-i create pods
```

## PTG members
Other team members will need to follow the same steps and download their own configuration file. Once this is done contact HSRN staff member (hsrn-support@nyu.edu) so they can add you to the ptg namespace.

# Building And Deploying PTG applications on Kubernetes

## Push the image to a container registry
In order for the cluster to be able to get your container image, you have to put it on a registry. There are multiple free registries available. We are using GitHub Actions to build and push Docker images. Each repository has its Actions.

## Create the Deployment
Create the Deployment on the cluster by running:
```
$ kubectl apply -f deployment.yml
```
## Create the Service
Create the Service on the cluster by running:
```
kubectl apply -f service.yml
```
## Create an Ingress with a subdomain
Create the Ingress on the cluster by running:
```
kubectl apply -f ingress.yml
```

## Kubernetes Dashboard NYU
Kubernetes provides a web-based user interface (UI) that lets you perform various actions on your cluster. You can use the dashboard to: 
- Deploy containerized applications to your cluster
- Troubleshoot containerized applications
- Manage cluster resources
- View information related to applications running on a cluster
- Create or modify Kubernetes resources, including Deployments, DaemonSets, and Jobs
- Provides information about the state of cluster resources and various errors.
  
You can access the Kubernetes Dashboard [here](https://k8s-dashboard.hsrn.nyu.edu/). To get access you need to use your NYU credentials (NYU email and password). Inside the dashboard, select the namespace "ptgproject" using the dropdown menu.

<img width="1437" alt="kubernetesdashboard_select_ptgproject" src="https://github.com/VIDA-NYU/ptg-k8s-cluster/assets/11592889/86f78ae3-afaa-4e89-bcaa-1333faf24439">

# Using ptgctl to replay recordings
ptgctl is a Python Library and Command Line tool for interacting with the PTG API and data streams. Installation details are available [here](https://github.com/VIDA-NYU/ptgctl/tree/main?tab=readme-ov-file#install). After ptgctl is installed, run the following code:

```bash
# upgrading ptgctl
ptgctl upgrade
# url to another machine
ptgctl login --url https://argus-api.hsrn.nyu.edu
```

To replay a mock video
```bash
ptgctl mock video <path/to/video.mp4>
```

To replay a video that is stored in the cluster
```bash
# list available recordings
ptgctl recordings ls
# example: replay recording 2023.11.01-18.08.15 
ptgctl recordings replay 2023.11.01-18.08.15  main+depthlt
```



