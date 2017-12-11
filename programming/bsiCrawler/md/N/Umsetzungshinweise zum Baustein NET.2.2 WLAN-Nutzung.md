1 Beschreibung
--------------

### 1.1 Einleitung

Über Wireless LANs (WLANs) können drahtlose lokale Netze aufgebaut oder bestehende drahtgebundene Netze erweitert werden. Bis heute basieren fast alle am Markt verfügbaren WLAN-Komponenten auf dem Standard IEEE 802.11 und seinen Ergänzungen. Eine besondere Rolle nimmt dabei das Hersteller-Konsortium Wi-Fi Alliance ein, das basierend auf dem Standard IEEE 802.11 mit "Wi-Fi" einen Industriestandard geschaffen hat. Dabei bestätigt die Wi-Fi Alliance mit dem Wi-Fi-Gütesiegel, dass ein Gerät gewisse Interoperabilitäts- und Konformitätstests bestanden hat. 

Alle Benutzer (inklusive Leitung der Institution) müssen über WLAN-Grundlagen informiert und zu möglichen Gefahren sensibilisiert sein, die entstehen können, wenn WLANs unsachgemäß verwendet werden. Sie müssen über die erforderlichen Kenntnisse verfügen, um Sicherheitsmaßnahmen richtig verstehen und anwenden zu können. Insbesondere muss ihnen bekannt sein, was von ihnen im Hinblick auf Informationssicherheit erwartet wird und wie sie in bestimmten Situationen bei der Nutzung von WLANs reagieren sollten.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Bevor WLANs betrieben und genutzt werden, ist eine sorgfältige Planung notwendig. Um Benutzer nicht mit zu vielen betrieblichen und sicherheitstechnischen Details einer WLAN-Infrastruktur zu überlasten, sollte eine eigene WLAN-Richtlinie speziell für diese Zielgruppe erstellt werden (siehe NET.2.2.M1 *Erstellung einer Benutzerrichtlinie für WLAN*). 

**Umsetzung**

Um die Sicherheitsanforderungen der Institution in der täglichen Nutzung von WLANs zu erfüllen, müssen die Benutzer mit eingebunden werden. So müssen sie über Sicherheitsmaßnahmen informiert werden, die nicht nur mit technischen Mitteln umgesetzt werden können und die ihre Mitwirkung erfordern. Um Sicherheitsvorfälle zu minimieren und auf mögliche Gefahren hinzuweisen, die entstehen können, wenn WLANs unsachgemäß genutzt werden, sind Benutzer ausreichend zu schulen und zu sensibilisieren (siehe NET.2.2.M2 *Sensibilisierung und Schulung der WLAN-Benutzer*).

**Betrieb **

Dürfen externe Hotspots genutzt werden, dann müssen die Mitarbeiter gezielt hinsichtlich der Hotspot-Nutzung geschult werden und entsprechende Maßnahmen umsetzen (siehe NET.2.2.M3 *Absicherung der WLAN-Nutzung in unsicheren Umgebungen*).

**Notfallvorsorge**

Wurden Angriffe auf ein WLAN oder innerhalb eines WLANs erkannt, so müssen die Benutzer des WLANs wissen, wie sie sich zu verhalten haben (siehe NET.2.2.M4 *Verhaltensregeln bei WLAN-Sicherheitsvorfällen*).

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "WLAN-Nutzung" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### NET.2.2.M1 Erstellung einer Benutzerrichtlinie für WLAN [Leiter IT]

Um Benutzer nicht mit zu vielen betrieblichen und sicherheitstechnischen Details einer WLAN-Infrastruktur zu überlasten, sollte eine eigene WLAN-Richtlinie speziell für diese Zielgruppe erstellt werden. Die Benutzerrichtlinie baut auf der allgemeinen Sicherheitsrichtlinie der Institution auf und konkretisiert die wesentlichen Kernaspekte, um WLANs sicher zu nutzen. In einer solchen Benutzerrichtlinie sollten dann kurz die Besonderheiten bei der WLAN-Nutzung beschrieben werden, wie z. B.

* mit welchen internen und externen Netzen die WLAN-Clients verbunden werden dürfen,
* unter welchen Rahmenbedingungen sie sich an internen oder externen WLANs anmelden dürfen,
* ob und wie Hotspots genutzt werden dürfen,
* dass der Ad-hoc-Modus abzuschalten ist, damit kein anderer Client direkt auf die WLAN-Clients zugreifen kann,
* welche Schritte bei (vermuteter) Kompromittierung der WLAN-Clients zu unternehmen sind, vor allem, wer zu benachrichtigen ist.
Wichtig ist auch, dass klar beschrieben wird, wie mit clientseitigen Sicherheitslösungen umzugehen ist. Dazu gehört beispielsweise, dass

* keine sicherheitsrelevanten Konfigurationen verändert werden dürfen,
* eine vorhandene Personal Firewall nicht abgeschaltet werden darf,
* alle Freigaben von Verzeichnissen oder Diensten deaktiviert oder zumindest durch gute Passwörter geschützt sind,
* für die Nutzung externer WLANs nach Möglichkeit nur spezielle Benutzerkonten mit restriktiver Rechtevergabe verwendet werden sollten.
Außerdem sollte die Benutzerrichtlinie ein klares Verbot enthalten, ungenehmigt Access Points an das LAN der Institution anzuschließen. Auch muss in der Richtlinie darauf hingewiesen werden, dass die WLAN-Schnittstelle deaktiviert werden muss, wenn sie über einen längeren Zeitraum nicht genutzt wird. Des Weiteren sollte die Richtlinie insbesondere im Hinblick auf die Nutzung von klassifizierten Informationen, beispielsweise Verschlusssachen, Angaben dazu enthalten, welche Daten in WLANs genutzt und übertragen werden dürfen und welche nicht. Benutzer sollten für WLAN-Gefährdungen sowie für Inhalte und Auswirkungen der WLAN-Richtlinie sensibilisiert werden. 

Es muss regelmäßig überprüft werden, ob die in der Richtlinie geforderten Inhalte richtig umgesetzt worden sind und die Ergebnisse sollten sinnvoll dokumentiert werden.

#### NET.2.2.M2 Sensibilisierung und Schulung der WLAN-Benutzer [Vorgesetzte, Leiter IT]

Heutzutage ist fast jeder Mitarbeiter mit einem mobilen Gerät ausgestattet und kann sich mit einem öffentlichen oder internen WLAN verbinden. Über mobile Geräte (z. B. Smartphones) lassen sich WLAN-Hotspots für andere erzeugen oder Ad-Hoc-WLANs aufbauen. Durch diese vielseitigen Nutzungsmöglichkeiten können Sicherheitsprobleme entstehen, wenn die Geräte unsachgemäß eingesetzt werden. Daher müssen alle Mitarbeiter entsprechend sensibilisiert werden. Dies kann beispielsweise mithilfe eines Merkblatts zu möglichen Gefahren, die mit der Nutzung von WLANs verbunden sind, geschehen. Das Merkblatt sollte außerdem die wichtigsten Maßnahmen und Verhaltensweisen enthalten, um entsprechenden Gefährdungen entgegenwirken zu können. Das Merkblatt sollte gemeinsam mit den Geräten übergeben werden, damit die Benutzer verantwortungsvoll mit den Geräten umgehen und diese gewissenhaft nutzen können. Sollte es den Benutzern erlaubt sein, über ihr Gerät sich selbst oder anderen ein WLAN (als Hotspot) zur Verfügung zu stellen, sollten die Schulungsinhalte auch die damit verbundenen Gefährdungen und Maßnahmen enthalten. Es kann beispielsweise darauf hingewiesen werden, dass die WLAN-Kommunikation geschützt werden kann, indem ein komplexes Passwort konfiguriert wird.

Die Sensibilisierung insbesondere von Benutzern, die auf vertrauliche Informationen zugreifen dürfen, sollte multimedial und durch praktische Beispiele geübt und unterstützt werden.

Eine besondere Gefährdung für die WLAN-Clients besteht, wenn öffentliche Funknetze (sog. Hotspots) genutzt werden. Hotspots verwenden häufig keine oder nur schwache Sicherheitsmechanismen, um Kunden einen unkomplizierten Zugang zu ermöglichen. Dadurch können übertragene Informationen in der Regel leicht abgehört werden. Sollen Hotspots für die Einwahl in die Institution genutzt oder vertrauliche Informationen hierüber übertragen werden, müssen die Benutzer gezielt hinsichtlich der Hotspot-Nutzung geschult werden und entsprechende Maßnahmen umsetzen. Beispielsweise müssen sie darauf achten, dass alle Verbindungen geeignet verschlüsselt sind. Bei eventuellen Verdachtsmomenten verursacht durch Warnhinweise oder Umleitungen auf IT-Systeme, die nicht zur Institution gehören, muss davon ausgegangen werden, dass dies ein Sicherheitsvorfall sein könnte.

Jedem Benutzer muss klar sein, dass WLANs zu nutzen die Mobilität stark unterstützt, jedoch auch Gefahren birgt, da Angreifer sich außerhalb des Sichtfeldes oder des vermuteten räumlichen WLAN-Empfangsbereiches befinden können. 

#### NET.2.2.M3 Absicherung der WLAN-Nutzung in unsicheren Umgebungen [IT-Betrieb]

Bei Hotspots handelt es sich um einen räumlich begrenzten Funkbereich. Meistens werden Hotspots explizit aufgebaut, damit sie durch fremde Teilnehmer genutzt werden können. Ihr Hauptzweck ist üblicherweise der drahtlose Zugang zum Internet. Häufig findet man solche Hotspots in Hotels, Flughäfen, Messehallen, Bahnhöfen und Kongresszentren.

Hotspots sollten immer als unsicheres Netz betrachtet werden, zum einem, da das dort vorhandene Sicherheitsniveau von außen nur schwer einzuschätzen ist und zum anderen, weil die meisten Hotspots ihre Dienste in Form von "Shared Networks" anbieten. Dadurch kann im Allgemeinen von jedem Endgerät auf jedes andere Endgerät im Netz zugegriffen werden. Ist das Risiko, das bei der Nutzung eines Hotspots entsteht, generell nicht abschätzbar, so kann erwogen werden, die Nutzung von Hotspots durch die WLAN-Sicherheitsrichtlinie vollständig zu verbieten. 

Die Betreiber von Hotspots können viel für die Sicherheit der von ihnen angebotenen Funkstrecke und anderen Dienstleistungen tun (siehe NET.2.3 *Betrieb von Hotspots*), ohne Mitarbeit der Benutzer ist eine vernünftige Absicherung allerdings nicht zu erreichen. Hierzu gehören unter anderem folgende Maßnahmen:

* Jeder Benutzer eines Hotspots sollte seine Sicherheitsanforderungen kennen und danach entscheiden, ob bzw. unter welchen Bedingungen ihm die Nutzung des Hotspots erlaubt ist.
* Die Anmeldung am Hotspot erfolgt meist über ein Web-Portal bzw. über eine Web-Applikation. Diese muss für den Schutz der Anmelde-Information sorgen. Die Authentisierung sollte immer verschlüsselt erfolgen.
* WLANs, die nur sporadisch genutzt wurden, sollten durch die Benutzer aus der Historie entfernt werden. Dazu wird die Kennung des WLANs (SSID) aus der Liste entfernt. Dadurch wird verhindert, dass sich das Endgerät ungewollt in das WLAN einbucht.
* Wenn möglich, sollten für die Nutzung von Hotspots spezielle Benutzerkonten mit sicherer Grundkonfiguration und restriktiven Rechten angelegt werden. Keinesfalls sollte sich ein Benutzer mit Administratorrechten von seinem Client aus an externen WLANs anmelden.
* Spätestens dann, wenn finanzrelevante, personenbezogene oder andere sensible Daten wie Kreditkartennummern, PINs, Passwörter oder auch E-Mails übertragen werden sollen, muss sichergestellt werden, dass alle notwendigen Sicherheitsmaßnahmen auf den Clients, vor allem Verschlüsselung, aktiviert sind. Als Beispiel wäre hier das sichere Bearbeiten von E-Mails über eine HTTPS-Webschnittstelle zu nennen. Vertrauliche Informationen dürfen nie unverschlüsselt über fremde Netze übertragen werden.
* Über fremde WLANs (z. B. bereitgestellte Gastzugänge fremder Institution oder öffentliche Hotspots) dürfen die Benutzer nur über VPNs auf interne Ressourcen der Institution zugreifen. Dadurch kann die Kommunikation in die eigene Institution unabhängig von den etablierten Schutzmechanismen der verwendeten WLAN-Infrastruktur zusätzlich abgesichert werden. Weitere Informationen hierzu finden sich im Baustein NET.3.3 VPN bzw. in den zugehörigen Umsetzungshinweisen.
### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "WLAN-Nutzung".

#### NET.2.2.M4 Verhaltensregeln bei WLAN-Sicherheitsvorfällen

Falls sich das WLAN in nicht vorgesehener Weise verhält (z. B. WLAN ist längere Zeit nicht verfügbar, auf Netzressourcen kann nicht zugegriffen werden, die Netzperformance bricht dauerhaft ein), kann dies durch einen Sicherheitsvorfall verursacht worden sein.

Die WLAN-Benutzer sollten Folgendes umsetzen:

* Sie sollten ihre Arbeitsergebnisse sichern, den WLAN-Zugriff beenden und die WLAN-Schnittstelle ihres Clients deaktivieren.
* Sollten Fehlermeldungen erscheinen oder sich der Client nicht normal verhalten haben, so sollten diese durch die Benutzer genau dokumentiert werden. Ebenso sollte dokumentiert werden, was der Benutzer getan hat bevor bzw. während der Sicherheitsvorfall eingetreten ist. Mithilfe dieser Informationen kann der IT-Betrieb den Grund und die Auswirkungen des Vorfalls eventuell schneller eingrenzen und Gegenmaßnahmen gezielter einleiten.
* Außerdem sollten sie den IT-Betrieb über eine geeignete Eskalationsstufe benachrichtigen. 
### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Über den Baustein, die Umsetzungshinweise und die Literaturübersicht hinausgehend liegen derzeit keine weiteren wissenswerten Informationen vor.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "WLAN-Nutzung" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSIDKS] Drahtlose Kommunikationssysteme und ihre Sicherheitsaspekte

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2009 <https://www.bsi.bund.de/DE/Publikationen/Broschueren/Drahtloskom/drahtloskom.html>

 
* #### [IEEE] Institute of Electrical and Electronics Engineers (IEEE)

  

 IEEE, (zuletzt abgerufen am 05.10.2017)  
 <https://www.ieee.org/index.html>

 
* #### [ISIWLAN] BSI-Standard zur Internet-Sicherheit (ISi-Reihe)

  

 Sichere Anbindung von lokalen Netzen an das Internet (Isi-LANA), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2014   
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/ISi-Reihe/ISi-LANA/lana_node.html)

 
* #### [KB2977292] Microsoft security advisory

  

 Sicherheitsupdate für Windows 7 für x64-basierte Systeme, (zuletzt abgerufen am 05.10.2017)  
 <https://www.microsoft.com/de-de/download/details.aspx?id=44350>

 
* #### [NIST800153] NIST Special Publication 800-153

  

 Guidelines for Securing Wireless Local Area Networks (WLANs), NIST, 02.2012 http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-153.pdf

 
* #### [NIST80097] NIST Special Publication 800-97

  

 Establishing Wireless Robust Security Networks, A Guide to IEEE 802.11, NIST, 02.2007  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>

 
* #### [RSWLAN] Mehr Rechtssicherheit bei WLAN

  

 BMWi, (zuletzt abgerufen am 05.10.2017)  
 <https://www.bmwi.de/Redaktion/DE/Artikel/Digitale-Welt/wlan.html>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
* #### [TR03103] Technische Richtlinie Sicheres Wireless LAN

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 2005 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr03103/index_htm.html)

 
* #### [WIFIA] Wi-Fi Allianz

  

 The worldwide netword of companies, (zuletzt abgerufen am 05.10.2017)  
 <http://www.wi-fi.org/>

 
