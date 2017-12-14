1 Beschreibung
--------------

### 1.1 Einleitung

Smartphones, Tablets und Phablets sind für viele Mitarbeiter ein nicht mehr wegzudenkender Teil ihrer Arbeit. Die IT-Abteilungen müssen jedoch immer mehr solcher Geräte in vielen unterschiedlichen Ausführungen bereitstellen und dabei gleichzeitig für eine angemessene Sicherheit sorgen. Hinzu kommt, dass mobile Endgeräte (Mobile Devices) besonderen Gefahren ausgesetzt sind und die Administration sich in grundlegenden Punkten von anderen IT-Systemen unterscheidet. 

Deswegen ist ein Mobile Device Management (MDM) besonders in Institutionen mit einer größeren Anzahl von Smartphones, Tablets und Phablets unabdingbar für einen geregelten und sicheren Betrieb dieser Geräte. Mit einer solchen Software können die Endgeräte zentral verwaltet werden, es lassen sich Sicherheitsregeln durchsetzen und es können Notfallaktionen ausgelöst werden. Ein MDM gewährleistet somit auf allen Geräten einen gleichen oder zumindest vergleichbaren Sicherheitsstandard.

### 1.2 Zielsetzung

Der Baustein zeigt auf, wie mit einem MDM mobile Endgeräte sicher von Institutionen genutzt und wie das MDM selber sicher betrieben werden kann.

### 1.3 Abgrenzung

Mobile Endgeräte (Mobile Devices) im Sinne dieses Bausteins sind Smartphones, Tablets und Phablets, auf denen mobile Betriebssysteme wie Android, iOS, Windows Phone sowie BlackBerry OS installiert sind. Die Sicherheitsanforderungen von Notebooks und Tablets mit Desktop-Betriebssystemen werden in anderen Bausteinen beschrieben. Auch geht dieser Baustein nicht darauf ein, wie die Smartphones, Tablets und Phablets verschiedener Hersteller spezifisch abgesichert werden, da dies detailliert in den Bausteinen für die jeweiligen Betriebssysteme beschrieben wird, z. B. SYS.3.2.3 *iOS (for Enterprise)* oder SYS.3.2.4 *Android.*

2 Gefährdungslage
-----------------

Die folgenden spezifischen Bedrohungen und Schwachstellen sind im Bereich Mobile Device Management (MDM) von besonderer Bedeutung.

### 2 1 Verlust des Endgeräts

Da mobile Endgeräte oft klein sind und ständig transportiert werden, werden sie leicht vergessen, gehen verloren oder werden gestohlen. Neben dem wirtschaftlichen Schaden wiegt der Verlust der Vertraulichkeit und Integrität der enthaltenen Daten besonders schwer. Es besteht zudem die Gefahr, dass Angreifer über ein entwendetes mobiles Endgerät auf interne IT-Ressourcen der Institution zugreifen können.

### 2 2 Gefahr durch Schadsoftware

Wie jedes mit dem Internet verbundene Gerät sind auch mobile Endgeräte von Schadsoftware bedroht. Das Infektionsrisiko ist verglichen mit PC-Betriebssystemen derzeit noch geringer, jedoch konzentrieren sich Cyberkriminelle immer mehr auf diese Geräte. Wird ein Gerät infiziert, können Angreifer beispielsweise Daten auslesen, verändern oder löschen oder Zugriff auf interne IT-Ressourcen der Institution erlangen.

### 2 3 Gefahren durch private Nutzung mobiler Endgeräte

Wenn Mitarbeiter firmeneigene Smartphones, Tablets und Phablets ausgehändigt bekommen, besteht immer die Gefahr, dass sie die Geräte auch unerlaubt privat benutzen. Dadurch entstehen gleich mehrere Probleme für die Informationssicherheit der Institution. So könnten sich Benutzer selbstständig Apps installieren, die Schadfunktionen enthalten, oder Webseiten besuchen, die das Gerät mit Malware infizieren können. Ebenso können vom Benutzer privat installierte Apps ein Risiko für die auf dem Gerät gespeicherten Informationen der Institution sein, wenn sie z. B. direkt auf Kontakte, Kalender, E-Mails oder Dokumente zugreifen können. So können Daten abfließen oder umgekehrt unkontrolliert in die Institution gelangen. Bekannte Beispiele sind dafür sind Social-Media- und Instant-Messaging-Apps.

### 2 4 Nicht ausreichende Synchronisation mit dem MDM

Damit das MDM die von den Verantwortlichen definierten Regelungen auf den mobilen Endgeräten durchsetzen kann, müssen die Geräte regelmäßig mit dem MDM synchronisiert werden. Wenn ein Gerät über einen längeren Zeitraum nicht mit dem MDM verbunden ist, können beispielsweise neue oder aktualisierte Regelungen nicht aufgespielt werden. Auch können, wenn zu einem verlorenen Gerät keine Verbindung besteht, die Daten nicht mehr aus der Ferne gelöscht werden.

### 2 5 Fehlerhafte Administration des MDM

MDM-Lösungen sind komplexe Anwendungen mit typischerweise mehreren Hundert unterschiedlichen Regeln. Nicht alle Regeln sind dabei miteinander kombinierbar und umgekehrt hängen viele Regeln voneinander ab. Durch Fehler bei der Administration können die Endgeräte diversen Gefahren ausgesetzt sein, die sich direkt oder indirekt auf die Vertraulichkeit, Verfügbarkeit oder Integrität der Daten und Anwendungen auswirken.

### 2 6 Ungeeignetes Rechtemanagement im MDM

Das Rechtemanagement des MDM entscheidet, wer welche Einstellungen vornehmen und wer auf welche Daten zugreifen darf. Wenn einem Mitarbeiter eine falsche Rolle zugeordnet wird, besteht die Gefahr, dass ihm zu hohe Rechte eingeräumt werden. So könnte er beispielsweise Daten unbefugt einsehen oder Einstellungen am Gerät verändern. Auch wäre es möglich, dass er Apps installiert und benutzt, die in der Institution nicht zugelassen sind, beispielsweise zur Nutzung von Cloud-Speicherdiensten. Dadurch können schützenswerte Daten aus der Institution abfließen, oder es wird gegen den gesetzliche Datenschutzbestimmungen verstoßen.

### 2 7 Keine oder schwache Verschlüsselung der Kommunikation zwischen MDM und Endgerät

Wird die Datenverbindung zwischen dem mobilen Endgerät und dem MDM-Server gar nicht oder mit veralteten Algorithmen verschlüsselt oder werden nicht ausreichende Schlüssellängen eingesetzt, ist die Vertraulichkeit und Integrität aller übertragenen Daten gefährdet. Zum Beispiel könnte ein Angreifer dadurch sein IT-System als MDM-Server ausgeben und so an schützenswerte Informationen gelangen oder auch Einstellungen auf allen mobilen Endgeräten der Institution verändern.

### 2 8 Unberechtigte Erstellung von Bewegungsprofilen durch das MDM

Mit den meisten MDM-Produkten lässt sich ermitteln, wo sich ein Gerät gerade befindet, und es können standortabhängig Daten oder Apps freigegeben bzw. gesperrt werden (sogenanntes Geofencing). Dadurch entstehen minutiöse Bewegungsprofile der Geräte und somit auch der Benutzer. Werden diese Daten erhoben, ohne den Benutzer geeignet darüber zu informieren, verstoßen die Verantwortlichen unter Umständen gegen datenschutzrechtliche Bestimmungen. Auch besteht die Gefahr, dass Angreifer auf diese Daten zugreifen. Ebenso kann Geofencing dazu missbraucht werden, um Mitarbeiter unzulässig zu kontrollieren.

### 2 9 Gefahren durch Bring Your Own Device (BYOD)

Werden private Endgeräte dienstlich genutzt, ergeben sich diverse Gefährdungspotentiale. Beispielsweise kann es bezüglich der Software-Lizenzen zu rechtlichen Problemen kommen. Wenn im Notfall dienstliche Daten durch das MDM auf dem Gerät gelöscht werden müssen, kann dies auch Auswirkungen auf die privaten Daten des Benutzers haben. Zudem können die IT-Verantwortlichen nicht mehr jedes einzelne Mitarbeiter-Gerät daraufhin prüfen, ob es sich auch dienstlich einsetzen lässt. Dadurch besteht die Gefahr, dass ungeeignete Geräte verwendet werden und so gegen interne Datenschutz- und Sicherheitsanforderungen verstoßen wird. Zudem sind die Benutzer oft selbst dafür verantwortlich, ihre privaten Geräte zu warten und reparieren zu lassen. Bei einer solchen Reparatur könnten beispielsweise Firmendaten unbefugt eingesehen werden. Die gleiche Gefahr besteht, wenn nicht geregelt ist, was mit den Daten auf dem Gerät geschehen soll, wenn der Mitarbeiter die Institution verlässt.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Mobile Device Management (MDM) aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.3.2.2.A1 Festlegung einer Strategie für das Mobile Device Management

Es MUSS eine Strategie erarbeitet werden, die festlegt, wie Mitarbeiter mobile Endgeräte benutzen dürfen und wie die Geräte in die IT-Strukturen der Institution integriert sind. Grundlage ist dabei der Schutzbedarf der zu verarbeitenden Informationen. Die Strategie MUSS mindestens folgende Aspekte abdecken:

* Darf das MDM als Cloud-Dienst betrieben werden?
* Soll das MDM durch die Institution selbst betrieben werden?
* Welche Compliance-Anforderungen müssen durchgesetzt werden?
* Welche mobilen Geräte und welche Betriebssysteme muss das MDM unterstützen?
* Muss die MDM-Lösung mandantenfähig sein?
* Müssen Cloud-Dienste eingebunden werden?
* Müssen Dokumentenmanagementsysteme eingebunden werden?
* Muss das MDM auch Peripherie-Geräte einbinden und verwalten?
* Welches Betriebsmodell soll eingesetzt werden: private Endgeräte (Bring Your Own Device, BYOD), personalisierte Endgeräte (Eigentum der Institution) oder nicht personalisierte Endgeräte (Eigentum der Institution, gemeinsam genutzt)?
Die Strategie MUSS schriftlich fixiert und vom ISB freigegeben werden.

#### SYS.3.2.2.A2 Festlegen erlaubter mobiler Endgeräte

Es MUSS festgelegt werden, welche mobilen Endgeräte und Betriebssysteme in der Institution zugelassen sind. Alle erlaubten Geräte und Betriebssysteme MÜSSEN den Anforderungen der MDM-Strategie genügen und die technischen Sicherheitsanforderungen der Institution vollständig erfüllen. Das MDM MUSS so konfiguriert werden, dass nur mit freigegebenen Geräten auf Informationen der Institution zugegriffen werden kann. Wenn neue mobile Endgeräte beschafft werden, MÜSSEN sie auf der Liste der zugelassenen Endgeräte stehen.

#### SYS.3.2.2.A3 Auswahl einer MDM-Produkts

Wenn eine geeignete MDM-Software beschafft werden soll, MUSS sichergestellt sein, dass sich mit ihr alle in der MDM-Strategie festgelegten Anforderungen erfüllen lassen. Auch MUSS sie sämtliche technischen und organisatorischen Sicherheitsmaßnahmen umsetzen können und alle zugelassen mobilen Endgeräte unterstützten. Weitere Hinweise zur Beschaffung finden sich im Baustein OPS.1.2.6 *Beschaffung, Ausschreibung und Einkauf*.

#### SYS.3.2.2.A4 Verteilung der Grundkonfiguration auf mobile Endgeräte

Alle mobilen Endgeräte MÜSSEN so schnell wie möglich in das MDM integriert werden, damit sie nach den Richtlinien der Institution konfiguriert und verwaltet werden können. Wenn die Geräte die Grundkonfiguration erhalten, MÜSSEN sie sich im Werkszustand befinden. Bei bereits benutzten Geräten MÜSSEN vorher alle institutionsbezogenen Daten gelöscht werden. Ein nicht über MDM konfiguriertes Endgerät DARF NICHT auf Informationen der Institution zugreifen können.

#### SYS.3.2.2.A5 Sichere Grundkonfiguration für mobile Endgeräte

Alle mobilen Endgeräte MÜSSEN so konfiguriert sein, dass sie den Schutzbedarf angemessen erfüllen. Dafür MUSS eine passende Grundkonfiguration zusammengestellt und dokumentiert werden. Einzelheiten dazu werden in den spezifischen Geräte-Bausteinen definiert.

Wenn mobile Endgeräte an Mitarbeiter übergeben werden, MUSS darauf bereits der MDM-Client installiert sein. Andernfalls MUSS es den Benutzern selbst möglich sein, den Client zu installieren. 

#### SYS.3.2.2.A6 Protokollierung

Das MDM MUSS alle sicherheitsrelevanten Ereignisse und Konfigurationsänderungen protokollieren. Die erhobenen Daten DÜRFEN NICHT von unbefugten Personen eingesehen werden und MÜSSEN unveränderbar gespeichert werden. Auch MÜSSEN bei der Protokollierung gesetzliche und interne Regelungen eingehalten werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Mobile Device Management (MDM). Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.3.2.2.A7 Auswahl und Freigabe von Apps

Apps aus öffentlichen App-Stores SOLLTEN durch die Verantwortlichen geprüft und freigegeben werden. Dazu SOLLTE ein Freigabeprozess entwickelt werden, in dem auch geeignete Bewertungskriterien definiert sind. Alle freigegebenen Apps SOLLTEN intern in einem Standardkatalog veröffentlicht werden und dort für die Benutzer verfügbar sein.

#### SYS.3.2.2.A8 Festlegung erlaubter Informationen auf mobilen Endgeräten

Die Institution SOLLTE festlegen, welche Informationen die mobilen Endgeräte unter welchen Bedingungen verarbeiten dürfen. Grundlage für die Regelung SOLLTE einerseits die Klassifikation bzw. Schutzbedarf der Informationen sein und andererseits die Bedingungen, unter denen die Daten auf den Geräten verarbeitet werden, etwa in abgeschotteten Containern. Die Verantwortlichen SOLLTEN das MDM auf Basis dieser Regeln konfigurieren, so dass es diese auf allen mobilen Endgeräten durchsetzen kann. Den Benutzern SOLLTEN die Regeln geeignet bekannt gegeben werden.

#### SYS.3.2.2.A9 Auswahl von Sicherheits-Apps

Um das erforderliche Sicherheitsniveau durchzusetzen, SOLLTEN für das Endgerät geeignete Sicherheits-Apps ausgewählt werden. Die Sicherheits-Apps SOLLTEN durch das MDM automatisch installiert werden.

#### SYS.3.2.2.A10 Sichere Anbindung der mobilen Endgeräte an die Institution

Die Verbindung der mobilen Endgeräte ins Netz der Institution SOLLTE angemessen abgesichert werden. Wenn Daten zwischen den mobilen Endgeräte und dem IT-Netz der Institution übertragen werden, SOLLTE durch geeignete Maßnahmen (z. B. VPN) verhindert werden, dass Unbefugte sie verändern oder einsehen können.

#### SYS.3.2.2.A11 Berechtigungsmanagement im MDM

Für das MDM SOLLTE ein Berechtigungskonzept erstellt, dokumentiert und angewendet werden. Den Benutzergruppen und Administratoren SOLLTE das MDM nur so viele Berechtigungen einräumen, wie für die Aufgabenerfüllung notwendig ist (Minimalprinzip). Es SOLLTE regelmäßig überprüft werden, ob die zugeteilten Rechte noch angemessen sind.

#### SYS.3.2.2.A12 Abgesicherte MDM-Betriebsumgebung

Das MDM selbst SOLLTE durch technische Maßnahmen abgesichert werden, um dem Schutzbedarf der hinterlegten oder verarbeiteten Informationen zu genügen. So SOLLTE beispielsweise das zugrundeliegende Betriebssystem gehärtet werden und alle notwendigen Patches SOLLTEN eingespielt sein.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.2.2.A13 Einschränkung der App-Installation mittels Whitelist(CIA)

Bei erhöhtem Schutzbedarf SOLLTEN die Benutzer der mobilen Endgeräte nur freigegebene und geprüfte Apps installieren dürfen. Das MDM SOLLTE verhindern, dass andere Apps installiert werden oder alternativ unbefugt installierte Apps sofort wieder entfernen.

#### SYS.3.2.2.A14 Benutzung externer Reputation-Services für Apps(CI)

Wenn die Administratoren einer Institution die erlaubten Apps nicht selbst auswählen können und Benutzer selbstständig Apps auf ihren Geräten installieren dürfen, SOLLTE ein sogenannter Reputation-Service eingesetzt werden. Dabei handelt es sich um einen externen Dienst, der Apps nach bestimmten Kriterien untersucht und die Ergebnisse als Service bereitstellt. Das MDM SOLLTE dann mithilfe dieser Informationen die Installation von Apps zumindest einschränken. 

#### SYS.3.2.2.A15 Nutzung von PIM-Containern(CI)

Um Information auf den mobilen Endgeräten vor Spionage-Apps zu schützen, SOLLTEN diese gekapselt werden, zum Beispiel in einem PIM-Container. Zusätzlich SOLLTEN die Daten durch ein Passwort und eine vom Betriebssystem unabhängige Verschlüsselung abgesichert werden.

#### SYS.3.2.2.A16 Nutzung von getrennten Arbeitsumgebungen(CI)

Ist es den Mitarbeitern erlaubt, dienstliche Geräte auch privat zu nutzen, SOLLTEN Lösungen für getrennte Arbeitsumgebungen auf dem Endgerät eingesetzt werden. Wenn möglich, SOLLTEN dafür nur zertifizierte Produkte (z. B. nach Common Criteria) beschafft werden.

#### SYS.3.2.2.A17 Kontrolle der Nutzung von mobilen Endgeräten(I)

Mit MDM-Lösungen lässt sich kontrollieren, wie die mobilen Endgeräte benutzt werden. Es SOLLTEN angemessene Kriterien definiert werden, aufgrund derer die Geräte zu überwachen sind, ohne gegen gesetzliche oder interne Regelungen zu verstoßen.

#### SYS.3.2.2.A18 Besonders abgesicherte Betriebssysteme(CIA)

Es gibt mehrere Anbieter besonders abgesicherter mobiler Endgeräte, die teilweise zertifiziert sind für die Verarbeitung von Informationen nach gesetzlichen Informationsschutz-Klassifizierungen. Wenn ein sehr hoher Schutzbedarf besteht, SOLLTE die Institution ein solches Gerät einsetzen und in das MDM integrieren.

#### SYS.3.2.2.A19 Geofencing(CI)

Mittels Geofencing-Richtlinien ist es möglich, bestimmte Funktionen oder Apps nur an vorher definierten Orten zu erlauben oder auch zu verbieten. Mithilfe einer Schutzbedarfsanalyse SOLLTEN Bereiche identifizieren werden, an denen diese zusätzlichen Sicherheitsmaßnahmen nötig sind. Anschließend SOLLTEN sie unter Beachtung gesetzlicher und interner Regelungen umgesetzt werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Mobile Device Management (MDM)" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSICS052] Mobile Device Management BSI-CS 052

  

 BSI, Version 1.00, 03.2013  
 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_052.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_052.pdf)

 
* #### [BYOD] Überblickspapier Consumerisation und BYOD

  

 BSI, Version 1.2, 07.2013  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier\_BYOD\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/Download/Ueberblickspapier_BYOD_pdf.pdf)

 
* #### [NIST18001D] SECURING ELECTRONIC HEALTH RECORDS ON MOBILE DEVICES

  

 SPECIAL PUBLICATION 1800-1d, NIST, 07.2015   
 [https://nccoe.nist.gov/sites/default/files/nccoe/NIST\_SP1800-1d\_Draft\_HIT\_Mobile-StandardsControls.pdf ](https://nccoe.nist.gov/sites/default/files/nccoe/NIST_SP1800-1d_Draft_HIT_Mobile-StandardsControls.pdf)

 
* #### [NIST800124] Guidelines for Managing the Security of Mobile Devices in the Enterprise

  

 Special Publication 800-124 Revision 1, NIST, 06.2013  
 [http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf ](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-124r1.pdf)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Mobile Device Management (MDM)" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.13 Abfangen kompromittierender Strahlung
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.45 Datenverlust
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

