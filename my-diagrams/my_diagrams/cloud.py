# Infonuagique
from diagrams import Diagram, Cluster
from diagrams.azure.general import Resourcegroups
from diagrams.aws.engagement import Pinpoint
from diagrams.onprem.iac import Terraform

with Diagram("Infonuagique", direction="BT", show=False, filename="images/cloud"):
    tf = Terraform("Terraform")

    with Cluster("Azure"):
        rg = Resourcegroups("Ressources\nInfonuagiques")

    with Cluster("AWS"):
        pin = Pinpoint("SMS")

    tf >> rg
    tf >> pin