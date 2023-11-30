# Services mutualisés
from diagrams import Diagram, Cluster
from diagrams.onprem.storage import Ceph
from diagrams.onprem.inmemory import Redis
from diagrams.k8s.compute import Deployment
from diagrams.azure.identity import ADB2C


with Diagram("Services mutualisés", show=False, filename="images/servicesmut"):

    ceph = Ceph("Ceph/s3")
    adb2c = ADB2C("Azure AD B2C")

    with Cluster("K8S"):
        redis = Redis("Redis\n(cache)")
        client = Deployment("Application cliente")
        osapi = Deployment("OS-API")
    
    client >> redis
    client >> osapi >> ceph
    client >> adb2c

