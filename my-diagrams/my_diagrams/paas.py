from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.vcs import Git

with Diagram("PaaS/Kubernetes", show=False, filename="images/paas"):
    jenkins = Jenkins("Jenkins")
    bitbucket = Git("Bitbucket \n [Code applicatif]")

    with Cluster("Worker/Noeud (lab/dev/acc/prd)"):
        noeud = [Pod("web"),Pod("api")]
    
    bitbucket << Edge(label="sync") << jenkins >> Edge(label="deploie") >> noeud