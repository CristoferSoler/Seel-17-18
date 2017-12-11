1 Beschreibung
--------------

### 1.1 Einleitung

Auf Server-Systemen werden häufig die Betriebssysteme Linux oder Unix eingesetzt. Beispiele für klassische Unix-Systeme sind die BSD-Reihe (FreeBSD, OpenBSD und NetBSD), Solaris und AIX. Linux ist kein klassisches Unix (der Kernel basiert nicht auf dem ursprünglichen Quelltext, aus dem sich die verschiedenen Unix-Derivate entwickelt haben), sondern ein funktionelles Unix-System. In diesem Baustein werden alle Betriebssysteme der Unix-Familie betrachtet, also auch Linux als funktionelles Unix-System.

Linux ist freie Software und wird von der Open-Source-Gemeinschaft entwickelt. Daneben gibt es Anbieter, die die verschiedenen Software-Komponenten zu einer Distribution zusammenfassen und pflegen, sowie weitere Dienstleistungen anbieten. Für Linux-Server werden häufig die Distributionen

* Debian
* Red Hat Enterprise Linux
* SUSE Linux Enterprise Server
* Ubuntu Server
eingesetzt. Darüber hinaus gibt es für spezielle Einsatzzwecke und Geräte zugeschnittene Linux-Distributionen wie Endian für Firewall-Systeme, OpenMediaVault für NAS-Systeme oder OpenWRT für Router.

Die auf einem Server angebotenen Dienste sind oft zentral und daher in besonderem Maße exponiert. Hierdurch sind Unix-Server nicht nur für Geschäftsprozesse kritisch, sondern geraten deswegen nicht selten in den Fokus von Angreifern. Deswegen kommt der Verfügbarkeit und Absicherung von Unix-Servern eine besondere Bedeutung zu.

### 1.2 Zielsetzung

Zielsetzung des Bausteins ist der Schutz von Informationen, die von Unix-Servern verarbeitet werden. Die Anforderungen des Bausteins adressieren vorrangig Linux-Server, können aber generell für Unix-Server adaptiert werden. Es werden Anforderungen formuliert, wie das Betriebssystem konfiguriert und betrieben werden soll.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen zur Einrichtung und zum Betrieb von Unix-Servern. Er konkretisiert und ergänzt die Aspekte, die im Bausteinen SYS.1.1 Allgemeiner Server behandelt werden, um Spezifika von Unix-Systemen. 

Soll der Server nicht selber verwaltet werden, sondern wird dieser durch Dritte gehostet, sind zusätzlich die Anforderungen des Bausteins OPS.3.1 Outsourcing-Nutzung zu berücksichtigen. Sicherheitsanforderungen möglicher Server-Funktionen wie Webserver (APP.3.2 Webserver) oder Server für Groupware (siehe APP.5.1 Groupware) sind Gegenstand eigener Bausteine, eine Ausnahme sind die Unix-spezifischen Server-Dienste NIS, NFS und SSH, die ebenfalls in diesem Baustein behandelt werden. Das Thema Virtualisierung wird im Baustein SYS.1.5 Server-Virtualisierung beleuchtet. In diesem Baustein geht es um die grundlegende Absicherung auf Betriebssystemebene mit bordeigenen Mitteln unabhängig vom Einsatzzweck des Servers.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich* *Server unter Unix von besonderer Bedeutung:

### 2 1 Ausspähen von System- und Benutzerinformationen

Durch verschiedene Unix-Programme ist es möglich, Daten abzufragen, die das IT -System über die Benutzer speichert. Hiervon sind auch solche Daten betroffen, die Auskunft über das Leistungsprofil eines Benutzers geben können. Zu diesen Informationen zählen sowohl Informationen über weitere angemeldete Benutzer wie auch technische Informationen zur Betriebssysteminstallation und -konfiguration. 

Beispielsweise kann mit einem einfachen Programm, das in einem bestimmten Zeitintervall die Informationen auswertet, die der Befehl "who" liefert, jeder Benutzer ein genaues Nutzungsprofil für einen Account erstellen. Zum Beispiel lassen sich auf diese Weise die Abwesenheitszeiten des oder der Systemadministratoren feststellen, um diese Zeiten für unberechtigte Handlungen zu nutzen. Des Weiteren lässt sich feststellen, welche Terminals für einen privilegierten Zugang zugelassen sind. Weitere Programme mit ähnlichen Missbrauchsmöglichkeiten sind "finger" oder "ruser".

### 2 2 Ausnutzbarkeit der Skriptumgebung

In Unix-Betriebssystemen ist die Nutzung von Skriptsprachen weit verbreitet. Skripte sind eine Auflistung von einzelnen Kommandos, die in einer Textdatei gespeichert und aufgerufen werden. Durch den großen Funktionsumfang der Skriptumgebung können Angreifer Skripte umfangreich für ihre Zwecke nutzen. Darüber hinaus ist die Eindämmung von aktivierten Skriptsprachen sehr schwierig.

### 2 3 Dynamisches Laden von gemeinsam genutzten Bibliotheken

Mit der Kommandozeilenoption "LD\_PRELOAD" wird die angegebene Bibliothek vor allen anderen in einer Anwendung benötigten Bibliotheken geladen und deren Funktionen werden von der Anwendung genutzt. Ein Angreifer könnte das Betriebssystem so manipulieren, dass Schadfunktionen bei der Nutzung von bestimmten Anwendungen mit ausgeführt werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Server unter Unix aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.1.3.A1 Benutzerauthentisierung unter Unix

Um den Unix-Server zu nutzen, MÜSSEN sich die Benutzer gegenüber dem IT-System authentisieren. Die Authentisierung über ein Netz MUSS verschlüsselt werden. Wenn mit einem Benutzerkonto nur bestimmte Dienste genutzt werden dürfen, DARF das Benutzerkonto nicht für andere Dienste genutzt werden können. 

#### SYS.1.3.A2 Sorgfältige Vergabe von IDs

Jeder Login-Name, jede Benutzer-ID (UID) und jede Gruppen-ID (GID) DARF nur einmal vorkommen. Jeder Benutzer MUSS Mitglied mindestens einer Gruppe sein. Jede in der Datei "/etc/passwd" vorkommende GID MUSS in der Datei "/etc/group" definiert sein. Jede Gruppe SOLLTE nur die Benutzer enthalten, die unbedingt notwendig sind. Bei vernetzten Systemen MUSS außerdem darauf geachtet werden, dass die Vergabe von Benutzer- und Gruppennamen, UID und GID im System­verbund konsistent erfolgt. 

#### SYS.1.3.A3 Automatisches Einbinden von Wechsellaufwerken

Wechsellaufwerke wie z. B. USB-Sticks oder CDs/DVDs DÜRFEN nicht automatisch eingebunden werden.

#### SYS.1.3.A4 Schutz von Anwendungen

Um die Ausnutzung von Schwachstellen in Anwendungen zu erschweren, MUSS "ASLR" und "DEP/NX" im Kernel aktiviert und von den Anwendungen genutzt werden. Sicherheitsfunktionen des Kernels und der Standardbibliotheken, wie z. B. Heap- und Stackschutz, DÜRFEN NICHT deaktiviert werden.

#### SYS.1.3.A5 Sichere Installation von Software-Paketen

Die Integrität und Authentizität der zu installierenden Softwarepakete MUSS immer geprüft werden. Die Software-Pakete MÜSSEN unter einem unprivilegierten Benutzeraccount entpackt, konfiguriert und übersetzt werden. Erst der letzte Schritt, die eigentliche Installation des übersetzten Programms, DARF mit höheren Privilegien erfolgen. Dabei DARF die zu installierende Software NICHT unkontrolliert in das Wurzeldateisystem des Servers installiert werden.

Wird die Software aus dem Quelltext übersetzt, dann SOLLTEN die gewählten Parameter geeignet dokumentiert werden. Anhand dieser Dokumentation SOLLTE der Quelltext jederzeit nachvollziehbar und reproduzierbar kompiliert werden können. Alle weiteren Installationsschritte SOLLTEN dabei ebenfalls dokumentiert werden, damit sich die Konfiguration im Notfall schnell reproduzieren lässt.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Server unter Unix. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.1.3.A6 Verwaltung von Benutzern und Gruppen

Zur Verwaltung von Benutzern und Gruppen SOLLTEN die entsprechenden Verwaltungswerkzeuge genutzt werden. Von einer direkten Bearbeitung der Konfigurationsdateien "/etc/passwd" und "/etc/group" und "/etc/sudoers" SOLLTE abgesehen werden. 

#### SYS.1.3.A7 Zusätzliche Absicherung des Zugangs zum Single-User- und Wiederher­stellungs­modus

Der Unix-Server SOLLTE durch Vergabe eines Boot-Passworts in der Firmware des Servers abgesichert werden. Alternativ SOLLTE eine festgelegte Bootreihenfolge mit eingebauter Boot-Festplatte zuerst festlegt und der Bootloader abgesichert werden.

#### SYS.1.3.A8 Verschlüsselter Zugriff über Secure Shell

Um eine verschlüsselte und authentisierte interaktive Verbindung zwischen zwei IT-Systemen aufzubauen, SOLLTE ausschließlich SSH verwendet werden. Alle anderen Protokolle, deren Funktionalität durch Secure Shell abgedeckt wird, SOLLTEN vollständig abgeschaltet werden. 

#### SYS.1.3.A9 Absicherung des Bootvorgangs

Beim Booten SOLLTE die Integrität vom (Pre-)Bootloader bis zum Kernel überprüft werden. Die hierfür genutzten Schlüssel SOLLTEN bei der Ersteinrichtung überprüft werden. Es SOLLTE geprüft werden, ob hierfür Secure Boot als Teil der UEFI-Spezifikation genutzt werden kann. 

#### SYS.1.3.A10 Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen

Dienste und Anwendungen SOLLTEN mit individuellen Sicherheitsrichtlinien abgesichert werden (z. B. mit AppArmor oder SELinux). Auch chroot-Umgebungen sowie LXC- oder Docker-Container SOLLTEN dabei berücksichtigt werden. Es SOLLTE sichergestellt sein, dass mitgelieferte Standardprofile bzw. -Regeln aktiviert sind.

#### SYS.1.3.A11 Einsatz der Sicherheitsmechanismen von NFS

Nur hierfür vorgesehene Server SOLLTEN Verzeichnisse für andere Clients freigeben (siehe auch APP.3.3 Fileserver). Es SOLLTEN über NFS (Network File System) nur Verzeichnisse exportiert werden, die unbedingt notwendig sind. In den Dateien "/etc/exports" beziehungsweise "/etc/dfs/fstab" SOLLTEN die mountbaren Verzeichnisse auf das notwendige Maß reduziert werden. Die mountbaren Verzeichnisse SOLLTEN nur für bestimmte IT -Systeme sowie Benutzer unter Berücksichtigung der festgelegten Berechtigungsstruktur freigegeben werden.

#### SYS.1.3.A12 Einsatz der Sicherheitsmechanismen von NIS

NIS (Network Information Service) SOLLTE nur in einer sicheren Umgebung eingesetzt werden. In /etc/passwd, /etc/group sowie allen anderen sicherheitsrelevanten Dateien SOLLTE der Eintrag "+::0:0:::" nicht enthalten sein. Der Server-Prozess "ypserv" SOLLTE nur Anfragen von vorher festgelegten Rechnern beantworten.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.1.3.A13 Zusätzlicher Schutz der priviligierten Anmeldeinformationen(CI)

Die Passwörter der administrativen Konten SOLLTEN in mehrere Teile geteilt und durch Anwendung des Vier-Augen-Prinzips zusätzlich geschützt werden. Alternativ SOLLTE die Authentisierung mit Smartcards erfolgen.

Auch administrative Konten SOLLTEN so eingerichtet werden, dass diese nach einer vorher festgelegten Anzahl fehlerhafter Anmeldeversuche gesperrt werden.

#### SYS.1.3.A14 Verhinderung des Ausspähens von System- und Benutzerinformationen(C)

Die Ausgabe von Informationen über das Betriebssystem und der Zugriff auf Protokoll- und Konfigurationsdateien SOLLTE für Benutzer auf das notwendige Maß beschränkt werden. Außerdem SOLLTEN bei Befehlsaufrufen keine sensitiven Informationen als Parameter übergeben werden.

#### SYS.1.3.A15 Zusätzliche Absicherung des Bootvorgangs(CIA)

Bootloader und Kernel SOLLTEN durch selbstkontrolliertes Schlüsselmaterial signiert und nicht benötigtes Schlüsselmaterial entfernt werden.

#### SYS.1.3.A16 Zusätzliche Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen(CI)

Die Nutzung von Systemaufrufen SOLLTE insbesondere für exponierte Dienste und Anwendungen auf die unbedingt notwendigen Systemaufrufe beschränkt werden. Die Standardprofile bzw. -Regeln von z.B. SELinux, AppArmor SOLLTEN manuell überprüft und ggf. an die eigenen Sicherheitsrichtlinien angepasst werden. Falls erforderlich, SOLLTEN neue Regeln bzw. Profile erstellt werden.

#### SYS.1.3.A17 Zusätzlicher Schutz des Kernels(CI)

Es SOLLTEN mit speziell gehärteten Kernels geeignete Schutzmechanismen wie Speicherschutz, Dateisystemabsicherung und rollenbasierte Zugriffskontrolle, die die Ausnutzung von Schwachstellen und die Ausbreitung im Betriebssystem verhindern sollen, genutzt werden. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Server unter Unix" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISi-Server] Absicherung eines Servers (ISi-Server), BSI, 09.2013

  

 Bundesamt für Sicherheit in der Informatiostechnik, 02.2017  
 <https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Server unter Unix" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.39 Schadprogramme
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

