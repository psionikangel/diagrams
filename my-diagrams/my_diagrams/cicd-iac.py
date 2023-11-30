# CI/CD et IaC
from diagrams import Diagram, Cluster
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.iac import Awx
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.compute import Server
from diagrams.k8s.infra import Node


with Diagram("CI/CD et IaC", show=False, filename="images/cicd-iac"):

    vms = Server("Machine Virtuelle")

    with Cluster("K8S"):
        pod = Node()
        argo = ArgoCD("ArgoCD")
        jenkins = Jenkins("Jenkins")
        awx = Awx("AWX")
        argo >> pod << jenkins
        awx 

    
    awx >> vms