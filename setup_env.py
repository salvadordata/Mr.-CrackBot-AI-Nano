
#### **Automate in Another Script**

Example (in a `start.sh` shell script):
```bash
#!/bin/bash
echo "Running setup..."
python setup.py
echo "Setup complete. Starting program..."
python main.py
