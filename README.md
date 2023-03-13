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
- [Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
- [Bellman-Ford](https://fr.wikipedia.org/wiki/Algorithme_de_Bellman-Ford)
- [Floyd-Warshall](https://fr.wikipedia.org/wiki/Algorithme_de_Floyd-Warshall)
- [A*](https://fr.wikipedia.org/wiki/Algorithme_A*) était censée être implémentée, mais n'a pas été utilisée car la version visuelle n'a pas été implémentée.

## Les résultats
### Dijkstra
![Dijkstra](https://i.imgur.com/0ZQZQ9I.png)

### Bellman-Ford
![Bellman-Ford](https://i.imgur.com/0ZQZQ9I.png)

### Floyd-Warshall
![Floyd-Warshall](https://i.imgur.com/0ZQZQ9I.png)

## Les limitations
- Chronoplus / Txik Txak ne fournit pas d'API, et donc l'application n'évolue pas au fur et à mesure des changements de l'offre de transport.
- L'application ne prend pas en compte les horaires de passage des bus, puisque cela n'était pas demandé dans le sujet, mais cela aurait été intéressant à implémenter.
