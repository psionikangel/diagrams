from diagrams import Cluster, Diagram
from diagrams.k8s.infra import Node

with Diagram("PaaS/Kubernetes", show=False, filename="images/paas"):
    with Cluster("Environnement lab/dev/acc/prd"):
        Node("Worker")