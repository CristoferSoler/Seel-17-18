1 Beschreibung
--------------

### 1.1 Einleitung

Bei Advanced Persistent Threats (APT) handelt es sich um zielgerichtete Cyber-Angriffe auf ausgewählte Institutionen und Einrichtungen, bei denen sich ein Angreifer dauerhaften Zugriff zu einem Netz verschafft und diesen in der Folge auf weitere IT-Systeme ausweitet. Die Angriffe zeichnen sich durch einen sehr hohen Ressourceneinsatz und erhebliche technische Fähigkeiten aufseiten der Angreifer aus und sind in der Regel schwierig zu detektieren.

### 1.2 Lebenszyklus

Um ein APT-Vorfall erfolgreich bereinigen zu können, muss strategisch geplant und dann konsequent vorgegangen werden. Dies bedeutet, zunächst IT-Systeme gezielt abzuschalten, um den Angreifer auszusperren, dann planmäßig zu bereinigen und schließlich die bereinigte Umgebung wieder in einen produktiven Zustand zu überführen. 

Die Schritte, die dabei durchlaufen werden sollten, sowie die Maßnahmen, die in den jeweiligen Schritten beachtet werde müssen, sind im Folgenden aufgeführt:

**Planung und Konzeption**

Ein APT-Vorfall kann erst bereinigt werden, nachdem dieser detektiert und korrekt als APT eingestuft wurde. Dies geschieht im Rahmen der Detektion (siehe DER.1 *Detektion von Sicherheitsrelevanten Ereignissen*), einer initialen forensischen Untersuchung (siehe DER.2.2 *Vorsorge für die IT-Forensik* und des klassischen Incident Managements (siehe Baustein DER.2.1 *Incident Management*). Die Maßnahmen des vorliegenden Bausteins müssen daher erst umgesetzt werden, nachdem die anderen Bausteine durchlaufen worden sind. 

Die Bereinigung eines APT-Vorfalls stellt ein umfangreiches, arbeitsintensives Projekt dar. Daher ist zur erfolgreichen Bearbeitung ein Leitungsgremium notwendig, das dafür verantwortlich ist, die notwendigen Maßnahmen zu planen, zu konzipieren und nachzuverfolgen (siehe DER.2.3.M1 *Einrichtung eines Leitungsgremiums*). Ein APT-Vorfall stellt immer einen Notfall dar, weswegen eine Verzahnung mit dem Notfallmanagement und die Anwendung der dort definierten Maßnahmen erfolgen sollte (siehe DER.4 *BCM, Notfallmanagement*). Stellt sich heraus, dass der Vorfall unternehmensbedrohende Ausmaße hat, müssen sich die Verantwortlichen mit dem Krisenmanagement abstimmen. 

Üblicherweise geht der Bereinigung eines APT-Vorfalls, nachdem er entdeckt und klassifiziert ist, zunächst eine Phase der Beobachtung des Angreifers voraus. Diese Phase dient dazu, ausreichend Informationen zu sammeln, um den Angreifer effektiv aussperren und alle von ihm etablierten Zugriffskanäle beseitigen zu können. Das Leitungsgremium legt im Rahmen einer Bereinigungsstrategie fest, ob eine Beobachtungsphase durchgeführt wird, wie lange diese andauert und welche Maßnahmen getroffen werden, um den Angreifer zu beobachten (siehe DER.2.3.M2 *Entscheidung für eine Bereinigungsstrategie*). Weiterhin wird in dieser Strategie über die genaue Vorgehensweise entschieden, mit der IT-Systeme bereinigt werden. Diese kann von der gezielten Beseitigung einzelner Infektionen, über das erneute Aufsetzen von IT-Systemen bis hin zum Austausch betroffener IT-Systeme (siehe DER.2.3.M9 *Hardwareaustausch betroffener IT-Systeme*) reichen.

Da der Angreifer potenziell vollständig auf die bestehende Kommunikationsinfrastruktur der betroffenen Institution zugreifen kann und diese aktiv beobachtet, ist es notwendig die Beobachtungsphase und die Vorbereitung der Bereinigung über sichere, unabhängige Kommunikationskanäle zu koordinieren (siehe DER.2.3.M8 *Etablierung sicherer, unabhängiger Kommunikationskanäle*).

**Beschaffung**

Es müssen üblicherweise verschiedene Hard- und Softwarekomponenten kurzfristig beschafft werden, um einen APT-Vorfall zu bereinigen. Beispielsweise müssen eventuell Mechanismen für die sichere Kommunikation geschaffen werden (siehe DER.2.3.M8 *Etablierung sicherer, unabhängiger Kommunikationskanäle*), Hardware für forensische Untersuchungen muss beschafft werden und eventuell ist ein Hardwaretausch von IT-Systemen mit hohem Schutzbedarf notwendig (siehe DER.2.3.M9 *Hardwareaustausch betroffener IT-Systeme*). Da die Beschaffungen sehr kurzfristig erfolgen müssen, ist es gegebenenfalls notwendig, die üblichen Beschaffungswege der Institution zu umgehen. Weiterhin soll eventuell vermieden werden, dass der Vorfall vorzeitig in der Institution oder gar darüber hinaus bekannt wird. Auch das spielt bei der Beschaffung unter Umständen eine Rolle. Durch die genannten Anforderungen entstehen eventuell Konflikte zu den üblichen Vorgaben und Prozessen für die Beschaffung. Das Leitungsgremium muss daher über weitreichende Entscheidungskompetenzen verfügen.

**Umsetzung**

Die Umsetzung der Bereinigung beginnt damit, den Angreifer gezielt auszusperren. Dieser Vorgang wird häufig als Cut-Off bezeichnet. Der Cut-Off wird üblicherweise dadurch realisiert, dass die betroffenen Netzbereiche isoliert werden (siehe DER.2.3.M3 *Isolierung der betroffenen Netzabschnitte*).

Anschließend kann die zuvor geplante und beschlossene Strategie zur Bereinigung der betroffenen IT-Systeme umgesetzt werden (siehe DER.2.3.M2 *Entscheidung für eine Bereinigungsstrategie*). Neben der eigentlichen Bereinigung der IT-Systeme muss zusätzlich der initiale Einbruchsweg geschlossen (siehe DER.2.3.M5 *Schließen des initialen Einbruchswegs*) und sämtliche potenziell kompromittierten Zugangsdaten und Schlüsselmaterialien müssen geändert werden (siehe DER.2.3.M4 *Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln*).

Bevor die Umgebung wieder in den Produktivbetrieb übergeht, sollten Maßnahmen getroffen werden, um eine erneute Kompromittierung zu erschweren, bzw. die Wahrscheinlichkeit einer zeitnahen Detektion zu erhöhen. Hierzu sollten gezielte Härtungsmaßnahmen durchgeführt werden (DER.2.3.M7 *Gezielte IT-Systemhärtung*). Außerdem sollten erneute Angriffe durch denselben Angreifer erschwert werden (siehe DER.2.3.M10 *Umbauten zur Erschwerung eines erneuten Angriffs durch denselben Angreifer*). 

Erst wenn die Umgebung komplett bereinigt ist, kann sie wieder in den Produktivbetrieb überführt werden (DER.2.3.M6 *Rückführung in den Produktivbetrieb*). 

**Aussonderung**

Während die Bereinigungsstrategie erarbeitet wird und parallel die forensischen Untersuchungen laufen, werden üblicherweise zusätzliche Detektions- und Protokollierungsmechanismen geschaffen. Hierbei handelt es sich oftmals um Ad-hoc-Lösungen, die nicht immer den Anforderungen eines langfristigen produktiven Betriebs genügen. Meistens werden die getroffenen Maßnahmen durch Datenschutzbeauftragte, Betriebsrat oder Unternehmensführung auch nur temporär genehmigt, da beispielsweise Datenschutzaspekte nicht ausreichend berücksichtigt werden können. Aus diesen Gründen müssen diese IT-Systeme häufig wieder ausgesondert werden. Es sollte jedoch nach der Bereinigung eine Phase der intensiven Beobachtung der betroffenen Umgebung eingeplant werden. Wenn möglich, sollte in dieser Phase die temporär geschaffene Infrastruktur weiter genutzt werden. Auch eine teilweise Überführung von Ad-hoc-Monitoring-Infrastruktur in den produktiven Betrieb zur Ergänzung bereits vorhandener Detektionsmechanismen (siehe auch DER.1 *Detektion von sicherheitsrelevanten Ereignissen*) sollte geprüft werden.

Bei der Aussonderung von IT-Systemen, mit denen der Angreifer beobachtet wurde oder die für forensische Analysen benutzt wurden, muss unbedingt auf die sichere Löschung oder Vernichtung sämtlicher Speichermedien geachtet werden, da auf diesen meist schützenswerte Daten enthalten sind. Weiterhin ist gegebenenfalls zu prüfen, ob forensische Daten sicher archiviert werden müssen, um nachgelagerte weitergehende Untersuchungen zu ermöglichen oder um sie als Beweismittel sicherzustellen.

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Bereinigung weitreichender Sicherheitsvorfälle" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### DER.2.3.M1 Einrichtung eines Leitungsgremiums [Informationssicherheitsbeauftragter (ISB)]

Einen Informationsverbund nach einem APT-Angriff zu bereinigen, ist ein komplexes und umfangreiches Projekt. Üblicherweise müssen verschiedene Parteien bei der Aufklärung und Bereinigung koordiniert, taktische und strategische Entscheidungen auf einer teils unklaren Informationsbasis getroffen und gleichzeitig die Bereinigungstätigkeiten zumindest kurz bis mittelfristig geheimgehalten werden. Um diese Anforderungen zu gewährleisten, müssen kompetente Ansprechpartner die Bereinigungstätigkeiten steuern. Dafür sollte ein Leitungsgremium einberufen werden, das über die folgenden Kompetenzen verfügt:

* **Entscheidungskompetenz:** Die Verantwortlichen müssen zahlreiche Entscheidungen darüber treffen, wie bei der Bereinigung konkret vorgegangen werden soll. Oftmals müssen dabei die üblichen Prozesse und Vorgaben umgangen werden, damit der Vorgang geheim bleibt und zeitkritische Prozesse umgehend durchgeführt werden können. Deshalb sollten Mitarbeiter der Leitungsebene der Institution in das Gremium miteinbezogen werden. Auch der Informationssicherheitsbeauftragte muss aufgrund seiner Schnittstellenfunktion zwischen Technik und Management und seiner grundsätzlichen Zuständigkeit dem Leitungsgremium angehören. 
* **Sachkompetenz:** APT-Angriffe sind zumeist technisch sehr komplex. Die Vorfälle zu analysieren, eine wirksame Bereinigungsstrategie zu erarbeiten und Maßnahmen zu entwickeln, mit denen sich erneute Kompromittierungen vermeiden lassen, erfordern daher viel technische Expertise und umfangreiches Wissen über Informationssicherheit. Deshalb sollten zum einen erfahrene Administratoren mit möglichst bereichsübergreifenden Kenntnissen in das Gremium einbezogen werden. Zum anderen sollten interne oder externe Forensikexperten zumindest in beratender Funktion in das Gremium eingebunden sein.
* **Verwaltungskompetenz:** Die Bereinigung eines APT-Vorfalls erfordert ein komplexes Projektmanagement. Unterschiedliche Parteien müssen koordiniert und zahlreiche Aufgaben müssen unter hohem Zeitdruck aufeinander abgestimmt und umgesetzt werden. Während der Beobachtungsphase ist die Faktenlage oft noch unklar. Deswegen sollte aufgrund der sich ständig verändernden Informationsbasis und der daraus abzuleitenden Aktionen iterativ vorgegangen werden. Somit ist es notwendig, Mitarbeiter mit viel Kompetenz beim Projektmanagement in das Gremium einzubinden. Diese sind dafür zuständig, Zeitpläne zu erstellen, Aufgaben zu vergeben und nachzuverfolgen sowie die Gremiumsmitglieder mit den durchführenden Mitarbeitern zu koordinieren.
Das Leitungsgremium übernimmt das gesamte Projektmanagement für die Bereinigung. Sämtliche Entscheidungen, z. B. über die Dauer der Beobachtungsphase, zu analysierende IT-Systeme, Zeitpunkt des Cut-Offs, werden durch das Leitungsgremium getroffen. Allgemein ist das Gremium dafür zuständig, die Bereinigungsstrategie zu entwerfen, und die Durchführung zu planen und nachzuverfolgen.

Um diese Aufgaben zu bewältigen, sollte sich das Leitungsgremium regelmäßig treffen. Darüber hinaus sollten alle Gremiumsmitglieder ausschließlich über sichere Kommunikationskanäle miteinander kommunizieren (siehe DER.2.3.A7 *Etablierung sicherer, unabhängiger Kommunikationskanäle*).

Ist die IT zu stark kompromittiert oder sind die notwendigen Bereinigungsmaßnahmen sehr umfangreich, kann es sein, dass die betroffene Institution einen Krisenstab einrichtet. In diesem Fall muss das Leitungsgremium die Bereinigungsmaßnahmen überwachen. Das Leitungsgremium muss dann dem Krisenstab berichten. 

#### DER.2.3.M2 Entscheidung für eine Bereinigungsstrategie [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Bevor die Bereinigung technisch umgesetzt wird, müssen einige strategische Entscheidungen getroffen werden. Meistens wird die Bereinigungsstrategie nicht vollständig definiert, sondern vom Leitungsgremium basierend auf neuen Erkenntnissen immer wieder ergänzt und angepasst. Entscheidungen zu Eckpunkten der Bereinigungsstrategie sollten vom Leistungsgremium dokumentiert werden. Auch ist es für die praktische Arbeit hilfreich, wenn der jeweils aktuelle Stand der gesamten Strategie festgehalten und den Mitgliedern des Leitungsgremiums sowie in Ausschnitten den umsetzenden Mitarbeitern zur Verfügung gestellt wird.

Im Folgenden werden die wichtigsten Entscheidungen für eine Bereinigungsstrategie in der Reihenfolge ihrer Anwendung beschrieben. Die Entscheidungen bedingen sich teilweise, sodass später umzusetzende Entscheidungen bereits sehr früh getroffen werden müssen.

* Vor der eigentlichen Bereinigung stehen die Beobachtungsphase und der Cut-Off. Wie lang und ausführlich die Beobachtungsphase sein soll, ist bereits der erste Teil der Bereinigungsstrategie. Es sollte bestimmt werden, welche Erkenntnisse für den Cut-Off und die Bereinigung benötigt werden. Wird bereits in dieser Phase von einem vollständigen Neuaufbau der Infrastruktur ausgegangen, kann auf Detailerkenntnisse verzichtet werden. Wenn jedoch nicht ausgeschlossen wird, dass Malware später gezielt gelöscht werden soll, also die IT-Systeme möglicherweise nicht neu installiert werden müssen, werden sehr viele Informationen darüber benötigt, wie sich der Angriff ausgebreitet und wie er funktioniert hat. Außerdem werden dann Indikatoren für betroffene IT-Systeme (Indicators of Compromise, IoC) erforderlich.Das Ergebnis der Beobachtungsphase sollte eine Übersicht über die zu bereinigenden Assets sein. Stehen noch Untersuchungen aus, sollten die betroffenen Assets mit ihrem Status ebenfalls dokumentiert und die Übersichten regelmäßig aktualisiert werden. Die Übersichten sind später die Basis für die Bereinigung. 
* Der Cut-Off (siehe auch DER.2.3.A3 *Isolierung der betroffenen Netzabschnitte* und DER2.3.A4 *Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln*) sollte grundsätzlich ohne Rücksicht auf die spätere Wiederinbetriebnahme geplant werden. Durch den Cut-Off werden betroffene IT-Systeme, Netzabschnitte und Netzgeräte teilweise oder ganz abgeschaltet, sodass nicht mehr darauf zugegriffen werden kann. In der Regel werden Cut-Off und technische Bereinigung gemeinsam geplant. Wie ein Cut-Off umgesetzt werden kann, ist in DER.2.3.M3 *Isolierung der betroffenen Netzabschnitte* beschrieben.Vor dem Cut-Off sollte geprüft werden, wie er sich auf die Institution auswirkt. Schäden, die durch die Bereinigung entstehen, können den Schaden des eigentlichen Angriffs deutlich übersteigen und existenzbedrohend sein. Das Leitungsgremium sollte, gegebenenfalls gemeinsam mit dem Krisenstab, geeignete temporäre Ausweichlösungen prüfen und die Prioritäten festlegen, nach denen die Anwendungen wieder bereitgestellt werden sollen. Hierbei kann auf den Baustein DER.4 *BCM, Notfallmanagement* zurückgegriffen werden.
* Während der Beobachtungsphase kann ein APT-Vorfall noch vertraulich behandelt werden. Nach einem Cut-Off und während der technischen Bereinigung ist der Vorfall bzw. sind die Auswirkungen typischerweise auch für Mitarbeiter, Kunden und Geschäftspartner sichtbar. Es sollte daher rechtzeitig definiert werden, wie lange der APT-Vorfall geheim gehalten werden muss, um eine effektive technische Bereinigung sicherzustellen. Für die Zeit nach der Beobachtungsphase sollte eine Kommunikationsstrategie entworfen werden, die beispielsweise eine Legende für die sichtbaren Ausfälle, vorgefertigte Antworten auf mögliche Anfragen oder eine begleitende Pressemitteilung enthält. Die Strategie ist allen direkt beteiligten Mitarbeitern bekannt zu geben. Sie kann auch mithilfe von PR-Mitarbeitern oder externen PR-Agenturen erstellt werden.
* Während der Bereinigung kommt es wahrscheinlich zu vermehrten Anfragen an den Helpdesk. Das Leitungsgremium sollte sicherstellen, das in allen Phasen ausreichend fachkundiges Personal bereitsteht, das die Bereinigungsmaßnahmen umsetzt und die Benutzer unterstützt. Auch wenn die Bereinigungsmaßnahmen zu größeren Betriebsunterbrechungen führen, muss der Helpdesk arbeitsfähig bleiben. 
* Über die Beobachtungsphase hinaus müssen geeignete Monitoring-Maßnahmen etabliert werden, um bewerten zu können, ob der Cut-Off erfolgreich war und um erkennen zu können, ob es während oder nach der Bereinigung neue Angriffsaktivitäten gibt. Es ist darauf zu achten, dass diese Beobachtungsmöglichkeit durchgehend erhalten bleibt, auch wenn im Zuge der Bereinigung Systembestandteile verändert oder ausgetauscht werden. Um dies sicherzustellen, sollten die Monitoring-Maßnahmen in der Bereinigungsstrategie dokumentiert werden.
* Direkt nach dem Cut-Off können weitere forensische Untersuchungen vorgenommen werden, die zuvor nicht möglich waren, ohne den Angreifer zu warnen. Daraus können sich weiterführende Erkenntnisse für die Bereinigung ergeben. 
* Basierend auf der Übersicht der betroffenen IT-Systeme und der Analyseergebnisse wird entschieden, wie die Bereinigung konkret durchgeführt wird. Für jedes IT-System ist dabei zu entscheiden und zu dokumentieren, ob es komplett neu installiert wird (eventuell zusammen mit neuer Hardware, siehe DER.2.3.A9 *Hardwaretausch betroffener IT-Systeme*), ob die Schadsoftware und andere Änderungen des Angreifers gezielt entfernt bzw. bereinigt werden oder ob keine Bereinigung notwendig ist. Grundsätzlich ist es besser die IT-Systeme neu zu installieren, als sie nur gezielt zu bereinigen, da sonst Artefakte des Angreifers auf dem IT-System verbleiben könnten. Die Maßnahmen können sich von IT-System zu IT-System unterscheiden und sind daher für jedes IT-System oder jeweils für kleinere Gruppen abzustimmen.
* Das Leitungsgremium muss einen Zeitplan für die Bereinigung ausarbeiten und abstimmen. Dabei sollten die Verantwortlichen z. B. darauf achten, dass die Institution funktionsfähig bleibt bzw. die Ausfälle so kurz wie möglich sind. 
* Das Leitungsgremium sollte Vorgaben erstellen, ob und wie Datensicherungen bei der Bereinigung benutzt werden können. Datensicherungen, die noch vor dem APT-Angriff erstellt wurden, können in der Regel genutzt werden. Ist der Angriffszeitpunkt nicht sicher zu bestimmen oder liegen nur neuere Sicherungen vor, so sind die zurücksicherbaren Daten gezielt zu bestimmen. Installationen und Konfigurationen sollten händisch neu erstellt werden.
* Hat die Analyse ergeben, das der Angreifer Fehler in Betriebs- oder Anwendungssoftware ausgenutzt hat, sollte zusammen mit dem Hersteller bzw. den internen Entwicklern abgestimmt werden, wann und wie diese behoben werden. Ist es nicht möglich, die Schwachstellen zeitnah zu beheben und gibt es keine anderen Sicherungsmaßnahmen, sollte die Anwendung vorerst nicht weiter betrieben werden.
* Sind Teilnetze bereinigt, entscheidet das Leitungsgremium, wann und wie die Zugänge zu diesen Netzen wieder geöffnet werden. 
* Nachdem IT-Systeme und Netze wieder in Betrieb genommen wurden, sollte durch funktionale Tests geprüft werden, ob alle Anwendungen wieder einsatzbereit sind. Das Leitungsgremium entscheidet daraufhin, welche temporären Ausweichlösungen wieder aufgelöst oder dauerhaft übernommen werden.
#### DER.2.3.M3 Isolierung der betroffenen Netzabschnitte

Die Bereinigungsmaßnahmen beginnen damit, dass die betroffenen Netzbereiche isoliert werden. Ziel ist es, dem Angreifer den Zugriff auf die IT-Umgebung vollständig zu entziehen. Das sollte möglichst auf einen Schlag geschehen, damit der Angreifer nicht vorzeitig bemerkt, dass er entdeckt wurde und eventuell Gegenmaßnahmen ergreifen kann. Deshalb müssen die Netzabschnitte in einer konzertierten Aktion isoliert werden, dem sogenannten Cut-Off. 

Die Verantwortlichen sollten insbesondere sämtliche Internetzugänge auf einen Schlag abschalten, um die Kommunikation des Angreifers mit kompromittierten IT-Systemen zu verhindern. Zu diesem Zwecke müssen sämtliche Zugangswege identifiziert werden (siehe DER.2.3.M2 *Entscheidung für eine Bereinigungsstrategie*). Dazu zählen beispielsweise zentrale Zugänge, eventuell vorhandene Internet-Breakouts, z. B. DSL-Anschlüsse an einzelnen Standorten, redundante Anschlüsse und Notfallverbindungen, z. B. über UMTS/LTE. Es muss jedoch unbedingt vermieden werden, dass die IT-Umgebung versehentlich erneut an das Internet angeschlossen wird, bevor die Bereinigungsarbeiten abgeschlossen sind. 

Um IT-Systeme und Netze zu isolieren, sollte die Verbindung möglichst physisch getrennt werden, beispielsweise indem das entsprechende Netzkabel herausgezogen wird. Diese Vorgehensweise ist sicherer als Firewallregeln, Access Control Lists oder VLANs zu konfigurieren, um das Netz zu isolieren. Besteht der Verdacht, dass Netzgeräte kompromittiert wurden, müssen entweder die Verbindungen physisch getrennt oder die Geräte ausgeschaltet werden.

Sollte die forensische Untersuchung hinreichend sicher ergeben haben, dass nur einzelne Netzbereiche kompromittiert sind, beispielsweise eine einzelne Windows Domäne, so kann die Bereinigung auf diese Segmente begrenzt werden. In diesem Fall muss jedoch gewährleistet werden, dass die Bereiche zuverlässig von anderen Netzsegmenten abgeschottet sind.

Besonders mobile Clients sind schwer zu isolieren, da die IT zum Zeitpunkt der Isolation eventuell nicht auf alle Endgeräte zugreifen kann. Sollen mobile Endgeräte bereinigt werden, muss zunächst sichergestellt werden, dass sämtliche Zugänge (VPN, E-Mail usw.) dieser Geräte zum internen Netz getrennt werden. Es muss zudem sichergestellt sein, dass die Zugänge getrennt bleiben, bis die Bereinigungsmaßnahmen abgeschlossen sind. Anschließend müssen die Benutzer aufgefordert werden, ihr Endgerät zur Bereinigung einzureichen oder einzuschicken. 

#### DER.2.3.M4 Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln

Das wesentliche Ziel der Bereinigung eines weitreichenden Sicherheitsvorfalls ist es, den Zugriff des Angreifers auf die betroffene Umgebung zu beenden und zukünftig zu unterbinden. Hierzu reicht es nicht aus, ausschließlich die Schwachstelle zu schließen, die der Angreifer zur initialen Kompromittierung ausgenutzt hat. Vielmehr muss davon ausgegangen werden, dass er alle Zugangsdaten kennt, die auf den kompromittierten Rechnern vorhanden waren. Daher müssen alle Zugangsdaten geändert werden, nachdem das Netz isoliert wurde.

Zugangsdaten sind dabei zum einen lokal gespeicherte IT-System- und Anwendungskennwörter, aber auch Passwörter von Benutzern, die sich im betroffenen Zeitraum an dem IT-System angemeldet haben, da ihre Kennwörter oder davon abgeleitete Zugangsdaten gegebenenfalls aus dem Arbeitsspeicher des IT-Systems extrahiert wurden. Weiterhin müssen auch zentral verwaltete Zugangsdaten zurückgesetzt werden, z. B. in Active-Directory-Umgebungen oder wenn Lightweight Directory Access Protocol (LDAP) benutzt wurde. Wurde einer der zentralen Authentisierungsserver (Domaincontroller oder LDAP-Server) kompromittiert, so müssen sämtliche dort vorhandenen Zugänge gesperrt und ihre Passwörter ausgetauscht werden.

Wenn ein zentraler Authentisierungsserver zurückgesetzt wird, muss dabei besonders sorgfältig vorgegangen werden. Hierbei handelt es sich um selten durchgeführte Administrationsvorgänge, die zudem oft über technische Fallstricke verfügen. Um sich beispielsweise vor sogenannten Golden Tickets zu schützen, ist es notwendig, das Kennwort des KRBTGT-Accounts zweimal zurückzusetzen. Ein Golden Ticket ist ein gefälschtes Kerberos-Ticket, mit dem für einen Zeitraum von zehn Jahren neue Zugriffstickets ausgestellt werden können. Wird das zugehörige Kennwort nicht oder lediglich einmalig zurückgesetzt, so kann ein Angreifer mit einem zuvor erstellten Golden Ticket weiterhin Zugriffstickets ausstellen und damit auf das IT-System zugreifen. Deshalb sollten ausschließlich erfahrene Administratoren mit Unterstützung durch interne oder externe Forensikexperten die entsprechenden Maßnahmen durchführen.

Üblicherweise müssen in einer solchen Situation große Teile der vorhandenen Zugangsdaten neu aufgesetzt werden. Oftmals findet dies zu einem Zeitpunk statt, zu dem die meisten Benutzer nichts oder nur sehr wenig von dem Sicherheitsvorfall wissen. Eine vorige Information der Benutzer ist oft nur schwer zu realisieren, da die IT-Infrastruktur kompromittiert ist und der Angreifer nicht vorzeitig über die anstehende Bereinigung informiert werden soll. Aus diesem Grund ist mit vermehrten Anfragen an den Help- bzw. Servicedesk zu rechnen. Wenn möglich, sollten für die erwartbaren Passwort-Anfragen zusätzliche Mitarbeiter bereitgestellt werden. Diese sollten möglichst über ein Skript verfügen, das die Vorgehensweise und die Antworten auf die erwarteten Fragen enthält. Dieses Skript sollte im Rahmen des Krisenmanagements entworfen werden, eventuell mithilfe von PR-Mitarbeitern oder externen PR-Agenturen. Die Mitarbeiter müssen insbesondere darauf hingewiesen werden, dass keine alten Passwörter wiederverwendet werden dürfen und sie auch keine Passwörter wählen sollen, die einfach aus alten Passwörter abgeleitet werden können.

Gegebenenfalls müssen auf den betroffenen IT-Systemen nicht nur Benutzerkonten und deren Passwörter zurückgesetzt werden, sondern auch Dienstkonten. Diese Änderungen müssen durch die Administratoren der jeweiligen IT-Systeme vorgenommen werden.

Weiterhin muss darauf geachtet werden, dass sämtliches kryptografisches Schlüsselmaterial, das auf kompromittierten IT-Systemen gespeichert ist, ausgetauscht werden muss. Hierzu gehören beispielsweise TLS oder SSH-Schlüssel. Wenn zentrale Schlüsselspeicher, wie z. B. eines Certification-Authority-(CA)-Servers einer selbst betriebenen Public Key Infrastructure (PKI) kompromittiert wurden, müssen sie neu aufgesetzt werden. Das impliziert auch, dass dort vorhandene Schlüssel gesperrt werden und eventuell alles abgeleitete Schlüsselmaterial neu ausgerollt werden muss. Die Zertifikate sind durch einen entsprechenden Eintrag in einer Certificate Revocation List (CRL) oder auf einem OCSP-Server zu sperren. Je nach Anwendungsfall der kompromittierten Schlüssel ist gegebenenfalls auch eine globale Sperrung durch einen externen Validierungsdienst notwendig. In diesem Fall muss bedacht werden, dass durch die Veröffentlichung von Sperrlisteneinträgen bei einem externen Validierungsdienst, öffentlich gemacht wird, dass der Schlüssel möglicherweise kompromittiert ist. Daher muss der Zeitpunkt für diese Maßnahme sorgfältig gewählt werden. Eventuell sollte auch eine entsprechende begleitende Kommunikationsstrategie erarbeitet werden.

#### DER.2.3.M5 Schließen des initialen Einbruchswegs

Um zu verhindern, dass ein Angreifer erneut auf eine kompromittierte Umgebung zugreift, muss der initiale Einbruchsweg des APT-Angriffs geschlossen werden. Das darf jedoch erst geschehen, nachdem die betroffenen Netzumgebungen isoliert wurden. So wird verhindert, dass der Angreifer vorzeitig gewarnt wird und eventuell noch IT-Systeme sabotiert, Spuren verschleiert oder sich zusätzliche Hintertüren schafft. 

Der initiale Angriffsweg muss im Rahmen der forensischen Analyse identifiziert werden. Wurden für die Kompromittierung mehrere Schwachstellen ausgenutzt, so kann, wenn nötig, eine priorisierte Beseitigung der Schwachstellen erfolgen. 

Die möglichen Einbruchswege lassen sich grundsätzlich in zwei Klassen gliedern: technische Schwachstellen und Angriffe auf Mitarbeiter. Für alle technischen Schwachstellen muss die Hauptursache identifiziert und behoben werden. Typische Beispiele sind:

* Der Angreifer hat eine bekannte Schwachstelle in veralteter Software benutzt, um auf das IT-System zuzugreifen. In diesem Fall muss geprüft werden, ob es eine aktualisierte Version der Software gibt, die nicht mehr verwundbar ist. Der Einbruchsweg ist meist geschlossen, wenn die Software aktualisiert wird. 
* Der Angreifer hat eine Schwachstelle benutzt, für die keine Patches existieren oder die völlig unbekannt ist (Zero-Day-Exploit). Wenn die Schwachstelle nicht öffentlich bekannt ist, sollte Kontakt mit dem Hersteller der Software oder den internen Entwicklern aufgenommen werden, damit sie einen Patch oder andere Gegenmaßnahmen entwickeln können. Die Entwicklung eines Patches kann allerdings länger dauern. In der Zwischenzeit müssen deswegen andere Sofortmaßnahmen umgesetzt werden. Das betroffene IT-System kann z. B. vom Netz genommen oder durch Firewall-Regeln unerreichbar gemacht werden. Auch ein für die beobachtete Schwachstelle speziell entwickelter Schutz durch vorgelagerte IT-Systeme, beispielsweise mithilfe maßgeschneiderter Regeln in einer Web-Application-Firewall oder einem Intrusion-Prevention-System, kann erwogen werden. Hierfür ist allerdings spezielle Expertise notwendig.
* Der Angreifer hat ein falsch konfiguriertes IT-System ausgenutzt. Beispiele hierfür sind etwa die versehentliche Veröffentlichung schützenswerter Informationen im Internet, die Nutzung von Standard- oder leicht erratbaren Passwörtern auf extern erreichbaren IT-Systemen oder ein ungeschützter Dienst über das Internet. Hier muss das grundlegende Problem durch eine Konfigurationsänderung beseitigt werden.
Bei Angriffen auf Mitarbeiter ist es nicht einfach, die ursprüngliche Schwachstelle zu beseitigen, da sich solche Angriffe nicht vollständig durch technische Maßnahmen verhindern lassen. Beispiele für solche Angriffe sind etwa: 

* Die Angreifer versenden äußerst glaubhafte Phishing-E-Mails, die entweder Schadsoftware enthalten oder den Mitarbeiter dazu bringen, schützenswerte Informationen auf nicht vertrauenswürdigen Seiten einzugeben. 
* Die Angreifer benutzen sogenannte Water-Hole-Angriffe, bei denen Schadsoftware oder Phishing-Links gezielt auf Seiten hinterlegt werden, die für einzelne Mitarbeiter interessant erscheinen, sodass sie mit erhöhter Wahrscheinlichkeit darauf zugreifen. 
Vor solchen Angriffen können sich Institution durch Awareness-Maßnahmen (siehe ORP.3 *Sensibilisierung und Schulung zur Informationssicherheit*) für Mitarbeiter schützen. Sensibilisierte Mitarbeiter werden auch eher Angriffsversuche bemerken, melden und so dazu beitragen, dass Attacken frühzeitig detektiert werden können. Awareness-Maßnahmen sind nach einem erfolgreichen APT-Vorfall sinnvoll, sollten allerdings erst nach der Bereinigung durchgeführt werden. 

Es können aber auch technische Maßnahmen ergriffen werden, um Angriffe auf Mitarbeiter abzuwehren. So sollten beispielsweise die IT-Systeme gezielt gehärtet (siehe DER.2.3.A7 *Gezielte IT-Systemhärtung*) und Maßnahmen umgesetzt werden, mit denen sich die IT-Umgebung überwachen lässt (Monitoring). Weitere technische Maßnahmen sind:

* Ausbau der Antivirus-Infrastruktur durch zusätzliche Prüfungen von E-Mails, ausgehendem Internetverkehr oder der Client-Endgeräte, 
* die Entkopplung der Endgeräte vom Internet (beispielsweise durch ReCoBS-Systeme) oder 
* die Einführung von Zwei-Faktor-Authentisierung für besonders schützenswerte Zugänge.
Es sollte jedoch vermieden werden, erfolgreich angegriffene Mitarbeiter zu bestrafen. Die Qualität der APT-Angriffe ist sehr hoch und die eingesetzten E-Mails oder Internetseiten sind oft äußerst glaubwürdig gestaltet, sodass die Angriffe nur schwer zu erkennen sind. Disziplinarische Maßnahmen wären in einem solchen Fall nicht nur unfair, sondern würden auch zu einem Vertrauensverlust führen, sodass künftige Angriffe nicht mehr frühzeitig gemeldet und erkannt werden.

#### DER.2.3.M6 Rückführung in den Produktivbetrieb

Nachdem die Bereinigungsarbeiten abgeschlossen sind, sollte die abgekoppelte IT-Umgebung wieder in den Produktivbetrieb überführt werden. Damit die Bereinigung möglichst wenig die Verfügbarkeit einschränkt, kann dieser Schritt stufenweise für einzelne Netzsegmente erfolgen. Hierbei muss jedoch zwingend sichergestellt sein, dass noch nicht bereinigte Netzabschnitte auf keinen Fall mit bereits bereinigten verbunden werden.

Häufig ist es erst in dieser Phase möglich, neue Passwörter und Zugangsdaten für Endanwender zu verteilen. Hierbei ist mit vermehrten Supportanfragen zu rechnen (siehe DER.2.3.M4 *Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln*). Auch hier kann ein stufenweiser Wiederanlauf die Anfragen reduzieren bzw. über die Zeit verteilen. Wenn möglich, sollten vor dem Neustart des Produktivbetriebs funktionale Tests durchgeführt werden, um Supportanfragen oder als Angriffssymptome missverstandene Fehlersymptome zu vermeiden.

Die zurückgeführten IT-Systeme sollten durch ein verstärktes Monitoring begleitet werden. So lassen sich erneute Zugriffsversuche des Angreifers und eventuell bisher übersehene Hintertüren identifizieren. Dazu können die während der Beobachtungsphase eingerichteten Monitoringsysteme weiter benutzt werden. Die temporär eingerichteten Überwachungs- und Analysesysteme sollten daher für einen im Rahmen der Bereinigungsstrategie definierten und mit Datenschutz und Personalvertretung abgestimmten Zeitraum weiter betrieben werden. Für diesen Zeitraum ist ein erhöhter Aufwand für die Überwachung einzuplanen.

Nachdem diese Überwachungsperiode abgeschlossen ist, sollten die Überwachungs- und Analysesysteme entsorgt oder aber in den Produktivbetrieb überführt werden. Wenn sie entsorgt werden, ist zu entscheiden, ob und gegebenenfalls welche Beweismittel zur weiteren Verwendung (beispielsweise vertiefende Analysen, für Nachweispflichten oder eventuelle Weitergabe an Strafverfolgungs- oder Ermittlungsbehörden) archiviert werden. Sollen die IT-Systeme archiviert werden, so darf dies nur in einer ausreichend gesicherten, dem Schutzbedarf der Beweismittel angemessenen Umgebung erfolgen. Nicht mehr benötigte Beweismittel und IT-Systeme, die ausgesondert werden, müssen sicher gelöscht oder vernichtet werden (siehe DER.2.3.M9 *Hardwaretausch betroffener IT-Systeme*). Auch temporär eingerichtete Kommunikations- und Kollaborationslösungen sollten wieder zurückgebaut werden.

Wenn die Monitoring- und Analysesysteme in den produktiven Betrieb übergehen, ist zu prüfen, ob diese für den gedachten Anwendungsfall auch geeignet sind. Oftmals werden in der Aufklärungsphase von APT-Vorfällen Ad-hoc-Installationen durchgeführt, die den Anforderungen an einen mittel- oder langfristigen Produktivbetrieb nicht genügen. Eventuell müssen daher Projekte zur Überarbeitung der IT-Systeme aufgesetzt werden.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich Bereinigung weitreichender Sicherheitsvorfälle.

#### DER.2.3.M7 Gezielte Systemhärtung

Häufig nutzt ein Angreifer nicht nur eine einzelne Schwachstelle aus, sondern bedient sich über den Verlauf eines APT-Angriffs hinweg unterschiedlicher Lücken. Insbesondere kombinieren und benutzen Angreifer häufig verschiedene Schwachstellen, mangelnde IT-Systemhärtung und unzureichende Detektionsmechanismen, um sich im internen Netz zu bewegen und ihre Berechtigungen auszuweiten (privilege escalation). Neben der Beseitigung des initialen Einbruchsweges (siehe DER.2.3.A5 *Schließen des initialen Einbruchsweg*), sollten daher die IT-Systeme gehärtet werden, um die vom Angreifer genutzten Techniken zur Ausbreitung im internen Netz zu erschweren oder zu verhindern. Dabei sollten Maßnahmen, die sich mit wenig Aufwand realisieren lassen, möglichst schon während der Bereinigung durchgeführt werden. Aufwändige und weitreichende Maßnahmen können nach der Bereinigung als mittel- und langfristige Projekte umgesetzt werden.

Grundsätzlich gibt es zahlreiche unterschiedliche Möglichkeiten, einzelne IT-Systeme und gesamte Netzumgebungen zu härten. Die Auswahl der konkreten Maßnahmen hängt von den benutzen Techniken des Angreifers ab. Im Rahmen der forensischen Analyse sollten seine Werkzeuge und Vorgehensweisen zur Rechteausweitung und Bewegung innerhalb des Netzes identifiziert und konkrete Maßnahmen erarbeitet werden, mit denen APT-Angriffe zukünftig erschwert und besser detektiert werden können. Hierzu sollte der ISB gemeinsam mit den Forensikern und den für die jeweiligen IT-Systeme zuständigen Administratoren die Ergebnisse der forensischen Analysen auswerten und Gegenmaßnahmen erarbeiten.

Sinnvolle Härtungsmaßnahmen können beispielsweise auf Basis des IT-Grundschutz-Kompendiums identifiziert werden. Es sollte geprüft werden, ob für die IT-Umgebung bisher nicht erfüllte IT-Grundschutz-Anforderungen die Angriffe verhindert oder zumindest erschwert hätten. Die Umsetzung der jeweiligen Maßnahmen sollte erneut geprüft werden.

Härtungsmaßnahmen sind sehr spezifisch für die jeweilige Einzelumgebung und sollten auch möglichst individuell an diese Umgebung angepasst werden, z. B.:

* **Netzsegmentierung:** Nutzte der Angreifer eine flache oder nur grob segmentierte Umgebung aus, um Zugriff auf zahlreiche IT-Systeme zu erhalten, so bietet es sich an, das Netz in kleinere Segmente mit klar definierten und überwachten Übergängen aufzuteilen. Hierdurch wird die Anzahl der aus einem einzelnen Segment erreichbaren (und damit angreifbaren) IT-Systeme reduziert. Auch lassen sich oft die Übergänge zwischen kleineren, wohldefinierten Segmenten besser überwachen. Eine sehr feingranulare Netzsegmentierung erfordert detaillierte Kenntnisse des Netzes und insbesondere der betrieblich notwendigen Übergänge. Diese ist oftmals in Institutionen nicht vorhanden, weswegen eine feingranulare Segmentierung nur mittel- bis langfristig umsetzbar ist. Eine grobe Segmentierung lässt sich jedoch bereits im Zuge der Bereinigungsmaßnahmen umsetzen und erschwert die Bewegung eines Angreifers innerhalb des Netzes bereits erheblich.
* **Abschottung von Administrationssystemen:** Ein Spezialfall der zuvor genannten Segmentierung ist die Abschottung von administrativen IT-Systemen. Aufgrund ihrer hohen Privilegien und ihres zumeist weitreichenden Zugriffs innerhalb einer Netzumgebung sind Administratoren oftmals ein Zwischenziel bei APT-Angriffen. Deshalb sollten Administrationssysteme abgeschottet und administrative Tätigkeiten auf anormale Verhaltensmuster überwacht werden, z. B. durch ein geeignetes Monitoring. Das kann beispielsweise durch ein spezielles Admin-Netz, aus dem heraus alle Zugänge über (gehärtete und überwachte) Jumphosts oder Terminalserver erfolgen, umgesetzt werden. Administrative Zugriffe (beispielsweise über RDP oder SSH) dürfen dabei nur von diesen IT-Systemen aus erfolgen. Abweichungen hiervon sollten zu einer Alarmierung führen. Eine sehr weitreichende Architektur zur Abschottung von privilegierten Nutzern sind Microsofts Red-Forest- und ESAE-Architekturen. Die Konzepte dieser Architekturen können für eine Zielumgebung adaptiert werden, wobei viele der dort beschriebenen Maßnahmen nur mittel- bis langfristig umsetzbar sind.
* **Beschränkung von Dienstkonten:** Wurden bei einem APT-Angriff Dienstkonten missbraucht, sollten diese Konten gehärtet werden. Übliche Beispiele für solche Maßnahmen sind etwa der Betrieb von Diensten mit minimalen Privilegien. Dienste sollten möglichst nicht als *root* oder *SYSTEM* betrieben werden, sondern nur mit den Privilegien, die tatsächlich für den konkreten Einsatzzweck benötigt werden. Beispielsweise sollte das Konto für den Betrieb einer Datenbank nicht in das Stammverzeichnis des Webservers schreiben dürfen, falls beide Dienste auf demselben Server betrieben werden. Diese Prinzipien können mithilfe unterschiedlicher Techniken umgesetzt werden. Zum Beispiel können Dienste durch Container isoliert werden oder aber es können spezielle Techniken zur Steuerung von Dienstrechten genutzt werden, wie *managed service accounts* oder *group managed service accounts* unter Windows oder MAC-Systemen, wie SELinux oder AppArmor unter Linux.
* **Zusätzliche Absicherung externer Zugänge:** Konnte der Angreifer legitime externe Zugänge nutzen, beispielsweise die VPN-Zugänge von Mitarbeitern, sollten diese Zugänge gehärtet werden. Mögliche Maßnahmen könnten etwa die Einführung einer Zwei-Faktor-Authentisierung, ein Monitoring auf den Transfer größerer Datenmengen oder aber die Beschränkung der Zugriffszeiten sein. 
Häufig müssen Maßnahmen im Rahmen der Bereinigung unter hohem Zeitdruck umgesetzt werden, um den Zeitraum der Isolation und damit der nicht- oder stark eingeschränkten Verfügbarkeit der Umgebung zu minimieren. Daher werden häufig zunächst Ad-hoc-Lösungen ohne die sonst üblichen Prozesse und Maßnahmen zur Qualitätssicherung umgesetzt. Es ist deswegen wichtig, die umgesetzten Maßnahmen zu überprüfen, nachdem der Regelbetrieb wieder aufgenommen wurde und Projekte für die Überarbeitung und Qualitätssicherung der entsprechenden Maßnahmen aufzusetzen. Dabei sollte auch geplant werden, wie sich Maßnahmen umsetzen lassen, für die während der Bereinigung keine Zeit mehr war.

#### DER.2.3.M8 Etablierung sicherer, unabhängiger Kommunikationskanäle

Bei einem APT-Angriff kann die Kommunikationsinfrastruktur kompromittiert sein. Gerade in der Beobachtungsphase, wenn das genaue Ausmaß des Angriffs unbekannt ist, sollten daher die bestehenden Kommunikationskanäle nicht benutzt werden. Andernfalls kann der Angreifer frühzeitig gewarnt werden oder ist über die angedachten Gegenmaßnahmen informiert und kann darauf reagieren.

Möglicherweise betroffene Kommunikationskanäle können sein:

* Telefonie (insbesondere mit VoIP oder bei Integration mit der IT),
* E-Mail (bei Einsatz eines E-Mail-Gateways für die Verschlüsselung auch verschlüsselte Mailserver),
* Chat und Kollaborationswerkzeuge.
Auch wenn der Angreifer nicht den Inhalt der Kommunikation kennt, kann er jedoch beispielsweise aus Kommunikationsmustern ableiten, dass er entdeckt wurde. Genauso kann der Angreifer davon über Seitenkanäle, wie abgespeicherte Anrufnotizen oder Kalendereinträge von Kommunikationsbeziehungen, erfahren.

Das Leitungsgremium und alle mit der Bereinigung beauftragten Mitarbeiter sollten daher über unabhängige Kommunikationskanäle und gegebenenfalls auch über unabhängige Kollaborationswerkzeuge verfügen. Darüber hinaus sollte geregelt werden, wann über die etablierten Kanäle kommuniziert werden darf und wann zwingend die unabhängigen Kanäle zu benutzen sind.

Es ist nicht notwendig, alle entfallenen Kommunikationskanäle zu ersetzen. Eine einfache Möglichkeit bieten persönliche Treffen und ein räumlich nahes Zusammenarbeiten des Leitungsgremiums und der direkten Unterstützer.

Üblicherweise ist es nicht möglich, neben den laufenden Untersuchungs- und Bereinigungsaktivitäten noch eine parallele Kommunikationsinfrastruktur aufzubauen. Daher wird in einer solchen Situation häufig auf Kommunikationsdienste Dritter zurückgegriffen. Bei der Auswahl eines geeigneten Kommunikationskanals ist darauf zu achten, dass die Vertraulichkeit und Integrität der Kommunikation möglichst gut geschützt wird.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.2.3.M9 Hardwaretausch betroffener IT-Systeme(CIA)

Bei einem APT-Angriff können Angreifer auch über die üblichen Wege hinaus (Betriebssystem, Anwendungen) die IT-Systeme manipulieren. Dazu gehören:

* hardwarenahe Software (z. B. UEFI),
* Firmware von Systemkomponenten (z. B. CPU, GPU, Zusatzhardware),
* nicht direkt betroffene Zusatzkomponenten (z. B. Fernwartungslösungen wie ILO)
* Firmware von Netzgeräten und eingebetteten Geräten (z. B. USV),
* sicherheitskritische Einstellungen der genannten Software (z. B. nicht dokumentierte Optionen und nicht in den Wartungsprogrammen abrufbare Optionen).
Da es häufig zu diesen Komponenten jeweils nur einen eingeschränkten Zugang über die Firmware selbst gibt, kann ein Angreifer seine Manipulationen leicht verschleiern. 

Diese Art von Angriffen ist für den Angreifer jedoch zeitlich, technisch und organisatorisch aufwändig. Zusätzlich muss er über weitreichenden Zugriff auf dem IT-System verfügen und den Angriff stark an die jeweilige Zielplattform anpassen. Ein solcher Angriffsvektor ist eher unwahrscheinlich, aber gerade bei einem APT-Angriff nicht auszuschließen.

Solche Manipulationen können von einer Institution nur mit hohem Aufwand und Spezialkenntnissen entdeckt werden. Da der Selbstauskunft der Komponenten nicht vertraut werden kann, müssen die Einstellungen und Firmwaredateien unabhängig von der laufenden Komponente extrahiert und analysiert werden.

Bei der Entscheidung über die Bereinigungsstrategie (siehe DER.2.3.A2 *Entscheidung für eine Bereinigungsstrategie*) sollte mindestens für Geräte mit hohem Schutzbedarf und solchen, die in Netzen mit hohem Schutzbedarf eingesetzt werden, überlegt werden, die potenziell manipulierte Hardware zu ersetzen. Grundsätzlich gibt es drei mögliche Behandlungsstrategien: 

* **Keine besondere Behandlung:** Die forensische Analyse hat ergeben, dass eine Manipulation ausgeschlossen ist, da der Angreifer nicht über den nötigen Zugriff verfügte, die Komponente verlässlich gegen Manipulation gesichert ist und eine Extraktion der Firmware auch keine Hinweise auf eine Manipulation gegeben hat. Nur wenn alle diese Punkte gegeben sind, kann die Komponente für die Neuinstallation genutzt werden.
* **Software und Einstellungen zurücksetzen:** Es ist laut forensischer Analyse möglich, die IT-Systeme zu bereinigen, indem sie in den Auslieferungszustand zurückgesetzt werden oder die Firmware erneut eingespielt wird. Die Komponente ist so gestaltet, dass ein Zurücksetzen in den Auslieferungszustand oder das erneute Einspielen der Firmware unabhängig von der potenziell manipulierten Software selbst möglich ist (z. B. auf einem gesonderten Datenträger oder über einen Bootloader im ROM). In diesem Fall kann die Komponente so auch bereinigt und dann für die Neuinstallation genutzt werden. 
* **Hardware tauschen:** Da eine verlässliche Erkennung unwirtschaftlich ist, sollte im Zweifel von einer Manipulation ausgegangen werden. In diesem Fall ist das gesamte System, mindestens jedoch die betroffene Komponente gegen ein Neugerät auszutauschen. 
Jedes potenziell betroffene IT-System sollte in eine der drei Gruppen klassifiziert werden. Wenn es ausreichend Gründe gibt, auf einen Hardwaretausch zu verzichten, ist die Entscheidung im Rahmen der Bereinigungsstrategie begründet zu dokumentieren.

Werden neue oder zurückgesetzte IT-Systeme wieder eingerichtet, kann dabei auf bestehende Wiederanlaufpläne zurückgegriffen werden. Können hierfür Datensicherungen der Komponenten benutzt werden, sollten diese jedoch nur eingesetzt werden, wenn sie zweifelsfrei vor der Kompromittierung angelegt wurden. Da diese Sicherungen häufig in einem undokumentierten Format angelegt werden, ist es sehr aufwändig, diese zu überprüfen. Im Zweifel sollte daher neu konfiguriert und das Backup nicht verwendet werden.

Ausgesonderte Geräte müssen geeignet entsorgt werden. Sie sollten möglichst nicht an Leasingpartner zurückgegeben oder als Gebrauchtgeräte verkauft werden.

#### DER.2.3.M10 Umbauten zur Erschwerung eines erneuten Angriffs durch denselben Angreifer(CI)

Während eines APT-Angriffs erwirbt ein Angreifer üblicherweise detailliertes Wissen darüber, wie die Zielumgebung aufgebaut und konfiguriert ist. Im Rahmen der Netzerkundung (Reconnaissance) lernt er, wie Netzabschnitte sowie Namensschemata für IT-Systeme aufgebaut sind. Auch kennt er Benutzer- und Dienstkonten, eingesetzte Software und Services sowie Methoden für Administration und Wartung. Dieses detaillierte Wissen erleichtert es ihm, dieselbe Umgebung erneut anzugreifen. Gelingt es dem Angreifer nach der Bereinigung, sich erneut Zugang zur IT-Umgebung zu verschaffen, z. B. indem er eine neue Schwachstelle oder eine übersehene Hintertür ausnutzt, kann er sein Wissen dazu benutzen, um innerhalb kurzer Zeit wieder weitreichende Kontrolle über die Zielumgebung zu erlangen.

Um einem APT-Angreifer die erneute tiefgreifende Kompromittierung einer Umgebung zu erschweren, kann die IT-Umgebung gezielt umgebaut werden, sodass das Wissen des Angreifers über den internen Aufbau nutzlos ist. Beispiele für solche Maßnahmen sind:

* Nutzung anderer IP-Adressbereiche für Netzsegmente und/oder anderer IP-Adressen für einzelne IT-Systeme,
* Änderung von Namensschemata für Computer und/oder Änderung von Namen einzelner IT-Systeme,
* Änderung von Namensschemata für Anwender- und Dienstkonten und/oder Änderung von Namen für einzelne Konten,
* Änderung von URL-Pfaden für Webanwendungen und/oder Web-Services.
Werden die Maßnahmen umgesetzt, müssen die relevanten Dokumentationen aktualisiert sowie die Nutzer benachrichtigt und durch Administratoren begleitet werden.

Bei den beschriebenen Maßnahmen handelt es sich nicht um Sicherheitsmaßnahmen im eigentlichen Sinne. Es sind vielmehr Verschleierungsmaßnahmen, die jedoch einen gewissen Schutz bieten können. Zum einen ist dann eine erneute Kompromittierung für den Angreifer aufwändiger, da er zuvor gewonnenes Wissen nicht wiederverwerten kann. Zum anderen können die beschriebenen Maßnahmen durch gezielte Detektion ergänzt werden. Werden Detektionsmechanismen etabliert, die auf die Nutzung des alten Angreiferwissens abzielen, steigt die Chance, einen wiederkehrenden Angreifer zu erkennen. Setzt er beispielsweise eine ehemals verwendete IP-Adresse oder einen alten Kontonamen ein, wird darüber der IT-Betrieb alarmiert. Solche Alarmierungen führen in der Anfangsphase nach einer Umstellung häufig zu vielen Fehlalarmen, da noch nicht alle Konfigurationen von benachbarten IT-Systemen angepasst wurden oder Benutzer und Administratoren sich noch nicht an die geänderten Gegebenheiten angepasst haben. Diese Fehlalarme lassen sich jedoch typischerweise mit überschaubarem Aufwand aussortieren und nehmen mit der Zeit ab, sodass letztlich ein hochwertiges Alarmierungskriterium etabliert werden kann.

Ebenso sollte gezieltes Monitoring eingesetzt werden, wenn das *KRBTGT*-Passwort zweimal zurückgesetzt wurde, um Golden-Ticket-Angriffe zu vermeiden (siehe auch DER.2.3.A4 *Sperrung und Änderung von Zugangsdaten und kryptografischen Schlüsseln*). Anschließend sollte überwacht werden, ob ungültige Kerberos-Tickets eingesetzt werden. Die Nutzung entsprechender Tickets lässt sich über Einträge mit der Event-ID *4769* im Security-Event-Log der Domänencontroller erkennen. Ist hier der Fehler-Code auf den Wert *0x1f* gesetzt, deutet das auf *Golden Tickets* hin und sollte zu einer umgehenden Alarmierung führen.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Bereinigung weitreichender Sicherheitsvorfälle" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [CS072] Erste Hilfe bei einem APT Angriff

  

 Bundesamt für Sicherheit in der Informationstechnik, Version 3.0, 01.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_072\_TLP-White.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_072_TLP-White.pdf)

 
* #### [DRP] Data Breach Response Guide

  

 Experian Data Breach Resolution, 2013  
 <https://www.experian.com/assets/data-breach/brochures/response-guide.pdf>

 
* #### [GMSA] Windows Server 2012: Group Managed Service Accounts

  

 Microsoft, (zuletzt abgerufen 05.10.2017)  
 <https://blogs.technet.microsoft.com/askpfeplat/2012/12/16/windows-server-2012-group-managed-service-accounts/>

 
* #### [KGT] Protection from Kerberos Golden Ticket

  

 CERT-EU, 06.2014  
 [https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP\_14\_07\_PassTheGolden\_Ticket\_v1\_1.pdf](https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP_14_07_PassTheGolden_Ticket_v1_1.pdf)

 
* #### [MSMSA] Managed Service Accounts

  

 Understanding, Implementing, Best Practices and Troubleshooting Microsoft (zuletzt abgerufen 05.10.2017)  
 <https://blogs.technet.microsoft.com/askds/2009/09/10/managed-service-accounts-understanding-implementing-best-practices-and-troubleshooting/>

 
* #### [PARM] Securing Privileged Access Reference Material

  

 Microsoft TechNet, (zuletzt abgerufen 05.10.2017)  
 <https://technet.microsoft.com/en-us/windows-server-docs/security/security-privileged-access/securing-privileged-access-reference-material>

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote-Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
* #### [SANS1] When Breaches Happen: Top Five Questions to Prepare For

  

 SANS Institute, 2000  
 <https://www.sans.org/reading-room/whitepapers/analyst/breaches-happen-top-questions-prepare-35220>

 
* #### [SANS2] Detection and Recovery from a Major security Breach

  

 SANS Institute, 2000  
 <https://giac.org/paper/gcux/50/detection-recovery-major-security-breach/100810>

 
