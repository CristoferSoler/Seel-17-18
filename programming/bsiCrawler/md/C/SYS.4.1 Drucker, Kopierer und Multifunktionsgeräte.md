1 Beschreibung
--------------

### 1.1 Einleitung

Obwohl sehr viele Informationen digital gespeichert sind, kann häufig auf Papierdokumente nicht verzichtet werden. Auch lesen oder bearbeiten viele Personen Dokumente lieber auf Papier als am Bildschirm. Drucker, Kopierer und Multifunktionsgeräte werden daher noch lange unverzichtbare Arbeitsmittel sein, die in so gut wie in allen Büros zu finden sind. 

Es ist es oft nicht effizient, jeden einzelnen Arbeitsplatz mit einem solchen Gerät auszustatten. Daher werden häufig zentrale Netzdrucker, Kopierer oder Multifunktionsgeräte eingesetzt, auf denen die Benutzer ihre Dokumente ausdrucken, einscannen oder vervielfältigen können. Da es einige Nachteile hat, wenn Aufträge vom Arbeitsplatz-PC direkt an einen Netzdrucker verschickt werden, setzen die meisten Institutionen zudem einen zentralen Druckserver ein, der die Aufträge annimmt und auf die verfügbaren Drucker verteilt. 

Dieser Baustein behandelt die Sicherheit von vernetzten Druckern, Kopierern, Multifunktionsgeräten, Druckservern und Dokumentenscannern. Als Multifunktionsgeräte werden dabei Geräte bezeichnet, die mehrere verschiedene papierverarbeitende Funktionen bieten, die also drucken, kopieren und scannen oder auch Fax-Dienste ermöglichen. 

### 1.2 Zielsetzung

Ziel des Bausteins ist es, zu beschreiben, wie Drucker, Kopierer und Multifunktionsgeräte sicher betrieben werden können, so dass weder Informationen über diese abfließenabfliessen können noch die Sicherheit der internen IT-Netze beeinträchtigt wird. 

### 1.3 Abgrenzung

Bei Druckservern kann es sich um gewöhnliche IT-Systeme handeln, die als entsprechende Server betrieben werden. In diesem Fall müssen betriebssystemspezifische Sicherheitsanforderungen für die Server umgesetzt werden, die dieser Baustein jedoch nicht beschreibt, sondern die in den Bausteinen SYS.1.1 *Allgemeiner Server* und den jeweiligen bBetriebssystem-spezifischen Server-Bausteinen zu finden sind. Auch werden keine Sicherheitsanforderungen für den Netzdienst Samba, mit dem Drucker in Netzen zentral bereitgestellt werden können, definiert. Hierfür ist der Baustein APP.3.4 *Samba* anzuwenden. 

Der vorliegende Baustein geht nicht auf Sicherheitsanforderungen für Clients ein, diese sind Bestandteil der Bausteine SYS.2.1 Allgemeiner Client und den jeweiligen betriebssystemspezifischen Client-Bausteinen.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich* Drucker, Kopierer und Multifunktionsgeräte* von besonderer Bedeutung:

### 2 1 Unzureichende oder falsche Versorgung mit Verbrauchsgütern

Viele Drucker, Kopierer und Multifunktionsgeräte benötigen für einen reibungslosen und unterbrechungsfreien Betrieb bestimmte Verbrauchsgüter in ausreichender Menge. Fehlen diese Verbrauchsgüter oder werden sie falsch eingesetzt, kann der Betriebsablauf empfindlich gestört werden. So kann beispielsweise ungeeignete Tinte einen Tintenstrahldrucker verunreinigen und zu Fehlfunktionen des Druckers führen. In Notfällen kann die Handlungsfähigkeit der Institution stark beeinträchtigt sein und es können hohe Folgekosten entstehen, zum Beispiel wenn sich wichtige Verträge nicht ausdrucken lassen. 

### 2 2 Unerlaubte Einsicht in ausgedruckte Dokumente

Bei Netzdruckern verbleiben oft ausgedruckte Dokumente eine längere Zeit im Ausgabefach. Besonders wenn sich die Drucker nicht im direkten Umfeld befinden, drucken die Benutzer häufig mehrere Dateien aus, bevor sie alle zusammen abholen. Da Etagen- oder Abteilungsdrucker von vielen Mitarbeitern benutzt werden, können so auch unberechtigte Personen Ausdrucke mit schützenswerten Informationen einsehen oder entwenden. Das muss nicht einmal böswillig geschehen: Wenn Mitarbeiter beispielsweise eine längere Zeitspanne auf ihren Ausdruck am Gerät warten müssen, werden sie eventuell die Wartezeit überbrücken und schauen, was andere Kollegen ausgedruckt haben. Auch an Kopierern finden sich immer wieder vertrauliche Dokumente, die dort beispielsweise im Einzug vergessen wurden. 

Benutzer suchen häufig nicht nach Ursachen, wenn sie ihre Ausdrucke sich nicht am Drucker finden. Stattdessen vermuten sie IT-Probleme und starten einen neuen Druckauftrag, da sie daran gewöhnt sind, dass mit der Hard- und Software immer wieder Probleme und auch unerklärliche Phänomene auftreten. Die Ausdrucke könnten allerdings auch von anderen mitgenommen worden sein. Ebenso kommt es häufig vor, dass Benutzer an ihrem Arbeitsplatz-Rechner versehentlich einen anderen Drucker ausgewählt haben. Typischerweise suchen dann die Benutzer ihre Ausdrucke am falschen Drucker, finden sie dort nicht und starten einfach einen neuen Druckauftrag, diesmal am Standard-Drucker. Dadurch finden sich an vielen Netzdruckern Fehlausdrucke, die nicht abgeholt werden.

### 2 3 Fehlerhafter Zugriffsschutz zur Administration

Bei einigen Druckern, Kopierern und Multifunktionsgeräten kann der Zugriff auf die Administrationsschnittstelle nicht abgesichert werden, also auch nicht über eine Passwortabfrage geschützt werden. Mit Administratorrechten könnte ein Angreifer die Geräte manipulieren. Das ist in einigen Fällen nicht nur von Arbeitsplätzen des lokalen Netzes möglich, sondern auch aus dem Internet. 

Viele Netzdrucker und Hochleistungskopierer haben eingebaute Webserver, um sie leichter administrieren zu können. Komfort wird hier aber mit zusätzlichen Risiken erkauft: So wird häufig die Webschnittstelle bei der Konfiguration vernachlässigt, sodass interne oder sogar externe Personen die Druckerkonfiguration und -nutzung manipulieren können. Beispielsweise könnten von beliebigen Benutzern absichtlich oder unbeabsichtigt Druckaufträge anderer gelöscht oder die Verfügbarkeit des Gerätes beeinträchtigt werden. Manche Webserver liefern außerdem Diagnosedaten zurück, wenn eine überlange URL angegeben wird. Mit diesen Informationen können Angriffe entwickelt werden. 

### 2 4 Missbrauch der Adressbuchfunktion

Verschiedene Hersteller haben auf Druckern, Kopierern und Multifunktionsgeräten eine Adressbuchfunktion für den integrierten E-Mail- oder Faxversand implementiert. Werden solche Funktionen benutzt, ist es schwierig auszuschließen, dass Daten über den Drucker unberechtigt weitergeleitet werden, z. B. ins Internet. 

### 2 5 Unverschlüsselte Druckerkommunikation

Drucker, Kopierer und Multifunktionsgeräte werden oft nicht lokal angesteuert, sondern über einen Netzanschluss. Der Druckertreiber des jeweiligen lokalen Rechners sendet dazu alle benötigten Informationen direkt an den Drucker oder an einen zentralen Druckerserver, der diese an einen Drucker weiterleitet. Diese Datenübertragung wird nur selten verschlüsselt. Dadurch könnte ein Angreifer direkt über das Netz mitlesen, was ausgedruckt wird.

Unverschlüsselte Kommunikationsschnittstellen zur Administration bilden eine weitere Gefahrenquelle. Bei einem Zugriff über HTTP oder Telnet werden die übertragenen Informationen ungeschützt transportiert. In dem Fall könnte ein Angreifer die Kommunikation und somit beispielsweise das Passwort zur Konfiguration mitlesen und es für Angriffe auf die Vertraulichkeit, Verfügbarkeit und Integrität benutzen.

### 2 6 Fehlende Netztrennung

Sicherheitsgateways zwischen LAN und Internet werden häufig so konfiguriert, dass der Internet-Zugriff für ganze Subnetze freigeschaltet ist. Andererseits werden Drucker, Kopierer und Multifunktionsgeräte oft dem gleichen Subnetz zugeordnet wie die Arbeitsplatz-PCs, von denen auf diesen Geräten gedruckt wird. Dadurch kann es passieren, dass z. B. auch die Netzdrucker auf das Internet zugreifen können. Wenn die Verbindungen von und zu den Druckern aus dem Internet nicht von den Sicherheitsgateways abgewiesen werden, können unter Umständen sensible Informationen unerwünscht das Netz verlassen. Umgekehrt könnte ein netzfähiges Gerät aber auch unerwünscht Daten aus dem Internet empfangen und eventuell weiter verteilen. Ein Netzdrucker kann dadurch z. B. zu einem Einfallstor für Angriffe aus dem Internet werden.

### 2 7 Beeinträchtigung von Gesundheit und Umwelt

Laserdrucker und Kopierer nutzen meist Trockentoner, der auf das Papier übertragen wird. Der staubförmige Toner enthält neben dem eigentlichen Farbstoff auch Schwermetalle wie Blei und Cadmium. Dieser Tonerstaub wird nicht komplett auf das Papier übertragen, sodass sich Reste davon im gesamten Raum verteilen können. Auch beim Austausch einer fast leeren Toner-Kartusche kann Toner austreten. So kann der feine gesundheitsgefährdende Tonerstaub eingeatmet werden und sich in der Lunge ablagern. Zusätzlich wird bei einigen Geräten im Betrieb Ozon freigesetzt. Moderne Geräte besitzen aber Filter, die die Freigabe von Ozon verringern.

### 2 8 Auswertung von Restinformationen

Viele Kopierer, Drucker und Multifunktionsgeräte sind mit einem umfangreichen internen Speicher ausgestattet. Wenn Informationen dort abgelegt wurden, können eventuell auch unberechtigte Personen hierauf zugreifen. Im einfachsten Fall ist es dabei lediglich möglich, das zuletzt gespeicherte Dokument auszudrucken. Problematischer ist es, wenn Angreifer den gesamten Speicher auslesen können, um dessen Inhalt zu analysieren.

Auch wenn die gespeicherten Informationen direkt nach der Verwendung gelöscht werden, könnten die gelöschten Daten rekonstruiert werden. Nicht jedes Gerät überschreibt die Daten zusätzlich zur Löschung noch einmal. 

Häufig werden digitale Kopierer oder Drucker nur gemietet. Nach einem vorher festgelegten Zeitraum wird das Gerät dann zurückgegeben und eventuell gegen ein aktuelleres ausgetauscht. Der Vermieter oder der nächste Besitzer des Geräts könnten so Zugriff auf noch vorhandene Informationen im Speicher erhalten.

### 2 9 Yellow Dots

Auf bestimmten Druckern und Kopierern werden auf das Papier sogenannte "Yellow Dots" (oder auch "Machine Identification Code, "tracking dots", "secret dots") gedruckt. Diese oft undokumentierten Wasserzeichen können das Datum und die Zeit sowie die Seriennummer des Druckers beinhalten und sind mit dem bloßen Auge kaum zu erkennen. Auf diese Weise kann ein Ausdruck direkt einer Institution oder sogar einem bestimmten Benutzer zugewiesen und so zum Verfasser zurückverfolgt werden. Neben datenschutzrechtlichen Auswirkungen könnten so ungewollt Informationen die Institution verlassen. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Drucker, Kopierer und Multifunktionsgeräte aufgeführt. Grundsätzlich ist der *IT-Betrieb* für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### SYS.4.1.A1 Erstellung eines Basis-Konzepts für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten [Leiter IT]

Bevor Drucker, Kopierer und Multifunktionsgeräte beschafft werden, MÜSSEN die Verantwortlichen ein Basis-Konzept für den sicheren Einsatz entwickeln. Darin MUSS geregelt sein, wo die Geräte aufgestellt werden dürfen, wer darauf zugreifen darf und wie sie vor Angriffen geschützt werden sollen.

#### SYS.4.1.A2 Geeignete Aufstellung von Druckern, Kopierern und Multifunktionsgeräten

Drucker, Kopierer und Multifunktionsgeräte SOLLTENMÜSSEN so aufgestellt werden, dass nur befugte Benutzer zu ihnen Zutritt haben. Zumindest SOLLTEN sie NICHT in Bereichen aufgestellt werden, in denen sich häufig Externe aufhalten, also nicht in der Nähe von Besprechungs-, Veranstaltungs- oder Schulungsräumen. Außerdem SOLLTENMÜSSEN die Benutzer dafür sensibilisiert werden, dass keine vertraulichen Dokumente an den Geräten liegengelassen werden sollten.

#### SYS.4.1.A3 Regelmäßige Aktualisierung

Es MUSS regelmäßig überprüft werden, ob die Drucker, Kopierer und Multifunktionsgeräte auf dem aktuellen Stand sind. Wenn Sicherheitslücken identifiziert werden, MÜSSEN diese so schnell wie möglich behoben werden. Vorhandene Patches und Updates MÜSSEN sofort eingespielt werden oder anderweitige Sicherheitsmaßnahmen ergriffen werden, wenn keine Patches zur Verfügung stehen. Generell MUSS darauf geachtet werden, dass Patches und Updates nur aus vertrauenswürdigen Quellen bezogen werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Drucker, Kopierer und Multifunktionsgeräte. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### SYS.4.1.A4 Planung des Einsatzes von Druckern, Kopierern und Multifunktionsgeräten [Leiter IT]

Aufbauend auf dem Konzept aus SYS.4.1.A1 Erstellung eines *Basis-Konzepts für den Einsatz von Druckern, Kopierern und Multifunktionsgeräten* SOLLTEN für die jeweiligen Teilkomponenten spezifische Sicherheitskonzepte entwickelt werden. Darin SOLLTEN beispielsweise allgemeine Fragen geregelt werden. Zum Beispiel: Sollen lokale oder netzfähige Drucker verwendet werden? Wer darf welche Funktionen benutzen? Welche Richtlinien soll es geben? Weiterhin SOLLTEN Aspekte geregelt werden wie 

* Dokumentenzugriff,
* Patchen der Geräte,
* Schutz der Geräte,
* Verfügbarkeit und
* Verschlüsselung (Speicher und Kommunikation).
Ebenso SOLLTE sichergestellt werden, dass der Speicher der Geräte gelöscht wird, nachdem sie verwendet wurden. Alle getroffenen Entscheidungen SOLLTEN nachvollziehbar dokumentiert werden.

#### SYS.4.1.A5 Erstellung von Benutzerrichtlinien für den Umgang mit Druckern, Kopierern und Multifunktionsgeräten

Für den sicheren Umgang mit Druckern, Kopierern und Multifunktionsgeräten MUSS eine Administratorenrichtlinie ausgearbeitet werden. Für Benutzer MUSS außerdem ein Merkblatt erstellt werden, auf dem die Sicherheitsrichtlinien für die Benutzer übersichtlich zusammengefasst sind. Das Merkblatt MUSS allen Benutzern bekannt gemacht werden. 

#### SYS.4.1.A6 Sicherer Einsatz von CUPS

Benutzt eine Institution das netzfähige Drucksystem Common Unix Printing System (CUPS), SOLLTE dessen Konfiguration den festgelegten Regelungen für Drucker, Kopierer und Multifunktionsgeräte entsprechen. Der administrative Zugriff auf den CUPS-Server SOLLTE beschränkt werden. Den Druckserver SOLLTEN (berechtigte) Benutzer nur zum Drucken nutzen können. 

#### SYS.4.1.A7 Beschränkung der Administrationszugriffe auf Drucker, Kopierer und Multifunktionsgeräte

Der Zugriff auf die Konfiguration von Druckern, Kopierern und Multifunktionsgeräten SOLLTE beschränkt werden. Wenn Administratoren die Geräte mittels Fernzugriff konfigurieren, SOLLTE das durch eine Authentisierung und eine verschlüsselte Verbindung geschützt werden. Ebenso SOLLTEN alle nicht benötigten Funktionen von Druckern, Kopierern und Multifunktionsgeräten abgeschaltet sein. 

#### SYS.4.1.A8 Versorgung und Kontrolle der Verbrauchsgüter [Innerer Dienst, Benutzer]

Drucker, Kopierer und Multifunktionsgeräte sind auf Verbrauchsgüter wie Papier oder Toner angewiesen, um funktionieren zu können. Die Versorgung mit diesen Verbrauchsgütern SOLLTE sichergestellt sein. Die Entsorgung der Verbrauchsgüter SOLLTE geregelt sein. Die Verantwortlichkeiten hierfür SOLLTEN geregelt und kommuniziert werden. 

#### SYS.4.1.A9 Protokollierung bei Druckern, Kopierern und Multifunktionsgeräten

Aktivitäten auf Druckern, Kopierern und Multifunktionsgeräten SOLLTEN protokolliert werden. Es SOLLTE abgestimmt sein, was protokolliert wird, wo dies gespeichert wird und wer dies in welchen Zeiträumen auswertet. Nur berechtigte Personen SOLLTEN auf die protokollierten Informationen zugreifen können. Wenn die Verantwortlichen die Protokolle auswerten, SOLLTEN dabei geltenden Gesetze und Vorschriften eingehalten werden, zum Beispiel zum Datenschutz. Unberechtigte SOLLTEN nicht auf die Protokolldaten zugreifen können. Zudem SOLLTE sichergestellt sein, dass alle Geräte eine korrekte Systemzeit haben. 

#### SYS.4.1.A10 Einsatz von netzfähigen Dokumentenscannern

Wenn netzfähige Scanner eingesetzt werden, SOLLTEN nur berechtigte Personen auf die digitalisierten Dokumente zugreifen können. Die gescannten Informationen SOLLTEN sicher zum Client des Erfassenden übertragen werden. Alle Speicherbereiche des Scanners SOLLTEN nach der Benutzung gelöscht werden. Beim Scannen SOLLTEN geeignete Bildkompressionsverfahren verwendet werden.

#### SYS.4.1.A11 Netztrennung beim Einsatz von Multifunktionsgeräten

Wenn eine Institution Multifunktionsgeräte einsetzt, die sich direkt an das Telefonnetz anschließen lassen, SOLLTE überprüft werden, ob die Fax- und Modem-Funktionalität der Geräte abgeschaltet werden kann. Wird diese Funktion doch benutzt, SOLLTEN unkontrollierte Datenverbindungen zwischen dem LAN und Fremdnetzen zuverlässig unterbunden werden. Netzfähige Drucker, Multifunktionsgeräte und auch Dokumentenscanner SOLLTEN in einem separaten Netzsegment angeschlossen werden, das insbesondere von externen Netzen getrennt ist.

#### SYS.4.1.A12 Ordnungsgemäße Entsorgung von schützenswerten Betriebsmitteln [Leiter Haustechnik, Benutzer]

Es SOLLTE sichergestellt und geregelt sein, dass alle schutzbedürftigen Betriebsmittel, die bei Druckern, Kopierern und Multifunktionsgeräten anfallen, ordnungsgemäß entsorgt werden. Damit Mitarbeiter schutzbedürftiges Material entsorgen können, SOLLTEN geeignete Entsorgungseinrichtungen vorhanden sein, z. B. Aktenvernichter. 

Wenn das Material erst gesammelt und später entsorgt wird, SOLLTE es vor unberechtigtem Zugriff geschützt sein. Die mit der Entsorgung beauftragten Unternehmen SOLLTEN regelmäßig daraufhin überprüft werden, ob der Entsorgungsvorgang verlässlich ist. 

#### SYS.4.1.A13 Sichere Außerbetriebnahme von Druckern, Kopierern und Multifunktionsgeräten

Bevor *Drucker, Kopierer und Multifunktionsgeräte* entsorgt, zurückgegeben oder ausgetauscht werden, SOLLTEN alle auf ihnen befindlichen Information sicher gelöscht werden. Auch SOLLTEN die Verantwortlichen überprüfen, ob die Speicherinhalte tatsächlich gelöscht sind.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.4.1.A14 Authentisierung bei Druckern, Kopierern und Multifunktionsgeräten(CI)

Es SOLLTEN Geräte mit einer Authentisierungsmöglichkeit eingesetzt werden. Diese Funktion SOLLTE aktiviert und genutzt werden. 

#### SYS.4.1.A15 Informationsschutz bei Druckern, Kopierern und Multifunktionsgeräten(CI)

Bei einem erhöhtem Schutzbedarf SOLLTEN die eingesetzten Drucker, Kopierer und Multifunktionsgeräte Informationen verschlüsselt abspeichern. Auch SOLLTEN Druckaufträge nur verschlüsselt an die Geräte übertragen werden. 

Weiterhin SOLLTE durch geeignete Mechanismen sichergestellt werden, dass sich gelöschte Daten aus dem Gerätespeicher nicht wiederherstellen lassen. Letztlich SOLLTEN auch Maßnahmen ergriffen werden, die es Angreifern erschweren, interne Speicherkomponenten von Druckern, Kopierern und Multifunktionsgeräten auszubauen. 

#### SYS.4.1.A16 Notfallvorsorge bei Druckern, Kopierern und Multifunktionsgeräten

Die Ausfallzeiten von Druckern, Kopierern und Multifunktionsgeräten SOLLTEN so gering wie möglich sein. Deshalb SOLLTEN bei höherem Schutzbedarf unter anderem

* Ersatzgeräte bereitstehen, 
* in Wartungsverträgen auf eine angemessene Reaktionszeit geachtet werden, 
* eine Liste mit Fachhändlern geführt werden, um schnell Ersatzgeräte oder -teile beschaffen zu können und 
* falls erforderlich, Ersatzteile gelagert werden, die häufig benötigt werden. 
4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Drucker, Kopierer und Multifunktionsgeräte" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ACSD] Datenschutz und Sicherheit in Druckinfrastrukturen

  

 mc² management consulting GmbH, 12.2016 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/partner/161219\_mc2\_drucker\_sicherheit.pdf](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/partner/161219_mc2_drucker_sicherheit.pdf)

 
* #### [CERT] Informationen zu Schwachstellen und Sicherheitslücken von Druckern und zugehörigen Diensten, Warn- und Informationsdienst

  

 CERT-Bund, (zuletzt abgerufen am 28.09.2017)   
 <https://www.cert-bund.de/search>

 
* #### [CSE015] Netzwerk-verbundene Bürogeräte

  

 CSE 015, V1.0, Allianz für Cyber-Sicherheit, 10.2012 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_015.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_015.html)

 
* #### [CSE069] Sichere Passwörter in Embedded Devices

  

 CSE 069, V1.0, Allianz für Cyber-Sicherheit vom 12.2013 [https://www.allianz-fuer-cybersicherheit.de/ACS/DE/\_/downloads/BSI-CS\_069.html](https://www.allianz-fuer-cybersicherheit.de/ACS/DE/_/downloads/BSI-CS_069.html)

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
* #### [PP0058] IEEE Standard Protection Profile for Hardcopy Devices in IEEE Std 2600-2008

  

 Operational Environment B, IEEE Std 2600.2-2009, IEEE Computer Society, Information Assurance (C/IA) Committee, BSI-CC-PP-0058-2010, 07.2010   
 [https://www.bsi.bund.de/SharedDocs/Zertifikate\_CC/PP/aktuell/PP\_0058.html](https://www.bsi.bund.de/SharedDocs/Zertifikate_CC/PP/aktuell/PP_0058.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Drucker, Kopierer und Multifunktionsgeräte" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.21 Manipulation von Hard- oder Software
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.37 Abstreiten von Handlungen
* G 0.39 Schadprogramme
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

