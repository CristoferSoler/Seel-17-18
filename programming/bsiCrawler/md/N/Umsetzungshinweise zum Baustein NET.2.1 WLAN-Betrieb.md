1 Beschreibung
--------------

### 1.1 Einleitung

WLANs können entsprechend den Bedürfnissen eines Betreibers und der Hardware-Ausstattung, die zur Verfügung steht, in zwei verschiedenen Modi betrieben werden. Im Ad-hoc-Modus kommunizieren zwei oder mehr mobile Endgeräte, die mit einer WLAN-Karte ausgestattet sind, direkt miteinander. Da sich WLANs im Ad-hoc-Modus selbstständig, ohne feste Infrastruktur aufbauen und konfigurieren können und somit eine vollvermaschte parallele Netz-Infrastruktur etablieren können, wird davon abgeraten, WLANs im Ad-hoc-Modus in einer zu schützenden Umgebung zu betreiben. Dieser wird im Folgenden nicht weiter betrachtet. In den vorliegenden Umsetzungshinweisen wird davon ausgegangen, dass alle Access Points (Zugangspunkte) zentral administriert und nicht im Ad-hoc-Modus betrieben werden. 

Für die Umsetzungshinweise wird auf die folgenden drei fiktiven Szenarien zurückgegriffen.

1. Szenario

* Die Informationen sind nicht als vertraulich klassifiziert.
* Access Points dürfen über eine Cloud-Infrastruktur administriert werden.
* Die Benutzer nutzen die zur Verfügung gestellte WLAN-Infrastruktur für die Telefonie.
2. Szenario

* Die Informationen sind teilweise als vertraulich klassifiziert.
* Access Points dürfen nicht über eine Cloud-Infrastruktur administriert werden.
* Die Benutzer nutzen die zur Verfügung gestellte WLAN-Infrastruktur für die Telefonie.
* Die Benutzer können über die WLAN-Infrastruktur außerdem auf interne Kollaborations- und Dokumentenmanagementsysteme zugreifen.
3. Szenario

* Die Informationen sind teilweise als streng vertraulich klassifiziert.
* Access Points dürfen nicht über eine Cloud-Infrastruktur administriert werden.
* Die Benutzer nutzen die zur Verfügung gestellte WLAN-Infrastruktur für die Telefonie.
* Die Benutzer können über die WLAN-Infrastruktur außerdem auf interne Kollaborations- und Dokumentenmanagementsysteme, Finanzdaten oder kritische Systeme der Institution zugreifen.
### 1.2 Lebenszyklus

**Planung und Konzeption**

Alle gewünschten Nutzungsszenarien und Funktionen sowie die damit einhergehenden regulatorischen Anforderungen sollten in der Planungs- und Konzeptionsphase in das Design der zukünftigen WLAN-Infrastruktur einfließen. Grundlage hierfür ist eine durchdachte WLAN-Strategie (siehe NET.2.1.M1 *Festlegung einer Strategie für den Einsatz von WLANs*). Die bestehenden Prozesse sollten darauf hin analysiert werden, ob sie mögliche Schnittstellen zu den Prozessen der zukünftigen WLAN-Infrastruktur aufweisen und bei Bedarf sollten sie aktualisiert werden. Zudem sollte geprüft werden, ob die Funktionen, die die WLAN-Infrastruktur mit sich bringt mit den geschäftlichen, sicherheitstechnischen und datenschutzrechtlichen Regelungen vereinbar sind.

Neben der Strategie sind die Auswahl des richtigen WLAN-Standards und den damit verbundenen Kryptoverfahren (siehe NET.2.1.M2 *Auswahl eines geeigneten WLAN-Standards* und NET.2.1.M3 *Auswahl geeigneter Kryptoverfahren für WLAN*) wichtige Themen, die bereits in der Planungsphase adressiert werden müssen.

Alle getroffenen Entscheidungen über Sicherheitseinstellungen, ausgewählte WLAN-Standards, sowie die Regelungen für die Administration des WLANs, sollten in einer WLAN-Sicherheitsrichtlinie niederzuschreiben (siehe NET.2.1.M10 *Erstellung einer Sicherheitsrichtlinie für den Betrieb von WLANs*). Wissenswertes zu WLANs ist unter "Wissenswertes" im Kapitel 3.1.1 *Einführung in WLAN-Grundbegriffe* zu finden. 

**Beschaffung**

Bei der Auswahl der WLAN-Komponenten ist die Maßnahme NET.2.1.M11 *Geeignete Auswahl von WLAN-Komponenten* anzuwenden. Da sich Standards, Protokolle und integrierte Sicherheitsmechanismen stetig fortentwickeln, unterliegen WLANs einem schnellen Wandel. Dies bedeutet, dass die WLAN-Infrastruktur an sich oder einzelne Komponenten häufiger migriert werden müssen. Für Migrationsphasen einzelner WLAN-Komponenten oder gar ganzer WLAN-Bereiche müssen notwendige WLAN-Migrationsschritte sorgfältig geplant und idealerweise in einem Proof of Concept (Machbarkeitsnachweis) vor der eigentlichen Migration verifiziert werden.

**Umsetzung**

Um die maximal möglichen Übertragungsraten zu erreichen, ist es nicht unerheblich, an welcher Stelle die Access Points im Raum positioniert sind (siehe NET.2.1.M4 *Geeignete Aufstellung von Access Points*). Die WLAN-Komponenten oder die WLAN-Managementlösung müssen bei der Installation stets gemäß den internen Sicherheitsrichtlinien konfiguriert werden (siehe NET.2.1.M5 *Sichere Basis-Konfiguration der Access Points* und NET.2.1.M6 *Sichere Konfiguration der WLAN-Clients*). Werden WLANs mit der eventuell bereits vorhandenen kabelgebundenen Infrastruktur verbunden, muss der Übergang zwischen WLANs und LAN entsprechend des höheren Schutzbedarfs abgesichert werden (siehe NET.2.1.M7 *Aufbau eines Distribution Systems* und NET.2.1.M9 *Sichere Anbindung von WLANs an ein LAN*).

Um Fehlkonfigurationen oder Fehlbedienungen zu vermeiden und auf mögliche Gefahren hinzuweisen, die entstehen können, wenn WLANs unsachgemäß betrieben werden, sind Verantwortliche ausreichend zu schulen und zu sensibilisieren. Weitere Informationen hierzu sind im Baustein ORP.3 *Sensibilisierung und Schulung zur Informationssicherheit* zu finden. 

**Betrieb**

Ist das WLAN in Betrieb genommen und wurden alle WLAN-Verantwortlichen ausreichend geschult, so ist durch regelmäßige Audits (siehe NET.2.1.M14 *Regelmäßige Audits der WLAN-Komponenten*) sicherzustellen, dass alle getroffenen Sicherheitseinstellungen stets aktuell sind und diese Einstellungen auch greifen. Unumgänglich ist ein Schlüsselmanagement für die eingesetzten kryptographischen Schlüssel, um die Kommunikation in WLANs abzusichern (siehe CON.1 *Kryptokonzept*). Wird eine WLAN-Managementlösung (siehe NET.2.1.M12 *Einsatz einer geeigneten WLAN-Management-Lösung*) eingesetzt, können die Schlüssel, Einstellungen sowie die WLAN-Komponenten selbst zentral von einer Stelle aus verwaltet werden.

**Aussonderung**

Werden WLAN-Komponenten außer Betrieb genommen, sind Konfigurationseinstellungen zu entfernen und wieder auf Standardwerte zurückzusetzen. Weitere Informationen hierzu sind im Baustein CON.6 *Löschen und Vernichten* zu finden.

**Notfallvorsorge**

Wurden Angriffe auf WLANs erkannt, so müssen die Verantwortlichen der WLANs wissen, wie sie sich zu verhalten haben (siehe NET.2.1.M8 *Verhaltensregeln bei WLAN-Sicherheitsvorfällen*). Hieraus ergibt sich ein Notfallplan, welche Schritte notwendig und welche Personen zu informieren sind, wenn ein Sicherheitsvorfall eintritt. 

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "WLAN-Betrieb" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### NET.2.1.M1 Festlegung einer Strategie für den Einsatz von WLANs [Leiter IT]

Wenn die folgenden Fragen beantwortet werden, kann hieraus die WLAN-Strategie in ihren Grundzügen hergeleitet werden.

* In welchen Bereichen (organisatorisch sowie räumlich) soll eine WLAN-Infrastruktur genutzt werden?
* Welche Potenziale erschließt die Nutzung einer WLAN-Infrastruktur? 

 
	+ Welche Aspekte der Mobilität werden durch WLANs ermöglicht?
	+ Welche Funktionen bzw. Anwendungen sollen durch die WLAN-Nutzung bereitgestellt bzw. unterstützt werden (z. B. Voice over WLAN, Media Broadcasting, Kollaboration, Videokonferenzen, Gastzugang/Hotspot, Einbindung von mobilen Endgeräten, Client-Netz-Segmentierung)?
	+ Welche Geschäftsprozesse lassen sich durch die Nutzung von WLANs optimieren?
	  

 
* Welches Sicherheitsrisiko entsteht dadurch, dass eine WLAN-Infrastruktur genutzt wird bzw. welches Risiko stellt der Verlust von Daten/Informationen über WLANs dar?
* Welche gesetzlichen Regelungen müssen eingehalten werden?
* Welche klassifizierten Daten/Informationen dürfen nicht ohne zusätzliche kryptographische Schutzmechanismen übertragen werden?
* Wer ist für den Betrieb der WLAN-Infrastruktur verantwortlich? 

 
	+ Wird die WLAN-Infrastruktur extern administriert?
	+ Darf die WLAN-Infrastruktur cloudbasiert administriert werden?
	  

 
* Welche Anforderungen werden an die Verfügbarkeit der WLAN-Infrastruktur gestellt?
#### NET.2.1.M2 Auswahl eines geeigneten WLAN-Standards [Planer]

Im Rahmen des WLAN-Designs, das den dokumentierten strategischen Anforderungen folgt, müssen potenziell störende Systeme in der Nähe des späteren Aufstellungsorts von Access Points ermittelt und evaluiert werden. Werden Mikrowellen in der Nähe von Access Points oder anderen IT-Systemen betrieben, können Störungen auftreten. Mögliche weitere Störquellen können Bluetooth-Sender, Hochspannungsleitungen, schnurlose Telefone (DECT) oder LCD-Monitore sowie das Baumaterial selbst sein.

Wenn die Anforderungen an die Beschaffung von Hard- und Software zusammengestellt werden, muss darauf geachtet werden, dass die Authentisierung nach dem Standard IEEE 802.11i-2004 oder neuer realisiert wird.

Um Brute-Force-Angriffe auf WLAN-Passwörter zu vermeiden, sollte die WLAN-Infrastruktur den Standard IEEE 802.11s unterstützen. Dieser Standard definiert mittels Simultaneous Authentication of Equals (SAE), dass das eigentliche Passwort nicht mehr über den Funkkanal übertragen wird. Hierdurch kann den bisher üblichen Angriffen durch Mitschneiden eines Verbindungsaufbaus mit anschließendem Brute-Force-Angriff auf das WLAN-Passwort effektiv begegnet werden. Der Standard IEEE 802.11ac definiert, wie Management-Frames mittels Protected Management Frames (PMF) gegen gefälschte Deassoziierungspakete eines Angreifers abzusichern sind. Um PMF effektiv nutzen zu können, muss jedoch auch das Endgerät den Standard IEEE 802.11ac unterstützen.

In Tabelle 1 sind diverse Authentisierungsmöglichkeiten für die drei fiktiven Szenarien abgebildet.

Tabelle : WLAN-Authentisierungsmethoden

Tabelle 2 gibt einen Überblick über die unterstützten IEEE-802.1X-EAP-Lösungen auf Basis der aufgeführten Endgeräte bzw. deren Betriebssysteme. Sie listet nicht alle Varianten auf und zeigt nicht die Wertigkeit der einzelnen Systeme. Es sollte EAP-TLS oder EAP-AKA anstelle von EAP-PEAP, EAP-TTLS oder EAP-SIM verwendet werden. Da EAP-PEAP und EAP-TTLS derzeit jedoch noch häufig eingesetzt werden, werden sie in der Tabelle dennoch aufgeführt.

Tabelle : WLAN-EAP-Authentisierungsvarianten je nach Art des Betriebssystems

Wenn EAP-TTLS verwendet wird, müssen kryptographisch abgesicherte Authentisierungsverfahren eingesetzt werden. Für die IEEE-802.1X-basierte Authentisierung von Smartphones und Tablets an der WLAN-Infrastruktur bietet sich zusätzlich EAP-SIM/EAP-AKA an.

#### NET.2.1.M3 Auswahl geeigneter Kryptoverfahren für WLAN [Planer]

Um WLANs sicher zu betreiben, muss die Kommunikation hierüber kryptographisch über Wi-Fi Protected Access 2 (WPA2) abgesichert sein. Leicht zu kompromittierende kryptographische Verfahren dürfen nicht mehr eingesetzt werden. Falls WEP oder WPA noch benutzt werden, sollte durch eine hierfür geplante Migration auf WPA2 aktualisiert werden.

Wird WPA2 mit Pre-Shared Keys (WPA2-PSK) verwendet, muss ein komplexer Schlüssel mit einer Mindestlänge von 20 Zeichen konfiguriert sein. Da der Schlüssel regelmäßig ausgetauscht werden muss, ist diese Methode nur für kleine WLAN-Installationen wirtschaftlich tragbar. Zudem muss bei WPA2-PSK darauf geachtet werden, dass die deutschen Umlaute und spezielle Steuerzeichen nicht eingesetzt werden können.

#### NET.2.1.M4 Geeignete Aufstellung von Access Points [Haustechnik]

Um Manipulationen an den Access Points vorzubeugen, müssen diese in stabilen Gehäusen untergebracht sein, die im Inneren eines Gebäudes an der Wand montiert werden können. Zusätzlich kann ein Access Point gegen zu einfachen Diebstahl z. B. durch ein Kensington Lock am Gehäuse selbst abgesichert werden. Aus WLAN-versorgungstechnischen Gründen sollten Access Points nicht in Zwischendecken oder abgehängten Decken untergebracht werden, wenn keine externen Antennen genutzt werden. Dies gilt auch für die Anbringung von Metallkäfigen zum Schutz von Access Points, da auch sie die Übertragungsqualität und den Durchsatz eines WLANs essentiell beeinflussen, insbesondere wenn Beamforming-Technik entsprechend dem Standard IEEE 802.11ac eingesetzt wird.

Die optimalen Aufstellungsorte der Access Points sollten durch eine Ausleuchtungsmessung ermittelt werden. 

Werden Außenbereiche versorgt, müssen Außeninstallationen (Antennen und gegebenenfalls Access Points) vor Witterungseinflüssen, elektrischen Entladungen und unberechtigtem Zugriff geeignet geschützt werden. Außerhalb von Gebäuden sollten Access Points möglichst nicht angebracht werden.

#### NET.2.1.M5 Sichere Basis-Konfiguration der Access Points

Voreingestellte SSIDs, Zugangskennwörter oder kryptographische Schlüssel müssen direkt nach Inbetriebnahme geändert werden, um den späteren sicheren Betrieb nicht zu gefährden. Die Access Points dürfen nicht im Auslieferungszustand produktiv in Betrieb genommen werden. Beispielsweise sollte der Name des Service Set Identifiers (SSID) keine Rückschlüsse auf die Hardware, die Institution, eventuelle Dienstleister und den Einsatzzweck ermöglichen. 

Durch die Verantwortlichen muss regelmäßig überprüft werden, ob alle sicherheitsrelevanten Updates und Patches für die etablierte WLAN-Infrastruktur eingespielt sind. Damit Empfänger und Sender optimal und sicher zusammenspielen, ist dies auch für die zugehörigen WLAN-Gerätetreiber auf den WLAN-Clients zu berücksichtigen. Eine neue Software-Version oder ein Patch sollten erst nach einem angemessenen Test eingespielt werden. Die spezifizierten Melde- und Informationsprozeduren im Änderungsmanagement sollen beschreiben, wer und wie bei derartigen Änderungen zu informieren ist. Ebenso ist die Dokumentation der WLAN-Infrastruktur anzupassen.

Im Folgenden wird aufgezeigt, mit welchen Einstellungsempfehlungen die WLAN-Infrastruktur weiter abgesichert werden kann.

**Schließen aller nicht benötigten offenen Ports**

Tabelle 3: Schließen aller nicht benötigten offenen Ports

**Sperren nicht benötigter Services**

Für alle drei fiktiven Szenarien wird empfohlen, die Verschlüsselungsmethode WPA2-AES-CCM (128 Bit) anstelle von WPA2-TKIP zu nutzen.

Das Dokument Technische Richtlinie TR-02102 (siehe [TR02102]) des BSI enthält Empfehlungen für die Verwendung von SSL/TLS. Diese Empfehlungen sollten die Basis für die spätere Aktivierung der genutzten Cipher-Suiten sein. Mit welcher TLS-Version für welches der drei fiktiven Szenarien die Informationen ausreichend abgesichert werden können, zeigt die folgende Tabelle.

Tabelle 4: Empfohlene TLS-Versionen je Szenario

**Sperren nicht benötigter Management-Zugänge**

Um potentielle Angriffsvektoren zu reduzieren, sollte die Administration der WLAN-Komponenten z. B. via Secure Shell (SSH), HyperText Transfer Protocol Secure (HTTPS) oder SNMP aus einem dedizierten Management-Netz heraus erfolgen. Die WLAN-Infrastruktur sollte nicht über einen per WLAN angebundenen Client administriert werden.

Um Innentäter-Angriffe vorzubeugen, sollte eine zentrale Authentisierung auf Basis von personalisierten Benutzerkonten etabliert werden. Die für das Benutzerkonto des Administrators hinterlegten Berechtigungen müssen nach dem Minimalprinzip erfolgen.

Im Rahmen der Notfallvorsorge ist es empfehlenswert, ein lokales Benutzerkonto (Notfallbenutzerkonto) zu hinterlegen. Das Passwort des Notfallbenutzerkontos muss der etablierten Passwortrichtlinie der Institution genügen. Nach jeder Verwendung des Notfallbenutzerkontos muss dessen Passwort geändert werden. Verwendung und Einsatzgrund müssen anschließend nachvollziehbar dokumentiert werden.

**Erkennen und Sperren unberechtigter Benutzer-Zugänge**

ARP-Spoofing-Angriffe sollten erkannt und abgewehrt werden, wenn IP-Adressen via DHCP-Server vergeben werden. Hierfür können DHCP Snooping und Dynamic ARP Inspection (DAI) eingesetzt werden.

#### NET.2.1.M6 Sichere Konfiguration der WLAN-Clients

Für einen sicheren WLAN-Betrieb ist es wichtig, dass auch alle mit den WLANs gekoppelten Clients sicher konfiguriert sind. Geeignete Anforderungen für eine sichere Konfiguration von Clients sind im Baustein SYS 2.1 *Allgemeiner Client* und NET.2.2 *WLAN-Nutzung* definiert. Zusätzlich muss die WLAN-Schnittstelle deaktiviert werden, wenn sie über einen längeren Zeitraum nicht genutzt wird. Durch den Betrieb von WLANs dürfen etablierte Sicherheitsinfrastrukturen (und insbesondere Firewalls) nicht umgangen werden können.

Sollen WLAN-Clients (z. B. Smartphones) selbst Hotspot-ähnliche Funktionen zur Verfügung stellen, müssen die Benutzer sicherstellen, dass voreingestellte SSIDs, kryptographische Schlüssel und Passwörter durch sie geändert wurden, bevor die Hotspot-Funktionen aktiviert werden. Das Passwort (WPA2-Schlüssel) sollte so gewählt sein, dass es nur schwer erraten werden kann.

#### NET.2.1.M7 Aufbau eines Distribution Systems [Planer]

Ein Distribution System verbindet die Access Points untereinander und bindet die weitere Infrastruktur ein. Es gibt zwei Arten von Distribution Systemen:

* kabelgebundene Distribution Systeme (alle Access Points werden untereinander und mit der weiteren Infrastruktur verkabelt)
* Wireless Distribution Systeme (eine direkte Verkabelung zwischen den Access Points ist nicht notwendig)
Sind hohe Verfügbarkeitsanforderungen zu erfüllen, sollte kein Wireless Distribution System eingerichtet werden. In einem Wireless Distribution System müssen Repeater sowohl mit den WLAN-Clients als auch mit dem Access Point kommunizieren. Hierdurch reduziert sich die Übertragungsrate um die Hälfte. Diese drastische Reduzierung der Übertragungsrate lässt sich nur umgehen, indem Clients und Repeater auf einer anderen Frequenz miteinander kommunizieren als Repeater und Access Point/WLAN-Router. Theoretisch lässt sich ein Wireless Distribution System mit bis zu 254 Repeatern in einem Netz betreiben, wenn die Repeater nicht in Reihe, sondern im Stern angebunden sind, um Signalüberschneidungen zu vermeiden.

Bevor ein kabelgebundenes Distribution System aufgebaut wird, sollte entschieden werden, ob eine eigenständige physische Switch-Infrastruktur für die WLANs aufgebaut werden soll, eine virtualisierte Switch-Infrastruktur oder ob alternativ eine logische Segmentierung durch Virtual Local Area Networks (VLANs) ausreichend ist. Hierbei sind insbesondere Sicherheitsaspekte zu beachten.

#### NET.2.1.M8 Verhaltensregeln bei WLAN-Sicherheitsvorfällen

Falls sich das WLAN in nicht vorgesehener Weise verhält (z. B. WLAN ist längere Zeit nicht verfügbar, Zugriff auf Netzressourcen ist nicht möglich, Netzperformance bricht dauerhaft ein), kann dies durch einen Sicherheitsvorfall verursacht worden sein. Dieser kann durch einen Angreifer, Fehlkonfigurationen oder Systemfehler herbeigeführt worden sein.

Der IT-Betrieb sollte die folgenden Maßnahmen umsetzen:

* Die Benutzer müssen den IT-Betrieb über geeignete Eskalationsstufen erreichen können. 
* Am Übergabepunkt der WLAN-Kommunikation ins interne LAN sollte bei einem Angriff auf das WLAN die Kommunikation selektiv pro SSID, Access Point oder sogar für die komplette WLAN-Infrastruktur gesperrt werden.
* Bei einem Sicherheitsvorfall oder einem Diebstahl sollte der IT-Betrieb passende Sicherheitsmaßnahmen einleiten können. Idealerweise greifen sie auf abgestimmte und dokumentierte Prozeduren zurück. Mögliche Aktionen sind z. B.: 

 
	+ Abschaltung von Access Points
	+ Herunterfahren von Servern 
	+ Überprüfung der Konfigurationen der Access Points
	+ Sicherung aller Dateien, die Aufschluss über die Art und Ursache des aufgetretenen Problems geben könnten (z. B. ob tatsächlich ein Angriff erfolgt ist und auf welche Weise der Angreifer eindringen konnte), d. h. insbesondere Sicherung aller relevanten Protokolldateien.
	+ Gegebenenfalls Wiedereinspielen der Original-Konfigurationsdaten 
	+ Benachrichtigung der Benutzer mit der Bitte, ihre Arbeitsbereiche auf Unregelmäßigkeiten zu prüfen.
	  

 
Falls Access Points gestohlen worden sind, müssen gezielte Sicherheitsmaßnahmen ergriffen werden, wie z. B.:

* Änderung aller eingesetzten kryptographischen Schlüssel, also z. B. der PSKs im Falle der Verwendung von WPA2-PSK
* Konfigurationsänderung auf RADIUS-Servern, um den entwendeten Access Point (IP, Name, RADIUS-Client, Shared Secret, IPSec) zu sperren.
Sind WLAN-Clients entwendet worden und wird eine zertifikatsbasierte Authentisierung verwendet, müssen auch die Client-Zertifikate gesperrt werden.

Die möglichen Konsequenzen sicherheitskritischer Ereignisse müssen untersucht werden. Letztlich sind alle erforderlichen Maßnahmen zu ergreifen, um eine missbräuchliche Verwendung von entwendeten Geräten zum Zugriff auf das Netz der Institution auszuschließen.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "WLAN-Betrieb".

#### NET.2.1.M9 Sichere Anbindung von WLANs an ein LAN [Planer]

Die WLAN-Komponenten müssen an den Übergängen zwischen WLANs und LAN abgesichert werden, beispielsweise durch einen Paketfilter. Um unnötigen Broadcast und Multicast Traffic zu vermeiden, sollte für jede vergebene SSID ein korrespondierendes VLAN etabliert sein. Weitere Anforderungen, die zu beachten sind, finden sich im Baustein NET.1.1 *Netz-Architektur und -design*.

Sollen WLANs sicher an ein LAN angebunden werden, kann zwischen einer Controller-basierten und einer Controller-losen Administration von Access Points unterschieden werden. Angemessene Absicherungsmaßnahmen für die jeweilige Variante werden nachfolgend aufgezeigt.

**Controller-basierte Verwaltung der Access Points**

Für eine Controller-basierte Verwaltung der WLAN-Infrastruktur werden in der folgenden Tabelle angemessene Absicherungsmaßnahmen für die Anbindung des Access Points an das LAN benannt.

Tabelle 5: Empfohlene Access-Point-Funktionen je Szenario

Ein pragmatischer Ansatz für eine lokale Auskopplung der Nutzdaten kann in Teilen für Szenario 3 gewählt werden, sofern der berechtigte Zugang zum WLAN mittels IEEE 802.1X und EAP-TLS überprüft wird und die Access Points und Endgeräte den Standard IEEE 802.11ac vollumfänglich unterstützen. Die Kommunikation zwischen den Access Points und den WLAN-Controllern muss auch kryptographisch abgesichert sein. Um mögliche Risiken des Verlusts der Vertraulichkeit und Integrität der über Funk übertragenen Informationen zu kompensieren, wird eine zusätzliche Overlay-Verschlüsselung empfohlen.

Bei den Szenarien 1 und 2 geht die Benutzerkommunikation direkt vom Access Point über den Switch in die internen Netze über. Ein pragmatischer Ansatz ist deshalb nicht möglich. Lediglich freigegebene und in die etablierten Prozesse aufgenommene Access Points der Institution dürfen an das Netz angebunden sein. Dies sollte mittels IEEE 802.1X sichergestellt werden. 

Alle Access Points beziehen ihre Betriebssoftware direkt vom zugeordneten WLAN-Controller. Die Betriebssoftware eines Access Points wird über einen kryptographisch abgesicherten Kanal aktualisiert. Wird die Betriebssoftware auf Basis von Klartext-Protokollen ausgetauscht, sollte im Anschluss die Integrität der Software anhand von Signaturen verifiziert werden.

Die WLAN-typischen Kommunikationsenden für bereitgestellte Gastzugänge müssen in einer Demilitarized Zone (DMZ) enden. Zugriffe aus dem Gast-WLAN sind wie Zugriffe aus dem Internet zu behandeln. Sie dürfen nur über ein Sicherheitsgateway zugelassen werden.

**Controller-lose Verwaltung der Access Points**

Ein pragmatischer Ansatz ist bei einer Controller-losen Verwaltung der Access Points meist nicht möglich, da die Benutzerkommunikation direkt vom Access Point über den Switch in die internen Netze übergeht.

Um Roaming-Funktionen bereitzustellen, werden zwischen den einzelnen Access Points autarke Netze aufgespannt, meist im Default-VLAN. Ob die Anforderungen für den Betrieb der Access Points mit den Sicherheitsanforderungen vereinbar sind, kann mit den folgenden Fragen überprüft werden:

* Ist die Kommunikation der Access Points untereinander ausreichend kryptographisch abgesichert?
* Ist die Gruppe der Mitarbeiter mit Zugang zu Spiegelports an den Switches bekannt und begrenzt?
* Ist ein nicht genutzter Switch-Port aus dem Default-VLAN entbunden?
* Ist eine Hardware-Authentisierung am Switch-Port eingerichtet?
* Sind die Roaming-Funktionen durch Bridging- und Tunneling-Methoden realisiert?
* Endet die Gast-Zugangskommunikation über einen kryptographischen Tunnel in der DMZ?
Auch für Access Points, die ohne Controller administriert werden, gilt, dass lediglich freigegebene und in die etablierten Prozesse aufgenommene Access Points der Institution an das Netz angebunden sein dürfen. Mittels IEEE 802.1X sollte sichergestellt werden, dass diese Anforderung erfüllt ist. Der berechtigte Zugang von Endgeräten zum WLAN sollte ebenfalls mittels IEEE 802.1X und EAP-TLS überprüft werden. 

Alle Access Points beziehen ihre Betriebssoftware direkt vom zugeordneten WLAN-Managementsystem (WNMS). Die Betriebssoftware eines Access Points sollte über einen kryptographisch abgesicherten Kanal aktualisiert werden. Wird die Betriebssoftware auf Basis von Klartext-Protokollen ausgetauscht, sollte im Anschluss die Integrität der Software anhand von Signaturen verifiziert werden.

Die eingesetzten Access Points und eingebundenen WLAN-Clients sollten den Standard IEEE 802.11ac vollumfänglich unterstützen. Die Access-Point-zu-Access-Point-Kommunikation muss auf Basis von Internet Protocol Security (IPsec) oder TLS in einem gekapselten Tunnel stattfinden.

#### NET.2.1.M10 Erstellung einer Sicherheitsrichtlinie für den Betrieb von WLANs

Für den Einsatz von WLAN-Komponenten in Institutionen sollte eine geeignete Sicherheitsrichtlinie erstellt werden. Diese WLAN-spezifische Sicherheitsrichtlinie sollte konform zum generellen Sicherheitskonzept und den allgemeinen Sicherheitsrichtlinien der Institution sein. Sie sollte regelmäßig auf Aktualität überprüft und gegebenenfalls angepasst werden. 

Eine WLAN-Sicherheitsrichtlinie sollte unter anderem folgende Punkte umfassen:

* Es sollte beschrieben sein, wer in der Institution WLAN-Komponenten installieren, konfigurieren und benutzen darf. 
* Für alle WLAN-Komponenten sollten Sicherheitsmaßnahmen und eine Standard-Konfiguration festgelegt werden. 
* Bei einem Verdacht auf Sicherheitsprobleme muss ein Sicherheitsverantwortlicher hierüber informiert werden, damit dieser weitere Schritte unternehmen kann (siehe auch DER.2.1 Behandlung von Sicherheitsvorfällen).
Der IT-Betrieb sollte über die Gefährdungen, denen WLAN-Komponenten ausgesetzt sind und die zu beachtenden Sicherheitsmaßnahmen informiert bzw. geschult werden.

Die korrekte Umsetzung der in der WLAN-Sicherheitsrichtlinie beschriebenen Sicherheitsmaßnahmen sollte regelmäßig kontrolliert werden.

#### NET.2.1.M11 Geeignete Auswahl von WLAN-Komponenten

Wichtige Kriterien für die Auswahl von WLAN-Komponenten sind Sicherheit, Datenschutz und Kompatibilität. Kompatibilitätsprobleme können bei der Vielzahl verschiedener WLAN-Komponenten nicht ausgeschlossen werden. Um Kompatibilitätsprobleme zu vermeiden, müssen alle Komponenten von der Wi-Fi Alliance zertifiziert sein und die IEEE 802.11 Standards unterstützen. Alle WLAN-Komponenten dürfen nur von den Regulierungsgremien des Landes freigegebene Frequenzbänder verwenden. Jeder Anbieter von WLAN-Komponenten muss hierüber in den Datenblättern zu seinem Produkt kostenfrei Auskunft erteilen.

Im Rahmen der Beschaffung von Access Points und korrespondierenden Managementsystemen sollte Folgendes geprüft werden:

* Wie viele WLAN-Kanäle können verwaltet werden?
* Ist die SSID einstellbar?
* Welche kryptographischen Verfahren sind implementiert?
* Können für die Authentisierung die gewünschten Modi eingestellt werden?
* Welche EAP-Methoden werden unterstützt?
* Kann die Administration auf kryptographisch abgesicherte Kommunikationswege beschränkt werden? Können Klartextprotokolle abgeschaltet werden?
* Ist Netflow in Version 9 (RFC 3954) zur Informationsflusskontrolle nutzbar?
* Sind Mechanismen zur Zugriffssteuerung vorhanden?
* Sind Mechanismen für eine applikationsbasierte Umsetzung von Quality of Service integriert?
Einige WLAN-Komponenten können drahtlos direkt über das WLAN konfiguriert werden. Ist diese Funktion integraler Bestandteil der Komponenten, sollte sie abschaltbar sein, um Risiken zu minimieren. Um in der Institution etablierte Rollen- und Berechtigungskonzepte umzusetzen, darf ein Administrationszugriff auf WLAN-Komponenten nur für autorisierte Personen möglich sein.

Im Rahmen der Beschaffung sollte auch geprüft werden, ob alle WLAN-Komponenten mit den etablierten Netz-, Sicherheits-, Authentisierungs-, Monitoring- und Protokollierungsinfrastrukturen korrekt zusammenarbeiten. Hierzu zählt z. B. Folgendes:

* Die im WLAN genutzten Authentisierungsmethoden müssen von den Betriebssystemen und der Hardware der Clients, den Access Points, den Netzmanagementsystemen und den Authentisierungsservern unterstützt werden.
* Falls im WLAN die Authentisierung nach IEEE 802.1X erfolgt, müssen die Access Points die Authentisierungsmethoden der EAP-Familie unterstützen und die mitgeteilten Informationen innerhalb von IEEE 802.1X korrekt verarbeiten.
* Zusätzlich ist zu prüfen, ob die Authentisierungsanfragen mittels sicherer Abfragemethoden an eine zentrale Benutzerdatenbank durchgereicht werden können.
Ist geplant, eine größere WLAN-Infrastruktur zu etablieren, sollte durch eine entsprechende Teststellung geprüft werden, ob die definierten und dokumentierten Anforderungen eingehalten werden, bevor die Infrastruktur endgültig beschafft wird.

#### NET.2.1.M12 Einsatz einer geeigneten WLAN-Management-Lösung

Der Leistungsumfang der eingesetzten WLAN-Managementlösung sollte mindestens die folgenden Aspekte erfüllen:

* Dokumentation der Firmware-Stände der Access Points und der WLAN-Clients, 
* Dokumentation der Konfigurationen, 
* Historienverwaltung von Konfigurationsänderungen, 
* Auswertung und Bewertung von Alarmen,
* Auswertung von Statistiken zur Fehlersuche, 
* Auslösung von Maßnahmen bei einem vermuteten Sicherheitsvorfall, 
* Anpassung von Schwellwerten zur Alarmauslösung an eine geänderte WLAN-Nutzung,
* Protokollierung und deren sinnvollen Aufbereitung für die Auswertung und 
* versenden der Protokolldaten an ein zentrales Logging-System zur nachgelagerten Auswertung.
Beim WLAN-Konfigurationsmanagement sind im Hinblick auf die Sicherheit einer Installation die zentrale Administration der Sicherheitseinstellungen und die Bereitstellung abgesicherter Installations- und Managementwege von entscheidender Bedeutung. Unter Sicherheitsaspekten ist darüber hinaus dringend zu empfehlen, dass WLAN-Managementsysteme dabei unterstützen, die Luftschnittstelle zu überwachen und die dabei gewonnenen Messergebnisse und Funktionen zu interpretieren. Zu diesen Messergebnissen und Funktionen gehören Rogue Access Point Detection, Wireless Intrusion Detection System (WIDS) sowie Wireless Intrusion Prevention System (WIPS). Die beiden nachfolgenden Tabellen benennen für die drei fiktiven Szenarien die Mindestparameter zur Erkennung von Manipulationen und Angriffen.

Tabelle 6: Erkennung von Manipulationen und Angriffen durch ein WIDS an der Infrastruktur

Tabelle 7: Erkennung von Manipulationen und Angriffen durch ein WIDS auf dem Client

Mittels einer Controller-basierten Lösung können Richtlinien zentral verwaltet und der WLAN-Traffic kann auf dem WLAN-Controller terminiert werden. Hierdurch kann z. B. der eventuell vorhandene Gästeverkehr zur DMZ oder Firewall weitergeleitet werden. Bei einer Controller-losen Umgebung müssen die Access Points und nachgelagerte Systeme mittels VPN diese Funktion übernehmen.

Ein weiterer Aspekt der Controller-basierten Lösung ist, dass das Failover- sowie das Failback-Verhalten einfach koordiniert werden können. Der IT-Betrieb muss sicherstellen, dass bei Ausfall eines Access Points der Netzverkehr nicht zu stark beeinträchtigt wird. In einem Controller-basierten Modell dient der Controller als Single Point of Coordination für alle Access Points. Fällt einer der Access Points aus, reagiert der Controller, um so die Latenzen so kurz wie möglich zu halten. Dies wird erreicht, indem er die zentral gespeicherten Session-Informationen eines WLAN-Benutzers sofort an einen verfügbaren Access Point weitergibt. Bei Controller-losen Infrastrukturen muss dies durch dem Routing-Protokoll ähnliche Mechanismen innerhalb des lokalen Netzes implementiert werden.

#### NET.2.1.M13 Regelmäßige Sicherheitschecks in WLANs

Um WLANs sicher betreiben zu können, ist es besonders wichtig, die Sicherheitsvorgaben umzusetzen und die Verfügbarkeit regelmäßig zu überprüfen. Die Messungen der Performance müssen in die vorhandene Monitoring- und Protokollierungsinfrastruktur integriert sein. Im einfachsten Fall kann eine WLAN-Analyse über einen WLAN-Client erfolgen, der mit entsprechender Spezial-Software ausgestattet ist. Diese Art der Überwachung ist jedoch nur für Szenario 1 zu empfehlen. Besser und stetiger kann die WLAN-Infrastruktur kontrolliert werden, wenn die hierfür notwendigen Überwachungsfunktionen mit in die Access Points integriert sind. Mit Hilfe von in den Access Points integrierten Detektoren können folgende Überwachungsaktionen automatisiert durchgeführt werden:

* Fremdgeräte (insbesondere fremde Access Points) können erkannt werden.
* Wireless Site Surveys können mit dem Ziel durchgeführt werden, Informationen zu Abdeckung, Datenraten, Übertragungskapazität, Applikationsbitrate, Bitübertragungsrate pro WLAN-Benutzer, Quality of Service (QoS) usw. zu erhalten.
* Die Konfiguration von WLAN-Netzelementen kann überwacht werden.
Der IT-Betrieb sollte die folgenden Aufgaben planen und festschreiben, um eine angemessene Alarm- und Fehlerbehandlung sicherzustellen:

* Alarme sollten ausgewertet und bewertet werden.
* Statistiken sollten zur Fehlersuche ausgewertet werden. 
* Bei einem vermuteten Sicherheitsvorfall sollten abgestimmte Maßnahmen ausgelöst werden.
* Bei einer geänderten WLAN-Nutzung sollten die Schwellwerte zur Alarmauslösung angepasst werden.
Im Zuge eines Sicherheitschecks kann ein WLAN auch mit Hilfe eines Penetrationstests auf Schwachstellen untersucht werden. Dabei ist für alle getroffenen Sicherheitsmaßnahmen genau zu prüfen, ob diese den Angriffen gewachsen sind, gegen die sie wirken sollen. In Tabelle 8 sind Empfehlungen für Zeitintervalle abgebildet, um interne und externe Penetrationstests durchzuführen.

Tabelle 8: Empfohlene Zeitintervalle für regelmäßige Penetrationstests

#### NET.2.1.M14 Regelmäßige Audits der WLAN-Komponenten

Bei allen Komponenten der WLAN-Infrastruktur (Access Points, Distribution System, WLAN-Management-Lösung etc.) sollte regelmäßig überprüft werden, ob alle festgelegten Sicherheitsmaßnahmen umgesetzt und korrekt konfiguriert sind. Das WLAN-Managementsystem sollte je nach bereitgestelltem Funktionsumfang nicht nur die aktuellen, sondern auch zurückliegende Konfigurationen der Access Points verwalten. Öffentlich aufgestellte Access Points sollten regelmäßig stichprobenartig darauf geprüft werden, ob es gewaltsame Öffnungs- oder Manipulationsversuche gab. Sollten Unregelmäßigkeiten oder Schwachstellen erkannt werden, sollten diese dokumentiert werden. Abweichungen sollte nachgegangen werden.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.2.1.M15 Verwendung eines VPN zur Absicherung von WLANs(CI)

Um die Kommunikation über die WLAN-Infrastruktur zusätzlich abzusichern und so sicherzustellen, dass die Übertragung schutzbedarfsgerecht vollständig abgesichert ist, sollte ein VPN eingesetzt werden. Weiterführende Informationen zum Thema VPN können dem Baustein NET.3.3 *VPN* bzw. den zugehörigen Umsetzungshinweisen entnommen werden.

#### NET.2.1.M16 Zusätzliche Absicherung bei der Anbindung von WLANs an ein LAN(CIA)

Wird eine WLAN-Infrastruktur an ein LAN angebunden, sollte der Übergang zwischen WLAN- und LAN-Infrastruktur entsprechend dem höheren Schutzbedarf, beispielsweise durch ein Intrusion Detection System bzw. Intrusion Prevention System (IDS/IPS) abgesichert sein. Weiterführende Informationen zum Thema IDS/IPS können dem Baustein NET.3.4 *IDS/IPS* bzw. den zugehörigen Umsetzungshinweisen entnommen werden.

#### NET.2.1.M17 Absicherung der Kommunikation zwischen Access Points(C)

Zwischen den Access Points sollte über die Funkschnittstelle und das LAN verschlüsselt kommuniziert werden, um die Vertraulichkeit der übermittelten Informationen zu gewährleisten.

**Kommunikation über die Funkschnittstelle**

Um die Kommunikation über die Funkschnittstelle abzusichern, sind die Maßnahmen NET.2.1.M3 *Auswahl geeigneter Kryptoverfahren für WLAN* und NET.2.1.M5 *Sichere Basis-Konfiguration der Access Points* anzuwenden.

**Kommunikation zwischen Access Point und WLAN-Managementsystem**

Aufgrund des erhöhten Schutzbedarfs wird davon ausgegangen, dass die Kommunikation zwischen einem Access Point und dem WLAN-Managementsystem nicht cloudbasiert erfolgt. In der folgenden Tabelle sind Protokolle zu finden, die dazu eingesetzt werden können, um die Kommunikation abzusichern. Der zu erfüllende Schutzbedarf wird dabei berücksichtigt.

Tabelle 9: Kommunikation zwischen Access Point und WLAN-Managementsystem

**Kommunikation von Access Point zu Access Point**

Eine Kommunikation von Access Point zu Access Point ist in der Controller-basierten WLAN-Infrastruktur nicht direkt möglich, sondern erfolgt immer über den zentralen WLAN-Controller. Die möglichen Protokolle und zugehörigen Authentisierungsmethoden wurden bereits in Tabelle 9 aufgezeigt. Die folgende Tabelle führt deshalb nur die Protokolle und zugehörigen Authentisierungsmethoden für eine Controller-lose WLAN-Infrastruktur auf.

Tabelle 10: Kommunikation von Access Point zu Access Point

Das aufgezeigte GRE-Protokoll in Beispiel 1 bietet selbst keine Verschlüsselung und schützt nicht ausreichend hinsichtlich der Vertraulichkeit und Integrität für Roaming- und WLAN-Managementinformationen. Es dient an dieser Stelle nur der Sensibilisierung bei der Auswahl der WLAN-Produkte und sollte nicht verwendet werden.

#### NET.2.1.M18 Einsatz von Wireless Intrusion Detection / Wireless Intrusion Prevention Systemen(CIA)

Um Sicherheitsvorfälle und Schwachstellen zeitnah zu identifizieren und entsprechende Gegenmaßnahmen direkt einleiten zu können, sollten WIDS/ WIPS eingesetzt werden.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

WLANs können in zwei verschiedenen Architekturen betrieben werden. Im Ad-hoc-Modus kommunizieren zwei oder mehr mobile Endgeräte (also Clients), die mit WLAN-Funktionalität ausgestattet sind, direkt miteinander. In den meisten Fällen wird ein WLAN im Infrastruktur-Modus betrieben, d. h. die Kommunikation der Clients erfolgt über zentrale Access Points. Über die Access Points erfolgt auch die Verbindung in kabelgebundene LAN-Segmente.

Der Infrastruktur-Modus lässt mehrere Einsatzvarianten zu:

* Mittels mehrerer Access Points können überlappende Funkzellen installiert werden, sodass beim Übergang eines Clients in die nächste Funkzelle die Funkverbindung aufrecht erhalten werden kann ("Roaming"). Zwei Access Points können als Brücke (Bridge) zwischen zwei leitungsgebundenen LANs eingesetzt werden. Ebenso ist der Einsatz eines Access Points als Relaisstation (Repeater) möglich, um die Reichweite zu erhöhen 
* Werden entsprechende Komponenten (Richtantennen) an den Access Points verwendet, können WLANs auch dazu eingesetzt werden, um Liegenschaften zu vernetzen. Hier können laut Herstellerangaben Reichweiten im Kilometerbereich erreicht werden. Die Access Points können dabei als Relaisstation oder Brücke betrieben werden.
Im Standard IEEE 802.11 werden die Bezeichnungen Independent Basic Service Set (IBSS) für Funk-Netze im Ad-hoc-Modus und Basic Service Set (BSS) für Konstellationen im Infrastruktur-Modus mit einem Access Point verwendet. Mehrere gekoppelte BSS werden als Extended Service Set (ESS) bezeichnet, das koppelnde Netz wird Distribution System (DS) genannt.

Im 2,4 GHz-Frequenzbereich stehen in Deutschland 13 Frequenzkanäle mit einem Frequenzabstand von 5 MHz für die Funkübertragung zur Verfügung. Bei einer Kanalbandbreite von ca. 22 MHz können jedoch nur maximal 3 Kanäle gleichzeitig überlappungsfrei genutzt werden. Im Frequenzbereich von 5,15 bis 5,35 GHz und bei 5,47 bis 5,725 GHz sind in Deutschland insgesamt 19 Kanäle in einem Abstand von 20 MHz unter Auflagen freigegeben worden. Bei einer Kanalbandbreite von 20 MHz werden direkt benachbarte Kanäle hier nicht gestört. Im 5 GHz Frequenzbereich arbeiten auch militärische und zivile Radar- und Navigationsanwendungen, und es dürfen hier nur Systeme eingesetzt werden, die eine dynamische Frequenzwahl und eine Anpassung der Sendeleistung unterstützen.

Die in IEEE 802.11 definierten Mechanismen dienen ausschließlich dazu, die Funkstrecke zwischen den Clients und Access Points zu sichern. 

Als zusätzlicher Schutz der Authentisierung kann das Extensible Authentication Protocol (EAP) gemäß Standard IEEE 802.1X verwendet werden. EAP wird im RFC 3748 genau beschrieben. Die Benutzer melden sich hier bei einer Authentisierungsinstanz an, z. B. an einem RADIUS-Server, und dieser prüft die Zugangsberechtigung, bevor der Sitzungsschlüssel ausgetauscht wird. EAP unterstützt eine Reihe von Authentisierungsmethoden, so dass auch Zertifikate und Zwei-Faktor-Authentisierungen genutzt werden können.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "WLAN-Betrieb" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSIDKS] Drahtlose Kommunikationssysteme und ihre Sicherheitsaspekte

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [IEEE] Institute of Electrical and Electronics Engineers (IEEE)

  

 IEEE, (zuletzt abgerufen am 05.10.2017)  
 <https://www.ieee.org/index.html>

 
* #### [ISIWLAN] BSI-Standard zur Internet-Sicherheit (ISi-Reihe)

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [KB2977292] Microsoft security advisory

  

 Sicherheitsupdate für Windows 7 für x64-basierte Systeme, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/de-de/download/details.aspx?id=44350>

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02.2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [RSWLAN] Mehr Rechtssicherheit bei WLAN

  

 BMWi, (zuletzt abgerufen am 05.10.2017)  
 <https://www.bmwi.de/Redaktion/DE/Artikel/Digitale-Welt/wlan.html>

 
* #### [TR03103] Technische Richtlinie Sicheres Wireless LAN

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
* #### [WIFIA] Wi-Fi Allianz

  

 The worldwide netword of companies, (zuletzt abgerufen am 05.10.2017)  
 <http://www.wi-fi.org/>

 
