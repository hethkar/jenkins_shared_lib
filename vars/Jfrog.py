#!/usr/bin/env python3
import requests

url = "http://192.168.0.104:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
file_path = '/home/osboxes/Java_app_3.0/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
username = 'admin'
password = 'Admin@123'

with open(file_path, 'rb') as file:
   response = requests.put(url, auth=(username, password), data=file)

if response.status_code == 201:
    print("\nPUT request was successful")
else:
   print(f"PUT request failed with status code {response.status_code}")
   print("Response content:")
   print(response.text)  
