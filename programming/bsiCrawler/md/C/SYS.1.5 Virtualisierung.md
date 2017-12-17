1 Beschreibung
--------------

### 1.1 Einleitung

Bei der Virtualisierung von IT-Systemen werden ein oder mehrere virtuelle IT-Systeme auf einem physischen IT-System ausgeführt. Ein solches physisches IT-System wird als Virtualisierungsserver bezeichnet. Mehrere Virtualisierungsserver können zu einer virtuellen Infrastruktur zusammengefasst werden. Darin können die Virtualisierungsserver selbst und die auf ihnen betriebenen virtuellen IT-Systeme gemeinsam verwaltet werden.

Die Virtualisierung von IT-Systemen bietet viele Vorteile für den IT-Betrieb in einem Informationsverbund. Es können Kosten für Hardwarebeschaffung, Strom und Klimatisierung eingespart werden, wenn die Ressourcen der physischen IT-Systeme effizienter genutzt werden. Allerdings ist die Virtualisierung auch eine Herausforderung für den Betrieb des Informationsverbundes. Da durch die eingesetzte Virtualisierungstechnik unterschiedliche Bereiche und Arbeitsfelder im Informationsverbund berührt werden, müssen Wissen und Erfahrungen aus den unterschiedlichsten Bereichen zusammengeführt werden. 

### 1.2 Zielsetzung

Der Baustein beschreibt, wie virtualisierte IT-Systeme im Informationsverbund sicher eingeführt und betrieben werden können.

### 1.3 Abgrenzung

In diesem Baustein wird nur die Virtualisierung vollständiger IT-Systeme behandelt, andere Techniken, die teilweise ebenfalls mit dem Wort Virtualisierung in Verbindung gebracht werden (Anwendungsvirtualisierung mittels Terminalservern, Storage-Virtualisierung, Container etc.), sind nicht Gegenstand dieses Bausteins. 

Im Bereich der Software-Entwicklung werden die Begriffe *Virtuelle Maschine* und *Virtueller-Maschinen-Monitor* auch für Laufzeitumgebungen benutzt, z. B. Java, Microsoft .NET. Solche Laufzeitumgebungen werden in diesem Baustein ebenfalls nicht betrachtet. 

Virtuelle Infrastrukturen werden in der Regel mit speziellen Management-Systemen verwaltet. Da mit diesen umfassend auf die Virtualisierungsinfrastruktur zugegriffen werden kann, ist es wichtig, diese ausreichend abzusichern. Das betrifft sowohl den Server (kann physisch oder virtuell sein), auf dem die Management-Software ausgeführt wird, als auch das Produkt selber. Details werden im Baustein NET.1.2 *Netzmanagement* beschrieben. 

Virtualisierungsumgebungen werden meistens gemeinsam mit Massenspeichern (NAS oder SAN) eingesetzt. Anbindung und Absicherung dieser Systeme werden in diesem Baustein ebenfalls nicht betrachtet (siehe hierfür Baustein SYS.1.8 *Speicherlösungen*). 

Durch die Virtualisierung müssen die Netze der Institution anders strukturiert werden. Dieses Thema wird in diesem Baustein nicht umfassend behandelt. Dafür muss der Baustein NET.1.1 *Netzarchitektur und -design *umgesetzt werden. Auch die Netzvirtualisierung wird im vorliegenden Baustein nur angerissen. Sicherheitsaspekte von virtuellen Netzkomponenten werden im Baustein NET.1.4 *Netzvirtualisierung* behandelt.

Um virtuelle IT-Systeme abzusichern, müssen die jeweils zutreffenden Bausteine der Schicht *SYS (IT-Systeme)* angewendet werden. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Virtualisierung von besonderer Bedeutung:

### 2 1 Fehlerhafte Planung der Virtualisierung

Ein Virtualisierungsserver ermöglicht den Betrieb virtueller IT-Systeme, integriert die Systeme in das Rechenzentrum und steuert dabei deren Anbindung an weitere Infrastrukturelemente, z. B. Netze und Speichernetze. Wird nicht geplant, wie die Virtualisierungsserver technisch und organisatorisch in die bestehende Infrastruktur zu integrieren sind, kann dies dazu führen, dass die Verantwortlichkeiten für unterschiedliche Bereiche womöglich nicht klar definiert sind, z. B. für Anwendungen, Betriebssysteme und Netzkomponenten. Weiterhin können sich die Zuständigkeiten verschiedener Bereiche überschneiden oder es ist keine passende Rechtestruktur vorhanden, um administrative Zugriffe für die unterschiedlichen Bereiche zu trennen. 

### 2 2 Fehlerhafte Konfiguration der Virtualisierung

Durch Virtualisierung ändert sich die Art und Weise, wie Server provisioniert werden. Ressourcen wie CPU, RAM, Netzanbindung und Speicher werden in der Regel zentral über ein Management-System konfiguriert und sind nicht mehr durch Hardware und Verkabelung vorgegeben. Dadurch kann es schneller zu Konfigurationsfehlern kommen. Wird beispielsweise ein hoch schutzbedürftiges virtuelles IT-System fälschlicherweise in einer externen DMZ platziert, ist dieses dadurch aus dem Internet erreichbar und somit einem erhöhten Risiko ausgesetzt.

### 2 3 Unzureichende Ressourcen für virtuelle IT-Systeme

Virtualisierungsserver benötigen für den Betrieb der virtuellen IT-Systeme Speicherplatz, der entweder lokal im Virtualisierungsserver selbst oder in einem Speichernetz bereitgestellt wird. Werden die hierfür benötigten Speicherkapazitäten nicht ausreichend groß geplant, bestehen weitreichende Risiken für die Verfügbarkeit der virtuellen IT-Systeme und die Integrität der in ihnen verarbeiteten Informationen. Das gilt insbesondere dann, wenn spezielle Virtualisierungsfunktionen, wie Snapshots oder die Überbuchung von Speicherplatz, benutzt werden. 

Engpässe können nicht nur den Speicherplatz auf Festplatten oder in Speichernetzen betreffen, sondern auch den Arbeitsspeicher (RAM) oder die Netzanbindung. Außerdem könnten sich durch unzureichende Ressourcen auf dem Virtualisierungsserver die virtuellen Maschinen gegenseitig in ihrem Betrieb stören und letztlich nicht mehr korrekt arbeiten oder ganz ausfallen. 

### 2 4 Informationsabfluss oder Ressourcen-Engpass durch Snapshots

Durch einen Snapshot kann der Zustand einer virtuellen Maschine eingefroren und gesichert werden. Wird ein solcher Snapshot zu einem späteren Zeitpunkt wiederhergestellt, gehen alle in der Zwischenzeit vorgenommenen Änderungen verloren. Dadurch können auch bereits gepatchte Sicherheitslücken wieder offen sein. Weiterhin können durch offene Dateien, Dateitransfers oder Datenbanktransaktionen zum Zeitpunkt des Snapshots inkonsistente Daten entstehen.

Außerdem können Angreifer Snapshots dazu missbrauchen, um unberechtigt auf die Daten eines virtuellen IT-Systems zuzugreifen. Denn wenn der Snapshot im laufenden Betrieb erstellt wurde, ist auch der Inhalt des Hauptspeichers auf die Festplatte gesichert worden und kann auf einer virtuellen Umgebung außerhalb der ursprünglichen IT-Infrastruktur wiederhergestellt und analysiert werden. Ebenso können Snapshots sehr groß werden und dadurch kann die Speicherkapazität knapp werden.

### 2 5 Ausfall des Verwaltungsservers für Virtualisierungssysteme

Da über den Verwaltungsserver sämtliche Funktionen einer virtuellen Infrastruktur gesteuert und administriert werden, führt ein Ausfall dieses Verwaltungssystems dazu, dass keine Konfigurationsänderungen an der virtuellen Infrastruktur durchgeführt werden können. Die Administratoren können in dieser Zeit weder auf auftretende Probleme wie Ressourcenengpässe oder den Ausfall einzelner Virtualisierungsserver reagieren noch neue Virtualisierungsserver in die Infrastruktur integrieren bzw. neue virtuelle IT-Systeme anlegen. Auch die *Live Migration* und damit die dynamische Zuteilung von Ressourcen für einzelne Gast-Systeme ist ohne Verwaltungsserver nicht möglich. 

### 2 6 Missbräuchliche Nutzung von Gastwerkzeugen

Gastwerkzeuge werden häufig mit sehr hohen Berechtigungen ausgeführt. Dadurch lassen sie sich beispielsweise für Denial-of-Service-Angriffe missbrauchen oder Angreifer übernehmen mit ihnen gleich das ganze Host-System.

### 2 7 Kompromittierung der Virtualisierungssoftware

Die Virtualisierungssoftware (auch: Hypervisor) ist die zentrale Komponente eines Virtualisierungsservers, sie steuert alle auf diesem Server ausgeführten virtuellen Maschinen und teilt ihnen Prozessor- und Speicherressourcen zu. Wird diese Komponente erfolgreich angegriffen, führt dies auch dazu, dass alle virtuellen IT-Systeme des Servers kompromittiert sind.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Virtualisierung aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.1.5.A1 Einspielen von Aktualisierungen und Sicherheitsupdates

Host-Betriebssystem, Management-Software und Hardware-Firmware MÜSSEN regelmäßig aktualisiert werden. Vorhandene Sicherheitsupdates MÜSSEN zeitnah eingespielt werden. Vorab MUSS auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. 

#### SYS.1.5.A2 Sicherer Einsatz virtueller IT-Systeme

Jeder Administrator von virtuellen IT-Systemen MUSS wissen, wie sich eine Virtualisierung auf die betriebenen IT-Systeme und Anwendungen auswirkt. Die Zugriffsrechte für Administratoren auf virtuelle IT-Systeme MÜSSEN auf das tatsächlich notwendige Maß reduziert sein. 

Es MUSS gewährleistet sein, dass die für die virtuellen IT-Systeme notwendigen Netzverbindungen in der virtuellen Infrastruktur verfügbar sind. Auch MUSS geprüft werden, ob die Anforderungen an die Isolation und Kapselung der virtuellen IT-Systeme sowie der darauf betriebenen Anwendungen hinreichend erfüllt sind. Weiterhin MÜSSEN die eingesetzten virtuellen IT-Systeme den Anforderungen an die Verfügbarkeit und den Datendurchsatz genügen. Im laufenden Betrieb MUSS die Performance der virtuellen IT-Systeme überwacht werden.

#### SYS.1.5.A3 Sichere Konfiguration virtueller IT-Systeme

Gast-Systeme DÜRFEN NICHT auf Geräte und Schnittstellen des Virtualisierungsservers zugreifen. Ist eine solche Verbindung jedoch notwendig, MUSS diese exklusiv und nur für die notwendige Dauer vom Administrator des Host-Systems hergestellt werden. Dafür MÜSSEN verbindliche Regelungen festgelegt werden. 

Virtuelle IT-Systeme SOLLTEN nach den Sicherheitsrichtlinien der Institution konfiguriert und geschützt werden (siehe dazu die jeweils passenden Bausteine der Schicht *SYS*). 

#### SYS.1.5.A4 Sichere Konfiguration eines Netzes für virtuelle Infrastrukturen

Es MUSS sichergestellt werden, dass bestehende Sicherheitsmechanismen (z. B. Firewalls) und Monitoring-Systeme nicht durch virtuelle Netze umgangen werden können. Auch MUSS ausgeschlossen sein, dass über virtuelle IT-Systeme, die mit mehreren Netzen verbunden sind, unerwünschte Netzverbindungen aufgebaut werden können.

Netzverbindungen zwischen virtuellen IT-Systemen und physischen IT-Systemen sowie für virtuelle Sicherheitsgateways SOLLTEN gemäß den Sicherheitsrichtlinien der Institution konfiguriert werden. 

#### SYS.1.5.A5 Schutz der Administrationsschnittstellen

Alle Administrations- und Management-Zugänge zum Mananagement-System und zu den Host-Systemen MÜSSEN eingeschränkt werden. Es MUSS sichergestellt sein, dass aus nicht-vertrauenswürdigen Netzen heraus nicht auf die Administrationsschnittstellen zugegriffen werden kann.

Um die Virtualisierungsserver oder die Management-Systeme zu administrieren bzw. zu überwachen, SOLLTEN ausreichend verschlüsselte Protokolle eingesetzt werden. Sollte dennoch auf unverschlüsselte und damit unsichere Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz genutzt werden. 

#### SYS.1.5.A6 Protokollierung in der virtuellen Infrastruktur

Betriebszustand, Auslastung und Netzanbindungen der virtuellen Infrastruktur MÜSSEN laufend protokolliert werden. Werden Kapazitätsgrenzen erreicht, MÜSSEN virtuelle Maschinen verschoben und eventuell die Hardware erweitert werden. Die Protokollierungsdaten SOLLTEN regelmäßig ausgewertet werden.

#### SYS.1.5.A7 Zeitsynchronisation in virtuellen IT-Systemen

Die Systemzeit aller produktiv eingesetzten IT-Systeme MUSS immer synchron sein (siehe auch OPS.1.1.5 *Protokollierung*).

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Virtualisierung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.1.5.A8 Planung einer virtuellen Infrastruktur [Leiter IT, Leiter Netze]

Der Aufbau der virtuellen Infrastruktur SOLLTE detailliert geplant werden. Dabei SOLLTEN die geltenden Regelungen und Richtlinien für den Betrieb von IT-Systemen, Anwendungen, Netzen und Speichernetzen berücksichtigt werden. Wenn mehrere virtuelle IT-Systeme auf einem Virtualisierungsserver betrieben werden, SOLLTEN keine Konflikte hinsichtlich des Schutzbedarfs der IT-Systeme auftreten. 

Weiterhin SOLLTEN die Aufgaben der einzelnen Administratorengruppen festgelegt und klar voneinander abgegrenzt werden. Es SOLLTE auch geregelt werden, welcher Mitarbeiter für den Betrieb welcher Komponente verantwortlich ist. Die Administratoren SOLLTEN ausreichend qualifiziert sein. 

#### SYS.1.5.A9 Netzplanung für virtuelle Infrastrukturen [Leiter IT, Leiter Netze]

Der Aufbau des Netzes für virtuelle Infrastrukturen SOLLTE detailliert geplant werden. Dafür SOLLTE der Baustein NET.1.1 *Netzarchitektur und -design *berücksichtigt werden. Auch SOLLTE geprüft werden, ob für bestimmte Virtualisierungsfunktionen (wie z. B. die *Live Migration*) ein eigenes Netz aufgebaut und genutzt werden muss. 

Es SOLLTE geplant werden, welche Netzsegmente aufgebaut werden müssen (z. B. Managementnetz, Speichernetz) und wie sie sich sicher voneinander trennen und schützen lassen. Dabei SOLLTE sichergestellt werden, dass das produktive Netz vom Managementnetz getrennt ist (siehe SYS.1.5.A11 *Administration der Virtualisierungsinfrastruktur über ein gesondertes Managementnetz*). Auch die Verfügbarkeitsanforderungen an das Netz SOLLTEN beachtet und erfüllt werden.

#### SYS.1.5.A10 Einführung von Verwaltungsprozessen für virtuelle IT-Systeme [Leiter IT]

Für Virtualisierungsserver und virtuelle IT-Systeme SOLLTEN Prozesse für die Inbetriebnahme, die Inventarisierung, den Betrieb und die Außerbetriebnahme definiert und etabliert werden. Die Prozesse SOLLTEN dokumentiert und regelmäßig aktualisiert werden. 

Wenn der Einsatz geplant wird, SOLLTE festgelegt werden, welche Virtualisierungsfunktionen die virtuellen IT-Systeme benutzen dürfen. 

Bevor ein virtuelles IT-System betrieben wird, SOLLTE in einer Test- und Entwicklungsumgebung geprüft werden, ob es für den Produktiveinsatz geeignet ist. Test- und Entwicklungsumgebungen SOLLTEN NICHT auf demselben Virtualisierungsserver betrieben werden wie produktive virtuelle IT-Systeme. 

#### SYS.1.5.A11 Administration der Virtualisierungsinfrastruktur über ein gesondertes Managementnetz

Die Virtualisierungsinfrastruktur SOLLTE ausschließlich über ein separates Managementnetz administriert werden. Die verfügbaren Sicherheitsmechanismen der eingesetzten Managementprotokolle zur Authentisierung, Integritätssicherung und Verschlüsselung SOLLTEN aktiviert und alle unsicheren Managementprotokolle deaktiviert werden (siehe NET.1.2 *Netz-Management*).

#### SYS.1.5.A12 Rechte- und Rollenkonzept für die Administration einer virtuellen Infrastruktur

Anhand der in der Planung definierten Aufgaben und Rollen (siehe SYS.1.5.A8 *Planung einer virtuellen Infrastruktur*) SOLLTE für die Administration virtueller IT-Systeme und Netze, der Virtualisierungsserver sowie der Management-Umgebung ein Rechte- und Rollenkonzept erstellt und umgesetzt werden. Alle Komponenten der virtuellen Infrastruktur SOLLTEN in ein zentrales Identitäts- und Berechtigungsmanagement eingebunden werden.

Administratoren von virtuellen Maschinen und Administratoren der Virtualisierungsumgebung SOLLTEN unterschieden und mit unterschiedlichen Zugriffsrechten ausgestattet werden. 

Weiterhin SOLLTE die Management-Umgebung virtuelle Maschinen gruppieren können, um eine geeignete Strukturierung verbunden mit einer entsprechenden Administratoren-Rollenzuteilung einzuführen. 

#### SYS.1.5.A13 Auswahl geeigneter Hardware für Virtualisierungsumgebungen

Die verwendete Hardware SOLLTE kompatibel zur eingesetzten Virtualisierungslösung sein. Dabei SOLLTE darauf geachtet werden, dass der Hersteller der Virtualisierungslösung über den geplanten Einsatzzeitraum auch Support für die betriebene Hardware anbietet.

#### SYS.1.5.A14 Einheitliche Konfigurationsstandards für virtuelle IT-Systeme [Leiter IT]

Für die eingesetzten virtuellen IT-Systeme SOLLTEN einheitliche Konfigurationsstandards definiert werden. Die virtuellen IT-Systeme SOLLTEN nach diesen Standards konfiguriert werden. Die Konfigurationsstandards SOLLTEN regelmäßig überprüft und falls erforderlich angepasst werden.

#### SYS.1.5.A15 Betrieb von Gast-Betriebssystemen mit unterschiedlichem Schutzbedarf

Falls virtuelle IT-Systeme mit unterschiedlichem Schutzbedarf gemeinsam auf einem Virtualisierungsserver betriebenen werden, SOLLTE dabei sichergestellt sein, dass die virtuellen IT-Systeme ausreichend gekapselt und voneinander isoliert sind. Auch SOLLTE dann die Netztrennung in der eingesetzten Virtualisierungslösung ausreichend sicher sein. Ist das nicht der Fall, SOLLTEN weitergehende Sicherheitsmaßnahmen identifiziert und umgesetzt werden.

#### SYS.1.5.A16 Kapselung der virtuellen Maschinen

Die Funktionen *Kopieren* und *Einfügen* von Informationen zwischen virtuellen Maschinen SOLLTEN deaktiviert sein. 

#### SYS.1.5.A17 Überwachung des Betriebszustands und der Konfiguration der virtuellen Infrastruktur

Der Betriebszustand der virtuellen Infrastruktur SOLLTE überwacht werden. Dabei SOLLTE z. B. geprüft werden, ob noch ausreichend Ressourcen verfügbar sind und ob es eventuell Konflikte bei gemeinsam benutzten Ressourcen eines Virtualisierungsservers gibt.

Weiterhin SOLLTEN die Konfigurationsdateien der virtuellen IT-Systeme regelmäßig auf unautorisierte Änderungen überprüft werden. Auch SOLLTE überwacht werden, ob die virtuellen Netze den jeweiligen virtuellen IT-Systemen korrekt zugeordnet sind. 

Werden Konfigurationsänderungen an der Virtualisierungsinfrastruktur vorgenommen, SOLLTEN diese geprüft bzw. getestet werden, bevor sie umgesetzt werden.

#### SYS.1.5.A18 Schulung der Administratoren virtueller Umgebungen [Vorgesetzte, Leiter IT, Leiter Netze]

Alle Administratoren der virtuellen Umgebung SOLLTEN ausreichend geschult werden. In der Schulung SOLLTE vermittelt werden, wie virtuelle Infrastrukturen sicher aufgebaut und betrieben werden können. 

#### SYS.1.5.A19 Regelmäßige Audits der Virtualisierungsinfrastruktur

Es SOLLTE regelmäßig auditiert werden, ob der Ist-Zustand der virtuellen Infrastruktur dem in der Planung festgelegtem Zustand entspricht und ob die Konfiguration der virtuellen Komponenten die vorgegebene Standardkonfiguration einhält. Die Auditergebnisse SOLLTEN nachvollziehbar dokumentiert werden. Abweichungen SOLLTEN behoben werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.1.5.A20 Verwendung von hochverfügbaren Architekturen [Leiter IT, Leiter Netze](A)

Die virtuelle Infrastruktur SOLLTE hochverfügbar ausgelegt werden. Alle Virtualisierungsserver SOLLTEN in Clustern zusammengeschlossen werden.

#### SYS.1.5.A21 Sichere Konfiguration virtueller IT-Systeme bei erhöhtem Schutzbedarf(IA)

Für virtuelle IT-Systeme SOLLTEN Überbuchungsfunktionen für Ressourcen deaktiviert werden.

#### SYS.1.5.A22 Härtung des Virtualisierungsservers(CI)

Der Virtualisierungsserver SOLLTE gehärtet werden. Um virtuelle IT-Systeme voreinander und gegenüber dem Virtualsierungsserver zusätzlich zu isolieren und zu kapseln, SOLLTEN Mandatory Access Controls eingesetzt werden. Ebenso SOLLTE das IT-System gehärtet werden, auf dem die Management-Software installiert ist.

#### SYS.1.5.A23 Rechte-Einschränkung der virtuellen Maschinen(CI)

Alle Schnittstellen und Kommunikationskanäle, die es einem virtuellen IT-System erlauben, Informationen über das Host-System auszulesen und abzufragen, SOLLTEN deaktiviert sein oder unterbunden werden. Weiterhin SOLLTE ausschließlich der Virtualisierungsserver auf seine Ressourcen zugreifen können. Außerdem SOLLTE es NICHT möglich sein, dass sich virtuelle IT-Systeme sogenannte *Pages* des Arbeitsspeichers teilen.

#### SYS.1.5.A24 Deaktivierung von Snapshots virtueller IT-Systeme(CIA)

Für alle virtuellen IT-Systeme SOLLTE die Snapshot-Funktion deaktiviert werden.

#### SYS.1.5.A25 Minimale Nutzung von Konsolenzugriffen auf virtuelle IT-Systeme(A)

Direkte Zugriffe auf die emulierten Konsolen virtueller IT-Systeme SOLLTEN auf ein Mindestmaß reduziert werden. Die virtuellen Systeme SOLLTEN möglichst über das Netz gesteuert werden.

#### SYS.1.5.A26 Einsatz einer PKI [Leiter IT, Leiter Netze](CIA)

Da die Kommunikation zwischen den Komponenten der IT-Infrastruktur häufig mithilfe von Zertifikaten abgesichert wird, SOLLTE eine Public-Key-Infrastruktur (PKI) eingesetzt werden. 

#### SYS.1.5.A27 Einsatz zertifizierter Virtualisierungssoftware [Leiter IT](CIA)

Es SOLLTE zertifizierte Virtualisierungssoftware der Stufe EAL 4 oder höher eingesetzt werden.

#### SYS.1.5.A28 Verschlüsselung von virtuellen IT-Systemen(CI)

Alle virtuellen IT-Systeme SOLLTEN verschlüsselt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Virtualisierung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [CSE113] CSE-113: Server-Virtualisierung

  

 CSE-113:Server-Virtualisierung, BSI-Veröffentlichung zur Cyber-Sicherheit, 03.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_113.htm](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_113.htm)

 
* #### [ISFSY13] Information Security Forum (ISF)

  

 insbesondere Area SY1.3 - Virtual Servers, 06.2016

 
* #### [NIST800125] NIST Special Publication (SP) 800-125, Guide to Security for Full Virtualization Technologies, 01.2011

  

 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-125.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Virtualisierung" von Bedeutung.

* G 0.15 Abhören
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
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

