# Environnement Grafana+Mariadb

# Installation
On se place dans le répertoire courant, puis on exécute:
```sh
docker compose up -d
```

On vérifie que tout fonctionne avec
```sh
docker ps
```

# Mariadb
On se connecte à la base de données sur localhost (port 3306)

# phpMyAdmin (interface pour Mariadb)
On se connecte sur [http://localhost:8080](http://localhost:8080) pour administer les bases de données Mariadb (user: root, pass: master2)

# Interface Grafana (dashboards)
On se connecte sur [http://localhost:3000](http://localhost:3000) (user: admin, pass: admin)

# Configuration
Dans Grafana, avant de pouvoir réaliser des dashboard, il faudra ajouter une connection MySQL vers votre base de données (projet). 

Le host doit être `db` et la database name `projet`, le user `root` et le password `master2`.

# Grafana: démos et exemples
- [https://grafana.com/grafana/dashboards/](https://grafana.com/grafana/dashboards/)
- [https://grafana.com/blog/2023/12/27/grafana-dashboards-in-2023-memorable-use-cases-of-the-year](https://grafana.com/blog/2023/12/27/grafana-dashboards-in-2023-memorable-use-cases-of-the-year/)
- [https://play.grafana.org/d/bdnahipisghdsa/getting-started-with-grafana-play](https://play.grafana.org/d/bdnahipisghdsa/getting-started-with-grafana-play)
- [https://grafana.com/grafana/dashboards/19870-demo-dashboard/](https://grafana.com/grafana/dashboards/19870-demo-dashboard/)
- [https://www.timescale.com/blog/grafana-webinar-1-recap/](https://www.timescale.com/blog/grafana-webinar-1-recap/)
