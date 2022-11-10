# Jupyter Notebook

## Installation
```bash
pip install jupyterlab
pip install notebook
pip install voila

pip install notedown  # converter markdown to ipynb and viceversa
pip install jupyterthemes
```


## Configuration
```bash
jt -l  # lists the themes
jt -t monokai # applies the theme
# jupyter nbconvert https://github.com/jupyter/nbconvert

sudo nano ~/.local/lib/python3.7/site-packages/jupyter_core/tests/dotipython/profile_default/ipython_notebook_config.py
# add c.NotebookApp.notebook_dir = '/path/to/your/notebooks'
```

## Run
```bash
jupyter notebook --ip='*'
jupyter lab --ip='*'
 
jupyter notebook --ip='*' --notebook-dir=~/Notebook& 
```



## Installing Jupyter Notebook as Service (Advanced Installation)
https://tech.amikelive.com/node-768/how-to-install-jupyter-notebook-as-service-for-tensor-flow-and-deep-learning-on-ubuntu-16-04/
https://naysan.ca/2019/09/07/jupyter-notebook-as-a-service-on-ubuntu-18-04-with-python-3/


1. Create a password
  ```bash
  jupyter notebook password
  ```

1. Create `jupyter.service`
  ```
  [Unit]
  Description=Jupyter Notebook
  [Service]
  Type=simple
  PIDFile=/run/jupyter.pid
  ExecStart=/bin/bash -c "/home/pi/.local/bin/jupyter-lab --ip='*' --notebook-dir=/home/pi/Notebook  --no-browser --port=8102"
  User=pi
  Group=pi
  WorkingDirectory=/home/pi/Notebook
  Restart=always
  RestartSec=10
  [Install]
  WantedBy=multi-user.target
  ```
  
  > Paths needs to be absolute

2. Run the following commands
  ```bash
  sudo cp jupyter.service /etc/systemd/system/
  sudo systemctl enable jupyter.service
  sudo systemctl daemon-reload
  sudo systemctl start jupyter.service
  ```
alias refresh="sudo nano /etc/systemd/system/jupyter.service && sudo systemctl daemon-reload && sudo systemctl start jupyter.service && sudo systemctl status jupyter.service"     







## Installing Jupyter Notebook as Service (Advanced Installation) - option 2

1. Generate automatic password for Jupyter
  ```bash
  jupyter notebook password
  ```

  Sample output:

  ```
  Enter password: 
  Verify password: 
  [NotebookPasswordApp] Wrote hashed password to ~/.jupyter/jupyter_notebook_config.json
  
  ```
  
  ```
  
1. Generate default Jupyter configuration
  ```bash
  jupyter notebook --generate-config
  ```

1. Modify the default Jupyter configuration file
  ```bash
  vi ~/.jupyter/jupyter_notebook_config.py
  ```
  
  jupyter_notebook_config.py
  
  ```
  c.NotebookApp.ip = '*'
  c.NotebookApp.port = 8888
  c.NotebookApp.open_browser = False
  ## Whether to allow the user to run the notebook as root.
  c.NotebookApp.allow_root = True
  ```

1. Create a directory and file for Jupyter log file
  ```bash
  mkdir -p ~/logs/jupyter
  touch ~/logs/jupyter/jupyter.log
  ```
  
1. Create a shell script to start Jupyter service. We name this script as `start-jupyter-service.sh`
  ```bash
  vi ~/start-jupyter-service.sh
  ```
  
  ```
  #!/bin/bash
   
  . ~/virtualenv/tensorflow/bin/activate
  nohup ~/virtualenv/tensorflow/bin/jupyter-notebook --config=~/.jupyter/jupyter_notebook_config.py > ~/logs/jupyter/jupyter.log 2>&1 < /dev/null 
  ```
  
1. Add execution right to the shell script
  ```bash
  chmod u+x ~/start-jupyter-service.sh
  ```
  
1. Create `jupyter.service` in `~/.config/systemd/user/jupyter.service`
  ```bash
  mkdir -p ~/.config/systemd/user
  vi ~/.config/systemd/user/jupyter.service
  ```
  
  jupyter.service
  ```
  [Unit]
  Description=Jupyter Notebook
  AssertPathExists=~/virtualenv/tensorflow
   
  [Service]
  Type=simple
  PIDFile=/run/jupyter.pid
  ExecStart=/bin/bash ~/start-jupyter-service.sh
  WorkingDirectory=~/notebooks/
  Restart=always
  RestartSec=10
   
  [Install]
  WantedBy=default.target
  ```
  
1. Enable the service to start after system boot

1. Enable MYUSER to keep running the service even though the user is not currently logged in
  ```bash
  sudo loginctl enable-linger MYUSER
  ```
  
1. Automatically start the Jupyter service registered by MYUSER on every system restart
  ```bash
  systemctl --user enable jupyter.service
  ```
  
1. Start the service
  ```bash
  systemctl --user start jupyter.service
  ```