import requests
import subprocess



def jfrogUpload():

    url =""
    file_path ="/var/lib/jenkins/workspace/first_pipeline/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = "admin"
    password = "Pass@123"

    with open(file_path,"rb") as file:
        response = requests.put(url,auth=(username,password),data=file)


    if response.status_code==201:
        print("\nPut Request was Sucessfullll")

    else:
        print(f"\nPut Request was Unsuccessfullll with Status Code{response.status_code}")
        print("Response Content")
        print(response.content)

def main():

    jfrogUpload()

if __name__== "__main__":
           
    main()
