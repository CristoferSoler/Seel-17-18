1 Beschreibung
--------------

### 1.1 Einleitung

Ein Laptop (oder auch Notebook) ist ein PC, der mobil genutzt werden kann. Er hat eine kompakte Bauform, integriert Peripheriegeräte wie Tastatur und Bildschirm, ist über Akkus zeitweise unabhängig von einer externen Stromversorgung und besteht oft aus speziell für den mobilen Einsatz konzipierten Hardware-Komponenten. Laptops können mit allen üblichen Betriebssystemen wie Windows, Apple macOS oder Linux betrieben werden. Die Geräte sind in den meisten Institutionen verbreitet und ersetzen für einige Mitarbeiter den klassischen Desktop-PC. 

Da Laptops häufig mobil genutzt werden, sind sie oft nicht permanent am LAN der Institution angeschlossen, sondern können sich in der Regel per Virtual Private Network (VPN) über das Internet oder andere Datennetze einwählen, um so auf die Ressourcen des LANs zuzugreifen. Auch die Infrastruktur einer klassischen Büroumgebung, wie kontrollierbare Umwelteinflüsse, eine stabile Stromversorgung oder zutrittsgeschütze Bereiche, kann für den mobilen Einsatz von Laptops nicht vorausgesetzt werden.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, einen sicheren Betrieb von Laptops in Institutionen zu ermöglichen sowie für die spezifischen Gefährdungen dieser Geräteklasse zu sensibilisieren.

### 1.3 Abgrenzung

Um Risiken durch Fehlbedienung oder den absichtlichen Missbrauch der Laptops auszuschließen, ist es notwendig, die Betriebssystem- und Software-Komponenten sorgfältig auszuwählen und zu installieren. Die hier zu erfüllenden Anforderungen sind abhängig vom Betriebssystem des Laptops und werden daher in den Client-spezifischen Bausteinen beschrieben, beispielsweise SYS.2.2.3 *Client unter Windows 10, *SYS 2.3 *Clients unter Unix *oder* SYS.2.4 Clients unter OS X*. Ebenso sind Anforderungen, die für jede Art von Clients gelten, nicht Bestandteil dieses Bausteins, diese sind in SYS.2.1 *Allgemeiner Client* zu finden. 

Auch wird nicht behandelt, wie die jeweilige Datenübertragung einzurichten ist, wie z. B. die WLAN-Konfiguration (siehe NET.2.2 *WLAN-Nutzung*) oder die VPN-Anbindung (siehe NET.3.3 Virtual Private Networks (VPN)).

Um Angriffsversuche und missbräuchliche Nutzung erkennen zu können, sind bei Laptops vor allem organisatorische Anforderungen notwendig. Die notwendigen Anforderungen werden im Rahmen der Umsetzung des Bausteins OPS.1.1.2 *Ordnungsgemäße IT-Administration* und daher nicht hier betrachtet.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich *Laptop* von besonderer Bedeutung:

### 2 1 Beeinträchtigung durch wechselnde Einsatzumgebung

Laptops werden in sehr unterschiedlichen Umgebungen eingesetzt und sind dadurch vielen Gefährdungen ausgesetzt. Dazu gehören beispielsweise schädigende Umwelteinflüsse, wie zu hohe oder zu niedrige Temperaturen, ebenso wie Staub oder Feuchtigkeit. Bei mobilen Geräten besteht auch stets die Gefahr von Transportschäden. Außerdem kommunizieren Laptops vor allem unterwegs oft mit unbekannten IT-Systemen oder Netzen, was immer ein Gefährdungspotenzial für den eigenen Laptop mit sich bringt. So können dabei beispielsweise Schadprogramme mit übertragen oder schützenswerte Informationen kopiert werden. 

### 2 2 Diebstahl

Mitarbeiter benutzen ihre Laptops regelmäßig auch außerhalb der Institution. Die Geräte werden in privaten Kraftfahrzeugen oder öffentlichen Verkehrsmitteln transportiert, in fremden Büroräumen in Pausen zurückgelassen oder in Hotelzimmern unbewacht aufgestellt. Aufgrund dieser Umfeldbedingungen sind Laptops naturgemäß einem höheren Diebstahlrisiko ausgesetzt. Wird ein Laptop gestohlen, entstehen Kosten für die Wiederbeschaffung sowie für die Wiederherstellung eines arbeitsfähigen Zustandes. Ebenso könnten dadurch aber auch Unbefugten schützenswerte Daten offengelegt werden, wodurch es zu weiteren Schäden kommen kann. Diese wiegen in vielen Fällen deutlich schwerer als der rein materielle Verlust des Gerätes. 

### 2 3 Ungeordneter Benutzerwechsel bei Laptops

Wenn Mitarbeiter nur in Ausnahmefällen mobile IT-Systeme benötigen, wie beispielsweise für selten durchgeführte Dienstreisen, ist es oft zweckmäßiger, wenige Laptops für viele Benutzer vorzuhalten, die weitergereicht werden. Wird jedoch bei einem Benutzerwechsel der Laptop einfach an den nächsten Mitarbeiter übergeben, besteht die Gefahr, dass auf dem Gerät noch schutzbedürftige Daten gespeichert sind und dass es mit Schadsoftware verseucht ist. Zudem ist nach einiger Zeit nicht mehr nachvollziehbar, wer den Laptop wann benutzt hat oder wer ihn zurzeit benutzt. Der ungeordnete Benutzerwechsel ohne Speicherkontrollen und ohne entsprechende Dokumentation kann dazu führen, dass der Laptop nur noch eingeschränkt verfügbar ist und Restdaten auf der Festplatte unbefugt ausgelesen werden können.

### 2 4 Fehler bei der Synchronisation

Wenn Daten lokal auf einem Laptop bearbeitet werden, müssen sie wann immer es geht mit den Dateiservern der Institution synchronisiert werden, z. B. wenn sich der Mitarbeiter wieder über das VPN einloggt. Dabei können die Daten allerdings auch zerstört werden. Im Allgemeinen muss vor einer Synchronisation eingestellt werden, wie mit Konflikten beim Datenabgleich umzugehen ist: ob beispielsweise bei gleichlautenden Dateien die Version auf dem Laptop oder die von einem anderen Mitarbeiter ebenfalls bearbeitete Version auf dem Server ungefragt aktualisiert wird oder ob der Benutzer das entscheiden soll. Das wird häufig einmal konfiguriert und danach oft wieder vergessen. Werden dann aber Daten in einer anderen Reihenfolge geändert als ursprünglich einmal gedacht, gehen dabei schnell wichtige Informationen verloren.

### 2 5 Datenverlust bei mobilem Einsatz

Bei Laptops ist das Risiko von Datenverlusten höher als bei stationären Systemen. Ursache können Diebstahl oder Geräteverlust sein, aber auch technische Probleme oder schlichter Strommangel. So können zum Beispiel die Daten eines Laptops temporär nicht verfügbar sein, wenn der Akku leer ist. Sie können unter Umständen, wie z. B. bei älteren Geräten, aber auch vollständig vernichtet sein, wenn neben dem Akku auch die eventuell vorhandene Sicherungsbatterie leer ist und damit alle nicht bereits synchronisierten Daten verloren sind. 

### 2 6 Datendiebstahl mithilfe von Laptops

Mit Laptops können sehr leicht Daten mit anderen IT-Systemen ausgetauscht werden, z. B. über WLAN, Bluetooth oder eine Mobilfunkverbindung. Wo ein offener Zugang zu einem Laptop möglich ist, können Angreifer damit Informationen unauffällig abfragen, verändern oder mitnehmen. Eine nachträgliche Überprüfung oder gar ein Nachweis ist nicht immer möglich, da häufig die Zugriffe nicht entsprechend protokolliert werden. Auch können Angreifer in öffentlichen WLANs, die nicht ausreichend abgesichert sind und über die ein Laptop kommuniziert, alle übermittelten Daten mitschneiden und haben so im schlechtesten Fall Zugriff auf die Dateien im Netz der Institution.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen an Laptops aufgeführt. Grundsätzlich ist der *IT-Betrieb *für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.3.1.A1 Regelungen zur mobilen Nutzung von Laptops

Es MUSS klar geregelt werden, was Mitarbeiter beachten sollen, wenn sie Laptops mitnehmen. Es MUSS insbesondere festgelegt werden, welche Laptops außer Haus mitgenommen werden dürfen, wer sie mitnehmen darf und welche grundlegenden Sicherheitsmaßnahmen dabei zu beachten sind. Die Benutzer MÜSSEN auf die Regelungen hingewiesen werden. 

#### SYS.3.1.A2 Zugriffsschutz am Laptop [Benutzer]

Auf allen Laptops MUSS ein angemessener Zugriffsschutz vorhanden sein, der verhindert, dass das Gerät unberechtigt benutzt werden kann. Es MUSS geprüft werden, ob alle Mitarbeiter sich an die Regeln für den korrekten Umgang mit dem eingerichteten Zugriffsschutz halten.

#### SYS.3.1.A3 Einsatz von Personal Firewalls

Auf Laptops MUSS eine Personal Firewall aktiv sein. Die Filterregeln der Firewall MÜSSEN so restriktiv wie möglich sein. Sie MÜSSEN regelmäßig getestet werden. Die Personal Firewall MUSS so konfiguriert werden, dass die Benutzer nicht durch Warnmeldungen belästigt werden, die sie nicht interpretieren können. 

#### SYS.3.1.A4 Einsatz von Antivirenprogrammen [Benutzer]

Abhängig vom installierten Betriebssystem und anderer vorhandener Schutzmechanismen MUSS auf allen Laptops der Institution ein Antivirenprogramm installiert und aktiviert sein. Es MUSS sichergestellt werden, dass sowohl das Scan-Programm als auch die Signaturen stets auf dem aktuellsten Stand sind. Die Benutzer MÜSSEN mit der Antivirensoftware vertraut gemacht werden, besonders auch mit On-Demand-Scans. 

Der gesamte Datenbestand der Laptops MUSS regelmäßig auf Schadprogramme geprüft werden. Wenn der Rechner infiziert ist, MUSS im Offlinebetrieb untersucht werden, ob das gefundene Schadprogramm bereits vertrauliche Daten gesammelt, Schutzfunktionen deaktiviert oder Code aus dem Internet nachgeladen hat. 

Das Antivirenprogramm MUSS zudem nach Schadsoftware suchen, wenn Dateien ausgetauscht oder übertragen werden. Auch MÜSSEN alle auf dem Laptop benutzten Internet-Dienste (HTTP, FTP) sowie verschlüsselte Daten ausreichend vor Schadprogrammen geschützt werden. 

Außerdem MUSS sichergestellt werden, dass die Benutzer keine sicherheitsrelevanten Änderungen an den Einstellungen der Antivirenprogramme vornehmen können.

#### SYS.3.1.A5 Datensicherung [Benutzer]

Alle Daten, die auf Laptops lokal gespeichert werden, MÜSSEN regelmäßig gesichert werden. Hierfür MÜSSEN abhängig vom Volumen des Datenbestands geeignete Verfahren zur Datensicherung ausgewählt werden. Die Datensicherung MUSS weitgehend automatisiert werden, sodass die Benutzer möglichst wenig Aktionen selbst durchführen müssen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Laptops. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.3.1.A6 Sicherheitsrichtlinien für Laptops [Leiter IT]

Für Laptops SOLLTE eine Sicherheitsrichtlinie erstellt werden, die regelt, wie die Geräte benutzt werden dürfen. Die Benutzer SOLLTEN hinsichtlich des Schutzbedarfs von Laptops und der auf ihnen befindlichen Daten sensibilisiert werden. Auch SOLLTEN sie auf die spezifischen Gefährdungen bzw. die entsprechenden Anforderungen für die Nutzung aufmerksam gemacht werden. Sie SOLLTEN außerdem darüber informiert werden, welche Art von Informationen sie auf Laptops verarbeiten dürfen. 

#### SYS.3.1.A7 Geregelte Übergabe und Rücknahme eines Laptops [Benutzer]

Wenn Laptops von verschiedenen Personen abwechselnd genutzt werden, SOLLTE geregelt werden, wie Laptops sicher an Mitarbeiter übergeben werden können bzw. wie sie wieder sicher zurückzunehmen sind. Beim Benutzerwechsel eines Laptops SOLLTEN eventuell vorhandene schützenswerte Daten sicher gelöscht werden. Falls der Laptop nach dem Benutzerwechsel nicht neu aufgesetzt wird, SOLLTE sichergestellt sein, dass sich auf dem System bzw. allen damit verbundenen Datenträgern keine Schadsoftware befindet. Mit einem Laptop SOLLTE den Mitarbeitern ein Merkblatt für den sicheren Umgang mit dem Gerät ausgehändigt werden. 

#### SYS.3.1.A8 Sicherer Anschluss von Laptops an Datennetze [Benutzer]

Es SOLLTE geregelt werden, wie Laptops sicher an eigene oder fremde Netze und an das Internet angeschlossen werden. Laptops SOLLTEN wirksam vor Schadcode und vor Angriffen aus Fremdnetzen und aus dem Internet geschützt werden. Dafür SOLLTEN das Betriebssystem und die installierte Software von Laptops immer auf dem aktuellen Stand sein. Es SOLLTEN sich nur zugelassene Laptops am internen Netz der Institution anmelden können. Nicht benötigte Schnittstellen SOLLTEN bei allen Laptops deaktiviert werden.

#### SYS.3.1.A9 Sicherer Fernzugriff von unterwegs [Benutzer]

Daten, die zwischen einem Laptop von außerhalb und dem internen Netz der Institution übertragen werden, SOLLTEN durch geeignete Maßnahmen ausreichend geschützt werden, zum Beispiel durch ein VPN oder mit TLS. Auch SOLLTE der Laptop selbst abgesichert sein, wenn Daten mit anderen IT-Systemen ausgetauscht werden. 

#### SYS.3.1.A10 Abgleich der Datenbestände von Laptops [Benutzer]

Es SOLLTE geregelt werden, wie Daten von Laptops in den Informationsverbund der Institution übernommen werden. Wenn ein Synchronisationstool benutzt wird, SOLLTE sichergestellt sein, dass Synchronisationskonflikte aufgelöst werden können, der Synchronisationsvorgang protokolliert wird und die Benutzer angewiesen sind, die Synchronisationsprotokolle zu prüfen. 

#### SYS.3.1.A11 Sicherstellung der Energieversorgung [Benutzer]

Alle Benutzer SOLLTEN darüber informiert werden, wie sie die Energieversorgung von Laptops im mobilen Einsatz optimal sicherstellen können. Falls für die Laptops Ersatzakkus verfügbar sind, SOLLTEN diese in entsprechenden Hüllen gelagert und transportiert werden. 

#### SYS.3.1.A12 Verlustmeldung [Benutzer]

Es SOLLTE umgehend gemeldet werden, wenn ein Laptop verloren gegangen ist oder gestohlen wurde. Dafür SOLLTE es in jeder Institution klare Meldewege geben. Wenn verlorene Laptops wieder auftauchen, SOLLTE untersucht werden, ob sie eventuell manipuliert wurden. Sie SOLLTEN komplett neu installiert werden. 

#### SYS.3.1.A13 Verschlüsselung von Laptops

Die Festplatten eines Laptops SOLLTEN verschlüsselt werden. Für die Verschlüsselung SOLLTE ein sicherer Verschlüsselungsalgorithmus eingesetzt werden. Die Schlüssel SOLLTEN zufällig erzeugt und Daten und Schlüssel getrennt aufbewahrt werden.

#### SYS.3.1.A14 Geeignete Aufbewahrung von Laptops [Benutzer]

Alle Benutzer SOLLTEN darauf hingewiesen werden, wie Laptops außerhalb der Institution geeignet aufbewahrt werden sollen. Auch in den Räumen der Institution SOLLTEN Laptops außerhalb der Nutzungszeiten gegen Diebstahl gesichert bzw. verschlossen aufbewahrt werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.3.1.A15 Geeignete Auswahl von Laptops [Beschaffungsstelle](A)

Bevor Laptops beschafft werden, SOLLTEN die Verantwortlichen eine Anforderungsanalyse durchführen. Sie SOLLTE auch auf zusätzlich benötigte Hardware, wie z. B. Dockingstations und Monitore, erweitert werden. Anhand der Ergebnisse SOLLTEN alle infrage kommenden Geräte bewertet werden. Die Beschaffungsentscheidung SOLLTE mit den Administratoren und dem technischen Personal abgestimmt sein.

#### SYS.3.1.A16 Zentrale Administration von Laptops(CI)

Es SOLLTE eine geeignete Vorgehensweise definiert werden, wie Laptops zentral zu administrieren sind, da sich so nicht nur Software und Informationen einfacher verteilen lassen, sondern auch die institutionsseigenen Sicherheitsrichtlinien besser durchgesetzt werden können. Deswegen SOLLTE eine geeignete Vorgehensweise definiert werden, wie Laptops zentral zu administrieren sind. Ein Tool zum zentralen Laptop-Management SOLLTE möglichst alle eingesetzten Betriebssysteme unterstützen.

#### SYS.3.1.A17 Sammelaufbewahrung(A)

Nicht benutzte Laptops SOLLTEN in einem geeignet abgesicherten Raum vorgehalten werden. Der dafür genutzte Raum SOLLTE den Anforderungen aus *INF.5 Technikraum* entsprechen.

#### SYS.3.1.A18 Einsatz von Diebstahl-Sicherungen(CIA)

Es SOLLTE geregelt werden, welche Diebstahlsicherungen für Laptops eingesetzt werden sollen. Bei mechanischen Sicherungen SOLLTE besonders auf ein gutes Schloss geachtet werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Laptops " finden sich unter anderem in folgenden Veröffentlichungen:

5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Laptops " von Bedeutung.

* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.22 Manipulation von Informationen
* G 0.39 Schadprogramme
* G 0.45 Datenverlust
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

