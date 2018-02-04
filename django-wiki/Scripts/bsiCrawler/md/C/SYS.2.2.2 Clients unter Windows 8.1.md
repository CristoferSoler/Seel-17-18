1 Beschreibung
--------------

### 1.1 Einleitung

Mit Windows 8 hat Microsoft sein Client-Betriebssystem Windows sowie die damit eingeführten Funktionen und Komponenten weiterentwickelt. Neu an Windows 8 ist die auf den Einsatz portabler Geräte mit Touchscreen ausgerichtete Bedienungsführung. Diese bringt ein neues Bedienkonzept für Anwendungen mit sich. Neben den klassischen Desktop-Anwendungen hat Microsoft dazu eine Klasse mobiler Anwendungen zur Nutzung unter Windows 8 vorgesehen, die sogenannten "Apps". Diese sind konsequent auf die Steuerung durch Berührung ausgelegt. Zusätzlich können sie als "Kachel" auf dem Bildschirm Anzeigefunktionen wahrnehmen. Einige Anwendungen, allen voran der mit Windows 8 ausgelieferte Internet Explorer, stehen entsprechend in zwei Varianten für Windows 8 zur Verfügung. Seit der Markteinführung von Windows 8 hat Microsoft einige Verbesserungen vorgenommen und in das Betriebssystem integriert, das damit die Versionsnummer 8.1 erhält.

### 1.2 Zielsetzung

Zielsetzung dieses Bausteins ist der Schutz von Informationen, die durch und auf Windows 8.1-Clients verarbeiten werden.

### 1.3 Abgrenzung

Dieser Baustein ist auf alle Zielobjekte anzuwenden, auf denen das Betriebssystem Windows 8.1 betrieben werden. Soweit die beschriebenen Sicherheitsanforderungen und Gefährdungen ausschließlich für Windows 8 gelten, ist dies explizit in den Texten ausgewiesen. Die Anforderungen aus dem Baustein [ *SYS.2.1 Allgemeiner Client*](DE/Themen/ITGrundschutz/ITGrundschutzKompendium/bausteine/SYS/SYS_2_1_Allgemeiner_Client.html?nn=10137184 "SYS.2.1 Allgemeiner Client") sind in jedem Fall ebenfalls zu erfüllen. Der vorliegende Baustein präzisiert und ergänzt Anforderungen, die für Windows 8.1 spezifisch sind. Für Anwendungsprogramme, die auf den Windows-Clients verwendet werden, sind die Anforderungen der entsprechenden Bausteine zu erfüllen, beispielsweise APP.1.1 Office-Produkte oder APP.1.6 Browser. Beim Einsatz in einer Windows-Domäne sind die Anforderungen der entsprechenden Bausteine wie APP.2.2 Active Directory zu erfüllen.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Windows 8.1 von besonderer Bedeutung:

### 2 1 Auf Windows ausgerichtete Schadprogramme

Schadprogramme bieten einem Angreifer umfangreiche Kommunikations- als auch Steuerungsmöglichkeiten und besitzen eine Vielzahl von Funktionen. Unter anderem können Schadprogramme gezielt Passwörter ausforschen, Systeme fernsteuern, Schutzsoftware deaktivieren und Daten ausspionieren. Ein Wechseldatenträger könnte so manipuliert werden, dass Schadsoftware ausgeführt und installiert wird, wenn der Wechseldatenträger eingelegt oder angeschlossen wurde. Als Schaden ist hier insbesondere der Verlust oder die Verfälschung von Informationen oder Anwendungen von größter Tragweite. Aber auch ein Imageverlust und finanzieller Schaden, der folglich durch Schadprogramme entstehen kann, ist von großer Bedeutung. Windows ist aufgrund seiner großen Verbreitung ein primäres Ziel für Angriffe mit Schadprogrammen, so dass hier eine große Bedrohung durch zahlreiche Angreifer und Angriffsarten besteht.

### 2 2 Software-Schwachstellen oder -Fehler

Windows 8.1 ist inklusive seiner zahlreichen mitgelieferten Anwendungen ein sehr komplexes Software-Produkt. Werden Software-Fehler darin nicht rechtzeitig erkannt, können die bei der Anwendung entstehenden Abstürze oder Fehler zu weitreichenden Folgen führen (z. B. falsche Berechnungsergebnisse, Fehlentscheidungen der Leitungsebene und Verzögerungen beim Ablauf der Geschäftsprozesse). Durch Software-Schwachstellen oder -Fehler können schwerwiegende Sicherheitslücken in einzelnen Anwendungen, dem gesamten IT-System oder sogar allen damit vernetzten IT-Systemen entstehen. Sicherheitslücken in Windows können unter Umständen von Angreifern ausgenutzt werden, um Schadsoftware einzuschleusen, unerlaubt Daten auszulesen oder zu manipulieren.

### 2 3 Integrierte Cloud-Funktionalitäten

Windows 8.1 bringt zahlreiche Funktionen mit, mit denen Daten in den Cloud-Diensten von Microsoft abgelegt und darüber synchronisiert werden. Dadurch besteht die Gefahr, Cloud-Diensten unbewusst (oder zumindest unbedacht) auch für möglicherweise sensible oder personenbezogene Daten zu nutzen. Gleichzeitig kann auch gegen Datenschutzgesetze verstoßen werden, wenn Daten bei Dritten, vor allem im Ausland gespeichert werden. Meldet sich ein Benutzer mit bereits aktiviertem Microsoft-Account an ein neues Gerät an, werden dort automatisch die von ihm genutzten Microsoft-Cloud-Dienste eingerichtet. So können Daten des Unternehmens ungewollt auf die privaten Geräte der Mitarbeiter synchronisiert werden. Als weiteres Beispiel bietet Windows 8 als Standardeinstellung die Möglichkeit, den Bitlocker-Recovery-Schlüssel direkt über den Microsoft-Account in der Cloud zu sichern. Damit werden kritische kryptographische Geheimnisse in die Hände Dritter gegeben.

### 2 4 Beeinträchtigung von Software-Funktionen durch Kompatibilitätsprobleme

Software, die auf Windows-Vorgängerversionen erfolgreich betrieben wurde, muss nicht auch mit einer aktuellen Version des Betriebssystems zusammenarbeiten. Mögliche Ursachen sind neue Sicherheitsmerkmale oder Betriebssystemeigenschaften, sowie der Wegfall von Funktionalitäten oder Diensten. In der Folge kann die Software nicht oder nur mit Einschränkungen verwendet werden. Bei neuen Windows-Versionen kann beispielsweise die Aktivierung neuer Sicherheitsmerkmalen zu Kompatibilitätsproblemen führen. Beispiele dafür sind die Benutzerkontensteuerung (UAC) oder bei 64-Bit-Versionen des Betriebssystems Kernel Patch Guard sowie die Notwendigkeit signierter Treiber. Bei neueren Windows-Versionen fallen aber auch Funktionalitäten weg. Ein Beispiel hierfür ist der Wegfall der GINA-Anmeldekomponente in neueren Windows-Versionen, die z. B. von einigen Fingerabdrucklesern verwendet wurde. 

### 2 5 Fehlerhafte Administration oder Nutzung von Geräten und Systemen

Windows-Betriebssysteme sind komplexe Systeme, deren Sicherheit im Wesentlichen durch die eingestellten Parameter bestimmt wird. Dadurch können insbesondere Fehlkonfiguration von Komponenten die Sicherheit beeinträchtigen, sodass es zu Fehlfunktionen kommen kann oder das IT-System kompromittiert wird. Grundsätzlich beinhaltet jede Schnittstelle an einem IT-System nicht nur die Möglichkeit, darüber bestimmte Dienste des IT-Systems berechtigt zu nutzen, sondern auch das Risiko, dass darüber unbefugt auf das IT-System zugegriffen wird. Wenn etwa durch Fehlkonfiguration der Windows-eigenen Authentisierungsmechanismen Benutzerkennungen und zugehörige Passwörter ausgespäht werden können, ist eine unberechtigte Nutzung der damit geschützten Anwendungen oder IT-Systeme denkbar.

Auch eine fehlerhafte oder nicht ordnungsgemäße Nutzung von Geräten, Systemen und Anwendungen kann die Sicherheit unter Windows beeinträchtigen, vor allem, wenn vorhandene Sicherheitsmaßnahmen missachtet oder umgangen werden. Zu großzügig vergebene Rechte, leicht zu erratende Passwörter, nicht ausreichend geschützte Datenträger mit Sicherungskopien oder bei vorübergehender Abwesenheit nicht gesperrte Arbeitsplätze können zu Sicherheitsvorfällen führen. Eine weitere Folge der fehlerhaften Bedienung von Windows-Systemen oder Anwendungen kann das versehentlich Löschen oder Verändern von Daten sein. Dabei ist es ebenfalls möglich, dass vertrauliche Informationen an die Öffentlichkeit gelangen, wenn beispielsweise Zugriffsrechte falsch gesetzt werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Windows 8.1 aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.2.2.2.A1 Geeignete Auswahl einer Windows 8.1-Version

Es MUSS der Funktionsumfang einer Windows-Version vor der Beschaffung auf die Einsatzfähigkeit geprüft und eine geeignete Version ausgewählt werden. Es SOLLTEN bevorzugt 64-Bit Versionen eingesetzt werden, die erweiterte Sicherheitsfeatures enthalten.

#### SYS.2.2.2.A2 Festlegung eines Anmeldeverfahrens

Abhängig von den Sicherheitsanforderungen MUSS entschieden werden, ob neben dem klassischen Anmeldeverfahren mit Passwort auch andere Mechanismen wie PIN erlaubt sein sollen. Dies MUSS entsprechend auf allen Clients eingestellt werden.

#### SYS.2.2.2.A3 Einsatz von Viren-Schutzprogrammen

Sofern nicht gleich- oder höherwertige Maßnahmen zum Schutz des IT-Systems vor einer Infektion mit Schadsoftware getroffen wurden, MUSS ein Virenschutz-Programm auf Windows 8-Clients eingesetzt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Clients unter Windows 8.1. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.2.2.2.A4 Beschaffung von Windows 8.1

Die Anforderungen gemäß der Windows Hardware Certification Requirements SOLLTEN bei der Beschaffung von Windows 8.1 bzw. der entsprechenden Hardware für das Windows 8.1-System berücksichtigt werden. Des weiteren SOLLTEN die zu beschaffenden Systeme über eine Firmware-Konfigurationsoberfläche für UEFI SecureBoot und für das TPM (sofern vorhanden) verfügen, die die Kontrolle durch den Eigentümer ermöglicht. Der Beschaffungsprozess von Windows 8.1 SOLLTE die Auswahl eines geeigneten Lizenzmodells enthalten.

#### SYS.2.2.2.A5 Lokale Sicherheitsrichtlinien

Es SOLLTEN alle sicherheitsrelevanten Einstellungen über Sicherheitsrichtlinien bedarfsgerecht konfiguriert, getestet und regelmäßig überprüft werden. Alle nicht benötigten Anwendungen und Komponenten SOLLTEN mittels Sicherheitsrichtlinien deaktiviert werden. Die Verteilung der Sicherheitseinstellungen auf mehrere Windows-8.1-Clients SOLLTE entsprechend der Gegebenheiten der Institution erfolgen.

#### SYS.2.2.2.A6 Datei- und Freigabeberechtigungen

Um eine einheitliche restriktive Rechtevergabe zu ermöglichen, SOLLTE ein Berechtigungs- und Zugriffskonzept für Windows vorhanden sein, das geeignete Datei- und Verzeichnisberechtigungen nach dem Need-to-Know-Prinzip für Inhalte auf den Windows-8.1-Clients definiert. 

Neben Berechtigungen auf dem lokalen Dateisystem SOLLTE das Berechtigungs- und Zugriffskonzept die Zugriffsrechte für freigegebene Verzeichnisse im Netzzugriff beachten. Eine Prüfung der Berechtigungen der Dateien und Verzeichnisse SOLLTE insbesondere bei Rechnern, die von älteren Betriebssystemversionen aktualisiert wurden, erfolgen.

#### SYS.2.2.2.A7 Einsatz der Windows-Benutzerkontensteuerung UAC

Um eine restriktive Rechtevergabe zu unterstützen, SOLLTE die Benutzerkontensteuerung (UAC, User Account Control) aktiviert sein. Für Standardbenutzer SOLLTE festgelegt sein, dass die Aufforderung zur Passworteingabe für erhöhte Rechte automatisch abgelehnt wird. Für Administratorkonten SOLLTE die Einstellung von UAC zwischen Bedienbarkeit und Sicherheitsniveau abgewogen werden. Die Entscheidung SOLLTE dokumentiert und die entsprechenden Einstellungen konfiguriert werden. Es SOLLTE regelmäßig geprüft werden, ob die Notwendigkeit noch besteht und die Rechte entsprechend angepasst oder entzogen werden.

#### SYS.2.2.2.A8 Verwendung der Heimnetzgruppen-Funktion [Benutzer]

Clients SOLLTEN keine Dienste wie Datei- oder Druckerfreigaben anbieten. Eine Sicherheitsrichtlinie (GPO) mit der Einstellung "Beitritt des Computers zu einer Heimnetzgruppe verhindern" SOLLTE für alle Clients gelten. Wird die Funktion aus betrieblichen Gründen eingesetzt, SOLLTEN die Benutzer im Umgang mit den Freigaben der Heimnetzgruppe geschult werden.

#### SYS.2.2.2.A9 Datenschutz und Datensparsamkeit bei Windows 8.1-Clients [Benutzer]

Werden Microsoft-Konten für die Benutzer angelegt, SOLLTEN nur unbedingt erforderliche Angaben zu den Personen hinterlegt werden. Die SmartScreen-Funktion SOLLTE auf die Verträglichkeit mit internen oder externen Datenschutzvorgaben überprüft und bewertet werden. Bevor eine Anwendung oder App zur Nutzung innerhalb der Institution freigegeben wird, SOLLTE sorgfältig geprüft werden, welche Daten Anwendungen und Apps automatisch an die Microsoft-Cloud übersenden. Anwendungen SOLLTEN so konfiguriert werden, dass keine solchen Daten übertragen werden. Apps mit unerwünschter oder unnötig umfangreicher Datenübertragung an Dritte SOLLTEN nicht verwendet werden.

#### SYS.2.2.2.A10 Integration von Online-Konten in das Betriebssystem

Die Anmeldung am IT-System und der Domäne SOLLTE nur mit einem Konto eines selbst betriebenen Verzeichnisdienstes, wie z. B. Active Directory, möglich sein. Eine lokale Anmeldung SOLLTE Administratoren vorbehalten sein. Bei Verwendung von Online-Konten zur Anmeldung, z. B. eines Microsoft-Kontos oder Konten anderer Anbieter von Diensten zum Identitätsmanagement, SOLLTE auf ausreichende Sicherheit des Anbieters und auf die Einhaltung des Datenschutzes geachtet werden.

#### SYS.2.2.2.A11 Konfiguration von Synchronisationsmechanismen in Windows 8.1

Die Synchronisierung von Nutzerdaten mit Microsoft Cloud-Diensten SOLLTE vollständig deaktiviert werden.

#### SYS.2.2.2.A12 Zentrale Authentifizierung in Windows-Netzwerken

In reinen Windows-Netzen SOLLTE zur zentralen Authentifizierung für SSO (Single Sign On) ausschließlich Kerberos eingesetzt werden. Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern. Die Speicherung der LAN-Manager-Hashwerte bei Kennwortänderungen SOLLTE per Gruppenrichtlinie deaktiviert werden. Die Überwachungseinstellungen gemeinsam mit den Serverkomponenten von DirectAccess SOLLTEN sorgfältig auf die Anforderungen des Informationsverbunds abgestimmt werden. Eine Protokollierung auf Clientseite SOLLTE sichergestellt werden.

#### SYS.2.2.2.A13 Anbindung von Windows 8.1 an AppStores

Die Möglichkeit zur Installation von Apps aus dem Microsoft AppStore SOLLTE deaktiviert werden, sofern sie nicht benötigt wird.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.2.2.2.A14 Anwendungssteuerung mit Software Restriction Policies und AppLocker(CIA)

Anwendungen in Pfaden, die von Benutzern schreibbar sind, SOLLTEN durch Software Restriction Policies (SRP) oder AppLocker an der Ausführung gehindert werden. Die Verwaltung der AppLocker- und SRP-GPO in einem domänenbasierten Netz SOLLTE zentralisiert mittels Gruppenrichtlinienobjekten je Benutzer/Benutzergruppe erfolgen.

AppLocker SOLLTE nach dem Ansatz einer Positivliste genutzt werden. Es sollte alles verboten werden, was nicht explizit erlaubt ist. Bei AppLocker SOLLTEN bevorzugt Regeln auf der Grundlage von Anwendungssignaturen definierter Herausgeber genutzt werden. Versuchte Regelverstöße SOLLTEN protokolliert und geeignet ausgewertet werden. 

Für Clients mit besonders hohen Anforderungen an die Sicherheit SOLLTE AppLocker die Ausführung aller ungenehmigten Anwendungen verhindern, statt diese zu protokollieren.

Die Umsetzung der SRP- und AppLocker-Regeln SOLLTEN vor dem Einsatz auf einem produktiven System zunächst auf einem Testsystem oder durch den Betrieb im Überwachungsmodus erprobt werden.

#### SYS.2.2.2.A15 Verschlüsselung des Dateisystems mit EFS(CI)

Bei erhöhtem Schutzbedarf SOLLTE das Dateisystem verschlüsselt werden. Wird hierzu das Encrypting File System (EFS) verwendet, SOLLTE ein komplexes Passwort für den Schutz der mit EFS verschlüsselten Daten verwendet werden. Zusätzlich SOLLTEN die mit EFS verschlüsselten Dateien durch restriktive Zugriffsrechte geschützt werden. Statt des Administratorkontos SOLLTE ein dediziertes Konto der Wiederherstellungsagent sein. Der private Schlüssel dieses Kontos SOLLTE auf einen externen Datenträger ausgelagert und sicher aufbewahrt sowie aus dem System entfernt werden. Dabei SOLLTEN von allen privaten Schlüsseln Datensicherungen erstellt werden. Beim Einsatz von EFS mit lokalen Benutzerkonten SOLLTE die Registry-Verschlüsselung mittels syskey verwendet werden. Beim Einsatz von EFS SOLLTEN die Benutzer im korrekten Umgang mit EFS geschult werden.

#### SYS.2.2.2.A16 Verwendung der Windows PowerShell(CIA)

Wenn die Windows PowerShell (WPS) nicht benötigt wird, SOLLTE sie deinstalliert werden. Bei Windows 8.1 lässt sich die PowerShell-Skriptumgebung allerdings nur noch entfernen, wenn auch das .NET-Framework deinstalliert wird. Daher SOLLTE alternativ die Ausführung der WPS-Dateien nur den Gruppen der Administratoren, lokal und Domäne, gestattet werden. Die Protokollierung von Schreib- und Lesezugriffen auf das Windows PowerShell-Profil SOLLTE aktiviert und für eine regelmäßige Kontrolle der Protokolle gesorgt werden. Die Ausführung von Windows PowerShell-Skripten mit dem Befehl "Set-Execution Policy AllSigned" SOLLTE eingeschränkt werden, um zumindest die versehentliche Ausführung unsignierter Skripte zu verhindern.

#### SYS.2.2.2.A17 Sicherer Einsatz des Wartungscenters(CIA)

In der Sicherheitsrichtlinie SOLLTE der Umgang mit dem Wartungscenter durch die Benutzer definiert werden, Änderungen der Standard-Starteinstellungen der Windows 8-Dienste DPS, WDiSvcHost und WerSvc sind notwendig. Die Einstellungen für "Neueste Problembehandlungen vom Windows-Onlinedienst für Problembehandlung abrufen", "Problemberichte senden", "Regelmäßig Daten über Computerkonfiguration an Microsoft senden", "Windows-Sicherung", "Programm zur Benutzerfreundlichkeit" und "Problembehandlung - andere Einstellungen" SOLLTEN unter Windows 8.1 deaktiviert werden.

#### SYS.2.2.2.A18 Aktivierung des Last-Access-Zeitstempels(A)

Im Rahmen der Erstellung eines Sicherheitskonzeptes für ein IT-System mit Windows 8.1 SOLLTE geprüft werden, ob der Last-Access-Zeitstempel aktiviert wird, um die Analyse eines Systemmissbrauchs zu erleichtern. Dabei SOLLTEN besonders Performance-Aspekte bei der Prüfung berücksichtigt werden.

#### SYS.2.2.2.A19 Verwendung der Anmeldeinformationsverwaltung(C)

Die Erlaubnis oder das Verbot der Speicherung von Zugangsdaten im sogenannten "Tresor" SOLLTE in einer Richtlinie festgelegt werden. Ein Verbot SOLLTE technisch durchgesetzt werden.

#### SYS.2.2.2.A20 Sicherheit beim Fernzugriff über RDP(CIA)

Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTE bei der Planung der Remote-Unterstützung berücksichtigt werden. Die Gruppe der berechtigten Benutzer für den Remote-Desktopzugriff SOLLTE durch die Zuweisung entsprechender Benutzerrechte und in der Richtlinie festgelegt werden. Eine Remote-Unterstützung SOLLTE nur nach einer expliziten Einladung über EasyConnect oder auf Grundlage einer Einladungsdatei erfolgen. Bei der Speicherung einer Einladung in einer Datei SOLLTE die Datei mit einem Kennwort geschützt sein. Der aktuell angemeldete Benutzer SOLLTE dem Aufbau einer Sitzung immer explizit zustimmen müssen. Die maximale Gültigkeitsdauer der Einladung SOLLTE eine angemessene Größe haben. Zudem SOLLTE eine starke Verschlüsselung (128 Bit, Einstellung "Höchste Stufe") verwendet werden. Außerdem SOLLTE die automatische Kennwortanmeldung deaktiviert werden. Es SOLLTE geprüft werden, ob Umleitungen der Zwischenablage, Drucker, Dateiablage und Smartcard-Anschlüsse notwendig sind, andernfalls SOLLTEN diese deaktiviert werden. Sofern der Einsatz der Fernsteuerungsmechanismen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden.

#### SYS.2.2.2.A21 Einsatz von File und Registry Virtualization(CI)

Es SOLLTE geprüft werden, ob der Betrieb von Altanwendungen noch notwendig ist, die Schreib­rechte auf kritische System-Ordner oder Registry-Schlüssel erfordern oder mit Administratorrechten ausgeführt werden müssen. Sofern dies zutrifft, SOLLTE eine Strategie entwickelt werden, um die noch benötigten Altanwendungen auf sichere Alternativen umzustellen. Bis zur Ablösung der Altanwendungen SOLLTE der Einsatz der Windows-Techniken File Virtualization und Registry Virtualization zur Absicherung geprüft werden. Zusätzlich SOLLTE die Registry Virtualization nur auf die notwendigen Registry-Schlüssel Zugriff haben.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Clients unter Windows 8.1" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [MicSAO] Security Auditing Overview ,Microsoft, 07.2013

  

 <https://technet.microsoft.com/en-us/library/dn319078.aspx>

 
* #### [MicSE] Liste von Sicherheitsereignissen: Windows 8 und Windows Server 2012, Microsoft, (zuletzt abgerufen am 27.09.2017)

  

 <https://www.microsoft.com/en-us/download/confirmation.aspx?id=50034>

 
* #### [WIN8] Informationen zu Einsatz, Bereitstellung und Verwaltung von Windows 8.1, Micorosoft, (zuletzt abgerufen am 27.09.2017)

  

 <https://technet.microsoft.com/de-de/windows/windows-8.aspx>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Clients unter Windows 8.1" von Bedeutung.

* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.39 Schadprogramme
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

