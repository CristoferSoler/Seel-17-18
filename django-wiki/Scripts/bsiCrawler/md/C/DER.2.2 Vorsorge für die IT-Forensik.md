1 Beschreibung
--------------

### 1.1 Einleitung

IT-Forensik ist die streng methodisch vorgenommene Datenanalyse auf Datenträgern und in Computernetzen zur Aufklärung von Vorfällen unter Einbeziehung der Möglichkeiten der strategischen Vorbereitung insbesondere aus der Sicht des Anlagenbetreibers eines IT-Systems.

IT-Sicherheitsvorfälle forensisch zu untersuchen, ist immer dann notwendig, wenn eingetretene Schäden bestimmt, Angriffe abgewehrt und künftig vermieden sowie Angreifer identifiziert werden sollen. Ob ein IT-Sicherheitsvorfall forensisch untersucht wird, entscheidet sich während der Vorfall behandelt wird. Eine IT-forensische Untersuchung im Sinne dieses Bausteins besteht aus den folgenden Phasen:

* strategische Vorbereitung: In dieser Phase werden Prozesse geplant und aufgebaut, die sicherstellen, dass eine Institution IT-Sicherheitsvorfälle forensisch analysieren kann. Sie ist auch dann notwendig, wenn die Institution über keine eigenen Forensik-Experten verfügt.
* Initialisierung: Nachdem die verantwortlichen Mitarbeiter entschieden haben, einen IT-Sicherheitsvorfall forensisch zu untersuchen, werden die vorher geplanten Prozesse angestoßen. Weiterhin wird der Untersuchungsrahmen festgelegt und es werden Erstmaßnahmen durchgeführt.
* Spurensicherung: Hier werden die zu sichernden Beweismittel ausgewählt und die Daten forensisch gesichert. Dabei wird zwischen Live-Forensik und Post-Mortem-Forensik unterschieden: Die Live-Forensik stellt sicher, dass flüchtige Daten (z. B. Netzverbindungen, RAM) von einem laufenden IT-System gesichert werden. Bei der Post-Mortem-Forensik hingegen werden forensische Kopien von Datenträgern erstellt.
* Analyse: Die gesammelten Daten werden forensisch analysiert. Dabei werden die Daten sowohl für sich als auch im Gesamtzusammenhang betrachtet. 
* Ergebnisdarstellung: Die relevanten Untersuchungsergebnisse werden zielgruppengerecht aufbereitet und vermittelt. 
### 1.2 Zielsetzung

Der Baustein zeigt auf, welche Vorsorgemaßnahmen notwendig sind, um IT-forensische Untersuchungen zu ermöglichen. Dabei wird vor allem darauf eingegangen, wie die Spurensicherung vorbereitet und durchgeführt werden kann. Führen Forensik-Dienstleister Spurensicherung ganz oder teilweise durch, gelten die Anforderungen auch für die Dienstleister. Durch vertragliche Vereinbarungen und Prüfungen, kann dabei sichergestellt werden, dass sich der Dienstleister auch daran hält.

### 1.3 Abgrenzung

Der Baustein beschreibt keine Anforderungen, die sicherstellen, dass Angriffe erkannt werden. Diese sind im Baustein DER.1 *Detekction von sicherheitsrelevanten Ereignissen* enthalten und werden im vorliegenden Baustein vorausgesetzt. Auch werden keine Kriterien und Prozesse erläutert, anhand derer die Verantwortlichen entscheiden können, ob ein IT-Sicherheitsvorfall forensisch untersucht werden muss oder nicht. Die Entscheidung darüber wird getroffen, während der Sicherheitsvorfall behandelt wird (siehe DER.2.1 *Incident Management*). 

Weiterhin befasst sich der Baustein nur mit Vorsorgemaßnahmen, die grundlegend für spätere IT-forensische Untersuchungen sind. Wie die eigentliche forensische Analyse durchgeführt wird, ist daher nicht Thema dieses Bausteins.

Letztlich geht der Baustein auch nicht darauf ein, wie sich IT-Infrastrukturen bereinigen lassen, nachdem sie angegriffen worden sind (siehe dazu DER.2.3 *Bereinigung weitreichender Sicherheitsvorfälle*). Die dort beschriebenen Tätigkeiten können jedoch durch die Ergebnisse von IT-forensischen Untersuchungen maßgeblich unterstützt werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für die Vorsorge für die IT-Forensik von besonderer Bedeutung:

### 2 1 Verstoß gegen rechtliche Rahmenbedingungen

Für IT-forensische Untersuchungen werden oft alle als notwendig erachteten Daten kopiert, sichergestellt und ausgewertet. Darunter befinden sich meistens auch personenbezogene Daten von Mitarbeitern oder Partnern. Wird darauf z. B. unbegründet und ohne dass der Datenschutzbeauftragte miteinbezogen wird, zugegriffen, verstößt die Institution gegen gesetzliche Regelungen, z. B. wenn dabei die Zweckbindung missachtet wird. Auch ist es möglich, dass aus den erhobenen Daten beispielsweise abgeleitet werden kann, wie sich Mitarbeiter verhalten, oder es kann ein Bezug zu ihnen hergestellt werden. Dadurch besteht die Gefahr, dass auch gegen interne Regelungen verstoßen wird. 

### 2 2 Verlust von Beweismitteln durch fehlerhafte oder unvollständige Beweissicherung

Werden Beweismittel falsch oder nicht schnell genug gesichert, können dadurch wichtige Daten verlorengehen, die später auch nicht wiederherstellbar sind. Schlimmstenfalls führt das zu einer ergebnislosen forensischen Untersuchung. Mindestens ist jedoch die Beweiskraft eingeschränkt. 

Die Gefahr wichtige Beweismittel zu verlieren, steigt stark an, wenn Mitarbeiter Forensik-Werkzeuge fehlerhaft benutzen, Daten zu langsam sichern oder zu wenig üben. Oft gehen auch Beweismittel verloren, wenn die Verantwortlichen flüchtige Daten nicht als relevant erkennen und sichern. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Vorsorge für die IT-Forensik aufgeführt. Grundsätzlich ist der Informationssicherheitsbeauftragte für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### DER.2.2.A1 Prüfung rechtlicher und regulatorischer Rahmenbedingungen zur Erfassung und Auswertbarkeit [Institutionsleitung, Datenschutzbeauftragter]

Werden Daten für forensische Untersuchungen erfasst und ausgewertet, MÜSSEN alle rechtlichen und regulatorischen Rahmenbedingungen identifiziert und eingehalten werden (siehe ORP.5 *Anforderungsmanagement*). Auch DARF NICHT gegen interne Regelungen und Mitarbeitervereinbarungen verstoßen werden. Im Einzelfall kann es jedoch notwendig sein, das Interesse der Institution gegen das der Mitarbeiter abzuwägen. Dabei MUSS der Betriebs- oder Personalrat sowie der Datenschutzbeauftragte einbezogen werden.

#### DER.2.2.A2 Erstellung eines Leitfadens für Erstmaßnahmen bei einem IT-Sicherheitsvorfall

Es MUSS ein Leitfaden erstellt werden, der für die eingesetzten IT-Systeme beschreibt, welche Erstmaßnahmen bei einem IT-Sicherheitsvorfall durchgeführt werden müssen, um möglichst wenig Spuren zu zerstören. Darin MUSS auch beschrieben sein, durch welche Handlungen potenzielle Spuren vernichtet werden können und wie sich das vermeiden lässt.

#### DER.2.2.A3 Vorauswahl von Forensik-Dienstleistern

Verfügt eine Institution nicht über ein eigenes Forensik-Team, MÜSSEN bereits in der Vorbereitungsphase mögliche geeignete Forensik-Dienstleister identifiziert werden. Welche Forensik-Dienstleister infrage kommen, MUSS dokumentiert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Vorsorge für die IT-Forensik. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.2.2.A4 Festlegung von Schnittstellen zum Krisen- und Notfallmanagement

Die Schnittstellen zwischen IT-forensischen Untersuchungen und dem Krisen- und Notfallmanagement SOLLTEN definiert und dokumentiert werden. Hierzu SOLLTE geregelt werden, welche Mitarbeiter für was verantwortlich sind und wie mit ihnen kommuniziert werden soll. Darüber hinaus SOLLTE sichergestellt werden, dass Ansprechpartner erreichbar sind.

#### DER.2.2.A5 Erstellung eines Leitfadens für Beweissicherungsmaßnahmen bei IT-Sicherheitsvorfällen

Es SOLLTE ein Leitfaden erstellt werden, in dem beschrieben wird, wie Beweise gesichert werden sollen. Darin SOLLTEN Vorgehensweisen, technische Werkzeuge, rechtliche Rahmenbedingungen und Dokumentationsvorgaben aufgeführt werden.

#### DER.2.2.A6 Schulung des Personals für die Umsetzung der forensischen Sicherung

Alle verantwortlichen Mitarbeiter SOLLTEN wissen, wie sie Spuren korrekt sichern und Forensik-Werkzeuge richtig einsetzen. Dafür SOLLTEN geeignete Schulungen angeboten werden.

#### DER.2.2.A7 Auswahl von Forensik-Werkzeugen

Es SOLLTE sichergestellt werden, dass Werkzeuge, mit denen Spuren forensisch gesichert und analysiert werden, auch dafür geeignet sind. Bevor ein Forensik-Werkzeug eingesetzt wird, SOLLTE zudem geprüft werden, ob es richtig funktioniert. Auch SOLLTE überprüft und dokumentiert werden, dass es nicht manipuliert wurde. 

#### DER.2.2.A8 Auswahl und Reihenfolge der zu sichernden Beweismittel [Ermittlungsleiter]

Eine forensische Untersuchung SOLLTE immer damit beginnen, die Ziele bzw. den Arbeitsauftrag zu definieren. Die Ziele SOLLTEN möglichst konkret formuliert sein. Danach SOLLTEN alle notwendigen Datenquellen identifiziert werden. Auch SOLLTE festgelegt werden, in welcher Reihenfolge die Daten gesichert werden und wie genau dabei vorgegangen werden soll. Die Reihenfolge SOLLTE sich danach richten, wie flüchtig (volatil) die zu sichernden Daten sind. So SOLLTEN schnell flüchtige Daten zeitnah gesichert werden. Erst danach SOLLTEN beispielsweise Festspeicherinhalte und schließlich Backups folgen.

#### DER.2.2.A9 Vorauswahl forensisch relevanter Daten [Ermittlungsleiter]

Es SOLLTE festgelegt werden, welche sekundären Daten (z. B. Logdaten oder Verkehrsmitschnitte) auf welche Weise und wie lange im Rahmen der rechtlichen Rahmenbedingungen für mögliche forensische Beweissicherungsmaßnahmen vorgehalten werden.

#### DER.2.2.A10 IT-forensische Sicherung von Beweismitteln [Ermittler, Ermittlungsleiter]

Um Beweismittel zu sichern, SOLLTEN möglichst die kompletten Datenträger forensisch dupliziert werden. Wenn das nicht möglich ist, z. B. bei flüchtigen Daten im RAM oder in SAN-Partitionen, SOLLTE eine Methode gewählt werden, die möglichst wenig Daten verändert.

Um nachweisen zu können, dass die Daten integer sind, SOLLTEN die Originaldatenträger versiegelt aufbewahrt werden. Existieren kryptografische Prüfsummen von forensischen Kopien oder Originalen, kann die Integrität auch darüber nachgewiesen werden. Dazu SOLLTEN die schriftlich dokumentierten kryptografischen Prüfsummen von den Datenträgern getrennt und in mehreren Kopien aufbewahrt werden. Zudem SOLLTE sichergestellt sein, dass die so dokumentierten Prüfsummen nicht verändert werden können. Damit die Daten gerichtlich verwertbar sind, SOLLTE ein Zeuge bestätigen, wie dabei vorgegangen wurde und die erstellen Prüfsummen beglaubigen. 

Es SOLLTE ausschließlich geschultes Personal (siehe DER.2.2.A6 *Schulung des Personals für die Umsetzung der forensischen Sicherung*) oder ein Forensik-Dienstleister (siehe DER.2.2.A3 *Vorauswahl von Forensik-Dienstleistern*) eingesetzt werden, um Beweise forensisch zu sichern.

#### DER.2.2.A11 Dokumentation der Beweissicherung [Ermittler, Ermittlungsleiter]

Wenn Beweise forensisch gesichert werden, SOLLTEN alle dafür durchgeführten Schritte dokumentiert werden. Die Dokumentation SOLLTE lückenlos nachweisen, wie mit den gesicherten Originalbeweismitteln umgegangen wurde. Auch SOLLTE dokumentiert werden, welche Methoden eingesetzt wurden und warum sich die Verantwortlichen dafür entschieden haben. 

#### DER.2.2.A12 Sichere Verwahrung von Originaldatenträgern und Beweismitteln [Ermittler, Ermittlungsleiter]

Alle sichergestellten Originaldatenträger SOLLTEN physisch so gelagert werden, dass nur ermittelnde und namentlich bekannte Mitarbeiter darauf zugreifen können. Wenn Originaldatenträger und Beweismittel eingelagert werden, SOLLTE festgelegt werden, wie lange sie aufzubewahren sind. Nachdem die Frist abgelaufen ist, SOLLTE geprüft werden, ob die Datenträger und Beweise noch weiter aufbewahrt werden müssen. Nach der Aufbewahrungsfrist SOLLTEN Beweismittel sicher gelöscht oder vernichtet und Originaldatenträger zurückgegeben werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.2.2.A13 Rahmenverträge mit externen Dienstleistern(CIA)

Damit IT-Sicherheitsvorfälle schneller forensisch untersucht werden können, SOLLTE die Institution Abrufvereinbarungen bzw. Rahmenverträge mit Forensik-Dienstleistern abschließen. 

#### DER.2.2.A14 Festlegung von Standardverfahren für die Beweissicherung(CIA)

Für Anwendungen, IT-Systeme bzw. IT-Systemgruppen mit hohem Schutzbedarf sowie für verbreitete Systemkonfigurationen SOLLTEN Standardverfahren erstellt werden, die es erlauben, flüchtige und nichtflüchtige Daten möglichst vollständig forensisch zu sichern.

Die jeweiligen systemspezifischen Standardverfahren SOLLTEN durch erprobte und möglichst automatisierte Prozesse umgesetzt werden. Sie SOLLTEN zudem durch Checklisten und technische Hilfsmittel unterstützt werden, z. B. durch Software, Software-Tools auf mobilen Datenträgern und IT-forensischer Hardware wie Schreibblockern.

#### DER.2.2.A15 Durchführung von Übungen zur Beweissicherung(CIA)

Alle an forensischen Analysen beteiligten Mitarbeiter SOLLTEN regelmäßig üben, wie Beweise bei einem IT-Sicherheitsvorfall zu sichern sind.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Vorsorge für die IT-Forensik" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSIFor] BSI Leitfaden IT-Forensik

  

 BSI, Version 1.0.1, 03.2011  
 [https://www.bsi.bund.de/DE/Themen/Cyber-Sicherheit/Dienstleistungen/IT-Forensik/forensik\_node.html](https://www.bsi.bund.de/DE/Themen/Cyber-Sicherheit/Dienstleistungen/IT-Forensik/forensik_node.html)

 
* #### [ISFTM24] Information Security Forum (ISF), insbesondere Area TM 2.4 Forensic Investigations

  

 ISF, insbesondere Area TM 2.4 Forensic Investigations, 06.2016

 
* #### [ISO27042] ISO/IEC 27042:2015

  

 Information technology- Security techniques- Guidelines for the analysis and interpretation of digital evidence, ISO, 06.2015  
 <https://www.iso.org/standard/44406.html>

 
* #### [ISO27043] DIN EN ISO/IEC 27043

  

 Informationstechnik- IT- Sicherheitsverfahren- Grundsätze und Prozesse für die Untersuchung von Vorfällen (ISO/IEC 27043:2015); Deutsche Fassung EN ISO/IEC27043:2016 

 
* #### [NIST80086] NIST Special Publikaton 800-86

  

 NIST, Guide to Integrating Forensic Techniques into Incident Response, 08.2006  
 <https://csrc.nist.gov/publications/detail/sp/800-86/final>

 
* #### [RFC3227] Guidelines for Evidence Collection and Archiving

  

 RFC, 02.2002  
 <https://tools.ietf.org/html/rcf3227>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Vorsorge für die IT-Forensik" von Bedeutung.

* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.37 Abstreiten von Handlungen
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

