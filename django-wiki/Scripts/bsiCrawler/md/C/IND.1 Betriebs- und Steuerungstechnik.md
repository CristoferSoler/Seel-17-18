1 Beschreibung
--------------

### 1.1 Einleitung

Betriebstechnik (englisch: Operational Technology (OT)) ist Hard- und Software, die Änderung durch die direkte Überwachung und / oder Steuerung von physikalischen Geräten, Prozessen und Ereignissen im Unternehmen erfasst und bewirkt [GART1].

In der Industrie, zu der unter anderem auch die Kritischen Infrastrukturen gehören, zählen dazu insbesondere industrielle Steuerungssystemen (Industrial Control Systems, ICS) und Automationslösungen, die dort die Steuerungs- und Regelfunktionen aller Art übernehmen. Weitere Beispiele sind Laborgeräte (z. B. automatisierte Mikroskop oder Analysewerkzeuge), Logistiksysteme (Barcodescanner mit Kleinrechner) oder Gebäudeleittechnik.

Die in der Vergangenheit übliche physische Trennung der OT von anderen IT-Systemen und Netzen in Büroanwendungen ist heute aufgrund zunehmender Integrationsanforderungen nur in Ausnahmefällen bei erhöhtem Schutzbedarf anwendbar. Mehrstufige Produktionsschritte und deren übergreifende Steuerung wie auch regulatorische Anforderungen erfordern eine zunehmende Öffnung auch über Organisationsgrenzen hinweg. Diese Entwicklung wird durch den Trend zur Optimierung von Fertigungsprozessen zur Steigerung der Wettbewerbsfähigkeit im Rahmen von Industrie 4.0 beschleunigt.

Da neben OT-spezifischen Komponenten zunehmend IT-Komponenten und Technologien aus der Office-IT in der OT eingesetzt werden, sind diese inzwischen vergleichbaren Gefährdungen ausgesetzt. Zugleich weisen die OT gegenüber der klassischen IT wesentliche Unterschiede auf, die das Anwenden dort etablierter Sicherheitsverfahren erschweren. So kann es Restriktionen aufgrund Herstellervorgaben oder gesetzlichen Anforderungen geben, die Veränderungen an Komponenten verhindern oder erschweren. Ein Beispiel hierfür sind die Anwendung von Sicherheitsupdates oder nachträgliche Härtungsmaßnahmen. Die OT unterliegt in der Regel auch deutlich längeren Lebenszyklen, auch über die Herstellerunterstützung hinaus, so dass auch die Verfügbarkeit von Sicherheitsupdates nicht durchgängig gewährleistet werden kann.

Ein wesentlicher Unterschied ergibt sich für die OT auch aus den oft hohen Verfügbarkeits- und Integritätsanforderungen, während im Vergleich zu Office-IT die Vertraulichkeit häufig von nachrangiger Bedeutung ist. Störungen dieser Systeme können Gefährdungen von Leib, Leben und Umwelt nach sich ziehen und sind zumeist nicht durch einen Neustart zu beheben.

### 1.2 Zielsetzung

Das Ziel des Bausteins besteht darin, geeignete Anforderungen an die Informationssicherheit der OT aufzuzeigen. Er adressiert komponentenübergreifende, konzeptionelle und architektonische Sicherheitsanforderungen.

Der Baustein ist übergreifend zu modellieren und umzusetzen. Dabei kann eine mehrfache Verwendung in unterschiedlichen Bereichen der OT in einer Institution (Betreiber im Sinne der VDI 2182) nicht ausgeschlossen werden, da in diesen unterschiedliche Anforderungen bzgl. der Informationssicherheit vorliegen.

### 1.3 Abgrenzung

Die Ausgestaltung der OT kann je nach Zweck, Branche, der eingesetzten IT-Systeme und Technik sowie aufgrund des langen Einsatzzeitraums (zum Teil ohne Updates) selbst bei vergleichbaren Anwendungsfällen stark variieren. Bei der Ausgestaltung der Sicherheitsmaßnahmen auf Basis der Anforderungen aus diesem Baustein sind daher die vorhandenen Besonderheiten zu berücksichtigen. Diese können wesentlichen Einfluss auf die Ausgestaltung des Sicherheitskonzepts nehmen. Der Risikoanalyse kann aus diesem Grund bereits bei der Erstellung eines Sicherheitskonzepts für den normalen Schutzbedarf eine hohe Bedeutung zukommen. Dies kann mehrfache Verwendung des Bausteins für unterschiedliche Bereiche erforderlich machen.

Zusätzlich ist die umgebende Infrastruktur der OT – also Standorte, Anlagen, Gebäude, Räume etc. – durch möglichst spezifisch geeignete Bausteine zu modellieren, um die Schutzwirkung dieses Bausteins zu komplementieren.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Betriebs- und Steuerungstechnik von besonderer Bedeutung:

### 2 1 Ungeeignete Einbindung der OT in die Sicherheitsorganisation

Durch unterschiedliche Rahmenbedingungen, Kenntnisse und Vorgehensweisen in den Bereichen Office-IT und ICS kann es bei übergreifenden Sicherheitsvorgaben zu Umsetzungsproblemen kommen. Sicherheitsvorgaben aus dem Bereich der IT können einerseits aufgrund technischer oder prozessualer Besonderheiten bei ICS-Systemen nicht umsetzbar sein. Andererseits können ICS-spezifische Informationssicherheits- und Safety-Aspekte (Aspekte der funktionalen Sicherheit) den Zuständigen für Informationssicherheit der Office-IT nicht bekannt sein. Auf diese Weise kann es zu Reibungsverlusten in der Kommunikation und der Umsetzung sowie zu nicht ausreichend behandelten bzw. nicht erkannten Risiken kommen.

### 2 2 Ungeeignete Einbindung der OT in betriebliche Abläufe

Ungeachtet der zunehmenden Konvergenz von OT und IT sind Besonderheiten vorhanden, die das Übertragen etablierter betrieblicher Abläufe erschweren. Betriebliche Eingriffe im Rahmen des Change- und (Security) Incident-Managements zur sicheren Konfiguration, Störungsbehebung oder dem Einspielen von Sicherheitsupdates etwa können eine erneute behördliche Freigabe oder den Verlust des Herstellersupports nach sich ziehen. Nicht autorisierte Änderungen können die Funktion einer Komponente beeinflussen und damit potenziell auch Auswirkungen auf deren Safety-Funktionen besitzen.

Die OT dient der Überwachung, Steuerung und Automatisierung von technischen Abläufen. Störungen dieser Systeme können zu Produktionsausfällen, technischen oder personellen Schäden und Umweltschäden führen. Diese potenziellen Auswirkungen müssen bei betrieblichen Eingriffen berücksichtigt werden.

### 2 3 Unzureichender Zugangsschutz

Industrielle Steuerungsanlagen werden immer seltener vollständig autark von der Außenwelt betrieben. Moderne Fertigungs- und Erzeugungsprozesse erfordern einen Informationsaustausch mit vor- und nachgelagerten Produktionsschritten und sind häufig an zentrale Produktionsplanungs- und Steuerungssysteme (Manifacturing Execution System / Enterprise Ressource Planning) einer Institution angebunden. Der elektronische Informationsaustausch erfordert eine Vernetzung der Produktionsanlagen mit Drittnetzen wie der Office-IT oder auch den Netzen von Partnern und Dienstleistern. Anforderungen an interaktive Zugriffe von Büro- oder Mobilarbeitsplätzen als auch betrieblich bedingte Anforderungen an den elektronischen Datenaustausch, etwa zur Bereitstellung von Software und Updates, oder zur Realisierung von Fernzugängen für eine Rufbereitschaft oder für Dienstleister fördern die Vernetzung mit der Außenwelt.

Werden die erforderlichen Kommunikationskanäle zu weit gefasst oder unzureichend gesichert, können Angreifer diese Zugangswege zum netzbasierten Zugriff und zur Kompromittierung des Automatisierungssystems nutzen.

### 2 4 Unzureichendes Schutzkonzept gegen Schadprogramme für die OT

Industrielle Steuerungsanlagen können sowohl von zielgerichteten Schadsoftware-Angriffe als auch zufällig von Schadprogrammen betroffen sein, die auf die Kompromittierung der Office-IT zielen. Mögliche Infektionswege ergeben sich aus Datentransfers, dem Einsatz von Wechselmedien und mobilen Endgeräten oder fehlender Segmentierung oder Kontrolle des Datenverkehrs.

Auf der anderen Seite kann der Einsatz von Virenschutz-Software auch Risiken für die OT darstellen, wenn keine Herstellerfreigabe für die Umgebung vorliegt oder Fehlerkennungen und aktive Systemeingriffe den Betrieb gefährden. Ein vergleichbares Störungspotenzial (durch die Unterbrechung von Verbindungen) kann sich auch aus dem Betrieb netzbasierter Intrusion Prevention Systeme (IPS) ergeben.

Zusätzlich ist beim Einsatz von Virenschutz-Software eine regelmäßige Aktualisierung notwendig. Wenn dies nicht gewährleistet ist, können neue Angriffe durch Schadsoftware nicht erkannt werden. Dies gilt auch allgemein Angriffe, für die die Virenschutz-Software keine Signaturen besitzt.

### 2 5 Unsicherer Projektierungsprozess / Anwendungsentwicklungsprozess

Anpassungen und Weiterentwicklungen von IT-Systemen, Anwendungen und Steuerungsprogrammen stellen einen kritischen Eingriff in die Steuerungsanlage dar. Störungen können aus funktionalen Fehlern bei unzureichenden Test- und Validierungsschritten, fehlerhaften oder manipulierten Projektierungsdaten oder Schwachstellen in der Software entstehen, wenn wichtige Sicherheitsfunktionen wie Ein- und Ausgabe- oder Berechtigungsprüfungen unzureichend umgesetzt werden.

Weitere Gefahren können sich aus unsicheren Entwicklungsumgebungen, der ungeeigneten Ablage von Programmcode, Dokumentation oder Projektdaten sowie aus den Datentransferschnittstellen ergeben. 

### 2 6 Unsicheres Administrationskonzept und Fernadministration

Die Verwaltung industrieller Steuerungssysteme erfolgt in bestimmten Fällen abgesetzt über Netzzugriffe. Hierbei werden unterschiedliche öffentliche und private Netze wie z. B. Telefonnetze, Funknetze, Mobilfunknetze und zunehmend das Internet eingesetzt. Sind diese Zugänge unzureichend geplant, unsicher konfiguriert oder werden diese nicht überwacht, so können Angreifer unter Umständen unbefugt auf einzelne OT-Komponeten oder die Infrastruktur zugreifen und so die Sicherheitsmechanismen am Perimeter umgehen.

Lokale Administratoren verfügen ebenfalls über privilegierte Rechte, welche einen Missbrauch durch Innentäter oder über kompromittierte Accounts für Angreifer attraktiv machen.

### 2 7 Unzureichende Überwachungs- und Detektionsverfahren

Das Überwachen von Betriebszuständen des zu automatisierenden Prozesses ist eine wesentliche Funktion industrieller Steuerungssysteme. So werden gewöhnlich den Prozess betreffende Warnungen (z. B. bei unterschrittenen Füllständen) und technische Parameter (z. B. Temperaturen, Ventilstellungen) abgebildet. Dagegen fehlt es häufig an einer angemessenen Überwachung der unterstützenden IT-Infrastruktur.

Werden ungewöhnliche oder sicherheitsrelevante Ereignisse solcher Betriebsumgebungen nicht oder nur unzureichend überwacht, können Angriffsversuche, Netzengpässe oder absehbare Ausfälle nicht frühzeitig erkannt werden.

Darüber hinaus kann auch eine mangelhafte Auswertung oder unübersichtliche Darstellung der Ereignisse dazu führen, dass Warnungen und Fehler verspätet erkannt werden.

### 2 8 Unzureichendes Testkonzept

Industrielle Steuerungsanlagen unterliegen oft hohen Verfügbarkeitsanforderungen. Störungen oder technische Ausfälle können unter Umständen schwerwiegende Schäden und hohe Folgekosten nach sich ziehen. Aus diesem Grund sind Systeme oft ausfallsicher konzipiert und redundant ausgelegt.

Werden Änderungen an einer solchen Umgebung nicht sorgfältig geplant, abgestimmt und in einer realitätsnahen Umgebung getestet, besteht die Gefahr, dass logische oder softwaretechnische Fehler übersehen werden und Störungen in der Anlage auftreten. Selbst herstellerseitig freigegebene Updates können bei Modifikationen oder Anpassung von Parametern an der Anlage Störungen verursachen.

### 2 9 Mangelnde Life Cycle Konzepte

Neben spezifischen OT-Komponenten werden zunehmend Komponenten, Technologien und Software aus der Office-IT eingesetzt, sogenannte Commercial-off-the-shelf-Produkte (COTS). Aufgrund der sehr langen Lebenszyklen in der OT werden diese Komponenten in der Regel deutlich länger betrieben als in der Office-IT üblich, teilweise auch über die Hersteller-Support-Zyklen hinaus.

Dies hat zur Folge, dass nach dem Ablauf der Herstellerunterstützung keine Updates für Schwachstellen mehr zur Verfügung gestellt werden. Dem gegenüber stehen oftmals öffentlich dokumentierte Schwachstellen, sowie Werkzeuge, die diese Schwachstellen ausnutzen. Dies ermöglicht auch nicht versierten Angreifern ein erfolgreiches eindringen in die Systeme. Dies gilt auch, wenn Updates nicht oder nur mit sehr großer Verzögerung eingespielt werden.

Die langen Einsatzzeiten können zudem zu Problemen bei der Beschaffung von Ersatzteilen führen, wenn diese nicht mehr durch den Hersteller produziert werden. Dies gilt auch für mögliches Knowhow zur Pflege und Wartung von Alt-Systemen, dass bei neuen Mitarbeitern nicht mehr vorliegt

### 2 10 Einsatz unsicherer Protokolle

Die OT-Komponenten kommunizieren untereinander über verschiedene Netzprotokolle und Technologien. Neben Protokollen und Technologien aus der Office-IT (z. B. Ethernet, TCP/ IP, WLAN, GSM) werden ICS-spezifische Protokolle eingesetzt. Diese sind nicht immer unter dem Gesichtspunkt der Informationssicherheit entwickelt worden und bieten demgemäß teilweise keine oder nur eingeschränkte Sicherheitsmechanismen. Informationen werden häufig im Klartext und ohne Integritätssicherung oder Authentisierung übertragen.

Ein Angreifer mit Zugang zum Netz könnte die Inhalte der Kommunikation auslesen oder verändern und auf diese Weise Einfluss auf die Prozesse nehmen, etwa durch Vortäuschen von Sensordaten oder Fälschen von Steuerungsbefehlen. Dies trifft in besonderem Maße auf Protokolle zu, welche für die Kommunikation über frei zugängliche Gebiete eingesetzt werden, etwa bei Funkprotokollen oder im Rahmen der Standortvernetzung (Fernwirktechnik).

### 2 11 Unsichere Konfigurationen

In der Standardkonfiguration von OT-Komponenten sind Sicherheitsmaßnahmen nicht immer aktiviert, wodurch unbefugt Zugriffe erheblich erleichtert werden. Der Betrieb unsicher konfigurierter Komponenten kann darüber hinaus auch die Sicherheit anderer Komponenten der Umgebung bedrohen, etwa wenn Zugangsdaten zu diesen ausgelesen werden können oder diese in einer Vertrauensstellung zu anderen Systemen stehen.

Beispiele für unsichere Konfigurationen sind etwa der Gebrauch von Standardpasswörtern, die Nutzung von Klartextprotokollen zur Systemverwaltung, der Betrieb nicht erforderlicher Dienste, ungesicherte Schnittstellen, wie z. B. USB oder Firewire-Ports, oder deaktivierte Sicherheitsfunktionen.

### 2 12 Abhängigkeiten der OT von IT-Netzen

Die OT wird mittlerweile immer weniger völlig autark betrieben. Bestehen Abhängigkeiten zu anderen Systemen, Netzen oder Diensten, so wirken sich Ausfälle oder Sicherheitsvorfälle im IT-Netz auch auf die OT aus.

Insbesondere, wenn diese Systeme und Netze nicht unter der Kontrolle der Institution (des Betreibers der ICS-Infrastruktur) stehen, kann dies zu starken Beeinträchtigungen der Verfügbarkeit der OT und der Prozesse führen. Darüber hinaus kann der Vorfall oder Fehler in der Regel nur mit externer Unterstützung behoben werden.

Beispiele für Abhängigkeiten zu anderen Systemen und Netzen sind Internetanbindungen (sowohl drahtgebunden als auch über Mobilfunk), gemeinsam genutzte Infrastrukturkomponenten, eine Betriebsführung und Überwachung durch Dienstleister oder die Nutzung von Cloud-Diensten.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Betriebs- und Steuerungstechnik aufgeführt. Grundsätzlich ist ICS-Informationssicherheitsbeauftragte (ICS-ISB) für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### IND.1.A1 Einbindung in die Sicherheitsorganisation

Ein Informationssicherheits-Managementsystem (ISMS) für den Betrieb der OT-Infrastruktur MUSS entweder als selbständiges ISMS oder als Teil eines Gesamt-ISMS existieren und MUSS in seinem Geltungsbereich die Definition von Zielen und Werten, Prozessen, Rollen, Verantwortlichkeiten und Vorgaben für die OT explizit umfassen.

Die Leitungsebene der Institution MUSS den Sicherheitsprozess initiieren, steuern und kontrollieren. Die Institution MUSS eine Sicherheitsorganisation aufbauen, welche die Rollen und Verantwortlichkeiten für die Informationssicherheit der OT-Infrastruktur und -Komponenten regelt.

Es MUSS ein Gesamtverantwortlicher für die Informationssicherheit im OT-Bereich bestimmt und innerhalb der Institution bekannt gegeben werden. Gesetzliche, regulatorische und sonstige besonderen Vorgaben für den OT-Bereich sowie die jeweilige Branche bzw. den Sektor MÜSSEN bekannt und ihre Auswirkungen auf die Institution ausgewertet sein.

Es MUSS ein Prozess existieren, wie konkrete Vorgaben (Richtlinien) für bestimmte Themenbereiche im Prozessbereich verfasst, kommuniziert, zur Umsetzung gebracht, fortgeschrieben, bewertet und verbessert werden.

Weiterführende Informationen sind im Baustein ISMS Sicherheitsmanagement beschrieben.

#### IND.1.A2 Sensibilisierung und Schulung des Personals

Betriebspersonal MUSS regelmäßig zu relevanten IT-Sicherheitsbedrohungen im OT-Bereich informiert und sensibilisiert werden. OT-Verantwortliche MÜSSEN regelmäßig zur Bedrohungslage und Handlungsbedarfen informiert oder geschult werden.

Weiterführende Informationen sind im Baustein ORP.3 Sensibilisierung und Schulung beschrieben.

#### IND.1.A3 Schutz vor Schadprogrammen

Zur Vorbeugung vor Risiken durch Schadprogramme MUSS ein Konzept zum Schutz vor Schadprogrammen erstellt und umgesetzt werden. Darin MÜSSEN die bedrohten IT-Systeme sowie die möglichen Infektionswege (Außenschnittstellen, Wechselmedien, Service- und Parametrier-/Programmiergeräte) betrachtet und geeignete technische und organisatorische Schutzmaßnahmen festgelegt sein.

Beim Einsatz von Virenschutz-Software auf OT-Komponenten MUSS berücksichtigt werden, ob und in welcher Konfiguration der Betrieb von Virenschutz-Software vom Hersteller unterstützt wird. Ist dies nicht der Fall, MUSS im Rahmen einer Risikoanalyse der Bedarf an alternativen Schutzverfahren geprüft werden.

Eingesetzte Virenschutz-Software MÜSSEN mit aktuellen Signaturen versorgt werden. Das Virenschutzkonzept MUSS die Aktualisierungsstrategie festlegen. Dies umfasst den Bezug von Signaturen, deren Verteilungsverfahren und die Häufigkeit der Aktualisierung. Der Bezug und die Verteilung von Signaturen können automatisiert erfolgen. Der Bezug von Virensignaturen durch OT-Systeme DARF NICHT direkt aus dem Internet erfolgen, sondern MUSS indirekt über einen Proxy- oder Virensignaturverteildienst erfolgen. Die Schnittstellensysteme MÜSSEN in einer eigenständigen Zone (z. B. DMZ) von der OT-Umgebung getrennt betrieben werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Betriebs- und Steuerungstechnik. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### IND.1.A4 Dokumentation der OT-Infrastruktur

Die sicherheitsrelevanten Parameter der OT-Infrastruktur SOLLTEN dokumentiert sein. In einem Bestandsverzeichnis SOLLTEN alle Software- und Systemkomponenten geführt werden. Hieraus SOLLTEN die eingesetzten Produkt- und Protokollversionen sowie die Zuständigkeiten hervorgehen. Zu den eingesetzten Komponenten SOLLTEN eventuelle Restriktionen der Hersteller oder regulatorische Auflagen wie etwa Zertifizierungen bestimmt sein. Diese Dokumentation und ein Systeminventar SOLLTE beispielsweise in einem Leitsystem geführt werden.

Zusätzlich SOLLTE ein aktueller Netzplan Zonen, Zonenübergänge (Conduits), eingesetzte Kommunikationsprotokolle und -verfahren sowie Außenschnittstellen dokumentieren. Bei den Schnittstellen SOLLTEN aktive Netzkomponenten wie auch manuelle Datentransferverfahren (z. B. durch Wechseldatenträger) berücksichtigt werden. Die Dokumentation SOLLTE Redundanzen, IP-Adressen bzw. -Bereiche und die Zuordnung zu physischen Sicherheitszonen erfassen.

Da die Dokumentation vertrauliche Informationen enthält, sind sämtliche Dokumente sicher abzulegen und mit einer Einstufung bzgl. der Schutzbedarfs zu versehen.

#### IND.1.A5 Entwicklung eines geeigneten Zonenkonzepts [IT-Betrieb]

Es SOLLTE ein Zonenkonzept vorliegen, welches verschiedene Level mit unterschiedlichen Schutzbedarfen definiert und die komplette OT-Infrastruktur sowie mindestens den Übergang zur Office-IT umfasst. Das Netz SOLLTE den Zonen entsprechend segmentiert sein und der Datenfluss zwischen den Zonen geeignet kontrolliert werden, um Angriffe aufwändiger, unwahrscheinlicher und leichter feststellbar zu machen. 

Es SOLLTE auch eine horizontale Segmentierung in unabhängige Funktionsbereiche (etwa Anlagen) erfolgen. Die einzelnen Zonen SOLLTEN so weit wie möglich im Betrieb voneinander unabhängig sein. Insbesondere die Zonen, in denen der technische Prozess gesteuert wird, SOLLTEN bei einem Ausfall der anderen Zonen oder deren bewusster Abkopplung nach einer Kompromittierung eine vorbestimmte Zeitspanne weiter betreibbar sein. Dieser Zeitraum SOLLTE im Rahmen der Risikoanalyse oder alternativ im Rahmen der Notfallplanung definiert und dokumentiert werden. Das Netz SOLLTE daher stabil im Sinn von manipulations- und fehlerresistent konzipiert werden. 

Alle Schnittstellen/Verbindungen zwischen den Zonen SOLLTEN einer Risikobetrachtung unterzogen sein. An den Außenschnittstellen SOLLTEN authentisierte Benutzer und integritätsgeschützte Protokolle eingesetzt werden.

#### IND.1.A6 Änderungsmanagement im OT-Betrieb

Für Änderungen an der OT SOLLTE ein Änderungsprozess (Change Management) definiert, dokumentiert und gelebt werden. Der Änderungsprozess SOLLTE gewährleisten, dass Änderungen geplant, dokumentiert, angemessen, auf unerwünschte Seiteneffekte und Funktionalität getestet, objektiv auf sicherheitsrelevante oder betriebliche Auswirkungen bewertet und freigegeben werden.

Es SOLLTE ein Konzept zur sicheren Erprobung von Änderungen vorliegen. Die Systemzeit der OT-Infrastruktur SOLLTE synchron gehalten werden. Dies SOLLTE mit einer externen Referenz erfolgen.

Weitere Informationen sind im Baustein OPS.1.2.1 Änderungsmanagement beschrieben.

#### IND.1.A7 Etablieren einer Berechtigungsverwaltung

Die Institution SOLLTE einen Prozess zur Verwaltung von Benutzerzugänge und zugeordneten Berechtigungen für den Zugriff auf die OT etablieren. Die Berechtigungsverwaltung SOLLTE den Prozess, die Durchführung und die Dokumentation für die Beantragung, Einrichtung und den Entzug von Berechtigungen umfassen.

Die Berechtigungsverwaltung SOLLTE gewährleisten, dass Berechtigungen nach dem Minimalprinzip vergeben und regelmäßig überprüft werden. In der Berechtigungsverwaltung SOLLTEN die Zugriffe auf IT-Systeme für Mitarbeiter, Administratoren und Dritte geregelt sein. Jeder Beteiligte SOLLTE regelmäßig zu den einzuhaltenden Regelungen geschult werden. Die Einhaltung SOLLTE überprüft und Fehlverhalten sanktioniert werden.

Weitere Informationen sind im Baustein ORP.4 Identitäts- und Berechtigungsmanagement beschrieben.

#### IND.1.A8 Sichere Administration [IT-Betrieb]

Für die Erstkonfiguration, Verwaltung (Administration) und Fernwartung in der OT SOLLTEN entweder sichere Protokolle oder aber abgetrennte Administrationsnetze mit entsprechendem Schutzbedarf genutzt werden. Der Zugang zu diesen Schnittstellen SOLLTE auf die Berechtigten eingeschränkt sein. Es SOLLTE nur der Zugriff auf die Systeme und Funktionen gewährt sein, welche für die jeweilige Administrationsaufgabe benötigt werden.

Die Systeme und Kommunikationskanäle, mit denen die Administration oder Fernwartung durchgeführt wird, SOLLTEN das gleiche Schutzniveau aufweisen wie die verwalteten OT-Komponenten. Jede Fernwartung und -überwachung SOLLTE durch die Institution autorisiert, überwacht und gesteuert werden. Dazu SOLLTE der Fernwartungszugang nur für die Nutzung aktiviert und danach wieder deaktiviert werden. Dies SOLLTE dokumentiert werden

Dabei SOLLTE darauf geachtet werden, dass es nicht möglich ist, unerwünschte Tunnel zur Umgehung von Sicherheitsmaßnahmen aufzubauen. Bei höherem Schutzbedarf SOLLTE zudem für kritische administrative Schritte ein Vier-Augen-Prinzip gelten.

#### IND.1.A9 Restriktiver Einsatz von Wechseldatenträgern und mobilen Endgeräten

Für die Nutzung von Wechseldatenträgern und mobilen Endgeräten SOLLTEN Regelungen für den Umgang aufgestellt und bekannt gemacht werden. Grundsätzlich SOLLTE der Einsatz von Wechseldatenträgern und mobilen Endgeräten in ICS-Umgebungen beschränkt werden. Für Medien und Geräte von Dienstleistern SOLLTEN ein Genehmigungsprozess und eine Anforderungsliste existieren. Die Vorgaben SOLLTEN jedem Dienstleister bekannt sein und von diesen schriftlich bestätigt werden.

Auf den OT-Komponenten SOLLTEN alle nicht benötigten Schnittstellen deaktiviert werden. An den aktiven Schnittstellen kann die Nutzung auf bestimmte Geräte bzw. Medien eingeschränkt werden.

Weitere Informationen sind im Baustein SYS.3.4 Mobile Datenträger beschrieben.

#### IND.1.A10 Monitoring, Protokollierung und Detektion [Bereichs-Sicherheitsbeauftragter]

Zur Begrenzung der möglichen Auswirkungen von Sicherheitsvorfällen SOLLTEN betriebs- und sicherheitsrelevante Ereignisse zeitnah identifiziert werden. Hierzu SOLLTE ein geeignetes Log- und Event-Management entwickelt und umgesetzt werden. Das Log- und Event-Management SOLLTE angemessene Maßnahmen zur Erhebung und Erkennung von sicherheitsrelevanten Ereignissen sowie einen Reaktionsplan (Security Incident Response) umfassen.

Der Reaktionsplan SOLLTE Verfahren zur Sicherheitsvorfallbehandlung festlegen. Darin abgedeckt sein SOLLTEN Klassifizierung von Ereignissen, Meldewege und Festlegung der einzubeziehenden Organisationseinheiten, Reaktionspläne zur Schadensbegrenzung, Analyse und Wiederherstellung von Systemen und Diensten sowie die Dokumentation und Nachbereitung von Vorfällen. Der Reaktionsplan SOLLTE regelmäßig getestet und auf Aktualität geprüft werden.

#### IND.1.A11 Sichere Beschaffung und Systementwicklung

Für Beschaffungen, Planungen oder Entwicklungen von ICS SOLLTEN Regelungen zur Informationssicherheit getroffen und dokumentiert werden. Die Unterlagen SOLLTEN Teil der Ausschreibung sein.

Bei Beschaffungen, Planungen oder Entwicklungen SOLLTE die Informationssicherheit in dem gesamten Lebenzyklus berücksichtigt werden. Voraussetzungen und Umsetzungshinweise für einen sicheren Betrieb von OT-Komponenten von Herstellern oder Integratoren SOLLTEN frühzeitig eingeplant und umgesetzt werden. Die Einhaltung und Umsetzung SOLLTE dokumentiert werden

Die Institution SOLLTE dokumentieren, wie sich das System in die Konzepte für Zonierung, Berechtigungs-, Schwachstellen-Management und Virenschutz einfügt und diese gegebenenfalls anpassen. Es SOLLTE geregelt sein, wie der Betrieb aufrechterhalten werden kann, falls einer der Partner keine Dienstleistungen mehr anbietet.

Weitere Informationen sind im Bausteinen OPS.2.1 Outsourcing-Nutzung beschrieben.

#### IND.1.A12 Etablieren eines Schwachstellen-Managements

Für den sicheren Betrieb einer ICS-Umgebung SOLLTE die Institution ein Schwachstellen-Management etablieren. Das Schwachstellen-Management SOLLTE Lücken in Software, Komponenten, Protokollen und Außenschnittstellen der Umgebung identifizieren und mögliche Handlungserfordernisse und -möglichkeiten (z. B. ein Patchmanagement) ableiten, bewerten und umsetzen.

Grundlage dafür SOLLTEN Schwachstellenmeldungen (Advisories) von Herstellern oder öffentlich verfügbare CERT-Meldungen sein. Ergänzend hierzu können organisatorische und technische Audits zur Schwachstellenanalyse durchgeführt werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### IND.1.A13 Notfallplanung für OT(A)

Bei hoher Verfügbarkeit SOLLTEN Notfallpläne für den Ausfall und für die Kompromittierung jeder Zone definiert, dokumentiert, nach jeder größeren Änderung getestet und regelmäßig geübt sein (siehe hierzu auch BSI-Standard 100-4).

Zudem SOLLTE ein wirksames Ersatzverfahren für den Ausfall der (Fern-) Administrationsmöglichkeit definiert, dokumentiert und getestet sein.

#### IND.1.A14 Starke Authentisierung an OT-Komponenten(CIA)

Zur sicheren Authentisierung von privilegierten Anwendern in Steuerungssystemen SOLLTE ein zentraler Verzeichnisdienst eingerichtet werden. Die Authentisierung SOLLTE durch den Einsatz mehrerer Faktoren (Wissen, Besitz, Biometrie) zusätzlich abgesichert werden.

Bei der Planung SOLLTE darauf geachtet werden, dass daraus entstehende Abhängigkeiten in der Benutzerauthentisierung bekannt sind und bei der Umsetzung der Lösung berücksichtigt werden.

Der zentrale Verzeichnisdienst SOLLTE NICHT zur Authentisierung von betrieblich erforderlichen technischen Konten dienen. Beim Einsatz eines Verzeichnisdienstes SOLLTEN lokale System- und Anwendungskennungen für Notfallsituationen eingerichtet und sicher hinterlegt werden.

Authentisierungssysteme, welche sensible Authentisierungsdaten verwalten, SOLLTEN angemessen vor unbefugtem Zugriff gesichert, Änderungen nachvollziehbar dokumentiert und auf Auffälligkeiten überwacht werden.

#### IND.1.A15 Prüfung und Überwachung von Berechtigungen(CIA)

Um die effektive Verifikation von Berechtigungen zu ermöglichen, SOLLTE die Institution ein Bestandsverzeichnis führen, welches alle vergebenen Zutritts-, Zugangs und Zugriffsrechte auf kritische Systeme enthält. Das Verzeichnis SOLLTE einerseits Antwort darauf geben können, welche Rechte ein bestimmter Benutzer effektiv hat, und andererseits, wer an einem bestimmten System über welche Rechte verfügt.

Alle kritischen administrativen Tätigkeiten SOLLTEN protokolliert werden. Der IT-Betrieb SOLLTE NICHT die Protokolle löschen oder manipulieren können.

#### IND.1.A16 Stärkere Abschottung der Zonen(IA)

Bei hoch schutzbedürftigen oder schlecht auf System- und Netzebene absicherbaren ICS-Umgebungen SOLLTEN vorbeugend Schnittstellensystemen mit Sicherheitsprüffunktionen eingesetzt werden um Risiken aus Außenanbindungen vorbeugen.

Wie in IND.1.A5 Entwicklung eines geeigneten Zonenkonzepts gefordert, SOLLTEN alle Außenschnittstellen der Umgebung einer Risikobetrachtung unterzogen werden. Aus den hiermit ermittelten Risiken SOLLTEN spezifische Einzelsicherungsmaßnahmen abgeleitet werden.

Durch Realisierung einer oder mehrerer Anbindungszonen (DMZ) in P-A-P-Struktur (durch Firewalls gekapselte Application Layer Gateways) KÖNNEN durchgängige Außenverbindungen terminiert werden und erforderliche Sicherheitsprüfungen (Virenschutz, Formatierung von Daten, Prüfung und Filterung von Inhalten, Medienbrüche) erfolgen, ohne dass Anpassungen an der ICS-Anlage notwendig sind.

Die Umsetzung dieser Anforderung erhöht die Perimetersicherheit. Ergänzende organisatorische und technische Maßnahmen SOLLTEN identifiziert und umgesetzt werden, um Risiken aus vorsätzlicher und versehentlicher Umgehung des Perimeters, wie etwa durch den Einsatz von Wechseldatenträgern oder Mobilgeräten, weiter zu reduzieren.

#### IND.1.A17 Regelmäßige Sicherheitsüberprüfung(I)

Die Sicherheitskonfiguration von OT-Komponenten SOLLTE in einem angemessenen Zyklus und/oder bedarfsorientiert bei plötzlich auftretenden neuen, bisher unbekannten Gefährdungen überprüft werden. Die Sicherheitsüberprüfung SOLLTE zumindest die exponierten Systeme mit Außenschnittstellen oder Benutzerinteraktion umfassen. 

Auch das realisierte Sicherheitskonzept SOLLTE regelmäßig überprüft werden.

Die Sicherheitsüberprüfung SOLLTE als Konfigurationsprüfung oder auch durch automatisierte Konformitätsprüfungen erfolgen. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Betriebs- und Steuerungstechnik" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27019] ISO/IEC TR 27019:2013

  

 Information technology- Security techniques- Information security management guidelines based in ISO/ IEC 27002 for process control systems specific on the energy utility industry, Internationale Organisation für Normung, 07.2013  
 <https://www.iso.org/standard/43759.html>

 
* #### [AHWAST] Ausführungshinweise zur Anwendung des Whitepaper - Anforderungen an sichere Steuerungs- und Telekommunikationssysteme (Version 1.1, 2014)

  

 BDEW Bundesverband der Energie- und Wasserwirtschaft e.V. und Oesterreichs E-Wirtschaft, Version 1.1, 2014  
 [https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
* #### [CSE] Empfehlungen für Fortbildungs-und Qualifizierungsmaßnahmen im ICS-Umfeld

  

 BSI-Veröffentlichungen zur Cyber-Sicherheit (BSI-CS 123), Bundesamt für Sicherheit in der Informationstechnik, 11.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_123.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_123.pdf)

 
* #### [ICSSK] ICS-Security-Kompendium

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2016  
 [https://www.bsi.bund.de/DE/Themen/Industrie\_KRITIS/Empfehlungen/ICS/empfehlungen\_node.html](https://www.bsi.bund.de/DE/Themen/Industrie_KRITIS/Empfehlungen/ICS/empfehlungen_node.html)

 
* #### [ICSSKfH] ICS-Security-Kompendium für Hersteller und Integratoren

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014  
 <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/ICS/ICS-Security-Kompendium-Hersteller.html>

 
* #### [IEC62443] IEC 62443-2-1:2010 Industrial communication networks - Network and system security - Part 2-1:

  

 Establishing an industrial automation and control system security program, International Electrotechnical Commission (IEC), 2010  
 <https://webstore.iec.ch/publication/7030>

 
* #### [WAST] Whitepaper Anforderungen an sichere Steuerungs- und Telekommunikationssysteme

  

 BDEW Bundesverband der Energie- und Wasserwirtschaft e.V, Version 1.1, 01.2015  
 [https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge](https://www.bdew.de/internet.nsf/id/it-sicherheitsempfehlunge?open&ccm)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Betriebs- und Steuerungstechnik" von Bedeutung.

* G 0.5 Naturkatastrophen
* G 0.6 Katastrophen im Umfeld
* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.39 Schadprogramme
* G 0.41 Sabotage
* G 0.42 Social Engineering
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

