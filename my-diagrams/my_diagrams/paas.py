from diagrams import Cluster, Diagram
from diagrams.k8s.infra import Node
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Git

with Diagram("PaaS/Kubernetes", show=False, filename="images/paas"):
    jenkins = Jenkins("Jenkins")
    bitbucket = Git("Bitbucket")

    with Cluster("Environnement lab/dev/acc/prd"):
        noeud = Node("Worker")
    
    bitbucket << jenkins >> noeud