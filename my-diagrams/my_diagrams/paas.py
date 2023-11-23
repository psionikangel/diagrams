from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.infra import Node
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Git

with Diagram("PaaS/Kubernetes", show=False, filename="images/paas"):
    jenkins = Jenkins("Jenkins")
    bitbucket = Git("Bitbucket \n [Code applicatif]")

    with Cluster("Environnement lab/dev/acc/prd"):
        noeud = Node("Worker/Noeud")
    
    bitbucket << Edge(label="sync") << jenkins >> Edge(label="deploie") >> noeud