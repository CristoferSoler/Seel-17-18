1 Beschreibung
--------------

### 1.1 Einleitung

Ein Verzeichnisdienst stellt in einem Datennetz Informationen über beliebige Objekte in einer definierten Art zur Verfügung. Mit einem Objekt können zugehörige Attribute gespeichert werden, zum Beispiel zu einer Benutzerkennung Namen und Vornamen des Benutzers, die Personalnummer und der Rechnername. Diese Daten können dann gleichermaßen von verschiedenen Applikationen verwendet werden. Der Verzeichnisdienst und seine Daten werden in der Regel von zentraler Stelle aus verwaltet.

Einige typische Anwendungsgebiete von Verzeichnisdiensten sind:

* Verwaltung von Adressbüchern, z. B. für Telefonnummern, E-Mail-Adressen, Zertifikate für elektronische Signaturen
* Ressourcen-Verwaltung, z. B. für Computer, Drucker, Scanner und andere Peripherie-Geräte
* Benutzer-Verwaltung, z. B. zur Verwaltung von Benutzerkonten und Benutzerberechtigungen
* Authentisierung, z. B. zur Anmeldung an Betriebssystemen oder Anwendungen
Verzeichnisdienste sind auf Lesezugriffe hin optimiert, da Daten aus dem Verzeichnisdienst typischerweise abgerufen werden. Schreibzugriffe, wie das Erstellen, Ändern oder Löschen von Einträgen, sind seltener notwendig.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, allgemeine Verzeichnisdienste sicher zu betreiben sowie die damit verarbeiteten Informationen angemessen zu schützen. 

### 1.3 Abgrenzung

Dieser Baustein betrachtet allgemeine Sicherheitsaspekte von Verzeichnisdiensten unabhängig vom eingesetzten Produkt. Für produktspezifische Sicherheitsaspekte existieren im IT-Grundschutz-Kompendium weitere Bausteine, die zusätzlich auf den jeweiligen Verzeichnisdienst anzuwenden sind.

Ein Beispiel hierfür ist Active Directory von Microsoft (siehe APP.2.2 *Active Directory*). Andere Verzeichnisdienste basieren auf dem frei verfügbaren OpenLDAP (siehe APP.2.3 *OpenLDAP*), das in vielen Unix-basierten Systemen verwendet und beispielsweise auch von Apples macOS genutzt wird. Bausteine zu Server-Systemen, auf denen Verzeichnisdienste üblicherweise betrieben werden, sind in der Schicht SYS.1 *Server* des IT-Grundschutz-Kompendiums aufgeführt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Allgemeiner Verzeichnisdienst von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichende Planung des Einsatzes von Verzeichnisdiensten

Die Sicherheit von Verzeichnisdiensten stützt sich stark auf die Sicherheit des Basisbetriebssystems und hierbei vor allem auf die Dateisystemsicherheit. Verzeichnisdienste lassen sich auf einer Vielzahl von Betriebssystemen installieren und betreiben, wodurch sich eine große Vielfalt der vorzunehmenden Sicherheitseinstellungen ergeben kann. Diese Vielfalt erhöht die Anforderungen an die Planung und setzt entsprechende Kenntnisse des als Basis dienenden Betriebssystems voraus. Sollte die entstehende Gesamtlösung sehr heterogen oder komplex sein, kann ein nicht ausreichend geplanter Einsatz des Verzeichnisdienstes im Wirkbetrieb zu Sicherheitslücken führen. Da bei Verzeichnisdiensten außerdem eine rollenbasierte Administration der Verzeichnisdatenbank üblich ist sowie einzelne Administrationsaufgaben delegiert werden können, besteht bei fehlerhafter Planung der Administrationsaufgaben die Gefahr, dass das System unsicher oder unzulänglich administriert wird.

### 2 2 Fehlerhafte oder unzureichende Planung der Partitionierung und Replizierung im Verzeichnisdienst

Bei der Partitionierung handelt es sich um eine Aufteilung der Verzeichnisdaten eines Verzeichnisdienstes in einzelne Teilbereiche (Partitionen). Die Replizierung von Partitionen des Verzeichnisdienstes dient in der Regel zur Lastverteilung. Weiter wird durch die Redundanz in der Datenhaltung die Ausfallsicherheit verbessert und somit die Verfügbarkeit erhöht. Von entscheidender Bedeutung ist deshalb auch hier eine geeignete Planung, da nachträgliche Änderungen an den Partitions- und Replikationseinstellungen zwar möglich sind, aber unter Umständen Probleme nach sich ziehen können. Wird die Partitionierung und die Replizierung des Verzeichnisdienstes fehlerhaft oder unzureichend geplant, kann dies zu Datenverlusten sowie Inkonsistenzen in der Datenhaltung, zu einer mangelhaften Verfügbarkeit des Verzeichnisdienstes und zu einer insgesamt schlechten Systemperformance bis hin zu Ausfällen führen.

### 2 3 Fehlerhafte oder unzureichende Planung des Zugriffs auf den Verzeichnisdienst

Zugangs- und Zugriffsrechten im Kontext eines Verzeichnisdienstes zu verwalten, ist eine äußerst arbeitsintensive Aufgabe, bei der im Extremfall viele manuelle Arbeitsschritte erforderlich sind, die zu Fehlern und Mängeln im Überblick über durchgeführte Arbeiten führen können. Eine unzureichende Planung, ob und welche Daten im Klartext übertragen werden dürfen, kann Inkonsistenzen oder Widersprüche zu organisationsinternen Sicherheitsrichtlinien hervorrufen. Auch kann eine fehlerhafte Planung der Sicherheitsmaßnahmen und -techniken des Verzeichnisdienstes zum Schutz vertraulicher Daten zu Inkompatibilitäten bis hin zum Ausfall der Verschlüsselung führen, was sich unmittelbar auf die Vertraulichkeit und die Integrität auswirken kann.

### 2 4 Fehlerhafte Administration von Zugangs- und Zugriffsrechten

Zugangsrechte zu einem IT-System und Zugriffsrechte auf gespeicherte Daten und IT-Anwendungen dürfen nur in dem Umfang eingeräumt werden, wie sie für die durchzuführenden Aufgaben erforderlich sind. Dies gilt auch für die Berechtigungen, die über einen Verzeichnisdienst verwaltete Benutzer und Gruppen erhalten. Werden diese Rechte fehlerhaft administriert, so kommt es zu Betriebsstörungen, falls erforderliche Rechte nicht zugewiesen wurden. Andererseits kann es zu Sicherheitslücken kommen, falls über die notwendigen Rechte hinaus weitere vergeben werden. Sofern die Zugriffsrechte im Verzeichnisdienst falsch oder inkonsistent vergeben werden, ist dadurch die Sicherheit des Gesamtsystems erheblich gefährdet. Ein besonders kritischer Punkt sind auch die Administrationsrechte. Werden diese Rechte falsch vergeben, kann das gesamte Administrationskonzept in Frage gestellt oder unter Umständen sogar die Administration des Verzeichnissystems selbst blockiert werden.

### 2 5 Fehlerhafte Konfiguration des Zugriffs auf Verzeichnisdienste

In vielen Einsatzszenarien müssen weitere Applikationen, wie Internet- oder Intranet-Anwendungen, auf den Verzeichnisdienst zugreifen. Eine Fehlkonfiguration kann dazu führen, dass Zugriffsrechte falsch vergeben werden oder unautorisiert auf den Verzeichnisdienst zugegriffen werden kann, oder dass Daten zur Authentisierung im Klartext übermittelt und somit unverschlüsselte Informationen ausgespäht werden können.

### 2 6 Ausfall von Verzeichnisdiensten und Verschlüsselung

Durch technisches Versagen aufgrund von Hardware- oder Software-Problemen können Verzeichnisdienste oder Teile davon ausfallen. Als Folge sind die im Verzeichnis gehaltenen Daten temporär nicht mehr zugänglich. Im Extremfall können Daten verloren gehen. Dadurch können Geschäftsprozesse und interne Arbeitsabläufe behindert werden. Sind funktionsfähige Kopien der ausgefallenen Systemteile vorhanden, so ist der Zugriff zwar weiterhin möglich, jedoch unter Umständen je nach gewählter Netztopologie nur mit eingeschränkter Leistungsfähigkeit.

### 2 7 Kompromittierung von Verzeichnisdiensten durch unbefugten Zugriff

Wenn es einem Angreifer gelungen ist, eine notwendige Authentisierung gegenüber dem Verzeichnisdienst erfolgreich zu umgehen, kann er danach im Allgemeinen auf eine Vielzahl von Daten zugreifen, für die er keine Berechtigung besitzen sollte. Somit kann der gesamte Verzeichnisdienst kompromittiert werden. Außerdem könnten Unbefugten durch erweiterte Berechtigungen auf Netzressourcen oder Dienste zugreifen. Dies kann dazu führen, dass ein Angreifer alle Verteidigungsmaßnahmen des Verzeichnisdienstes umgeht. Dadurch könnte das betroffene System beeinträchtigt oder gar zerstört werden. Die Sicherheit eines Verzeichnisdienstes kann ebenfalls gefährdet werden, wenn anonyme Benutzer zugelassen werden. Dadurch, dass deren Identität nicht überprüft wird, können anonyme Benutzer zunächst beliebige Abfragen an den Verzeichnisdienst richten, durch die sie zumindest Teilinformationen über dessen Struktur und Inhalt erlangen. Wenn anonyme Zugriffe zugelassen werden, sind außerdem DoS-Attacken auf den Verzeichnisdienst leichter durchführbar, da Angreifer mehr Zugriffsmöglichkeiten haben, die nur schlecht kontrollierbar sind.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Allgemeiner Verzeichnisdienst aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.2.1.A1 Erstellung einer Sicherheitsrichtlinie für Verzeichnisdienste

Es MUSS eine Sicherheitsrichtlinie für den Verzeichnisdienst erstellt werden. Diese SOLLTE mit dem übergreifenden Sicherheitskonzept der gesamten Institution abgestimmt sein.

#### APP.2.1.A2 Planung des Einsatzes von Verzeichnisdiensten [Datenschutzbeauftragter, Fachverantwortliche]

Der Einsatz von Verzeichnisdiensten MUSS sorgfältig geplant werden. Neben der Festlegung der Nutzung des Verzeichnisdienstes MUSS ein Modell aus Objektklassen und Attributtypen entwickelt werden, das den Ansprüchen der vorgesehenen Nutzungsarten genügt. Bei der Planung des Verzeichnisdienstes MÜSSEN Personalvertretung und Datenschutzbeauftragter beteiligt werden. Ein bedarfsgerechtes Berechtigungskonzept zum Verzeichnisdienst MUSS entworfen werden. Generell SOLLTE die geplante Verzeichnisdienst-Struktur vollständig dokumentiert werden. Es SOLLTEN Maßnahmen geplant werden, die das unbefugte Sammeln von Daten aus dem Verzeichnisdienst unterbinden.

#### APP.2.1.A3 Einrichtung von Zugriffsberechtigungen auf Verzeichnisdienste [Fachverantwortliche]

Die administrativen Aufgaben für die Administration des Verzeichnisdienstes selbst sowie für die eigentliche Verwaltung der Daten MÜSSEN strikt getrennt werden. Die administrativen Tätigkeiten SOLLTEN so delegiert werden, dass sich möglichst keine Überschneidungen ergeben. Alle administrativen Aufgabenbereiche und Berechtigungen SOLLTEN ausreichend dokumentiert werden.

Die Zugriffsrechte der Benutzer- und Administratorengruppen MÜSSEN anhand der erstellten Sicherheitsrichtlinie konfiguriert und umgesetzt werden. Bei einer eventuellen Zusammenführung mehrerer Verzeichnisdienst-Bäume MÜSSEN die resultierenden effektiven Rechte kontrolliert werden.

#### APP.2.1.A4 Sichere Installation von Verzeichnisdiensten

Es MUSS ein Konzept für die Installation erstellt werden, nach dem Administrations- und Zugriffsberechtigungen bereits bei der Installation des Verzeichnisdienstes konfiguriert werden.

#### APP.2.1.A5 Sichere Konfiguration und Konfigurationsänderungen von Verzeichnisdiensten

Der Verzeichnisdienst MUSS sicher konfiguriert werden. Für die sichere Konfiguration einer Verzeichnisdienstes-Infrastruktur MÜSSEN neben dem Server auch die Clients (Rechner und Programme) einbezogen werden. 

Administrative Zugänge zum Verzeichnisdienst MÜSSEN geschützt werden. Bei der Durchführung von Konfigurationsänderungen der vernetzten IT-Systeme SOLLTEN die Benutzer rechtzeitig über Wartungsarbeiten informiert werden. Vor den Konfigurationsänderungen SOLLTEN von allen betroffenen Dateien und Verzeichnissen Datensicherungen angefertigt werden.

#### APP.2.1.A6 Sicherer Betrieb von Verzeichnisdiensten

Die Sicherheit des Verzeichnisdienstes MUSS im Betrieb permanent aufrechterhalten werden. Alle für den Betrieb eines Verzeichnisdienst-Systems betreffenden Richtlinien, Regelungen und Prozesse SOLLTEN dokumentiert werden. Der Zugriff auf alle Administrationswerkzeuge MUSS für normale Benutzer unterbunden werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Allgemeiner Verzeichnisdienst. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.2.1.A7 Erstellung eines Sicherheitskonzepts für den Einsatz von Verzeichnisdiensten

Durch das Sicherheitskonzept für Verzeichnisdienste SOLLTEN sämtliche sicherheitsbezogenen Themenbereiche eines Verzeichnisdienstes geregelt werden. Die daraus entwickelten Sicherheitsrichtlinien SOLLTEN schriftlich festgehalten und im erforderlichen Umfang den Benutzern des Verzeichnisdienstes mitgeteilt werden.

#### APP.2.1.A8 Planung einer Partitionierung und Replikation im Verzeichnisdienst

Bei einer Partitionierung SOLLTE auf die Verfügbarkeit und den Schutzbedarf des Verzeichnisdienstes geachtet werden. Die Partitionierung des Verzeichnisdienstes SOLLTE schriftlich dokumentiert werden, so dass sie manuell wieder rekonstruiert werden kann. Um die Replikationen zeitgerecht ausführen zu können, SOLLTE eine ausreichende Bandbreite sichergestellt werden.

#### APP.2.1.A9 Geeignete Auswahl von Komponenten für Verzeichnisdienste [Fachverantwortliche]

Für den Einsatz eines Verzeichnisdienstes SOLLTEN geeignete Komponenten identifiziert werden. Es SOLLTE ein Kriterienkatalog erstellt werden, aufgrund dessen die Komponenten für den Verzeichnisdienst ausgewählt und beschafft werden. Im Rahmen der Planung und Konzeption des Verzeichnisdienstes SOLLTEN Anforderungen an dessen Sicherheit in Abhängigkeit vom Einsatzzweck formuliert werden.

#### APP.2.1.A10 Schulung zu Administration und Betrieb von Verzeichnisdiensten

Die Administratoren SOLLTEN mit allen Sicherheitsmechanismen und -aspekten von Verzeichnisdiensten in ihrem Tätigkeitsbereich vertraut sein. Sie SOLLTEN vor der Einrichtung sowie anschließend regelmäßig hierzu geschult werden.

#### APP.2.1.A11 Einrichtung des Zugriffs auf Verzeichnisdienste

Der Zugriff auf den Verzeichnisdienst SOLLTE entsprechend der Sicherheitsrichtlinie konfiguriert werden. Wird der Verzeichnisdienst als Server im Internet eingesetzt, so SOLLTEN er entsprechend durch ein Sicherheitsgateway geschützt werden. Sollen anonymen Benutzern auf einzelne Teilbereiche des Verzeichnisbaums weitergehende Zugriffe eingeräumt werden, so SOLLTE ein gesondertes Benutzerkonto, ein sogenannter Proxy-User, für den anonymen Zugriff eingerichtet werden. Des Weiteren SOLLTEN die Zugriffsrechte für diesen Proxy-User hinreichend restriktiv vergeben werden. Sie SOLLTEN wieder komplett entzogen werden, wenn der Account nicht mehr gebraucht wird. Um die unnötige Herausgabe sicherheitssensitiver Informationen zu verhindern, SOLLTE die Suchfunktion des Verzeichnisdienstes dem Einsatzzweck angemessen eingeschränkt werden.

#### APP.2.1.A12 Überwachung von Verzeichnisdiensten

Zur Überwachung von Verzeichnisdiensten SOLLTE ein Überwachungskonzept entworfen und umgesetzt werden. Verzeichnisdienst-spezifische Ereignisse und Ereignisse des Betriebssystems SOLLTEN beobachtet, protokolliert und ausgewertet werden.

#### APP.2.1.A13 Absicherung der Kommunikation mit Verzeichnisdiensten

Der Datenaustausch zwischen Client und Verzeichnisdienst-Server SOLLTE abgesichert werden, dies gilt insbesondere bei Außenanbindungen. Es SOLLTE definiert werden, auf welche Daten zugegriffen werden darf. Im Falle einer serviceorientierten Architektur (SOA) SOLLTEN zum Schutz von Service-Einträgen in einer Service-Registry sämtliche Anfragen an die Registratur auf Gültigkeit des Benutzers überprüft werden.

#### APP.2.1.A14 Geregelte Außerbetriebnahme eines Verzeichnisdienstes [Fachverantwortliche]

Bei einer Außerbetriebnahme des Verzeichnisdienstes SOLLTE sichergestellt sein, dass weiterhin benötigte Rechte bzw. Informationen in ausreichendem Umfang zur Verfügung stehen, alle anderen aber gelöscht werden. Zudem SOLLTEN die Benutzer darüber informiert werden, wenn ein Verzeichnisdienst außer Betrieb genommen wird. Bei der Außerbetriebnahme einzelner Partitionen eines Verzeichnisdienstes SOLLTE darauf geachtet werden, dass dadurch andere Partitionen nicht beeinträchtigt werden.

#### APP.2.1.A15 Migration von Verzeichnisdiensten

Bei einer geplanten Migration von Verzeichnisdiensten SOLLTE vorab ein Migrationskonzept erstellt werden. Die Schema-Änderungen, die am Verzeichnisdienst vorgenommen wurden, SOLLTEN dokumentiert werden. Weitreichende Berechtigungen, die zur Durchführung der Migration des Verzeichnisdienstes verwendet wurden, SOLLTEN wieder zurückgesetzt werden. Die Zugriffsrechte für Verzeichnisdienst-Objekte bei Systemen, die von Vorgängerversionen aktualisiert bzw. von anderen Verzeichnissystemen übernommen wurden, SOLLTEN aktualisiert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.2.1.A16 Erstellung eines Notfallplans für den Ausfall eines Verzeichnisdienstes(CIA)

Im Rahmen der Notfallvorsorge SOLLTE eine bedarfsgerechte Notfallplanung für Verzeichnisdienste durchgeführt werden. Für den Ausfall wichtiger Verzeichnisdienst-Systeme SOLLTEN Notfallpläne vorliegen. Alle Notfall-Prozeduren für die gesamte Systemkonfiguration der Verzeichnisdienst-Komponenten SOLLTEN dokumentiert werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeiner Verzeichnisdienst" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISFTM12] The Standard of Good Practice - Area TM 1.2 Security Event Logging

  

 insbesondere Area TM 1.2 Security Event Logging, Information Security Forum (ISF), 06.2016 

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
* #### [TKOM1] Telekom - Privacy and Security Assessment Verfahren

  

 Proxyserver, Deutsche Telekom, 10.2016  
 <https://www.telekom.com/de/verantwortung/datenschutz-und-datensicherheit/sicherheit/sicherheit/privacy-and-security-assessment-verfahren-342724>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Allgemeiner Verzeichnisdienst" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
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
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

