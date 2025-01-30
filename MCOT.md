## Motivation (au maximum 50 mots)

1) Première version:
Avec l'avènement qui semble imminent de la suprématie quantique, la recherche d'algorithmes
plus robustes et théoriquement prouvés comme difficiles s'est intensifiée et suscite
de plus en plus d'intérêt. En particulier, l'obfuscation de circuits s'inscrit dans la
cryptographie. La théorie des tresses propose des moyens raffinés pour
parvenir à cette sûreté escomptée.

2) Deuxième version:
Face à l'émergence des ordinateurs quantiques, les protocoles classiques sont menacés. L'obfuscation de circuits,
essentielle pour garantir la confidentialité des systèmes embarqués, constitue un enjeu clé en cryptographie.
La théorie des tresses offre des outils mathématiques prometteurs pour concevoir des obfuscations robustes et résistantes aux attaques post-quantiques.

3) Troisième version:
De nombreuses machines nécessitent pour leur sécurité de composants cryptographiques qui 
dans le cas souvent récurrents de systèmes embarqués nécessitent que le fonctionnement
de ses composants reste caché pour garantir la sécurité. C'est pour cela que nous nous somment intéressés
à la manière dont on peut transformer un circuit en un circuit équivalent qu'il serait très difficile à
comprendre.

4) Quatrième version:
Avec l’essor des ordinateurs quantiques, garantir la confidentialité des systèmes embarqués nécessite des algorithmes robustes.
L’obfuscation de circuits, qui consiste à rendre leur fonctionnement incompréhensible tout en préservant leur utilité, s’avère essentielle.
La théorie des tresses offre des outils prometteurs pour développer des solutions sécurisées et résistantes aux attaques post-quantiques.

5) Tentative de synthèse :
Avec l’essor des ordinateurs quantiques, garantir la confidentialité des systèmes embarqués nécessite des algorithmes robustes.
L'obfuscation de circuits dont le but est d'empêcher la rétro-ingénierie d'un circuit logique permet grâce à ( aux propriétés algébriques de ) la théorie mathématique
des tresses ( du groupe des tresses ) d'obtenir un composant fonctionnellement identique, mais humainement illisible/incompréhensible. 

## Rapport au thème (au maximum 50 mots)

Ce travail explore la transformation de circuits en versions plus sécurisées,
une approche essentielle pour accompagner la transition vers une cryptographie
post-quantique. En combinant des outils mathématiques issus de la théorie des
tresses, il vise à répondre aux enjeux de sécurité face aux menaces des technologies émergentes.

## Bibliographie commentée (au maximum 650 mots)

L’étude des tresses, un domaine fascinant des mathématiques qui repose sur le comportement de ficelles que l'on tresse et qui étudie la manière 
dont elles se combinent entre elles. Son étude théorique remonte à l’époque d'Emil Artin qui, en 1925, publia une première formalisation 
de la théorie des groupes de tresses dans « Theory of Braids ». Plus tard, en 1969, F. A. Garside proposa une présentation constructive 
du groupe des tresses dans son article fondateur « The Braid Group and Other Groups », introduisant des notions clés comme la forme normale 
et les invariants qui facilitent la résolution de problèmes complexes, notamment le problème de l’isotopie. Ces avancées ont servi de base à 
une multitude de recherches subséquentes, avec des contributions remarquables de Patrick Dehornoy dans les années 1990, qui ont enrichi la théorie 
par des approches algébriques et topologiques innovantes, comme illustré dans son étude « Le problème d'isotopie des tresses » (2010).
La théorie des tresses, au-delà de son aspect purement mathématique, trouve aussi beaucoup d'applications notamment dans la cryptographie où elles 
semble revenir à la mode. (Plus précisément, les tresses sont étudiées pour leur capacité à modéliser des systèmes complexes et à créer des structures 
algorithmiques résistantes à l’analyse.) Dans le contexte de la cryptographie moderne, l’obfuscation de circuits constitue un champ d’application 
prometteur. L’objectif principal de cette technique est de transformer un circuit logique en un équivalent fonctionnellement identique mais difficile 
à comprendre de sorte à avoir une véritable boite noire. Cela s’inscrit dans une réponse globale à la montée des menaces liées aux technologies 
quantiques, susceptibles de briser les systèmes de cryptographie classique. Dans cet esprit, des travaux récents, comme « Circuit Obfuscation Using Braids » 
(2014) de Gorjan Alagic, Stacey Jeffery et Stephen Jordan, ont montré comment les relations des groupes de tresses peuvent être exploitées pour créer 
des circuits indéchiffrables, tout en maintenant leur efficacité computationnelle.
Historiquement, la difficulté majeure dans la théorie des tresses a été de développer des solutions au problème de l’isotopie. Ce problème consiste à déterminer 
si deux diagrammes de tresses sont isotopes, c’est-à-dire s’ils représentent la tresse. Les approches algébriques ont été déterminantes pour proposer des 
invariants utilisables et des structures de groupe facilitant la comparaison entre diagrammes. Les résultats de Garside sur les formes normales des 
tresses nous est particulièrement intéressants.
Ces concepts se retrouvent naturellement dans l’obfuscation de circuits, qui repose sur la difficulté à distinguer deux circuits fonctionnellement équivalents 
( isotopes ) mais représentés de manière différente. L’idée de base, comme le décrit « Partial-indistinguishability obfuscation using braids » (2012)
par les mêmes auteurs (, est de s’appuyer sur des relations mathématiques simples issues des groupes de tresses pour obtenir une obfuscation résistante aux attaques computationnelles. )
Ces travaux exploitent les propriétés des formes normales des tresses pour transformer les circuits en versions obfusquées, garantissant une indistinguabilité 
partielle face aux adversaires. En plus de leur pertinence pour les circuits classiques, ces techniques se généralisent aux circuits quantiques, 
où les propriétés topologiques des tresses jouent un rôle central.
L’efficacité de ces méthodes repose sur l’existence d’algorithmes efficaces pour réduire des tresses quelconques en leurs formes normales. Ces algorithmes, 
basés sur les travaux de Garside, permettent une représentation abstraite des circuits obfusqués fournissant peut d'informations exploitables par des attaquants. 
L’utilisation de groupes comme les groupes de tresses Bn ou leurs variantes, combinée avec des algorithmes efficaces pour résoudre des problèmes 
d’équivalence, constitue une étape cruciale vers des systèmes cryptographiques sécurisés.
Enfin, le lien entre théorie des tresses et cryptographie ouvre des perspectives intéressantes pour d'autres applications, notamment la vérification 
d'intégrité dans des systèmes distribués ou la modélisation de systèmes complexes. Bien que des questions subsistent, notamment sur la robustesse 
des méthodes d’obfuscation face à des adversaires quantiques, les travaux récents offrent une base solide pour explorer ces nouveaux horizons. 
En somme, l’application de la théorie des tresses à l’obfuscation de circuits représente une symbiose unique entre mathématiques fondamentales et 
enjeux pratiques de la cybersécurité moderne.

639 mots.


## Problématique retenue (au maximum 50 mots)

La théorie des tresses offre des perspectives prometteuses en matière de sécurisation de
systèmes d'information dans un contexte post-quantique. Comment la théorie des tresses
peut-elle être exploitée pour développer des outils cryptographiques robustes, adaptés
à la transition post-quantique, tout en répondant aux enjeux d'efficacité et de sécurité algorithmique ?

50 mots

## Objectifs du TIPE Acssiohm (au maximum 100 mots)

## Objectifs du TIPE Marius (au maximum 100 mots)

L’objectif est d’explorer l’application de la théorie des
tresses à l’obfuscation de circuits dans un contexte post-quantique.
En partant des propriétés algébriques des groupes de tresses, le
travail consiste à analyser leur potentiel pour renforcer la sécurité
des circuits, tout en évaluant leur complexité algorithmique. Des exemples
concrets de circuits seront étudiés pour tester la faisabilité et
l’efficacité de ces approches, dans le but de proposer des bases solides
pour des outils cryptographiques à la fois robustes et pratiques,
répondant ainsi aux enjeux de sécurité et d’efficacité des systèmes d’information modernes. 
(91 mots)


### Brouillon général ( au maximum 10^10 mots )
Le problème de garder en sécurité un circuit électronique....etc.
ET/OU
Avec l'avènement de la suprématie quantique, de nombreux algorithmes quantiques
sont à revoir si on veut éviter leur obsolescense face aux ordinateurs quantiques.
Il est donc nécessaire de travailler sur une transition post-quantique, pour 
construire des systèmes robustes face aux attaques quantique, ce qui peut se faire selon [?]
par la constitution de problèmes NP-complets.



Ainsi l'objectif de l'obsufaction de circuit est de prendre un cicuit logique et le 
transformer en un circuit équivalent < plus difficile à comprendre (évitant le rétro-ingénieuring) 
/ qui n'est pas plus utile qu'une boite noire pour en déduire le fonctionnement > 