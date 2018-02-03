1 Beschreibung
--------------

### 1.1 Einleitung

Sensoren sind als elektronische Komponente mit Mikroprozessor und Software ausgeführte Messumformer, die eine physikalische Größe in einen elektrischen Ausgabewert wandeln. Dieser wird als normiertes Einheitssignal (häufig 4 bis 20 mA, 0 bis 10 V) als Daten an einer seriellen Schnittstelle oder als digitale Informationen, die über einen Feldbus oder Ethernet-Protokolle übertragen werden, bereitgestellt. Messumformer stellen neben den Messwerten häufig noch Schnittstellen, über die eine Diagnose und Parametrierung erfolgt, bereit. So kann ein Sensor neben einem elektronischen Ausgabewert auch noch über weitere Schnittstellen verfügen, z. B. WLAN, Bluetooth oder Wireless-HART-Schnittstellen für Parametrierung und Diagnose.

Auf dem Markt gibt es viele unterschiedliche Sensoren, z. B. um physikalische Größen zu messen. Je nach Aufgabe variieren der Funktionsumfang und die Leistungsfähigkeit eines Sensors stark. Die Bandbreite reicht von Sensoren, die lediglich Messwerte liefern und nicht konfiguriert werden müssen, über solche, die eine Kalibrierung, Konfiguration oder Vorverarbeitung von Daten bis hin zur vollständigen Signalverarbeitung (intelligente Sensoren, smart sensors) ermöglichen.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, alle Arten von intelligenten Sensoren abzusichern, unabhängig von Hersteller, Bauart, Einsatzzweck und -ort. Er kann für einen einzelnen Sensor oder eine zusammenhängende, als Sensor eingesetzte Baugruppe angewendet werden.

### 1.3 Abgrenzung

Der vorliegende Systembaustein ist anzuwenden, um intelligente Sensoren abzusichern. Er ergänzt den übergeordneten Baustein IND.2.1 *Allgemeine ICS-Komponente *und setzt diesen voraus.

Einfache Sensoren ohne Konfigurationsschnittstellen oder komplexere Verarbeitungslogik werden durch den Baustein nicht erfasst, da sich hier die möglichen Schutzmaßnahmen darauf beschränken, den Zugang zum Sensor abzusichern und zu überwachen, ob er aktiv ist.

Auch behandelt der Baustein nicht den Schutz komplexer drahtloser Sensornetze. Er beschreibt lediglich, wie sich einzelne Sensoren absichern lassen. Weiterhin werden keine Sicherheitsanforderungen für Betriebs- und Steuerungstechnik beschrieben. Dafür muss der Baustein IND.1 *Betriebs- und Steuerungstechnik* umgesetzt werden.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Sensoren von besonderer Bedeutung:

### 2 1 Unzureichende Sicherheitsanforderungen bei der Beschaffung

Aus mangelndem Bewusstsein für die Risiken und aus Kostengründen wird bei der Beschaffung häufig die Informationssicherheit nicht berücksichtigt. Dadurch können in Sensoren mitunter schwerwiegende Schwachstellen enthalten sein, die sich später nur sehr aufwändig beheben lassen.

Sensoren für ICS-Komponenten in industriellen Umgebungen sind häufig besonderen Bedingungen ausgesetzt, die den sicheren Betrieb beeinträchtigen können. Beispiele hierfür sind extreme Wärme, Kälte, Feuchtigkeit, Staub, Vibration oder auch ätzend oder korrodierend wirkende Atmosphären. Häufig treten auch mehrere Faktoren gleichzeitig auf. Durch solche schädlichen Umgebungseinflüsse können die Sensoren von ICS-Komponenten schneller verschleißen und früher ausfallen oder fehlerhafte Werte messen. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Sensoren aufgeführt. Grundsätzlich ist der ICS-Informationssicherheitsbeauftragte (ICS-ISB) für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### IND.2.3.A1 Installation von Sensoren [ICS-Administrator, Wartungspersonal]

Sensoren MÜSSEN geeignet installiert werden. Die Sensoren MÜSSEN ausreichend robust und zuverlässig unter den vorgesehenen Umgebungsbedingungen (Klima, Staub, Vibration, Korrosion etc.) messen können.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Sensoren und Aktoren. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### IND.2.3.A2 Kalibrierung von Sensoren [Wartungspersonal]

Wenn notwendig, SOLLTEN Sensoren regelmäßig kalibriert werden. Die Kalibrierungen SOLLTEN geeignet dokumentiert werden. Der Zugang zur Kalibrierung MUSS geschützt sein, da eine bewusste Fehl-Kalibrierung eines Sensors zu einem Angriffsvektor werden kann.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### IND.2.3.A3 Drahtlose Kommunikation(C)

Bei erhöhtem Schutzbedarf SOLLTEN drahtlose Verwaltungsschnittstellen wie Bluetooth, WLAN oder NFC NICHT benutzt werden. Alle nicht benutzten Kommunikationsschnittstellen MÜSSEN deaktiviert werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Sensoren und Aktoren" finden sich unter anderem in folgenden Veröffentlichungen:

5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Sensoren und Aktoren" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.21 Manipulation von Hard- oder Software
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

