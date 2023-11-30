# Mise en réseau
from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.network import Ingress
from diagrams.k8s.compute import Pod
from diagrams.onprem.network import Nginx, Kong
from diagrams.onprem.client import User

with Diagram("Mise en réseau", show=False, filename="images/mer"):
    nginx = Nginx("nginx corpo")
    kong = Kong("API Gateway")
    user = User("Utilisateur")

    with Cluster("K8S (dev/acc/prod)"):
        web = Pod("web")
        api = Pod("api")
        ingress = Ingress()
        noeud = [web,api]
    
    user >> nginx >> Edge(label="api", color="darkblue") >> \
        kong >> Edge(color="darkblue") >> ingress >> Edge(color="darkblue") >> api
    nginx >> Edge(label="website", color="darkgreen") >> \
        ingress >> Edge(color="darkgreen") >> web
