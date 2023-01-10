# My Public Knowledge base

## How to render the content

1. Install `pip`
    
    ```bash
    sudo apt install python3-pip
    ```
    
1. Install `virtualenv` as root
    
    ```bash
    sudo -i
    pip3 install virtualenv
    ```
    
1. Go back to standard user with `CTRL+D`
1. Create virtual environment `venv-mkdocs`
    
    ```bash
    virtualenv -p python3 venv-mkdocs
    ```
    
1. Activate it
    
    ```bash
    source venv-mkdocs/bin/activate
    ```
    
1. Install `mkdocs`
    
    ```bash
    pip3 install mkdocs
    ```
    
1. Create mkdocs project
    
    ```bash
    mkdocs new mkdocs-Notebook
    ```
    
1. Install extra
    
    ```bash
    pip install mkdocs-material
    pip install pymdown-extensions
    ```
    
1. Adjust settings: 
    
    ```bash
    nano mkdocs.yml
    ```
    
    1. doc folder: `docs_dir`
    2. Theme: [https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) or create a custom theme ([https://www.mkdocs.org/user-guide/custom-themes/](https://www.mkdocs.org/user-guide/custom-themes/))
    
    ```bash
    site_name: Notebook
    docs_dir: /srv/4dcdd73e-69f1-4caf-80fb-1d51b969fbb4
    theme: readthedocs
    ```
    
    - [http://www.tips.mostserio.us/usgMkDc/](http://www.tips.mostserio.us/usgMkDc/)
        
        ```yaml
        markdown_extensions:
          - admonition
          - attr_list
          - codehilite:
              guess_lang: false
          - def_list
          - footnotes
          - md_in_html
          - meta
          - pymdownx.caret
          - pymdownx.critic
          - pymdownx.details
          - pymdownx.keys
          - pymdownx.snippets
          - pymdownx.superfences
          - pymdownx.tabbed
          - pymdownx.tasklist:
              custom_checkbox: true
          - pymdownx.tilde
        theme:
          name: 'material'
        extra_css:
          - 'extra.css'
        extra:
          social:
            - icon: 'fontawesome/brands/github-alt'
              link: 'https://github.com/dartie'
        repo_name: 'dartie/knowledge-base'
        repo_url: 'https://github.com/dartie/knowledge-base'
        edit_uri: ''
        ```
        
        requires `pymdown-extensions`
        
        ```bash
        pip install pymdown-extensions
        ```

## Create service

Create file `mkdocs.service` in `/etc/systemd/system`:
```bash
sudo nano /etc/systemd/system/mkdocs.service
```

```
[Unit]
Description=Render markdown documentation with mkdocs
After=network.target
    
[Service]
User=root
WorkingDirectory=/home/Apps/venv-mkdocs
ExecStart=bash -c 'cd /Apps/venv-mkdocs/mkdocs-Notebook && /Apps/venv-mkdocs/bin/mkdocs serve -a 0.0.0.0:9001'
Restart=always
    
[Install]
WantedBy=multi-user.target
```

    
