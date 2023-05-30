# Docker

* [https://medium.com/@nagarwal/lifecycle-of-docker-container-d2da9f85959](https://medium.com/@nagarwal/lifecycle-of-docker-container-d2da9f85959)
* [https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/](https://www.howtoforge.com/tutorial/how-to-create-docker-images-with-dockerfile/)


## Terminology
-   _Images_ - The blueprints of our application which form the basis of containers. In the demo above, we used the `docker pull` command to download the **busybox** image.
-   _Containers_ - Created from Docker images and run the actual application. We create a container using `docker run` which we did using the busybox image that we downloaded. A list of running containers can be seen using the `docker ps` command.
-   _Docker Daemon_ - The background service running on the host that manages building, running and distributing Docker containers. The daemon is the process that runs in the operating system to which clients talk to.
-   _Docker Client_ - The command line tool that allows the user to interact with the daemon. More generally, there can be other forms of clients too - such as [Kitematic](https://kitematic.com/) which provide a GUI to the users.
-   _Docker Hub_ - A [registry](https://hub.docker.com/explore/) of Docker images. You can think of the registry as a directory of all available Docker images. If required, one can host their own Docker registries and can use them for pulling images.


An important distinction to be aware of when it comes to images is the difference between base and child images.

-   **Base images** are images that have no parent image, usually images with an OS like ubuntu, busybox or debian.
    
-   **Child images** are images that build on base images and add additional functionality.
    

Then there are official and user images, which can be both base and child images.

-   **Official images** are images that are officially maintained and supported by the folks at Docker. These are typically one word long. In the list of images above, the `python`, `ubuntu`, `busybox` and `hello-world` images are official images.
    
-   **User images** are images created and shared by users like you and me. They build on base images and add additional functionality. Typically, these are formatted as `user/image-name`.


## Installation


### Windows (7, 8, 10)


1. Enable Hyper-V 


   ```
   dism.exe /Online /Disable-Feature:Microsoft-Hyper-V
   ```


   or


   ```
   bcdedit /set hypervisorlaunchtype auto
   ```


   > Note1: Virtual-Box and Vmware are not going to work anymore since they require Hyper-V disabled
   >
   > Note2: To disable it again use
   >
   > ```
   > dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All
   > ```
   >
   > or
   >
   > ```
   > bcdedit /set hypervisorlaunchtype off
   > ```
   >
   > ​


2. Download the installer from the website https://store.docker.com/editions/community/docker-ce-desktop-windows (direct web installer link: https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe )


### Linux

```bash
sudo dnf -y install dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo dnf -y install docker-compose
sudo systemctl enable docker
sudo systemctl start docker
```

#### Linux Manual steps

The Post-installation steps for Linux documentation reveals the following steps:

1. Create the docker group.
    ```bash
    sudo groupadd docker
    ```
1. Add the user to the docker group.
    ```bash
    sudo usermod -aG docker $(whoami)
    ```
1. Log out and log back in to ensure docker runs with correct permissions.

1. Start docker.
    ```bash
    sudo service docker start
    ```


#### Linux Mint 18.2 (Sonya)

```shell
sudo apt-get update


sudo apt-get install apt-transport-https ca-certificates curl software-properties-common


curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -


sudo apt-key fingerprint 0EBFCD88


sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"


sudo apt-get update


sudo apt-get install docker-ce
```

#### Kali - Ubuntu
```bash
sudo apt-get -y install docker.io
```



### Mac OS X

As Dayel Ostraco says is necessary to add environments variables:
```bash
docker-machine start # Start virtual machine for docker
docker-machine env  # It's helps to get environment variables
eval "$(docker-machine env default)" # Set environment variables
```
The docker-machine start command outputs the comments to guide the process.



## Create image

### Docker file

#### ARG
Set variable in Docker file

```Dockerfile
ARG version=1.0

RUN echo $version
```

#### FROM
Pull baseline image from Docker hub

```Dockerfile
FROM <image-name>:[tag]
```

```Dockerfile
FROM ubuntu:22.10
```

If the tag is not specified, the latest version is used

```Dockerfile
FROM ubuntu
```


#### ENV
Set environment variable in docker image

```Dockerfile
ENV PATH="${PATH}:/kw-server/bin"
```

#### RUN
Run command in docker image

```Dockerfile
RUN apt-get update
```

#### CMD
A CMD command is used to set a default command that gets executed once you run the Docker Container. In case you provide a command with the Docker run command, the CMD arguments get ignored from the dockerfile. In the case of multiple CMD commands, only the last one gets executed.

```Dockerfile
CMD ["python3", "app.py"]
```

> :warning: Note that the CMD commands get ignored if you provide arguments in your Docker run command.
> ```bash
> sudo docker run -it ubuntu bash
> ```

#### ENTRYPOINT
An ENTRYPOINT command, unlike CMD, does not ignore additional parameters that you specify in your Docker run command.

#### RUN vs CMD vs ENTRYPOINT
* [codewithyury](https://codewithyury.com/docker-run-vs-cmd-vs-entrypoint/)
* [geeksforgeeks](https://www.geeksforgeeks.org/difference-between-run-vs-cmd-vs-entrypoint-docker-commands/)

`RUN` is an image build step, the state of the container after a RUN command will be committed to the container image. A Dockerfile can have many RUN steps that layer on top of one another to build the image.

`CMD` is the command the container executes by default when you launch the built image. A Dockerfile will only use the final CMD defined. The CMD can be overridden when starting a container with docker run $image $other_command.

`ENTRYPOINT` is also closely related to CMD and can modify the way a container is started from an image.

CMD: Sets default parameters that can be overridden from the Docker Command Line Interface (CLI) while running a docker container.
ENTRYPOINT: Default parameters that cannot be overridden while executing Docker Containers with CLI parameters.

#### WORKDIR
Change/set working directory

```Dockerfile
WORKDIR /home
```

#### COPY
Copy a file from host machine to the image

```Dockerfile
COPY . /klocwork
```

#### USER
Switch user

```Dockerfile
USER Alice
```

```Dockerfile
USER root
RUN useradd Alice -s /bin/bash

USER Alice
RUN mkdir AliceFolder
```


### Docker compose
Provides a yaml configuration for Docker file.

TBC


## Create image (Build image)
This is achieved using the Dockerfile. A [Dockerfile](https://docs.docker.com/engine/reference/builder/) is a simple text-file that contains a list of commands that the Docker client calls while creating an image.

```docker
# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "./app.py"]
```

```bash
docker build -t <tagname>:<tag_number> <Dockerfile location>
```

```bash
docker build -t prakhar1989/catnip .
```
- `-t` : optional tag name
- Dockerfile location

If you don't have the `python:3-onbuild` image, the client will first pull the image and then create your image.


## Publish images

### Publish to AWS

 1. Login with : `docker login` and fill with credential of docker hub (https://hub.docker.com/)
 2. push the image with : `docker push <image>`

### Place in the private repository (Docker - Private Registries)


## Run container of existing image

```bash
docker run --name <container-name> -p <new_port>:<origin_port> --mac-address <MAC> --hostname <hostname> --user <user> --rm -it <IMAGE-NAME> <command>
```

example

```bash
docker run --name srva -p 27001:27001 --mac-address 02:42:ac:11:00:03 --hostname srva --user username --rm -it flex bash
```

where:
* `--name <container-name>` : allows to specify the container name
* `--mac-address <MAC>` : allows to specify the container MAC address
* `--hostname <hostname>` : allows to specify the container hostname
* `--user <user>` : 
* `-p <new_port>:<origin_port>` : maps/expose the port from container to host
* `--rm` : Automatically remove the container when it exits
* `-i` : enables the interactive mode -> it starts and commands can be given using the host terminal
* `-t` : Allocate a pseudo-TTY (usually used with `-i`, combined becomes `-it`)
* `<IMAGE-NAME>` : image name to use
* `<command>` : command to run at container creation




## Docker images/containers management

### Pull image
```bash
docker pull "<image_name>"
```


* ```<image_name>``` : images are stored in an online repository (https://hub.docker.com/explore/)


```bash
docker pull busybox
```

### List images 
```bash
docker images
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
busybox             latest              59788edf1f3e        4 weeks ago         1.15MB
```


### Remove images
```bash
docker rmi <imageID>
```

```bash
docker rmi 59788edf1f3e
```


### Transfer images from one host to another

#### Export image to tar file 
```
docker save -o <path for generated tar file> <image name>
```
```bash
docker save -o /root/Desktop/image_dartie.tar image_dartie
```

#### Import image from tar file
Copy the image to the new system with a regular transfer:
```
docker load -i <path to image tar file>
```
```bash
docker load -i image_dartie.tar
```


### Create container (run container)
run a Docker **container** based on an image.
* The container boot, runs and destroys itself: so running it without any command will do nothing. 
* If the container has not been pulled first, it will be with the run command

```bash
docker run "[OPTIONS]" "<image_name>" "<cmd_to_execute_in_container"
```


* **[OPTIONS]:** 
  * `-t` : attach to the *terminal*
  * `-i` : *interactive*. It will keep stdin open
  * `-d` : *detach* to the terminal
  * `--name` : assign a *name* to the *container*
  * `-v` : specifies a *volume*, making the container persistent. This allows to save data to the disk. Without this options, all data are lost after the container has terminated.
  * `--rm` : removes the container after run it (by default only kill itself) - `docker container prune` command can be used to achieve the same effect.
  * `-P` will publish all exposed ports to random ports
  * `--name` corresponds to a name we want to give.
  * `-p <new_port>:<origin_port>`: specify a custom port to which the client will forward connections to the container.
  * `--privileged`: allows to run special commands such as `ifconfig eth0 down` which otherwise returns `SIOCSIFFLAGS: Operation not permitted`
  * `--mac-address`: run the container with a specific mac address
  * `--hostname`: run the container with a specific hostname


```bash
docker run busybox echo "hello from busybox"
```

#### Run with interactive mode
Allows to run commands in the container; the container does not kill itself

```bash
docker run -it busybox sh
```

#### Attach to running docker container interactive
Allows to attach (connect) to a running container

```bash
docker exec -it <container name or id> /bin/bash
```

### Stop containers
* [https://dbaontap.com/2017/04/16/removing-docker-containers-images/](https://dbaontap.com/2017/04/16/removing-docker-containers-images/)
```bash
docker stop <containerID or name>
```

```bash
docker stop 
```

#### Stop all containers
```bash
docker stop $(docker ps -a -q)
```
or (developed by me)
```bash
sudo docker ps | grep -P "(^[a-z0-9]+)\s" | xargs sudo docker stop
```
or (developed by me)
```bash
sudo docker ps -q | xargs sudo docker stop
```
or (developed by me)
```bash
sudo docker ps -q | xargs -i sudo docker stop {}
```


### List containers
```bash
docker ps  # displays all containers running
```

#### options
* `-a` : list all containers
* `-n` : list last n(int) containers created
* `-l` : list the latest container 
* `-q` : docker run busybox echo "hello from busybox"


### List ports in use for a container
```bash
docker port [CONTAINER]
```

```bash
docker port static-site
```


### Share files
```bash
docker cp <containerId>:/file/path/within/container /host/path/target
```
```bash
# Copy file from host to docker container
docker cp foo.txt mycontainer:/foo.txt

# Copy file from docker container to host
docker cp mycontainer:/foo.txt foo.txt
```

### Remove container
Running `docker run` multiple times and leaving stray containers will eat up disk space. So we need to clean up the space.

```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

### Remove all containers
```bash
docker rm $(docker ps -a -q)
```
or (created by me)

```bash
sudo docker ps -a -q | xargs -i sudo docker rm {}
```

or (not tested yet)
```bash
sudo docker images | grep none | awk '{ print $3; }' | xargs sudo d  
ocker rm
```

### Remove all exited containers
```bash
sudo docker ps -a | grep Exit | cut -d ' ' -f 1 | xargs sudo docker rm
```

or 

```bash
docker rm $(docker ps -a -q -f status=exited)
```
* `-q` flag, only returns the numeric IDs 
*  `-f` filters output based on conditions provided


### Commands in container
* ```CTRL + P + Q ``` : quit the container without stopping it
* ```CTRL + D``` : quit the container stopping it


### List containers

### List containers running


### Run command in a container
```bash
docker exec -it <container_id_or_name> echo "Hello from container!"
docker run "<options>" "<image_name>" "<cmd_to_execute_in_container"
```



## Resources


* https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes


## Troubleshooting

### docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.26/containers/create: dial unix /var/run/docker.sock: connect: permission denied. See 'docker run --help'.`

**Problem:**
You are trying to run a docker container or do the docker tutorial, but you only get an error message like this:

```
docker: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post http://%2Fvar%2Frun%2Fdocker.sock/v1.26/containers/create: dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
```

**Solution:**
The error message tells you that your current user can’t access the docker engine, because you’re lacking permissions to access the unix socket to communicate with the engine.

As a temporary solution, you can use sudo to run the failed command as root.
However it is recommended to fix the issue by adding the current user to the docker group:

Run this command in your favourite shell and then completely log out of your account and log back in (if in doubt, reboot!):
```bash
sudo usermod -a -G docker $USER
```
After doing that, you should be able to run the command without any issues. Run `docker run hello-world` as a normal user in order to check if it works. Reboot if the issue still persists.

Logging out and logging back in is required because the group change will not have an effect unless your session is closed.


### Docker Troubleshooting – “conflict: unable to delete, image is being used by running container”
* [https://www.thegeekdiary.com/docker-troubleshooting-conflict-unable-to-delete-image-is-being-used-by-running-container/](https://www.thegeekdiary.com/docker-troubleshooting-conflict-unable-to-delete-image-is-being-used-by-running-container/)


### None images - Error: Conflict, XXXXXXXX wasn't deleted - Error: failed to remove one or more images

```bash
$ sudo docker rmi 60afe4036d97
Error: Conflict, 60afe4036d97 wasn't deleted
2014/01/28 00:54:00 Error: failed to remove one or more images
```

**In order to delete all images, use the given command**
```bash
docker rmi $(docker images -q)
```

**In order to delete all containers, use the given command**
```bash
docker rm $(docker ps -a -q)
```

## Analyse logs


## Dockers life
[https://medium.com/devopsion/life-and-death-of-a-container-146dfc62f808](https://medium.com/devopsion/life-and-death-of-a-container-146dfc62f808)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM2OTIzNDMzMywtMTc3NTM2MDAyMCwtOT
kxNTA2MDEsLTEwNDIwMzg2NSwtMTA2NjYyMjI3NSwxMDc2OTg3
NTI1LDE2MDgzMDQ1MDYsMTcyNTQ3NzY3MiwtMTM1MjU0OTkzLD
IxMDU0NTUwODIsLTU1OTE4NjUyMSw3NjQ2Nzg1NjYsLTc1OTIz
NDcyNywtMTA0NDcxNTE0NiwxMTQ2NjY4NDgyLDE0NzU1NzEzOD
csNTIwOTIzNjIwLDEzMTgzMzUxNjAsMjEwNjEwNTY5MiwyNDM4
MzE3NTldfQ==
-->
