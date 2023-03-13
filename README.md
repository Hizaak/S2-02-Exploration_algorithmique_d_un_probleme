# S2.02 - Exploitation d'un problème algorithmique
## À propos de ce dépôt
Ce dépôt a été créé à l'occasion de la S2.02, un projet mettant en relation l'exploitation de données publiques, la visualisation via interface graphique et l'utilisation de méthodes algorithiques avancées.

## Les auteurs

Ce projet a été réalisé par : [Alexandre Maurice](https://github.com/Hizaak) et [Nicolas Dargazanli](https://github.com/noenic).

## Les données utilisées
Nous avons utilisé des données au format [GTFS](https://gtfs.org/), issues de la société de transports [Chronoplus](https://fr.wikipedia.org/wiki/Chronoplus) (maintenant devenue [Txix Txak](https://www.txiktxak.fr/)). Voir la [source](https://www.data.gouv.fr/fr/datasets/offre-transport-du-reseau-txik-txak-nord-ex-chronoplus-gtfs/) des données.

## Les outils utilisés
Nous avons utilisé [Python](https://www.python.org/) pour l'exploitation des données, ainsi que la bibliothèque [Graphics](https://pypi.org/project/graphics.py/) pour la visualisation.

## Les méthodes utilisées
- [Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra) :
Algorithme de recherche de plus court chemin dans un graphe pondéré. Il fonctionne en sélectionnant le nœud le plus proche du nœud de départ, en mettant à jour les coûts des chemins pour atteindre ses voisins, puis en répétant ce processus pour chaque nœud jusqu'à ce que le nœud d'arrivée soit atteint ou que tous les nœuds aient été explorés.
- [Bellman-Ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford) :
Algorithme de recherche de plus court chemin dans un graphe pondéré qui **peut traiter tous les sommets du graphe en même temps**. Il fonctionne en calculant les **distances les plus courtes entre toutes les paires de sommets en utilisant une méthode de programmation dynamique**. Cela permet de trouver le chemin le plus court entre n'importe quelle paire de sommets dans le graphe.
- [Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall) :
Algorithme de recherche de plus court chemin dans un graphe pondéré, qui peut **gérer les graphes avec des arêtes de poids négatif**. Il fonctionne en effectuant **une relaxation sur chaque arête du graphe pour mettre à jour les distances les plus courtes** jusqu'à ce qu'il n'y ait plus de changements à apporter. Cet algorithme peut également détecter la présence de cycles de poids négatif dans le graphe.
- [A*](https://fr.wikipedia.org/wiki/Algorithme_A*) était censée être implémentée, mais n'a pas été utilisée car la version visuelle n'a pas été implémentée.
C'est un algorithme de recherche de chemin qui **utilise une heuristique pour guider la recherche en direction de la solution la plus probable**. Il utilise une fonction d'estimation de coût pour chaque nœud, qui est la somme du coût réel pour atteindre ce nœud et d'une estimation du coût restant pour atteindre la destination finale. L'algorithme explore d'abord les nœuds les moins coûteux en utilisant cette fonction, en évaluant les nœuds voisins pour trouver le chemin le plus court jusqu'à la destination finale.

## Les résultats
### Dijkstra
![Dijkstra](https://github.com/Hizaak/S2-02-Exploration_algorithmique_d_un_probleme/blob/main/Sources/Dijkstra.PNG)

### Bellman-Ford
![Bellman-Ford](https://github.com/Hizaak/S2-02-Exploration_algorithmique_d_un_probleme/blob/main/Sources/Bellman.PNG)

### Floyd-Warshall
![Floyd-Warshall](https://github.com/Hizaak/S2-02-Exploration_algorithmique_d_un_probleme/blob/main/Sources/Floyd.PNG)

## Les limitations
- Chronoplus / Txik Txak ne fournit pas d'API, et donc l'application n'évolue pas au fur et à mesure des changements de l'offre de transport.
- L'application ne prend pas en compte les horaires de passage des bus, puisque cela n'était pas demandé dans le sujet, mais cela aurait été intéressant à implémenter.
