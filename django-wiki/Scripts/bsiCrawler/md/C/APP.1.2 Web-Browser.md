1 Beschreibung
--------------

### 1.1 Einleitung

Web-Browser sind Anwendungsprogramme, die (Hypertext-)Dokumente, Bilder, Video-, Audio- und andere Datenformate aus dem Internet abrufen, verarbeiten, darstellen, ausgeben und auf lokale IT-Systeme speichern können. Ebenso können Web-Browser auch Daten ins Internet übertragen. Stationäre und mobile Client-Systeme sind heute ohne Web-Browser nicht vorstellbar, weil sehr viele private und geschäftliche Anwendungen entsprechende Inhalte nutzen.

Gleichzeitig werden diese Inhalte im Internet immer vielfältiger. Immer weniger Websites kommen ohne eingebettete Videos, animierte Elemente und andere aktive Inhalte aus. Moderne Web-Browser decken zudem eine große Bandbreite an Zusatzfunktionen ab, indem sie Plug-ins und externe Bibliotheken einbinden. Hinzu kommen Erweiterungen für bestimmte Funktionen, Datenformate und Inhalte. Die Komplexität moderner Web-Browser bietet ein hohes Potential für gravierende konzeptionelle Fehler und programmtechnische Schwachstellen. Sie erhöht nicht nur die möglichen Gefahren für Angriffe aus dem Internet, sondern birgt zusätzliche Risiken durch Programmier- und Bedienungsfehler.

Die Folgen für die Vertraulichkeit und Integrität von Daten sind erheblich. Ebenso ist die Verfügbarkeit des gesamten IT-Systems durch solche Schwachstellen bedroht. Internetinhalte müssen demzufolge aus Sicht des Web-Browsers grundsätzlich als nicht vertrauenswürdig angesehen werden.

### 1.2 Zielsetzung

Dieser Baustein beschreibt Sicherheitsanforderungen für Web-Browser, die auf Client-Systemen, also auf stationären und mobilen Computern sowie teilweise auch auf Tablets und Smartphones, eingesetzt werden. Es werden sowohl zentral verwaltete als auch einzelne Betriebsumgebungen betrachtet.

### 1.3 Abgrenzung

Dieser Baustein enthält grundsätzliche Sicherheitsanforderungen, die bei der Installation und dem Betrieb von Web-Browsern für den Zugriff auf Daten aus dem Internet zu beachten und zu erfüllen sind. Browser für den Zugriff auf rein lokale oder Daten in internen Datennetzen ohne Internetzugriff werden in diesem Baustein nicht behandelt.

Web-Browser sind in eng mit dem Betriebssystem des Client-Systems verzahnt und greifen auf dort bereitgestellte Schnittstellen und Funktionen zurück. Um die Betriebssysteme abzusichern, sollten daher die Anforderungen der Bausteine der Schichten SYS.2.2 *Desktop-Systeme* und SYS.3.2 *Tablet und Smartphone* erfüllt werden.

Viele Plug-ins wie Java werden durch die Web-Browser-Instanzen ausgeführt und laufen in der Regel in separaten Ausführungsumgebungen ab. Anforderungen hierzu sind im Baustein SYS.2.7 *Internet-PC* zu finden.

Mit Browsern genutzte Web-Anwendungen sowie zuständige Server werden in den Bausteinen APP.3.1 *Web-Anwendungen* und APP.3.2 *Webserver* behandelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Web-Browser von besonderer Bedeutung:

### 2 1 Ausführung von Schadcode durch Web-Browser

Web-Browser können Daten aus nicht vertrauenswürdigen oder möglicherweise sogar kompromittierten Quellen laden. Solche Daten können ausführbaren Code mit Schadfunktion enthalten, der Schwachstellen ausnutzen kann und das Gerät des Benutzers ohne dessen Kenntnis und somit unbemerkt infiziert.

Dabei kann es sich um Code handeln, der durch den Web-Browser direkt ausgeführt werden kann, wie etwa JavaScript. Ebenso kann es auch ausführbarer Code eines Plug-ins oder einer Erweiterung im Kontext des Browsers sein, wie etwa Adobe Flash, Java oder Bestandteile von PDF-Dokumenten. Schließlich kann es sich auch um Code handeln, der vom Web-Browser auf den Client geladen und dort außerhalb des Browser-Prozesses ausgeführt wird. Vielfach wird auch durch den Schadcode weitere Schadsoftware nachgeladen, die dann auf dem Client mit den Rechten des Nutzers ausgeführt wird. Werden die grundlegenden Schutzmechanismen moderner Web-Browser nicht ausreichend angewendet, werden die Vertraulichkeit, Integrität oder Verfügbarkeit von Informationen oder Diensten des Clients oder der möglicherweise verbundenen Netze bedroht.

### 2 2 Exploit Kits

Schwachstellenlisten und sogenannte Exploit Kits erleichtern die Entwicklung individueller Schadsoftware erheblich. Cyberangriffe können automatisiert werden, um Drive-by-Downloads oder andere Verbreitungswege leicht und ohne Expertenwissen zu nutzen. Angreifer können ihnen bekannte Schwachstellen des Web-Browsers oder einer verbundenen Ressource oder Erweiterung ausnutzen, um Folgeangriffe vorzubereiten oder Code mit Schadfunktion auf den Client zu laden und zu installieren.

### 2 3 Mitlesen der Internetkommunikation

Die grundlegende Sicherheit der Kommunikation im Internet hängt ganz wesentlich vom eingesetzten Authentisierungsverfahren und von der Verschlüsselung der Daten auf dem Transportweg ab. Die nötigen Verfahren sind oft schlecht implementiert.

Schwache Implementierungen der nötigen Verfahren sind weit verbreitet und verhindern eine wirkungsvolle Authentisierung und Verschlüsselung. Viele Webdienste wenden außerdem immer noch veraltete Verschlüsselungsverfahren an. Somit kann ein Angreifer die Authentisierung von Servern unterlaufen oder die Kommunikation bzw. die Daten werden nicht wirkungsvoll verschlüsselt. Hierdurch können Informationen auf dem Übertragungsweg mitgelesen oder verändert werden. In der Vergangenheit wurden außerdem Zertifizierungsstellen kompromittiert, hierdurch konnten Angreifer an Zertifikate für fremde Websites gelangen. 

### 2 4 Integritätsverlust in Web-Browsern

Werden Browser, Plug-ins oder Erweiterungen aus nicht vertrauenswürdigen Quellen bezogen, können unabsichtlich und unbemerkt Schadfunktionen ausgeführt werden. Angreifer können beispielsweise Komponenten wie Toolbars von Web-Browsern fälschen, um die Benutzer auf manipulierte Kopien von Webseiten zu locken, mit deren Hilfe Phishing-Angriffe durchgeführt werden. Bösartige Erweiterungen können Inhalte der betrachteten Webseiten manipulieren oder Daten ausspionieren und an den Angreifer senden.

### 2 5 Verlust der Privatsphäre

Werden Browser unsicher konfiguriert, können so vertrauenswürdige Daten zufällig oder böswillig unbefugten Dritten zugänglich gemacht werden. Auch Passwörter können ungewollt weitergegeben werden. Werden Cookies, Passwörter, Historien, Eingabedaten und Suchanfragen gespeichert oder unnötige Erweiterungen aktiviert, können Daten von Dritten oder von Schadprogrammen leichter missbräuchlich ausgelesen werden.

### 2 6 Fehler bei Administration und Betrieb

Fehler in der Administration des Web-Browsers können zu einer unsicheren Konfiguration und zu unsicherem Betrieb führen. Ein wesentliches Bedrohungspotential erwächst in der mangelhaften Aktualität und Pflege des verwendeten Web-Browsers. Browserhersteller bieten zudem oftmals Sicherheitsupdates nicht zeitnah genug an. Dadurch steigt die Verbreitungsrate von ausnutzbaren Schwachstellen signifikant.

3 Anforderungen
---------------

Im Folgenden sind die spezifischen Anforderungen für Web-Browser aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der Informationssicherheitsbeauftragte dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.1.2.A1 Verwendung von Sandboxing

Der eingesetzte Web-Browser MUSS über sicherstellen, das jede Instanz und jeder Verarbeitungsprozess nur auf die eigenen Ressourcen zugreifen kann (Sandboxing). Web-Seiten MÜSSEN als eigenständige Prozesse oder mindestens als eigene Threads voneinander isoliert werden. Plug-ins und Erweiterungen MÜSSEN ebenfalls in isolieren Bereichen ausgeführt werden. Der verwendete Web-Browser SOLLTE die Content Security Policy gemäß den W3C-Spezifikationen umsetzen.

#### APP.1.2.A2 Verschlüsselung der Kommunikation

Der Web-Browser MUSS Transport Layer Security (TLS) in einer sicheren Version unterstützen. Unsichere Versionen von TLS Version SOLLTEN deaktiviert werden. Der Web-Browser MUSS den Sicherheitsmechanismus HTTP Strict Transport Security (HSTS) gemäß RFC 6797 unterstützen. Für alle wichtigen öffentlichen TLS-verschlüsselten Web-Dienste SOLLTEN die Domains in die HSTS-Preload-Liste des Browsers eingefügt werden.

#### APP.1.2.A3 Verwendung von Zertifikaten [Benutzer]

Der Web-Browser MUSS eine Liste vertrauenswürdiger Wurzelzertifikats-Aussteller bereitstellen sowie die von der Institution selbst bereitgestellte Zertifikate akzeptieren. Der Web-Browser MUSS Extended-Validation-Zertifikate unterstützen. Wurzelzertifikate DÜRFEN NUR mit Administrationsrechten hinzugefügt, geändert, oder gelöscht werden. Zertifikate MÜSSEN durch den Web-Browser (lokal) widerrufen werden können.

Der Web-Browser MUSS die Gültigkeit der Server-Zertifikate mit Hilfe des öffentlichen Schlüssels und des Gültigkeitszeitraums vollständig prüfen. Der Sperrstatus der Server-Zertifikate MUSS vom Web-Browser geprüft werden. Die Zertifikatskette einschließlich des Wurzelzertifikats MUSS verifiziert werden.

Der Web-Browser MUSS dem Benutzer eindeutig und gut bemerkbar darstellen, ob die Kommunikation im Klartext oder verschlüsselt erfolgt. Der Web-Browser SOLLTE dem Benutzer auf Anforderung das verwendete Serverzertifikat anzeigen können. Der Web-Browser MUSS dem Benutzer signalisieren, wenn Zertifikate fehlen, ungültig sind oder widerrufen wurden. Die verschlüsselte Verbindung DARF in einem solchen Fall NUR nach ausdrücklicher Bestätigung durch den Benutzer hergestellt werden.

#### APP.1.2.A4 Versionsprüfung und Aktualisierung des Web-Browsers

Der Web-Browser MUSS über einen Mechanismus verfügen, der den eigenen Versionsstand sowie denjenigen aller geladenen oder aktivierten Erweiterungen und Plug-ins zuverlässig erkennen und anzeigen kann.

Updates für den Web-Browser, Plug-ins und Erweiterungen MÜSSEN unverzüglich eingespielt werden. Der Web-Browser SOLLTE Updates automatisch einspielen können. Ist kein Update für eine bekannt gewordene kritische Schwachstelle verfügbar, MÜSSEN zeitnah Maßnahmen zur Mitigation ergriffen werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Web-Browser. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.1.2.A5 Basiskonfiguration

Der Browser SOLLTE zentral konfiguriert werden können. Zentral vorgegebene Einstellungen DÜRFEN NICHT von den Benutzern verändert werden können. Der Web-Browser SOLLTE NICHT dauerhaft mit erweiterten Rechten ausgeführt werden.

#### APP.1.2.A6 Kennwortmanagement im Web-Browser [Benutzer]

Wird ein Kennwortmanager im Browser verwendet, SOLLTE er eine direkte und eindeutige Beziehung zwischen Webseite und hierfür gespeichertem Kennwort herstellen. Der Kennwortspeicher SOLLTE geschützt sein. Auf die im Kennwortmanager gespeicherten Passwörter SOLLTE nur nach Eingabe eines Master-Kennwortes zugegriffen werden können. Die Authentisierung für den kennwortgeschützten Zugriff SOLLTE nur für die aktuelle Sitzung gültig sein. Der Kennwortmanager SOLLTE die Qualität der Kennwörter entsprechend der Sicherheitsrichtlinie der Institution vorgegeben. Die gespeicherten Kennwörter SOLLTEN durch den Benutzer gelöscht werden können.

#### APP.1.2.A7 Schutz von Daten [Benutzer]

Cookies von Drittanbietern SOLLTEN abgelehnt werden. Gespeicherte Cookies SOLLTEN durch den Benutzer gelöscht werden können.

Die Funktion zur Auto-Vervollständigung von Daten SOLLTE deaktiviert werden. Wird die Funktion doch genutzt, SOLLTE der Benutzer die Vervollständigungsdaten löschen können. Der Benutzer SOLLTE außerdem die Historiendaten des Browsers löschen können.

Sofern vorhanden, SOLLTE eine Synchronisationen des Browsers mit Cloud-Diensten deaktiviert werden. Telemetriefunktionen sowie das automatische Senden von Absturzberichten an den Hersteller SOLLTEN soweit wie möglich deaktiviert werden.

Sind Peripheriegeräte wie Mikrofon oder Webcam angeschlossen, SOLLTEN diese im Browser deaktiviert werden. Der Browser SOLLTE eine Möglichkeit bieten, um WebRTC, HSTS und JavaScript zu konfigurieren bzw. abzuschalten.

#### APP.1.2.A8 Verwendung von Plug-ins und Erweiterungen [Benutzer]

Es SOLLTEN nur unbedingt notwendige Plug-ins und Erweiterungen installiert werden. Plug-ins und Erweiterungen für den Browser SOLLTEN nur mit Administrationsrechten installiert werden dürfen. Die Ausführung von Plug-ins SOLLTE immer vom Benutzer bestätigt werden müssen. Der Browser SOLLTE die Möglichkeit bieten, Erweiterungen zu konfigurieren und abzuschalten.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.1.2.A9 Einsatz einer isolierten Browser-Umgebung

Bei erhöhtem Schutzbedarf SOLLTEN Web-Browser eingesetzt werden, die in einer isolierten Umgebung (wie ReCoBS) oder auf dedizierten IT-Systemen laufen.

#### APP.1.2.A10 Verwendung des privaten Modus [Benutzer]

Der Browser SOLLTE bei erhöhten Anforderungen bezüglich der Vertraulichkeit im sogenannten privaten Modus ausgeführt werden, sodass keinerlei Informationen oder Inhalte persistent auf dem IT-System des Benutzers gespeichert werden. Der Browser SOLLTE so konfiguriert werden, dass lokale Inhalte beim Beenden gelöscht werden.

#### APP.1.2.A11 Überprüfung auf schädliche Inhalte

Aufgerufene Internetadressen SOLLTEN durch den Browser auf potentiell schädliche Inhalte geprüft werden. Der Browser SOLLTE den Benutzer in geeigneter Form warnen, wenn Informationen über schädliche Inhalte vorliegen. Eine als schädlich klassifizierte Verbindung SOLLTE nicht aufgerufen werden können. Das verwendete Verfahren zur Überprüfung DARF NICHT gegen Datenschutz- oder Geheimschutz-Vorgaben verstoßen.

#### APP.1.2.A12 Zwei-Browser-Strategie

Für den Fall von ungelösten Sicherheitsproblemen mit dem verwendeten Web-Browser SOLLTE ein alternativer Browser eines anderen Herstellers installiert sein, um als Ausweichmöglichkeit dienen zu können. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Web-Browser" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [AbWeB] Absicherungsmöglichkeiten beim Einsatz von Web-Browsern

  

 Bundesamt für Sicherheit in der Informationstechnik, Version 1.0, 2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_047.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_047.pdf)

 
* #### [ACSDB] SSL Cipher Suite Details of Your Browser

  

 Aktive Cipher Suites Detais des Browsers, Check Möglichkeiten, (zuletzt abgerufen am 28.09.2017)  
 <https://cc.dcsec.uni-hannover.de/>

 
* #### [CSP] Content Security Polic W3C

  

 W3, Version 1.0, 2012  
 <https://www.w3.org/TR/2012/CR-CSP-20121115/>

 
* #### [HSTS] HTTP Strict Security Policy (HSTS), RFC 6797

  

 IETF, 2012  
 <https://tools.ietf.org/html/rfc6797>

 
* #### [MDST8SSL] Mindeststandard des BSI nach §8 Absatz 1 Satz 1 BSIG für den Einsatz des SSL/ TLS-Protokoll in der Bundesverwaltung

  

 Bundesamt für Sicherheit in der Informationstechnik, Version 1.0, 2015  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_0.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_BSI_TLS_1_2_Version_1_0.pdf)

 
* #### [MDST8Web] Mindeststandard des BSI nach §8 Absatz 1 Satz 1 BSIG für den sicheren Einsatz von Web-Browsern in der Bundesverwaltung

  

 Bundesamt für Sicherheit in der Informationstechnik, Version 1.0, 2017  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard\_Sichere\_Web-Browser.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Mindeststandard_Sichere_Web-Browser.pdf)

 
* #### [OWASPList] OWASP List of the 10 Most Critical Web Application Security Risks

  

 OWASP, (zuletzt abgerufen am 28.09.2017)  
 [https://www.owasp.org/index.php/Category:OWASP\_Top\_Ten\_Project](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)

 
* #### [ReCoBS] Common Criteria Protection Profile for Remote-Controlled Browsers System (ReCoBS)

  

 BSI, BSI-PP-0040; Version 1.0, 2008  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo\_pdf.pdf?\_blob=publicationBundesamt](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Internetsicherheit/recobslanginfo_pdf.pdf?_blob=publicationBundesamt)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Web-Browser" von Bedeutung.

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
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

