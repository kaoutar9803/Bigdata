Rapport de Projet : Analyse de Commentaires
Introduction
Ce rapport présente un projet visant à développer un système de classification automatique des commentaires en positifs, négatifs ou neutres en utilisant des techniques de Machine Learning. 
L'objectif est d'appliquer ces méthodes pour automatiser l'évaluation des sentiments exprimés dans les commentaires.

Méthodologie
1. Collecte et Préparation des Données
Source des données : Utilisation d'un ensemble de commentaires annotés manuellement avec des étiquettes de sentiment (positif, négatif, neutre).
Prétraitement des données : Nettoyage du texte en convertissant en minuscules, suppression de la ponctuation et des caractères spéciaux pour uniformiser le format des commentaires.
2. Traitement des Données
Vectorisation : Transformation des commentaires textuels en vecteurs numériques à l'aide de CountVectorizer, une méthode de représentation de texte en bag-of-words.
3. Modèle de Machine Learning
Algorithme choisi : Utilisation du classificateur Multinomial Naive Bayes, adapté aux données textuelles et connu pour sa simplicité et sa performance dans les tâches de classification de texte.
4. Entraînement et Évaluation
Division des données : Séparation en ensembles d'entraînement (80%) et de test (20%).
Entraînement du modèle : Apprentissage sur les données d'entraînement pour ajuster les paramètres du modèle.
Évaluation : Mesure de l'accuracy, de la précision, du rappel et du score F1 sur l'ensemble de test pour évaluer la performance du modèle.
Résultats
Performances du modèle : Le modèle a atteint une précision de X% sur l'ensemble de test, avec des scores significatifs en précision et en rappel pour les classes positives et négatives.
Analyse des erreurs : Identification des principaux types d'erreurs de classification pour orienter les améliorations futures.
