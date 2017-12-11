1 Beschreibung
--------------

### 1.1 Einleitung

Eine Firewall ist ein System aus soft- und hardwaretechnischen Komponenten, das dazu eingesetzt wird, IP-basiere Datennetze sicher zu koppeln. Dazu wird mit Hilfe einer Firewall-Struktur die technisch mögliche auf die in einer Sicherheitsrichtlinie als sicher definierte Kommunikation eingeschränkt. Sicherheit bedeutet hierbei, dass ausschließlich die erwünschten Zugriffe oder Datenströme zwischen verschiedenen Netzen zugelassen werden.

Um Netzübergänge abzusichern, wird oft nicht mehr eine einzelne Komponente verwendet, sondern eine ganze Reihe von IT-Systemen, die unterschiedliche Aufgaben übernehmen, z. B. ausschließlich Pakete zu filtern oder Netzverbindungen mithilfe von Proxy-Funktionen strikt zu trennen. Der in diesem Baustein verwendete Begriff Application Level Gateway (ALG) bezeichnet eine Firewallkomponente, die Datenströme auf Basis von Sicherheitsproxys regelt.

Eine Firewall wird am zentralen Übergang zwischen unterschiedlich vertrauenswürdigen Netzen eingesetzt. Unterschiedlich vertrauenswürdige Netze stellen dabei nicht unbedingt nur die Kombination Internet/Intranet dar. Vielmehr können auch zwei institutionsinterne Netze einen unterschiedlich hohen Schutzbedarf besitzen, z. B. hat das Netz der Bürokommunikation meistens einen anderen Schutzbedarf als das Netz der Personalabteilung, in dem besonders schützenswerte, personenbezogene Daten übertragen werden.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, eine Firewall bzw. eine Firewall-Struktur sicher einsetzen zu können, um Netze mit unterschiedlichen Schutzanforderungen sicher miteinander zu verbinden.

### 1.3 Abgrenzung

Der vorliegende Baustein baut auf den Baustein NET.1.1 *Netz-Architektur und -design* auf und enthält konkrete Anforderungen, die zu beachten und zu erfüllen sind, wenn netzbasierte Firewalls beschafft, aufgebaut, konfiguriert und betrieben werden. 

Um Netze abzusichern, sind meistens weitere Netzkomponenten erforderlich, z. B. Router und Switches. Anforderungen hierzu werden jedoch nicht in diesem Baustein aufgeführt, sondern sind in NET.3.1 *Router und Switches* zu finden. Wenn eine Firewall die Aufgaben eines Routers oder Switches übernimmt, gelten für sie zusätzlich die Anforderungen des Bausteins NET.3.1 *Router und Switches*.

Darüber hinaus wird nicht auf Produkte wie sogenannte Next Generation Firewalls (NGFW) oder Unified Threat Management Firewalls eingegangen, die zusätzlich funktionale Erweiterungen enthalten, z. B. VPN, Systeme zur Intrusion Detection und Intrusion Prevention (IDS/IPS), Virenscanner oder Spam-Filter. Sicherheitsaspekte dieser funktionalen Erweiterungen sind nicht Gegenstand des vorliegenden Bausteins, sondern werden z. B. in den Bausteinen NET.3.3 *VPN*, NET.3.4 *IDS/IPS*, OPS1.1.4 *Schutz vor Schadprogrammen* behandelt. 

Ebenso wird nicht auf eine Anwendungserkennung bzw. -filterung eingegangen. Sie ist eine gängige Funktion von Next Generation Firewalls sowie IDS/IPS. Da sich die Implementierungen zwischen den Produkten unterscheiden, wird empfohlen, sie je nach Einsatzszenario individuell zu betrachten. In diesem Baustein wird auch nicht auf die individuellen Schutzmöglichkeiten für extern angebotene Server-Dienste eingegangen, z. B. durch ein Reverse Proxy oder für Webdienste mithilfe einer Web Application Firewall (WAF). Darüber hinaus werden Aspekte der infrastrukturellen Sicherheit (z. B. geeignete Aufstellung oder Stromversorgung) nicht in diesem Baustein aufgeführt, sondern finden sich in den jeweiligen Bausteinen der Schicht INF.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Firewall von besonderer Bedeutung:

### 2 1 Distributed Denial of Service (DDoS)

Bei einem DDoS-Angriff auf ein geschütztes Netz (z. B. TCP-SYN-Flooding, UDP Packet Storm) kann aufgrund der vielen Netzverbindungen, die verarbeitet werden müssen, die Firewall ausfallen. Das kann dazu führen, dass bestimmte Dienste im Local Area Network (LAN) nicht mehr verfügbar sind oder das gesamte LAN ausfällt.

### 2 2 Manipulation

Gelingt es einem Angreifer, unberechtigt auf ein Firewall-System oder eine entsprechende Verwaltungsoberfläche zuzugreifen, kann er dort Dateien beliebig manipulieren. So kann er beispielsweise die Konfiguration ändern, zusätzliche Dienste starten oder Schadsoftware installieren. Ebenso kann er auf dem manipulierten System die Kommunikationsverbindungen mitschneiden. Auch lassen sich beispielsweise die Firewall-Regeln so verändern, dass aus dem Internet auf die Firewall und auf das Intranet der Institution zugegriffen werden kann. Weiterhin kann ein Angreifer einen Denial-of-Service-(DoS)-Angriff starten, indem er im Regelwerk den Zugriff auf einzelne Server-Dienste verhindert.

### 2 3 Software-Schwachstellen oder -Fehler

Firewalls sind komplexe Systeme und besonders am Übergang vom Intranet zum Internet zahlreichen Angriffen ausgesetzt. Hersteller von Firewalls veröffentlichen daher regelmäßig Updates und Patches, um Softwarefehler und bekannt gewordene Schwachstellen in ihren Produkten zu beheben. Werden diese jedoch nicht oder zu spät eingespielt, kann das Firewall-System erfolgreich angegriffen werden. Dadurch ist es möglich, dass Angreifer die Systeme manipulieren und so geschäftskritische Daten abfließen, Dienste ausfallen oder ganze Produktionsprozesse still stehen.

### 2 4 Umgehung der Firewall-Regeln

 Angreifer können mithilfe grundlegender Mechanismen in den Netzprotokollen die Firewall-Regeln umgehen (z. B. durch Fragmentierungsangriffe), um in einen durch die Firewall geschützten Bereich einzudringen. Im geschützten Bereich können sie anschließend weiteren Schaden anrichten (z. B. sensible Daten auslesen, manipulieren oder löschen).

### 2 5 Fehlerhafte Konfiguration und Bedienungsfehler einer Firewall

Eine fehlerhaft konfigurierte oder falsch bediente Firewall kann sich gravierend auf die Verfügbarkeit von Diensten auswirken. Werden beispielsweise Firewall-Regeln falsch gesetzt, können Netzzugriffe blockiert werden. Weiterhin können fehlerhafte Konfigurationen dazu führen, dass IT-Systeme nicht mehr ganz oder auch gar nicht mehr geschützt sind. Im schlimmsten Fall sind dadurch interne Dienste für Angreifer erreichbar.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Firewall aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.3.2.A1 Erstellung einer Sicherheitsrichtlinie [Informationssicherheitsbeauftragter (ISB)]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MUSS eine spezifische Sicherheitsrichtlinie erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie Firewalls sicher betrieben werden können. Die Richtlinie MUSS allen im Bereich Firewalls verantwortlichen Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, MUSS dies mit dem ISB abgestimmt und dokumentiert werden. Es MUSS regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse MÜSSEN sinnvoll dokumentiert werden.

#### NET.3.2.A2 Festlegen der Firewall-Regeln

Die gesamte Kommunikation zwischen den beteiligten Netzen MUSS über die Firewall geleitet werden. Es MUSS sichergestellt sein, dass von außen keine unbefugten Verbindungen in das geschützte Netz aufgebaut werden können. Ebenso DÜRFEN KEINE unbefugten Verbindungen aus dem geschützten Netz heraus aufgebaut werden. 

Für die Firewall MÜSSEN eindeutige Regeln definiert werden, die festlegen, welche Kommunikationsverbindungen und Datenströme zugelassen werden. Alle anderen Verbindungen MÜSSEN durch die Firewall unterbunden werden (Whitelist-Ansatz). Die Kommunikationsbeziehungen mit angeschlossenen Dienst-Servern (z. B. E-Mail-Servern, Web-Servern), die über die Firewall geführt werden, MÜSSEN in den Regeln berücksichtigt sein.

Es DÜRFEN KEINE IT-Systeme von außen über die Firewall auf das interne Netz zugreifen (siehe Vorgaben aus dem Baustein NET.1.1 *Netz-Architektur und -design)*. Etwaige Ausnahmen zu dieser Anforderung werden in den entsprechenden anwendungs- und systemspezifischen Bausteinen geregelt.

Es MÜSSEN Verantwortliche benannt werden, die Filterregeln entwerfen, umsetzen und testen. Zudem MUSS geklärt werden, wer Filterregeln verändern darf. Die getroffenen Entscheidungen sowie die relevanten Informationen und Entscheidungsgründe MÜSSEN dokumentiert werden.

#### NET.3.2.A3 Einrichten geeigneter Filterregeln am Paketfilter

Basierend auf den Firewall-Regeln aus NET.3.2.A2 *Festlegen der Firewall-Regeln* MÜSSEN geeignete Filterregeln für den Paketfilter definiert und eingerichtet werden.

Ein Paketfilter MUSS so eingestellt sein, dass er alle ungültigen TCP-Flag-Kombinationen verwirft. Grundsätzlich MUSS immer zustandsbehaftet gefiltert werden. Auch für die verbindungslosen Protokolle UDP und ICMP SOLLTEN zustandsbehaftete Filterregeln konfiguriert werden. Die Firewall MUSS die Protokolle ICMP und ICMPv6 restriktiv filtern.

#### NET.3.2.A4 Sichere Konfiguration der Firewall

Bevor eine Firewall eingesetzt wird, MUSS sie sicher konfiguriert werden. 

Eine Firewall DARF ausschließlich NUR von dafür autorisierten Personen installiert und konfiguriert werden, z. B. Verantwortlichen aus dem eigenen IT-Betrieb oder vertraglich gebundenen Dienstleistern.

Alle Konfigurationsänderungen MÜSSEN nachvollziehbar dokumentiert sein (siehe NET.3.2.A14 *Betriebsdokumentationen*). Die Integrität der Konfigurationsdateien SOLLTE geeignet geschützt werden. Zugangspasswörter MÜSSEN verschlüsselt gespeichert werden.

Eine Firewall MUSS so konfiguriert sein, dass ausschließlich zwingend erforderliche Dienste verfügbar sind. Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein. Auch MUSS begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden. Nicht benötigte (Auskunfts-) Dienste sowie nicht benötigte funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden.

Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen bestmöglich verborgen werden.

#### NET.3.2.A5 Restriktive Rechtevergabe

Es MUSS geregelt werden, wer auf die Firewall zugreifen darf, z. B. um sie zu konfigurieren oder zu überwachen. Dabei DÜRFEN immer NUR so viele Zugriffsrechte vergeben werden, wie für die jeweiligen Aufgaben erforderlich sind (Need-to-know-Prinzip). Unautorisierte Benutzerkonten MÜSSEN entfernt werden. Es MUSS sichergestellt werden, dass mit Administrator-Rechten (bzw. Root-Rechten) nur gearbeitet wird, wenn es notwendig ist.

#### NET.3.2.A6 Schutz der Administrationsschnittstellen

Alle Administrations- und Management-Zugänge der Firewall MÜSSEN auf einzelne Quell-IP-Adressen bzw. -Adressbereiche eingeschränkt werden. Es MUSS sichergestellt sein, dass aus nicht-vertrauenswürdigen Netzen heraus nicht auf die Administrationsschnittstellen zugegriffen werden kann.

Um die Firewall zu administrieren bzw. zu überwachen, DÜRFEN NUR sichere Protokolle eingesetzt werden oder es MUSS ein eigens dafür vorgesehenen Administrationsnetz (Out-of-Band-Management) verwendet werden (siehe Vorgaben aus dem Baustein NET.1.1 *Netz-Architektur und -design und NET.1.2 Netz-Management). *Für die Benutzerschnittstellen MÜSSEN geeignete Zeitbeschränkungen vorgegeben werden.

#### NET.3.2.A7 Notfallzugriff auf die Firewall

Es MUSS immer möglich sein, direkt auf die Firewall zugreifen zu können, sodass weiterhin lokal gearbeitet werden kann, auch wenn das gesamte Netz ausfällt.

#### NET.3.2.A8 Unterbindung von dynamischem Routing

In den Einstellungen der Firewall MUSS das dynamische Routing deaktiviert sein, es sei denn, der Paketfilter wird entsprechend dem Baustein NET.3.1 *Router und Switches* als Perimeter-Router eingesetzt. 

#### NET.3.2.A9 Protokollierung

Die Firewall MUSS so konfiguriert werden, dass sie mindestens folgende Ereignisse protokolliert:

* abgewiesene Netzverbindungen (Quell- und Ziel-IP-Adressen, Quell- und Zielport oder ICMP/ICMPv6-Typ, Datum, Uhrzeit),
* fehlgeschlagene Zugriffe auf System-Ressourcen aufgrund fehlerhafter Authentisierungen, mangelnder Berechtigung oder nicht vorhandener Ressourcen, 
* Fehlermeldungen der Firewall-Dienste und 
* allgemeine Systemfehlermeldungen.
Werden Sicherheitsproxys eingesetzt, MÜSSEN Sicherheitsverletzungen und Verstöße gegen Access-Control-Listen (ACLs oder auch kurz Access-Listen) geeignet protokolliert werden: mindestens Art der Protokollverletzung bzw. des ACL-Verstoßes, Quell- und Ziel-IP-Adresse, Quell- und Zielport, Dienst, Datum und Zeit sowie die Verbindungsdauer (falls erforderlich). 

Wenn sich ein Benutzer am Sicherheitsproxy authentisiert, MÜSSEN auch Authentisierungsdaten oder ausschließlich die Information über eine fehlgeschlagene Authentisierung protokolliert werden.

Die Verantwortlichen MÜSSEN darauf achten, dass bei der Protokollierung alle rechtlichen Rahmenbedingung eingehalten werden.

#### NET.3.2.A10 Abwehr von Fragmentierungsangriffen am Paketfilter

Am Paketfilter MÜSSEN Schutzmechanismen aktiviert sein, um IPv4- sowie IPv6-Fragmentierungsangriffe abzuwehren. 

#### NET.3.2.A11 Einspielen von Updates und Patches

Die Verantwortlichen MÜSSEN sich über bekannt gewordene Schwachstellen informieren. Updates und Patches MÜSSEN so schnell wie möglich eingespielt werden. Vorab SOLLTE auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. Solange keine Patches bei bekannten Schwachstellen verfügbar sind, MÜSSEN andere geeignete Maßnahmen getroffen werden, um die Firewall zu schützen.

Es MUSS darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden. Darauf MUSS auch bei zugehörigen Diensten innerhalb des Firewall-Systems geachtet werden.

#### NET.3.2.A12 Vorgehen bei Sicherheitsvorfällen

Es MUSS festgelegt werden, wie bei einem festgestellten Angriff reagiert werden soll. Die Aufgaben und Kompetenzen für die betroffenen Mitarbeiter MÜSSEN eindeutig festgelegt werden. Weitere Informationen hierzu siehe DER.2.1 *Incident Management*.

#### NET.3.2.A13 Regelmäßige Datensicherung

Es MÜSSEN in regelmäßigen Abständen Systemsicherungen der Firewall erstellt werden. Auch bevor eine Firewall neu installiert oder anders konfiguriert wird, MUSS das System gesichert werden. Wenn gesicherte Datenbestände wieder eingespielt werden, MÜSSEN sich die sicherheitsrelevanten Dateien wie Access-Listen, Passwortdateien und Filterregeln auf dem sicherheitstechnisch erforderlichen Konfigurationsstand befinden.

#### NET.3.2.A14 Betriebsdokumentationen

Die betrieblichen Aufgaben einer Firewall MÜSSEN nachvollziehbar dokumentiert werden. Es MÜSSEN alle Konfigurationsänderungen sowie sicherheitsrelevante Aufgaben dokumentiert werden, insbesondere Änderungen an den System-Diensten und dem Regelwerk der Firewall. Die Dokumentation MUSS vor unbefugten Zugriffen geschützt werden. Änderungen an der Konfiguration MÜSSEN zudem möglichst automatisch protokolliert werden.

#### NET.3.2.A15 Beschaffung einer Firewall

Bevor eine Firewall beschafft wird, MUSS eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Es MUSS darauf geachtet werden, dass das von der Institution angestrebte Sicherheitsniveau mit der Firewall erreichbar ist. Grundlage für die Beschaffung MUSS daher die Anforderungen aus der Sicherheitsrichtlinie sein.

Wird IPv6 eingesetzt, MUSS der Paketfilter die IPv6-Erweiterungsheader (Extension Header) überprüfen. Zudem MUSS sich IPv6 adäquat zu IPv4 konfigurieren lassen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Firewall. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.3.2.A16 Aufbau einer „P-A-P“-Struktur

Der Aufbau einer "Paketfilter – Application-Level-Gateway – Paketfilter"-(P-A-P)-Struktur SOLLTE aus mehreren Komponenten mit jeweils zugeeigneter Hard- und Software bestehen. Für die wichtigsten verwendeten Protokolle SOLLTEN Sicherheitsproxys auf Anwendungsschicht vorhanden sein und für andere Dienste zumindest generische Sicherheitsproxys für TCP und UDP. Die Sicherheitsproxys SOLLTEN zudem innerhalb einer abgesicherten Laufzeitumgebung des Betriebssystems ablaufen.

#### NET.3.2.A17 Deaktivierung von IPv4 oder IPv6

Wenn das IPv4- oder IPv6-Protokoll in einem Netz-Segment nicht benötigt wird, SOLLTE es am jeweiligen Firewall-Netzzugangspunkt (z. B. am entsprechenden Firewall-Interface) deaktiviert werden. Wenn das IPv4- oder IPv6-Protokoll gar nicht benötigt bzw. eingesetzt wird, SOLLTE es auf der Firewall komplett deaktiviert werden.

#### NET.3.2.A18 Administration über ein gesondertes Managementnetz

Firewalls SOLLTEN ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden. Eine eventuell vorhandene Administrationsschnittstelle über das eigentliche Datennetz (In-Band) MUSS deaktiviert werden. Die Kommunikation im Managementnetz SOLLTE über Management-Firewalls (siehe NET.1.1 *Netz-Architektur und -design*) auf wenige Managementprotokolle mit genau festgelegten Ursprüngen und Zielen beschränkt werden. Die verfügbaren Sicherheitsmechanismen der eingesetzten Managementprotokolle zur Authentisierung, Integritätssicherung und Verschlüsselung SOLLTEN aktiviert und alle unsicheren Managementprotokolle deaktiviert werden (siehe NET.1.2 *Netz-Management*).

#### NET.3.2.A19 Schutz vor TCP SYN Flooding, UDP Paket Storm und Sequence Number Guessing am Paketfilter

Am Paketfilter, der Server-Dienste schützt, die aus nicht-vertrauenswürdigen Netzen erreichbar sind, SOLLTE ein Limit für halboffene und offene Verbindungen gesetzt werden.

Am Paketfilter, der Server-Dienste schützt, die aus weniger oder nicht-vertrauenswürdigen Netzen erreichbar sind, SOLLTEN die sogenannten Rate Limits für UDP-Datenströme gesetzt werden. 

Am äußeren Paketfilter SOLLTE bei ausgehenden Verbindungen für TCP eine zufällige Generierung von Initial Sequence Numbers (ISN) aktiviert werden, sofern dieses nicht bereits durch Sicherheits-Proxys realisiert wird.

#### NET.3.2.A20 Absicherung von grundlegenden Internetprotokollen

Um ins Internet zu kommunizieren, SOLLTEN die Protokolle HTTP, SMTP und DNS inklusive ihrer verschlüsselten Versionen über protokollspezifische Sicherheitsproxys geleitet werden. 

#### NET.3.2.A21 Temporäre Entschlüsselung des Datenverkehrs

Verschlüsselte Verbindungen in nicht-vertrauenswürdige Netze SOLLTEN temporär entschlüsselt werden, um das Protokoll zu verifizieren und die Daten auf Schadsoftware zu prüfen. Hierbei MÜSSEN die rechtlichen Rahmenbedingungen beachtet werden.

Die Komponente, die den Datenverkehr temporär entschlüsselt, SOLLTE unterbinden, dass veraltete Verschlüsselungsoptionen (z. B. SSL) und kryptografische Algorithmen (z. B. DES, MD5, SHA1) benutzt werden.

Auch SOLLTE das eingesetzte TLS-Proxy prüfen können, ob Zertifikate vertrauenswürdig sind. Ist ein Zertifikat nicht vertrauenswürdig, SOLLTE es möglich sein, die Verbindung abzuweisen. Eigene Zertifikate SOLLTEN nachrüstbar sein, um auch "interne" Root-Zertifikate konfigurieren und prüfen zu können. Vorkonfigurierte Zertifikate SOLLTEN überprüft und entfernt werden, wenn sie nicht benötigt werden.

#### NET.3.2.A22 Sichere Zeitsynchronisation

Es SOLLTE eine sichere Zeitsynchronisation mit einem Network-Time-Protocol-(NTP)-Server erfolgen. Die Firewall SOLLTE keine externe Zeitsynchronisation zulassen. Weitere Anforderungen sind dem Baustein NET.1.2 *Netzmanagement* zu entnehmen.

#### NET.3.2.A23 Systemüberwachung und -Auswertung

Firewalls SOLLTEN in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden. Weiterhin SOLLTE ein Prozess definiert werden, der regelt, wie Protokolldaten ausgewertet werden sollen und welche Protokolle regelmäßig, sporadisch oder nur anlassbezogen auszuwerten sind. Es SOLLTE ständig überwacht werden, ob die Firewall selbst und die darauf betriebenen Dienste korrekt funktionieren. Bei Fehlern oder wenn Grenzwerte überschritten werden, SOLLTE das Betriebspersonal alarmiert werden. Zudem SOLLTEN automatisch Alarmmeldungen generiert werden, die bei festgelegten Ereignissen ausgelöst werden. Protokolldaten oder Statusmeldungen SOLLTEN nur über sichere Kommunikationswege übertragen werden. 

#### NET.3.2.A24 Revision und Penetrationstests

Die Firewall-Struktur SOLLTE regelmäßig auf bekannte Sicherheitsprobleme hin überprüft werden. Es SOLLTEN regelmäßige Penetrationstests und Revisionen durchgeführt werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.3.2.A25 Erweiterter Integritätsschutz für die Konfigurationsdateien(CI)

Stürzt ein System ab, SOLLTE sichergestellt werden, dass keine alten oder fehlerhaften Konfigurationen (unter anderem Access-Listen) benutzt werden. Dies SOLLTE auch gelten, wenn es einem Angreifer gelingt, die Firewall neuzustarten. 

#### NET.3.2.A26 Auslagerung von funktionalen Erweiterungen auf dedizierte Hardware(CIA)

Um das Angriffspotenzial weiter zu minimieren, SOLLTE eine Institution funktionale Erweiterungen der Firewall auf dedizierte Hard- und Software auslagern.

#### NET.3.2.A27 Einsatz verschiedener Firewall-Betriebssysteme und -Produkte in einer mehrstufigen Firewall-Architektur(CI)

In einer mehrstufigen Firewall-Architektur SOLLTEN unterschiedliche Betriebssysteme und -Produkte für die äußeren und inneren Firewalls eingesetzt werden, damit sich eine potenzielle Schwachstelle eines Betriebssystems oder eines Produkts weniger weitreichend auswirkt.

#### NET.3.2.A28 Zentrale Filterung von aktiven Inhalten(CI)

Aktive Inhalte SOLLTEN gemäß den Sicherheitszielen der Institution zentral gefiltert werden. Dafür SOLLTE auch der verschlüsselte Datenverkehr entschlüsselt werden. Die erforderlichen Sicherheitsproxys SOLLTEN es unterstützen, aktive Inhalte zu filtern.

#### NET.3.2.A29 Einsatz von Hochverfügbarkeitslösungen(A)

Paketfilter und Application-Level-Gateway SOLLTEN hochverfügbar ausgelegt werden. Zudem SOLLTEN zwei voneinander unabhängige Zugangsmöglichkeiten zum externen Netz bestehen, z. B. zwei Internetzugänge von unterschiedlichen Providern. Interne und externe Router sowie alle weiteren beteiligten aktiven Komponenten (z. B. Switches), die zum Verlust der Verfügbarkeit führen können, SOLLTEN ebenfalls hochverfügbarausgelegt sein. 

Auch nach einem automatischen Failover SOLLTE die Firewall-Struktur die Sicherheitsanforderungen der Sicherheitsrichtlinie erfüllen (Fail safe bzw. Fail secure).

Die Funktionsüberwachung SOLLTE anhand von zahlreichen Parametern erfolgen und sich nicht auf ein einzelnes Kriterium verlassen. Protokolldateien und Warnmeldungen der Hochverfügbarkeitslösung SOLLTEN regelmäßig kontrolliert werden.

#### NET.3.2.A30 Bandbreitenmanagement für kritische Anwendungen und Dienste(A)

Um Bandbreitenmanagement für kritische Anwendungen und Dienste zu gewährleisten, SOLLTEN Paketfilter mit entsprechender Bandbreitenmanagement-Funktion an Netzübergängen und am Übergang zwischen verschiedenen Sicherheitszonen eingesetzt werden. 

#### NET.3.2.A31 Einsatz von zertifizierten Produkten(CI)

Es SOLLTEN Firewalls mit einer Sicherheits-Evaluierung nach Common Criteria eingesetzt werden, mindestens mit der Stufe EAL4.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Firewall" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSICS112] Next Generation Firewalls - Veröffentlichungen zur Cyber-Sicherheit

  

 Empfehlung von Einsatzmöglichkeiten für den normalen Schutzbedarf, BSI, 04.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/infos/20150407\_BSI\_Empfehlung\_NGFW.htm](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/infos/20150407_BSI_Empfehlung_NGFW.htm)

 
* #### [ISILANA] BSI-Standard zur Internet-Sicherheit (Isi-Reihe):

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [NIST80041] NIST Special Publication 800-41

  

 Guidelines on Firewalls and Firewall Policy, 09.2009  
 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r3.pdf>

 
* #### [TR21022] BSI Technische Richtlinie, Kryptografische Verfahren

  

 Verwendung von Transport Layer Security (TLS), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2017  
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Firewall" von Bedeutung.

* G 0.8 Ausfall oder Störung der Stromversorgung
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

