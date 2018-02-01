1 Beschreibung
--------------

### 1.1 Einleitung

Router und Switches bilden das Rückgrat heutiger IT-Netze. Ein Ausfall eines oder mehrerer dieser Geräte kann zum kompletten Stillstand der gesamten IT-Infrastruktur führen. Sie müssen daher besonders abgesichert werden. 

Router arbeiten auf der OSI Schicht 3 (Netzschicht) und vermitteln Datenpakete anhand der Ziel-IP-Adresse im IP-Header. Router sind in der Lage, Netze mit unterschiedlichen Topographien zu verbinden. Sie werden verwendet, um lokale Netze zu segmentieren oder um lokale Netze über Weitverkehrsnetze zu verbinden. Ein Router identifiziert eine geeignete Verbindung zwischen dem Quellsystem bzw. Quellnetz und dem Zielsystem bzw. Zielnetz. In den meisten Fällen geschieht das, indem er die Datenpakete an den nächsten Router weitergibt. 

Switches arbeiteten ursprünglich auf der OSI-Schicht 2, mittlerweile sind sie jedoch mit unterschiedlichen Funktionen erhältlich. Hersteller kennzeichnen die Geräte meist mit dem OSI-Layer, der unterstützt wird. Dadurch entstanden die Begriffe Layer-2-, Layer-3- und Layer-4-Switch, wobei es sich bei Layer-3- und Layer-4-Switches eigentlich funktional bereits um Router handelt. Die ursprünglich unterschiedlichen Funktionen von Switches und Routern werden somit heute oft auf einem Gerät vereint.

### 1.2 Zielsetzung

Der Baustein beschreibt, wie Router und Switches sicher betrieben werden. 

### 1.3 Abgrenzung

Es ist eine große Auswahl von unterschiedlichen Routern und Switches von verschiedenen Herstellern am Markt verfügbar. Der Baustein beschreibt keine spezifischen Anforderungen für bestimmte Produkte. Er ist so weit wie möglich herstellerunabhängig gehalten. 

Durch die Verschmelzung der Funktionen von Routern und Switches kann der Großteil der Anforderungen sowohl für Router als auch für Switches benutzt werden. Der vorliegende Baustein unterscheidet hier weitgehend nicht zwischen den Gerätearten.

Heute bieten auch nahezu alle Betriebssysteme eine Routing-Funktionalität an. Dieser Baustein benennt keine Anforderungen für aktivierte Routing-Funktionen in Betriebssystemen.

Darüber hinaus werden Aspekte der infrastrukturellen Sicherheit (z. B. geeignete Aufstellung oder Stromversorgung oder Verkabelung) nicht in diesem Baustein aufgeführt, sondern finden sich in den jeweiligen Bausteinen der Schicht INF *Infrastruktur*.

Der vorliegende Baustein beschreibt keine Anforderungen, wie virtuelle Router und Switches abgesichert werden können. Sicherheitsaspekte von virtuellen aktiven Netzkomponenten werden im Baustein NET.1.4 *Netzvirtualisierung* behandelt. Ebenso wird nicht auf eventuell vorhandene Firewall-Funktionen von Routern und Switches eingegangen. Dazu muss zusätzlich der Baustein NET.3.2 *Firewall* umgesetzt werden. Einige Aspekte des Netzdesigns und -managements sind auch für den Einsatz von Routern und Switches von Bedeutung und werden im Rahmen der entsprechenden Anforderungen erwähnt. Weitere Informationen für den Aufbau, das Design und das Management eines Netzes sind in den Bausteinen NET.1.1 *Netzarchitektur und -design* und NET.1.2 *Netzmanagement* zu finden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für *Router und Switches* von besonderer Bedeutung:

### 2 1 Distributed Denial of Service (DDoS)

Bei einem DDoS-Angriff auf ein geschütztes Netz beispielsweise per TCP-SYN-Flooding oder UDP Packet Storm kann aufgrund der vielen Netzverbindungen, die verarbeitet werden müssen, der Router ausfallen. Das kann dazu führen, dass bestimmte Dienste im Local Area Network (LAN) nicht mehr verfügbar sind oder das gesamte LAN ausfällt.

### 2 2 Manipulation

Gelingt es einem Angreifer, unberechtigt auf einen Router oder Switch zuzugreifen, kann er die Geräte neu konfigurieren oder auch zusätzliche Dienste starten. Die Konfiguration lässt sich beispielsweise so verändern, dass Dienste, Clients oder ganze Netzsegmente geblockt werden.

### 2 3 Software-Schwachstellen oder -Fehler

Hersteller von Routern und Switches veröffentlichen regelmäßig Updates und Patches, um Softwarefehler und bekannt gewordene Schwachstellen in ihren Produkten zu beheben. Werden diese jedoch nicht oder zu spät eingespielt, kann der Router oder Switch erfolgreich angegriffen werden. Dadurch ist es möglich, dass Angreifer die Systeme manipulieren, sodass geschäftskritische Daten abfließen, Dienste ausfallen oder ganze Produktionsprozesse still stehen.

### 2 4 Fehlerhafte Konfiguration eines Routers oder Switches

Router und Switches werden mit einer Standardkonfiguration ausgeliefert, in der viele Dienste aktiviert sind. Auch verraten Login-Banner beispielsweise die Modell- und Versionsnummer des Gerätes. Werden Router und Switches mit unsicheren Werkeinstellungen produktiv eingesetzt, kann einfacher unberechtigt auf sie zugegriffen werden. Dies kann dazu führen, dass z. B. Dienste nicht mehr verfügbar sind.

### 2 5 Fehlerhafte Planung und Konzeption

Viele Institutionen planen und konzipieren den Einsatz von Routern und Switches fehlerhaft. So werden unter anderem Geräte beschafft, die nicht ausreichend dimensioniert sind, z. B. hinsichtlich der Port-Anzahl oder der Leistung. In der Folge ist ein Router oder Switch bereits überlastet, wenn er zum ersten Mal eingesetzt wird. Dadurch sind eventuell Dienste oder ganze Netze nicht erreichbar und der Fehler muss aufwändig korrigiert werden. 

### 2 6 Inkompatible aktive Netzkomponenten

Kompatibilitätsprobleme können insbesondere dann entstehen, wenn bestehende Netze um aktive Netzkomponenten anderer Hersteller ergänzt werden oder wenn Netze mit Netzkomponenten unterschiedlicher Hersteller betrieben werden. Werden aktive Netzkomponenten mit unterschiedlichen Implementierungen desselben Kommunikationsverfahrens gemeinsam in einem Netz betrieben, können einzelne Teilbereiche des Netzes, bestimmter Dienste oder sogar das gesamte Netz ausfallen.

### 2 7 MAC-Flooding

Beim MAC-Flooding schickt ein Angreifer viele Anfragen mit wechselnden Quell-MAC-Adressen an einen Switch. Sobald der Switch dann die Limits der MAC-Adressen, die er speichern kann, erreicht hat, fängt er an, sämtliche Anfragen an alle IT-Systeme im Netz zu schicken. Dadurch kann der Angreifer den Netzverkehr einsehen. 

### 2 8 Spanning-Tree-Angriffe

Bei Spanning-Tree-Angriffen versendet ein Angreifer sogenannte Bridge Protocol Data Units (BPDUs) mit dem Ziel, die Switches dazu zu bringen, seinen eigenen (bösartigen) Switch als Root Bridge anzusehen. Dadurch wird der Netzverkehr über den Switch des Angreifers umgeleitet, sodass er alle über ihn versendeten Informationen mitschneiden kann. In der Folge kann er DDoS-Attacken initiieren und durch falsche BPDUs das Netz dazu zwingen, die Spanning-Tree-Topologie neu aufzubauen, wodurch das Netz ausfallen kann.

### 2 9 GARP-Attacken

Bei Gratuitous-ARP-(GARP)-Attacken sendet der Angreifer unaufgeforderte ARP-Antworten an bestimmte Opfer oder an alle IT-Systeme im gleichen Subnetz. In dieser gefälschten ARP-Antwort trägt der Angreifer seine MAC-Adresse als Zuordnung zu einer fremden IP-Adresse ein und bringt das Opfer dazu, seine ARP-Tabelle so zu verändern, dass der Netzverkehr nun zum Angreifer anstatt zum validen Ziel gesendet wird. Dadurch kann er die Kommunikation zwischen den Opfern mitschneiden oder sie manipulieren.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von *Routern und Switches* aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist er dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.3.1.A1 Sichere Grundkonfiguration eines Routers oder Switches

Bevor ein Router oder Switch eingesetzt wird, MUSS er sicher konfiguriert werden. Die Geräte DÜRFEN NUR von dafür autorisierten Personen installiert und konfiguriert werden. Alle Konfigurationsänderungen SOLLTEN nachvollziehbar dokumentiert sein (siehe NET.3.2.A9 *Betriebsdokumentationen*). Die Integrität der Konfigurationsdateien MUSS geeignet geschützt werden. Zugangspasswörter MÜSSEN verschlüsselt gespeichert werden.

Router und Switches MÜSSEN so konfiguriert sein, dass nur zwingend erforderliche Dienste, Protokolle und funktionale Erweiterungen genutzt werden. Nicht benötigte Dienste, Protokolle und funktionale Erweiterungen MÜSSEN deaktiviert oder ganz deinstalliert werden. Ebenfalls MÜSSEN nicht benutzte Schnittstellen auf Routern und Switches deaktiviert oder zumindest einem dafür eingerichteten *Unassigned-VLAN* zugeordnet werden.

Wenn funktionale Erweiterungen benutzt werden, MÜSSEN die Sicherheitsrichtlinien der Institution weiterhin erfüllt sein. Auch SOLLTE begründet und dokumentiert werden, warum solche Erweiterungen eingesetzt werden. 

Informationen über den internen Konfigurations- und Betriebszustand MÜSSEN nach außen verborgen werden. Unnötige Auskunftsdienste MÜSSEN deaktiviert werden.

Bevor Router und Switches in Betrieb genommen werden, MÜSSEN die Standard-Benutzerkonten geändert werden. Passwörter dieser Konten MÜSSEN geändert werden. Nicht benutzte Benutzerkonten MÜSSEN deaktiviert werden. Entsprechend dem Rechte- und Rollenkonzept MÜSSEN anschließend die vorgesehenen Benutzerkonten und -rollen eingerichtet werden.

#### NET.3.1.A2 Einspielen von Updates und Patches

Die Verantwortlichen MÜSSEN sich über bekannt gewordene Schwachstellen informieren. Updates und Patches MÜSSEN so schnell wie möglich eingespielt werden. Vorab SOLLTE auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. Solange keine Patches für bekannte Schwachstellen verfügbar sind, MÜSSEN andere geeignete Maßnahmen getroffen werden, um Router und Switches zu schützen.

Es MUSS darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden. Sofern vom Hersteller angeboten, SOLLTEN die Update-Prüfsummen verglichen bzw. die digitalen Signaturen überprüft werden. 

#### NET.3.1.A3 Restriktive Rechtevergabe

Es MUSS geregelt werden, wer auf einen Router oder Switch zugreifen darf. Dabei DÜRFEN immer NUR so viele Zugriffsrechte vergeben werden, wie sie für die jeweiligen Aufgaben erforderlich sind (Minimalprinzip). Nicht mehr benötigte Benutzerkonten MÜSSEN entfernt werden. Es MUSS sichergestellt werden, dass mit Administrator-Rechten (bzw. Root-Rechten) nur gearbeitet wird, wenn es notwendig ist.

#### NET.3.1.A4 Schutz der Administrationsschnittstellen

Alle Administrations- und Management-Zugänge der Router und Switches MÜSSEN auf einzelne Quell-IP-Adressen bzw. -Adressbereiche eingeschränkt werden. Es MUSS sichergestellt sein, dass aus nicht-vertrauenswürdigen Netzen heraus nicht direkt auf die Administrationsschnittstellen zugegriffen werden kann.

Um Router und Switches zu administrieren bzw. zu überwachen, SOLLTEN ausreichend verschlüsselte Protokolle eingesetzt werden. Sollte dennoch auf unverschlüsselte und damit unsichere Protokolle zurückgegriffen werden, MUSS für die Administration ein eigenes Administrationsnetz (Out-of-Band-Management) genutzt werden. Die Managementschnittstellen und die Administrationsverbindungen MÜSSEN durch eine separate Firewall geschützt werden. Für die Schnittstellen MÜSSEN geeignete Zeitbeschränkungen vorgegeben werden.

Alle für das Management-Interface nicht benötigten Dienste MÜSSEN deaktiviert werden. Verfügt eine Netzkomponente über eine dedizierte Hardwareschnittstelle, MUSS der unberechtigte Zugriff auf diese geeignet unterbunden werden.

#### NET.3.1.A5 Schutz vor Fragmentierungsangriffen

Am Router und Layer-3-Switch MÜSSEN Schutzmechanismen aktiviert sein, um IPv4- sowie IPv6-Fragmentierungsangriffe abzuwehren. 

#### NET.3.1.A6 Notfallzugriff auf Router und Switches

Es MUSS für die Administratoren immer möglich sein, direkt auf Router und Switches zuzugreifen, sodass diese weiterhin lokal administriert werden können, auch wenn das gesamte Netz ausfällt.

#### NET.3.1.A7 Protokollierung bei Routern und Switches

Ein Router oder Switch MUSS so konfiguriert werden, dass er unter anderem folgende Ereignisse protokolliert:

* Konfigurationsänderungen (möglichst automatisch),
* Reboot,
* Systemfehler,
* Statusänderungen pro Interface, System und Netzsegment,
* Login-Fehler (zumindest dann, wenn sie wiederholt auftreten)
Die Verantwortlichen MÜSSEN darauf achten, dass bei der Protokollierung alle rechtlichen Rahmenbedingung eingehalten werden. Änderungen an der Konfiguration SOLLTEN zudem automatisch protokolliert werden.

#### NET.3.1.A8 Regelmäßige Datensicherung

Die Konfigurationsdateien von Routern und Switches MÜSSEN regelmäßig gesichert werden. Die Sicherungskopien MÜSSEN so abgelegt werden, dass im Notfall darauf zugegriffen werden kann.

#### NET.3.1.A9 Betriebsdokumentationen

Die wichtigsten betrieblichen Aufgaben eines Routers oder Switches MÜSSEN geeignet dokumentiert werden. Es SOLLTEN alle Konfigurationsänderungen sowie sicherheitsrelevante Aufgaben dokumentiert werden. Die Dokumentation SOLLTEN vor unbefugten Zugriffen geschützt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Router und Switches. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.3.1.A10 Erstellung einer Sicherheitsrichtlinie [Informationssicherheitsbeauftragter (ISB)]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Sicherheitsrichtlinie erstellt werden, in der nachvollziehbar Anforderungen und Vorgaben beschrieben sind, wie Router und Switches sicher betrieben werden können. Die Richtlinie SOLLTE allen Administratoren bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von den Anforderungen abgewichen, SOLLTE das mit dem ISB abgestimmt und dokumentiert werden. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse SOLLTEN geeignet dokumentiert werden.

#### NET.3.1.A11 Beschaffung eines Routers oder Switches

Bevor Router oder Switches beschafft werden, SOLLTE eine Anforderungsliste erstellt werden, anhand derer die am Markt erhältlichen Produkte bewertet werden. Es SOLLTE darauf geachtet werden, dass das von der Institution angestrebte Sicherheitsniveau mit den zu beschaffenden Geräten erreicht werden kann. Grundlage für die Beschaffung SOLLTEN daher die Anforderungen aus der Sicherheitsrichtlinie sein.

#### NET.3.1.A12 Erstellung einer Konfigurations-Checkliste für Router und Switches

ES SOLLTE eine Konfigurations-Checkliste erstellt werden, anhand derer die wichtigsten sicherheitsrelevanten Einstellungen auf Routern und Switches geprüft werden können. Da die sichere Konfiguration stark vom Einsatzzweck abhängt, SOLLTEN die unterschiedlichen Anforderungen der Geräte in der Konfigurations-Checkliste berücksichtigt werden.

#### NET.3.1.A13 Administration über ein gesondertes Managementnetz

Router und Switches SOLLTEN ausschließlich über ein separates Managementnetz (Out-of-Band-Management) administriert werden. Eine eventuell vorhandene Administrationsschnittstelle über das eigentliche Datennetz (In-Band) SOLLTE deaktiviert werden. Die verfügbaren Sicherheitsmechanismen der eingesetzten Managementprotokolle zur Authentisierung, Integritätssicherung und Verschlüsselung SOLLTEN aktiviert und alle unsicheren Managementprotokolle deaktiviert werden (siehe NET.1.2 *Netz-Management*).

#### NET.3.1.A14 Schutz vor Missbrauch von ICMP-Nachrichten

ES SOLLTE sichergestellt sein, dass die Protokolle ICMP und ICMPv6 restriktiv gefiltert werden.

#### NET.3.1.A15 Bogon- und Spoofing-Filterung

Es SOLLTE verhindert werden, dass Angreifer mithilfe gefälschter, reservierter oder noch nicht zugewiesener IP-Adressen in die Router und Switches eindringen können.

#### NET.3.1.A16 Schutz vor „IPv6 Routing Header Type-0“-Angriffen

Beim Einsatz von IPv6 SOLLTEN Mechanismen eingesetzt werden, die Angriffe auf den Routing-Header des Type-0 erkennen und verhindern.

#### NET.3.1.A17 Schutz vor DoS- und DDoS-Angriffen

Es SOLLTEN Mechanismen eingesetzt werden, die hochvolumige Angriffe sowie TCP-State-Exhaustion-Angriffe erkennen und abwehren. 

#### NET.3.1.A18 Einrichtung von Access Control Lists

Der Zugriff auf Router und Switches SOLLTE mithilfe von Access Control Lists (ACL) definiert werden. In der ACL SOLLTE anhand der Sicherheitsrichtlinie der Institution festgelegt werden, über welche IT-Systeme oder Netze mit welcher Methode auf einen Router oder Switch zugegriffen werden darf. Für den Fall, dass keine spezifischen Regeln existieren, SOLLTE generell der restriktivere Whitelist-Ansatz bevorzugt werden.

#### NET.3.1.A19 Sicherung von Switch-Ports

Die Ports eines Switches SOLLTEN vor unberechtigten Zugriffen geschützt werden.

#### NET.3.1.A20 Sicherheitsaspekte von Routing-Protokollen

Router SOLLTEN sich authentisieren, wenn sie Routing-Informationen austauschen oder Updates für Routing-Tabellen verschicken. Es SOLLTEN ausschließlich Routing-Protokolle eingesetzt werden, die das unterstützen.

Dynamische Routing-Protokolle SOLLTEN ausschließlich in sicheren Netzen verwendet werden. Sie DÜRFEN NICHT in demilitarisierten Zonen (DMZ) eingesetzt werden. In DMZs SOLLTEN stattdessen statische Routen eingetragen werden.

#### NET.3.1.A21 Identitäts- und Berechtigungsmanagement in der Netzinfrastruktur

Router und Switches SOLLTEN an ein zentrales Identitäts- und Berechtigungsmanagement angebunden werden (siehe ORP.4 *Identitäts- und Berechtigungsmanagement)*. 

#### NET.3.1.A22 Notfallvorsorge bei Routern und Switches

Um in Störungssituationen effektiv und schnell reagieren zu können, SOLLTEN Diagnose und Fehlerbehebungen im Vorfeld geplant und vorbereitet werden. Für typische Ausfallszenarien SOLLTEN entsprechende Handlungsanweisungen definiert werden.

Die Notfallplanungen für Router und Switches SOLLTEN mit der übergreifenden Störungs- und Notfallvorsorge abgestimmt sein und sich am allgemeinen Notfallvorsorgekonzept (siehe DER.4 *Notfallmanagement*) orientieren. Es SOLLTE sichergestellt sein, dass die Dokumentationen zur Notfallvorsorge und die darin enthaltenen Handlungsanweisungen in Papierform existiert. Die in der Notfallvorsorge notwendigen Vorgehensbeschreibungen SOLLTEN regelmäßig geprobt werden.

#### NET.3.1.A23 Revision und Penetrationstests

Router und Switches SOLLTEN regelmäßig auf bekannte Sicherheitsprobleme hin überprüft werden. Auch SOLLTEN regelmäßig Revisionen durchgeführt werden. Dabei SOLLTE z. B. geprüft werden, ob der Istzustand der festgelegten sicheren Grundkonfiguration entspricht. Die Ergebnisse SOLLTEN nachvollziehbar dokumentiert und mit dem Sollzustand abgeglichen werden. Abweichungen SOLLTE nachgegangen werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### NET.3.1.A24 Einsatz von Netzzugangskontrollen(IA)

Es SOLLTE eine Port-based Access Control nach IEEE 802.1x auf Basis von EAP-TLS implementiert werden. Es SOLLTE NICHT eine Implementierung nach den Standards IEEE 802.1x-2001 und IEEE 802.1x-2004 erfolgen.

#### NET.3.1.A25 Erweiterter Integritätsschutz für die Konfigurationsdateien(I)

Stürzt ein Router oder Switch ab, SOLLTE sichergestellt werden, dass bei der Wiederherstellung bzw. beim Neustart keine alten oder fehlerhaften Konfigurationen (unter anderem ACLs) benutzt werden. 

#### NET.3.1.A26 Hochverfügbarkeit(A)

Die Realisierung einer Hochverfügbarkeitslösung DARF NICHT den Betrieb der Router und Switches bzw. deren Sicherheitsfunktionen behindern oder das Sicherheitsniveau senken. Router und Switches SOLLTEN redundant ausgelegt werden. Dabei SOLLTE darauf geachtet werden, dass die Sicherheitsrichtlinie der Institution eingehalten wird. 

#### NET.3.1.A27 Bandbreitenmanagement für kritische Anwendungen und Dienste(A)

Um Bandbreitenmanagement für kritische Anwendungen und Dienste zu gewährleisten, SOLLTEN Router und Switches Funktionen enthalten und einsetzen, mit denen sich die Applikationen erkennen und Bandbreiten priorisieren lassen.

#### NET.3.1.A28 Einsatz von zertifizierten Produkten(CI)

Es SOLLTEN Router und Switches mit einer Sicherheits-Evaluierung nach Common Criteria eingesetzt werden, mindestens mit der Stufe EAL4.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Router und Switches" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [8021AD] IEEE 802.1ad

  

 Provider Bridges, 2006  
 <http://www.ieee802.org/1/pages/802.1ad.html>

 
* #### [8021AE] IEEE 802.1AE

  

 Media Access Control (MAC) Security, 2006  
 <http://www.ieee802.org/1/pages/802.1ae.html>

 
* #### [ISI] BSI-Standards zur Internet Sicherheit (Isi-Reihe)

  

 BSI, (zuletzt abgerufen am 28.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Reihe\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-Reihe_node.html)

 
* #### [NIST80046] NIST Special Publication 800-46 Revision 2

  

 Guide to Enterprise Telework, Remote Access and Bring Your Own Device (BYOD) Security, NIST, 07.2016  
 <http://dx.doi.org/10.6028/NIST.SP.800-46r2>

 
* #### [RFC6165] Extensions to IS-IS for Layer-2 Systems

  

 RFC, 2011  
 <https://tools.ietf.org/html/rfc6165>

 
* #### [RFC7348] Virtual EXtensible Local Area Network (VXLAN)

  

 A Framework for Overlaying Virtualized Layer 2 Networks over Layer 3 Networks, 2014  
 <https://tools.ietf.org/html/rfc7348>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Router und Switches" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
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
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

