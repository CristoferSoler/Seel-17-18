1 Beschreibung
--------------

### 1.1 Einleitung

Um IT-Systeme schützen zu können, müssen sicherheitsrelevante Ereignisse rechtzeitig erkannt und behandelt werden. Dazu ist es notwendig, dass Institutionen im Vorfeld geeignete organisatorische, personelle und technische Maßnahmen planen, implementieren und regelmäßig üben. Denn wenn auf ein vorgegebenes und erprobtes Verfahren aufgesetzt werden kann, lassen sich Reaktionszeiten verkürzen und vorhandene Prozesse optimieren. 

Als sicherheitsrelevantes Ereignis wird ein Ereignis bezeichnet, das sich auf die Informationssicherheit auswirkt und die Vertraulichkeit, Integrität und Verfügbarkeit beeinträchtigen kann. Typische Folgen solcher Ereignisse sind ausgespähte, manipulierte oder zerstörte Informationen. Die Ursachen hierfür sind dabei vielfältig: So spielen unter anderem Malware, veraltete Systeminfrastrukturen oder Innentäter eine Rolle. Angreifer nutzen aber auch oft Zero-Day-Exploits aus, also Sicherheitslücken in Programmen, bevor es für diese einen Patch gibt. Eine weitere erst zunehmende Gefährdung sind sogenannte Advanced Persistent Threats (APT). Dabei handelt es sich um zielgerichtete Cyber-Angriffe auf ausgewählte Institutionen und Einrichtungen, bei denen sich ein Angreifer dauerhaften Zugriff zu einem Netz verschafft und diesen auf weitere Systeme ausweitet. Die Angriffe zeichnen sich durch einen sehr hohen Ressourceneinsatz und erhebliche technische Fähigkeiten aufseiten der Angreifer aus und sind oft schwer zu detektieren. 

### 1.2 Zielsetzung

Dieser Baustein zeigt einen systematischen Weg auf, wie Informationen gesammelt, korreliert und ausgewertet werden können, um sicherheitsrelevante Ereignisse möglichst vollständig und zeitnah zu detektieren. Die aus der Detektion gewonnenen Erkenntnisse sollen die Fähigkeit von Institutionen verbessern, sicherheitsrelevante Ereignisse zu erkennen und darauf angemessen zu reagieren.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die zu beachten und zu erfüllen sind, wenn sicherheitsrelevante Ereignisse detektiert werden. Voraussetzung hierfür ist jedoch, dass umfassend protokolliert wird. Die dafür notwendigen Maßnahmen werden nicht im vorliegenden Baustein beschrieben, sondern sind in OPS.1.1.5 *Protokollierung* enthalten.

Außerdem beschreibt der Baustein nicht, wie mit sicherheitsrelevanten Ereignissen umzugehen ist, nachdem sie detektiert worden. Empfehlungen dazu werden in DER.2.1 *Incident Management* und DER.2.2 *Forensik* aufgeführt. Ebenso wird nicht auf die Themen Datenschutz und Archivierung von Protokolldaten eingegangen, diese werden in CON.2 *Datenschutz* und OPS.1.1.2 *Archivierung* behandelt.

Um sicherheitsrelevante Ereignisse zu erkennen, sind oft zusätzliche Programme erforderlich, z. B. Antivirenprogramme, Firewalls oder Intrusion-Detection-/Intrusion-Prevention-Systeme (IDS/IPS). Sicherheitsaspekte dieser Systeme sind ebenfalls nicht Gegenstand des vorliegenden Bausteins. Sie werden z. B. in NET.3.4 *IDS/IPS*, OPS.1.1.5 *Schutz vor Schadprogrammen* und NET.3.2 *Firewall* thematisiert.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Detektion von sicherheitsrelevanten Ereignissen von besonderer Bedeutung:

### 2 1 Missachtung von gesetzlichen Vorschriften und betrieblichen Mitbestimmungsrechten

Programme, die sicherheitsrelevante Ereignisse detektieren und Protokolldaten auswerten, sammeln oft viele Informationen über die Netzstruktur und die internen Abläufe einer Institution. Darin können z. B. schützenswerte Daten, wie personenbezogene Daten, Verschlusssachen oder Arbeitsabläufe von Mitarbeitern enthalten sein. Dadurch, dass solche Daten jedoch gespeichert werden, können Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeiter verletzt werden. Auch verstößt die Institution unter bestimmten Voraussetzungen eventuell gegen die jeweiligen Landesdatenschutzgesetze bzw. das Bundesdatenschutzgesetz.

### 2 2 Unzureichende Qualifikation der Verantwortlichen

Im täglichen IT-Betrieb einer Institution können viele Störungen und Fehler auftreten (z. B. starke Zunahme ankommender Protokolldaten). Sind die verantwortlichen Mitarbeiter nicht ausreichend sensibilisiert und geschult, besteht die Gefahr, dass sie sicherheitsrelevante Ereignisse nicht als solche identifizieren und so ein Angriff unerkannt bleibt. 

### 2 3 Fehlende oder unzureichende Protokollierung

Werden sicherheitsrelevante Ereignisse ungenügend oder gar nicht protokolliert, lässt sich nicht ausreichend und schnell genug feststellen, ob Sicherheitsvorgaben verletzt werden oder ob Angriffsversuche stattfinden. Auch kann im Schadenfall keine Fehleranalyse mehr durchgeführt werden und das Einfallstor eines Angriffs bleibt so eventuell bestehen. Auch werden Protokollinformationen dafür eingesetzt, Integritätsprüfungen durchzuführen. Fehlen die Protokolle jedoch, ist dies nicht möglich. 

### 2 4 Fehlerhafte Administration der eingesetzten Detektionssysteme

Fehlerhafte Konfigurationen können dazu führen, dass eingesetzte Detektionssysteme nicht ordnungsgemäß funktionieren. Ist beispielsweise die Alarmierung falsch eingestellt, kann es zu vermehrten Fehlalarmen kommen. Die verantwortlichen Mitarbeiter können dann eventuell nicht mehr zwischen einem Fehlalarm und einem sicherheitsrelevanten Ereignis unterscheiden. Auch nehmen sie die Meldungen eventuell nicht zeitnah wahr, da zu viele Alarme generiert werden. Dadurch bleiben möglicherweise Angriffe unerkannt. Ebenso steigt der Aufwand stark an, die Menge der Meldungen auszuwerten. 

### 2 5 Fehlende Informationen über den zu schützenden Informationsverbund

Sind keine oder nur ungenügende Informationen über den Informationsverbund vorhanden, besteht die Gefahr, dass wesentliche Bereiche des Informationsverbunds nicht ausreichend durch Detektionssysteme geschützt werden. Dadurch können Angreifer leicht in das Netz der Institution eindringen und zum Beispiel schützenswerte Informationen abgreifen. Auch ist es ihnen so möglich, lange unbemerkt im System zu bleiben und dauerhaft auf das Netz zuzugreifen.

### 2 6 Unzureichende Nutzung von Detektionssystemen

Wenn keine Detektionssysteme eingesetzt werden und auch die in IT-Systemen und Anwendungen vorhandenen Funktionen zur Detektion von sicherheitsrelevanten Ereignissen nicht benutzt werden, können Angreifer leichter unbemerkt in das Netz der Institution eindringen und unbefugt auf sensible Informationen zugreifen. Besonders kritisch ist es, wenn die Übergänge zwischen Netzgrenzen nur unzureichend überwacht werden. 

### 2 7 Unzureichende personelle Ressourcen

Ist nicht genügend Personal vorhanden, um Protokolldaten auszuwerten, können sicherheitsrelevante Ereignisse nicht vollständig detektiert werden. So bleiben Angriffe eventuell lange verborgen bzw. werden erst entdeckt, wenn z. B. schon sehr viele schützenswerte Informationen abgeflossen sind. Auch wenn durch zu wenig Personal keine externen Informationsquellen ausgewertet werden, bleiben Sicherheitslücken eventuell zu lange offen und können von Angreifern ausgenutzt werden, um unerlaubt in die IT-Systeme der Institution einzudringen. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen an die Detektion von sicherheitsrelevanten Ereignissen aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### DER.1.A1 Erstellung einer Sicherheitsrichtlinie für die Detektion von sicherheitsrelevanten Ereignissen [Informationssicherheitsbeauftragter (ISB)]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie die Detektion von sicherheitsrelevanten Ereignissen sicher geplant, aufgebaut und betrieben werden kann. Die Richtlinie MUSS allen im Bereich Detektion verantwortlichen Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem verantwortlichen ISB abgestimmt und dokumentiert werden. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.

#### DER.1.A2 Einhaltung rechtlicher Bedingungen bei der Auswertung von Protokolldaten [Informationssicherheitsbeauftragter (ISB)]

Wenn Protokolldaten ausgewertet werden, MÜSSEN dabei die gesetzlichen Bestimmungen aus den aktuellen Gesetzen zum Bundes-/Landesdatenschutz eingehalten werden. Darüber hinaus MÜSSEN die Persönlichkeitsrechte bzw. Mitbestimmungsrechte der Mitarbeitervertretungen gewahrt werden, wenn Detektionssysteme eingesetzt werden. Ebenso MUSS sichergestellt sein, dass alle weiteren relevanten gesetzlichen Bestimmungen beachtet werden, z. B. Telemediengesetz (TMG), Betriebsverfassungsgesetz und Telekommunikationsgesetz.

#### DER.1.A3 Festlegung von Meldewegen für sicherheitsrelevante Ereignisse

Es MÜSSEN geeignete Melde- und Alarmierungswege festgelegt und dokumentiert werden. Dabei MUSS bestimmt werden, welche Stellen wann zu informieren sind. Auch MUSS aufgeführt sein, wie die jeweiligen Personen erreicht werden können. Je nach Dringlichkeit MUSS ein sicherheitsrelevantes Ereignis über verschiedene Kommunikationswege gemeldet werden. 

Die Melde- und Alarmierungswege MÜSSEN den Mitarbeitern ausgedruckt vorliegen. Alle für die Meldung bzw. Alarmierung relevanten Personen MÜSSEN über ihre Aufgaben informiert sein. Es MÜSSEN alle Schritte des Melde- und Alarmierungsprozesses ausführlich beschrieben sein. Die eingerichteten Melde- und Alarmierungswege SOLLTEN regelmäßig geprüft, erprobt und falls erforderlich, aktualisiert werden.

#### DER.1.A4 Sensibilisierung der Mitarbeiter [Vorgesetzte, Leiter IT, Benutzer]

Damit Mitarbeiter mögliche Sicherheitsvorfälle schnell erkennen können, MÜSSEN sie entsprechend sensibilisiert werden. Dafür SOLLTEN regelmäßige Schulungen stattfinden, in denen gängige und aktuelle Bedrohungen sowie die Vorgehensweisen der Cyberkriminellen aufgezeigt werden. 

Auch MÜSSEN die Mitarbeiter dahingehend sensibilisiert werden, dass sie Ereignismeldungen der Clients nicht einfach ignorieren oder schließen, sondern die Meldungen entsprechend der Alarmierungswege an das verantwortliche Incident Management weitergeben (siehe DER.2.1 *Incident Management*).

Jeder Mitarbeiter MUSS einen von ihm erkannten Sicherheitsvorfall unverzüglich dem Incident Management melden.

#### DER.1.A5 Einsatz von mitgelieferten Systemfunktionen zur Detektion [Fachverantwortliche]

Verfügen eingesetzte IT-Systeme oder Anwendungen über Funktionen, mit denen sich sicherheitsrelevante Ereignisse detektieren lassen , MÜSSEN diese aktiviert und benutzt werden. 

Auf allen eingesetzten Komponenten MUSS die Protokollierung aktiviert werden (siehe OPS.1.1.5* Protokollierung*). Liegt ein sicherheitsrelevanter Vorfall vor, MÜSSEN die Meldungen mindestens lokal ausgewertet werden. Zusätzlich MÜSSEN die protokollierten Ereignisse anderer IT-Systeme überprüft werden. Auch SOLLTEN die gesammelten Meldungen in verbindlich festgelegten Zeiträumen stichpunktartig kontrolliert werden. 

Es MUSS geprüft werden, ob zusätzliche Schadcodescanner auf zentralen IT-Systemen installiert werden sollen (siehe auch SYS.1.1 *Allgemeiner Server*). Ist dies der Fall, MÜSSEN es diese über einen zentralen Zugriff ermöglichen, ihre Meldungen und Protokolle auszuwerten. Außerdem MÜSSEN sie regelmäßig aktualisiert werden. Es MUSS sichergestellt sein, dass die Schadcodescanner automatisch sicherheitsrelevante Ereignisse an die Verantwortlichen melden und die Meldungen auch ausgewertet und untersucht werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Detektion von sicherheitsrelevanten Ereignissen. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.1.A6 Kontinuierliche Überwachung und Auswertung von Protokolldaten [Benutzer]

Alle Protokolldaten SOLLTEN möglichst permanent aktiv überwacht und ausgewertet werden. Es SOLLTEN Mitarbeiter benannt werden, die dafür verantwortlich sind.

Müssen die verantwortlichen Mitarbeiter aktiv nach eingetretenen sicherheitsrelevanten Ereignissen suchen, z. B. wenn sie IT-Systeme kontrollieren oder testen, SOLLTEN solche Aufgaben in entsprechenden Verfahrensanleitungen dokumentiert sein.

Für die Detektion von sicherheitsrelevanten Ereignissen SOLLTEN genügend personelle Ressourcen bereitgestellt werden.

#### DER.1.A7 Schulung von Verantwortlichen [Vorgesetzte, Leiter IT]

Alle Verantwortlichen, die Ereignismeldungen kontrollieren, SOLLTEN weiterführende Schulungen und Qualifikationen erhalten. Wenn IT-Komponenten beschafft werden, SOLLTE ein Budget für Schulungen eingeplant und ein Schulungskonzept für die verantwortlichen Mitarbeiter erstellt werden.

#### DER.1.A8 Festlegung von zu schützenden Segmenten [Fachverantwortliche]

Anhand des Netzplans (siehe NET.1.1 *Netzarchitektur und -design*) SOLLTE festgelegt werden, welche Netzsegmente durch zusätzliche Detektionssysteme geschützt werden müssen (vgl. DER.1.A9 *Einsatz zusätzlicher Detektionssysteme*).

#### DER.1.A9 Einsatz zusätzlicher Detektionssysteme [Fachverantwortliche]

Um sicherheitsrelevante Ereignisse besser zu erkennen, SOLLTE der Informationsverbund um zusätzliche Detektionssysteme und Sensoren ergänzt werden. So SOLLTEN Schadcodedetektionssysteme eingesetzt und zentral verwaltet werden. Auch die im Netzplan definierten Übergange zwischen internen und externen Netzen SOLLTEN um netzbasierte Intrusion Detection Systeme (NIDS) ergänzt werden.

#### DER.1.A10 Einsatz von TLS/SSH-Proxies [Fachverantwortliche]

An den Übergängen zu externen Netzen SOLLTEN TLS/SSH-Proxies eingesetzt werden, die die verschlüsselte Verbindung unterbrechen und es so ermöglichen, die übertragenen Daten auf Malware zu prüfen. Alle TLS/SSH-Proxies SOLLTEN vor unbefugten Zugriffen geschützt werden. Außerdem SOLLTEN sicherheitsrelevante Ereignisse auf den TLS/SSH-Proxies automatisch detektiert werden. Es SOLLTE eine organisatorische Regelung erstellt werden, unter welchen datenschutzrechtlichen Voraussetzungen die Logdaten manuell ausgewertet werden dürfen. 

#### DER.1.A11 Nutzung einer zentralen Protokollierungsinfrastruktur für die Auswertung sicherheitsrelevanter Ereignisse [Fachverantwortliche]

Die gesammelten Ereignismeldungen der IT-Systeme und Anwendungssysteme SOLLTEN auf einer zentralen Protokollinfrastruktur (siehe OPS1.1.5 *Protokollierung*) aufbewahrt werden. Die eingelieferten Ereignismeldungen SOLLTEN mithilfe eines Tools zentral gespeichert, ausgewertet und abgerufen werden können. Damit die Daten korreliert und abgeglichen werden können, SOLLTEN sie alle zeitlich synchronisiert werden. Die gesammelten Ereignismeldungen SOLLTEN regelmäßig auf Auffälligkeiten kontrolliert werden. Damit sicherheitsrelevante Ereignisse auch nachträglich erkannt werden können, SOLLTEN die Signaturen der Detektionssysteme durchgängig aktuell und auf dem gleichen Stand sein. 

#### DER.1.A12 Auswertung von Informationen aus externen Quellen [Informationssicherheitsbeauftragter (ISB), Fachverantwortliche]

Um neue Erkenntnisse über sicherheitsrelevante Ereignisse für den eigenen Informationsverbund zu gewinnen, SOLLTEN externe Quellen herangezogen und ausgewertet werden. Da Meldungen über unterschiedliche Kanäle in eine Institution eingeliefert werden, SOLLTE sichergestellt sein, dass diese Meldungen von den Mitarbeitern auch als relevant erkannt und an die richtige Stelle weitergeleitet werden. Stammen Informationen aus qualifizierten Quellen, SOLLTEN sie grundsätzlich ausgewertet werden. Alle eingelieferten Informationen SOLLTEN bewertet werden, ob sie relevant für den eigenen Informationsverbund sind. Ist dies der Fall, SOLLTEN die Informationen entsprechend der Sicherheitsvorfallbehandlung eskaliert werden (siehe DER.2.1. *Incident Management*).

#### DER.1.A13 Regelmäßige Audits der Detektionssysteme

Die vorhandenen Detektionssysteme und getroffenen Maßnahmen SOLLTEN regelmäßig überprüft werden, ob sie noch aktuell und wirksam sind. Es SOLLTEN die Messgrößen ausgewertet werden, die beispielsweise anfallen, wenn sicherheitsrelevante Ereignisse aufgenommen, gemeldet und eskaliert werden. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Soll-Zustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.1.A14 Auswertung der Protokolldaten durch spezialisiertes Personal [Leiter IT](CI)

Es SOLLTEN Mitarbeiter überwiegend dafür abgestellt werden, alle Protokolldaten zu überwachen. Das abgestellte Personal SOLLTE spezialisierte weiterführende Schulungen und Qualifikationen erhalten. Ein Personenkreis SOLLTE benannt werden, der ausschließlich für das Thema Auswertung von Protokolldaten, wie z. B. aus dem Bereich Forensik, verantwortlich ist.

#### DER.1.A15 Zentrale Detektion und Echtzeitüberprüfung von Ereignismeldungen(CIA)

Es SOLLTEN zentrale Komponenten eingesetzt werden, um sicherheitsrelevante Ereignisse zu erkennen und auszuwerten. Zentrale automatisierte Analysen mit Softwaremitteln SOLLTEN dazu eingesetzt werden, um alle in der Systemumgebung anfallenden Ereignisse aufzuzeichnen, in Bezug zueinander zu setzen und sicherheitsrelevante Vorgänge sichtbar zu machen. Alle eingelieferten Daten SOLLTEN lückenlos in der Protokollverwaltung einsehbar und auswertbar sein. Die tatsächlichen Daten SOLLTEN möglichst permanent ausgewertet werden. Werden definierte Schwellwerten überschritten, SOLLTE automatisch alarmiert werden. Durch das Personal SOLLTE sichergestellt werden, dass bei einem Alarm unverzüglich eine qualifizierte und dem Bedarf entsprechende Reaktion eingeleitet wird. In diesem Zusammenhang SOLLTE auch der betroffene Mitarbeiter sofort informiert werden. 

Die Systemverantwortlichen SOLLTEN regelmäßig die Analyseparameter auditieren und, falls erforderlich, anpassen. Zusätzlich SOLLTEN bereits überprüfte Daten regelmäßig hinsichtlich sicherheitsrelevanter Ereignisse automatisch untersucht werden.

#### DER.1.A16 Einsatz von Detektionssystemen nach Schutzbedarfsanforderungen(CIA)

Anwendungen mit erhöhtem Schutzbedarf SOLLTEN durch zusätzliche Detektionsmaßnahmen geschützt werden. Dafür SOLLTEN z. B. solche Detektionssysteme eingesetzt werden, mit denen sich der erhöhte Schutzbedarf technisch auch sicherstellen lässt.

#### DER.1.A17 Automatische Reaktion auf sicherheitsrelevante Ereignisse(CI)

Bei einem sicherheitsrelevanten Ereignis SOLLTEN die eingesetzten Detektionssysteme das Ereignis automatisch melden und mit geeigneten Schutzmaßnahmen reagieren. Hierbei SOLLTEN Verfahren eingesetzt werden, die automatisch mögliche Angriffe, Missbrauchsversuche oder Sicherheitsverletzungen erkennen. Es SOLLTE möglich sein, automatisch in den Datenstrom einzugreifen, um einen möglichen Sicherheitsvorfall zu unterbinden.

#### DER.1.A18 Durchführung regelmäßiger Integritätskontrollen(CI)

Alle Detektionssysteme SOLLTEN regelmäßig daraufhin überprüft werden, ob sie noch integer sind. Auch SOLLTEN die Benutzerrechte kontrolliert werden. Zusätzlich SOLLTEN die Sensoren eine Integritätskontrolle von Dateien durchführen und bei sich ändernden Werten eine automatische Alarmierung auslösen.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Detektion von sicherheitsrelevanten Ereignissen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSILeit1] BSI-Leitfaden zur Einführung von Intrusion-Detection-Systemen,

  

 IDS, BSI, Version 1.0, 10.2002  
 [https://www.bsi.bund.de/DE/Publikationen/Studien/IDS02/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/Studien/IDS02/index_htm.html)

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Detektion von sicherheitsrelevanten Ereignissen" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

