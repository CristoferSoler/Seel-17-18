1 Beschreibung
--------------

### 1.1 Einleitung

*Samba* ist ein frei verfügbarer und vollwertiger Active Directory Domain Controller (AD DC), der Authentisierungs-, Datei- und Druckdienste bereitstellen kann und dadurch die Interoperabilität zwischen der Windows- und Unix-Welt ermöglicht. *Samba* führt viele unterschiedliche Protokolle und Techniken zusammen. Dazu gehört beispielsweise das *Server-Message-Block-(SMB)-*Protokoll, auch bekannt unter dem neueren Namen *Common Internet File System* (CIFS). Als *Samba*-Server werden Server bezeichnet, auf denen *Samba* betrieben wird. In der Regel sind das Linux-Server. 

Wurde *Samba* korrekt konzipiert und ordentlich konfiguriert, interagiert die Anwendung mit einem Windows-Client oder -Server, als ob er selbst ein Windows-System wäre.

### 1.2 Zielsetzung

Ziel des Bausteins ist es darzustellen, wie *Samba* in Institutionen sicher eingesetzt werden kann und wie sich die durch Samba bereitgestellten Informationen schützen lassen.

### 1.3 Abgrenzung

Dieser Baustein betrachtet *Samba* als Authentisierungs-, Datei- und Druckdienst. Da *Samba* in der Regel auf Linux-Servern eingesetzt wird und dort aus der Windows-Server-Welt bekannte Dienste darstellt, sind die Sicherheitsaspekte der Bausteine SYS.1.1 *Allgemeiner Server* und SYS.2.1 *Server unter Linux* zu berücksichtigen. Sicherheitsanforderungen für Drucker, Fileserver oder Verzeichnisdienste sind dagegen nicht Bestandteil dieses Bausteins, sondern werden in den Bausteinen SYS.4.1 *Drucker, Kopierer und Multifunktionsgeräte*, APP.2.1 *Allgemeiner Verzeichnisdienst* und APP.3.6 *DNS-Server* sowie APP.2.3 *OpenLDAP*, auch wenn die *Samba*-internen DNS- und LDAP-Dienste verwendet werden, beschrieben. Des Weiteren sind aufgrund der *Samba*-Funktionen, die Bausteine APP.3.3 *Fileserver* und APP.2.2 *Active Directory* zu berücksichtigen.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich* Samba* von besonderer Bedeutung:

### 2 1 Abhören ungeschützter Kommunikationsverbindungen von Samba

Wenn Angreifer ungeschützte Kommunikationsverbindungen von *Samba* abhören, können Informationen abgefangen und missbraucht werden. Beim Dateitransfer zwischen Linux-Servern, Windows-Servern und Clients werden oftmals Protokolle ohne umfangreiche Sicherheitseigenschaften eingesetzt, sodass sowohl Authentifizierungs- als auch Nutzdaten für Dritte zugänglich sind und von Unberechtigten missbraucht werden könnten. Das kann dazu führen, dass schützenswerte Informationen aus der Institution fließen.

### 2 2 Fehlerhafte Protokollierung in Samba

Nicht sachgerecht gestaltete oder fehlende Protokollierung in *Samba* kann zu Sicherheitsproblemen führen. Ohne eine angemessene Protokollierung bleiben Fehler oder Angriffe unerkannt und es können keine Präventivmaßnahmen und Indikatoren für Frühwarnsysteme definiert werden.

### 2 3 Fehlerhafte Notfallvorsorge in Samba

Auch Defizite bei der Notfallvorsorge können zu längeren Ausfallzeiten von *Samba* führen. So kann sich etwa nach einen erfolgten Angriff eine notwendige Neuinstallation verzögern, wenn Installationspakete nicht verfügbar sind. Vorhandene Installationspakete können wiederum zu unerwünschten Ergebnissen führen, wenn keine Versionsverwaltung für die Konfigurationsdateien verwendet wurde oder Kompilierungs- sowie Installationsoptionen der *Samba*-Server nicht vorgehalten werden.

### 2 4 Fehlende Anpassung von Samba

Um einige Fähigkeiten des *Samba*-Servers zu zeigen und um den Administratoren einen schnellen Einstieg zu ermöglichen, wird während der Installation des *Samba*-Servers die Konfigurationsdatei *smb.conf* mit Standardeinstellungen erzeugt. Mit den in dieser Datei voreingestellten Optionen kann der *Samba*-Server im Anschluss gestartet werden. Wird diese Datei unbedacht ohne weitere Einstellungen benutzt, kann das zu erheblichen Sicherheitslücken führen. Doch auch wenn die Datei geändert wird, können Fehler auftreten, die dazu führen, dass vertrauliche Informationen eingesehen werden können oder dass die Sicherheit, die Verfügbarkeit und die Leistung der Dienste eines *Samba*-Servers beeinträchtigt werden.

### 2 5 Software-Schwachstellen oder -Fehler in Samba

*Samba* ist eine freie Software, die innerhalb einer Community erstellt und weiterentwickelt wird. Eine gleichmäßige Qualität des Quellcodes kann daher nicht gewährleistet werden. Das kann zu Software-Schwachstellen oder -Fehlern und damit zu schwerwiegenden Sicherheitslücken in der Anwendung oder allen damit vernetzten IT-Systemen führen. Angreifer können solche Sicherheitslücken für unterschiedliche Angriffe nutzen. So beispielsweise, um Schadsoftware einzuschleusen und damit möglicherweise unbefugt an schützenswerte Informationen, wie vertrauliche Daten oder Dokumente und Zugangsdaten, zu gelangen. Ferner können Angreifer über Sicherheitslücken IT-Systeme manipulieren, was dazu führen kann, dass sich diese nicht mehr benutzen lassen oder nur noch fehlerhaft funktionieren.

### 2 6 Unberechtigte Nutzung oder Administration von Samba

Unbefugte können durch die Nutzung von Anwendungen oder Systemen an vertrauliche Informationen gelangen, diese manipulieren oder Störungen verursachen, sodass sie *Samba* unberechtigt administrieren können. Besonders kritisch ist es, wenn Konfigurationswerkzeuge wie z. B. das *Samba Web Administration Tool* (SWAT) eingesetzt werden. SWAT war bis vor Version 4 ein fester Bestandteil von *Samba*, wurde aber von den *Samba*-Entwicklern gering priorisiert. Daher wurden auch schwächere oder gar keine Sicherheitsmechanismen implementiert, beispielsweise wurde HTTPS nicht unterstützt.

### 2 7 Fehlerhafte Administration von Samba

Sind die Administratoren mit den umfangreichen Funktionen, Komponenten, Optionen und Konfigurationseinstellungen von *Samba* zu wenig vertraut, kann dies zu weitreichenden Komplikationen führen. So können Fehlkonfigurationen des DNS oder des Benutzer- und Rechtemanagements dazu führen, dass Unbefugte auf Ressourcen zugreifen können. Des Weiteren kann dies zu Betriebsunterbrechungen führen oder es können schützenswerte Informationen offengelegt werden.

### 2 8 Schadprogramme im Umfeld von Samba-Diensten

Wird *Samba* auf Linux-Systemen als Dateiserver eingesetzt, dann ist der Server selbst nicht direkt anfällig für Windows-Schadprogramme. Diese können aber in infizierten Dateien enthalten sein, die darauf abgelegt sind. Durch das *Samba*-System werden dann diese infizierten Dateien allen angebundenen Windows-Clients bereitgestellt und somit aktiv verbreitet.

### 2 9 Datenverlust bei Samba

Ein Datenverlust wirkt sich erheblich auf den IT-Einsatz aus. Wenn geschäftsrelevante Informationen zerstört oder verfälscht werden, können dadurch Geschäftsprozesse und Fachaufgaben verzögert oder gar nicht mehr ausgeführt werden. Bei *Samba* ist beispielsweise zu beachten, dass sich die Eigenschaften der Dateisysteme unter Windows und Unix erheblich voneinander unterscheiden. Deswegen ist nicht immer sichergestellt, dass die Zugriffsrechte unter Windows aufrechterhalten bleiben. Auch können dadurch Informationen zu *Alternate Data Streams* (ADS) und DOS-Attributen verloren gehen.

### 2 10 Integritätsverlust schützenswerter Informationen bei Samba

Wenn Informationen nicht mehr integer sind, kann es dadurch zu vielen Problemen kommen. Informationen können dann im einfachsten Fall nicht mehr gelesen, also auch nicht mehr weiterverarbeitet werden. *Samba* selbst legt wichtige Betriebsdaten in Datenbanken im *Trivial-Database*-(TDB)-Format ab. Sollten diese Datenbanken vom Betriebssystems nicht ausreichend leistungsfähig und konsistent behandelt werden, können sie Probleme verursachen, wenn *Samba*-Dienste benutzt werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich *Samba* aufgeführt. Grundsätzlich ist der IT-Betrieb dafür zuständig, die Anforderungen zu erfüllen. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.3.4.A1 Planung des Einsatzes eines Samba-Servers [Leiter IT]

Die Einführung eines *Samba*-Servers MUSS sorgfältig geplant und geregelt werden. Dabei MUSS abhängig vom Einsatzszenario definiert werden, welche Aufgaben der *Samba*-Server zukünftig erfüllen soll, in welcher Betriebsart er daher betrieben wird und welche Komponenten von *Samba* und welche weiteren Komponenten dafür erforderlich sind.

Soll die Cluster-Lösung CTDB (Cluster Trivia Data Base) eingesetzt werden, MUSS die Einführung von Samba sorgfältig konzeptioniert werden. Wenn *Samba* die Active-Directory-(AD)-Dienste auch für Linux- und Unix-Systeme bereitstellen soll, MUSS die Einführung sorgfältig geplant und die Installation getestet werden. Des Weiteren MUSS das Authentisierungsverfahren für das AD sorgfältig konzipiert und implementiert werden. Die Einführung und die Reihenfolge, in der die *Stackable-Virtual-File-System-*(VFS)-Module ausgeführt werden, MUSS sorgfältig konzipiert und die Umsetzung dokumentiert werden.

Wird IPv6 unter Samba benutzt, MUSS auch das sorgfältig geplant und zudem in einer betriebsnahen Testumgebung auf eine fehlerfreie Integration hin überprüft werden.

#### APP.3.4.A2 Sichere Grundkonfiguration eines Samba-Servers

Nachdem der *Samba*-Server installiert wurde, MUSS der Dienst sicher konfiguriert werden. Hierfür MÜSSEN unter anderem Einstellungen für die Zugriffskontrollen, aber auch Einstellungen, welche die Leistungsfähigkeit des Servers beeinflussen, angepasst werden. Es MUSS sichergestellt werden, dass die Zugriffsberechtigungen für jeden Benutzer individuell bestimmt werden.

Generell MUSS sichergestellt werden, dass nur ausgewählten Benutzern und Benutzergruppen erlaubt wird, sich mit dem *Samba*-Dienst zu verbinden und dass Benutzer nur auf die Informationen innerhalb ihrer Freigaben zugreifen können.

*Samba* MUSS so konfiguriert werden, dass Verbindungen nur von sicheren Hosts und Netzen entgegengenommen werden und dass es sich nur mit sicheren Netzadressen verbindet. Änderungen an der Konfiguration SOLLTEN sorgfältig dokumentiert werden, sodass zu jeder Zeit nachvollzogen werden kann, wer aus welchem Grund was geändert hat. Dabei MUSS nach jeder Änderung überprüft werden, ob die Syntax noch korrekt ist.

Zusätzliche Softwaremodule, wie SWAT, DÜRFEN NICHT installiert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Samba. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.3.4.A3 Sichere Konfiguration des Betriebssystems für einen Samba-Server

Datenbanken im Trivial-Database-(TDB)-Format SOLLTEN NICHT auf einer Partition gespeichert werden, die ReiserFS als Dateisystem benutzt. Wird eine *netlogon*-Freigabe konfiguriert, SOLLTEN unberechtigte Benutzer NICHT Dateien in dieser Freigabe modifizieren können.

Das Betriebssystem des *Samba*-Servers SOLLTE Access Control Lists (ACLs) in Verbindung mit dem eingesetzten Dateisystem unterstützen. Zusätzlich SOLLTE sichergestellt werden, dass das Dateisystem mit den passenden Parametern eingebunden wird.

Die Voreinstellungen von *SMB* *Message Signing* SOLLTEN beibehalten werden, sofern sie nicht im Widerspruch zu den existierenden Sicherheitsrichtlinien im Informationsverbund stehen. Mit einem lokalen Paketfilter SOLLTEN Ports, über die der *Samba*-Server nicht erreichbar sein soll, geblockt werden.

Es SOLLTE *Kerberos* eingesetzt werden, um die Schwachstellen von NT LAN-Manager (NTLM) oder NTLMv2 sowie eine zu hohe Netzlast zu vermeiden. Wird mit *Kerberos* authentisiert, SOLLTE der zentrale Zeitserver lokal auf dem Domain Controller installiert werden. Der NTP-Dienst SOLLTE so gehärtet werden, dass nur autorisierte Clients die Zeit abfragen können.

#### APP.3.4.A4 Sicherstellung der NTFS-Eigenschaften auf einem Samba-Server

Wird eine Version von *Samba* eingesetzt, die im *New Technology File System* (NTFS) sogenannte *Alternate Data Streams* (ADS) nicht abbilden kann, SOLLTE sichergestellt werden, dass Dateisystemobjekte keine ADS mit wichtigen Informationen enthalten, bevor diese über Systemgrenzen hinweg kopiert oder verschoben werden.

#### APP.3.4.A5 Sichere Konfiguration der Zugriffssteuerung bei einem Samba-Server

Die von *Samba* standardmäßig verwendeten Parameter, mit denen DOS-Attribute auf das Linux-Dateisystem abgebildet werden, SOLLTEN NICHT verwendet werden. Stattdessen SOLLTE *Samba* so konfiguriert werden, dass es DOS-Attribute und die Statusindikatoren zur Vererbung (Flag) in *Extended Attributes* speichert. Die Freigaben SOLLTEN ausschließlich über die Registry verwaltet werden.

Ferner SOLLTEN die effektiven Zugriffsberechtigungen auf die Freigaben des *Samba*-Servers ebenso wie die Protokolldateien regelmäßig überprüft werden.

#### APP.3.4.A6 Sichere Konfiguration von Winbind unter Samba

Der Einsatz von *Winbind* SOLLTE sorgfältig geplant und geregelt werden. Für jeden Windows-Domänenbenutzer SOLLTE im Betriebssystem des Servers ein Benutzerkonto mit allen Gruppenmitgliedschaften vorhanden sein. Falls das nicht möglich ist, SOLLTE *Winbind* eingesetzt werden. Dabei SOLLTE *Winbind* Domänen-Benutzernamen in eindeutige Linux-Benutzernamen umsetzen. Hierbei SOLLTE beachtet werden, dass Kollisionen zwischen lokalen Linux-Benutzern und Domänen-Benutzern verhindert werden.

Des Weiteren SOLLTEN die PAM (*Pluggable Authentication Modules*) eingebunden werden.

#### APP.3.4.A7 Sichere Konfiguration von DNS unter Samba

Wenn *Samba* als DNS-Server eingesetzt wird, SOLLTE die Einführung sorgfältig geplant und die Umsetzung vorab getestet werden. 

Da *Samba* verschiedene AD-Integrationsmodi unterstützt, SOLLTEN die DNS-Einstellungen entsprechend dem Verwendungsszenario von *Samba* vorgenommen werden. Wird *Samba* als primärer AD DC verwendet, SOLLTE der DNS-Dienst auf dem *Samba-*Server installiert und sorgfältig konfiguriert werden.

#### APP.3.4.A8 Sichere Konfiguration von LDAP unter Samba

Werden die Benutzer unter *Samba* mit LDAP verwaltet, SOLLTE das sorgfältig geplant und dokumentiert werden. Die Zugriffsberechtigungen auf das LDAP SOLLTEN mittels ACLs geregelt werden.

#### APP.3.4.A9 Sichere Konfiguration von Kerberos unter Samba

Zur Authentisierung SOLLTE das von *Samba* implementierte *Heimdal Kerberos Key Distribution Center* (KDC) verwendet werden. Es SOLLTE darauf geachtet werden, dass die von *Samba* vorgegebene Kerberos-Konfigurationsdatei verwendet wird. Es SOLLTEN nur ausreichend sichere Verschlüsselungsverfahren für Kerberos-Tickets benutzt werden.

#### APP.3.4.A10 Sicherer Einsatz externer Programme auf einem Samba-Server

Da externe Programme Einfallstore für Angreifer bieten, SOLLTE sichergestellt werden, dass *Samba* nur überprüfte und vertrauenswürdige externe Programme aufruft.

#### APP.3.4.A11 Sicherer Einsatz von Kommunikationsprotokollen beim Einsatz eines Samba-Servers

Für ein zuverlässig funktionierendes Netz SOLLTEN auf den Windows-Clients nur wirklich benötigte Protokolle genutzt werden. Falls *Netware*-Systeme auf den *Samba*-Server zugreifen müssen, SOLLTE berücksichtigt werden, dass *Internetwork Packet Exchange* (IPX) benötigt wird. Sofern IPv6 eingesetzt wird, SOLLTEN erforderliche Besonderheiten berücksichtigt werden.

#### APP.3.4.A12 Schulung der Administratoren eines Samba-Servers

Administratoren SOLLTEN zu den genutzten spezifischen Bereichen von *Samba*, wie z. B. Benutzerauthentisierung, Windows- und Unix-Rechtemodelle, aber auch zu NTFS ACLs und NTFS ADS ausgebildet werden.

#### APP.3.4.A13 Regelmäßige Sicherung wichtiger Systemkomponenten eines Samba-Servers

Es SOLLTEN alle Systemkomponenten in das institutionsweite Datensicherungskonzept eingebunden werden, die erforderlich sind, um einen *Samba*-Server wiederherzustellen. Auch die Kontoinformationen aus allen eingesetzten Backends SOLLTEN berücksichtigt werden. Ebenso SOLLTEN alle TDB-Dateien gesichert werden. Des Weiteren SOLLTE die Registry mitgesichert werden, falls sie für Freigaben eingesetzt wurde. 

Die Konfigurationsdaten, Statusinformationen und Systemdateien SOLLTEN kompatibel zueinander sein.

#### APP.3.4.A14 Erstellen eines Notfallplans für den Ausfall von Samba-Servern

Um den *Samba*-Server im Notfall schnell neu installieren zu können, SOLLTEN die notwendigen Installationspakete und Informationen an einem festgelegten Ort hinterlegt werden. Es SOLLTE gewährleistet sein, dass sie jederzeit verfügbar sind. Die Dokumentation der *Samba*-Konfiguration SOLLTE dabei stets aktuell und nachvollziehbar sein.

Für den *Samba*-Server SOLLTE abhängig von der Serverrolle und den Verfügbarkeitsanforderungen getestet werden, ob er sich wiederherstellen lässt und wie lange das dauert. Anhand der Ergebnisse SOLLTE der Notfallplan verbessert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.4.A15 Verschlüsselung der Datenpakete unter Samba(CI)

Um die Integrität und Vertraulichkeit der Datenpakete auf dem Transportweg zu gewährleisten, SOLLTEN die Datenpakete mit den in SBM3 integrierten Verschlüsselungsverfahren verschlüsselt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Samba" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [SAMBA] Samba

  

 Opening Windows to a Wider World, SAMBA, (zuletzt abgerufen am 29.09.2017)  
 <https://www.samba.org/>

 
* #### [UBUNTU] ubuntuuser

  

 Wiki Samba, (zuletzt abgerufen am 29.09.2017)  
 <https://wiki.ubuntuusers.de/Samba>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Samba" von Bedeutung.

* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

