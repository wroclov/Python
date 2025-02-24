Flask server has three API endpoints, each handling different HTTP methods.

locust: \
http://localhost:8089 

in browser: \
http://127.0.0.1:5000 \
http://127.0.0.1:5000/about

in Windows PowerShell: \
Invoke-WebRequest -Uri "http://127.0.0.1:5000/submit" -Method Post -Body "name=John Doe&email=john@example.com" -ContentType "application/x-www-form-urlencoded"

in sh: \
curl -X POST -d "name=John Doe&email=john@example.com" http://127.0.0.1:5000/submit
