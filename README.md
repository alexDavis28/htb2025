# htb2025 - Skissue.com - Submission for Viridien

### Image classification system for identifiying land use 


#### Usage
- Load https://skissue.com
- Enter a username sign-up / sign-in 
- Upload / Choose a file previously uploaded
- Select an image and click classify to get infromation about the plot

#### Hosting
- Edit caddy to run on target host (replace skissue.com with localhost etc)
- Create a `conf.py` file under `backend/app` using the following template
```python
CONFIG = {
    'db': '/path/to/db',
    'filestore': '/path/to/file/store/folder'
}⏎
```
- Launch caddy
- `docker compose up -d`

