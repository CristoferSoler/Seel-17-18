1 Beschreibung
--------------

### 1.1 Einleitung

Mobilgeräte sind ständige Begleiter in der heutigen Informationsgesellschaft. Sie sind ständig online, das heißt, mit dem Internet oder dem internen Institutionsnetz verbunden, und bieten damit jederzeit Zugriff auf digitale Informationen. Die Geräte können über diverse Schnittstellen kommunizieren, z. B. Mobilfunk, WLAN oder Bluetooth.

Aufgrund von modernen, einfachen Bedienkonzepten sowie hoher Leistungsfähigkeit sind Smartphones und Tablets heutzutage weit verbreitet. Ursprünglich wurden diese Geräte für den privaten Gebrauch konzipiert. Heute werden sie jedoch auch im beruflichen Umfeld verwendet.

Ein oft genutztes Betriebssystem für Mobiltelefone ist Android. Seit Version 4 wurde Android schrittweise für den Unternehmenseinsatz ausgebaut. So wurden z. B. Funktionen integriert, die es Institutionen erleichtern, Android-Geräte zu verwalten. Auch steigt die Zahl der von Android unterstützten Richtlinien mit jeder Version und es gibt herstellerspezifische Erweiterungen, die zusätzliche Richtlinien erlauben.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, über typische Gefährdungen für Android-basierte Geräte zu informieren sowie aufzuzeigen, wie Android-Geräte sicher in Institutionen eingesetzt werden können. Auf Basis der im Baustein aufgeführten Anforderungen können zudem Sicherheitsrichtlinien erstellt werden. 

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die beim Betrieb von Android-basierten Geräten zu beachten und zu erfüllen sind. Allgemeine und übergreifende Anforderungen an den Betrieb von Smartphones und Tablets werden nicht in diesem Baustein, sondern in SYS.3.2.1 *Smartphone und Tablet* behandelt. Ebenfalls nicht Bestandteil dieses Bausteins sind die Anforderungen an die zentrale Administration von Android-Geräten, diese sind im Baustein SYS 3.2.3 *MDM* aufgeführt. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Android von besonderer Bedeutung:

### 2 1 Rooten des Gerätes

Viele der bisherigen Versionen von Android enthielten Schwachstellen, die es ermöglichten, das vom Hersteller etablierte Sicherheitskonzept außer Kraft zu setzen. Frei erhältliche Werkzeuge nutzen diese Schwachstellen aus, um anderen Apps Superuser-Rechte (root) erteilen zu können.

Diese Apps können dann auf die Daten des Betriebssystems und die anderer Apps zugreifen. Auch benutzen Schadprogramme diese Schwachstellen, um sich auf dem Gerät zu installieren oder es zu manipulieren. Hierdurch kann das Betriebssystem anders als vorgesehen genutzt und wichtige Sicherheitsfunktionen übergangen werden.

Besonders Zugangsdaten, die Android in geschützten Bereichen lagert, sind betroffen, da eine App mit Superuser-Rechten diese unter Umständen auslesen kann und somit auf die dort abgelegten Informationen zugreifen kann.

### 2 2 Schadsoftware für das Android-Betriebssystem

Aufgrund der Verbreitung und der offenen Architektur sind Geräte mit Android-Betriebssystem ein beliebtes Ziel für Schadsoftware. Da es bei Android relativ einfach möglich ist, Apps nicht nur aus dem Play Store von Google, sondern auch aus alternativen Stores oder per direktem Download zu installieren, verbreiten sich Schadprogramme oft über diesem Weg. Ein Angreifer könnte so eine beliebte Software mit einer Schadsoftware infizieren und anschließend wieder zum Download zur Verfügung stellen.

### 2 3 Fehlende Updates für das Android-Betriebssystem

Viele Hersteller liefern Smartphone und Tablets mit veralteten Versionen von Android aus oder stellen keine regelmäßigen oder sogar überhaupt keine Updates zur Verfügung. Da regelmäßig Schwachstellen in Android entdeckt werden, sind solche Endgeräte besonders gefährdet. Diese Problematik betrifft vor allem günstige Geräte und kleinere Hersteller, aber auch große Hersteller und Premium-Modelle bieten oftmals keine ausreichende Versorgung mit Sicherheitsupdates über einen längeren Zeitraum.

### 2 4 Risikokonzentration durch ein Benutzerkonto (Google-ID) für alle Google-Dienste

Mit der Google-ID können Benutzer zentral auf alle Google-Dienste zugreifen, z. B. auf die Geräteverwaltung, die aufgezeichneten geographische Positionen, Chatsoftware, Cloud-Speicher, den Play Store, Musik-, Buch- und Filmangebote, Datensicherung, Bookmarks, Password-Speicher für Webseiten und Synchronisationsdienste. Auch viele andere Anbieter von Diensten im Internet verwenden die Google-ID, um Benutzer zu authentisieren. 

Kann sich ein Angreifer über die Google-ID authentisieren, kann er alle diese Dienste unter der gestohlenen Identität benutzen. Auch kann er auf alle dort gespeicherten Daten zugreifen und Geräte aus der Ferne lokalisieren oder sie zurücksetzen, also alle Daten auf dem Gerät löschen.

### 2 5 Integration für vorinstallierte Apps und deren Funktionalitäten bei Android-basierten Geräten

Mit dem Betriebssystem liefern die Hersteller oft bereits tief integrierte und vorinstallierte Apps (z. B. Play Store und die zugehörigen Play Services) sowie Schnittstellen zu Diensten von Drittanbietern (Twitter, Facebook, usw.) aus. Diese Apps kann der Anwender teilweise nicht entfernen. Damit vergrößert sich die Angriffsfläche des Android-Betriebssystems. Auch die nicht löschbaren bzw. nicht konfigurierbaren Schnittstellen sind oft in Institutionen nicht erwünscht.

Insgesamt steigt durch die tiefe Integration von Apps und Schnittstellen von Drittanbietern das Risiko, dass das Gerät mit Schadsoftware infiziert wird oder ein Angreifer unberechtigt darauf zugreifen kann. Der Schutz der Daten auf dem Gerät nimmt dadurch ab.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Android aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.3.2.4.A1 Auswahl von Endgeräten mit Android

Bei der Auswahl eines Endgeräts mit Android MUSS sichergestellt sein, dass der Hersteller regelmäßig Sicherheitsupdates für dieses Gerät bereitstellt. Das Endgerät MUSS mit einer aktuellen Version von Android ausgeliefert werden oder unmittelbar auf diese aktualisiert werden können.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Android. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.3.2.4.A2 Deaktivieren der Entwickler-Optionen

In allen Android-basierten Geräten SOLLTEN die Entwickleroptionen deaktiviert sein.

#### SYS.3.2.4.A3 Einsatz des Multi-User- und Gäste-Modus

Es SOLLTE geregelt sein, ob der Multi-User- und Gäste-Modus verwendet werden darf oder eventuell auch muss. Ein Benutzer auf dem Android-basierten Gerät SOLLTE einer natürlichen Person entsprechen.

#### SYS.3.2.4.A4 Regelung und Konfiguration von Cloud-Print

Cloud-Print SOLLTE nur dann erlaubt sein, wenn sichergestellt ist, dass der Benutzer nur genehmigte Drucker auswählen kann.

#### SYS.3.2.4.A5 Erweiterte Sicherheitseinstellungen

Es SOLLTEN nur die freigegebenen Sicherheits-Apps sich als Geräteadministrator oder "Trust Agents" eintragen. Das Sicherheitsmanagement SOLLTE das regelmäßig überprüfen.

Weiterhin SOLLTEN es die Einstellungen für "Zugriff auf Nutzungsdaten und Zugriff auf Benachrichtigungen" nur erlaubten Apps ermöglichen, auf diese schützenswerten Daten zuzugreifen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.2.4.A6 Einsatz eines Produkts zum Schutz vor Schadsoftware(CIA)

Es SOLLTE auf Android-basierten Geräten eine Software zum Schutz vor Schadsoftware installiert sein. Die Software SOLLTE immer aktuell sein. Es SOLLTE eine Software eingesetzt werden, die in unabhängigen Tests als sehr gut bewertet worde.

#### SYS.3.2.4.A7 Zusätzliche Firewall(CI)

Auf Android-basierten Geräten SOLLTE eine Firewall installiert und aktiviert sein.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Android" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [AN2] Two-factor Authentifizierung

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://www.google.com/landing/2step/>

 
* #### [ANH] Android Hilfe

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://support.google.com/android/?hl=de>

 
* #### [ANL] Übersicht Android-basierte Geräte

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://www.android.com>

 
* #### [ANS] Netzwerke und Sicherheit

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://www.android.com/security/overview>

 
* #### [ANU] App Updates

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://support.google.com/googleplay/answer/113412?hl=de>

 
* #### [GAGB] Google AGB

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://www.google.com/policies/terms/>

 
* #### [GPP] Goggle Pirvacy Policy

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://www.google.com/policies/privacy/>

 
* #### [GSUITE] G Suite für Unternehmen und Bildungseinrichtungen

  

 Google, (zuletzt abgerufen am 27.09.2017)  
 <https://gsuite.google.com>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Android" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.21 Manipulation von Hard- oder Software
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.41 Sabotage
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

