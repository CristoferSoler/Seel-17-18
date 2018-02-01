1 Beschreibung
--------------

### 1.1 Einleitung

Mit Windows 10 hat Microsoft sein Client-Betriebssystem Windows an eine neue Unternehmensstrategie angepasst. Verändert hat sich insbesondere auch die Designphilosophie des Betriebssystems weg von dem bisherigen Prinzip des "lokalen Betriebssystems" hin zu einem Dienst ("Windows as a Service"), welcher neben den bisherigen Betriebssystemfunktionalitäten auch darüber hinausgehende, insbesondere cloudbasierte, Anwendungen enthält und deswegen auf eine enge Anbindung an die Server-Infrastruktur des Herstellers angewiesen ist. Der tief verankerte und teilweise nicht beeinflussbare Datenaustausch zwischen Client und Herstellerinfrastruktur sowie die zunehmende Auslagerung von sicherheitskritischen Kernbestandteilen einer Windows-Infrastruktur in die Cloud, wie z. B. Authentifizierung, sind dabei wichtige und vor einem Einsatz unbedingt zu bewertende neue Aspekte im Vergleich zu den bisherigen Windows-Versionen.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist der Schutz von Informationen, die durch und auf Windows 10-Clients verarbeiten werden.

### 1.3 Abgrenzung

Aufbauend auf dem Baustein SYS.2.1 Allgemeiner Client, enthält dieser Baustein spezifische Anforderungen, die zum sicheren Betrieb von Clients unter dem Betriebssystem Windows 10 zusätzlich zu den Anforderungen aus dem Baustein SYS.2.1 Allgemeiner Client zu beachten und zu erfüllen sind. Die enthaltenen Anforderungen sind daher auch immer in Verbindung mit den Anforderungen aus dem "Allgemeinen Client" zu betrachten. Ein Schutz gegen fortgeschrittene und andauernde Bedrohungen muss durch die Erfüllung zusätzlicher Anforderungen der unterschiedlichen Schichten des modernisierten IT-Grundschutzes realisiert werden. 

2 Gefährdungslage
-----------------

Die folgenden spezifischen Bedrohungen und Schwachstellen sind für die betrachteten Clients auf Basis von Windows 10 von besonderer Bedeutung:

### 2 1 Schadprogramme unter Windows 10

Aufgrund der hohen Verbreitung von Windows-Betriebssystemen und der zwischen den Systemgenerationen oftmals vorhandenen Abwärtskompatibilität zu älteren Versionen ist die Gefährdung durch Schadprogramme und unbefugtes Eindringen in das IT-System vergleichsweise hoch. Schadprogramme können eine Vielzahl von Funktionen besitzen und einem Angreifer umfangreiche Steuerungsmöglichkeiten ermöglichen. Unter anderem können Schadprogramme gezielt Passwörter ausforschen, Systeme fernsteuern, Schutzsoftware deaktivieren und Daten ausspionieren. Als Schaden ist hier insbesondere der Verlust oder die Verfälschung von Informationen oder Anwendungen von größter Tragweite. Aber auch ein Imageverlust und finanzieller Schaden, der folglich durch Schadprogramme entstehen kann, ist von großer Bedeutung. Windows ist aufgrund seiner großen Verbreitung ein primäres Ziel für den Angriff mit Schadprogrammen, sodass hier eine große Bedrohung durch zahlreiche Angreifer und Angriffsarten besteht.

### 2 2 Software-Schwachstellen in Windows 10

Windows 10 ist inklusive seiner zahlreichen mitgelieferten Anwendungen ein sehr komplexes Software-Produkt. Werden Software-Fehler darin nicht rechtzeitig erkannt, können die bei der Anwendung entstehenden Abstürze oder Fehler zu weitreichenden Folgen führen (z. B. falsche Berechnungsergebnisse, Fehlentscheidungen der Leitungsebene und Verzögerungen beim Ablauf der Geschäftsprozesse). Durch Software-Schwachstellen oder -Fehler kann es zu schwerwiegenden Sicherheitslücken in einzelnen Anwendungen, dem gesamten IT-System oder sogar allen damit vernetzten IT-Systemen kommen. Sicherheitslücken in Windows können unter Umständen von Angreifern ausgenutzt werden, um Schadsoftware einzuschleusen, unerlaubt Daten auszulesen oder Manipulationen vorzunehmen.

### 2 3 Integrierte Cloud-Funktionalitäten

Windows 10 bringt zahlreiche Funktionen mit, mit denen Daten unter Nutzung der Dienste von Microsoft abgelegt und synchronisiert werden ("Cloud-Dienste"). Dadurch besteht die Gefahr, diese unbewusst (oder zumindest unbedacht) auch für möglicherweise sensible oder personenbezogene Daten zu nutzen. Gleichzeitig können sich Verstöße gegen die Datenschutzgesetze ergeben, wenn Daten bei Dritten, in der Regel im Ausland, gespeichert werden. Meldet sich ein Benutzer mit bereits aktiviertem Microsoft-Account an ein neues Gerät an, werden automatisch die von ihm genutzten Microsoft-Cloud-Dienste eingerichtet. So können Daten der Institution ungewollt auf die privaten Geräte der Mitarbeiter synchronisiert werden. Als weiteres Beispiel bietet Windows 10 als Standardeinstellung die Möglichkeit, den Bitlocker-Recovery-Schlüssel direkt über den Microsoft-Account in der Cloud zu sichern und somit kritische kryptographische Geheimnisse in die Hände Dritter zu übergeben.

### 2 4 Beeinträchtigung von Software-Funktionen durch Kompatibilitätsprobleme

Software, die auf Vorgängerversionen eines Betriebssystems erfolgreich betrieben werden konnte, muss nicht auch grundsätzlich mit der aktuellen Version von Windows 10 zusammenarbeiten. Mögliche Ursachen sind neue Sicherheitsmerkmale oder Betriebssystemeigenschaften, sowie der Wegfall von Funktionalitäten oder Diensten. In der Folge kann die Software nicht oder nur mit Einschränkungen verwendet werden. Beispiele für aktivierte Sicherheitsmerkmale, die bei neuen Windows-Versionen Ursache möglicher Kompatibilitätsprobleme sein können, sind die Benutzerkontensteuerung (UAC), oder bei 64-Bit-Versionen des Betriebssystems Kernel Patch Guard sowie die Notwendigkeit signierter Treiber, die möglicherweise für ältere Geräte nicht mehr zur Verfügung stehen.

### 2 5 Fehlerhafte Administration oder Nutzung von Windows 10

Windows 10 ist ein komplexes Betriebssystem, dessen Sicherheit im Wesentlichen durch ihre Konfiguration bestimmt wird. Dadurch ergeben sich insbesondere durch Fehlkonfiguration einzelner oder mehrerer Komponenten Beeinträchtigungen der Sicherheit für den Client selbst sowie für die genutzte Infrastruktur. Grundsätzlich beinhaltet jede Schnittstelle an einem IT-System nicht nur die Möglichkeit, darüber bestimmte Dienste des IT-Systems berechtigt zu nutzen, sondern auch das Risiko, dass darüber unbefugt auf das IT-System zugegriffen wird. Wenn etwa durch Fehlkonfiguration der Windows-eigenen Authentisierungsmechanismen Benutzerkennungen und zugehörige Passworte ausgespäht werden können, ist eine unberechtigte Nutzung der damit geschützten Anwendungen oder IT-Systeme möglich.

Auch eine fehlerhafte oder nicht ordnungsgemäße Nutzung von Geräten, Systemen und Anwendungen kann die Sicherheit unter Windows beeinträchtigen, vor allem, wenn vorhandene Sicherheitsmaßnahmen missachtet oder umgangen oder bewusst abgeschaltet werden. Zu großzügig vergebene Rechte, leicht zu erratende Passwörter, nicht ausreichend geschützte Datenträger mit Sicherungskopien oder bei vorübergehender Abwesenheit nicht gesperrte Arbeitsplätze können zu Sicherheitsvorfällen führen. Eine weitere Folge der fehlerhaften Bedienung von Windows-Systemen oder Anwendungen kann das versehentliche Löschen oder Verändern von Daten sein. Dabei ist es ebenfalls möglich, dass vertrauliche Informationen an die Öffentlichkeit gelangen, wenn beispielsweise Zugriffsrechte falsch gesetzt werden.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Windows 10 aufgeführt. Grundsätzlich ist *der IT-Betrieb* für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese werden in den entsprechenden Anforderungen gesondert erwähnt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.2.2.3.A1 Planung des Einsatzes von Cloud-Diensten

Windows 10-basierte Geräte sind eng mit den Cloud-Diensten des Herstellers Microsoft verzahnt. Es MUSS daher vor der Verwendung von Windows 10-basierten Geräten eine strategische Festlegung erfolgen, welche enthaltenen Cloud-Services in welchem Umfang genutzt werden sollen bzw. dürfen.

#### SYS.2.2.3.A2 Geeignete Auswahl einer Windows 10-Version und Beschaffung

Der Funktionsumfang und die Versorgung mit funktionalen Änderungen einer Windows 10-Version MUSS unter Berücksichtigung des ermittelten Schutzbedürfnisses und des Einsatzzwecks ausgewählt und die Umsetzbarkeit der erforderlichen Absicherungsmaßnahmen geprüft werden. Basierend auf dem Ergebnis der Überprüfung MUSS der etablierte Beschaffungsprozess um die Auswahl des entsprechenden Lizenzmodells und Releasepfades (CB, CBB oder LTSB) erweitert werden.

#### SYS.2.2.3.A3 Geeignetes Patch- und Änderungsmanagement

Um alle Änderungen erfassen und bewerten zu können, MÜSSEN alle Windows 10 Systeme einem Patch- und Änderungsmanagement unterstellt sein. Für komplexe Patches oder Änderungen MÜSSEN in einem Umsetzungsplan Tests, Kontroll- und Abbruchpunkte sowie Prioritäten für die Verteilung definiert sein. Nach einem funktionalen Update des Betriebssystems MUSS überprüft werden, ob alle Anforderungen aus dem IT-Grundschutz und den internen Vorgaben weiterhin erfüllt werden.

#### SYS.2.2.3.A4 Telemetrie und Datenschutzeinstellungen

Die Telemetriedienste, also die Diagnose- und Nutzungsdaten, die Microsoft zur Identifizierung und Lösung von Problemen, zur Verbesserung der Dienste und Produkte und zur Personalisierung des Systems mit eindeutigen Identifizierungsmerkmalen verknüpft in die U SA überträgt, können im Betriebssystem nicht vollständig abgeschaltet werden. Es MUSS daher durch geeignete Maßnahmen, etwa auf Netzebene, sichergestellt werden, dass diese Daten nicht an Microsoft übertragen werden.

#### SYS.2.2.3.A5 Schutz vor Schadsoftware

Sofern nicht gleich- oder höherwertige andere mitigierende Maßnahmen zum Schutz des IT-Systems vor einer Infektion mit Schadsoftware getroffen wurden, MUSS der Einsatz einer spezialisierten Komponente zum Schutz vor Schadsoftware auf Windows 10-Clients umgesetzt sein.

#### SYS.2.2.3.A6 Integration von Online-Konten in das Betriebssystem [Benutzer]

Die Anmeldung am System und der Domäne DARF NUR mit dem Konto eines selbst betriebenen Verzeichnisdienstes möglich sein. Anmeldungen mit lokalen Konten SOLLTEN Administratoren vorbehalten sein. Online-Konten zur Anmeldung, etwa ein Microsoft-Konto oder Konten anderer Anbieter von Identitätsmanagementsystemen, DÜRFEN NICHT verwendet werden, da hier personenbezogene Daten an die Systeme des Herstellers übertragen werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Clients unter Windows 10. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.2.2.3.A7 Lokale Sicherheitsrichtlinien

Alle sicherheitsrelevanten Einstellungen SOLLTEN bedarfsgerecht konfiguriert, getestet und regelmäßig überprüft werden. Die Sicherheitsrichtlinien SOLLTEN gemäß den Empfehlungen des Betriebssystemherstellers und dem voreingestellten Standardverhalten konfiguriert werden, sofern das Standardverhalten nicht anderen Anforderungen aus dem IT-Grundschutz oder der Organisation widerspricht. Abweichungen MÜSSEN dokumentiert und begründet werden. Alle nicht benötigten Anwendungen und Komponenten SOLLTEN deaktiviert werden. Sicherheitsrichtlinien SOLLTEN in jedem Fall gesetzt werden, auch dann, wenn die Einstellung nicht vom Standardverhalten einer nicht gesetzten Sicherheitsrichtlinie abweicht. 

#### SYS.2.2.3.A8 Zentrale Verwaltung der Sicherheitsrichtlinien von Clients

Alle Einstellungen des Windows 10 Clients SOLLTEN durch ein zentrales Management verwaltet und entsprechend dem ermittelten Schutzbedarf basierend auf den internen Richtlinien konfiguriert sein. Technisch nicht umsetzbare Konfigurationsparameter SOLLTEN dokumentiert, begründet und mit dem Sicherheitsmanagement abgestimmt werden.

#### SYS.2.2.3.A9 Sichere zentrale Authentisierung der Windows-Clients

Für die zentrale Authentisierung SOLLTE ausschließlich Kerberos eingesetzt werden. Eine Gruppenrichtlinie SOLLTE die Verwendung älterer Protokolle verhindern. Ist dies nicht möglich, MUSS alternativ NTLMv2 eingesetzt werden. Die Authentisierung mittels LAN Manager und NTLMv1 DARF innerhalb der Institution und in einer produktiven Betriebsumgebung NICHT erlaubt werden. Die eingesetzten kryptografischen Mechanismen SOLLTEN entsprechend dem ermittelten Schutzbedarf und basierend auf den internen Richtlinien konfiguriert, dokumentiert und abweichende Einstellungen begründet und mit dem Sicherheitsmanagement abgestimmt sein.

#### SYS.2.2.3.A10 Konfiguration zum Schutz von Anwendungen in Windows 10

Die Datenausführungsverhinderung für alle Programme und Dienste (Opt-Out Modus) SOLLTE aktiviert werden. 

#### SYS.2.2.3.A11 Schutz der Anmeldeinformationen in Windows 10

Sofern Windows 10 in der Enterprise-Version auf einem Hardware-System direkt (nativ) installiert ist, SOLLTE der Virtual Secure Mode (VSM) aktiviert werden. Zusätzlich zur Aktivierung von VSM SOLLTE Credential Guard gegen Angriffe auf die im System gespeicherten Authentisierungstoken und -hashes aktiviert werden. Ist dies nicht möglich, SOLLTE für den Betrieb des für die Verwaltung der Anmeldeinformationen zuständigen LSAS-Dienstes der geschützte Modus (PPL - Protected Process Light) aktiviert werden. Die Netzwerkanmeldung von lokalen Konten SOLLTE verboten werden.

#### SYS.2.2.3.A12 Datei- und Freigabeberechtigungen

Der Zugriff auf Dateien und Ordner auf dem lokalen System sowie auf Netzwerkfreigaben SOLLTE gemäß einem Berechtigungs- und Zugriffskonzept konfiguriert werden. Dies umfasst im speziellen auch die standardmäßig vorhandenen administrativen Freigaben auf dem System. Die Schreibrechte für Benutzer SOLLTEN auf einen definierten Bereich im Dateisystem beschränkt werden. Insbesondere SOLLTEN Benutzer keine Schreibrechte in Ordner des Betriebssystems oder von installierten Anwendungen erhalten.

#### SYS.2.2.3.A13 Einsatz der SmartScreen-Funktionen

Die SmartScreen-Funktion, die aus dem Internet heruntergeladene Dateien und Webinhalte auf mögliche Schadsoftware untersucht und dazu unter Umständen personenbezogene Daten an Microsoft überträgt, SOLLTE deaktiviert werden.

#### SYS.2.2.3.A14 Einsatz des Sprachassistenten Cortana [Benutzer]

Cortana nutzt personenbezogene Daten wie z. B. Sprachdaten, Benutzereingaben, Kalender- und Kontaktdaten, Namen von bevorzugten Orten und benutzten Anwendungen, die an Microsoft übertragen werden. Aus diesem Grund SOLLTE Cortana deaktiviert werden.

#### SYS.2.2.3.A15 Einsatz der Synchronisationsmechanismen in Windows 10

Die Synchronisierung von Nutzerdaten mit Microsoft Cloud-Diensten und das Sharing von WLAN-Passwörtern SOLLTE vollständig deaktiviert werden.

#### SYS.2.2.3.A16 Anbindung von Windows 10 an den Windows Store

Die Verwendung des Windows** **Store SOLLTE auf die Verträglichkeit mit den Datenschutz- und Sicherheitsvorgaben der Institution überprüft und bewertet werden. Die generelle Installation von Apps auf Windows 10 ist nicht an die Anbindung an den Windows Store gebunden. Daher SOLLTE diese Funktion, sofern sie nicht benötigt wird, deaktiviert werden.

#### SYS.2.2.3.A17 Verwendung der automatischen Anmeldung

Die Speicherung von Kennwörtern, Zertifikaten und anderen Anmeldeinformationen zur automatischen Anmeldung auf Webseiten und IT-Systemen SOLLTE NICHT erlaubt werden.

#### SYS.2.2.3.A18 Einsatz der Windows-Remoteunterstützung

Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTE bei der Planung der Windows-Remoteunterstützung (hiermit ist nicht RDP gemeint) berücksichtigt werden. Eine Remote-Unterstützung SOLLTE nur nach einer expliziten Einladung erfolgen. Bei der Speicherung einer Einladung in einer Datei SOLLTE diese ein Kennwort aufweisen. Der aktuell angemeldete Benutzer SOLLTE dem Aufbau einer Sitzung immer explizit zu stimmen. Die maximale Gültigkeitsdauer der Einladung für eine Unterstützung aus der Ferne SOLLTE eine angemessene Größe haben. Sofern dieser Service nicht verwendet wird, SOLLTE er vollständig deaktiviert werden.

#### SYS.2.2.3.A19 Verwendung des Fernzugriffs über RDP [Benutzer]

Die Auswirkungen auf die Konfiguration der lokalen Firewall SOLLTE bei der Planung des Fernzugriffs berücksichtigt werden. Die Gruppe der berechtigten Benutzer für den Remote-Desktopzugriff (RDP) SOLLTE durch die Zuweisung entsprechender Benutzerrechte festgelegt werden. In komplexen Infrastrukturen SOLLTE das RDP-Zielsystem nur durch ein dazwischen geschaltetes RDP-Gateway erreicht werden können. Für die Verwendung von RDP SOLLTE eine Prüfung und deren Umsetzung sicherstellen, ob die nachfolgend aufgeführten Komfortfunktionen im Einklang mit den Schutzbedarf des Zielsystems stehen:

* die Verwendung der Zwischenablage,
* die Einbindung von Druckern,
* die Einbindung von Wechselmedien und Netzlaufwerken
* die Nutzung der Dateiablagen und Smartcard-Anschlüssen
Sofern der Einsatz von Remote-Desktopzugriffen nicht vorgesehen ist, SOLLTEN diese vollständig deaktiviert werden. Die eingesetzten kryptographischen Protokolle und Algorithmen SOLLTEN den internen Vorgaben der Institution entsprechen.

#### SYS.2.2.3.A20 Einsatz der Benutzerkontensteuerung für privilegierte Konten

Die Konfigurationsparameter der Benutzerkontensteuerung (UAC) SOLLTEN für die privilegierten Konten zwischen Bedienbarkeit und Sicherheitsniveau abgewogen eingesetzt werden. Die Entscheidungen für die zu verwendenden Konfigurationsparameter SOLLTEN dokumentiert werden. Darüber hinaus SOLLTE die Dokumentation alle Konten mit Administratorrechten enthalten sowie eine regelmäßige Prüfung erfolgen, ob die Notwendigkeit zur Rechteerweiterung noch besteht.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.2.2.3.A21 Einsatz des Encrypting File Systems EFS(CI)

Da das Encrypting File System (EFS) die verwendeten Schlüssel mit dem Passwort des Benutzerkontos schützt, SOLLTE ein komplexes Passwort verwendet werden. Zusätzlich SOLLTEN restriktive Zugriffsrechte die mit EFS verschlüsselte Dateien schützen. Statt des Administrators SOLLTE ein dediziertes Konto der Wiederherstellungsagent sein. In diesem Zusammenhang SOLLTE dessen privater Schlüssel gesichert und aus dem System entfernt werden. Dabei SOLLTEN von allen privaten Schlüsseln Datensicherungen erstellt werden. Beim Einsatz von EFS mit lokalen Benutzerkonten SOLLTE die Verschlüsselung der lokalen Passwortspeicher mittels Syskey verwendet werden. Dies kann entfallen, wenn die Betriebssystemfunktion Credential Guard genutzt wird. Beim Einsatz von EFS SOLLTEN die Benutzer im korrekten Umgang mit EFS geschult werden.

#### SYS.2.2.3.A22 Windows PowerShell(CIA)

Die Ausführung der PowerShell sowie von WPS-Dateien SOLLTE nur Administratoren gestattet werden. Die PowerShell-Ausführung selbst SOLLTE zentral protokolliert und die Protokolle überwacht werden. Die Ausführung von PowerShell-Skripten SOLLTE mit dem Befehl Set-ExecutionPolicy-AllSigned eingeschränkt werden, um die versehentliche Ausführung unsignierter Skripte zu verhindern.

#### SYS.2.2.3.A23 Erweiterter Schutz der Anmeldeinformationen in Windows 10(CI)

Auf UEFI-basierten Systemen SOLLTE SecureBoot verwendet und der Status des geschützten Modus für LSASS bei Systemstart überwacht werden (vgl. hierzu SYS.2.2.3.A11 Schutz der Anmeldeinformationen in Windows 10). Ist eine Fernwartung der Client-Systeme mittels RDP vorgesehen, SOLLTE bei Einsatz von Windows 10 in einer Domäne ab dem Funktionslevel 2012 R2 von der Option "restrictedAdmin" Gebrauch gemacht werden. 

#### SYS.2.2.3.A24 Aktivierung des Last-Access-Zeitstempels(A)

Um die Analyse nach einem Systemmissbrauch zu erleichtern, SOLLTE der NTFS Last-Access-Zeitstempel aktiviert werden. Vor der Aktivierung SOLLTE geprüft werden, welche Auswirkungen die Aktivierung auf die Systemleistung hat. Die Ergebnisse der Überprüfung und die Entscheidung über die Aktivierung SOLLTEN dokumentiert werden.

#### SYS.2.2.3.A25 Umgang mit Fernzugriffsfunktionen der "Connected User Experience and Telemetry"(CI)

Die Komponente "Connected User Experience and Telemetry" (CUET) ist bei Windows 10 fester Bestandteil des Betriebssystems und stellt neben Telemetriefunktionalität auch eine Fernzugriffsmöglichkeit für den Betriebssystemhersteller auf das lokale System bereit. Ein Fernzugriff auf den Windows 10 Client durch den Betriebssystemhersteller SOLLTE netzwerkseitig geloggt und falls erforderlich geblockt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Clients unter Windows 10" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [TN408187] Configuring Additional LSA Protection

  

 Microsoft Technet, 03.2014  
 <https://technet.microsoft.com/en-us/library/dn408187.aspx>

 
* #### [TN621547] Credential Guard - Überblick

  

 Microsoft, (zuletzt abgerufen am 27.09.2017)  
 <https://docs.microsoft.com/de-de/windows/access-protection/credential-guard/credential-guard-requirements>

 
* #### [TN986865] Device Guard - Überblick

  

 Microsoft, (zuletzt abgerufen am 27.09.2017)  
 <https://technet.microsoft.com/de-de/library/dn986865.aspx>

 
* #### [WIN10E] Windows 10 Editionen vergleichen

  

 Microsoft, (zuletzt abgerufen am 27.09.2017)  
 <https://www.microsoft.com/de-de/WindowsForBusiness/Compare>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Clients unter Windows 10" von Bedeutung.

* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
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

