1 Beschreibung
--------------

### 1.1 Einleitung

Mit Windows Server 2012 hat Microsoft im September 2012 ein Serverbetriebssystem auf den Markt gebracht, das in Bezug auf die Sicherheit diverse Verbesserungen gegenüber bisherigen Windows-Versionen (insbesondere auch Windows Server 2008 R2) mitbringt. Technisch wird dabei nicht auf dem Vorgänger aufgebaut, sondern auf der Codebasis des Client-Betriebssystems Windows 8. Mit dem Release Windows Server 2012 R2 von Oktober 2013 wurde das Betriebssystem weiter verbessert und erweitert, um Windows 2012 R2 zum Server-Pendant zu Windows 8.1 auf der Clientseite machen. 

Dieser Baustein beschäftigt sich mit der Absicherung von Windows Server 2012 und Windows Server 2012 R2 gleichermaßen, auf relevante Unterschiede und Besonderheiten wird jeweils geeignet hingewiesen. Dabei wird die Schreibweise "Windows Server 2012 (R2)" verwendet, wenn beide Versionen gemeint sind. Das Ablaufdatum für den Mainstream Support bzw. den Extended Support ("End-of-Life", EOL) ist in beiden Fällen der 09.01.2018 bzw. der 10.01.2023.

### 1.2 Zielsetzung

Zielsetzung dieses Bausteins ist der Schutz von Informationen und Prozessen, die durch Serversysteme auf Basis von Windows Server 2012 (R2) im Regelbetrieb verarbeitet bzw. gesteuert werden.

### 1.3 Abgrenzung

Der Baustein Windows Server 2012 (R2) ist auf alle Zielobjekte anzuwenden, die unter dem Betriebssystem Microsoft Windows Server 2012 (R2) betrieben werden. Er konkretisiert und ergänzt die Aspekte, die im Bausteinen SYS.1.1 Allgemeiner Server behandelt werden, um Spezifika von Windows Server 2012 (R2), ohne dabei die Anforderungen des Bausteins APP.2.2 Active Directory zu wiederholen. 

Im Rahmen dieses Bausteins wird von einer Standardeinbindung in eine Active Directory-Domäne ausgegangen, wie sie in Unternehmen und Behörden üblich ist. Besonderheiten von Stand-alone-Systemen werden nur punktuell erwähnt, wo die Unterschiede besonders relevant erschienen.

Sicherheitsanforderungen möglicher Serverrollen und -Funktionen wie Fileserver (APP.3.3 Fileserver), Webserver (APP.3.2 Webserver) oder Exchange (APP.5.2 Exchange/Outlook) sind Gegenstand eigener Bausteine, genauso wie das Thema Virtualisierung (SYS.1.5 Server-Virtualisierung). In diesem Baustein geht es um die grundlegende Absicherung auf Betriebssystemebene mit bordeigenen Mitteln unabhängig vom Einsatzzweck des Servers.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Windows Server 2012 (R2) von besonderer Bedeutung:

### 2 1 Unzureichende Planung von Windows Server 2012 (R2)

Windows Server 2012 (R2) ist ein komplexes modernes Betriebssystem, das über eine große Zahl von Funktionen und Konfigurationsoptionen verfügt. Ein Beispiel sind die verschiedenen mächtigen installierbaren Serverrollen. Mit jeder weiteren Funktion vergrößert sich die Angriffsfläche, zudem steigt die Wahrscheinlichkeit von Schwachstellen und Fehlkonfigurationen. Bei der Einbindung in die Domäne und der Vernetzung mit anderen Systemen und Diensten gibt es ebenfalls sehr viele Freiheitsgrade. Auch wenn moderne Windows-Versionen in vielen Bereichen gute Standardeinstellungen mitbringen, ist die Grundkonfiguration immer noch nicht in jedem Fall die sicherste. Dies kann bei unzureichender Planung zu einer Vielzahl von Angriffsvektoren führen, die Angreifer leicht ausnutzen können. Werden außerdem nicht schon vor der Installation zentrale Entscheidungen getroffen, wird mit einem unsicheren und undefinierten Zustand begonnen, der sich kaum beheben lässt.

### 2 2 Unbedachte Cloud-Nutzung

Windows Server 2012 (R2) bietet an verschiedenen Stellen die Möglichkeit, Cloud-Dienste zu nutzen, ohne dass Drittsoftware installiert werden muss. Hierzu gehören beispielsweise Microsoft Azure Online Backup oder die Online-Speicherung von BitLocker-Wiederherstellungsschlüsseln. Während Cloud-Dienste grundsätzlich Vorteile insbesondere auf die Verfügbarkeit bieten können, bestehen bei unbedachtem Einsatz Risiken für die Vertraulichkeit sowie eine Abhängigkeit von Dienstleistern. So können Daten über Cloud-Dienste in die Hände unberechtigter Dritter gelangen, seien es Angreifer oder aber auch staatliche Akteure. Wird ein Cloud-Dienst durch den Anbieter eingestellt, kann dies erhebliche Auswirkungen auf die eigenen Geschäftsprozesse haben.

### 2 3 Fehlerhafte Administration von Windows-Servern

Windows Server 2012 und Windows Server 2012 R2 haben im Vergleich zu den Vorgängerversionen viele neue sicherheitsrelevante Funktionen hinzubekommen. Bei anderen Features haben sich Teilfunktionen, Parameter oder Standardkonfigurationen verändert. Sind die Administratoren nicht ausreichend in den Besonderheiten der Systeme geschult, so drohen Konfigurationsfehler und Fehlhandlungen, die neben der Funktionalität auch die Sicherheit beeinträchtigen können.

Eine besondere Gefahr stellen uneinheitliche Windows-Server-Sicherheitseinstellungen dar (z. B. bei (SMB, RPC oder LDAP). Wenn die Konfiguration nicht systematisch und zentral geplant, dokumentiert, überprüft und nachgehalten wird, droht ein sogenannter Konfigurationsdrift: Je mehr sich die konkreten Konfigurationen funktional ähnlicher Systeme unbegründet und undokumentiert auseinander bewegen, desto schwieriger wird es, einen Überblick über den Status Quo zu behalten und die Sicherheit ganzheitlich und konsequent aufrechtzuerhalten.

### 2 4 Unsachgemäßer Einsatz von Gruppenrichtlinien (GPOs)

Gruppenrichtlinien (GPOs) sind eine nützliche und mächtige Art, viele (Sicherheits-)Aspekte von Windows Server 2012 (R2) zu konfigurieren, insbesondere in einer Domäne. Bei der großen Zahl möglicher Einstellungen ist es leicht möglich, versehentlich widersprüchliche oder inkompatible Einstellungen zu setzen oder Themenbereiche zu vergessen. Dies führt bei unsystematischer Vorgehensweise mindestens zu Betriebsstörungen, die teilweise schwer zu beheben sind, wenn nicht gar zu schwerwiegenden Schwachstellen auf dem Server oder auf verbundenen Clientsystemen. Insbesondere falsch verstandene Vererbungsregeln und Filter können dazu führen, dass GPOs gar nicht auf ein System angewendet werden.

### 2 5 Verlust verschlüsselter Daten

Wenn Daten verschlüsselt sind, wie etwa beim Einsatz von BitLocker oder der Geräteverschlüsselung auf Windows Server 2012 (R2), kann es zum kompletten Datenverlust kommen, wenn der Schlüssel verloren geht und es keinen Wiederherstellungsschlüssel gibt. Auch ein Backup verschlüsselter Daten hilft hier nicht weiter.

### 2 6 Integritätsverlust schützenswerter Informationen oder Prozesse

Windows Server 2012 (R2) verfügt über eine Vielzahl von Funktionen, um die Integrität von durch das Betriebssystem verarbeiteten Informationen zu schützen. Jede einzelne davon kann mit Schwachstellen behaftet sein. Zudem mangelt es häufig an einer konsequenten Konfiguration, nicht zuletzt aus Gründen der vermuteten Benutzerfreundlichkeit oder Bequemlichkeit. Informationen und Prozesse können so durch unbefugte Mitarbeiter oder externe Angreifer verfälscht und oftmals sogar die Spuren verwischt werden. Häufig werden auch Schadprogramme eingesetzt, um Informationen aus der Ferne zu manipulieren.

### 2 7 Software-Schwachstellen oder -Fehler

Jede Software enthält Schwachstellen, umso mehr gilt dies für komplexe Systeme wie Windows Server 2012 (R2). Sicherheitslücken in Komponenten können es einem Angreifer ermöglichen, Schadprogramme einzuschleusen, auszuführen oder Funktionen des Systems zu missbrauchen bzw. Sicherheitsmechanismen zu umgehen. Das kann z. B. dazu führen, dass Informationen manipuliert werden oder in falsche Hände geraten. Jede weitere installierte Rolle oder Funktion erhöht die Chance, dass Schwachstellen auftreten und durch Angreifer entdeckt werden. Nicht alle Schwachstellen sind sofort öffentlich bekannt und nicht für alle bekannten Schwachstellen sind sofort Patches verfügbar. Zudem müssen diese auch erst eingespielt werden.

### 2 8 Unberechtigtes Erlangen oder Missbrauch von Administratorrechten

Die reguläre Arbeit unter Standardbenutzerrechten für Administratoren ist inzwischen gute Praxis. Da der Administrator jedoch an bestimmten Stellen trotzdem seine Rechte erhöhen muss, kann ein Angreifer dort potentiell eingreifen und privilegierte Rechte erlangen. Auch ein Missbrauch von Rechten durch legitime Administratoren ist ein relevantes Schadensszenario. Da die Rollen oft sehr mächtig sind, sind hier die Auswirkungen in der Regel beträchtlich, insbesondere bei Domänenadministratoren. Auch ohne Passwörter zu erraten oder zu brechen, können Angreifer z. B. durch sogenannte Pass-the-Hash-Verfahren geeignete Credentials auslesen und missbrauchen, um sich lateral im Netz weiterzubewegen.

### 2 9 Kompromittierung von Fernzugängen

Da Windows Server 2012 (R2) über eine Vielzahl von Möglichkeiten verfügt, aus der Ferne verwaltet zu werden, können diese grundsätzlich auch missbraucht werden. Fernzugänge, wie z. B. RDP-Benutzersitzungen, können durch unsichere bzw. unsicher verwendete Protokolle, schwache Authentifizierung (z. B. schwache Passwörter) oder fehlerhafte Konfiguration für Dritte erreichbar sein. Hierdurch können der Server und die dort gespeicherten Informationen weitgehend kompromittiert werden. Oft können so auch weitere, mit dem Server verbundene IT-Systeme kompromittiert werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Windows Server 2012 (R2) aufgeführt. Grundsätzlich ist der *IT-Betrieb* für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.1.2.2.A1 Planung von Windows Server 2012

Der Einsatz von Windows Server 2012 (R2) MUSS vor der Installation sorgfältig geplant werden. Die Anforderungen an die Hardware MÜSSEN vor der Beschaffung geprüft werden. Es MUSS eine begründete und dokumentierte Entscheidung für eine geeignete Windows Server 2012 (R2)-Edition getroffen werden. Der Einsatzzweck des Servers MUSS dabei spezifiziert werden, inkl. einer geplanten Einbindung ins Active Directory. Die Nutzung von ins Betriebssystem integrierten Cloud-Diensten MUSS grundsätzlich abgewogen und geplant werden. Wenn nicht benötigt, MUSS die Einrichtung von Microsoft-Konten auf dem Server blockiert werden. 

#### SYS.1.2.2.A2 Sichere Installation von Windows Server 2012

Das Installationsmedium MUSS aus einer nachweislich integren Quelle bezogen werden. Es DÜRFEN KEINE anderen als die benötigten Serverrollen und Features bzw. Funktionen installiert werden. Wenn vom Funktionsumfang her ausreichend, MUSS die Server-Core-Variante installiert werden. Andernfalls MUSS begründet werden, warum die Server-Core-Variante nicht genügt. Der Server MUSS im Rahmen der Installation zunächst auf einen aktuellen Patch-Stand gebracht werden.

#### SYS.1.2.2.A3 Sichere Administration von Windows Server 2012

Lokale Administrationskonten MÜSSEN einzigartige, sichere Passwörter besitzen. Alle Administratoren, die für das Serversystem zuständig sind, MÜSSEN in den sicherheitsrelevanten Aspekten der Administration von Windows Server 2012 bzw. R2 geschult sein. Sie DÜRFEN administrative Rechte NICHT einsetzen, wo diese nicht zwingend erforderlich sind. Browser auf dem Server DÜRFEN NICHT zum Surfen im Web verwendet werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Windows Server 2012. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.1.2.2.A4 Sichere Konfiguration von Windows Server 2012

Es SOLLTEN NICHT mehrere wesentliche Funktionen bzw. Rollen durch einen einzigen Server erfüllt werden. Vor Inbetriebnahme SOLLTE das System grundlegend gehärtet werden. Dafür SOLLTEN funktionsspezifische institutionsweite Sicherheitsvorlagen erstellt und gepflegt werden, die auf die Serversysteme ausgerollt werden. Die Einstellungen SOLLTEN anfangs und bei Änderungen vor Produktivnahme getestet werden. Der Internet Explorer SOLLTE auf dem Server nur in der Enhanced Security Configuration und im Enhanced Protected Mode genutzt werden.

#### SYS.1.2.2.A5 Schutz vor Schadsoftware

Außer bei IT-Systemen mit Windows Server 2012, die stand-alone ohne Netzanschluss und Wechselmedien betrieben werden, SOLLTE vor dem ersten Verbinden mit dem Netz oder Wechselmedien ein Virenschutzprogramm installiert werden. Die Signaturen SOLLTEN regelmäßig aktualisiert werden. Zudem SOLLTEN regelmäßig alle Festplatten vollständig gescannt werden. Es SOLLTEN Alarme für die zuständigen Administratoren bei Virenfunden konfiguriert sein.

#### SYS.1.2.2.A6 Sichere Authentisierung und Autorisierung in Windows Server 2012

In Windows Server 2012 R2 SOLLTEN alle Benutzer Mitglieder der Sicherheitsgruppe "Geschützte Nutzer" sein. Konten für Dienste und Computer SOLLTEN NICHT Mitglied von "Geschützte Nutzer" sein. Service-Accounts in Windows Server 2012 (R2) SOLLTEN Mitglieder der Gruppe "Managed Service Account" sein. Der Local Credential Store LSA SOLLTE geschützt sein. Der Einsatz dynamischer Zugriffsregeln auf Ressourcen SOLLTE bevorzugt werden. 

Die Administratoren von Windows Server 2012 (R2) SOLLTEN auf ihren eigenen Clients mit beschränkten Rechten arbeiten.

#### SYS.1.2.2.A7 Sicherheitsprüfung von Windows Server 2012

Die Sicherheitskonfiguration von Windows Server 2012 (R2) SOLLTE mittels geeigneter Tools regelmäßig überprüft, dokumentiert und verbessert werden.

#### SYS.1.2.2.A8 Schutz der Systemintegrität

Secure Boot SOLLTE aktiv sein. AppLocker SOLLTE aktiviert und möglichst strikt konfiguriert sein. Die Auswirkungen von Änderungen SOLLTEN vorab getestet werden. 

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.1.2.2.A9 Lokale Kommunikationsfilterung(CI)

Die lokale Firewall SOLLTE für eingehenden und ausgehenden Netzverkehr aktiviert und möglichst strikt eingestellt sein. Die Identität von Remote-Systemen und die Integrität der Verbindungen mit diesen SOLLTE kryptographisch abgesichert sein.

#### SYS.1.2.2.A10 Festplattenverschlüsselung bei Windows Server 2012(C)

Bei Systemen mit Windows Server 2012 (R2) SOLLTEN die Datenträger mit BitLocker oder einem anderen Produkt verschlüsselt werden. Dies SOLLTE auch für virtuelle Maschinen mit produktiven Daten gelten. Bei höherem Schutzbedarf SOLLTE nicht nur das TPM allein als Schlüsselschutz dienen. Das Wiederherstellungspasswort SOLLTE im Active Directory oder einem anderen geeigneten sicheren Ort gespeichert werden. Bei sehr hohen Vertraulichkeits- oder Abstreitbarkeitsanforderungen SOLLTE eine Full Volume Encryption erfolgen.

#### SYS.1.2.2.A11 Angriffserkennung bei Windows Server 2012(CIA)

Sicherheitsrelevante Ereignisse in Windows Server 2012 (R2) SOLLTEN an einem zentralen Punkt gesammelt und ausgewertet werden. Verschlüsselte Partitionen SOLLTEN nach einer definierten Anzahl von Entschlüsselungsversuchen gesperrt werden.

#### SYS.1.2.2.A12 Redundanz und Hochverfügbarkeit(A)

Es SOLLTE geprüft werden, welche Verfügbarkeitsanforderungen durch Betriebssystemfunktionen wie Failover Cluster und Network Load Balancing bzw. NIC-Teaming (LBFO) umgesetzt oder unterstützt werden kann. Für Außenstellen SOLLTE BranchCache aktiviert werden.

#### SYS.1.2.2.A13 Starke Authentifizierung bei Windows Server 2012(CI)

Es SOLLTE ein rollenbasiertes Administrations-Modell für die Administration unterschiedlicher Serverfunktionen entworfen und umgesetzt werden. Für kritische Dienste SOLLTE eine Zwei-Faktor-Authentifizierung implementiert sein.

#### SYS.1.2.2.A14 Herunterfahren verschlüsselter Server und virtueller Maschinen(CI)

Um die verschlüsselten Daten auch im Betrieb zu schützen, SOLLTEN nicht benötigte Server (inkl. virtuelle Maschinen) immer heruntergefahren oder in den Ruhezustand versetzt werden. Dies SOLLTE möglichst automatisiert erfolgen. Die Entschlüsselung der Daten SOLLTE einen interaktiven Schritt erfordern, oder sie SOLLTE zumindest im Sicherheitsprotokoll festgehalten werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Windows Server 2012" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ISFSY12] The Standard of Good Practice - Area SY1.2 Server Configuration

  

 Information Security Forum (ISF), June 2016, insbesondere Area SY1.2 - Server Configuration

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
* #### [PAYNE] Windows Event Forwarding for everyone

  

 Microsoft Technet, Blog, Jessica Payne, 11.2015  
 <https://blogs.technet.microsoft.com/jepayne/2015/11/23/monitoring-what-matters-windows-event-forwarding-for-everyone-even-if-you-already-have-a-siem/>

 
* #### [TN831360] Secure Windows Server 2012 R2 and Windows Server 2012, Microsoft

  

 Micorosoft Technet, 11.2013  
 <https://technet.microsoft.com/en-us/library/hh831360.aspx>

 
* #### [TN831778] Security and Protection, Micorosoft

  

 Microsoft Technet, 02.2014  
 <https://technet.microsoft.com/en-us/library/hh831778.aspx>

 
* #### [TN832031] Secure Windows

  

 Für Windows 8/8.1, gilt größtenteils auch für Windows Server 2012 / 2012 R2, 03.2014  
 <https://technet.microsoft.com/en-us/library/hh832031.aspx>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Windows Server 2012" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
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
* G 0.33 Personalausfall
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.41 Sabotage
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

