Table of content

[toc]

1 Beschreibung
--------------

### 1.1 Einleitung

In diesem Baustein werden Geräte mit Funktionalitäten aus dem Bereich Internet of Things (IoT) betrachtet. Dies sind im Gegensatz zu "klassischen" IT-Systemen "intelligente" Gegenstände, die zusätzliche "smarte" Funktionen enthalten. IoT-Geräte werden in der Regel an Datennetze angeschlossen, in vielen Fällen drahtlos, und können sogar oft auf das Internet zugreifen und darüber erreicht werden. Hierdurch können sie Auswirkungen auf die Informationssicherheit des gesamten Informationsverbunds haben. 

IoT-Geräte können in Institutionen vorhanden sein, weil sie durch Mitarbeiter oder Externe mitgebracht werden, z. B. Smartwatches oder Wearables. In vielen Institutionen werden aber auch IoT-Geräte beschafft und betrieben, z. B. Geräte wie Brand-, Gas- und andere Warnmelder, Kaffeemaschinen oder Elemente der Gebäudesteuerung wie Kameras und HVAC (Heating, Ventilation and Air Conditioning). 

Generell kann zwischen direkt adressierbaren IoT-Geräten und IoT-Geräten, die eine zentrale Steuereinheit voraussetzen, unterschieden werden. Direkt adressierbare Geräte werden in der Regel mit einer eigenen IP-Adresse an ein Datennetz angeschlossen und können autark agieren oder durch eine zentralen Steuereinheit verwaltet werden. Es gibt aber auch IoT-Geräte, die ausschließlich direkt mit Steuereinheiten kommunizieren, z. B. über Funknetze wie Bluetooth oder ZigBee, und somit nicht direkt an Datennetze angeschlossen werden. Die Reichweite dieser Funkverbindungen kann, wenn vorgesehen, über ein separates, vermaschtes Netz vergrößert werden, indem jedes Gerät mit jedem Gerät eine Funkverbindung aufbaut.

### 1.2 Lebenszyklus

**Planung und Konzeption**

In der Planungs- und Konzeptionsphase soll der Einsatz der IoT-Geräte innerhalb der Institution definiert werden. Hierbei muss der Einsatz von IoT-Geräten sorgfältig dokumentiert und geplant werden (siehe *SYS.4.4.M6 Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution* sowie *SYS.4.4.M7 Planung des Einsatzes von IoT-Geräten*).

**Beschaffung**

Um geeignete IoT-Geräte für die Institution auswählen zu können, müssen die Geräte hierzu bezüglich der Sicherheitskriterien, z. B. Update-Funktionen, Update-Prozess oder Authentisierung-Varianten, gesichtet werden (siehe *SYS.4.4.M1 Einsatzkriterien für IoT-Geräte*). Anderweitige Kriterien, wie z. B. organisatorische Randbedingungen oder materielle Sicherheit, sollten ebenso berücksichtigt werden (siehe *SYS.4.4.M8 Beschaffungskriterien für IoT-Geräte).*

**Umsetzung **

Nachdem Planung und Beschaffung abgeschlossen sind, müssen die Geräte anhand der Sicherheitsanforderungen installiert und konfiguriert werden. Bevor die IoT-Geräte installiert werden, sollten Einsatzumgebung und Stromversorgung geprüft werden, um den sicheren Betrieb der Geräte zu gewährleisten (siehe *SYS.4.4.M21 Einsatzumgebung und Stromversorgung).* Bei der Installation sollten verschiedene Einstellungsmöglichkeiten berücksichtigt und vorgenommen werden, die z. B. den Zugriff auf die Geräte zu regeln und abzusichern (siehe *SYS.4.4.M10 Sichere Installation und Konfiguration von IoT-Geräten).*

**Betrieb**

Bevor IoT-Geräte in Betrieb genommen werden, sollte deren Einsatz, anhand der Prüfung der Installations- und Konfigurationsdokumentation, freigegeben werden. Während des laufenden Betriebs ist neben der Protokollierung wichtiger und sicherheitsrelevanter Ereignisse auch die Überwachung des Netzverkehrs der IoT-Geräte von Wichtigkeit (siehe *SYS.4.4.M17 Überwachung des Netzverkehrs von IoT-Geräten* sowie *SYS.4.4.M18 Protokollierung sicherheitsrelevanter Ereignisse bei IoT-Geräten*).

**Aussonderung **

Wenn IoT-Geräte ausgesondert werden, sollte sichergestellt sein, dass keine wichtigen oder sensitiven Daten auf den IoT-Geräten zurück bleiben (S*YS.4.4.M20 Geregelte Außerbetriebnahme von IoT-Geräten*).

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Allgemeines IoT-Gerät" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### SYS.4.4.M1 Einsatzkriterien für IoT-Geräte

Viele auf dem Markt vorhandene IoT-Geräte weisen wenig bis gar keine Sicherheitsmechanismen auf und enthalten teilweise diverse Schwachstellen. Damit IoT-Geräte in Institutionen eingesetzt werden können, müssen sie ein Minimum an Sicherheitskriterien erfüllen.

Die Geräte müssen Update-Funktionen besitzen und der Hersteller muss einen Update-Prozess anbieten. Wenn IoT-Lösungen ein unzureichendes oder fehlendes Patchmanagement mitbringen, können keine Schwachstellen behoben werden. Ersatzweise müssten die Sicherheitslücken anderweitig abgeschirmt werden. Dies kann sehr aufwendig werden und auch das ganze Nutzungskonzept eines IoT-Gerätes ad absurdum führen.

Ein weiteres großes Problem bei IoT-Geräten sind voreingestellte und teilweise sogar fest codierte Standard-Passwörter. Geräte, bei denen keine Authentisierung möglich ist oder bei denen Standard-Passwörter nicht geändert werden können, dürfen nicht eingesetzt werden. 

Wenn sich im laufenden Betrieb herausstellt, dass in einem Gerät Zugangsdaten fest codiert sind, muss es vom Netz genommen werden. Dies gilt auch, wenn Zugangsmöglichkeiten mit Missbrauchspotential erst später bekannt werden, etwa zusätzliche Schnittstellen für den Fernzugriff (wie z. B. Telnet) oder Masterpasswörter des Herstellers, und sich diese nicht zuverlässig abschalten oder verhindern lassen.

#### SYS.4.4.M2 Authentisierung

In Unternehmen und Behörden sollten nur IoT-Geräte eingesetzt werden, die eine Authentisierung ermöglichen. Diese muss aktiviert sein. Werden hierfür Passwörter verwendet, müssen sichere Passwörter benutzt werden. Hierfür sollte es eine Passwort-Richtlinie geben (siehe auch ORP.4 Identitäts- und Berechtigungsmanagement). Grundsätzlich müssen die gewählten Passwörter komplex genug sein, geheim gehalten und regelmäßig gewechselt werden. Voreingestellte Passwörter müssen bei Inbetriebnahme geändert werden, sofern möglich, bevor ein Gerät online geht. Zusätzlich empfiehlt sich die Verwendung von alternativen Authentisierungsmechanismen, wie z. B. zertifikatsbasierte Authentisierung. Leider bieten nicht alle IoT-Geräte entsprechende Möglichkeiten.

#### SYS.4.4.M3 Regelmäßige Aktualisierung

Während des Betriebes der IoT-Geräte muss regelmäßig überprüft werden, ob neue Updates/Patches für die eingesetzten IoT-Geräte und zugehörige Komponenten wie Sensoren oder Management-Systeme zur Verfügung stehen, z. B. über einschlägige Webseiten mit Sicherheitsinformationen oder beim Hersteller. Vorhandene Patches und Updates müssen zeitnah installiert werden oder anderweitige Sicherheitsmaßnahmen ergriffen werden, wenn keine Patches zur Verfügung stehen. Im äußersten Fall dürfen die Geräte bei bekannten, nicht behebbaren Schwachstellen nicht mehr betrieben werden. Zusätzlich zur Firmware der IoT-Geräte sollten auch Drittkomponenten, wie z. B. Administrations- oder Managementsoftware, auf Aktualität überprüft werden. Falls neue Updates verfügbar sind, sind diese zeitnah einzuspielen. Generell muss darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden, in erster Linie ist dies der jeweilige Hersteller selbst.

#### SYS.4.4.M4 Aktivieren von Autoupdate-Mechanismen

Automatische Update-Mechanismen (Autoupdate) stellen eine regelmäßige Aktualisierung der Software auf den IoT-Geräten sicher. In kritischen Umgebungen oder bei hohen Ansprüchen vor allem an die Verfügbarkeit sollte jedoch die Durchführbarkeit einer manuellen Wartung vorrangig geprüft werden, da automatische, ungetestete Updates unerwartete Auswirkungen oder gar Ausfälle zur Folge haben können.

Auch bei automatischen Updates ist es wichtig, dass diese aus vertrauenswürdigen Quellen bezogen werden und der Download geeignet abgesichert ist, etwa durch entsprechende Authentisierung und eine Transportverschlüsselung (z. B. HTTPS). Es darf nicht möglich sein, dass ein Angreifer durch den Missbrauch von Updates (etwa durch Man-in-the-Middle-Angriffe) Zugriff auf die IoT-Geräte erlangen kann.

#### SYS.4.4.M5 Einschränkung des Netzzugriffs

Um den Netzzugriff der IoT-Geräte auf ein Minimum zu beschränken, sollten mittels einer Firewall nur zuvor definierte ein- und ausgehende Verbindungen erlaubt werden. Insgesamt sind ausgehende Verbindungen zu minimieren, sowohl im internen Netz als auch zum Internet hin.

Für ausgehende Verbindungen sollten die validen Ziele einer Verbindung, wie z. B. Update-Server des Herstellers, Speicherort der Videodaten und Managementsystem, konfiguriert werden. Ob und wie IoT-Geräte die Server des Herstellers kontaktieren müssen, um die Verfügbarkeit von Updates zu prüfen, sollte in der Produktdokumentation recherchiert werden.

Sollte eine Erreichbarkeit der IoT-Geräte von außen (d. h. aus dem Internet eingehend) erforderlich sein, so sollte dies nur mit hinreichender Authentisierung erfolgen.

Die Freigabe von extern eingehenden Verbindungen im Router sollte vermieden werden. Bei der Inbetriebnahme von IoT-Geräten muss außerdem sichergestellt werden, dass die UPnP-Funktion an allen Routern deaktiviert ist. 

Am Perimeter (Router, Firewall) darf auf keinen Fall der Zugriff über Telnet (Port 23) von außen freigegeben werden. 

Am Perimeter darf der Zugriff über SSH (Port 22) nur freigegeben werden, wenn dieser mit hinreichend sicheren individuellen Passwörtern geschützt ist. Eine höhere Sicherheit wird erreicht, wenn der Zugriff nicht über Benutzername und Passwort, sondern durch ein Softwarezertifikat gesichert wird. Auch hier sollte nach außen nicht einer der standardmäßig verwendeten Ports (22, 1022, 2222) genutzt werden, sondern ein Zufallswert im Bereich 10000 bis 65535.

Gegebenenfalls kann der Zugriff zusätzlich durch die Verwendung von VPN weiter abgesichert werden. Bei der Verwendung von VPN ist darauf zu achten, dass ausreichend starke kryptografische Verfahren und entsprechende Schlüssellängen verwendet werden.

Es empfiehlt sich auch, die IoT-Geräte in einem separaten physischen Netzbereich bzw. innerhalb eines separaten Virtual Local Area Networks (VLANs) zu betreiben, um ein laterales Ausbreiten bei einer Kompromittierung der IoT-Geräte zu vermeiden.

Basierend auf einem gepflegten Assetmanagement-System können folgende Maßnahmen ungewollte Kommunikation verhindern:

* Verkehrskontrolle an Netzübergängen, z. B. durch Regelwerke auf Firewalls und Access Control Lists (ACLs) auf Routern
* Restriktive Konfiguration des Routings auf IoT-Geräten und Sensoren, insbesondere die Unterdrückung von Default-Routen
* Signaturen auf Intrusion-Prevention-Systemen (IPS)
* Zusammenfassung der IoT-Geräte und Sensoren in einem eigenen Netzsegment, welches ausschließlich mit dem Netzsegment für das Management kommunizieren darf
* Konfiguration von Virtual Private Networks (VPNs) zwischen den IoT-Geräten und Sensor-Netzen und den Management-Netzen
* Deaktivierung der UPnP-Funktion an allen Routern
Abhängig vom Einsatzort der IoT-Geräte sollte ein physischer Zugriffsschutz umgesetzt werden. Dieser schützt nicht nur vor Vandalismus, sondern auch vor einer Veränderung der Konfiguration, die häufig durch das Zurücksetzen auf den Werkszustand ermöglicht wird.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Allgemeines IoT-Gerät".

#### SYS.4.4.M6 Aufnahme von IoT-Geräten in die Sicherheitsrichtlinie der Institution

Die Sicherheitsvorgaben für IoT-Geräte ergeben sich aus der institutionsweiten Sicherheitsrichtlinie. Ausgehend von der allgemeinen Richtlinie müssen die Anforderungen für den gegebenen Kontext konkretisiert werden und in einer Sicherheitsrichtlinie für die jeweilige Gruppe von IoT-Geräten zusammengefasst werden. In diesem Zusammenhang ist zu prüfen, ob neben der institutionsweiten Sicherheitsleitlinie weitere übergeordnete Vorgaben wie IT-Richtlinien, Passwortrichtlinien oder Vorgaben zur Internet-Nutzung zu berücksichtigen sind.

Die Sicherheitsrichtlinie muss allen Fachverantwortlichen und anderen Personen, die an der Beschaffung und dem Betrieb der IoT-Geräte beteiligt sind, bekannt sein und Grundlage für deren Arbeit sein. Wie bei allen Richtlinien sind ihre Inhalte und ihre Umsetzung im Rahmen einer übergeordneten Revision regelmäßig zu prüfen.

Die Sicherheitsrichtlinie sollte das generell zu erreichende Sicherheitsniveau spezifizieren und grundlegende Festlegungen treffen. Um die Übersichtlichkeit zu verbessern, kann es sinnvoll sein, für verschiedene Einsatzgebiete gesonderte Sicherheitsrichtlinien zu entwickeln.

Bei der Erstellung einer Sicherheitsrichtlinie ist es empfehlenswert, so vorzugehen, dass zunächst ein Maximum an Forderungen und Vorgaben für die Sicherheit der IoT-Geräte aufgestellt wird. Diese können anschließend den tatsächlichen Gegebenheiten angepasst werden. Idealerweise wird so erreicht, dass alle notwendigen Aspekte berücksichtigt werden. Für jede im zweiten Schritt verworfene oder abgeschwächte Vorgabe sollte der Grund für die Nicht-Berücksichtigung dokumentiert werden. Während die Sicherheitsrichtlinie für IoT-Geräte formuliert wird, ist es auch wichtig, eine Balance zwischen Sicherheit und Funktionalität zu finden. 

#### SYS.4.4.M7 Planung des Einsatzes von IoT-Geräten

Eine grundlegende Voraussetzung dafür, dass IoT-Geräte sicher betrieben werden können, ist ein angemessenes Maß an Planung im Vorfeld. Die Planung betrifft dabei nicht nur Aspekte, die klassischerweise mit dem Begriff Informationssicherheit verknüpft werden, sondern auch Aspekte der physischen, materiellen und funktionalen Sicherheit ebenso wie normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen.

In einem Grobkonzept sollten beispielsweise folgende typische Fragestellungen behandelt werden:

* Welche Aufgaben sollen die IoT-Geräte erfüllen? Auf welche Dienste muss von den IoT-Geräten zugegriffen werden können? Gibt es besondere Anforderungen an die Verfügbarkeit der IoT-Geräte oder an die Vertraulichkeit oder Integrität der gespeicherten oder verarbeiteten Daten?
* Welche Anforderungen an die IoT-Geräte ergeben sich aus den allgemeinen Anforderungen?
Es wird empfohlen, ein oder mehrere generische Anforderungsprofile (beispielsweise "Allgemeine IoT-Geräte", "Kameras" oder "IoT-Geräte zur Gebäudesteuerung") zu erstellen, die bei konkreten Planungen als Grundlage dienen können.

Die folgenden Teilkonzepte sollten bei der Planung berücksichtigt werden:

* Authentisierung: Welche Art der Benutzer-Authentisierung soll genutzt werden? Ist es erforderlich, Benutzer einzurichten?
* Administration: Wie sollen die IoT-Geräte administriert werden? Werden alle Einstellungen lokal vorgenommen oder sollen bzw. können die IoT-Geräte in ein zentrales Administrations- und Konfigurationsmanagement integriert werden?
* Netzdienste und Netzanbindung: Die Netzanbindung der IoT-Geräte sollte geplant werden. Hier sollten vor allem die notwendigen Einschränkungen und Überwachungsmaßnahmen geplant werden.
* Protokollierung: Auch bei IoT-Geräten spielt die Protokollierung eine wichtige Rolle, beispielsweise bei der Diagnose und Behebung von Störungen oder bei der Erkennung und Aufklärung von Angriffen. Sinnvollerweise sollte bereits in der Planungsphase festgelegt werden, wie und zu welchen Zeitpunkten Protokolldaten ausgewertet werden sollen.
Alle Entscheidungen, die in der Planungsphase getroffen wurden, müssen so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Dabei ist zu beachten, dass meist andere Personen neben dem Autor diese Informationen auswerten müssen. Daher ist auf passende Strukturierung und Verständlichkeit zu achten. 

#### SYS.4.4.M8 Beschaffungskriterien für IoT-Geräte [Informationssicherheitsbeauftragter (ISB), Beschaffungsstelle]

Schon bei der Produktwahl sollten nicht nur das Preis-Leistungs-Verhältnis betrachtet werden, sondern auch Aspekte der Informationssicherheit. Hier spielt vor allem die angebotene Funktionalität des Produktes und die Unterstützung durch den Herstellers eine wichtige Rolle. Der ISB sollte auch bei Beschaffungen von Geräten, die keine offensichtliche IT-Funktionalität haben, beteiligt werden, um einschätzen zu können, ob diese in die Sicherheitskonzeption der Institution eingebunden werden müssen.

Grundsätzlich ist von der Verwendung von IoT-Geräten mit einem Cloud-Konzept abzuraten. In diesem Falle fließen sensible Daten über Dritte (z. B. Kamerahersteller) und werden dort für einen Zugriff über das Internet gespeichert. Auch die Verwendung von WLAN – insbesondere in kritischen Einsatzbereichen – sollte vermieden werden, sofern dies die Einsatzbedingungen erlauben.

Ein grundlegendes Ziel zum sicheren Einsatz von IoT-Geräten ist die Minimierung der Angriffsfläche. Um diese von Beginn an gering zu halten, empfiehlt es sich, IoT-Geräte zu beschaffen, auf denen nur die für den konkreten Einsatzzweck erforderlichen Dienste/Ports vorhanden sind. Alternativ sollte es möglich sein, nicht benötigte Dienste zu deaktivieren. Ist auch dies nicht möglich, müssen entsprechende Einschränkungen bei der Inbetriebnahme auf Netzebene (z. B. Firewall) vorgenommen werden, um die Verwendung von nicht benötigten Diensten zu verhindern.

Um eine vertrauliche Übertragung von Nutz- und Konfigurationsdaten zu gewährleisten, sollte das IoT-Gerät ein auf Verschlüsselung basierendes Protokoll (z. B. SSL/TLS bzw. SSH) unterstützen. Bietet das Produkt selbst keine Verschlüsselung, muss dies bei der Inbetriebnahme, z. B. über ein Virtual Private Network (VPN), flankierend umgesetzt werden.

Sofern der Einsatzzweck dies erfordert, sollten die IoT-Geräte ein differenziertes Rollen-/Rechtekonzept für unterschiedliche Benutzer bereitstellen.

Weiterhin muss der Hersteller für einen hinreichend langen Zeitraum die Bereitstellung von Patches bzw. Updates gewährleisten. Dies wird meist mit End Of Service (EOS) beschrieben – nicht zu verwechseln mit End Of Life (EOL), was das Ende der Herstellung und des Verkaufs eines Produktes bezeichnet.

IoT-Geräte werden häufig in Zusammenhang mit übergeordneten Systemen beschafft, z.B. Gebäudesteuerungssystemen. Zusammen mit der reinen Hardware und Firmware können auch noch zusätzliche Komponenten und Leistungen beschafft werden.

Werden bei der Beschaffung von IoT-Geräten Fehler gemacht, so kann dies negative Folgen auf den sicheren Betrieb des übergeordneten Systems oder sogar des gesamten Informationsverbunds haben. Bevor ein IoT-Gerät beschafft wird, muss daher eine Anforderungsliste erstellt werden, anhand derer die in Frage kommenden Geräte bewertet werden. Aufgrund der Bewertung kann dann eine fundierte Kaufentscheidung erfolgen, die sicherstellt, dass das IoT-Gerät im praktischen Betrieb den Sicherheitsanforderungen genügt. Die Anforderungsliste sollte im Wesentlichen die im Folgenden dargestellten sicherheitsrelevanten Bereiche und Kriterien umfassen.

**Organisatorische Randbedingungen**

Die folgenden Aspekte sollten bei der Beschaffung berücksichtigt werden:

* Kann ein effektiver Prozess zur Versorgung mit sicherheitsrelevanten Firmware- bzw. Softwareupdates etabliert werden?
* Informiert der Hersteller die betroffenen Stellen, wenn Sicherheitslücken bekannt werden?
* Bietet der Hersteller einen technischen Kundendienst an, der in der Lage ist, in einer vertretbaren Zeit Auskunft zu geben bzw. Fehlfunktionen zu beheben?
* Bietet der Hersteller Schulungen oder Handbücher zur Sicherheit der IoT-Geräte an?
**Vorgaben aus dem Anwendungsgebiet**

Das IoT-Gerät muss im jeweiligen Anwendungsgebiet geltenden Standards und Normen entsprechen, sowie, falls zutreffend, die Kriterien für eine produktspezifische Zulassung erfüllen. Derartige Zulassungen sind z. B. in den Bereichen Luftverkehr, Straßenverkehr und Medizintechnik üblich.

**Materielle Sicherheit**

Wird das IoT-Gerät bei rauen Umweltbedingungen wie Feuchtigkeit, extremen Temperaturen, mechanischen Belastungen und Staub eingesetzt, muss es physikalisch robust sein. Es sollten keine oder nur wenige zuverlässige Steckverbindungen vorhanden sein. Empfindliche Komponenten sollten speziell gekapselt und mit Dämpfungsvorrichtungen versehen sein. Auf Bauteile mit beweglichen Komponenten sollte soweit wie möglich verzichtet werden.

**Ausfall- und Betriebssicherheit**

Abhängig von der geforderten Verfügbarkeit sind an das IoT-Gerät Anforderungen zur Ausfallsicherheit, zur elektromagnetischen Verträglichkeit, zu internen Überwachungs- und Selbsttestmechanismen und zum Wiederanlauf zu stellen.

**Systemarchitektur**

Die Bandbreite für Systemarchitekturen ist sehr groß. Neben Neuentwicklungen kommen, anders als im PC - oder Serverbereich, auch oftmals ältere Architekturen und Betriebssysteme zum Einsatz. Gründe dafür sind die niedrigeren Kosten für den Prozessor selbst und die Möglichkeit das Anwendungsdesign, Programmcode und Entwicklungswerkzeuge sowie Debugtools wiederverwenden zu können. Es ist darauf zu achten, dass die gewählte Systemarchitektur geeignet ist, die notwendigen Sicherheitsfunktionen zu realisieren.

**Betriebssystem und Anwendungssoftware**

Wird das IoT-Gerät zusammen mit einem Betriebssystemen und/oder Anwendungssoftware beschafft, muss festgelegt werden, welche sicherheitsrelevanten Merkmale diese aufweisen sollen, z. B. hinsichtlich

* Nutzung sicherer Kommunikationsprotokolle
* Sicherer Installation und Aktualisierung
* Absicherung von Zugang und Zugriff
* Benutzer- und Rechteverwaltung
* Protokollierung
* Alarmierung
* Integritätsschutz
#### SYS.4.4.M9 Regelung des Einsatzes von IoT-Geräten

Auch im laufenden Betrieb müssen eine Reihe von Sicherheitsanforderungen an den Einsatz von IoT-Geräten gestellt werden. Sie müssen adäquat in das technische und organisatorische Umfeld eingebunden sein, in dem sie eingesetzt werden. Dafür müssen die folgenden organisatorischen Regelungen getroffen werden.

Es müssen Verantwortliche für den Betrieb der IoT-Geräte benannt werden, die sich beispielsweise um Aktualisierungen, Wartungs- und Reparaturarbeiten, Protokollauswertung und für die Reaktion auf Sicherheitsvorfälle und Fehlfunktionen benannt werden. Bei Ausfällen, Fehlfunktionen und bei Sicherheitsvorfällen muss klar definiert sein, was zu unternehmen ist.

Es sind Regelungen festzulegen, um die Sicherheit und Funktionsfähigkeit der IoT-Geräte zu testen. Die Anforderungen an die physikalische Einsatzumgebung, wie z. B. der Luftfeuchtigkeits- und Temperaturbereich und die Energieversorgung, müssen festgelegt sein. Falls erforderlich sind dafür ergänzende Maßnahmen bei der Infrastruktur zu etablieren.

Die IoT-Geräte sollten so konfiguriert werden, dass eine angemessene Sicherheit und Funktionalität erreicht werden kann. Die Konfiguration der IoT-Geräte muss dokumentiert sein, damit sie nach einem Austausch, einer Aktualisierung oder um ein System wieder herzustellen entsprechend den Sicherheitsanforderungen wieder eingerichtet werden kann.

#### SYS.4.4.M10 Sichere Installation und Konfiguration von IoT-Geräten

Nachdem die Planung neuer IoT-Geräte abgeschlossen und eine Sicherheitsrichtlinie erstellt wurde, kann mit der Installation der IoT-Geräte begonnen werden.

Die Installation und Konfiguration der IoT-Geräte sollte nur von autorisierten Personen (Verantwortlich für IoT-Geräte, Administratoren oder vertraglich gebundene Dienstleister) durchgeführt werden. Administratoren für IoT-Geräte und deren Vertreter müssen sorgfältig ausgewählt werden. Sie müssen regelmäßig darüber belehrt werden, dass die Befugnisse nur für die erforderlichen Administrationsaufgaben verwendet werden dürfen. Da Administratoren hinsichtlich der Funktionsfähigkeit der eingesetzten Hard- und Software eine Schlüsselrolle inne haben, muss auch beim Ausfall von Administratoren die Weiterführung der Tätigkeiten gewährleistet sein. Hierzu müssen die benannten Vertreter über den aktuellen Stand der Systemkonfiguration verfügen sowie Zugriff auf die für die Administration benötigten Passwörter, Schlüssel und Sicherheitstoken haben. 

**Installation**

Während der Installation und der späteren Konfiguration sollten zumindest die wichtigen Schritte so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Beispielsweise kann eine Checkliste für die Installation erstellt werden, auf der durchgeführte Schritte abgehakt und vorgenommene Einstellungen vermerkt werden können. Eine entsprechende Dokumentation ist für eine Fehleranalyse oder spätere Neuinstallation hilfreich. Dabei sollte beachtet werden, dass neben dem Autor auch weitere, auf diesem Gebiet eventuell weniger spezialisierte, Administratoren auf die Dokumentation zurückgreifen müssen. Daher ist es wichtig, dass die Dokumentation gut strukturiert und verständlich ist.

Es sollte verhindert werden, dass andere IT-Systeme während der Installation auf das zu installierende IoT-Geräte zugreifen können. Dies ist wichtig, weil während der Installation meist noch keine Passwörter vergeben und keine Schutzmechanismen aktiv sind, aber eventuell schon Zugriffe möglich sind. Falls die Installation der IoT-Geräte über das Netz erfolgen soll oder muss (beispielsweise Nachladen von Paketen), so wird empfohlen, einen Installationsserver im abgesicherten Administrationsnetz zu nutzen.

Sofern dies nicht bereits automatisch geschehen ist, sollte spätestens beim Abschluss der Grundinstallation auch die Protokollierung der Systemereignisse aktiviert werden. Die Protokolldaten können bei Problemen bei der weiteren Installation und Konfiguration wertvolle Informationen liefern.

**Konfiguration**

Die Grundeinstellungen, die vom Hersteller oder Distributor eines IoT-Geräts vorgenommen werden, sind meist nicht auf Sicherheit optimiert, sondern auf eine einfache Installation und Inbetriebnahme sowie oft darauf, dass jeder Anwender möglichst einfach auf möglichst viele Features des IoT-Geräts zugreifen kann. Beim Einsatz von IoT-Geräten in Behörden oder Unternehmen ist dies oft nicht wünschenswert.

Der erste Schritt bei der Grundkonfiguration muss daher sein, die Grundeinstellungen zu überprüfen und nötigenfalls entsprechend den Vorgaben der Sicherheitsrichtlinie anzupassen. Die Grundkonfiguration ist naturgemäß relativ stark vom eingesetzten Betriebssystem abhängig. Aus diesem Grund sind in den betriebssystemspezifischen Bausteinen entsprechende detailliertere Empfehlungen enthalten.

Ziele einer sicheren Grundkonfiguration sollten sein, dass

* die IoT-Geräte gegen "einfache" Angriffe über das Netz abgesichert sind,
* niemand durch reine Neugierde oder gar zufällig Zugriff auf sensitive Daten erlangen kann, die nicht für ihn bestimmt sind,
* niemand beim Arbeiten mit den IoT-Geräten durch reine Bedienungsfehler schwerwiegenden Schaden an den IoT-Geräten verursachen kann, und dass
* die Auswirkungen kleinerer Fehler so weit wie möglich begrenzt sind.
Die Einstellungen, die im Rahmen der Grundkonfiguration überprüft und angepasst werden sollten, betreffen insbesondere die folgenden Bereiche:

**Einstellungen für Systemadministratoren**

Nicht alle IoT-Geräte bieten ein dediziertes Rechte- und Rollenmodell. Wenn, dann sollten die Kennungen, unter denen Systemadministratoren arbeiten, besonders stark abgesichert werden. Diese Einstellungen sollten überprüft und gegebenenfalls angepasst werden. 

**Einstellungen für Benutzerkennungen und Benutzerverzeichnisse**

Im Rahmen der Grundkonfiguration sollte überprüft werden, welche Standardeinstellungen für Benutzerkennungen gelten. Die Einstellungen müssen gegebenenfalls entsprechend der Sicherheitsrichtlinie angepasst werden. Dies betrifft im Wesentlichen dieselben Parameter wie für Systemadministrator-Kennungen, für normale Benutzer können aber unter Umständen andere Einstellungen sinnvoll sein.

**Einstellungen für den Zugriff auf das Netz**

Im Rahmen der Grundkonfiguration sollten auch die Einstellungen für den Zugriff auf das Netz sowie wichtige externe Dienste getroffen und dokumentiert werden. 

**Deaktivierung von "Call Home"-Funktionen**

Einige IoT-Geräte senden Informationen, beispielsweise über aufgetretene Fehler oder über die Systemkonfiguration, direkt an den Hersteller, damit dieser zukünftig das Produkt an die Bedürfnisse der Anwender anpassen kann. Hierfür wird eine Datenverbindung über Datennetze, wie dem Internet, zu den Servern des Herstellers aufgebaut. Eine solche Form des Datenabflusses kann kritisch sein, vor allem, wenn die Anwender nicht über die Häufigkeit und Inhalte der Datenweitergabe informiert werden.

Generell sollte dieser oft unerwünschte Informationsaustausch unterbunden werden. Ob und wie Informationen versendet werden, kann in der Regel den Lizenzvereinbarungen der eingesetzten Software entnommen werden.

Viele Applikationen bieten die Möglichkeit, diese "Call Home"-Funktion zu deaktivieren. Nur in begründeten Ausnahmefällen sollte diese aktiviert bleiben. Nach Updates sollte überprüft werden, ob die "Call Home"-Funktion weiterhin deaktiviert ist.

Durch lokale Paketfilter oder dem zentralen Sicherheitsgateway (Firewall) kann ebenfalls der Verbindungsaufbau mit dem Hersteller unterbunden werden. Beispielsweise könnten auf Grundlage der Zieladressen oder der Portnummern die Datenverbindungen abgewiesen werden. Hierbei ist zu beachten, dass die Berücksichtigung aller Applikationen aufwändig ist und automatische Update-Funktionen, falls benötigt, dann oft nicht mehr zur Verfügung stehen.

#### SYS.4.4.M11 Verwendung sicherer Protokolle

Bereits bei der Beschaffung sollte darauf geachtet werden, dass IoT-Geräte ein auf Verschlüsselung basierendes Protokoll (z. B. SSL/TLS bzw. SSH) unterstützen (siehe SYS.4.4.A8 Beschaffungskriterien für IoT-Geräte). Bei der Inbetriebnahme muss darauf geachtet werden, dass vorhandene sichere Protokolle aktiviert und eventuell vorhandene unsichere (wie z. B. telnet) deaktiviert werden. Bietet das Produkt selbst keine Verschlüsselung, muss dies bei der Inbetriebnahme, z. B. über ein Virtual Private Network (VPN), flankierend umgesetzt werden.

Soweit möglich sollten auf den IoT-Geräten alle nicht benötigten Netzprotokolle deaktiviert werden (siehe SYS.4.4.M13 Deaktivierung und Deinstallation nicht benötigter Komponenten). 

#### SYS.4.4.M12 Sichere Integration in übergeordnete Systeme [Informationssicherheitsbeauftragter (ISB)]

IoT-Geräte werden häufig in Zusammenhang mit übergeordneten Management-Systemen eingesetzt, z.B. Gebäudesteuerungssystemen. 

IoT-Geräte wie Überwachungskameras, Raum- und Umgebungssensoren sollten ausschließlich mit dem zugehörigen Managementsystem kommunizieren. Eine Kommunikation dieser Systeme mit dem Internet ist in aller Regel nicht notwendig und sollte unterbunden werden.

#### SYS.4.4.M13 Deaktivierung und Deinstallation nicht benötigter Komponenten

Oft sind nach einer Standardinstallation eines IoT-Geräts eine größere Anzahl von Benutzerkennungen, Protokollen, Diensten, Funktionen, Schnittstellen und sonstigen Komponenten eingerichtet, die für den Betrieb nicht in jedem Fall notwendig sind und die deswegen eine Quelle von Sicherheitslücken sein können. Dies gilt insbesondere für Netzdienste. Daher sollte im Rahmen der Grundkonfiguration geprüft werden, welche Protokolle und Dienste wirklich gebraucht werden. Nicht benötigte Dienste der IoT-Geräte sollten deaktiviert oder ganz deinstalliert werden. Dies gilt insbesondere für chronisch unsichere Dienste, wie z. B. Telnet oder SNMPv1/v2.

Nicht benötigte Benutzerkennungen sollten entweder gelöscht oder zumindest so deaktiviert werden, so dass unter der betreffenden Kennung keine Anmeldung am IoT-Gerät möglich ist.

Einige Schnittstellen können potentielle Sicherheitsprobleme mit sich bringen, denen durch geeignete organisatorische oder technische Sicherheitsmaßnahmen entgegengewirkt werden muss. Schnittstellen, deren Nutzung kontrolliert werden sollte, sind beispielsweise Bluetooth, WLAN, Zigbee, Firewire, eSATA (externer SATA-Festplattenanschluss) und Thunderbolt. Die Verwendung von nicht benötigten Schnittstellen sollte unterbunden werden. An vielen Geräten lassen sich die Funk-Schnittstellen nicht deaktivieren, dann muss die Nutzung der Geräte geprüft werden (Schutzbedarf, Kontroll- und Einschränkungsmöglichkeiten gegeneinander abwägen).

Die Überprüfung auf laufende Dienste sollte von außen durch einen Portscan von einem anderen System aus erfolgen.

#### SYS.4.4.M14 Einsatzfreigabe

Bevor IoT-Geräte im produktiven Betrieb eingesetzt und bevor sie an ein produktives Netz angeschlossen werden, sollte der Einsatz freigegeben werden, dies ist zu dokumentieren. Die Einsatzfreigabe basiert auf einer Prüfung der Installations- und Konfigurationsdokumentation und der Funktionsfähigkeit der IoT-Geräte in einem Test. Sie erfolgt durch eine in der Institution dafür autorisierte Stelle. Vertiefende Informationen hierzu sind in OPS.1.1.7 Softwaretests- und Freigaben zu finden.

#### SYS.4.4.M15 Restriktive Rechtevergabe

Grundsätzlich sollten Berechtigungen immer restriktiv vergeben werden, so dass Benutzer genau auf die Dienste und Daten zugreifen können, die sie für ihre Aufgaben benötigen. 

#### SYS.4.4.M16 Beseitigen von Schadprogrammen auf IoT-Geräten

Je nach Art und Einsatzgebiet von IoT-Geräten können diese von Schadprogrammen infiziert werden. Wie Infektionen mit Schadprogrammen vorgebeugt werden kann und wie sie beseitigt werden können, hängt von den verwendeten Betriebssystemen ab. Hierüber sollten regelmäßig aktuelle Sicherheitsinformationen eingeholt werden.

Aktuelle Schadsoftware auf Überwachungskameras und anderen IoT-Geräten befindet sich oftmals nur im flüchtigen Arbeitsspeicher, statt sich persistent im System einzunisten. Daher ist ein regelmäßiger Neustart solcher IoT-Geräte ratsam. Dies kann eine Infektion bereinigen, wenngleich es nicht vor einer Neuinfektion schützt.

Kann die Ursache für die Infektion nicht behoben bzw. eine Neuinfektion wirksam verhindert werden, sollten die betroffenen IoT-Geräte nicht mehr verwendet werden.

#### SYS.4.4.M17 Überwachung des Netzverkehrs von IoT-Geräten

Es empfiehlt sich, die Kommunikation (ein- und ausgehende Verbindungen) regelmäßig auf Auffälligkeiten zu kontrollieren. Hierbei können Logfiles von Firewalls genaue Informationen liefern, mit wem die IoT-Geräte über welchen Dienst kommunizieren möchten und ob diese Verbindungen erlaubt oder blockiert wurden. Weiterhin können auch die IoT-Geräte oder die dazugehörige Administrations- oder Managementsoftware Informationen liefern, ob die IoT-Geräte erwartungsgemäß verwendet werden.

Sollte eine präventive Unterdrückung ungewollter Kommunikation nicht möglich sein, können folgende Maßnahmen bei der Erkennung helfen:

* Aktivierung und nach Möglichkeit zentralisierte Sammlung und Auswertung von Logdaten von Systemen und Komponenten.
* Automatische Filter auf diese Logdaten, die einen Alarm auslösen, wenn Netzverkehr von den IoT-Geräten oder Sensor-Systemen zu Nicht-Managementsystemen beobachtet wird.
* Analyse der Netz-Statistik z.B. mit Netflow.
#### SYS.4.4.M18 Protokollierung sicherheitsrelevanter Ereignisse bei IoT-Geräten

Grundsätzlich sind sicherheitsrelevante Ereignisse im Betrieb von IoT-Geräten zu protokollieren. Die technischen Möglichkeiten dazu können bei unterschiedlichen Arten von IoT-Geräten und deren Umgebung stark variieren. Mögliche Ausprägungen, Funktionalitäten und Parameter sind:

* Protokollierung in einen nicht flüchtigen Speicher, kumulativ durch unterschiedliche Prozesse,
* Datenaufzeichnung in einfachen, formatierten Textdateien, CSV oder
* Aufzeichnung von Prozessdaten über Datenlogger, im Zeittakt, ereignisgesteuert oder bei Änderungen,
* Strukturierte Speicherung der Ereignisse in einem Datenbanksystem,
* Echtzeitüberwachung mit Information eines Anwenders und der Möglichkeit einer Interaktion zur Laufzeit,
* Protokollierung aller oder konfigurierbarer Zustands- und Transitionsänderungen,
* Variablenablaufverfolgung, Audit Trails,
* Statistische Auswertung in Berichtsform oder als grafische Darstellung und
* Korrelation, Bewertung.
Soweit möglich, sollten bei IoT-Geräten zumindest Sicherheitsverstöße protokolliert werden, wie versuchter und durchgeführter unautorisierter Zugang und Zugriff. Insbesondere sind die Aktivitäten von privilegierten Benutzern zu überwachen, wie Technikern und Administratoren. Dadurch kann zwar der Missbrauch von Rechten nicht verhindert werden, es ist aber die Voraussetzung, um gezielt Schwachstellen zu schließen. 

Ist eine elektronische Protokollierung wegen technischer Einschränkungen durch die begrenzten Ressourcen nicht oder nur sehr begrenzt realisierbar, sollten organisatorische Regelungen geschaffen werden. Zum einen sollten alle Arbeiten an einem IoT-Gerät mit Angaben zu Ort, Zeit, Ausführendem sowie Art und Grund der Tätigkeit in einem Logbuch festgehalten werden. Zum anderen sollten alle Ausfälle, offensichtliche Zugangs- und Zugriffsverletzungen und sonstige Auffälligkeiten im Logbuch dokumentiert werden. Die Einträge sollten regelmäßig und anlassbezogen ausgewertet werden.

Sowohl automatisch erzeugte Protokolle als auch Aufzeichnungen durch das Personal sind gegen unerlaubte nachträgliche Veränderung zu schützen. Nur dediziert Berechtigte dürfen auf die Protokolle zugreifen können. Soweit technisch möglich, sind Vorkehrungen zu treffen, dass die Protokolldaten auch nicht von privilegierten Nutzern gelöscht oder geändert werden können, durch Speicherung auf nicht wiederbeschreibbaren Datenträgern oder mittels elektronischer Signatur. Datenträger mit Protokolldaten sind sicher zu verwahren und die beteiligten Personen sind über den korrekten Umgang zu belehren.

#### SYS.4.4.M19 Schutz der Administrationsschnittstellen

Abhängig davon, ob IoT-Geräte 

* lokal, also am Gerät selber, direkt über das Netz, also an einem anderen IT-System über eine entsprechende vom IoT-Gerät selbst bereitgestellte Weboberfläche, oder über zentrale netzbasierte Tools, also über eine Managementsoftware auf einem Server,
* direkt über das Netz, also an einem anderen IT-System über eine entsprechende vom IoT-Gerät selbst bereitgestellte Weboberfläche, oder über zentrale netzbasierte Tools, also über eine Managementsoftware auf einem Server,
* über zentrale netzbasierte Tools, also über eine Managementsoftware auf einem Server,
administriert werden, sollten geeignete Sicherheitsvorkehrungen getroffen werden. Die zur Administration verwendeten Methoden sollten in der Sicherheitsrichtlinie festgelegt werden und die vereinbarten Sicherheitsvorkehrungen kurz beschrieben werden. Die Sicherheitsrichtlinie gibt auch vor, wie die IoT-Geräte zu administrieren sind. Für eine Administration über das Netz sollten sichere Protokolle verwendet werden.

#### SYS.4.4.M20 Geregelte Außerbetriebnahme von IoT-Geräten

Bei der Außerbetriebnahme von IoT-Geräten muss sichergestellt werden, dass

* keine wichtigen Daten, die eventuell auf diesen gespeichert sind, verloren gehen, und dass
* keine sensitiven Daten auf den Datenträgern von IoT-Geräten zurück bleiben.
Dazu ist es insbesondere wichtig, einen Überblick darüber zu haben, welche Daten wo auf den von IoT-Geräten gespeichert sind.

* Austragen des IT-Systems aus Verzeichnisdiensten und Datenbanken  
 Etwaige Berechtigungen im Netz, die an ein IoT-Gerät gekoppelt sind, müssen gelöscht werden. Beispiele hierfür sind Einträge auf Proxyservern am Sicherheitsgateway oder Zugriffsrechte auf Netzdienste, die anhand der IP-Adresse gewährt werden. Ist ein IoT-Gerät in netzweiten Verzeichnisdiensten oder Datenbanken eingetragen, so müssen die zugehörigen Einträge gelöscht oder zumindest die entsprechenden Kennungen deaktiviert werden. 
* Löschen der Daten auf den IoT-Geräten  
 Es muss sichergestellt werden, dass keine schützenswerten Informationen mehr auf den Speicherbereichen von IoT-Geräten vorhanden sind. Alle auf Datenträgern vorhandenen bzw. permanent gespeicherten Daten sollten so gelöscht werden, dass sie nachträglich auch nicht durch spezielle Software lesbar wiederhergestellt und missbräuchlich verwendet werden können. Ist es nicht möglich, die Daten sicher zu löschen, sollten bei höherem Schutzbedarf die betreffenden Datenträger vernichtet werden.
* Entfernen sonstiger Informationen  
 Sind von einem IoT-Gerät noch an anderen Stellen schützenswerte Daten gespeichert, etwa in einem nichtflüchtigen Speicher oder in der Cloud, so müssen auch diese bei der Außerbetriebnahme des Geräts gelöscht werden.
### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.4.4.M21 Einsatzumgebung und Stromversorgung [Informationssicherheitsbeauftragter (ISB), Haustechnik](I)

Bevor IoT-Geräte installiert werden, sollte geklärt werden, ob sie in der angedachten Einsatzumgebung betrieben werden dürfen. Der ISB sollte beispielsweise prüfen, ob IoT-Geräte wie Kameras mit dem Blickwinkel auf Eingabegeräte (Tastaturen, PIN-Pads) oder Monitore sinnvoll sind. Diese könnten somit auch vertrauliche Zugangsdaten aufzeichnen. Je nach Schutzbedarf der Umgebung sollten potentiell unsichere Geräte dort überhaupt nicht installiert werden. Bei IoT-Geräten wie Kameras müssen außerdem die entsprechenden Datenschutz-Vorgaben beachtet werden.

Es sollte geklärt sein, ob ein IoT-Gerät bestimmte Anforderungen an die physikalische Einsatzumgebung hat, wie z. B. Luftfeuchtigkeit, Temperatur oder Energieversorgung. Dies ist insbesondere bei IoT-Geräten, die in Außenbereichen betrieben werden, wichtig. Falls erforderlich, sollten dafür ergänzende Maßnahmen bei der Infrastruktur umgesetzt werden, beispielsweise passende Einhausungen.

IoT-Geräte sollten in der Einsatzumgebung vor Diebstahl, Zerstörung und Manipulation geschützt werden. Dies kann beispielsweise durch geeignete Anbringung oder zusätzliche Schutzmechanismen wie Einhausungen erreicht werden. Wichtig ist das vor allem bei an der externen Peripherie angebrachten Geräten, z. B. zur Videoüberwachung. 

IoT-Geräte sind häufig nicht an Stromnetze angeschlossen, sondern werden mit Batterien betrieben. Dann sollte der regelmäßige Funktionstest und Austausch der Batterien geregelt werden.

IoT-Geräte sollten entsprechend ihrer vorgesehenen Einsatzart und des vorgesehenen Einsatzorts vor Staub und Verschmutzungen geschützt werden.

#### SYS.4.4.M22 Systemüberwachung(A)

Um auf kritische Systemereignisse reagieren zu können, sollte auch für IoT-Geräte ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept erstellt werden. Dazu gehört, dass Systemzustand und Funktionsfähigkeit der IoT-Geräte laufend überwacht werden. Wenn Fehler auftreten oder definierte Grenzwerte über- oder unterschritten werden, sollte dies automatisch an das Betriebspersonal gemeldet werden. Dafür sollten die IoT-Geräte in ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept eingebunden werden.

#### SYS.4.4.M23 Auditierung von IoT-Geräten(CIA)

Bei allen IoT-Geräten sollte regelmäßig überprüft werden, ob diese korrekt konfiguriert und ob alle festgelegten Sicherheitsmaßnahmen umgesetzt sind. Werden Abweichungen vom Soll-Zustand gefunden und sind Abhilfe-Maßnahmen bekannt, so sollten diese dokumentiert werden.

Außerdem sollten, zumindest in sicherheitskritischen Bereichen, alle zum Einsatz kommenden IoT-Geräte durch Experten vor dem Einsatz sicherheitstechnisch überprüft werden.

#### SYS.4.4.M24 Sichere Konfiguration und Nutzung eines eingebetteten Webservers(CIA)

Einige IoT-Geräte besitzen einen integrierten Webserver, mit dem Informationen abgerufen und eingesteuert werden können. Dabei handelt es sich für gewöhnlich um einen sogenannten Embedded-Webserver mit eingeschränkter Funktionalität, der für die meist knappen Ressourcen optimiert ist. Auf dem Markt sind zahlreiche eingebettete Webserver verfügbar, sie haben eine geringe Größe, belasten die CPU nur moderat und sind weitgehend plattformunabhängig. Als Hauptaufgabe können sie Webdokumente an den Client via HTTP(S) übertragen. Einige beherrschen zudem das dynamische Erstellen von Dokumenten, etwa per Server-Side Scripting.

Für einen eingebetteten Webserver sollten möglichst nur die benötigten Komponenten und Funktionen installiert bzw. aktiviert werden. Bei einigen IoT-Geräten sind hier wenige oder gar keine Konfigurationsmöglichkeiten vorhanden. Der Webserver sollte unter einem Konto mit möglichst geringen Rechten ablaufen. Falls zum Start höhere Privilegien benötigt werden, sollte anschließend in ein nicht privilegiertes Konto gewechselt werden. Es sollten alle für die Sicherheit und die Fehlerbehandlung relevanten Meldungen protokolliert werden, z. B. strukturiert nach erfolgreichen und nicht erfolgreichen Zugriffen, internen Fehlern, fehlerhaften oder unvollständigen HTTP-Anfragen und sonstigen relevanten Systemmeldungen. Diese Protokollierung sollte in der Sicherheitsdokumentation beschrieben sein (weitere Informationen hierzu finden sich in OPS.1.1.6 Protokollierung)Mit dem Webserver sollte möglichst nur über eine gesicherte SSL-Verbindung kommuniziert werden und der Zugang sollte nur nach einer starken Authentisierung möglich sein.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Es gibt auch darüber hinaus Sicherheitsmaßnahmen, die zur Absicherung von IoT-Geräten umgesetzt werden könnten und die je nach Einsatzumgebung und Schutzbedarf sinnvoll sind. Dazu gehören:

* Penetrationstests bzw. Sicherheitsanalysen der IoT-Geräte oder deren Firmware
* Prüfen auf versteckte Links (vor allem im Bereich der Administrationsfunktionen)
* Ergänzung fehlender oder unzureichender Authentisierungsfunktionen
* verfügbare Funktionen auf Konsolenebene 
Dies ist der Bereich, wo weitere Sicherheitsüberlegungen und Maßnahmen gesammelt werden können und daraus ergänzende Maßnahmen abgeleitet werden könnten. Ideen dazu bitte an mailen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeines IoT-Gerät" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ACS1] Sicherheit von IP-basierten Überwachungskameras

  

 CSE 128, Version 1.0, Allianz für Cyber-Sicherheit, 11.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_128.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_128.html)

 
* #### [ACS2] Spionageangriffe mittels Hintertüren in Überwachungskameras und Raumsensoren

  

 So schützen Sie Ihr Unternehmen, Expertenkreis Cyber-Sicherheit, Allianz für Cyber-Sicherheit, 10.2016  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161010\_expkr\_statement01.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/partner/161010_expkr_statement01.pdf)

 
* #### [DHS] Department of Homeland Security

  

 Securing the Internet of Things, 12.2016,   
 <https://www.dhs.gov/securingtheIoT>

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (zuletzt abgerufen am 28.09.2017)  
 <https://www.owasp.org>

 
