1 Beschreibung
--------------

### 1.1 Einleitung

Die meisten Institutionen benötigen heute für ihren Geschäftsbetrieb Rechnernetze über die z. B. Informationen und Daten ausgetauscht sowie verteilte Anwendungen realisiert werden. In solche Netze werden nicht nur herkömmliche Endgeräte, Partner-Institutionen und das Internet eingebunden, sondern sie integrieren zunehmend auch mobile Endgeräte und Elemente, die dem Internet of Things (IoT) zugerechnet werden. Darüber hinaus werden über Rechnernetze vermehrt auch Cloud-Dienste sowie Dienste für Unified Communication and Collaboration (UCC) genutzt. Die Vorteile, die sich dadurch ergeben, sind unbestritten. Aber durch die vielen Endgeräte und Dienste steigen jedoch auch die Risiken. Deshalb ist es wichtig, das eigene Netz bereits durch eine sichere Netzarchitektur zu schützen. Hierfür muss zum Beispiel geplant werden, wie ein lokales Netz (Local Area Network, LAN) oder ein Wide Area Network (WAN) sicher aufgebaut werden kann. Ebenso müssen nur eingeschränkt vertrauenswürdige externe Netze, z. B. das Internet oder Kunden-Netze, geeignet angebunden werden. 

Um ein hohes Sicherheitsniveau zu gewährleisten, sind zusätzliche sicherheitsrelevante Aspekte zu berücksichtigen: So sollten z. B. verschiedene Mandanten und Gerätegruppen sicher auf Ebene des Netzes getrennt und ihre Kommunikation durch Firewall-Techniken kontrolliert werden. Ein weiteres wichtiges Sicherheitselement speziell im Client-Bereich ist außerdem die Netzzugangskontrolle (siehe NET.1.3 *Network Access Control*). 

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, die Informationssicherheit als integralen Bestandteil der Netzarchitektur und des Netzdesigns zu etablieren.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die es zu beachten und erfüllen gilt, wenn Netze geplant, aufgebaut und betrieben werden. Anforderungen für den sicheren Betrieb der entsprechenden Netzkomponenten, inklusive Sicherheitskomponenten wie z. B. Firewalls und Intrusion Detection Systems / Intrusion Prevention Systems (IDS/IPS), sind nicht Gegenstand des vorliegenden Bausteins. Diese werden in der Bausteingruppe NET.3 *Netzkomponenten* behandelt.

Der Fokus dieses Bausteins liegt auf kabelgebundenen Netzen und auf Datenkommunikation. Jedoch müssen allgemeine Anforderungen an die Architektur und das Design, z. B. Sicherheitszonen und -segmente trennen, für alle Netztechniken beachtet und erfüllt werden. Weitergehende spezifische Anforderungen für Netzbereiche wie Wireless LAN (WLAN) oder Speichernetze (Storage Area Networks, SAN) werden in den Bausteingruppen NET.2 *Funknetze* bzw. im Baustein SYS.1.8 *Speichersysteme* behandelt. Darüber hinaus werden auch die Themen UCC und Voice over IP (VoIP) sowie die hierfür zugrunde liegende Sicherheitsinfrastruktur nicht in diesem Baustein erörtert, sondern in den entsprechenden Bausteinen NET.4.2 *VoIP* bzw. NET.4.5 *Unified Communications* behandelt.

Spezifische sicherheitstechnische Anforderungen für Virtual Private Clouds und Hybrid Clouds liegen nicht im Fokus dieses Bausteins (siehe dafür OPS.3.2 *Cloud-Anbieter* und OPS.3.4 *Managed Security Services*).

Das Netzmanagement wird im Rahmen der Zonierung und Segmentierung betrachtet, alle weitergehenden Themen des Netzmanagements werden im Baustein NET.1.2 *Netzmanagement* behandelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Netzarchitektur und -design von besonderer Bedeutung:

### 2 1 Ausfall oder unzureichende Performance von Kommunikationsverbindungen

Sind die Kommunikationsverbindungen unzureichend dimensioniert oder reicht ihre Leistung aufgrund von technischen Ausfällen oder aufgrund eines Denial-of-Service-(DoS)-Angriffs nicht mehr aus, können z. B. Clients nur noch eingeschränkt mit Servern kommunizieren. Dadurch erhöhen sich die Zugriffszeiten auf interne und externe Dienste (z. B. Cloud-Dienste), die so mitunter nur noch eingeschränkt oder gar nicht mehr nutzbar sind. Auch sind eventuelle geschäftsrelevante Informationen nicht mehr verfügbar. In der Folge kann es beispielsweise zu Produktionsausfällen kommen oder essenzielle Geschäftsprozesse fallen aus.

### 2 2 Ungenügend abgesicherte Netzzugänge

Ist das interne Netz mit dem Internet verbunden und der Übergang nicht ausreichend geschützt, z. B. weil keine Firewall eingesetzt wird oder sie falsch konfiguriert ist, können Angreifer auf schützenswerte Informationen der Institution zugreifen und diese kopieren oder manipulieren.

### 2 3 Unsachgemäßer Aufbau von Netzen

Wird ein Netz unsachgemäß aufgebaut oder fehlerhaft erweitert, können unsichere Netztopologien und Netzkonfigurationen entstehen. Angreifer können so leichter Sicherheitslücken finden, ins interne Netz der Institution eindringen und dort Informationen abziehen, Daten manipulieren oder auch ganze Produktionssysteme stören. Auch bleiben Angreifer in einem fehlerhaft aufgebauten Netz, das die Sicherheitssysteme nur eingeschränkt überwachen können, länger unerkannt.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Netzarchitektur und -design aufgeführt. Grundsätzlich ist der Leiter Netze für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.1.1.A1 Sicherheitsrichtlinie für das Netz [Leiter IT, Informationssicherheitsbeauftragter (ISB)]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie für das Netz erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie Netze sicher konzipiert und aufgebaut werden. In der Richtlinie MUSS unter anderem festgelegt werden:

* in welchen Fällen die Sicherheitszonen zu segmentieren sind und in welchen Fällen Benutzergruppen bzw. Mandanten logisch oder sogar physisch zu trennen sind,
* welche Kommunikationsbeziehungen und welche Netz- und Anwendungsprotokolle jeweils zugelassen werden,
* wie der Datenverkehr für Administration und Überwachung netztechnisch zu trennen ist,
* welche institutionsinterne, standortübergreifende Kommunikation (WAN, Funknetze) erlaubt und welche Verschlüsselung im WAN, LAN oder auf Funkstrecken erforderlich ist,
* welche institutionsübergreifende Kommunikation zugelassen ist.
Die Richtlinie MUSS allen im Bereich Netzdesign verantwortlichen Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies dokumentiert und mit dem verantwortlichen ISB abgestimmt werden. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.

#### NET.1.1.A2 Dokumentation des Netzes [IT-Betrieb]

Es MUSS eine vollständige Dokumentation des Netzes (inklusive Netzplan) erstellt und nachhaltig gepflegt werden. Darin MÜSSEN die initiale Ist-Aufnahme (einschließlich der Netzperformance) sowie alle durchgeführten Änderungen im Netz enthalten sein. Auch MUSS die logische Struktur des Netzes dokumentiert werden, insbesondere wie die Subnetze zugeordnet und wie das Netz zoniert und segmentiert wird.

#### NET.1.1.A3 Anforderungsspezifikation für das Netz

Ausgehend von der Sicherheitsrichtlinie (siehe NET.1.1.A1 *Sicherheitsrichtlinie für das Netz*) MUSS eine Anforderungsspezifikation für das Netz erstellt und nachhaltig gepflegt werden. Aus den Anforderungen MÜSSEN sich alle wesentlichen Elemente für Netzarchitektur und -design ableiten lassen.

#### NET.1.1.A4 Netztrennung in Sicherheitszonen

Das Gesamtnetz MUSS in mindestens folgende drei Sicherheitszonen physisch separiert sein: internes Netz, demilitarisierte Zone (DMZ) und Außenanbindungen (inklusive Internetanbindung sowie Anbindung an andere nicht vertrauenswürdige Netze). Zonenübergänge MÜSSEN durch eine Firewall abgesichert werden. Diese Kontrolle MUSS dem Prinzip der lokalen Kommunikation folgen, sodass von Firewalls ausschließlich erlaubte Kommunikation weitergeleitet wird (Whitelisting).

Nicht vertrauenswürdige Netze (z. B. Internet) und vertrauenswürdige Netze (z. B. Intranet) MÜSSEN durch eine zweistufige Firewall-Struktur, bestehend aus zustandsbehafteten Paketfiltern (Firewall), getrennt werden. Um Internet und externe DMZ netztechnisch zu trennen, MUSS mindestens ein zustandsbehafteter Paketfilter (Firewall) eingesetzt werden.

In der zweistufigen Firewall-Architektur MUSS jeder ein- und ausgehende Datenverkehr durch den äußeren Paketfilter (Firewall) bzw. den internen Paketfilter (Firewall) kontrolliert und gefiltert werden. 

Eine P-A-P-Struktur, die aus Paketfilter, Application-Layer-Gateway bzw. Sicherheits-Proxies und Paketfilter besteht, MUSS immer realisiert werden, wenn die Sicherheitsrichtlinie oder die Anforderungsspezifikation dies fordern.

#### NET.1.1.A5 Client-Server-Segmentierung

Clients und Server MÜSSEN in unterschiedlichen Sicherheitssegmenten platziert werden. Die Kommunikation zwischen diesen Segmenten MUSS mindestens durch einen zustandsbehafteten Paketfilter (Firewall) kontrolliert werden.

Es SOLLTE beachtet werden, dass etwaige Ausnahmen, die es erlauben, Clients und Server in einem gemeinsamen Sicherheitssegment zu positionieren in den entsprechenden anwendungs- und systemspezifischen Bausteinen geregelt werden.

Für Gastzugänge und für Netzbereiche, in denen keine ausreichende interne Kontrolle über die Endgeräte gegeben ist, MÜSSEN dedizierte Sicherheitssegmente eingerichtet werden.

#### NET.1.1.A6 Endgeräte-Segmentierung im internen Netz

Es DÜRFEN NUR Endgeräte in einem Sicherheitssegment positioniert werden, die einem ähnlichen Sicherheitsniveau entsprechen.

#### NET.1.1.A7 Absicherung von schützenswerten Informationen

Schützenswerte Informationen MÜSSEN über nach dem derzeitigen Stand der Technik sichere Protokolle übertragen werden, falls nicht über vertrauenswürdige dedizierte Netzsegmente (z. B. innerhalb des Managementnetzes) kommuniziert wird. Können solche Protokolle nicht genutzt werden, MUSS nach Stand der Technik angemessen verschlüsselt und authentisiert werden (siehe NET.3.3 *VPN).*

#### NET.1.1.A8 Grundlegende Absicherung des Internetzugangs

Der Internetzugang MUSS entsprechend NET.1.1.A4 *Netztrennung in Sicherheitszonen* gestaltet werden. Der Internetverkehr MUSS über die Firewall-Struktur geführt werden. Die Datenflüsse MÜSSEN durch die Firewall-Struktur auf die benötigten Protokolle und Kommunikationsbeziehungen eingeschränkt werden.

#### NET.1.1.A9 Grundlegende Absicherung der Kommunikation mit nicht vertrauenswürdigen Netzen

Für jedes Netz MUSS festgelegt werden, inwieweit es als vertrauenswürdig einzustufen ist. Netze, die überhaupt nicht vertrauenswürdig sind, MÜSSEN wie das Internet behandelt und entsprechend abgesichert werden.

#### NET.1.1.A10 DMZ-Segmentierung für Zugriffe aus dem Internet

Die Firewall-Strukur MUSS für alle Dienste bzw. Anwendungen, die aus dem Internet erreichbar sind, um eine sogenannte externe DMZ ergänzt werden. Es SOLLTE ein Konzept zur DMZ-Segmentierung erstellt werden, das die Sicherheitsrichtlinie und die Anforderungsspezifikation nachvollziehbar umsetzt. Abhängig vom Sicherheitsniveau der IT-Systeme MÜSSEN die DMZ-Segmente weitergehend unterteilt werden. Eine externe DMZ MUSS am äußeren Paketfilter angeschlossen werden.

#### NET.1.1.A11 Absicherung eingehender Kommunikation vom Internet in das interne Netz

Ein IP-basierter Zugriff auf das interne Netz MUSS über einen sicheren Kommunikationskanal erfolgen und auf vertrauenswürdige IT-Systeme und Benutzer beschränkt werden (siehe NET.3.3 *VPN*). Derartige VPN-Gateways SOLLTEN in einer externen DMZ realisiert werden. Es SOLLTE beachtet werden, dass hinreichend gehärtete VPN-Gateways direkt aus dem Internet erreichbar sein können. Die über das VPN-Gateway authentisierten Netzzugriffe ins interne Netz MÜSSEN mindestens die interne Firewall (zur Absicherung des internen Netzes) durchlaufen.

IT-Systeme DÜRFEN via Internet oder externer DMZ NICHT auf das interne Netz zugreifen. Es SOLLTE beachtet werden, dass etwaige Ausnahmen zu dieser Anforderung in den entsprechenden anwendungs- und systemspezifischen Bausteinen (z. B. APP.5.1 *E-Mail/Groupware*, NET.4.2 *VoIP)* geregelt werden.

#### NET.1.1.A12 Absicherung ausgehender interner Kommunikation zum Internet

Ausgehende Kommunikation aus dem internen Netz zum Internet MUSS an einem Sicherheits-Proxy entkoppelt werden. Die Entkoppelung MUSS außerhalb des internen Netzes erfolgen. Wird eine P-A-P-Struktur eingesetzt, SOLLTE die ausgehende Kommunikation immer durch die Sicherheits-Proxies der P-A-P Struktur entkoppelt werden.

#### NET.1.1.A13 Netzplanung

Jede Netzimplementierung MUSS geeignet, vollständig und nachvollziehbar geplant werden. Dabei MÜSSEN die Sicherheitsrichtlinie sowie die Anforderungsspezifikation beachtet werden. Darüber hinaus MÜSSEN in der Planung mindestens die folgenden Punkte bedarfsgerecht berücksichtigt werden:

* Anbindung von Internet und, sofern vorhanden, Standortnetz und Extranet,
* Topologie des Gesamtnetzes und der Netzbereiche, d. h. Sicherheitszonen und -segmente,
* Dimensionierung und Redundanz der Netz- und Sicherheitskomponenten, Übertragungsstrecken und Außenanbindungen,
* zu nutzende Protokolle und deren grundsätzliche Konfiguration und Adressierung, insbesondere IPv4/IPv6-Subnetze von Endgerätegruppen,
* Administration und Überwachung (siehe NET.1.2 *Netzmanagement*).
Die Netzplanung MUSS regelmäßig überprüft werden.

#### NET.1.1.A14 Umsetzung der Netzplanung

Das geplante Netz MUSS fachgerecht umgesetzt werden. Dies MUSS während der Abnahme geprüft werden.

#### NET.1.1.A15 Regelmäßiger Soll-Ist-Vergleich [Informationssicherheitsbeauftragter (ISB)]

Es MUSS regelmäßig geprüft werden, ob das bestehende Netz dem Soll-Zustand entspricht. Dabei MUSS mindestens geprüft werden, inwieweit es die Sicherheitsrichtlinie und Anforderungsspezifikation erfüllt und inwiefern die umgesetzte Netzstruktur dem aktuellen Stand der Netzplanung entspricht. Dafür MÜSSEN zuständige Personen sowie Prüfkriterien bzw. Vorgaben festgelegt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Netzarchitektur und -design. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.1.1.A16 Spezifikation der Netzarchitektur

Auf Basis der Sicherheitsrichtlinie und der Anforderungsspezifikation SOLLTE eine Architektur für die Sicherheitszonen inklusive internem Netz, DMZ-Bereich und Außenanbindungen entwickelt und nachhaltig gepflegt werden. Dabei SOLLTEN je nach spezifischer Situation der Institution alle relevanten Architekturelemente betrachtet werden, mindestens jedoch:

* Netzarchitektur des internen Netzes mit Festlegungen dazu, wie Netzvirtualisierungstechniken, Layer-2- und Layer-3-Kommunikation sowie Redundanzverfahren einzusetzen sind,
* Netzarchitektur für Außenanbindungen, inklusive Firewall-Architekturen, sowie DMZ- und Extranet-Design und Vorgaben an die Standortkopplung,
* Festlegung, an welchen Stellen des Netzes welche Sicherheitskomponenten wie Firewalls oder IDS/IPS zu platzieren sind und welche Sicherheitsfunktionen diese realisieren müssen,
* Vorgaben für die Netzanbindung der verschiedenen IT-Systeme,
* Netzarchitektur in Virtualisierungs-Hosts, wobei insbesondere Network Virtualization Overlay (NVO) und die Architektur in Vertikal integrierten Systemen (ViS) zu berücksichtigen sind,
* Festlegungen der grundsätzlichen Architektur-Elemente für eine Private Cloud sowie Absicherung der Anbindungen zu Virtual Private Cloud, Hybrid Cloud und Public Cloud (siehe OPS.3.2 *Cloud-Anbieter* und OPS.3.4 *Managed Security Services*),
* Architektur zur sicheren Administration und Überwachung der IT-Infrastruktur.
#### NET.1.1.A17 Spezifikation des Netzdesigns

Basierend auf der Netzarchitektur SOLLTE das Netzdesign für die Sicherheitszonen inklusive internem Netz, DMZ-Bereich und Außenanbindungen entwickelt und nachhaltig gepflegt werden. Dafür SOLLTEN die relevanten Architekturelemente detailliert werden, mindestens jedoch:

* zulässige Formen von Netzkomponenten inklusive virtualisierter Netzkomponenten,
* Festlegungen darüber, wie WAN- und Funkverbindungen abzusichern sind,
* Anbindung von Endgeräten an Switching-Komponenten, Verbindungen zwischen Netzelementen sowie Verwendung von Kommunikationsprotokollen,
* Redundanzmechanismen für alle Netzelemente,
* Adresskonzept für IPv4 und IPv6 sowie zugehörige Routing- und Switching-Konzepte,
* virtualisierte Netze in Virtualisierungs-Hosts inklusive NVO,
* Aufbau, Anbindung und Absicherung von Private Clouds sowie sichere Anbindung von Virtual Private Clouds, Hybrid Clouds und Public Clouds,
* Festlegungen zum Netzdesign für die sichere Administration und Überwachung der IT-Infrastruktur.
#### NET.1.1.A18 P-A-P-Struktur für die Internet-Anbindung

Zwischen den beiden Firewall-Stufen (siehe NET.1.1.A4 *Netztrennung in Sicherheitszonen*) MUSS ein proxy-basiertes Application-Layer-Gateways (ALG) bzw. MÜSSEN entsprechende Sicherheits-Proxies realisiert werden. Diese MÜSSEN jeweils über ein Transfernetz (dual-homed) zur äußeren Firewall und zur internen Firewall angebunden werden. In diesen Transfernetzen DARF NUR das proxy-basierte ALG bzw. DÜRFEN NUR entsprechende Sicherheits-Proxies integriert werden. Jeglicher Datenverkehr MUSS über das ALG bzw. entsprechende Sicherheits-Proxies entkoppelt werden. Ein Transportnetz, das beide Firewall-Stufen direkt miteinander verbindet, DARF NICHT konfiguriert werden. Die interne Firewall MUSS zudem die Angriffsfläche des ALGs bzw. der Sicherheits-Proxies gegenüber Innentätern oder IT-Systemen im internen Netz reduzieren. 

Authentisierte und vertrauenswürdige Netzzugriffe, ausgehend von dem VPN-Gateway ins interne Netz, SOLLTEN NICHT das ALG bzw. die Sicherheits-Proxies der P-A-P-Struktur durchlaufen.

#### NET.1.1.A19 Separierung der Infrastrukturdienste

Server, die grundlegende Dienste für die IT-Infrastruktur bereitstellen, SOLLTEN in einem dedizierten Sicherheitssegment positioniert werden. Die Kommunikation mit ihnen SOLLTE durch einen zustandsbehafteten Paketfilter (Firewall) kontrolliert werden. 

#### NET.1.1.A20 Zuweisung dedizierter Subnetze für IPv4/IPv6-Endgerätegruppen

Unterschiedliche IPv4-/IPv6- Endgeräte SOLLTEN je nach verwendeten Protokoll (IPv4-/IPv6- oder IPv4/IPv6-DualStack) dedizierten Subnetzen zugeordnet werden.

#### NET.1.1.A21 Separierung des Management-Bereichs

Es SOLLTE durchgängig ein Out-of-Band-Management genutzt werden, um die Infrastruktur zu managen. Dabei SOLLTEN alle Endgeräte, die für das Management der IT-Infrastruktur benötigt werden, in dedizierten Segmenten positioniert werden. Die Kommunikation mit diesen Endgeräten SOLLTE durch einen zustandsbehafteten Paketfilter (Firewall) kontrolliert werden. Die Kommunikation von und zu diesen Management-Segmenten SOLLTE auf die notwendigen Management-Protokolle mit definierten Kommunikations-Endpunkten beschränkt werden.

Der Management-Bereich SOLLTE mindestens die folgenden Sicherheitssegmente umfassen, die abhängig von der Sicherheitsrichtlinie und der Anforderungsspezifikation weiter unterteilt werden SOLLTEN:

* Segment(e) für IT-Systeme, die für die Authentisierung und Autorisierung der administrativen Kommunikation zuständig sind,
* Segment(e) für die Administration der IT-Systeme,
* Segment(e) für die Überwachung und das Monitoring,
* Segment(e), die die zentrale Protokollierung inklusive Syslog-Server und SIEM-Server enthalten,
* Segment(e) für IT-Systeme, die für grundlegende Dienste des Management-Bereichs benötigt werden,
* Segment(e) für die Management-Interface der zu administrierenden IT-Systeme.
Die verschiedenen Management-Interface der IT-Systeme MÜSSEN nach ihrem Einsatzzweck und ihrer Netzplatzierung über einen zustandsbehafteten Paketfilter (Firewall) getrennt werden. Dabei SOLLTEN die IT-Systeme (Management-Interface) zusätzlich folgender Zugehörigkeit über dedizierte Firewalls getrennt werden:

* IT-Systeme, die aus dem Internet erreichbar sind, 
* IT-Systeme im internen Netz,
* Sicherheitskomponenten, die sich zwischen den aus dem Internet erreichbaren IT-Systemen und dem internen Netz befinden.
Es MUSS sichergestellt werden, dass die Segmentierung nicht durch die Management-Kommunikation unterlaufen werden kann, d. h. eine Überbrückung von Segmenten MUSS ausgeschlossen werden.

#### NET.1.1.A22 Spezifikation des Segmentierungskonzepts

Auf Basis der Spezifikationen von Netzarchitektur und Netzdesign SOLLTE ein umfassendes Segmentierungskonzept für das interne Netz, inklusive eventuell vorhandener virtualisierter Netze in Virtualisierungs-Hosts, geplant, umgesetzt, betrieben und nachhaltig gepflegt werden. Das Konzept SOLLTE mindestens die folgenden Punkte umfassen, soweit diese in der Zielumgebung vorgesehen sind:

* Initial anzulegende Sicherheitssegmente und Vorgaben dazu, wie neue Sicherheitssegmente zu schaffen sind und wie Endgeräte in den Sicherheitssegmenten zu positionieren sind.
* Festlegung für die Segmentierung von Entwicklungs- und Testsystemen (Staging)
* Netzzugangskontrolle für Sicherheitssegmente mit Clients
* Anbindung von Netzbereichen, die über Funktechniken oder Standleitung an die Sicherheitssegmente angebunden sind
* Anbindung der Virtualisierungs-Hosts und von virtuellen Maschinen auf den Hosts an die Sicherheitssegmente
* Rechenzentrumsautomatisierung
* Festlegungen dazu, wie Endgeräte einzubinden sind, die mehrere Sicherheitssegmente versorgen, z. B. Load Balancer, und Speicher- sowie Datensicherungslösungen
Abhängig von der Sicherheitsrichtlinie und der Anforderungsspezifikation SOLLTE für jedes Sicherheitssegment konzipiert werden, wie es netztechnisch realisiert werden soll. Darüber hinaus SOLLTE festgelegt werden, welche Sicherheitsfunktionen die Koppelelemente zwischen den Sicherheitssegmenten bereitstellen müssen (z. B. Firewall als zustandsbehafteter Paketfilter oder IDS/IPS).

#### NET.1.1.A23 Trennung von Sicherheitssegmenten

IT-Systeme mit unterschiedlichem Schutzbedarf SOLLTEN in verschiedenen Sicherheitssegmenten platziert werden. Ist dies nicht möglich, richtet sich der Schutzbedarf nach dem höchsten vorkommenden Schutzbedarf im Sicherheitssegment. Darüber hinaus SOLLTEN die Sicherheitssegmente abhängig von ihrer Größe und den Anforderungen des Segmentierungskonzepts weiter unterteilt werden. Es MUSS sichergestellt werden, dass keine Überbrückung von Segmenten oder gar Zonen möglich ist.

Gehören die VLANs an einem Switch unterschiedlichen Institutionen an, SOLLTE die Trennung entweder physisch erfolgen oder es SOLLTE Verschlüsselung eingesetzt werden, um die übertragenen Informationen vor unbefugtem Zugriff zu schützen.

#### NET.1.1.A24 Sichere logische Trennung mittels VLAN

Durch ein Virtual LAN (VLAN) DARF KEINE Verbindung zwischen einer Zone vor dem ALG bzw. den Sicherheits-Proxies einer P-A-P-Struktur und dem dahinter liegenden internen Netz geschaffen werden. 

Generell MUSS sichergestellt werden, dass keine Überbrückung von Zonen möglich ist, wenn VLANs eingesetzt werden.

#### NET.1.1.A25 Fein- und Umsetzungsplanung von Netzarchitektur und -design

Eine Fein- und Umsetzungsplanung für die Netzarchitektur und das Netzdesign SOLLTE durchgeführt, dokumentiert, geprüft und nachhaltig gepflegt werden.

#### NET.1.1.A26 Spezifikation von Betriebsprozessen für das Netz

Für einen sicheren und effektiven Netzbetrieb SOLLTEN Betriebsprozesse bedarfsgerecht erzeugt oder angepasst und dokumentiert werden (siehe Bausteingruppe Kern-IT-Betrieb, insbesondere OPS.1.1.3 *Patch- und Änderungsmanagement*). Dabei SOLLTE insbesondere berücksichtigt werden, wie sich die Zonierung sowie das Segmentierungskonzept auf den IT-Betrieb auswirken.

#### NET.1.1.A27 Einbindung der Netzarchitektur in die Notfallplanung [Leiter IT]

Initial und in regelmäßigen Abständen SOLLTE nachvollziehbar analysiert werden, wie sich die Netzarchitektur und die abgeleiteten Konzepte auf die Notfallplanung auswirken.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.1.1.A28 Hochverfügbare Netz- und Sicherheitskomponenten(A)

Zentrale Bereiche des internen Netzes sowie die Sicherheitskomponenten SOLLTEN hochverfügbar realisiert werden. Hierzu SOLLTEN die Komponenten redundant ausgelegt und auch intern hochverfügbar realisiert werden.

#### NET.1.1.A29 Hochverfügbare Realisierung von Netzanbindungen(A)

Die Netzanbindungen (z. B. Internet-Anbindung und WAN-Verbindungen) SOLLTEN vollständig redundant gestaltet werden. Je nach Verfügbarkeitsanforderung SOLLTEN redundante Anbindungen an einen oder verschiedene Anbieter, bedarfsabhängig mit unterschiedlicher Technik und Performance, bedarfsgerecht umgesetzt werden. Auch SOLLTE Wegeredundanz innerhalb und außerhalb der eigenen Zuständigkeit bedarfsgerecht umgesetzt werden. Hierbei SOLLTEN mögliche Single Points of Failures (SPoF) und störende Umgebungsbedingungen berücksichtigt werden.

#### NET.1.1.A30 Schutz vor Distributed-Denial-of-Service(A)

Um DDoS-Angriffe abzuwehren, SOLLTE per Bandbreitenmanagement die verfügbare Bandbreite gezielt zwischen verschiedenen Kommunikationspartnern und Protokollen aufgeteilt werden.

Um DDoS-Angriffe mit sehr hohen Datenraten abwehren zu können, SOLLTEN Mitigation-Dienste über größere Internet Service Provider (ISPs) eingekauft und deren Nutzung SOLLTE in Verträgen geregelt werden. 

#### NET.1.1.A31 Physische Trennung von Sicherheitssegmenten(CIA)

Abhängig von Sicherheitsrichtlinie und Anforderungsspezifikation SOLLTEN Sicherheitssegmente physisch durch separate Switches getrennt werden.

#### NET.1.1.A32 Physische Trennung von Management-Segmenten(CIA)

Abhängig von Sicherheitsrichtlinie und Anforderungsspezifikation SOLLTEN Sicherheitssegmente des Management-Bereichs physisch voneinander getrennt werden.

#### NET.1.1.A33 Mikrosegmentierung des Netzes(CIA)

Um potenzielle Angriffe auf eine geringe Zahl von Endgeräten zu beschränken, SOLLTE das Netz in kleine Segmente mit sehr ähnlichem Anforderungsprofil und selbem Schutzbedarf unterteilt werden. Insbesondere SOLLTE dies für die DMZ-Segmente berücksichtigt werden.

#### NET.1.1.A34 Einsatz kryptografischer Verfahren auf Netzebene(CI)

Die Sicherheitssegmente SOLLTEN im internen Netz, im Extranet und im DMZ-Bereich mittels kryptografischer Techniken bereits auf Netzebene realisiert werden. Dafür SOLLTEN VPN-Techniken oder IEEE 802.1AE eingesetzt werden.

Wenn innerhalb von internem Netz, Extranet oder DMZ über Verbindungsstrecken kommuniziert wird, die für einen erhöhten Schutzbedarf nicht ausreichend sicher sind, SOLLTE die Kommunikation angemessen auf Netzebene verschlüsselt werden.

#### NET.1.1.A35 Einsatz von netzbasiertem DLP [Informationssicherheitsbeauftragter (ISB)](CI)

Auf Netzebene SOLLTEN Systeme zur Data Loss Prevention (DLP) eingesetzt werden, um das Risiko von Datenabflüssen zu verringern.

#### NET.1.1.A36 Trennung mittels VLAN bei sehr hohem Schutzbedarf

Bei sehr hohem Schutzbedarf SOLLTEN KEINE VLANs eingesetzt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Netzarchitektur und -design" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27033-5] ISO/IEC 27033-5:2013

  

 Information technology - Security techniques - Network Security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs), ISO, 08.2013   
 <https://www.iso.org/standard/51584.html>

 
* #### [ISILANA] BSI-Standard zur Internet-Sicherheit (Isi-Reihe):

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [TL2103] BSI TL-02103 - Version 2.0 "Technische Leitlinie für organisationsinterne Telekommunikationssysteme mit erhöhtem Schutzbedarf"

  

 Bundesamt für Sicherheit in der Informationstechnik, 2014   
 [https://www.bsi.bund.de/DE/Publikationen/TL-sichere-TK-Anlagen/TL02103\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TL-sichere-TK-Anlagen/TL02103_htm.html)

 
* #### [TR21022] BSI Technische Richtlinie, Kryptografische Verfahren

  

 Verwendung von Transport Layer Security (TLS), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2017  
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Netzarchitektur und -design" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

