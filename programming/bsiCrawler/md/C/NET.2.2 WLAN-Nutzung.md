1 Beschreibung
--------------

### 1.1 Einleitung

Über Wireless LANs (WLANs) können drahtlose lokale Netze aufgebaut oder bestehende drahtgebundene Netze erweitert werden. Bis heute basieren fast alle am Markt verfügbaren WLAN-Komponenten auf dem Standard IEEE 802.11 und seinen Ergänzungen. Eine besondere Rolle nimmt dabei das Hersteller-Konsortium Wi-Fi Alliance ein, das basierend auf dem Standard IEEE 802.11 mit "Wi-Fi" einen Industriestandard geschaffen hat. Dabei bestätigt die Wi-Fi Alliance mit dem Wi-Fi-Gütesiegel, dass ein Gerät gewisse Interoperabilitäts- und Konformitätstests bestanden hat. 

WLANs bieten einen Gewinn an Komfort und Mobilität, jedoch birgt die Nutzung auch zusätzliches Gefährdungspotenzial für die Sicherheit der Informationen, da drahtlos kommuniziert wird. Daher ist es unabdingbar, dass neben den IT-Verantwortlichen auch die Benutzer zu möglichen Gefahren sensibilisiert sind, die entstehen können, wenn WLANs unsachgemäß verwendet werden. Dies bedeutet, dass die Benutzer über die erforderlichen Kenntnisse verfügen müssen, um Sicherheitsmaßnahmen richtig verstehen und anwenden zu können. Insbesondere muss ihnen bekannt sein, was von ihnen im Hinblick auf Informationssicherheit erwartet wird und wie sie in bestimmten Situationen reagieren sollten, wenn sie WLANs nutzen.

### 1.2 Zielsetzung

In diesem Baustein soll aufgezeigt werden, wie WLANs sicher genutzt werden können.

### 1.3 Abgrenzung

Der Baustein enthält grundsätzliche Anforderungen, die bei der Nutzung von WLANs zu beachten und zu erfüllen sind, um den spezifischen Gefährdungen entgegenwirken zu können. Anforderungen, mit deren Hilfe WLANs sicher betrieben werden können, sind dagegen nicht Gegenstand des vorliegenden Bausteins, sondern sind im Baustein NET.2.1 *WLAN-Betrieb* beschrieben. Darüber hinaus geht der Baustein nicht auf allgemeine Aspekte eines Clients ein. Solche Aspekte werden im Baustein SYS2.1 *Allgemeiner Client* behandelt. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich WLAN-Nutzung von besonderer Bedeutung:

### 2 1 Unzureichende Kenntnis über Regelungen

Sind den Benutzern die Regelungen für den korrekten Umgang mit WLANs nicht hinreichend bekannt, können sie sich auch nicht daran halten. Werden WLAN-Clients zum Beispiel gedankenlos an fremde Netze angeschlossen, können die hierüber übertragenen Informationen (z. B. Sitzungs-Cookies, Passwörter) abgehört werden.

### 2 2 Nichtbeachtung von Sicherheitsmaßnahmen

Aufgrund von Nachlässigkeit und fehlenden Kontrollen kommt es immer wieder vor, dass Personen die ihnen empfohlenen oder angeordneten Sicherheitsmaßnahmen nicht oder nicht im vollen Umfang berücksichtigen. Wird beispielsweise ein WLAN-Client im Ad-hoc-Modus genutzt, obwohl dies ausdrücklich in der Benutzerrichtlinie verboten ist, kann ein anderer Client direkt mit dem WLAN-Client kommunizieren und z. B. unberechtigt auf vertrauliche Dokumente zugreifen, die auf dem Client gespeichert sind.

### 2 3 Abhören der WLAN-Kommunikation

Da es sich bei Funk um ein Medium handelt, das sich mehrere Benutzer teilen können ("Shared Medium"), können die über WLANs übertragenen Daten problemlos mitgehört und aufgezeichnet werden. Wenn die Daten nicht oder nur unzureichend verschlüsselt werden, können übertragene Nutzdaten leicht gewonnen werden. Zudem überschreiten Funknetze bzw. die ausgesendeten Funkwellen nicht selten die Grenzen der selbstgenutzten Räumlichkeiten, so dass Daten auch noch in Bereiche ausgestrahlt werden, die nicht von den Benutzern oder einer Institution kontrolliert und gesichert werden können.

### 2 4 Auswertung von Verbindungsdaten bei der drahtlosen Kommunikation

Bei WLANs auf Basis von IEEE 802.11 wird die MAC-Adresse einer WLAN-Karte bei jeder Datenübertragung mit versendet. Da sie unverschlüsselt übertragen wird, können Bewegungsprofile über mobile Nutzer erstellt werden, z. B. wenn diese sich in öffentliche Hotspots einbuchen.

### 2 5 Vortäuschung eines gültigen Access Points (Rogue Access Point)

Ein Angreifer kann sich als Teil der WLAN-Infrastruktur ausgeben, indem er einen eigenen Access Point mit einer geeignet gewählter SSID in der Nähe eines Clients installiert. Dieser vorgetäuschte Access Point wird als "Rogue Access Point" bezeichnet. Bietet dieser dem WLAN-Client eine stärkere Sendeleistung als der echte Access Point, wird der Client diesen als Basisstation nutzen, falls keine beidseitige Authentisierung erzwungen wird. Zusätzlich könnte auch der echte Access Point durch einen Denial-of-Service-Angriff ausgeschaltet werden. Die Benutzer melden sich an einem Netz an, das nur vorgibt, das Zielnetz zu sein. Dadurch ist es einem Angreifer möglich, die Kommunikation abzuhören. Auch durch Poisoning- oder Spoofing-Methoden kann ein Angreifer eine falsche Identität vortäuschen bzw. den Netzverkehr zu seinen Systemen umlenken. So kann er die Kommunikation belauschen und kontrollieren. Besonders in öffentlichen Funknetzen (sog. Hotspots) ist ein Rogue Access Point ein beliebtes Angriffsmittel. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich WLAN-Nutzung aufgeführt. Grundsätzlich ist der Benutzer für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### NET.2.2.A1 Erstellung einer Benutzerrichtlinie für WLAN [Leiter IT]

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution MÜSSEN die wesentlichen Kernaspekte für eine sichere WLAN-Nutzung in einer WLAN-Benutzerrichtlinie konkretisiert werden. In einer solchen Benutzerrichtlinie MÜSSEN die Besonderheiten bei der WLAN-Nutzung beschrieben sein, z. B. ob und wie Hotspots genutzt werden dürfen.

Des Weiteren MUSS die Richtlinie, insbesondere im Hinblick auf die Nutzung von eingestuften Informationen, Angaben dazu enthalten, welche Daten im WLAN genutzt und übertragen werden dürfen und welche nicht.

Es MUSS beschrieben sein, wie mit Client-seitigen Sicherheitslösungen umzugehen ist. Die Benutzerrichtlinie MUSS ein klares Verbot enthalten, ungenehmigte Access Points an das LAN der Institution anzuschließen. Außerdem MUSS in der Richtlinie darauf hingewiesen werden, dass die WLAN-Schnittstelle deaktiviert werden MUSS, wenn sie über einen längeren Zeitraum nicht genutzt wird.

Es MUSS regelmäßig überprüft werden, ob die in der Richtlinie geforderten Inhalte richtig umgesetzt worden sind. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.

#### NET.2.2.A2 Sensibilisierung und Schulung der WLAN-Benutzer [Vorgesetzte, Leiter IT]

Die Benutzer von WLAN-Komponenten, vornehmlich von WLAN-Clients, MÜSSEN sensibilisiert und zu den in der Benutzerrichtlinie aufgeführten Maßnahmen geschult werden. Den Benutzern MUSS genau erläutert werden, was die WLAN-spezifischen Sicherheitseinstellungen bedeuten und warum sie wichtig sind. Außerdem MÜSSEN sie auf die Gefahren hingewiesen werden, wenn diese Sicherheitseinstellungen umgangen oder deaktiviert werden.

Die Schulungsinhalte MÜSSEN immer entsprechend der jeweiligen Einsatzszenarien angepasst werden. Neben der reinen Schulung zu WLAN-Sicherheitsmechanismen MÜSSEN die Benutzer jedoch auch die WLAN-Sicherheitsrichtlinie ihrer Institution vorgestellt bekommen. Ebenso MÜSSEN sie über die Gefahren sensibilisiert werden, wenn fremde WLANs verwendet werden sollen.

#### NET.2.2.A3 Absicherung der WLAN-Nutzung in unsicheren Umgebungen [IT-Betrieb]

DÜRFEN externe Hotspots genutzt werden MUSS Folgendes umgesetzt werden:

* Jeder Benutzer eines Hotspots MUSS seine Sicherheitsanforderungen kennen (siehe NET.2.2.A2 Sensibilisierung und Schulung der WLAN-Benutzer) und danach entscheiden, ob bzw. unter welchen Bedingungen ihm die Nutzung des Hotspots erlaubt ist.
* WLANs, die nur sporadisch genutzt werden, SOLLTEN durch die Benutzer aus der Historie gelöscht werden. 
* Wenn möglich, SOLLTEN separate Benutzerkonten mit einer sicheren Grundkonfiguration und restriktiven Berechtigungen verwendet werden. 
* Es SOLLTE sichergestellt sein, dass sich kein Benutzer mit Administratorrechten von seinem Client aus an externen WLANs anmelden kann. 
* Sensible Daten DÜRFEN NUR übertragen werden, wenn entsprechende Sicherheitsmaßnahmen umgesetzt und sichere Protokolle verwendet werden. 
* Über öffentlich zugängliche WLANs DÜRFEN die Benutzer NUR über ein Virtual Private Network (VPN) auf interne Ressourcen der Institution zugreifen. Weitere Informationen hierzu sind im Baustein NET.3.3 VPN zu finden.
### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich WLAN-Nutzung. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### NET.2.2.A4 Verhaltensregeln bei WLAN-Sicherheitsvorfällen

Bei WLAN-Sicherheitsvorfällen SOLLTEN die Benutzer Folgendes umsetzen:

* Sie SOLLTEN ihre Arbeitsergebnisse sichern, den WLAN-Zugriff beenden und die WLAN-Schnittstelle ihres Clients deaktivieren.
* Fehlermeldungen und Abnormalitäten SOLLTEN durch die Benutzer genau dokumentiert werden. Ebenso SOLLTEN die Benutzer dokumentieren, was sie getan haben bevor bzw. während der Sicherheitsvorfall eingetreten ist.
* Die Benutzer SOLLTEN über eine geeignete Eskalationsstufe (z. B. User Help Desk) den IT-Betrieb benachrichtigen. 
### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "WLAN-Nutzung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSIDKS] Drahtlose Kommunikationssysteme und ihre Sicherheitsaspekte

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [ISIWLAN] BSI-Standard zur Internet-Sicherheit (ISi-Reihe)

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02.2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [TR03103] Technische Richtlinie Sicheres Wireless LAN

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "WLAN-Nutzung" von Bedeutung.

* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.43 Einspielen von Nachrichten
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

