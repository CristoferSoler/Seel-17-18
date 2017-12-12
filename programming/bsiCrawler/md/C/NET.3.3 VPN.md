1 Beschreibung
--------------

### 1.1 Einleitung

Mithilfe von Virtuellen Privaten Netzen (VPNs) können Sicherheitsmaßnahmen realisiert werden, um schutzbedürftige Daten über nicht-vertrauenswürdige Netze wie das Internet zu übertragen. Ein VPN ist ein Netz, das physisch innerhalb eines anderen Netzes, wie beispielsweise des Internets, betrieben wird, jedoch logisch von diesem Netz getrennt ist. VPNs können mithilfe kryptografischer Verfahren die Integrität und Vertraulichkeit von Daten schützen. Die sichere Authentisierung der Kommunikationspartner ist auch dann möglich, wenn mehrere Netze oder Rechner über gemietete Leitungen oder öffentliche Netze miteinander verbunden sind.

### 1.2 Zielsetzung

Der Baustein definiert Anforderungen, mit denen sich ein VPN zielgerichtet und sicher planen, umsetzen und betreiben lässt. 

### 1.3 Abgrenzung

Ein VPN im Sinne dieses Bausteins ist ein Netz, das physisch innerhalb eines anderen Netzes betrieben wird, jedoch logisch von diesem Netz getrennt ist. Der Baustein VPN geht nicht auf Grundlagen für sichere Netze ein (siehe dazu NET.1.1 *Netzarchitektur und -design*). Auch deckt er nicht alle mit dem Betrieb eines VPNs zusammenhängenden Prozesse ab. So müssen zusätzlich vor allem die Bausteine OPS.1.1.3 *Patch- und Änderungsmanagement*, ORP.3 *Sensibilisierung und Schulung zur Informationssicherheit*, CON.1 *Kryptokonzept*, OPS.1.1.5 *Datensicherung*, DER.4 *Notfallmanagement* und OPS.2.4 *Fernwartun*g beachtet werden.

Der vorliegende Baustein muss für jede Art von Fernzugriffen auf den Informationsverbund angewendet werden. Hierzu gehören Verbindungen über Datennetze, wie zum Beispiel Site-to-Site-, End-to-End- oder Remote-Access-VPNs, und über Telekommunikationsverbindungen, wie beispielsweise über analoge Wählleitungen, ISDN- oder Mobiltelefone. Es werden in diesem Baustein nur VPN-Systeme für die Schichten 2 (Sicherungsschicht) bis 4 (Transportschicht) des Open-Systems-Interconnection-(OSI)-Modells abgedeckt.

Empfehlungen, wie die Betriebssysteme der VPN-Endpunkte konfiguriert werden können, sind ebenfalls nicht Bestandteil dieses Bausteins. Entsprechende Anforderungen sind im Baustein SYS.1.1 *Allgemeiner Server *beziehungsweise SYS.2.1* Allgemeiner Client* sowie den jeweiligen betriebssystemspezifischen Bausteinen des IT-Grundschutz-Kompendiums zu finden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich VPN von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichende Planung und Reglementierung des VPN-Einsatzes

Bei einem nicht sorgfältig geplanten, aufgebauten oder konfigurierten VPN können Sicherheitslücken entstehen, die alle mit dem VPN vernetzten IT-Systeme beeinträchtigen. Angreifern kann es so möglich sein, auf vertrauliche Informationen der Institution zuzugreifen. 

So ist es durch eine unzureichende VPN-Planung und Reglementierung beispielsweise möglich, dass die Benutzer nicht ordnungsgemäß geschult wurden und dadurch das VPN in einer unsicheren Umgebung benutzen oder sich von einem unsicheren Client aus einwählen. Dies ermöglicht es Angreifern eventuell, auf das gesamte Firmennetz zuzugreifen. 

Auch wenn die regelmäßige Kontrolle der Zugriffe auf das VPN unzureichend geplant wurde, könnten Angriffe nicht rechtzeitig erkannt werden. Somit kann nicht zeitnah reagiert werden und ein Angreifer kann unbemerkt Daten stehlen oder ganze Prozesse sabotieren.

### 2 2 Unsichere VPN-Dienstleister

VPN-Verbindungen können bis in kritische Bereiche des Netzes hineinreichen. Greift die Institution auf einen VPN-Dienstleister zurück und hat sie diesen nicht sorgfältig ausgewählt, könnte hierdurch das gesamte Netz der Institution unsicher werden. So könnte beispielsweise ein vom Dienstleister unsicher angebotener VPN-Zugang von Angreifern benutzt werden, um gezielt Informationen zu stehlen. 

### 2 3 Probleme bei der lokalen Speicherung der Authentisierungsdaten für VPNs

Viele VPN-Clients für den Fernzugriff erlauben es, die zur Authentisierung notwendigen Daten lokal zu speichern, sodass sie der Benutzer beim erneuten Verbindungsaufbau nicht noch einmal eingeben muss. Wenn es einem Angreifer gelingt, auf den VPN-Client zuzugreifen, kann er eventuell so die Zugangsdaten auslesen und sich als legitimer Benutzer am Netz anmelden. Somit kann er auf die lokalen Netze und die darin erreichbaren Informationen und Dienste der Institution zugreifen.

### 2 4 Unsichere Konfiguration der VPN-Clients für den Fernzugriff

Wird ein VPN-Client nicht sicher konfiguriert, könnten die Benutzer dessen Sicherheitsmechanismen falsch oder gar nicht benutzen. Auch verändern sie eventuell die Konfiguration des Clients. Ebenso ist es durch eine unsichere Konfiguration möglich, dass vom Benutzer installierte Software auch die Sicherheit des VPN-Clients gefährdet. 

### 2 5 Unsichere Standard-Einstellungen auf VPN-Komponenten

Die Standard-Einstellungen von VPN-Komponenten weisen nicht immer alle Merkmale einer sicheren Installation auf. Oft wird mehr auf Benutzerfreundlichkeit und problemlose Integration in bestehende Systeme als auf Sicherheit geachtet. Wenn VPN-Komponenten nicht oder nur mangelhaft an die konkreten Sicherheitsbedürfnisse der Institution angepasst werden, können daher Schwachstellen und somit gefährliche Angriffspunkte entstehen. So ist beispielsweise das gesamte VPN und damit das interne Netz der Institution angreifbar, wenn vom Hersteller voreingestellte Passwörter nicht geändert werden.

### 2 6 Diebstahl von mobilen Endgeräten mit VPN-Client

Mobile Endgeräte werden öfter gestohlen oder gehen anderweitig verloren. Dadurch besteht die Gefahr, dass Angreifer über die dort eingerichtete VPN-Verbindung auf das interne Netz der Institution zugreifen können. Oftmals fehlen auch Verlustmeldeprozesse, sodass z. B. ein gestohlener Laptop nicht zeitnah der richtigen Stelle in der Institution gemeldet wird. Dadurch kann sich der Angreifer möglicherweise lange unbemerkt im internen Netz aufhalten und zahlreiche schützenswerte Informationen kopieren.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich VPN aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.3.3.A1 Planung des VPN-Einsatzes

Vor der Einführung eines VPNs MUSS eine sorgfältige Planung erfolgen. Dabei MÜSSEN die Verantwortlichkeiten für den VPN-Betrieb festgelegt werden. Es MÜSSEN zudem für das VPN Benutzergruppen und deren Berechtigungen geplant werden. Ebenso MUSS definiert werden, wie erteilte, geänderte oder entzogene Zugriffsberechtigungen zu dokumentieren sind.

#### NET.3.3.A2 Auswahl eines VPN-Dienstleisters [Informationssicherheitsbeauftragter (ISB)]

Mit einem VPN-Dienstleister MÜSSEN Service Level Agreements (SLAs) ausgehandelt und schriftlich dokumentiert werden. Es MUSS regelmäßig kontrolliert werden, ob der VPN-Dienstleister die vereinbaren SLAs einhält.

#### NET.3.3.A3 Sichere Installation von VPN-Endgeräten

Das zugrundeliegende Betriebssystem der VPN-Plattform MUSS sicher konfiguriert werden. Wird eine Appliance benutzt, MUSS es dafür einen gültigen Wartungsvertrag geben. Es MUSS sichergestellt werden, dass nur qualifiziertes Personal VPN-Komponenten installiert. Die Installation der VPN-Komponenten sowie eventuelle Abweichungen von den Planungsvorgaben SOLLTEN dokumentiert werden. Die Funktionalität und die gewählten Sicherheitsmechanismen des VPN MÜSSEN vor Inbetriebnahme geprüft werden.

#### NET.3.3.A4 Sichere Konfiguration eines VPNs

Für VPN-Clients, VPN-Server und VPN-Verbindungen MUSS eine sichere Konfiguration festgelegt werden. Diese SOLLTE geeignet dokumentiert werden. Auch MUSS der zuständige Administrator regelmäßig kontrollieren, ob die Konfiguration noch sicher ist und sie eventuell für alle IT-Systeme anpassen. 

#### NET.3.3.A5 Sperrung nicht mehr benötigter VPN-Zugänge

Es MUSS regelmäßig geprüft werden, ob ausschließlich berechtigte IT-Systeme und Benutzer auf das VPN zugreifen können. Nicht mehr benötigte VPN-Zugänge MÜSSEN zeitnah deaktiviert werden. Der VPN-Zugriff MUSS auf die benötigten Benutzungszeiten beschränkt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich VPN. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.3.3.A6 Durchführung einer VPN-Anforderungsanalyse

Es SOLLTE eine Anforderungsanalyse durchgeführt werden, um für das jeweilige VPN die Einsatzszenarien zu bestimmen und daraus Anforderungen an die benötigte Hard- und Software-Komponenten ableiten zu können. In der Anforderungsanalyse SOLLTEN folgende Punkte betrachtet werden: 

* Geschäftsprozesse,
* Zugriffswege, 
* Identifikations- und Authentisierungsverfahren, 
* Benutzer und Benutzerberechtigungen,
* Zuständigkeiten und 
* Meldewege.
#### NET.3.3.A7 Planung der technischen VPN-Realisierung

Neben der allgemeinen Planung (siehe NET.3.3.A1 *Planung des VPN-Einsatzes*) SOLLTEN die technischen Aspekte eines VPNs sorgfältig geplant werden. So SOLLTEN für das VPN die Verschlüsselungsverfahren, VPN-Endpunkte, erlaubten Zugangsprotokolle, Dienste und Ressourcen festgelegt werden. Zudem SOLLTEN die Teilnetze (siehe NET.1.1 *Netzarchitektur und -design*) definiert werden, die über das VPN erreichbar sind.

#### NET.3.3.A8 Erstellung einer Sicherheitsrichtlinie zur VPN-Nutzung

Es SOLLTE eine Sicherheitsrichtlinie zur VPN-Nutzung erstellt und den Mitarbeitern bekannt gegeben werden. Die Sicherheitsmaßnahmen SOLLTEN im Rahmen von Schulungen erläutert werden. Wird einem Mitarbeiter ein VPN-Zugang eingerichtet, SOLLTE ihm ein Merkblatt mit den wichtigsten VPN-Sicherheitsmechanismen ausgehändigt werden. Alle VPN-Benutzer SOLLTEN verpflichtet werden, die Sicherheitsrichtlinien einzuhalten. 

#### NET.3.3.A9 Geeignete Auswahl von VPN-Produkten

Bei der Auswahl von VPN-Produkten SOLLTEN die Anforderungen der Institutionen an die Vernetzung unterschiedlicher Standorte und die Anbindung mobiler Mitarbeiter oder Telearbeiter berücksichtigt werden.

#### NET.3.3.A10 Sicherer Betrieb eines VPNs

Für VPNs SOLLTE ein Betriebskonzept erstellt werden. Darin SOLLTEN die Aspekte Qualitätsmanagement, Überwachung, Wartung, Schulung und Autorisierung beachtet werden. 

#### NET.3.3.A11 Sichere Anbindung eines externen Netzes

Wird ein VPN benutzt, um ein externes Netz anzubinden, SOLLTEN dabei nach dem derzeitigen Stand der Technik sicherere Authentisierungs- und Verschlüsselungsverfahren mit ausreichender Schlüssellänge verwendet werden. Auch das gewählte Verfahren zum Schlüsselaustausch SOLLTE dem Stand der Technik entsprechen. Es SOLLTE sichergestellt werden, dass VPN-Verbindungen nur zwischen den hierfür vorgesehenen IT-Systemen und Diensten aufgebaut werden. Die dabei eingesetzten Tunnel-Protokolle SOLLTEN für den Einsatz geeignet sein.

#### NET.3.3.A12 Benutzer- und Zugriffsverwaltung bei Fernzugriff-VPNs

Für Fernzugriff-VPNs SOLLTE eine zentrale und konsistente Benutzer- und Zugriffsverwaltung gewährleistet werden. Die genutzten Authentisierungsverfahren SOLLTEN die Anforderungen des Bausteins ORP.4 *Identitäts- und Berechtigungsmanagement* erfüllen. 

Werden eigenständige Server für die Benutzer- und Zugriffsverwaltung genutzt, SOLLTE sichergestellt sein, dass diese sicher und konsistent zu den Anforderungen des Bausteins ORP.4 *Identitäts- und Berechtigungsmanagement* eingerichtet und betrieben werden. Weiterhin SOLLTEN die eingesetzten Server vor unbefugten Zugriffen geschützt sein.

#### NET.3.3.A13 Integration von VPN-Komponenten in eine Firewall

Die VPN-Komponenten SOLLTEN in die Firewall integriert werden, damit der Datenverkehr wirksam kontrolliert und gefiltert werden kann. Es SOLLTE dokumentiert werden, wie die VPN-Komponenten in die Firewall integriert sind.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "VPN" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27033-5] ISO/IEC 27033-5:2013

  

 Information technology - Security techniques - Network Security - Part 5: Securing communications across networks using Virtual Private Networks (VPNs), ISO, 08.2013   
 <https://www.iso.org/standard/51584.html>

 
* #### [ISIVPN] Virtuelles Privates Netz (ISi-VPN)

  

 BSI-Leitlinie zur Internet Sicherheit (ISi-L), BSI, 2009  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi\_vpn\_leitlinie\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/isi_vpn_leitlinie_pdf.pdf)

 
* #### [NIST80077] NIST Special Publication 800-77

  

 Guide to IPsec VPNs, NIST, 12.2005  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-77.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "VPN" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.32 Missbrauch von Berechtigungen
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

