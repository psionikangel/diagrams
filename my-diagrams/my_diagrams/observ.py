# Observabilité
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.logging import Graylog, FluentBit
from diagrams.programming.language import NodeJS


with Diagram("Observabilité", show=False, filename="images/observ"):
    log = Graylog()
    with Cluster("K8S"):
        prom = Prometheus("Prometheus\n[Métriques]")
        graf = Grafana("Grafana\n[Dashboards]")
        status = NodeJS("Page d'état")
        fluent = FluentBit()

        graf >> prom << status
        fluent >> Edge(label="logs") >> log