1 Beschreibung
--------------

### 1.1 Einleitung

Neben Windows werden auf immer mehr Client-Betriebssystemen Linux oder seltener Unix installiert. Beispiele für klassische Unix-Systeme sind die BSD-Reihe (FreeBSD, OpenBSD und NetBSD), Solaris und AIX. Linux hingegen ist kein klassisches Unix (der Kernel basiert nicht auf dem ursprünglichen Quelltext, aus dem sich die verschiedenen Unix-Derivate entwickelt haben), sondern ein funktionelles Unix-System. Da sich die Konfiguration und der Betrieb von Linux- und Unix-Client ähneln, werden in diesem Baustein alle Betriebssysteme der Unix-Familie betrachtet.

Linux ist freie Software und wird von der Open-Source-Gemeinschaft entwickelt. Daneben gibt es Anbieter, die den Linux-Kernel und die verschiedenen Software-Komponenten zu einer Distribution zusammenfassen und pflegen, sowie weitere Dienstleistungen anbieten. Häufig werden Derivate zu den Distributionen Ubuntu, Debian, Red Hat Enterprise Linux SUSE Linux Enterprise eingesetzt. Darüber hinaus gibt es für spezielle Einsatzzwecke und Geräte zugeschnittene Linux-Distributionen wie Qubes OS, das versucht, ein hohes Maß an Sicherheit durch Virtualisierung zu erreichen, IGEL Linux als Thin Client, LibreElec für den Einsatz eines Home Theater PCs (HTPC) oder Kali Linux, eine auf Sicherheit, Computerforensik und Penetrationstests spezialisierte Distribution. Außerdem können Clients auch Live-Distributionen starten, ohne dass das vorhandene Betriebssystem verändert wird.

Der Marktanteil des Betriebssystems Linux auf Clients hat in den letzten Jahren zugenommen, in speziellen Einsatzumgebungen werden weiterhin "klassische" Unix-Systeme in verschiedenen Derivaten eingesetzt. Durch die Menge der vorausgewählten Softwarepakete einer Standardinstallation der gängigen Linux-Distributionen, beziehungsweise der Unix-Derivate, erhöht sich die Angriffsfläche, gleichzeitig bieten unixähnliche Betriebssysteme aber auch umfangreiche Schutzmechanismen. Typischerweise ist ein solches IT-System vernetzt und wird als Client in einem Client-Server-Netz betrieben. Da Clients oftmals aus Sicherheitsgründen unter Unix oder Linux betrieben werden und wie bei allen Clients nicht auf korrektes Nutzerverhalten vertraut werden kann, kommt der Absicherung von unixähnlichen Clients eine besondere Bedeutung zu.

### 1.2 Zielsetzung

Zielsetzung dieses Bausteins ist der Schutz von Informationen, die auf Unix-Clients erstellt, bearbeitet, gespeichert oder versendet werden. Die Anforderungen des Bausteins adressieren vorrangig Linux-Clients, können aber generell für Unix-Clients adaptiert werden. Der vorliegende Baustein unterscheidet hier weitgehend nicht zwischen Unix- und Linux, unter dem Begriff "Unix" werden Unix- und Linux-Clients zusammengefasst.

### 1.3 Abgrenzung

Dieser Baustein enthält grundsätzliche Anforderungen zum Betrieb von unixähnlichen Clients auf handelsüblichen IT-Systemen. Er konkretisiert und ergänzt die Aspekte, die im Bausteinen SYS.2.1 Allgemeiner Client behandelt werden, um Spezifika von Unix-Systemen. Auch wenn es sich bei OS X von Apple um ein unixartiges Betriebssystem handelt, wird dieses Betriebssystem nicht in diesem Baustein behandelt, Empfehlungen hierzu sind im Baustein SYS.2.4 Client unter Apple OS X zu finden.

Soll der Client nicht selber verwaltet werden, sondern wird dieser durch Dritte verwaltet, sind zusätzlich die Anforderungen des Bausteins OPS.3.1 Outsourcing-Nutzung zu berücksichtigen.

Der Baustein umfasst nur das unixartige Betriebssystem, dass in der Regel bei einer Basisinstallation einer Linux-Desktop-Distribution installiert wird. Der Baustein umfasst insbesondere nicht darauf aufbauende Software wie E-Mail-Clients oder Office-Software, Anforderungen hierzu sind in der Schicht APP.1 Client-Anwendungen des IT-Grundschutz-Kompendiums zu finden. Falls der Client Schnittstellen zum Datenaustausch hat, wie z. B. CD/DVD, USB, Bluetooth oder WLAN, müssen die Sicherheitsvorgaben des Bausteins SYS.3.4 Mobile Datenträger erfüllt werden 

Es wird bei diesem Client-Baustein davon ausgegangen, dass neben dem Administrator dauerhaft nur eine unveränderte Person mit einem interaktiven Benutzerkonto aktiv ist. Clients, die von mehreren Personen nacheinander oder gleichzeitig genutzt werden, erfordern zusätzliche Maßnahmen, die im Rahmen dieses Bausteins nicht behandelt werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für Clients unter Unix von besonderer Bedeutung:

### 2 1 Schadprogramme

Schadprogramme werden mit dem Ziel entwickelt, unerwünschte und meistens schädliche Funktionen auszuführen. Schadprogramme werden meist heimlich, ohne Wissen und Einwilligung des Benutzers aktiv. Schadprogramme bieten heutzutage einem Angreifer umfangreiche Kommunikations- und Steuerungsmöglichkeiten und besitzen eine Vielzahl von Funktionen. Unter anderem können die Programme gezielt Passwörter ausforschen, Systeme fernsteuern, Schutzfunktionen deaktivieren und Daten ausspionieren. Insbesondere sind Anwender, die auf die von vornherein höhere Sicherheit von unixähnlichen Systemen vertrauen, oftmals sorgloser im Umgang mit unbekannten Dateien.

### 2 2 Software aus Drittquellen

Bei unixähnlichen IT-Systemen ist es nicht ungewöhnlich, Software selbst herunterzuladen und zu kompilieren, statt fertige Softwarepakete zu installieren. Wenn fertige Softwarepakete genutzt werden, werden diese oft nicht nur aus den vorhanden Paketquellen des Unix-Derivates installiert, sondern werden aus Drittquellen ohne weitere Prüfung bezogen. Jeder dieser alternativen Wege der Softwareinstallation birgt zusätzliche Risiken, indem so fehlerhafte oder inkompatible Software sowie Schadsoftware installiert werden kann.

### 2 3 Software-Schwachstellen oder -Fehler

Auf unixähnlichen IT-Systemen werden in der Regel eine Vielzahl von Anwendungen zur Installation angeboten. Da jede der installierbaren Anwendungen Software-Schwachstellen und -Fehler haben können, wird die potentielle Angriffsfläche erhöht, wenn bei der Installation nicht darauf geachtet, dass nur die benötigte Software installiert wird.

### 2 4 Ausnutzbarkeit der Skriptumgebung

Oft werden in unixähnlichen Betriebssystemen Skriptsprachen genutzt. Skripte sind eine Auflistung von einzelnen Kommandos, die in einer Textdatei gespeichert und beispielsweise in der Kommandozeile aufgerufen werden. Durch den großen Funktionsumfang der Skriptumgebungen können Angreifer Skripte umfangreich für ihre Zwecke nutzen. Darüber hinaus können aktivierte Skriptsprachen nur sehr schwer eingedämmt werden. 

### 2 5 Dynamisches Laden von gemeinsam genutzten Bibliotheken

Mit der Kommandozeilenoption LD\_PRELOAD wird die angegebene Bibliothek vor allen anderen in einer Anwendung benötigten Bibliotheken geladen und deren Funktionen werden von der Anwendung genutzt. Ein Angreifer könnte das Betriebssystem so manipulieren, dass Schadfunktionen bei der Nutzung von bestimmten Anwendungen mit ausgeführt werden.

### 2 6 Fehlerhafte Konfiguration

Schon in einer Standardinstallation werden bei unixähnlichen Betriebssystemen zahlreiche Anwendungen installiert, die separat konfiguriert werden müssen. Auch nachinstallierte Anwendungen müssen separat konfiguriert werden, so dass auf unixähnlichen Betriebssystemen unzählige Konfigurationsdateien vorzufinden sind.

Da diese Anwendungen unabhängig voneinander konfiguriert werden, können die Konfigurationsoptionen im Widerspruch zueinander stehen, ohne dass dies aus den einzelnen Einstellungen ersichtlich ist. Beispielsweise kann ein Dienst für eine Fernadministration auf einem Port lauschen, der von Paketfilterregeln blockiert wird oder Samba gibt das eigene Home-Verzeichnis unbeabsichtigt im Netz frei. Auf diese Weise können die Anwendungen ungewollt zusätzliche Funktionen bereitstellen oder wichtige Funktionen nicht anbieten und so die Aufgabenerfüllung am Client erschweren.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Client unter Unix aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.2.3.A1 Authentisierung von Administratoren und Benutzer [Benutzer]

Um den Client zu nutzen, MÜSSEN sich die Benutzer gegenüber dem IT-System authentisieren. Administratoren DÜRFEN sich nicht im Normalbetrieb als root anmelden. Für die Systemadministrationsaufgaben SOLLTE "sudo" oder eine geeignete Alternative mit einer geeigneten Protokollierung genutzt werden. Es SOLLTE verhindert werden, dass sich mehrere Benutzer auf einem Gerät gleichzeitig einloggen können.

#### SYS.2.3.A2 Auswahl einer geeigneten Distribution

Es MUSS auf Grundlage der Sicherheitsanforderungen und des Einsatzzwecks ein geeignetes Unix-Derivat bzw. Linux-Distribution ausgewählt werden. Alle vorinstallierten Anwendungsprogramme, die nicht benötigt werden, MÜSSEN deinstalliert werden können. Es MUSS für die geplante Einsatzzeit des Betriebssystems Support angeboten werden. Alle benötigten Anwendungsprogramme SOLLTEN direkt verfügbar sein, ohne dass diese aus Drittquellen bezogen werden müssen. 

Es SOLLTEN nur Anwendungsprogramme ausgewählt und installiert werden, für die Support angeboten wird. Betriebssystem und Anwendungsprogramme ohne regelmäßige Sicherheitsupdates SOLLTEN nicht eingesetzt werden. Es SOLLTE auf Distributionen mit einem Rolling-Release-Modell verzichtet werden. Distributionen, bei denen das Betriebssystem selber kompiliert wird, SOLLTEN nicht in Produktivumgebungen eingesetzt werden.

#### SYS.2.3.A3 Cloud- und Online-Inhalte [Benutzer]

Nur zwingend notwendige Cloud- und Online-Dienste des Betriebssystems DÜRFEN genutzt werden. Die notwendigen Cloud- und Online-Dienste SOLLTEN dokumentiert werden. Die Einstellungen des Betriebssystems MÜSSEN auf Konformität mit den organisatorischen Datenschutz- und Sicherheitsvorgaben überprüft und restriktiv konfiguriert bzw. deaktiviert werden.

#### SYS.2.3.A4 Einspielen von Updates und Patches

Die Verantwortlichen MÜSSEN sich über bekannt gewordene Schwachstellen informieren. Updates und Patches MÜSSEN so schnell wie möglich eingespielt werden. Vorab SOLLTE auf einem Testsystem überprüft werden, ob die Sicherheitsupdates kompatibel sind und keine Fehler verursachen. Solange keine Patches für bekannte Schwachstellen verfügbar sind, MÜSSEN andere geeignete Maßnahmen getroffen werden, um den Client zu schützen. Der Client SOLLTE zeitnah rebootet werden, nachdem der Kernel aktualisiert wurde. Alternativ MUSS Live-Patching des Kernels aktiviert werden.

#### SYS.2.3.A5 Sichere Installation von Software-Paketen

Es DÜRFEN nur benötigte Anwendungen installiert werden. Nicht mehr benötigte Anwendungen MÜSSEN deinstalliert werden.

Die Integrität und Authentizität der zu installierenden Softwarepakete MUSS immer geprüft werden. Die Software-Pakete MÜSSEN unter einem unprivilegierten Benutzeraccount entpackt, konfiguriert und übersetzt werden. Erst der letzte Schritt, die eigentliche Installation des übersetzten Programms, DARF mit höheren Privilegien erfolgen. Dabei DARF die zu installierende Software NICHT unkontrolliert in das Wurzeldateisystem des Servers installiert werden.

Wird die Software aus dem Quelltext übersetzt, dann SOLLTEN die gewählten Parameter geeignet dokumentiert werden. Anhand dieser Dokumentation SOLLTE der Quelltext jederzeit nachvollziehbar und reproduzierbar kompiliert werden können. Alle weiteren Installationsschritte SOLLTEN dabei ebenfalls dokumentiert werden, damit sich die Konfiguration im Notfall schnell reproduzieren lässt.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Clients unter Unix. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.2.3.A6 Automatisches Einbinden von Wechsellaufwerken [Benutzer]

Wechsellaufwerke SOLLTEN nicht automatisch eingebunden werden. Die Einbindung von Wechsellaufwerken SOLLTE so konfiguriert sein, dass alle Dateien als nicht ausführbar markiert sind (Mountoption "noexec").

#### SYS.2.3.A7 Restriktive Rechtevergabe auf Dateien und Verzeichnisse

Der Zugriff von Benutzern auf Dateien und Verzeichnisse SOLLTE immer auf das erforderliche Minimum beschränkt werden. Dabei SOLLTE in jedem Fall sichergestellt werden, dass Dienste und Anwendungen nur ihre zugeordneten Dateien erstellen, verändern oder löschen dürfen. Auf Verzeichnissen, in denen alle Benutzer Schreibrechte haben (z. B. /tmp) SOLLTE das Sticky-Bit gesetzt werden. 

#### SYS.2.3.A8 Einsatz von Techniken zur Rechtebeschränkung von Anwendungen

Zur Beschränkung der Zugriffsrechte von Anwendungen auf Dateien, Geräte und Netze SOLLTE App-Armor oder SELinux eingesetzt werden. Es SOLLTEN die von der jeweiligen Unix-Derivat bzw. Linux-Distribution am besten unterstützte Lösung eingesetzt werden. Statt Blacklisting SOLLTEN die notwendigen Anwendungen durch Whitelisting reglementiert werden. Erweiterungen zur Rechtebeschränkung SOLLTEN im Enforcement Mode oder mit geeigneten Alternativen verwendet werden.

#### SYS.2.3.A9 Passwörter auf der Kommandozeile [Benutzer]

Passwörter SOLLTEN NICHT als Parameter an Programme übergeben werden.

#### SYS.2.3.A10 Absicherung des Bootvorgangs

Der Client SOLLTE durch Vergabe eines Boot-Passworts in der Firmware abgesichert werden. Zusätzlich SOLLTE eine Bootreihenfolge festgelegt werden, bei der von der eingebauten Boot-Festplatte zuerst gebootet wird. Der Bootloader SOLLTE mit einem Passwort so abgesichert werden, dass nur der unveränderte Standardeintrag ohne Passwort genutzt werden kann.

Beim Booten SOLLTE die Integrität vom (Pre-)Bootloader bis zum Kernel geprüft werden. Die hierfür genutzten Schlüssel SOLLTEN bei der Ersteinrichtung überprüft werden. Es SOLLTE geprüft werden, ob hierfür Secure Boot als der Teil der UEFI-Spezifikation oder äquivalente Lösungen genutzt werden können.

#### SYS.2.3.A11 Verhinderung der Überlastung der Festplatte

Es SOLLTEN Quotas für Benutzer bzw. Dienste eingerichtet werden, die ausreichend Freiraum für das Betriebssystem lassen. Generell SOLLTEN unterschiedliche Partitionen für Betriebssystem und Daten genutzt werden. Alternativ SOLLTEN auch Mechanismen des verwendeten Dateisystems genutzt werden, die ab einem geeigneten Füllstand nur noch dem Benutzer root Schreibrechte einräumen.

#### SYS.2.3.A12 Einsatz von Appliances als Clients

Es SOLLTE sichergestellt werden, dass Appliances ein ähnliches Sicherheitsniveau wie Clients auf Standard-IT-Systemen erfüllen. Es SOLLTE dokumentiert werden, wie entsprechende Sicherheitsanforderungen mit einer eingesetzten Appliance erfüllt werden. Wenn die Anforderungen nicht zweifelsfrei erfüllt werden können, SOLLTE eine Konformitätserklärung vom Hersteller angefordert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.2.3.A13 Schutz vor unbefugten Anmeldungen(CIA)

Es SOLLTE eine Zwei-Faktor-Authentisierung verwendet werden.

#### SYS.2.3.A14 Absicherung gegen Nutzung unbefugter Peripheriegeräte(CIA)

Peripheriegeräte SOLLTEN nur nutzbar sein, wenn sie auf einer zentral verwalteten Whitelist geführt sind. Kernelmodule für Peripheriegeräte SOLLTEN nur geladen und aktiviert werden, wenn das Gerät auf der Whitelist steht.

#### SYS.2.3.A15 Zusätzlicher Schutz vor der Ausführung unerwünschter Dateien(CI)

Partitionen und Verzeichnisse, in denen Benutzer Schreibrechte haben, SOLLTEN so gemountet werden, dass keine Dateien ausgeführt werden können (/noexec).

#### SYS.2.3.A16 Zusätzliche Absicherung des Bootvorgangs(CIA)

Bootloader und Kernel SOLLTEN durch selbstkontrolliertes Schlüsselmaterial signiert und nicht benötigtes Schlüsselmaterial entfernt werden.

#### SYS.2.3.A17 Zusätzliche Verhinderung der Ausbreitung bei der Ausnutzung von Schwachstellen(CI)

Die Nutzung von Systemaufrufen SOLLTE insbesondere für exponierte Dienste und Anwendungen auf die unbedingt notwendigen Systemaufrufe beschränkt werden (z B. durch "seccomp"). Die vorhandenen Standardprofile bzw. -Regeln von "SELinux", "AppArmor" sowie alternativen Erweiterungen SOLLTEN manuell überprüft und gegebenenfalls an die eigene Sicherheitsrichtlinie angepasst werden. Falls erforderlich, SOLLTEN neue Regeln bzw. Profile erstellt werden.

#### SYS.2.3.A18 Zusätzlicher Schutz des Kernels(CI)

Es SOLLTEN mit speziell gehärteten Kernels geeignete Schutzmechanismen wie Speicherschutz, Dateisystemabsicherung und rollenbasierte Zugriffskontrolle, die die Ausnutzung von Schwachstellen und Ausbreitung im Betriebssystem verhindern sollen, genutzt werden (z. B. "grsecurtiy", "PaX").

#### SYS.2.3.A19 Festplatten- oder Dateiverschlüsselung(CI)

Festplatten oder die hierauf abgespeicherten Dateien SOLLTEN verschlüsselt werden. Die dazugehörigen Schlüssel SOLLTEN NICHT auf dem IT-System gespeichert sein. Es SOLLTE "AEAD" bei der Festplatten- und Dateiverschlüsselung eingesetzt werden. Alternativ SOLLTE "dm-crypt" in Kombination mit "dm-verity" genutzt werden.

#### SYS.2.3.A20 Abschaltung kritischer SysRq-Funktionen(CIA)

Es SOLLTEN kritische SysRq-Funktionen deaktiviert werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Clients unter Unix" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISiClient] Absicherung eines PC-Clients (ISi-Client),

  

 (zuletzt abgerufen am 27.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client_node.html)

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Clients unter Unix" von Bedeutung.

* G 0.19 Offenlegung schützenswerter Informationen
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
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

