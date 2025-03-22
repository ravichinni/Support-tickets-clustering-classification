c = get_config()

# Set password for Jupyter
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$/SOYrXltsn7TNv4hyTWltA$tvQ6tRHyUlkDLkFGMmpOv9JziZ11Pm1HLrVPxxVs/sM'

# Allow connections from all IPs
c.NotebookApp.ip = '*'

# Set the port
c.NotebookApp.port = 8888 