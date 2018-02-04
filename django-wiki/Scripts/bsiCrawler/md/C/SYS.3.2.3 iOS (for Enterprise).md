1 Beschreibung
--------------

### 1.1 Einleitung

Mobilgeräte sind ständige Begleiter in der heutigen Informationsgesellschaft. Sie sind ständig online, das heißt mit dem Internet oder dem internen Institutionsnetz verbunden, und bieten damit jederzeit Zugriff auf digitale Informationen. Die Kommunikation geschieht über diverse Schnittstellen, Beispiele sind GSM/UMTS/LTE, WLAN, Bluetooth.

Aufgrund von modernen, einfachen Bedienkonzepten sowie hoher Leistungsfähigkeit sind Smartphones und Tablets heutzutage weit verbreitet. Dazu zählen auch die von der Firma Apple produzierten Mobilgeräte iPhone und iPad mit dem Betriebssystem iOS. Ursprünglich wurden diese Geräte für den privaten Gebrauch konzipiert. Durch die Umgestaltung der Infrastrukturen und der Art der Informationserhebung und Verarbeitung finden sie jedoch immer häufiger auch Verwendung im beruflichen Umfeld und lösen teilweise sogar Notebooks ab.

Durch die Integration von Business-Funktionen wurde iOS seit der Version 4 schrittweise für den Einsatz in Unternehmen und Behörden ausgebaut und Funktionen für die Verwaltung aus Sicht einer Institution integriert. Hierzu gehören unter anderem Apples Programm zur zentralisierten Geräteregistrierung sowie Optionen wie Single Sign-on (SSO).

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, aufzuzeigen, wie mit iOS (for Enterprise) betriebene Geräte sicher in Institutionen eingesetzt werden können. Dazu werden Anforderungen für Einstellungen der iOS-basierten Endgeräte aufgestellt, die in Form von Konfigurationsprofilen auf den Endgeräten verteilt werden können. iOS-Konfigurationsprofile enthalten einheitlich definierte Einstellun­gen z. B. für Sicherheitsrichtlinien oder einzelne Systemaspekte, um iOS-basierte Geräte einheit­lich und zentral zu verwalten und automatisch zu konfigurieren.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die beim Betrieb von iOS-basierten Geräten, die in die Prozesse der Institution integriert sind, zu beachten und zu erfüllen sind. Anforderungen an die Integration in die Sicherheits- oder Kollaborations-Infrastruktur der Institution sind nicht im Fokus dieses Bausteins. Mit einem sogenannten „Mobile Device Management“ (MDM) besteht die Möglichkeit, die Geräte zentral zu verwalten und Konfigurationsprofile pro Benutzergruppe oder Einsatzzweck auszurollen. Über ein MDM lassen sich auch Sicherungsmaßnahmen einheitlich durchsetzen. Es wird vorausgesetzt, dass die iOS-basierten Geräte in ein solches MDM eingebunden sind. Anforderungen für den Betrieb solcher MDMs finden sich im Baustein SYS.3.2.2 MDM. Für kleinere Umgebungen kann auch der Apple Configurator verwendet werden, um die in diesem Baustein aufgeführten Anforderungen auf mehrere Endgeräte auszurollen. Allgemeine und übergreifende Aspekte zum Betrieb von Smartphones und Tablets unabhängig vom darauf eingesetzten Betriebssystem finden sich im Baustein SYS.3.2.1 Smartphone/Tablet.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich iOS (Apple) von besonderer Bedeutung:

### 2 1 Fehlende oder schlechte Qualität des Gerätecodes (Passcode)

Mit der sogenannten Codesperre werden iOS-basierte Geräte gegen unbefugten Zugriff gesperrt. Wenn diese Funktion nicht aktiviert wird oder wenn ein leicht zu erratender Code verwendet und dieser dadurch umgangen werden kann, besteht die erhöhte Gefahr, dass Unbefugte auf iOS-basierte Geräte zugreifen. Zudem ist der verwendete Gerätecode ein essentieller Bestandteil für die Entropie bestimmter Verschlüsselungscodes.

### 2 2 Jailbreak

In den bisherigen Versionen des iOS-Betriebssystems wurden meist Schwachstellen gefunden, die es ermöglichen, das von der Firma Apple etablierte Sicherheitsframework zu unterlaufen und somit auf Systemprozesse und geschützte Speicherbereiche zuzugreifen. Sogenannte „Jailbreaks“ nutzen diese Schwachstellen aus, um beispielsweise alternative App-Stores oder von Apple unerwünschte Erweiterungen nutzen zu können. Jailbreak-Techniken werden von Angreifern verwendet, um Schadprogramme zu installieren oder andere schädliche Manipulationen auf dem iOS-basierten Gerät vorzunehmen.

### 2 3 Risikokonzentration durch ein Benutzerkonto (Apple ID) für alle Apple-Dienste

Mit der Apple ID besteht ein zentraler Zugang zu allen von der Firma Apple zur Verfügung gestellten Diensten (z. B. iMessage, FaceTime, iCloud, App Store, iTunes, iBook-Store, iPhone-Suche oder Synchronisationsdienste). Wenn Unbefugte Zugriff auf eine nicht ausreichend abgesicherte Apple ID erlangen, können sie unter Umständen diese Apple-Dienste unter einer falschen Identität nutzen, die Verfügbarkeit der Apple-ID-basierten Dienste stören, iOS-basierte Geräte aus der Ferne lokalisieren oder alle Daten zurücksetzen sowie auf Informationen des Cloud-Dienstes „iCloud“ zugreifen. Insbesondere ist es einem Angreifer bei aktivierten iCloud-Backups möglich, die gespeicherten Daten auf ein eigenes iOS-Gerät zu klonen.

### 2 4 Fehlende Betriebssystem-Updates bei alten Geräten

Es erscheinen regelmäßig neue Versionen des iOS-Betriebssystems und Updates. Diese werden in der Regel für die neueste Gerätegeneration und für eine Reihe von älteren Gerätegenerationen (siehe weiterführende Informationen) bereitgestellt. Allerdings werden nicht alle zurückliegenden Betriebssystem-Versionen im gleichen Umfang mit Updates und Sicherheitsupdates versorgt. Nachträglich bekannt gewordene Schwachstellen im Betriebssystem einer bereits abgekündigten Gerätegeneration werden nicht mehr durch Updates geschlossen.

### 2 5 Software-Schwachstellen in Apps

Apps für iOS können Schwachstellen enthalten, die für lokale Angriffe oder für Angriffe über Netzverbindungen ausgenutzt werden können. Außerdem werden viele Apps von Drittentwicklern nach einiger Zeit nicht mehr weiter gepflegt. Dadurch besteht die Gefahr, dass erkannte Sicherheitsmängel nicht durch entsprechende Updates behoben werden.

### 2 6 Tiefere Integration für vorinstallierte Apps und deren Funktionalitäten

Mit dem Betriebssystem liefert Apple bereits tief integrierte und vorinstallierte Apps (z. B. die Apps „Mail“ und „Uhr“) sowie Schnittstellen zu Diensten von Drittanbietern (wie Twitter oder Facebook) aus. Diese Apps werden teilweise mit höheren Berechtigungen als aus dem App Store herunterladbare Apps ausgeführt, wodurch sich die Angriffsfläche des iOS-basierten Geräts vergrößert. Die Verwendung der nicht löschbaren bzw. nicht konfigurierbaren Schnittstellen ist bei dienstlicher Nutzung meist nicht erwünscht und vergrößert ebenfalls die Angriffsfläche des Geräts.

### 2 7 Missbrauch des Fingerabdrucksensors

Das Betriebssystem iOS enthält spezielle Funktionen, die durch den Fingerabdrucksensor Touch ID vereinfacht genutzt werden können. Dieses sind z. B. das vereinfachte Freischalten des Geräts oder der Einkauf bei iTunes und im App Store. Diese biometrische Sicherheitsfunktion lässt sich mit entsprechendem Aufwand durch den Nachbau eines künstlichen Fingers auf Basis eines digital gesäuberten Fingerabdrucks umgehen. Bis zu 48 Stunden nach der letzten Eingabe des gesetzten Passcodes akzeptiert das Gerät eine Freischaltung über Fingerabdruck, dies ist somit das maximale Zeitfenster für einen Missbrauch.

### 2 8 Missbrauch von Fitness- oder Ortungsdaten unter iOS

Das Betriebssystem iOS enthält spezielle Funktionen zur Verwaltung von Fitness- und Ortungsdaten. Diese Daten sind besonders sensitiv und stellen ein attraktives Angriffsziel dar, insbesondere wenn sie über einen längeren Zeitraum gesammelt und gespeichert werden.

### 2 9 Missbrauch sensitiver Daten im gesperrten Zustand

Das Betriebssystem iOS verfügt über eine Funktion, um Mitteilungen von aktivierten Widgets und Push-Nachrichten auf dem Sperrbildschirm anzeigen zu lassen. Dadurch besteht die Gefahr, dass sensitive Informationen des Benutzers ungeschützt auf dem Sperrbildschirm unberechtigten Dritten preisgegeben werden und ausgenutzt werden können. Über den Sprachassistenten Siri besteht zudem auch im gesperrten Zustand die Möglichkeit zum Zugriff auf Telefonfunktionen und Kontaktdaten. Auch dies kann dazu führen, dass unberechtigte Dritte an sensitive Informationen gelangen können.

### 2 10 Missbrauch in iOS-basierten Geräten gespeicherter Daten

Aufgrund der vielen Funktionen und der Erweiterungsmöglichkeiten enthält ein iOS-basiertes Gerät oft sensitive Daten, z. B. E-Mails, Dokumente, Kurznachrichten, Passwörter, Kreditkarteninformationen oder Gesundheitsdaten. Es besteht die Gefahr, dass diese Daten missbraucht werden, wenn Täter bei Verlust, Diebstahl oder Aussonderung an das Gerät gelangen oder sich technisch Zugriff auf die Daten verschaffen.

### 2 11 Missbräuchlicher Zugriff auf ausgelagerte Daten

Für eine Reihe iOS-spezifischer Funktionen muss die von der Firma Apple betriebene Infrastruktur verwendet werden. Bei Verwendung der Funktionalitäten iCloud-Schlüsselbund, iMessage, FaceTime, Siri, Continuity, Spotlightvorschläge sowie der iCloud zum Anlegen verschlüsselter Backups oder zum gemeinsamen Arbeiten an Dokumenten erfolgt die Synchronisierung von Daten zwischen unterschiedlichen Geräten oder Benutzern stets über die Infrastruktur der Firma Apple. Ebenfalls werden Push-Nachrichten für iOS-basierte Geräte über diese Infrastruktur weitergeleitet. Es besteht somit prinzipiell die Gefahr, dass Unbefugte auf Apple-Server zugreifen und die dort gespeicherten oder übertragenen Daten für ihre Zwecke missbrauchen.

### 2 12 Webbasierte Angriffe auf Browser

Browser, aber auch viele andere iOS-basierte Apps, können Webseiten und Webinhalte anzeigen. Dadurch können iOS-basierte Geräte von Phishing-Angriffen, Drive-by-Exploits und anderen webbasierten Angriffsformen betroffen sein.

### 2 13 Unzureichende Vorgaben zum Lizenz-Management

Das Management von Software-Lizenzen ist eine der Kernaufgaben der IT-Compliance. Somit besteht für eine Institution die Notwendigkeit zur Definition klarer Verantwortlichkeiten und Regelungen. Gerade die Thematik der Lizenzen von Apps wird jedoch häufig nicht ausreichend betrachtet. Im Rahmen der allgemeinen Compliance haben die Verantwortlichen der Institution dafür Sorge zu tragen, dass ihre Mitarbeiter keine Lizenzverstöße begehen. 

3 Anforderungen
---------------

Im Folgenden sind die spezifischen Anforderungen für iOS-basierte Systeme aufgeführt. Grundsätzlich ist der *IT-Betrieb* für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.3.2.3.A1 Strategie für die iOS-Nutzung

Dieser Baustein setzt voraus, dass zu verwaltende iOS-Geräte in eine MDM-Infrastruktur integriert sind. Eine begründete Ausnahme unter Betrachtung von wirtschaftlichen Aspekten kann die Verwaltung einer kleineren, einstelligen Anzahl von Geräten ohne Einsatz eines MDM sein. Wird ein MDM eingesetzt, so MUSS die Verwaltung der Geräte zum Zwecke der vereinfach­ten Administration und des einheitlichen Aufspielens von sicherheitstechnischen sowie sonstigen Ein­stellungen über das MDM erfolgen. Hierzu MUSS eine Strategie zur iOS-Nutzung vorliegen, in der Aspekte wie Endgeräte-Auswahl oder Backup-Strategien festgelegt werden. Es MUSS außerdem geregelt werden, ob zusätzliche Apps von Drittanbietern genutzt werden sollen.

#### SYS.3.2.3.A2 Planung des Einsatzes von Cloud-Diensten

iOS-basierte Geräte sind grundsätzlich eng mit iCloud-Diensten des Herstellers Apple verzahnt, dies betrifft grundsätzlich bereits die Aktivierung der Geräte mit einer Apple ID. Es wird keine Apple ID benötigt, wenn das Apple-Programm zur Geräteregistrierung (Device Enrollment Program, DEP) genutzt wird. Sofern auf die Nutzung der Aktivierungssperre verzichtet werden kann, wird ebenfalls keine Verknüpfung der Cloud-Dienste mit einer personalisierten Apple ID benötigt. Es MUSS daher vor der Verwendung von iOS-basierten Geräten eine strategische Festlegung erfolgen, welche Cloud-Services in welchem Umfang genutzt werden sollen bzw. dürfen.

#### SYS.3.2.3.A3 Verwendung des Gerätecodes

Mit der Aktivierung des Gerätecodes wird die Sicherheit der Daten auf dem iOS-basierten Gerät erhöht und zusätzlich basierend auf der Komplexität des Gerätecodes eine verbesserte Entropie für bestimmte Verschlüsselungscodes zur Verfügung gestellt. Basierend auf dem festgelegten Sicherheitskonzept und dem Schutzbedarf der auf dem iOS-basierten Gerät verarbeiteten bzw. gespeicherten Daten MUSS ein angemessen komplexer Gerätecode verwendet werden.

#### SYS.3.2.3.A4 Verwendung der Konfigurationsoption "Automatische Sperre"

Basierend auf dem Einsatzzweck und Schutzbedarf MUSS die Zeitspanne für die "Automatische Sperre" des Geräts auf einen möglichst niedrigen Wert eingestellt sein. Durch einen niedrigen Wert wird sichergestellt, dass keine unberechtigte Nutzung des unbeaufsichtigten Geräts möglich ist. Durch eine angemessen kurze Zeitspanne für die automatische Sperre wird der Benutzer bei der Einhaltung der Sicherheitsregelungen der Institution unterstützt, sofern das Gerät nicht durch Interaktion mit der Benutzeroberfläche im ungesperrten Zustand verweilt. Bei der Definition des Zeitraums bis zur Passcode-Abfrage MÜSSEN die Anforderungen an den Schutzbedarf und die Benutzbarkeit beachtet werden.

#### SYS.3.2.3.A5 Verwendung der Konfigurationsoption "Gerätesperrung"

Um bei einem gesperrten Gerät zu vermeiden, dass Unbefugte auf die Benutzerdateien zugreifen können, MUSS der Zeitraum bis zu einer Passcode-Abfrage definiert sein. Bei der Definition des Zeitraums bis zur Passcode-Abfrage MÜSSEN die Anforderungen an den Schutzbedarf und die Benutzbarkeit beachtet werden.

#### SYS.3.2.3.A6 Verwendung der Konfigurationsoption "Maximale Anzahl von Fehlversuchen"

Um das systematische Ausspionieren des Passcodes zu verhindern, MUSS eine dem Schutzbedarf gerechte Anzahl maximal möglicher Fehleingaben des Passcodes konfiguriert werden. Bei Überschreiten dieses festgelegten Werts MUSS eine vollständige lokale Löschroutine (Wipe) auf dem iOS-basierten Gerät automatisch initialisiert werden.

#### SYS.3.2.3.A7 Verhinderung des unautorisierten Löschens von Konfigurationsprofilen

Um eine unautorisierte Löschung von Konfigurationsprofilen zu verhindern, MÜSSEN durch die Verantwortlichen geeignete Regelungen getroffen und umgesetzt sein. Beispielsweise kann die Löschung technisch durch eine passwortgeschützte Authentisierung realisiert werden oder organisatorisch grundsätzlich verboten sein.

#### SYS.3.2.3.A8 Zeitnahe Aktualisierung des Betriebssystems

Apple stellt in unregelmäßigen Abständen neue Versionen mit integrierten Sicherheitsaktualisierungen des Betriebssystems iOS für aktuell unterstützte Geräte zur Verfügung. Bevor alle iOS-basierten Geräte der Institution auf eine neue Version aktualisiert werden, MUSS diese getestet worden sein. Ziel dieses Validierungsprozesses ist die Verifizierung der bisherigen Funktionen, Sicherheitsmechanismen und die Durchsetzbarkeit von Compliance-Anforderungen. Um aufgetretene Sicherheitslücken zu schließen, MUSS eine Aktualisierung des installierten Betriebssystems zeitnah nach Freigabe auf die Geräte ausgerollt werden. Durch eine aktive Teilnahme an Apples Beta-Programm kann in den meisten Fällen die neue Betriebssystemversion vorab getestet werden, um die Freigabe hinsichtlich der genannten Aspekte zeitnah ermöglichen zu können. Ältere Geräte, für die keine aktuellen iOS-Versionen mehr bereitgestellt werden, MÜSSEN ausgesondert und durch unterstützte Geräte ersetzt werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich iOS (for Enterprise). Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.3.2.3.A9 Verwendung eines komplexen Gerätecodes

Basierend auf dem Schutzbedürfnis SOLLTE zum Zwecke der Wahrung der Vertraulichkeit ein komplexes Passwort verwendet werden. Bei der Regelung der Komplexität (Mindestlänge des Codes, Mindestanzahl an Sonderzeichen) SOLLTE eine Balance zwischen Benutzbarkeit, Risikoakzeptanz und Schutzbedürfnis gewahrt werden. Beispielsweise können die in der Institution etablierten Regelungen für mobile Arbeitsmittel (Notebooks) die Grundlage für die umzusetzende Komplexität bilden.

#### SYS.3.2.3.A10 Verwendung des Fingerabdrucksensors

Bei iOS-basierten Geräten mit biometrischem Fingerabdrucksensor, der sogenannten Touch ID, SOLLTE dieser den Benutzern alternativ zur Entsperrung des Geräts freigegeben werden, wenn gleichzeitig organisatorisch und technisch geregelt wird, dass die Benutzer komplexere Gerätecodes verwenden müssen. Einhergehend mit der Aktivierung der Touch ID SOLLTE eine Sensibilisierung der Benutzer hinsichtlich der Fälschbarkeit von Fingerabdrücken erfolgen.

#### SYS.3.2.3.A11 Verwendung nicht personalisierter Gerätenamen

Wird ein iOS-basiertes Gerät mit iTunes oder zum Laden mit einem Notebook oder einer Workstation gekoppelt, wird automatisch der Gerätename angezeigt und ermöglicht so Rückschlüsse auf den Besitzer oder die Institution. Um zu verhindern, dass unter Umständen der Benutzer und das Gerätepasswort (Passcode) erraten werden können, SOLLTE der Gerätename keine persönlichen Namens- und Institutionsmerkmale enthalten.

#### SYS.3.2.3.A12 Verwendung institutionsbezogener Apple IDs

In den allgemeinen Geschäftsbedingungen schließt die Firma Apple die Möglichkeit der Übertragung der Apple ID an einen anderen Mitarbeiter aus. Zum Zwecke der Notfallvorsorge vor Verlust geschäftlicher Daten, die auf dem Gerät selbst oder in der iCloud gespeichert sind, und der Möglichkeit der Weiterverwendung des Geräts SOLLTE das iOS-basierte Gerät mit einer institutionsbezogenen Apple ID verwendet werden.

Als zusätzliche Vorsorgemaßnahme zur Verhinderung des Missbrauchs dienstlicher Zahlungsmittel (Kreditkarten) SOLLTE das Programm für Volumenlizenz (VPP) von Apple verwendet werden.

#### SYS.3.2.3.A13 Verwendung der Konfigurationsoption "Einschränkungen unter iOS"

Um die Vertraulichkeit und Integrität der verarbeiteten bzw. auf dem Gerät gespeicherten Daten sicherzustellen, SOLLTEN alle nicht benötigten oder erlaubten Funktionen oder Dienste deaktiviert werden. Welche zu deaktivieren sind, muss basierend auf dem Einsatzzweck und dem zugrundeliegenden Schutzbedarf für die Punkte Sperrbildschirm, Unified Communication, Siri, Hintergrundbild, Verbindung mit Host-Systemen und Diagnose- und Nutzungsdaten entschieden werden.

#### SYS.3.2.3.A14 Verwendung der iCloud-Infrastruktur

Durch die Firma Apple wird allen Benutzern mit einer Apple ID die iCloud-Infrastruktur zur Verfügung gestellt. So besteht z. B. die Möglichkeit, über die iCloud-Infrastruktur Dokumente und Fotos zu teilen, Standortinformationen der hinterlegten Freunde abzurufen oder OS X-basierte und iOS-basierte Geräte um Continuity-Funktionen zu erweitern. Bevor die umfängliche oder selektive Nutzung der iCloud-Infrastruktur freigegeben wird, SOLLTE eine Bewertung der Vereinbarkeit der allgemeinen Geschäftsbedingungen der Firma Apple mit den internen Richtlinien hinsichtlich Verfügbarkeit, Vertraulichkeit, Integrität und Datenschutz erfolgen. Wird die Nutzung der iCloud-Infrastruktur erlaubt, SOLLTE die Authentisierung am iCloud-Webservice durch eine Zwei-Faktor-Authentisierung erfolgen. Durch die Verwendung verwalteter Apps kann die iCloud-Nutzung für einen rein dienstlichen Bedarf zusätzlich auf ein geringes Maß reduziert oder komplett ausgeschlossen werden.

#### SYS.3.2.3.A15 Verwendung der Continuity-Funktionen

Wurde die Nutzung der iCloud-Infrastruktur nicht grundsätzlich durch das Sicherheitsmanagement der Institution untersagt, SOLLTE eine Bewertung der Vereinbarkeit der Continuity-Funktionen (AirDrop und Handoff) mit den internen Richtlinien unter Berücksichtigung der Aspekte Vertraulichkeit und Integrität erfolgen. Auf Basis der Bewertungsergebnisse SOLLTE geregelt werden, inwieweit technisch bzw. organisatorisch diese Funktionen eingeschränkt werden.

#### SYS.3.2.3.A16 Verwendung der Konfigurationsoption für AirPlay

Mit AirPlay wird es dem Anwender ermöglicht, an einen AirPlay-Empfänger (wie das Apple-TV) Musik, Videos, Präsentationen oder den kompletten Bildschirminhalt des Geräts zu übertragen. Um einen angemessenen Umgang mit der Funktion AirPlay sicherzustellen, SOLLTE es technische bzw. organisatorische Regelungen geben sowie die Benutzer sensibilisiert werden und im sicherheitskonformen Umgang mit AirPlay Unterstützung erhalten.

#### SYS.3.2.3.A17 Verwendung der Gerätecode-Historie

Um die Vertraulichkeit des verwendeten Passcodes zu wahren und zu schnelle Wiederholungen vom Benutzer verwendeter Passwörter zu verhindern, SOLLTE im Konfigurationsprofil die Anzahl der eindeutigen Codes bis zur ersten Wiederholung festgelegt sein. Bei der Festlegung des Wertes können beispielsweise die etablierten Regelungen innerhalb der Windows-Domäne oder ähnlichen als Grundlage dienen.

#### SYS.3.2.3.A18 Verwendung der Konfigurationsoption für den Browser Safari

Der Browser Safari ist in iOS tief integriert und besitzt gegenüber den aus dem App-Store installierten Browsern anderer Anbieter teils höhere Rechte. Die bereits in der Institution etablierten Browserrichtlinien SOLLTEN entsprechend auch für Safari durch technische und organisatorische Maßnahmen umgesetzt werden. Dabei SOLLTEN die bereits etablierten Anforderungen für Browser auf stationären und tragbaren PCs als Grundlage für die Absicherung der iOS-basierten Geräte dienen sowie die Einsatzszenarien und das Einsatzumfeld der Geräte beachtet werden. 

#### SYS.3.2.3.A19 Verwendung der Filteroption für Webseiten

Sind die Geräte nicht in eine vorhandene Proxy- und Reputations-Infrastruktur der Institution eingebunden, SOLLTE für den Browser Safari durch die Nutzung der Filteroptionen auf Basis von erlaubten URLs (diese sind eine Ergänzung der bereits durch Apple vorselektierten URL-Gruppen), Whitelist-URLs, Blacklist-URLs oder durch die Einbindung von Inhaltsfiltern Dritter die Erfüllung gesetzlicher Regelungen und interner Vorgaben erfolgen.

Wird durch die Verantwortlichen in der IT bereits ein Reputation Service oder eine Proxy-Infrastruktur angeboten, lassen sich die iOS-basierten Geräte durch die Hinterlegung eines globalen HTTP-Proxy für alle installierten Browser integrieren. Bei der Verwendung eines globalen nur intern erreichbaren HTTP-Proxies SOLLTE die Integration mittels einer VPN-Verbindung wahlweise permanent oder basierend auf den verwendeten Apps in die Infrastrukturen erfolgen.

#### SYS.3.2.3.A20 Einbindung der Geräte in die interne Infrastruktur via VPN

Um die Vertraulichkeit und Integrität der Informationen der Institution zu wahren, SOLLTEN die iOS-basierten Geräte mittels VPN in die Infrastruktur integriert werden. In Abhängigkeit von Schutzbedarf, Zweck und technischen Möglichkeiten des VPN-Servers SOLLTE eine VPN-Verbindung auf Basis der Technologien IKEv2, IPSec, L2TP, PPTP oder SSL/TLS realisiert werden. Die Authentisierung SOLLTE bevorzugt durch Einmal-Passwörter und Zertifikate statt durch den Einsatz klassischer Passwörter implementiert und betrieben werden.

#### SYS.3.2.3.A21 Freigabe von Apps und Einbindung des Apple App Stores

Wenn zusätzliche Apps von Drittanbietern eingesetzt werden (siehe SYS.3.2.3.A1), MUSS durch die Verantwortlichen der interne Software-Freigabeprozess bzgl. der Validierung und Freigabe von Anwendungen (Apps) aus dem Apple App-Store ergänzt werden. Um die institutionsinternen App-Freigabeprozesse zu unterstützen, SOLLTE das eingesetzte MDM eine Filterung auf Basis von Whitelists, Blacklists oder App-Reputationsservices ermöglichen. 

Alle freigegebenen Anwendungen SOLLTEN intern in einem Standardkatalog veröffentlicht und den Benutzern zur Verfügung gestellt werden. Als unterstützendes Mittel zur Sicherstellung, dass den autorisierten Anwendern die benötigten Apps zum benötigten Zeitpunkt ausreichend zur Verfügung stehen, kann eine Integration des Programms für Volumenlizenzen (VPP) für Unternehmen der Firma Apple in die MDM-Infrastruktur erfolgen. Ein weiterer Aspekt der Nutzung des VPP ist, dass die verwendeten Apple IDs nicht mit einem Zahlungsmittel hinterlegt sein müssen. Die Zahlungsbestätigung von Apps im App-Store DARF NICHT mit der Touch ID erfolgen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.2.3.A22 Durchsetzung von Compliance-Anforderungen(CI)

Einen Verstoß gegen die Regelungen der Institution oder sogar die Manipulation des Betriebssystems zu erkennen, ist über die Abfrage einer von Apple freigegebenen Schnittstelle nicht möglich. Diese Aufgabe SOLLTE durch die vom MDM-Anbieter bereitgestellte Lösung erfolgen. Die folgenden Aktionen sollten bei Verdacht auf Verstoß gegen Regelungen oder Manipulation des Betriebssystems ausgeführt werden. Hierzu sollten entsprechende Funktionen bereitgestellt werden:

Bei Verdacht auf einen Verstoß oder Manipulation muss ein Alarm an die verantwortlichen Administratoren und das Sicherheitsmanagement in der Institution gesandt werden.

#### SYS.3.2.3.A23 Verwendung der automatischen Konfigurationsprofillöschung(CI)

Durch die Verwendung der automatischen Konfigurationsprofillöschung SOLLTE sichergestellt werden, dass auch nicht permanent online erreichbare Geräte ohne Zutun der IT-Verantwortlichen den bisher gewährten Zugang in die interne Infrastruktur nach Ablauf eines definierten Zeitraums oder an einem bestimmten Tag verlieren, sofern der Zeitraum nicht durch Zugriff auf das interne Netz erneuert wird. Zur Sicherstellung, dass der Benutzer noch im Besitz des Geräts ist, kann diese Methodik auch präventiv verwendet werden.

#### SYS.3.2.3.A24 Verwendung standortbasierter Policies(CI)

Durch die Hinterlegung einer Geofencing-Richtlinie SOLLTE sichergestellt werden, dass Geräte mit Informationen von hohem Schutzbedarf nicht den zuvor festgelegten geographischen Bereich verlassen. Sollte der geographische Bereich verlassen werden, SOLLTE eine selektive Löschung der klassifizierten Informationen oder eine vollständige Löschung des Geräts erfolgen. Bevor eine selektive oder vollständige Löschung des Geräts erfolgt, müssen die verantwortlichen Administratoren und das Sicherheitsmanagement sowie der Benutzer eine Information, z. B. per Push-Nachricht, E-Mail oder SMS, über diesen Sachverhalt erhalten. Zum Zwecke der besseren Akzeptanz und um dem Benutzer die Möglichkeit zu geben, wieder in den zulässigen geographischen Bereich zurückzukehren, sollte die selektive oder vollständige Löschung um einen hinterlegten Zeitraum kurzzeitig verzögert erfolgen. Der Einsatz von Geofencing-Richtlinien darf nicht gegen interne und gesetzliche Anforderungen verstoßen.

#### SYS.3.2.3.A25 Verwendung der Konfigurationsoption für AirPrint(CI)

Seitens der Firma Apple wurde die AirPrint-Funktionalität fest in das Betriebssystem eingebaut. Diese Funktion lässt sich nicht grundsätzlich einschalten oder abschalten. Freigegebene AirPrint-Drucker SOLLTEN durch ein Konfigurationsprofil dem Benutzer bereitgestellt werden. Um zu vermeiden, dass Informationen auf nicht vertrauenswürdigen Druckern durch die Benutzer ausgedruckt werden können, SOLLTE sichergestellt sein, dass stets alle Kommunikationsverbindungen über die Infrastruktursysteme der Institution geführt werden.

#### SYS.3.2.3.A26 Keine Verbindung mit Host-Systemen(CI)

Um zu vermeiden, dass iOS-basierte Geräte unautorisiert mit Notebooks, PCs o. ä. verbunden werden, SOLLTEN die Benutzer iOS-basierte Geräte ausschließlich mit dem MDM verbinden können. Hierdurch wird sichergestellt, dass keine lokalen Backups mittels iTunes oder ähnlichen Programmen erstellt werden können. Zusätzlich werden hierdurch Angriffe unter Zuhilfenahme forensischer Mittel stark erschwert oder komplett verhindert.

#### SYS.3.2.3.A27 Verwendung der Konfigurationsoption für APN

Bei Verwendung eines institutionsbezogenen Zugangspunkts zum Mobilfunknetz (APN, Access Point Name) bildet dieser die Grundlage zur Eingrenzung des erlaubten Geräte-Pools. Alle Geräte, die diesen APN verwenden, erhalten vom Mobilfunk-Provider einen mit der Institution abgestimmten IP-Adressenbereich. Zur Vermeidung von Sicherheitsvorfällen, die durch zu kurze Passwörter für die Authentisierung verursacht werden, SOLLTE ein komplexes Passwort mit maximal 64 Stellen mit dem Mobilfunk-Provider vereinbart werden. Beim Einsatz eines institutionsbezogenen APN SOLLTE die Authentisierung auf Basis des Protokolls CHAP realisiert sein.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "iOS (for Enterprise)" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ACSIOS] Allianz für Cybersicherheit: Empfehlung zu iOS - BSI-CS 074

  

 BSI, Version 1.20, 12.2015  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_074.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_074.pdf)

 
* #### [AppAGB] AGB für iTunes

  

 Apple (zuletzt abgerufen am 27.09.2017)  
 <https://www.apple.com/legal/internet-services/itunes/de/terms.htm>l

 
* #### [AppAGBCl] Apple AGB iCloud

  

 Apple (zuletzt abgerufen am 27.09.2017)  
 <https://www.apple.com/legal/internet-services/icloud/de/terms.html>

 
* #### [AppAGBGC] AGB für Game-Center

  

 Apple (zuletzt abgerufen am 27.09.2017)  
 <https://www.apple.com/legal/internet-services/itunes/gamecenter/de/terms.html>

 
* #### [AppCon] Appel Configuration

  

 Apple, (zuletzt abgerufen am 27.09.2017)  
 <https://support.apple.com/de-de/apple-configurator>

 
* #### [AppDS] Apple Datenschutzrichtlinie

  

 Apple (zuletzt abgerufen am 27.09.2017)  
 <https://www.apple.com/legal/privacy/de-ww/>

 
* #### [AppLPG] Apple ''Legal Process Guidelines''

  

 Apple, 06.2017  
 <https://images.apple.com/legal/privacy/law-enforcement-guidelines-outside-us.pdf>

 
* #### [AppSiup] Apple Sicherheitsupdates

  

 Apple (zuletzt abgerufen am 27.09.2017)  
 <https://support.apple.com/de-de/HT201222>

 
* #### [AppViPro] Abgekündigte und Vintage-Produkte

  

 Apple, (zuletzt abgerufen am 27.09.2017)  
 <https://support.apple.com/de-de/HT201624>

 
* #### [DEP] Programm zur Geräteregistrierung

  

 Apple, (zuletzt abgerufen am 27.09.2017)  
 <https://www.support.apple.com/de-de/HT6578>

 
* #### [Support] Support für Unternehmen und Bildungseinrichtungen

  

 Apple, (zuletzt abgerufen am 27.09.2017)  
 <https://www.apple.com/de/support/business-education/>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
* #### [VPP] Programm für Volumenlizenz

  

 Apple, (zuletzt abgerufen am 27.09.2017)  
 <https://vpp.itunes.apple.com/de/store>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "iOS (for Enterprise)" von Bedeutung.

* G 0.9 Ausfall oder Störung von Kommunikationsnetzen
* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
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
* G 0.32 Missbrauch von Berechtigungen
* G 0.35 Nötigung, Erpressung oder Korruption
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.41 Sabotage
* G 0.42 Social Engineering
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

