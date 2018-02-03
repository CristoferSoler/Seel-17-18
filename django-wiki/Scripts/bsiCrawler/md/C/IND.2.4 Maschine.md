1 Beschreibung
--------------

### 1.1 Einleitung

Eine Maschine ist eine technische Vorrichtung, die automatisierte Aufgaben durchführt. Ein typisches Beispiel dafür ist eine Werkzeugmaschine, die Produkte auf eine vorgegebene Art bearbeitet. Dabei wird sie von einem IT-System unter Nutzung eines Programms gesteuert, das die entsprechenden Arbeitsanweisungen und -Schritte vorgibt. Solche Maschinen werden auch als Automaten bezeichnet. 

Meistens werden Maschinen von Maschinenbauern konstruiert und mit bestimmten vordefinierten Funktionen ausgestattet. Der Betreiber der Maschine kann allerdings noch die Parameter bestimmen, nach denen sie arbeiten soll. So lassen sich beispielsweise Formen, die gefräst werden sollen oder Kalibrierungen für bestimmte Materialien einstellen. Damit der Betreiber die Parameter verändern kann, verfügen Maschinen über verschiedene Schnittstellen, z. B. für Wechseldatenträger, spezialisierte Programmiergeräte oder Netzzugriffe.

Häufig werden von Maschinenbauern auch Fernwartungsdienstleistungen angeboten, um frühzeitigen Verschleiß zu erkennen oder in Problemsituationen schnell reagieren zu können.

### 1.2 Zielsetzung

Der Baustein beschreibt, wie elektronisch gesteuerte, halb- oder vollautomatische Maschinen (z. B. CNC-Maschinen) unabhängig von Hersteller, Bauart, speziellem Einsatzzweck und -ort abgesichert werden können.

### 1.3 Abgrenzung

Der vorliegende Baustein ergänzt den übergeordneten Baustein IND.2.1 *Allgemeine* *ICS-Komponente *und setzt voraus, dass dieser umgesetzt wurde. Darüber hinaus werden nur Anforderungen für Maschinen definiert, auf deren interne Strukturen eine Institution nicht zugreifen kann. 

Auch werden keine Sicherheitsanforderungen für Betriebs- und Steuerungstechnik beschrieben. Dafür muss der Baustein IND.1 *Betriebs- und Steuerungstechnik *umgesetzt werden. Ebenso wird der Bereich funktionale Sicherheit (Safety) nicht behandelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Maschine von besonderer Bedeutung:

### 2 1 Ausfall oder Störung durch ungenügende Wartung

Wenn Maschinen nicht regelmäßig gewartet werden, funktionieren sie früher nicht mehr korrekt oder fallen ganz aus. Durch Fehlfunktionen können z. B. Mitarbeiter gefährdet oder die Produktion kann erheblich beeinträchtigt werden. 

### 2 2 Gezielte Manipulationen

Sind die Schnittstellen einer Maschine ungenügend geschützt, können Angreifer die Parameter der Maschine manipulieren, z. B. über lokale Programmiergeräte oder Netzdienste. Dadurch können Werkstücke beschädigt werden oder ganze Produktreihen fehlerhaft sein. Die Angreifer können aber auch die Maschine selbst beschädigen, sodass auch dadurch ein wirtschaftlicher Verlust entsteht. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Maschine aufgeführt. Grundsätzlich ist der ICS-Informationssicherheitsbeauftragte (ICS-ISB) für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### IND.2.4.A1 Fernwartung durch Maschinen- und Anlagenbauer [ICS-Administrator]

Für die Fernwartung einer Maschine SOLLTE es eine zentrale Richtlinie geben. Darin SOLLTE geregelt werden, wie die jeweiligen Fernwartungslösungen einzusetzen sind und wie Kommunikationsverbindungen geschützt werden. Sie SOLLTE auch beschreiben, welche Aktivitäten während der Fernwartung überwacht werden sollen. 

Außerdem SOLLTE NICHT möglich sein, dass über die Fernwartung einer Maschine auf andere Systeme oder Maschinen der Institution zugegriffen werden kann. 

Mit einem Dienstleister SOLLTE vereinbart werden, wie er die in der Maschine gespeicherten Informationen verwerten darf. 

#### IND.2.4.A2 Betrieb nach Ende der Gewährleistung [ICS-Administrator]

Es SOLLTE ein Prozess etabliert werden, der gewährleistet, dass die Maschine auch über den Gewährleistungszeitraum hinaus sicher weiterbetrieben werden kann. Hierzu SOLLTEN mit dem Lieferanten weitere Unterstützungsleistungen vertraglich vereinbart werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Maschine. Sie SOLLTEN grundsätzlich umgesetzt werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Maschine" finden sich unter anderem in folgenden Veröffentlichungen:

5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Maschine" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

