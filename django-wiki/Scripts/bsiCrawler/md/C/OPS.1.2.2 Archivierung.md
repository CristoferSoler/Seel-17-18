1 Beschreibung
--------------

### 1.1 Einleitung

Die Archivierung spielt im Dokumentenmanagement-Prozess eine besondere Rolle: Denn es wird erwartet, dass einerseits die Dokumente bis zum Ablauf einer vorgegebenen Aufbewahrungsfrist verfügbar sind und andererseits soll deren Vertraulichkeit und Integrität bewahrt bleiben. Zusätzlich muss der Kontext erhalten werden, damit der jeweilige gespeicherte Vorgang wieder rekonstruierbar ist.

Während der gesamten Dauer der Langzeitspeicherung müssen entsprechend Maßnahmen zur Informationserhaltung und, falls erforderlich, Maßnahmen zur Beweiswerterhaltung umgesetzt werden.

Im deutschen informationstechnischen Sprachgebrauch wird mitunter der Begriff elektronische Archivierung synonym zum Begriff elektronische Langzeitspeicherung verwendet. Zur besseren Verständlichkeit wird in diesem Baustein daher allgemein nur von Archivierung oder auch digitalem Langzeitarchiv gesprochen. Ein IT-Verfahren zur Aufbewahrung elektronischer Dokumente wird als Archivsystem bzw. digitales Archiv bzw. Langzeitspeicher bezeichnet. Die Aufbewahrungsdauer der Dokumente bemisst sich nach den rechtlichen und sonstigen Vorgaben sowie dem Anwendungszweck der Daten. 

Der in diesem Baustein verwendete Begriff Dokumente subsumiert Daten und Dokumente, sofern sie nicht ausdrücklich in anderer Bedeutung gebraucht werden.

Aus rechtlicher Sicht ist der Begriff Archivierung in Deutschland durch die Archivgesetze des Bundes und der Länder konkretisiert und belegt. Daher ist er von der in diesem Dokument betrachteten zeitlich beschränkten Aufbewahrung zu unterscheiden. Archivierung im juristisch korrekten Sinne betrifft allein Unterlagen der öffentlichen Verwaltung und bezieht sich darauf, dass Unterlagen einer Behörde, sobald sie für die Zwecke der Behörde nicht mehr benötigt werden, ausgesondert und durch eine zuständige staatliche Einrichtung (Bundesarchiv) auf unbegrenzte Zeit verwahrt werden sollen (vgl. §§ 1 und 2 BArchG).

### 1.2 Zielsetzung

Der Baustein beschreibt, wie Dokumente langfristig, sicher, unveränderbar und wieder reproduzierbar archiviert werden können. Dazu werden Anforderungen definiert, mit denen sich ein Archivsystem sicher planen, umsetzen und betreiben lässt.

### 1.3 Abgrenzung

Der Baustein Archivierung beschreibt Sicherheitsmaßnahmen zur Aufbewahrung und Erhaltung von elektronischen Dokumenten für die Langzeitspeicherung im Rahmen von geltenden Aufbewahrungsfristen. Maßnahmen für eine operative Datensicherung werden nicht in diesem Baustein behandelt. Anforderungen dazu werden in OPS.1.1.6 Datensicherung dargestellt. dargestellt.

Ein digitaler Langzeitspeicher besteht aus einzelnen Komponenten, z. B. einer Datenbank. Wie sich solche Komponenten detailliert sicher betreiben lassen, ist jedoch ebenfalls nicht Thema des vorliegenden Bausteins. Dazu können z. B. zusätzlich die Anforderungen aus den Bausteinen APP.4.3 Relationale Datenbanksysteme, SYS.1.1 Allgemeiner Server sowie SYS.1.8 Speichersysteme ergänzt werden.systeme, SYS.1.1 Allgemeiner Server sowie SYS.1.8 Speichersysteme ergänzt werden., SYS.1.1 Allgemeiner Server sowie SYS.1.8 Speichersysteme ergänzt werden. sowie SYS.1.8 Speichersysteme ergänzt werden. ergänzt werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Archivierung von besonderer Bedeutung:

### 2 1 Unzureichende Migration von Archivsystemen

Archivierte Daten sollen typischerweise über einen sehr langen Zeitraum gespeichert bleiben. Während dieses Zeitraums können die zugrundeliegenden technischen Systemkomponenten, Speichermedien und Datenformate physisch oder technisch altern und dadurch unbrauchbar werden. Außerdem können sich im Laufe der Zeit Probleme mit der Kompatibilität der verwendeten Datenformate ergeben.

Wenn auf die Alterung des bestehenden Systems nicht reagiert wird, ist langfristig damit zu rechnen, dass beispielsweise archivierte Rohdaten nicht mehr von den Archivmedien lesbar sind oder archivierte Daten durch physische Fehler an Archivsystem und -medien verändert werden.

### 2 2 Unzureichende Ordnungskriterien für Archive

Elektronische Archive können sehr große Datenmengen enthalten. Die einzelnen Datensätze werden dabei nach bestimmten Ordnungskriterien abgelegt, die in Indexdaten der Geschäftsanwendungen und Indexdaten des Archivsystems zu unterscheiden sind. Werden ungeeignete Ordnungskriterien verwendet, können archivierte Dokumente eventuell nicht oder nur sehr aufwändig wieder recherchiert werden oder die Semantik der Dokumente ist nicht eindeutig bestimmbar. Ebenso besteht die Gefahr, dass durch eine ungeeignete oder begrenzte Auswahl von Ordnungskriterien Aufbewahrungsziele verfehlt werden, z. B. die Nachweisfähigkeit gegenüber Dritten.

### 2 3 Unzureichende Dokumentation von Archivzugriffen

Unbefugte Archivzugriffe werden üblicherweise mithilfe von Protokolldateien aufgedeckt. Wurde jedoch nicht umfangreich genug protokolliert, besteht die Gefahr, dass solche Zugriffe nicht aufgedeckt werden. In der Folge könnten Angreifer unbemerkt an die dort gespeicherten Informationen gelangen und sie z. B. kopieren oder verändern. 

### 2 4 Unzulängliche Übertragung von Papierdaten in ein elektronisches Archiv

Wenn Dokumente eingescannt werden, kann dabei das Erscheinungsbild oder die Semantik der aufgenommenen Daten verfälscht werden oder auch Dokumente verloren gehen. Dadurch kommt es zu falschen Interpretationen und Berechnungen, z. B. wenn wichtige Teile des Dokuments oder des Dokumentenstapel beim Scannen vergessen werden.

### 2 5 Unzureichende Erneuerung von kryptographischen Verfahren bei der Archivierung

Kryptographische Verfahren, die z. B. bei Signaturen, Siegeln, Zeitstempeln, technischen Beweisdaten (Evidence Records) oder Verschlüsselungen verwendet werden, müssen regelmäßig an den aktuellen Stand der Technik angepasst werden, damit die Schutzwirkung erhalten bleibt. Wird das versäumt, kann beispielsweise aufgrund einer veralteten unsicheren Signatur, die Integrität des Dokumentes angezweifelt werden, sodass die Datei nicht als Beweismittel vor Gericht zugelassen wird. Auch geht so die Vertraulichkeit eines verschlüsselten Dokumentes verloren.

### 2 6 Unzureichende Durchführung von Revisionen bei der Archivierung

Wenn der Archivierungsprozess zu selten oder zu ungenau überprüft wird, kann das mittelbar dazu führen, dass der gesamte Prozess nicht mehr ordnungsgemäß funktioniert. Damit kann die Integrität der archivierten Dokumente selbst angezweifelt werden. Hieraus können sich für die Institution rechtliche und wirtschaftliche Nachteile ergeben: So kann unter Umständen eine Datei nicht als Beweismittel vor Gericht zugelassen werden, weil nicht ausgeschlossen werden kann, dass sie manipuliert wurde.

### 2 7 Verstoß gegen rechtliche Rahmenbedingungen beim Einsatz von Archivierung

Bei der Archivierung von elektronischen Dokumenten sind verschiedene rechtliche Rahmenbedingungen zu beachten. Werden diese nicht eingehalten, kann das zivil- oder strafrechtliche Konsequenzen haben, z. B. bei Mindestaufbewahrungsfristen, die sich aus steuerlichen, haushaltsrechtlichen oder sonstigen Gründen ergeben.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Archivierung aufgeführt. Grundsätzlich ist der Archivverwalter dafür zuständig, die Anforderungen zu erfüllen. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.2.2.A1 Ermittlung von Einflussfaktoren für die elektronische Archivierung

Bevor entschieden wird, welche Verfahren und Produkte für die elektronische Archivierung eingesetzt werden, MÜSSEN die technischen, rechtlichen und organisatorischen Einflussfaktoren ermittelt und dokumentiert werden. Die Ergebnisse MÜSSEN in das Archivierungskonzept einfließen. 

#### OPS.1.2.2.A2 Entwicklung eines Archivierungskonzepts

Es MUSS definiert werden, welche Ziele mit der Archivierung erreicht werden sollen. Hierbei MUSS insbesondere berücksichtigt werden, welche Regularien einzuhalten sind, welche Mitarbeiter verantwortlich sind und welcher Funktions- und Leistungsumfang angestrebt wird. 

Die Ergebnisse MÜSSEN in einem Archivierungskonzept erfasst werden. Das Management MUSS in diesen Prozess einbezogen werden. Das Archivierungskonzept MUSS regelmäßig an die aktuellen Gegebenheiten der Institution angepasst werden.

#### OPS.1.2.2.A3 Geeignete Aufstellung von Archivsystemen und Lagerung von Archivmedien [Leiter IT, IT-Betrieb]

Da Archivsysteme schützenswerte Daten einer Institution zentral aufbewahren, MÜSSEN deren IT-Komponenten in gesicherten Räumen aufgestellt werden. Es MUSS sichergestellt sein, dass nur berechtigte Personen die Räume betreten dürfen. Damit Archiv-Speichermedien langfristig aufbewahrt werden können, MÜSSEN sie geeignet gelagert werden. 

#### OPS.1.2.2.A4 Konsistente Indizierung von Daten bei der Archivierung [Leiter IT, IT-Betrieb, Benutzer]

Alle in einem Archiv abgelegten Daten, Dokumente und Datensätze MÜSSEN eindeutig indiziert werden, um sie bei späteren Suchanfragen schnell wiederfinden zu können. Dazu MUSS bereits während der Konzeption festgelegt werden, welche Struktur und welchen Umfang die Indexangaben für ein Archiv haben sollen.

#### OPS.1.2.2.A5 Regelmäßige Aufbereitung von archivierten Datenbeständen [Leiter IT]

Es MUSS über den gesamten Archivierungszeitraum hinweg sichergestellt werden, dass 

* das verwendete Datenformat von den benutzten Anwendungen verarbeitet werden kann,
* die gespeicherten Daten auch zukünftig lesbar und so reproduzierbar sind, dass Semantik und Beweiskraft beibehalten werden können,
* das benutzte Dateisystem auf dem Speichermedium von allen beteiligten Komponenten verarbeitet werden kann,
* die Speichermedien jederzeit technisch einwandfrei gelesen werden können und
* die verwendeten kryptographischen Verfahren zur Verschlüsselung und zum Beweiswerterhalt mittels digitaler Signatur, Siegel, Zeitstempel oder technischen Beweisdaten (Evidence Records) dem Stand der Technik entsprechen.
#### OPS.1.2.2.A6 Schutz der Integrität der Indexdatenbank von Archivsystemen [Leiter IT, IT-Betrieb]

Die Integrität der Indexdatenbank MUSS sichergestellt und überprüfbar sein. Außerdem MUSS die Indexdatenbank regelmäßig gesichert werden. Die Datensicherungen MÜSSEN wiederherstellbar sein. Mittlere und große Archive MÜSSEN über redundante Indexdatenbanken verfügen. 

#### OPS.1.2.2.A7 Regelmäßige Datensicherung der System- und Archivdaten [Leiter IT, IT-Betrieb]

Alle Archivdaten, die zugehörigen Indexdatenbanken sowie die Systemdaten MÜSSEN regelmäßig gesichert werden (siehe OPS.1.1.6 *Datensicherung). *). 

#### OPS.1.2.2.A8 Protokollierung der Archivzugriffe [Leiter IT, IT-Betrieb]

Alle Zugriffe auf elektronische Archive MÜSSEN protokolliert werden. Dafür SOLLTEN Datum, Uhrzeit, Benutzer, Clientsystem und die ausgeführten Aktionen sowie Fehlermeldungen aufgezeichnet werden. Die Aufbewahrungsdauer der Protokolldaten SOLLTE im Archivierungskonzept festgelegt werden. 

Die Protokolldaten der Archivzugriffe SOLLTEN regelmäßig ausgewertet werden. Dabei SOLLTEN die institutionsinternen Vorgaben beachtet werden. 

Auch SOLLTE definiert sein, welche Ereignisse (z. B. Systemfehler, Timouts oder Datensätze kopieren) welchen Mitarbeitern angezeigt signalisiert werden. Kritische Ereignisse SOLLTEN sofort nach der Signalisierung geprüft und, falls nötig, weiter eskaliert werden. 

#### OPS.1.2.2.A9 Auswahl geeigneter Datenformate für die Archivierung von Dokumenten [Leiter IT, IT-Betrieb]

Für die Archivierung MUSS ein geeignetes Datenformat ausgewählt werden. Es MUSS gewährleisten, dass sich Archivdaten sowie ausgewählte Merkmale des ursprünglichen Dokumentmediums langfristig und originalgetreu reproduzieren lassen.

Die Dokumentstruktur des ausgewählten Datenformats MUSS eindeutig interpretierbar und elektronisch verarbeitbar sein. Die Syntax und Semantik der verwendeten Datenformate SOLLTE dokumentiert und von einer Standardisierungsorganisation veröffentlicht sein. Es SOLLTE für eine beweis- und revisionssichere Archivierung ein verlustfreies Bild-Kompressionsverfahren benutzt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Archivierung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.2.2.A10 Erstellung einer Richtlinie für die Nutzung von Archivsystemen [Leiter IT, IT-Betrieb]

Es SOLLTE sichergestellt werden, dass Mitarbeiter das Archivsystem so benutzen, wie es im Archivierungskonzept vorgesehenen ist. Dazu SOLLTE eine Administrations- und eine Benutzerrichtlinie erstellt werden. Die Administrationsrichtlinie SOLLTE folgende Punkte enthalten:

* Festlegung der Verantwortung für Betrieb und Administration,
* Vereinbarungen über Leistungsparameter beim Betrieb (Service Level Agreements),
* Modalitäten der Vergabe von Zutritts- und Zugriffsrechten,
* Modalitäten der Vergabe von Zugangsrechten zu den vom Archiv bereitgestellten Diensten,
* Regelungen zum Umgang mit archivierten Daten und Archivmedien,
* Überwachung des Archivsystems und der Umgebungsbedingungen,
* Regelung zur Datensicherung
* Regelungen zur Protokollierung
* Trennung von Produzenten und Konsumenten (OAIS-Modell).
#### OPS.1.2.2.A11 Einweisung in die Administration und Bedienung des Archivsystems [Leiter IT, IT-Betrieb, Benutzer]

Die verantwortlichen IT-Betrieben und die Benutzer SOLLTEN für ihren Aufgabenbereich geschult werden. 

Die Schulung der IT-Betrieben SOLLTE folgende Themen umfassen: 

* Systemarchitektur und Sicherheitsmechanismen des verwendeten Archivsystems und des darunterliegenden Betriebssystems,
* Installation und Bedienung des Archivsystems und Umgang mit Archivmedien,
* Dokumentation der Administrationstätigkeiten und
* Eskalationsprozeduren.
Die Schulung der Benutzer SOLLTE folgende Themen umfassen: 

* Umgang mit dem Archivsystem, 
* Bedienung des Archivsystems, 
* rechtliche Rahmenbedingungen der Archivierung. 
Die Durchführung und Teilnahme an den Schulungen SOLLTEN dokumentiert werden. 

#### OPS.1.2.2.A12 Überwachung der Speicherressourcen von Archivmedien [Leiter IT, IT-Betrieb]

Die auf den Archivmedien vorhandene freie Speicherkapazität MUSS kontinuierlich überwacht werden. Sobald ein definierter Grenzwert unterschritten wird, MUSS ein verantwortlicher Mitarbeiter automatisch alarmiert werden. Es SOLLTE darauf geachtet werden, dass die Alarmierung rollenbezogen erfolgt. Es MÜSSEN immer ausreichend leere Archivmedien verfügbar sein, um Speicherengpässen schnell vorbeugen zu können. 

#### OPS.1.2.2.A13 Regelmäßige Revision der Archivierungsprozesse

ES SOLLTE regelmäßig überprüft werden, ob die Archivierungsprozesse noch korrekt und ordnungsgemäß funktionieren. Dazu SOLLTE eine Checkliste erstellt werden, die Fragen zu Verantwortlichkeiten, Organisationsprozessen, Einsatz der Archivierung, Redundanz der Archivdaten, Administration und der technischen Beurteilung des Archivsystems enthält. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

#### OPS.1.2.2.A14 Regelmäßige Beobachtung des Markes für Archivsystemen [Leiter IT]

Der Markt für Archivsysteme SOLLTE regelmäßig und systematisch beobachtet werden. Dabei SOLLTEN unter anderem folgende Kriterien beobachtet werden: Veränderungen bei Standards, Technologiewechsel bei Herstellern von Hard- und Software, veröffentlichte Sicherheitslücken oder Schwachstellen sowie Verlust der Sicherheitseignung bei kryptographischen Algorithmen.

#### OPS.1.2.2.A15 Regelmäßige Aufbereitung von kryptographisch gesicherten Daten bei der Archivierung [Leiter IT, IT-Betrieb]

Es SOLLTE kontinuierlich beobachtet werden, wie sich das Gebiet der Kryptographie entwickelt, um beurteilen zu können, ob ein Algorithmus weiterhin zuverlässig und ausreichend sicher ist (siehe auch OPS.1.2.2.A20 Geeigneter Einsatz kryptographischer Verfahren).

Archivdaten, die mit kryptographischen Verfahren gesichert wurden, deren Sicherheitseignung in absehbarer Zeit verloren gehen wird, SOLLTEN rechtzeitig mit sicheren Verfahren neu gesichert, z.B. verschlüsselt bzw. signiert, werden. 

#### OPS.1.2.2.A16 Regelmäßige Erneuerung technischer Archivsystem-Komponenten [Leiter IT, IT-Betrieb]

Archivsysteme SOLLTEN über lange Zeiträume auf dem aktuellen technischen Stand gehalten werden. Neue Hard- und Software SOLLTE vor der Installation in ein laufendes Archivsystem ausführlich getestet werden. Wenn neue Komponenten in Betrieb genommen oder neue Dateiformate eingeführt werden, SOLLTE ein Migrationskonzept erstellt werden. Darin SOLLTEN alle Änderungen, Tests und erwartete Testergebnisse beschrieben sein. Die Konvertierung der einzelnen Daten SOLLTE dokumentiert (Transfervermerk) werden.

Wenn Archivdaten in neue Formate konvertiert werden, SOLLTE geprüft werden, ob aufgrund rechtlicher Anforderungen zusätzlich die Daten in ihren ursprünglichen Formaten zu archivieren sind.

#### OPS.1.2.2.A17 Auswahl eines geeigneten Archivsystems [Leiter IT]

Ein neues Archivsystem SOLLTE immer aufgrund der im Archivierungskonzept beschriebenen Vorgaben ausgewählt werden. Es SOLLTE die dort formulierten Anforderungen erfüllen. 

#### OPS.1.2.2.A18 Verwendung geeigneter Archivmedien [Leiter IT, IT-Betrieb]

Für die Archivierung SOLLTEN geeignete Medien ausgewählt und benutzt werden. Dabei SOLLTEN die Aspekte zu archivierendes Datenvolumen, mittlere Zugriffszeiten und mittlere gleichzeitige Zugriffe auf das Archivsystem beachtet werden. Ebenfalls SOLLTEN die Archivmedien die Anforderungen an eine Langzeitarchivierung hinsichtlich Revisionssicherheit und Lebensdauer erfüllen. 

#### OPS.1.2.2.A19 Regelmäßige Funktions- und Recoverytests bei der Archivierung [Leiter IT, IT-Betrieb]

Für die Archivierung SOLLTE es regelmäßige Funktions- und Recoverytests geben. Die Archivierungsdatenträger SOLLTEN mindestens einmal jährlich überprüft werden, ob sie noch lesbar und integer sind. Für die Fehlerbehebung SOLLTEN geeignete Prozesse definiert werden. 

Weiterhin SOLLTEN die Hardwarekomponenten des Archivsystems regelmäßig auf ihre einwandfreie Funktion hin geprüft werden. Es SOLLTE regelmäßig geprüft werden, ob alle Archivierungsprozesse fehlerfrei funktionieren.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.2.2.A20 Geeigneter Einsatz kryptographischer Verfahren bei der Archivierung [Leiter IT](CI)

Um lange Aufbewahrungsfristen abdecken zu können, SOLLTEN Archivdaten nur mit kryptographischen Verfahren auf Basis aktueller Standards und Normen gesichert werden.

#### OPS.1.2.2.A21 Übertragung von Papierdaten in elektronische Archive(CI)

Werden Dokumente auf Papier und Gegenstände des Augenscheins digitalisiert und in ein elektronisches Archiv überführt, SOLLTE sichergestellt werden, dass die digitale Kopie mit dem Originaldokument bildlich und inhaltlich übereinstimmt. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Archivierung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [AlgKat] Bekanntmachung zur elektronischen Signatur nach dem Signaturgesetz und der Signaturverordnung

  

 Übersicht über geeignete Algorithmen, BNetzA, 2017  
 [https://www.bundesnetzagentur.de/DE/Service-Funktionen/ElektronischeVertrauensdienste/QES/WelcheAufgabenhatdieBundesnetzagentur/GeeigneteAlgorithmenfestlegen/geeignetealgorithmenfestlegen\_node.html](https://www.bundesnetzagentur.de/DE/Service-Funktionen/ElektronischeVertrauensdienste/QES/WelcheAufgabenhatdieBundesnetzagentur/GeeigneteAlgorithmenfestlegen/geeignetealgorithmenfestlegen_node.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Archivierung" von Bedeutung.

* G 0.2 Ungünstige klimatische Bedingungen
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.37 Abstreiten von Handlungen
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

