1 Beschreibung
--------------

### 1.1 Einleitung

Webanwendungen stellen Funktionen und dynamische Inhalte über das Internetprotokoll HTTP (Hypertext Transfer Protocol) bzw. HTTPS (HTTP über SSL/TLS, d. h. geschützt durch eine verschlüsselte Verbindung) zur Verfügung. Dazu werden auf einem Server Dokumente und Benutzeroberflächen (z. B. Bedienelemente und Eingabemasken) erzeugt und an entsprechende Clientprogramme (Web-Browser) ausgeliefert.

Webanwendungen werden gewöhnlich auf der Grundlage von Frameworks entwickelt. Diese stellen ein Rahmenwerk für häufig wiederkehrende Aufgaben zur Verfügung (z. B. für Sicherheitskomponenten). Für eine Webanwendung werden oft mehrere Frameworks für verschiedene Bereiche (z. B. Zugriff auf Datenbanken, Formatierung der Ausgaben) und Komponenten (z. B. Authentisierung, Session-Management) eingesetzt. 

Um eine Webanwendung zu betreiben, sind in der Regel mehrere IT-Systemkomponenten notwendig. Hierzu gehören üblicherweise ein Webserver zur Auslieferung der Daten, ein Applikationsserver für den Betrieb der Anwendung und zusätzliche Hintergrundsysteme, die als Datenquellen über unterschiedliche Schnittstellen angebunden sind (z. B. Datenbank oder Verzeichnisdienst). 

Mithilfe von Webanwendungen werden sowohl in öffentlichen IT-Netzen (z. B. dem Internet) als auch in Firmennetzen (Intranet) Daten und Anwendungen bereitgestellt. Dabei müssen Webanwendungen Sicherheitsmechanismen umsetzen, die den Schutz der Daten gewährleisten und Missbrauch verhindern.

Typische Sicherheitskomponenten bzw. -mechanismen einer Webanwendung sind:

* Authentisierung  
 Für den Zugriff auf geschützte Ressourcen der Webanwendung müssen sich die Benutzer gegenüber der Authentisierungskomponente ausweisen (z. B. durch Zugangsdaten).
* Autorisierung  
 Vor dem Zugriff auf geschützte Ressourcen und Funktionen muss geprüft werden, ob die Benutzer über ausreichend Rechte verfügen.
* Ein- und Ausgabevalidierung  
 Ein- und Ausgabedaten müssen geprüft und gefiltert werden, damit die Verarbeitung von schädliche Daten (z. B. ausführbarer Schadcode) vermieden wird.
* Session-Management  
 Da das Internetprotokoll HTTP keine Zuordnung zusammengehörender Anfragen zu einem Benutzer unterstützt, erfolgt diese Zuordnung durch das Session-Management der Webanwendung.
* Fehlerbehandlung  
 Auftretende Fehler müssen so behandelt werden, dass die Daten der Webanwendung auch im Fehlerfall geschützt werden.
* Protokollierung  
 Ereignisse müssen von der Webanwendung derart erfasst werden, dass durchgeführte Aktionen und sicherheitsrelevante Vorfälle auch zu einem späteren Zeitpunkt nachvollzogen werden können.
### 1.2 Lebenszyklus

**Planung und Konzeption**

Bei der Planung einer Webanwendung muss üblicherweise entschieden werden, ob die Anforderungen an die Webanwendung durch Standardprodukte abgedeckt werden können oder eine Eigenentwicklung notwendig ist. Wird eine Webanwendung auf Basis von Standardsoftware umgesetzt, so sind gewöhnlich Anpassungen erforderlich, die über reine Konfigurationsänderungen hinausgehen und oft auch Entwicklungsarbeiten einschließen. Daher müssen auch Webanwendungen, die auf Standardsoftware basieren, häufig die Vorgaben an die Entwicklung und Erweiterung von Webanwendungen erfüllen (siehe APP.3.1.M9* Beschaffung, Entwicklung und Erweiterung von Webanwendungen*).

Bereits in der Entwurfsphase einer Webanwendung müssen Sicherheitsaspekte beachtet werden, um die zu verarbeitenden Daten zu schützen (siehe APP.3.1.M8 *Systemarchitektur einer Webanwendung*). Hierbei müssen auch die Integration der Hintergrundsysteme (z. B. Datenbank) und deren sichere Anbindung einbezogen werden (siehe APP.3.1.M11 *Sichere Anbindung von Hintergrundsystemen*).

Werden personenbezogene Daten von Webanwendungen verarbeitet, aufgezeichnet oder ausgewertet (z. B. Nutzerverhalten), sind die rechtlichen Rahmenbedingungen bei der Planung von technischen Lösungen zu berücksichtigen (siehe APP.3.1.M17 *Kontrolle der Protokolldateien*).

**Beschaffung**

Soll eine Webanwendung mit verfügbarer Standardsoftware realisiert werden, muss ein passendes Produkt ausgewählt werden (siehe *APP.3.1.M9 Beschaffung, Entwicklung und Erweiterung von Webanwendungen*).

**Umsetzung**

Bevor eine Webanwendung in den Wirkbetrieb übernommen wird, müssen die Sicherheitsfunktionen konfiguriert. Die dafür umzusetzenden Komponenten müssen die Webanwendung vor bekannten Bedrohungen und Angriffstechniken schützen (siehe z. B. APP.3.1.M18 *Schutz gegen SQL-Injection*).

Darüber hinaus sind die kontextbezogene Validierung und Filterung der Daten (siehe APP.3.1.M1 *Authentisierung bei Webanwendungen*) und der Schutz von Benutzer-Sitzungen durch das Session-Management (siehe APP.3.1.M3 *Sicheres Session-Management*) wesentliche Sicherheitskomponenten einer Webanwendung.

**Betrieb**

Nachdem eine Webanwendung das Abnahme- und Freigabeverfahren erfolgreich durchlaufen hat und betriebsbereit konfiguriert wurde, kann der Regelbetrieb aufgenommen werden.

Insbesondere bei der Nutzung einer Webanwendung über öffentliche Netze (z. B. Internet) besteht die Gefahr, dass bekannt gewordene Schwachstellen ausgenutzt werden. Daher müssen Prozesse definiert werden, um das angestrebte Sicherheitsniveau der Webanwendung dauerhaft aufrechterhalten zu können (siehe APP.3.1.M6 *Zeitnahes Einspielen sicherheitsrelevanter Patches und Updates*).

Es muss sichergestellt werden, dass von Webanwendungen übermittelte Daten keine sicherheitsrelevanten Informationen beinhalten, die einem Angreifer Hinweise zur Umgehung von Sicherheitsmechanismen geben (siehe APP.3.1.M14* Schutz vertraulicher Daten*).

Für den hohen Schutzbedarf sind Penetrationstests auf die Webanwendung durchzuführen, um das Sicherheitsniveau der Webanwendung zu überprüfen und mögliche Schwachstellen schnell abzustellen (APP.3.1.M21 *Durchführung von Penetrationstests*).

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Webanwendungen" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### APP.3.1.M1 Authentisierung bei Webanwendungen [Entwickler]

Sollen eine Webanwendung oder Teile davon ausschließlich von einem eingeschränkten Benutzerkreis genutzt werden können, so müssen sich die Benutzer gegenüber der Anwendung authentisieren. Dafür können unterschiedliche Methoden verwendet werden, die zum Beispiel im Abschnitt *Auswahl einer Authentisierungsmethode* beschrieben ist.

Bei der Umsetzung von Authentisierungsmechanismen für Webanwendungen sind folgende Punkte zu berücksichtigen:

**Anforderungen an die Authentisierungskomponente **

Die Authentisierungslogik sollte nur an einer Stelle und nicht mehrfach im Programmcode realisiert werden. Treten während der Authentisierung Fehler auf, sollte die angeforderte Aktion abgebrochen und die Anfrage zurückgewiesen werden.

Die Authentisierungskomponente sollte sichere Passwörter gemäß einer Passwort-Richtlinie erzwingen können. Anforderungen an sichere Passwörter können dem Abschnitt *Regelung des Passwortgebrauchs* entnommen werden.

Darüber hinaus wird empfohlen, die geschätzte Stärke des eingegebenen Passworts einzublenden (z. B. schwach, mittel, sicher). Dadurch wird der Benutzer dabei unterstützt, sichere Passwörter zu wählen.

Um Fehler bei der Entwicklung der Authentisierungskomponente zu vermeiden, wird empfohlen sie auf Basis etablierter Standardkomponenten (Bibliotheken oder Frameworks) umzusetzen (z. B. *Enterprise Security API* der OWASP).

Besteht ein erhöhter Schutzbedarf der Webanwendung, sollte eine Zwei-Faktor-Authentisierung eingesetzt werden.

Damit ein Benutzer den Missbrauch seines Benutzerkontos erkennen kann, sollte die Webanwendung das Datum und die Uhrzeit der letzten erfolglosen und erfolgreichen Anmeldeversuche nach der Anmeldung eines Benutzers als Warnhinweis anzeigen.

**Auswahl einer Authentisierungsmethode**

Das Protokoll HTTP/1.1 sieht zwei verschiedene Methoden zur Benutzerauthentisierung vor.

Die erste Methode ist die so genannte Basic-Access-Authentisierung. Dabei sendet der Client den Benutzernamen und das Passwort Base64-kodiert im sogenannten Authorization Header des HTTP-Requests an den Server. Base64 ist eine Methode zur Kodierung von Binärdaten in 7-Bit ASCII, die hier zur Übertragung von Sonderzeichen über die HTTP-Schnittstelle genutzt wird. Das Passwort ist somit zwar nicht auf den ersten Blick ablesbar, kann aber von einem potenziellen "Lauscher" problemlos ermittelt werden, da es unverschlüsselt ist. Daher ist dieser Authentisierungstyp allenfalls für sehr geringe Vertraulichkeitsanforderungen zu gebrauchen.

Die zweite Methode zur HTTP-Authentisierung ist die Digest-Authentisierung. Bei dieser Art der Authentisierung muss auf dem Server das Passwort des Benutzers im Klartext vorliegen. Der Client erhält vom Server einen Zufallsstring, die sogenannte Challenge. Aus dieser Challenge und dem Passwort des Benutzers errechnet der Client nach einem standardisierten Verfahren einen sogenannten Digest, der dann zur Authentisierung an den Server gesandt wird. Da der Server sowohl über den von ihm generierten Zufallsstring, als auch über das Passwort des Benutzers verfügt, kann er den Digest ebenfalls berechnen und so die Authentisierung durchführen. Da bei der Digest-Authentisierung das Passwort nicht über das Netz verschickt wird, eignet sich diese Methode für einen etwas höheren Schutzbedarf.

Ein Problem bei der Verwendung der oben genannten Authentisierungsmethoden ist die Sicherheit der Passwortdaten auf dem Server: Bei der Digest-Authentisierung müssen die Authentisierungsdaten der Benutzer auf dem Webserver im Klartext vorhanden sein. Bei der Basic-Authentisierung wird meist ein Hash-Wert des Passwortes gespeichert. Eine Sicherung der Passwortdateien auf dem Server vor unbefugtem Zugriff ist daher besonders wichtig.

Neben der HTTP-Authentisierung existiert ein weiterer Weg, den Zugriff über das HTTP-Protokoll zu kontrollieren: Die Authentisierung wird dabei nicht über den Webserver selbst, sondern über eine serverseitige Anwendung durchgeführt. Dabei werden Benutzername und Passwort über normale HTML Formulare eingegeben und von der Anwendung überprüft. Es sollte jedoch stets beachtet werden, dass Passwörter oder PINs, die im Klartext über das Internet übertragen werden, leicht mitgelesen werden können. Zudem werden natürlich auch sämtliche Daten, selbst wenn sie auf authentisierte Anfragen hin ausgeliefert werden, unverschlüsselt übermittelt.

Manche Webangebote identifizieren die Benutzer über spezielle Cookies, die im Browser gespeichert werden. Da Cookies bei der Verwendung von HTTP ebenfalls im Klartext übertragen werden, ist diese Methode für die Authentisierung beim Zugriff auf schutzbedürftige Informationen ebenfalls nicht geeignet. Da im Zusammenhang mit Cookies noch weitere Sicherheitsprobleme existieren, sollte diese Methode generell nicht verwendet werden. 

**Benutzerauthentisierung über SSL/TLS **

Die Authentisierungsdaten sollten grundsätzlich verschlüsselt werden, siehe APP.3.1.A14 *Schutz vertraulicher Daten*. Eine häufig verwendete Methode der Benutzerauthentisierung für Webangebote ist die Kombination von formularbasierter Authentisierung und SSL/TLS-verschlüsselter Datenübertragung. Diese Methode bietet, wenn die gewählte SSL/TLS-Verschlüsselung ausreichend stark gewählt wird, bei vertretbarem Aufwand (Benutzerverwaltung in der Webanwendung und Implementierung eines SSL/TLS-geschützten Zugriffs auf den Webserver) ein Sicherheitsniveau, das auch für höhere Sicherheitsanforderungen angemessen ist.

Die folgende Tabelle fasst die verschiedenen Möglichkeiten der Benutzerauthentisierung bei Webservern zusammen.

Tabelle: Benutzerauthentisierung bei Webservern

Der Microsoft-Internet-Information-Server bietet darüber hinaus noch eine weitere Methode, bei der die Windows-Benutzeranmeldung benutzt wird. Diese Methode funktioniert allerdings nur mit dem Microsoft Internet Explorer als Client.

**Remember-Me-Funktion**

Um die Benutzerfreundlichkeit zu verbessern, werden die Authentisierungsdaten von Webanwendungen teilweise dauerhaft auf den Clients der Benutzer gespeichert (z. B. innerhalb eines Cookies im Webbrowser). Diese Möglichkeit wird häufig als Remember-Me-Funktion bezeichnet. Wurden Authentisierungsdaten im Rahmen der Remember-Me-Funktion auf dem Client gespeichert, werden diese bei einer späteren Nutzung der Webanwendung automatisch übertragen. Der Benutzer muss somit keine Zugangsdaten mehr eingeben.

Erhält ein Angreifer Zugriff auf den Webbrowser oder wird Schadcode auf dem Client ausgeführt, können diese gespeicherten Authentisierungsdaten ausgelesen werden. Aus diesem Grund sollte diese Funktion vermieden werden. Kann auf die Remember-Me-Funktion jedoch nicht verzichtet werden, so sollte der Benutzer explizit einer Aktivierung zustimmen müssen (Opt-In). Darüber hinaus sollte der Benutzer auf die Risiken der Funktion hingewiesen werden.

Neben Authentisierungsdaten in Cookies können aktuelle Browser häufig Formularfelder (z. B. Benutzername/Passwort oder Adressdaten) für eine spätere Wiederverwendung speichern. Wird ein Web-Formular, für das die eingegebenen Daten zuvor gespeichert wurden, erneut aufgerufen, so werden die Daten automatisch vom Browser in die Felder eingetragen. Daher sollte die Option *autocomplete=off* für alle Formularfelder mit vertraulichen Daten gesetzt werden. Dadurch werden die Browser angewiesen, die Daten der entsprechenden Formularfelder nicht zu speichern.

**Zusätzliche Authentisierung bei kritischen Funktionen**

Hat sich ein Benutzer erfolgreich authentisiert, so wird ihm von der Webanwendung üblicherweise eine eindeutige Sitzung (mittels Session-ID) zugewiesen. Die Webanwendung kann mithilfe dieser Session-ID die eintreffenden Requests den angemeldeten Benutzern zuordnen. Somit kann die Session-ID als eine Art temporäres Anmeldedatum betrachtet werden, mit dessen Hilfe auf die Sitzungen angemeldeter Benutzer zugegriffen werden kann (siehe auch APP.3.1.M3 *Sicheres Session-Management*). 

Da die Session-ID oft angegriffen wird, lässt sich nicht vollständig ausschließen, dass ein Angreifer sie nicht bereits übernommen hat. Daher sollte bei sicherheitskritischen Aktionen (z. B. Änderung des Passworts oder Löschung des kompletten Datenbestandes) eine erneute Authentisierung des Benutzers (z. B. durch Eingabe des alten Passworts bei einem Passwortwechsel) erfolgen.

**Grenzwerte für gescheiterte Anmeldeversuche**

Versucht ein Benutzer sich mehrfach in kurzen Zeitabständen an der Webanwendung anzumelden, so sollten diese Authentisierungsversuche als Angriff gewertet werden. Wenn die Zahl der fehlgeschlagenen Versuche einen festgelegten Wert überschreitet (z. B. fünf Fehlversuche), sollte das Benutzerkonto für ein definiertes Zeitintervall (z. B. 10 Sekunden) gesperrt werden. Darüber hinaus können die Zeitintervalle zur Sperrung des Benutzerkontos mit der Anzahl der Fehlversuche progressiv ansteigen. Hierdurch soll verhindert werden, dass Benutzer unbefugt Kennwörter anderer Benutzer erraten.

Bei der Wahl des Grenzwerts und der Zeitintervalle sollte beachtet werden, dass dieser Mechanismus für Denial-of-Service-Angriffe missbraucht werden kann. Ein Angreifer kann bewusst das Sperren vieler Benutzerkonten provozieren und somit diese Benutzer von der Nutzung der Webanwendung ausschließen.

**Automatisiertes Zurücksetzen von Authentisierungsdaten**

Da Webanwendungen oftmals von einem großen Benutzerkreis genutzt werden, bieten sie häufig Funktionen zum automatisierten Zurücksetzen der Authentisierungsinformationen (Passwort-Reset) an. So soll der administrative Aufwand möglichst gering gehalten werden, wenn z. B. ein Benutzer sein Passwort vergessen hat. Können die Authentisierungsdaten unbefugt zurückgesetzt werden, kann auf diese Weise der Authentisierungsmechanismus umgangen werden. Deshalb ist darauf zu achten, dass alle Funktionen einer Webanwendung zur Änderung der Authentisierungsdaten mindestens genauso abgesichert sind wie die primäre Authentisierung.

Wird beispielsweise im Prozess zum Zurücksetzen des Passworts die Authentisierung des Benutzers über eine geheime Frage mit entsprechender Antwort sichergestellt, so sollten die Merkmale vom Benutzer formuliert werden können. Er sollte darauf hingewiesen werden, dass sie keine Daten beinhalten sollten, die öffentlich verfügbar oder leicht zu erraten sind. Um das Schutzniveau zu erhöhen, können mehrere Fragen und Antworten bei der Registrierung aufgenommen werden (z. B. fünf, von denen mindestens drei Fragen für eine erfolgreiche Authentisierung richtig beantwortet werden müssen).

Zusätzlich kann noch ein weiteres Sicherheitsmerkmal verwendet werden, indem nach der korrekten Beantwortung der Fragen ein Link an eine zuvor vom Benutzer spezifizierte E-Mail-Adresse versendet wird oder ein weiteres Sicherheitstoken (z. B. eine PIN) per SMS an eine hinterlegte Rufnummer gesendet wird. Erst nachdem der Benutzer auf den Link klickt bzw. die PIN eingibt, kann er sich dann anmelden.

Da das Authentisierungsverfahren beim Zurücksetzen von Anmeldeinformationen in der Regel nur schwer auf das gleiche Sicherheitsniveau wie bei der primären Authentisierung zu bringen ist, sollte auf ein automatisiertes Zurücksetzen durch die Webanwendung verzichtet werden. Bei eingeschränkten Nutzerkreisen der Webanwendung (z. B. bei einer Webanwendung im Intranet) kann stattdessen das Passwort manuell beispielsweise über eine Hotline mit sicheren Authentisierungsmerkmalen und entsprechendem Freigabeverfahren zurückgesetzt werden. Insbesondere bei einem hohen Schutzbedarf ist dieses Verfahren zu bevorzugen.

**Regelung des Passwortgebrauchs**

Für Webanwendungen, die Passwörter zur Authentisierung verwenden, muss eine Regelung zum Passwortgebrauch eingeführt werden. Die Benutzer müssen darauf hingewiesen werden. Vorgaben für die Passwortgestaltung finden sich ORP.4 Identitäts- und Berechtigungsmanagement. Für Webanwendungen haben sich folgende Regeln zur Passwortgestaltung bewährt:

Ein Passwort sollte aus Großbuchstaben, Kleinbuchstaben, Sonderzeichen und Zahlen bestehen. Es sollten mindestens zwei dieser Zeichenarten verwendet werden.

* Wenn für das Passwort alphanumerische Zeichen gewählt werden können, sollte es mindestens 8 Zeichen lang sein. 
* Die Benutzer sollten regelmäßig angehalten werden, das Passwort zu wechseln, z. B. alle 180 Tage.
* Die Wiederholung alter Passwörter beim Passwortwechsel sollte vom IT-System verhindert werden (Passworthistorie).
* Die Wahl von Trivialpasswörtern (z. B. *BBBBBBBB*, *123456, Namen, Geburtsdaten*) sollte verhindert werden.
* Jeder Benutzer muss sein eigenes Passwort jederzeit ändern können.
* Die Benutzer sollten bei der Änderung von Passwörtern durch eine Entropie-Messung (Anzeige der Passwort-Güte) unterstützt werden.
* Für die Erstanmeldung neuer Benutzer sollten Initial-Passwörter vergeben werden, die nach einmaligem Gebrauch gewechselt werden müssen. 
* Erfolglose Anmeldeversuche sollten mit einer kurzen Fehlermeldung ohne Angabe von näheren Einzelheiten abgelehnt werden. Insbesondere darf bei erfolglosen Anmeldeversuchen nicht erkennbar sein, ob der eingegebene Benutzername oder das eingegebene Passwort (oder beides) falsch sind. Nach fünf aufeinanderfolgenden fehlerhaften Passworteingaben für dieselbe Kennung sollte das Authentisierungssystem den Zugang hierfür sperren (für eine bestimmte Zeitspanne oder dauerhaft). Wenn die Webanwendung eine Kennung sperrt, darf dies bei nachfolgenden erfolglosen Anmeldeversuchen ebenfalls nicht erkennbar sein, sondern sollte dem jeweiligen Benutzer auf einem separaten Weg mitgeteilt werden.
* Bei der Authentisierung in vernetzten Systemen sollten Passwörter selbst im Intranet nicht unverschlüsselt übertragen werden. Erfolgt die Authentisierung über ein ungesichertes Netz hinweg, so dürfen Passwörter keinesfalls unverschlüsselt übertragen werden.
* Bei der Eingabe sollte das Passwort nicht auf dem Bildschirm angezeigt werden.
**Zurücksetzen von Passwörtern**

Es kommt regelmäßig vor, dass Benutzer ihre Authentisierungsinformationen oder -token vergessen oder verlieren. Daher muss für jede Webanwendung ein angemessenes Verfahren vorhanden sein, um Benutzern schnell wieder Zugriff geben zu können, aber hierdurch keine Sicherheitslücken zu öffnen. Je nach Art der gewählten Authentisierungsverfahren und abhängig vom Schutzbedarf gibt es verschiedene Möglichkeiten, Passwörter zurückzusetzen oder Token freizuschalten, siehe ORP.4 Identitäts- und Berechtigungsmanagement.

#### APP.3.1.M2 Zugriffskontrolle bei Webanwendungen [Entwickler]

Eine Zugriffskontrolle muss auf allen Ebenen einer Webanwendung (z. B. durch die Webanwendung, den Applikationsserver, den Webserver und das Betriebssystem) umgesetzt werden. Demzufolge sollten neben einem Zugriffsschutz auf Webanwendungs-Ebene die Anforderung APP.3.1.M11 *Sichere Anbindung von Hintergrundsystemen* für den Zugriffsschutz von Daten in Hintergrundsystemen berücksichtigt werden.

Folgende Punkte sollten für eine sichere Zugriffskontrolle auf Webanwendungs-Ebene berücksichtigt werden:

**Generelle Aspekte**

Arbeiten mit einer Webanwendung mehrere Benutzer, so müssen die Zugriffsrechte ordnungsgemäß administriert und verwaltet werden. 

Jeder Zugriff auf geschützte Inhalte und Funktionen muss kontrolliert werden, bevor er ausgeführt wird. Dies gilt auch dann, wenn beispielsweise der gleiche Benutzer auf eine geschützte Ressource wiederholt zugreift. Auch automatisierte Client-Requests durch Web-Technologien (z. B. Ajax) sollten als unabhängige Requests behandelt und entsprechend kontrolliert werden.

**Vergabe von Zugriffsrechten**

Über Zugriffsrechte wird geregelt, welche Person im Rahmen ihrer Funktion bevollmächtigt wird, Webanwendungen zu nutzen. Die Zugriffsrechte (z. B. Lesen, Schreiben, Ausführen) auf Webanwendungen, Teilanwendungen oder Daten sind von der Funktion abhängig, die die Person wahrnimmt. Dabei dürfen immer nur so viele Zugriffsrechte vergeben werden wie für die Aufgabenwahrnehmung notwendig sind (*Need-to-know-Prinzip*). Umgesetzt werden müssen die Zugriffsrechte durch die Rechteverwaltung der Anwendung.

Viele Webanwendungen lassen es zu, dass verschiedene Rechte als Gruppenrechte bzw. als Rechteprofil definiert werden (z. B. Gruppe *Datenerfassung*). Diese Definition entspricht der technischen Umsetzung der Rechte, die einer Funktion zugeordnet werden. Um Zugriffsrechte effizient administrieren zu können, ist es vorteilhaft, solche Gruppen oder Profile zu erstellen.

Die Festlegung und Veränderung von Zugriffsrechten ist vom jeweils Verantwortlichen zu veranlassen und zu dokumentieren (siehe auch ORP.4 Identitäts- und Berechtigungsmanagement). 

**Dokumentation der zugelassenen Benutzer und Rechteprofile**

Es muss eine Dokumentation der für die Webanwendung zugelassenen Benutzer, angelegten Benutzergruppen und Rechteprofile erfolgen (siehe auch ORP.4 Identitäts- und Berechtigungsmanagement). 

Die Dokumentation der zugelassenen Benutzer und Rechteprofile muss regelmäßig (mindestens alle 6 Monate) daraufhin überprüft werden, ob sie den tatsächlichen Stand der Rechtevergabe widerspiegelt und ob die Rechtevergabe noch den Sicherheitsanforderungen und den aktuellen Aufgaben der Benutzer entspricht. Die vollständige Dokumentation ist Voraussetzung für Kontrollen der vergebenen Benutzerrechte. 

**Anforderungen an die Autorisierungskomponente**

Die Nutzung von Webanwendungen erfolgt gewöhnlich über einen generischen Client, der nicht unter der Kontrolle der Webanwendung steht. Damit kann ein Angreifer die Anfrage grundsätzlich beliebig manipulieren und clientseitig umgesetzte Sicherheitsmechanismen umgehen. Aus diesem Grund muss die Autorisierung serverseitig auf einem vertrauenswürdigen IT-System umgesetzt werden.

Die Autorisierungskomponente muss alle verwalteten Ressourcen einer Webanwendung berücksichtigen. Dazu zählen z. B. URLs, Dateien, Objektreferenzen, Geschäftsfunktionen, Anwendungsdaten, Konfigurationsdaten und Protokolldaten.

Die Routinen zur Autorisierung sollten zentral an einer Stelle und nicht verteilt im Programmcode der Webanwendung umgesetzt werden. Auf diese Weise wird der Code der Autorisierungskomponente von der Geschäftslogik der Webanwendung getrennt und eine redundante und fehleranfällige Umsetzung vermieden. Bei der Entwicklung der Autorisierungskomponente sollte auf Funktionen aus bereits existierenden Frameworks zurückgegriffen werden.

Kommt es zu Fehlern während der Zugriffskontrolle (z. B. weil unzureichende Informationen für die Autorisierung verwendet werden), müssen Zugriffe abgelehnt werden. Im Fehlerfall dürfen keine angeforderten Ressourcen übermittelt oder Funktionen unkontrolliert ausgeführt werden.

**Kontrolle aller beteiligten Ressourcen an einer Aktion**

Es darf einem Benutzer nicht möglich sein, eine Aktion auf eine Ressource durchzuführen, für die er keine ausreichenden Rechte hat. Falls z. B. ein authentisierter Benutzer einen URL-Parameter für die Zuordnung zu einem Bankkonto ändert, darf dieser dadurch keinen Zugriff auf ein fremdes Bankkonto erlangen. Werden die Rechte zur Durchführung einer Aktion geprüft, sollten daher ebenso alle an der Aktion beteiligten Ressourcen mit überprüft werden.

Dies betrifft ebenfalls die Umsetzung und Konfiguration der Suchfunktion einer Webanwendung. Es sollte darauf geachtet werden, dass zugriffsgeschützte Ressourcen einem unbefugten Benutzer nicht als Suchergebnis präsentiert werden. Bevor die Webanwendung die Suchergebnisse ausgibt, sollte daher beispielsweise geprüft werden, ob der Benutzer über ausreichende Rechte verfügt, um diese zu betrachten.

**Zugriffskontrolle bei URL-Aufrufen und Objekt-Referenzen**

Webseiten und andere Ressourcen der Webanwendung werden gewöhnlich über die URL identifiziert und abgerufen. Dabei ruft ein Benutzer Webseiten oder Funktionen der Webanwendung in der Regel über die angezeigten Verlinkungen auf einer bereits dargestellten Webseite der Anwendung auf.

Wenn Ressourcen der Webanwendung geschützt werden sollen, ist es nicht ausreichend, den Link auf die Ressource aus den angezeigten Webseiten zu entfernen (z. B. ein Link auf die Administrationsseite), sondern es muss auch der direkte Aufruf der Ressource über die URL geschützt werden.

Die Seiten von Webanwendungen werden häufig dynamisch anhand von Referenzen auf Objekte (z. B. die ID eines Datenbankeintrags) erstellt. Werden diese Referenzen durch die Benutzer der Webanwendung übergeben (z. B. als Parameter in der URL), kann der Parameter und somit die Referenz von einem Benutzer beliebig geändert werden.

Da es sich hierbei nicht um direkte Referenzen (z. B. auf Dateien), sondern um indirekte Referenzen (Verweise auf Objekte) handelt, sollte eine Zugriffskontrolle anhand der Referenzwerte (z. B. IDs) erfolgen. Des Weiteren sollte nach Möglichkeit eine zusätzliche Zugriffskontrolle für die angeforderten Objekte in den Hintergrundsystemen durchgeführt werden. Dies kann beispielsweise durch das Durchreichen der Benutzerauthentisierung an die Hintergrundsysteme realisiert werden (siehe auch APP.3.1.M11 *Sichere Anbindung von Hintergrundsystemen*).

**Restriktive Dateisystemberechtigungen bei der Upload-Funktion**

Grundsätzlich muss der Zugriff auf Dateien durch die Benutzer der Webanwendung durch restriktive Dateisystemberechtigungen beschränkt werden (siehe APP.3.1.M12 *Sichere Konfiguration von Webanwendungen*).

Stellt die Webanwendung eine Funktionalität zum Hochladen von Dateien bereit, darf nach dem erfolgten Hochladevorgang ausschließlich der Besitzer die Dateisystemberechtigung für den Zugriff auf die erstellten Dateien haben. In einem weiteren Schritt kann der Zugriff auf die Dateien explizit für andere Benutzer freigegeben werden. Generell ist darauf zu achten, dass hochgeladenen Dateien keine Ausführungsrechte haben, sodass ein Angreifer hierüber keinen Schadcode ausführen kann (siehe auch APP.3.1.M4 *Kontrolliertes Einbinden von Daten und Inhalten bei Webanwendungen*).

**Schutz temporärer Dateien **

Bei dynamisch erstellten Webseiten werden häufig temporäre Daten (z. B. Auswertungsgrafiken, Berichte) erzeugt. Handelt es sich dabei um schützenswerte Daten, so sollten diese nicht im Dateisystem zwischengespeichert werden. Stattdessen sollten die Daten direkt an den Benutzer ausgeliefert werden. Falls die zu schützenden Daten in temporären Dateien gespeichert werden müssen, sollten folgende Punkte berücksichtigt werden:

* Die Zugriffsberechtigungen im Dateisystem sind restriktiv zu setzen, sodass der Zugriff nur befugten Benutzern und Diensten möglich ist.
* Dateinamen sollten sich aus Zufallswerten zusammensetzen (z. B. einem Globally Unique Identifier (GUID)), sodass sie nicht leicht erraten werden können.
* Sobald die Daten nicht mehr benötigt werden, sollten sie zeitnah gelöscht werden.
* Es wird empfohlen, die Dateien in einem Verzeichnis zu speichern, das nicht über den Webserver erreichbar ist (z. B. außerhalb des Wurzelverzeichnisses des Webservers).
* Der Zugriff auf die Dateien sollte ausschließlich über solche Schnittstellen der Webanwendung möglich sein, die ausreichende Sicherheitsmechanismen bei der Zugriffskontrolle und Protokollierung umsetzen.
#### APP.3.1.M3 Sicheres Session-Management [Entwickler]

Webanwendungen verwenden in der Regel das zustandslose Protokoll HTTP, um Daten zu übertragen. Anfragen, die von einem Benutzer generiert werden, werden diesem nicht zugeordnet, wie zum Beispiel einzelne Seitenaufrufe zur Füllung eines virtuellen Warenkorbs. Um zusammengehörende Anfragen eines Benutzers zu erkennen und einer Sitzung zuzuordnen, wird eine Session-ID (zum Beispiel nach erfolgreicher Anmeldung) vergeben, die anschließend bei jedem Seitenaufruf übertragen wird. Die Session-ID wird typischerweise von der Webanwendung selbst erzeugt.

Wenn sich der Benutzer bei der Webanwendung angemeldet hat, ist die Session-ID vergleichbar mit seinen Zugangsdaten. Die Webanwendung identifiziert mit ihr bei jedem Seiten- oder Dienstaufruf den Benutzer und ordnet ihn einer (falls erforderlich privilegierten) Sitzung zu. Nutzen Unbefugte die Session-ID, werden sie als legitime Benutzer identifiziert und können die Anwendung oder den Dienst im Namen des Opfers verwenden.

Das Session-Management einer Webanwendung hat zur Aufgabe, die Sitzungen zu verwalten und neue Session-IDs zu vergeben. Dabei sollten die folgenden Anforderungen und Aspekte berücksichtigt werden.

**Anforderungen an die Session-ID**

Es ist zu beachten, dass die Gültigkeitsdauer einer Session-ID (siehe auch Abschnitt „Beschränkte Sitzungsdauer“) deutlich kleiner sein sollte als die Zeit, die ein Angreifer benötigt, um die Session-ID zu erraten. Dies kann mit einer Formel für eine Webanwendung individuell bewertet werden (siehe [GSSID]).

Die Session-ID sollte mindestens folgende Anforderungen erfüllen:

* Die Session-ID muss mithilfe kryptografischer Zufallszahlengeneratoren zufällig erzeugt werden und sollte eine Entropie von mindestens 64 Bit haben, damit sie von einem potenziellen Angreifer nicht erraten werden kann. Um die Entropie der Session-ID zu erhöhen, kann die Länge erhöht (zum Beispiel 128 Bit) und der Zeichenraum der Session-ID (zum Beispiel alphanumerische Zeichen und Sonderzeichen) vergrößert werden. Als Richtwert sollte hierbei die Länge der Session-ID mindestens die doppelte Anzahl an Bits haben wie die Anzahl an Entropie-Bits der Session-ID. Demzufolge sollte die Session-ID mindestens 128 Bit lang sein. Unter der Annahme, dass ein Zeichen durch 8 Bit dargestellt wird, bestünde eine solche Session-ID aus mindestens 16 Zeichen (128 Bit / 8 = 16 Byte).
* Es sollten keine extern bekannten oder erratbaren Daten (zum Beispiel IP-Adresse, Uhrzeit) in die Berechnung der Session-ID einfließen, sofern dies die Entropie nicht tolerierbar verringert.
* Unterstützt das der Webanwendung zugrunde liegende Framework die Generierung von Session-IDs, sollte vorzugsweise die Funktion des Frameworks verwendet werden. Die Funktionalität von führenden Frameworks ist in der Regel getestet und unterstützt die sichere Erzeugung von Session-IDs. Eine fehleranfällige Neuentwicklung sollte daher vermieden werden.
* Werden Session-IDs mit einem Framework verwaltet und erzeugt, so ist auf eine sichere Konfiguration des Frameworks zu achten, sodass die zuvor genanten Anforderungen an die Session-ID erfüllt sind.
**Schutz vor unbefugtem Zugriff auf die Session-ID**

Die Session-ID kann sowohl in der URL eines Requests (GET-Methode), im Rumpf des Requests (POST-Methode) oder als Cookie im Header des Requests übertragen werden. Wenn Daten mithilfe der GET-Methode übermittelt werden, können sie von beteiligten IT-Systemen gespeichert und dadurch von Dritten eingesehen werden (zum Beispiel im Browser-Verlauf, auf Bildschirmfotos, Seitenkopien oder Ausdrucken). Daher sollte die Session-ID nicht über die GET-Methode (also in der URL) übertragen werden. Für Webanwendungen mit hohem Schutzbedarf ist dies nicht erlaubt. Stattdessen sollte die Session-ID vorzugsweise in Cookies übertragen werden.

Erfordert die Anwendung die GET-Methode (zum Beispiel, weil einige Clients keine Cookies verarbeiten können), sind folgende Punkte zu beachten:

* Benutzer sollten auf die genannten Gefahren hingewiesen werden und beim Verlassen des Rechners die Sitzung beenden oder den Rechner sperren.
* Die Benutzer sollten angewiesen werden, keine gespeicherten Seiten oder Bildschirmfotos von Seiten der Webanwendung zu versenden, bei der die Session-ID in der URL sichtbar ist.
* Bei Nutzung der Webanwendung über einen öffentlichen Rechner sollte eine Meldung darauf hinweisen, dass der Browser-Verlauf nach der Sitzung gelöscht werden sollte.
* Sehr lange Session-IDs erschweren es Unbefugten, abzuschreiben oder auch zufällig mitzulesen.
* Bei der Verlinkung auf externe Seiten darf die Session-ID nicht übertragen werden. Dies gilt sowohl für die Übertragung in der URL als auch für das Referrer-Feld. Daher sollte bei Verlinkungen auf externe Seiten eine erzwungene Weiterleitung erfolgen, welche das Referrer-Feld bereinigt.
Zum Schutz vor unbefugtem Mitlesen der Session-ID sollte nach einer erfolgreichen Anmeldung die Kommunikation über eine sichere Verbindung stattfinden. Dies kann über eine Transportsicherung, beispielsweise mittels SSL/TLS verschlüsselt werden. Die Session-ID kann über eine ungesicherte Verbindung übertragen werden, wenn mit der bestehenden Sitzung keine zugriffsgeschützten Bereiche der Webanwendung verwendet werden können. Gewöhnlich ist der Benutzer in diesem Fall noch nicht authentisiert.

Der Zugriff auf die Session-ID als Authentisierungsmerkmal sollte streng reglementiert werden. Wird die Session-ID in einem Cookie übertragen, sollte der clientseitige Zugriff auf diesen Cookie möglichst mit folgenden Flags eingeschränkt werden (für eine detaillierte Beschreibung der Cookie-Flags siehe APP.3.1.M14 *Schutz vertraulicher Daten*): Path (zum Beispiel */webapp/*), Secure und HttpOnly.

**Beschränkte Sitzungsdauer**

Eine Webanwendung muss Benutzern die Möglichkeit geben, eine bestehende Sitzung nach ihrer Nutzung explizit zu beenden. Daher muss auf allen Webseiten, für deren Abruf eine Authentisierung des Benutzers notwendig ist, eine deutlich sichtbare Abmeldemöglichkeit bestehen. Nach erfolgter Abmeldung sollte die Sitzung vollständig beendet werden und die Session-ID nicht mehr gültig sein. Darüber hinaus sollte der Benutzer für folgende Verhaltensweisen sensibilisiert werden:

* Ist der Benutzer angemeldet, sollte er sich nach Abschluss der Tätigkeiten von der Webanwendung ordnungsgemäß abmelden.
* Falls beim letzten Besuch keine Abmeldung erfolgt ist, sollte der Benutzer bei dem nächsten Anmeldevorgang an der Webanwendung darauf hingewiesen werden, sich zukünftig abzumelden.
Ungenutzte, bestehende Sitzungen bieten eine Angriffsfläche für Brute-Force-Angriffe auf die Session-ID. Daher sollten Sitzungen nach einem Zeitintervall der Inaktivität nicht mehr gültig sein (Idletime). Darüber hinaus sollte eine maximale Gültigkeitsdauer vergeben werden (Timeout), sodass auch die Session-IDs von aktiven Sitzungen eine begrenzte Gültigkeit haben. Diese sollte für die Sitzungen so gering wie möglich gewählt werden, sodass Brute-Force-Angriffe erschwert werden, wobei die Benutzbarkeit der Webanwendung hierbei nicht unnötig eingeschränkt werden sollte. Mit der Formel aus dem Abschnitt „Anforderungen an die Session-ID“ lässt sich hierfür eine angemessene Gültigkeitsdauer ermitteln.

Treten bei der Nutzung der Webanwendung schwerwiegende Fehler auf, sollten angeforderte Aktionen abgebrochen und zusätzlich die Sitzung beendet werden. Schwerwiegende Fehler sind zum Beispiel auftretende Ausnahmefehler (Exceptions) und erkannte Angriffsversuche. Bei einem hohen Schutzbedarf sollten noch engere Kriterien erwogen werden, durch die die Sitzung ungültig wird (zum Beispiel ungültige Eingaben, Aufruf fehlender Seiten).

Bei der Invalidierung sollten die Sitzungsdaten server- und clientseitig vollständig gelöscht werden, sodass die Sitzung serverseitig nicht weiter akzeptiert wird und clientseitig keine Informationen über zuvor aufgebaute Sitzungen verbleiben. Dies kann zum Beispiel erreicht werden, indem das Cookie mit der Session-ID gelöscht wird.

Darüber hinaus können mehrere parallele Sitzungen unter dem gleichen Benutzerkonto verhindert werden. Eine bestehende Sitzung kann bei erneuter Anmeldung invalidiert werden, sodass nur die neue Sitzung gültig bleibt. Alternativ ist es beispielsweise möglich, die erste Sitzung über einen begrenzten Zeitraum (zum Beispiel 15 Minuten) aufrechtzuerhalten, bevor sie invalidiert wird. Dabei sollte dem Benutzer bei der Anmeldung über eine parallele, zweite Sitzung eine Meldung über die ablaufende, erste Sitzung eingeblendet werden. Auf diese Weise können noch bestehende, aber nicht mehr verwendete Sitzungen nach erneuter Anmeldung nicht oder nur eingeschränkt unbefugt von Dritten genutzt werden.

Zum Schutz vor Session-Fixation-Angriffen sollte nach erfolgter Anmeldung eine bereits bestehende Session-ID durch eine neue ersetzt werden.

Ebenso sollte nach einem Wechsel von einem ungesicherten Kommunikationskanal (HTTP) auf einen gesicherten Kommunikationskanal (HTTPS) eine neue Session-ID vergeben werden, da die Session-ID bei der Übertragung über einen ungesicherten Kanal mitgelesen worden sein könnte.

**Schutz der Sitzungsdaten**

Anfallende Sitzungsdaten (zum Beispiel Warenkorb) dürfen ausschließlich serverseitig auf einem vertrauenswürdigen IT-System gespeichert werden. Darüber hinaus müssen die Daten vor unbefugtem Zugriff von anderen Benutzern durch eine Zugriffskontrolle geschützt werden. Falls die Webanwendung eine clientseitige Speicherung der Sitzungsdaten erfordert, sollte ebenfalls APP.3.1.M14 *Schutz vertraulicher Daten* für die Speicherung von Daten auf dem Client beachtet werden.

**Zuordnung einer Sitzung anhand zusätzlicher Attribute**

Neben der Session-ID können weitere Merkmale verwendet werden, um Benutzer und Sitzung miteinander zu verknüpfen (zum Beispiel die IP-Adresse). Hierdurch ist es für einen Angreifer noch schwieriger eine Sitzung zu übernehmen, da er dafür neben einer gültigen Session-ID auch die zusätzlichen Merkmale kennen müsste. Die Verwendung von zusätzlichen Attributen zur Zuordnung einer Sitzung ist zumindest bei Webanwendungen mit hohem Schutzbedarf zu berücksichtigen.

Wird die IP-Adresse als zusätzliches Merkmal für die Sitzungszuordnung verwendet, so ist diese serverseitig zu speichern und zu prüfen. Wechselt die IP-Adresse im Laufe einer Sitzung, so sollte dies bei Anwendungen mit hohem Schutzbedarf als Angriffsversuch gewertet und demzufolge die Sitzung invalidiert werden. Dabei ist jedoch zu berücksichtigen, dass die IP-Adresse nicht immer einem Benutzer eindeutig zugeordnet werden kann. Erfolgt die Verbindung einiger Benutzer der Webanwendung über einen Proxy mit gleicher (zum Beispiel Reverse-Proxy) oder wechselnder IP-Adresse (zum Beispiel wechselnde, ausgehende Proxys), besteht die Gefahr, dass die IP-Adressen dieser Benutzer nicht eindeutig einer Sitzung zugeordnet werden können. Es sollte somit bedacht werden, dass die Sicherheitsmaßnahme dazu führt, dass einige Benutzer die Webanwendung möglicherweise nur eingeschränkt oder gar nicht nutzen können.

Wenn der Referrer als Identitätsmerkmal verwendet wird, kann auf einen festen Teil des Referrer-Pfades geprüft werden, der für alle Zugriffe identisch bleibt (zum Beispiel die Domäne der Webanwendung). Die Benutzer müssen demnach eine Webseite der Webanwendung im Referrer vorweisen. Hierbei ist zu berücksichtigen, dass einige Browser eine Deaktivierung oder benutzerseitige Manipulation der Referrer-Übermittlung erlauben und Content-Filter dieses Feld eventuell filtern.

Die Identitätsmerkmale können zum Schutz vor unbefugter Nutzung der Sitzung auf mehrere Eigenschaften des HTTP-Headers verteilt werden. Denkbar sind zum Beispiel HTTP-Header-Informationen wie

* die Browsertypenbezeichnung (User-Agent-Header),
* unterstützte Formate und Sprachen des Clients (Accept- und Accept-Language-Header) und
* der Referrer (Referrer-Header).
Aufgrund der teilweise geringen Variationsbreite der genannten Merkmale des HTTP-Headers ist der zusätzlich erreichte Schutz begrenzt. Dagegen erhöhen sich der Umsetzungsaufwand und unter Umständen die Komplexität bei der Fehlersuche. Aus diesem Grund sollte im Einzelfall abgewogen werden, ob der zusätzlich erreichte Schutz den Umsetzungsaufwand rechtfertigt.

**Eigenimplementierungen vermeiden**

Kann für die Sitzungsverwaltung einer Webanwendung auf eine erprobte Implementierung in einem Framework oder einen verbreiteten Standard zurückgegriffen werden, so ist dies gegenüber einer Eigenimplementierung in jedem Fall zu bevorzugen, da sich Eigenimplementierungen dieser sicherheitskritischen, komplexen Funktion sehr häufig als angreifbar erweisen.

#### APP.3.1.M4 Kontrolliertes Einbinden von Daten und Inhalten bei Webanwendungen [Entwickler]

Eine Webanwendung erstellt zur Laufzeit Webseiten, deren Inhalte sich aus unterschiedlichen Quellen zusammensetzen können. Diese Inhalte werden z. B. in Form von Dateien dynamisch bei der Erstellung der Webseite eingebunden oder von der Webanwendung generiert. Da einem Benutzer die fertige Webseite ausgeliefert wird, ist für ihn häufig nicht ersichtlich, aus welcher Quelle die angezeigten Inhalte stammen. Daher muss die Webanwendung sicherstellen, dass ausschließlich vorgesehene Daten und Inhalte eingebunden und an den Benutzer ausgeliefert werden.

Die Inhalte können mittels unterschiedlicher Techniken eingebunden werden. Daher werden in den folgenden Abschnitten Hinweise zur sicheren Verwendung üblicher Techniken zusammengefasst.

**Einbinden von Dateien (File Inclusion)**

Wenn Webseiten von einer Webanwendung generiert werden, bindet sie häufig Teile der ausgelieferten Internet-Seite aus unterschiedlichen Dateien dynamisch ein (z. B. eine Navigationsleiste). Hierdurch verringert sich der Wartungsaufwand bei Änderungen an der Webseite (z. B. ein neuer Navigations-Eintrag). Dabei sollten der Inhalt und der Pfad der einzubindenden Dateien ausschließlich vom Administrator oder von privilegierten Benutzern der Webanwendung geändert werden können. Gewöhnlichen Benutzern sollte es dagegen nicht möglich sein, die Dateien zur Einbindung frei zu wählen oder zu modifizieren (z. B. über veränderte Parameter). Aus diesem Grund sollte die Webanwendung Benutzer-Eingaben zur Einbindung von Dateien nicht verarbeiten.

Erfordert die Webanwendung jedoch Benutzer-Eingaben als Quelle zur Einbindung von Dateien, sollten die vorgesehenen Pfadangaben zu den Quell-Dateien nicht frei wählbar sein. Benutzer sollten nicht in der Lage sein, den gesamten Pfad vorzugeben, sondern stattdessen sollten Benutzer-Eingaben in vordefinierte Pfadangaben gekapselt werden.

Angriffe, wie Path Traversal, versuchen durch relative Bezüge den Pfad auf schützenswerte Dateien umzusetzen (z. B.* /../../../etc/passwd*) und so aus den vorgegebenen Pfadangaben auszubrechen. Zur Verhinderung derartiger Angriffe sollten daher die Benutzereingaben auf unerwünschte Zeichen zur Manipulation des Pfades (z. B. */..* und *\..*) gefiltert werden (siehe auch APP.3.1.M15 *Umfassende Ein- und Ausgabevalidierung*).

Bei der Auswahl der Quell-Dateien können Indizes anstelle von Dateinamen verwendet werden, denen serverseitig hinterlegte Dateinamen zugeordnet werden. Somit hat ein Angreifer keinen direkten Einfluss auf den Dateinamen und kann durch Manipulation des Index keine beliebigen Inhalte direkt einbinden.

Webanwendungen können, neben Dateien auf dem Serversystem, auch entfernt gespeicherte Ressourcen über die Netzverbindung mittels URL einbinden (Remote File Inclusion). Das sollte möglichst komplett unterbunden werden. Kann darauf jedoch nicht verzichtet werden, so muss die vertrauenswürdige Herkunft dieser Dateien unbedingt sichergestellt werden (z. B. auf Basis einer Whitelist mit der Limitierung auf einen Server oder eine Auflistung von absoluten URLs).

**Verwendung von Datei-Uploads**

Bei vielen Webanwendungen können Benutzer Inhalte mittels einer Upload-Funktion übermitteln. Ein typischer Anwendungsfall ist der Upload eines Profilfotos. Die hochgeladenen Daten sind auf die benötigten Dateiformate zu beschränken (z. B. sollten für das Profilfoto ausschließlich Bilddateien zugelassen werden). Hierbei sollte sowohl die Dateiendung als auch der Inhalt der Datei, z. B. durch eine Auswertung des Dateiheaders, geprüft werden.

Hochgeladene Dateien sollten in einem Verzeichnis gespeichert werden, das nicht über die Web-Schnittstelle erreichbar ist (z. B. außerhalb des Wurzelverzeichnisses des Webservers). So wird verhindert, dass ein Benutzer auf seine hochgeladenen Dateien direkt zugreifen kann (z. B. auf schädliche Skripte). Werden die hochgeladenen Dateien zunächst in einem temporären Verzeichnis gespeichert, so ist sicherzustellen, dass andere Benutzer nicht unerlaubt auf die Datei zugreifen können.

Stellt eine Webanwendung dem Benutzer eine Upload-Funktion von Dateien zur Verfügung, so sind folgende Punkte zu beachten:

* Die Funktionalität sollte nur für angemeldete Benutzer verfügbar sein.
* Hochgeladene Dateien dürfen nicht im Wurzelverzeichnis des Webserver-Dienstes gespeichert werden. Es sollten entweder feste Verzeichnisstrukturen vorgegeben werden, in denen Ordner und Dateien angelegt werden können oder die Speicherung in einem anderen Kontext (wie z. B. in einer Datenbank oder einem fest vorgegebenen Pfad) erfolgen. Ein Benutzer sollte nicht aus dem vorgegebenen Kontext ausbrechen können.
* Der vorgegebene Pfad zur Speicherung der hochgeladenen Dateien darf nicht von den Benutzern geändert werden können.
* Zum Schutz vor Denial-of-Service-Angriffen sollte die Dateigröße begrenzt werden.
* Die Berechtigungen hochgeladener Dateien sollten restriktiv gesetzt sein, um einen unberechtigten Zugriff zu verhindern. Auf diese Weise soll unterbunden werden, dass hochgeladene Dateien eines Angreifers ausgeführt werden.
* Ein Virenschutzprogramm sollte die hochgeladenen Dateien auf Schadsoftware untersuchen.
* Die Wahl des Dateinamens sollte wie folgt eingeschränkt werden:
* Der Dateiname mit der Dateiendung sollte auf eine feste Anzahl von Zeichen begrenzt werden (z. B. 200 Zeichen).
* Alle nicht sichtbaren Zeichen (z. B. Steuerzeichen) und alle kodierten Varianten dieser Zeichen sollten vom Dateinamen entfernt werden (z. B. Unicode).
* Alle Zeichen mit einer spezifischen Bedeutung für Interpreter sollten entfernt werden (z. B. *; : > < / \ . * % $*).
* Falls möglich sollten ausschließlich alphanumerische Zeichen und der Punkt für die Dateiendung erlaubt sein.
**Einbinden von Inhalten aus übergebenen Parametern**

Webanwendungen nehmen häufig Eingaben in Form von Parametern (z. B. aus Formularen) entgegen, verarbeiten diese und stellen sie erneut in der Rückantwort dar (z. B. der Suchbegriff bei einer Websuche). Ein Angreifer kann dies ausnutzen, um über ausgewählte Eingaben die Darstellung der Webseite zu manipulieren. Daher müssen alle von der Webanwendung zur Darstellung von Webseiten verwendeten Parameter gemäß APP.3.1.M15 *Umfassende Ein- und Ausgabevalidierung* validiert werden.

**Sicheres Weiterleiten von Requests (Redirect)**

Die Weiterleitungsfunktion einer Webanwendung darf nicht beliebige Webseiten als Weiterleitungsziel zulassen, sodass Benutzer ausschließlich auf vertrauenswürdige, vorgesehene Webseiten weitergeleitet werden. So sollte vermieden werden, dass Benutzer beispielsweise über einen präparierten Link auf die Weiterleitungsfunktion der Webanwendung auf eine Phishing-Seite geführt werden.

Die folgenden Punkte geben Hinweise zu Einschränkungsmöglichkeiten von Weiterleitungszielen.

* Beschränkung auf lokale Seiten  
 Wenn keine Weiterleitung auf externe Webseiten erfolgen muss, kann das Weiterleitungsziel auf externe Adressen geprüft und nur lokale Seiten zugelassen werden. Hierbei sollten ausschließlich relative Pfadangaben auf Ziele innerhalb der Webanwendung als Eingabe zugelassen und der notwendige Host-Teil nachträglich statisch hinzugefügt werden.
* Vordefinierte Weiterleitungsziele  
 Ist eine Weiterleitung ausschließlich auf bekannte, statische Ziele vorgesehen, sollten diese serverseitig in einer vordefinierten Liste mit Indizes hinterlegt werden. Den Zielen werden somit statische Index-Werte zugeordnet. Anstelle der Zieladresse übergibt der Client einen Index-Wert (z. B. aus einer Auswahlliste eines Formulars), der serverseitig einer Zieladresse aus der Liste zugeordnet wird.
* Manuelle Bestätigung  
 Der Benutzer muss vor der Weiterleitung die Zieladresse und somit die Vertrauenswürdigkeit des Weiterleitungsziels prüfen und bestätigen (z. B. über eine eingeblendete Weiterleitungsseite). Hiermit wird der Benutzer gewarnt, bevor er die Webanwendung und damit den Sicherheitskontext verlässt.
* Referrer-Test  
 Das Refferer-Feld des HTTP-Requests kann von der Weiterleitungsfunktion als zusätzliches Merkmal für die bestimmungsgemäße Nutzung geprüft werden. Eine Weiterleitung sollte nur dann erfolgen, wenn das Referrer-Feld die Adresse zu einer Webseite der Webanwendung mit einem Verweis auf das Weiterleitungsziel enthält.
**Einbindung von Inhalten Dritter**

Von Partnern eingebundene Daten und Inhalte (z. B. Werbeeinblendungen) sollten grundsätzlich als weniger vertrauenswürdig eingestuft werden. Es wird daher eine starke Kontrolle dieser Inhalte empfohlen, da die Gefahr besteht, dass Schadcode oder nicht vertrauenswürdige Inhalte eingebettet werden.

#### APP.3.1.M5 Protokollierung sicherheitsrelevanter Ereignisse von Webanwendungen [Entwickler]

Sicherheitsrelevante Ereignisse (zum Beispiel Zugriffe auf Ressourcen, Authentisierungsversuche) müssen nachvollziehbar protokolliert werden, damit im Stör- oder Fehlerfall oder nach Angriffsversuchen die Protokolldaten herangezogen werden können, um die Ursachen zu ermitteln. Vertiefende Informationen sind in OPS.1.1.6 *Protokollierung* zu finden.

Es sollten folgende Punkte bei der Protokollierung sicherheitsrelevanter Ereignisse von Webanwendungen beachtet werden.

**Zu protokollierende Ereignisse bei Web-Anwendungen **

Zusätzlich zur Protokollierung auf den Server- und Hintergrundsystemen (zum Beispiel Betriebssystem, Web- und Applikationsserver, Datenbank) muss auch die Anwendung sicherheitsrelevante Ereignisse protokollieren. Mindestens folgende Ereignisse sollten auf Anwendungsebene erfasst werden:

* erfolgreiche und erfolglose Anmeldeversuche an der Webanwendung,
* fehlgeschlagene Autorisierungsversuche beim Zugriff auf Ressourcen (zum Beispiel Datenbankzugriffe) und Funktionen der Webanwendung,
* fehlgeschlagene Validierung von Ein- und Ausgabedaten,
* fehlgeschlagene XML-Schema-Validierungen,
* XML-Parser-Fehler,
* aufgetretene Fehler (zum Beispiel Exceptions),
* Änderungen von Berechtigungen für Benutzer oder Benutzergruppen der Webanwendung (zum Beispiel Zugriffsrechte),
* Änderungen an Benutzerkonten (zum Beispiel Passwortänderung),
* Löschvorgänge der Webanwendung (zum Beispiel Beiträge),
* erkannte Manipulationsversuche und unerwartete Änderungen (zum Beispiel Anmeldeversuche mit ungültigen oder abgelaufenen Session-IDs),
* administrative Funktionsaufrufe und Änderungen an der Konfiguration (zum Beispiel Abruf von Benutzerdaten, Aktivierung und Deaktivierung der Protokollierung),
* Starten und Stoppen von Diensten.
**Zu protokollierende Merkmale von Ereignissen**

Um sicherheitsrelevante Vorgänge anhand von Protokolldaten nachvollziehen zu können, müssen grundlegende Merkmale der Ereignisse verfügbar sein. Daher sollten mindestens die folgenden Merkmale protokolliert werden:

* Datum,
* Uhrzeit mit Zeitzone,
* assoziierter Benutzername,
* betroffenes Objekt (zum Beispiel Benutzerkonto, Datei, Datenquelle),
* Status der Aktion (zum Beispiel fehlgeschlagen, erfolgreich),
* Ort des Auftretens (zum Beispiel Komponente),
* Aktion (zum Beispiel Authentisierung, Autorisierung),
* Schweregrad (zum Beispiel Information, Warnung, Fehler).
Darüber hinaus kann es auch hilfreich sein, folgende Merkmale zu protokollieren:

* Source-IP-Adresse,
* Referenzen auf die Session-ID (nicht die Session-ID selbst),
* IT-System, an dem der Fehler aufgetreten ist,
* Softwarestand (Version) der Webanwendung.
Vertrauliche und sicherheitsrelevante Daten (zum Beispiel Session-ID, Zugangsdaten) sollten nicht protokolliert werden.

**Geeignete Datenformate und Mechanismen**

Die protokollierten Daten sollten in einem einheitlichen Format gespeichert werden, damit eine effiziente Auswertung möglich ist. Die Protokollierungskomponente der Webanwendung sollte aus diesem Grund ein Datenformat verwenden, das in bestehende Lösungen integriert werden kann. Wird beispielsweise eine zentrale Komponente für die Auswertung der Protokolldaten verwendet, so sollten Datenformate gewählt werden, die diese Komponente unterstützt.

**Serverseitige Protokollierung durch eine zentrale Komponente**

Die Protokollierung der Webanwendung ist ausschließlich serverseitig durchzuführen, da nur auf diese Weise die Protokolldaten zentral ausgewertet werden können. Die Protokolldaten sollten von einer einzigen, zentralen Protokollierungskomponente der Webanwendung und nicht von unterschiedlichen Protokollierungskomponenten erhoben werden.

Eine fehleranfällige Neuentwicklung der Protokollierungskomponente sollte vermieden werden. Stattdessen sollte auf die Funktionalität etablierter Frameworks zurückgegriffen werden, die in der Regel einen zentralisierten Protokollierungsansatz und die Protokollierung in verbreiteten Protokolldatenformaten unterstützen (siehe Abschnitt *Geeignete Datenformate und Mechanismen*).

**Schutz vor unbefugtem Zugriff und der Manipulation von Protokolldaten**

Da die Protokolldaten vertrauliche Informationen (zum Beispiel über das Benutzerverhalten und den Aufbau beziehungsweise die Konfiguration der Webanwendung) enthalten können, muss der Zugriff auf die Protokolldaten reglementiert und nur befugten Benutzern ermöglicht werden. Der Zugriff auf Protokolldaten sollte nicht über öffentliche Schnittstellen möglich sein. Protokolldaten sollten daher in dedizierten Logverzeichnissen (zum Beispiel außerhalb des Web-Root-Verzeichnisses des Web-Servers) gespeichert werden.

Werden die Protokolldaten in einer Datenbank abgelegt, so sollten die Protokolldaten von den eigentlichen Nutzdaten getrennt werden. Diese Trennung kann mittels einer separaten Datenbanktabelle erreicht werden. Darüber hinaus kann ein eigener Datenbankbenutzer für die Protokollierung den Schutz der Protokolldaten erhöhen. In diesem Fall darf der Datenbankbenutzer für die Nutzdaten keine Zugriffsrechte auf die Protokolldaten haben.

Alternativ können die Protokollierungsdaten mit hohem Schutzbedarf auch in einer separaten Datenbankinstanz gespeichert werden.

**Sichere Protokollauswertung**

Ein Angreifer kann bewusst Protokoll-Einträge provozieren (zum Beispiel wenn Eingabefelder protokolliert werden), die schädlichen Programmcode beinhalten. Daher muss bei der Auswertung der Protokolldaten sichergestellt werden, dass Schadcode in Protokoll-Einträgen vom Auswertungsprogramm nicht interpretiert wird, was zum Beispiel durch die Ansicht in einem Browser und die Interpretation von JavaScript-Code in den Protokolldaten der Fall sein könnte. 

Da bei der Protokollauswertung keine Änderungen an den Protokolldaten vorgenommen werden dürfen, sind die Protokolldaten ausschließlich in einem schreibgeschützten Modus zu analysieren.

**Zeitsynchronisation**

Die Protokolldaten verschiedener Komponenten einer Webanwendung (zum Beispiel Applikationsserver, Webserver, Datenbankserver) müssen in der Regel korreliert werden, um komponentenübergreifende Vorgänge vollständig nachvollziehen zu können. Dazu sollte die Zeit auf den Systemen synchronisiert sein, um anhand der Uhrzeiten Vorgänge in den Protokollen konsistent nachverfolgen zu können. 

#### APP.3.1.M6 Zeitnahes Einspielen sicherheitsrelevanter Patches und Updates

Häufig werden Fehler in Produkten bekannt, die dazu führen können, dass die Informationssicherheit des Informationsverbundes, in dem diese betrieben werden, beeinträchtigt wird. Entsprechende Fehler können Hardware, Firmware, Betriebssysteme und Anwendungen betreffen. Diese Schwachstellen müssen so schnell wie möglich behoben werden, damit sie nicht durch interne oder externe Angreifer ausgenutzt werden können. Dies ist ganz besonders wichtig, wenn die betreffenden Systeme mit dem Internet verbunden sind. Die Hersteller von Betriebssystem- oder Software-Komponenten veröffentlichen in der Regel Patches oder Updates, die auf dem jeweiligen IT-System installiert werden müssen, um den oder die Fehler zu beheben.

Die Systemadministratoren sollten sich daher regelmäßig über bekannt gewordene Schwachstellen informieren (siehe auch Abschnitt *Informationsbeschaffung über Sicherheitslücken des Systems*). 

Wichtig ist, dass Patches und Updates, wie jede andere Software, nur aus vertrauenswürdigen Quellen bezogen werden dürfen. Für jedes eingesetzte System oder Softwareprodukt muss bekannt sein, wo Sicherheitsupdates und Patches erhältlich sind. Außerdem ist es wichtig, dass Integrität und Authentizität der bereits installierten Produkte oder der einzuspielenden Sicherheitsupdates und Patches überprüft werden, bevor ein Update oder Patch installiert wird. Vor der Installation sollten sie außerdem mithilfe eines Virenschutzprogramms geprüft werden. Dies sollte auch bei solchen Paketen gemacht werden, deren Integrität und Authentizität verifiziert wurde.

Sicherheitsupdates oder Patches dürfen jedoch nicht voreilig eingespielt werden, sondern müssen davor getestet werden. Falls sich ein Konflikt mit anderen kritischen Komponenten oder Programmen herausstellt, kann ein solches Update sonst zu einem Ausfall des Systems führen. Nötigenfalls muss ein betroffenes System so lange durch andere Maßnahmen geschützt werden, bis die Tests abgeschlossen sind.

Vor der Installation eines Updates oder Patches sollte stets eine Datensicherung des Systems erstellt werden, die es ermöglicht, den Originalzustand wieder herzustellen, falls Probleme auftreten. Dies gilt insbesondere dann, wenn ausführliche Tests aus Zeitgründen oder mangels eines geeigneten Testsystems nicht durchgeführt werden können.

In jedem Fall muss dokumentiert werden, wann, von wem und aus welchem Anlass Patches und Updates eingespielt wurden. Aus der Dokumentation muss sich der aktuelle Patchlevel des Systems jederzeit schnell ermitteln lassen, um beim Bekanntwerden von Schwachstellen schnell Klarheit darüber zu erhalten, ob das System dadurch gefährdet ist.

Falls festgestellt wird, dass ein Sicherheitsupdate oder Patch mit einer anderen wichtigen Komponente oder einem Programm inkompatibel ist oder Probleme verursacht, so muss sorgfältig überlegt werden, wie weiter vorgegangen wird. Wird entschieden, dass aufgrund der aufgetretenen Probleme ein Patch nicht installiert wird, so ist diese Entscheidung auf jeden Fall zu dokumentieren. Außerdem muss in diesem Fall klar beschrieben sein, welche Maßnahmen ersatzweise ergriffen wurden, um die Sicherheit zu gewährleisten. Eine solche Entscheidung darf nicht von den Administratoren allein getroffen werden, sondern sie muss mit den Vorgesetzten und dem Sicherheitsbeauftragten abgestimmt sein.

**Informationsbeschaffung über Sicherheitslücken des Systems**

Es ist sehr wichtig, dass sich Systemadministratoren regelmäßig über neu bekannt gewordene Schwachstellen informieren. Informationsquellen zu diesem Thema sind beispielsweise:

* Das Bundesamt für Sicherheit in der Informationstechnik (BSI) (siehe http://www.bsi.bund.de/) 
* Hersteller bzw. Distributoren von Programmen und Betriebssystemen. Diese informieren oft registrierte Kunden über bekannt gewordene Sicherheitslücken ihrer Systeme und stellen korrigierte Varianten des Systems oder Patches zur Behebung der Sicherheitslücken zur Verfügung.
* Computer Emergency Response Teams (CERTs).  
 Dies sind Computer-Notfallteams, die als zentrale Anlaufstelle für präventive und reaktive Maßnahmen in Bezug auf sicherheitsrelevante Vorfälle in Computersystemen dienen. CERTs informieren in sogenannten Advisories über aktuelle Schwachstellen in Hard- und Softwareprodukten und geben Empfehlungen zu deren Behebung. Verschiedene Organisationen oder Verbände unterhalten eigene CERTs.   
 Das ursprüngliche CERT der Carnegie Mellon Universität diente als Vorbild für viele weitere derartige Teams und ist heute eine Art "Dach-CERT":   
 Computer Emergency Response Team / Coordination Center (CERT/CC), Software Engineering Institute, Carnegie Mellon University, Pittsburgh, PA 15213-3890,  
 Telefon: +1-412-268-7090 (24-Stunden-Hotline), E-Mail: cert@cert.org, WWW: http://www.cert.org  
 Die CERT-Mitteilungen werden in Newsgruppen (comp.security.announce und info.nsfnet.cert) und über Mailinglisten (Aufnahme durch E-Mail an: cert-advisory-request@cert.org) veröffentlicht.  
 In Deutschland existieren unter anderem folgende CERTs:
* CERT-Bund, Bundesamt für Sicherheit in der Informationstechnik, Postfach 20 03 63, D-53133 Bonn, Telefon: 0228 99-9582-222, Fax: 022899-9582-5427, E-Mail: certbund@bsi.bund.de, WWW: https://www.bsi.bund.de/certbund/
* DFN-CERT, Zentrum für sichere Netzdienste GmbH, DFN-CERT, DFN-CERT Services GmbH, Sachsenstraße 5, D-20097 Hamburg, Telefon: 040-808077-555, Fax: -556, E-Mail: info@dfn-cert.de, WWW: http://www.dfn-cert.de.
* An verschiedenen Hochschulen existieren CERTs, die auch Informationen öffentlich zur Verfügung stellen. Ein Beispiel ist das RUS-CERT der Universität Stuttgart (siehe http://cert.uni-stuttgart.de).
* Hersteller- und systemspezifische sowie sicherheitsspezifische Newsgruppen oder Mailinglisten. In solchen Foren werden Hinweise auf existierende oder vermutete Sicherheitslücken oder Fehler in diversen Betriebssystemen und sonstigen Softwareprodukten diskutiert. Besonders aktuell sind meist die englischsprachigen Mailinglisten wie Bugtraq, von denen es an vielen Stellen öffentlich zugängliche Archive gibt, beispielsweise unter http://www.securityfocus.com. 
* Manche IT-Fachzeitschriften veröffentlichen ebenfalls regelmäßig Beiträge mit einer Übersicht über neue Sicherheitslücken in verschiedenen Produkten.
Idealerweise sollten sich die Administratoren und der Sicherheitsbeauftragte bei mindestens zwei verschiedenen Stellen über Sicherheitslücken informieren. Dabei ist es empfehlenswert, neben den Informationen des Herstellers auch eine "unabhängige" Informationsquelle zu benutzen. 

Die Administratoren sollten jedoch in jedem Fall auch produktspezifische Informationsquellen des Herstellers nutzen, um beispielsweise darüber Bescheid zu wissen, ob für ein bestimmtes Produkt beim Bekanntwerden von Sicherheitslücken überhaupt Patches oder Updates bereitgestellt werden. Bei Produkten, für die der Hersteller keine Sicherheitspatches mehr zur Verfügung stellt, muss rechtzeitig geprüft werden, ob ein Einsatz unter diesen Umständen noch zu verantworten ist und durch welche zusätzlichen Maßnahmen ein Schutz der betroffenen Systeme trotzdem gewährleistet werden kann.

#### APP.3.1.M7 Schutz vor unerlaubter automatisierter Nutzung von Webanwendungen [Entwickler]

Eine Webanwendung wird gewöhnlich von Menschen genutzt und erfordert somit keine automatisierte Nutzung (z. B. durch Skripte). Brute-Force-Angriffe (z. B. Erraten von Zugangsdaten) und Enumeration-Angriffe (z. B. automatisiertes Ermitteln von gültigen Login-Namen) beruhen hingegen auf der automatisierten Steuerung einer Webanwendung (Automation). Bei diesen Angriffen wird zumeist versucht, vertrauliche Daten durch wiederholende, leicht variierende Abfragen (z. B. geänderte Benutzernamen) zu sammeln.

Um solche Angriffe zu verhindern, muss die Webanwendung automatisierte von manuellen Zugriffen unterscheiden können. Automatisierte Angriffe zeichnen sich durch eine hohe Zahl an Zugriffsversuchen innerhalb einer kurzen Zeitspanne aus, die das übliche Maß deutlich übersteigt.

Daher kann eine Toleranzschwelle für wiederholt abgerufene Ressourcen derartige Angriffe erschweren (Teergrube). Werden Grenzwerte gegen automatisierte Anfragen festgelegt, ist darauf zu achten, dass legitime Benutzer in der Funktionalität und der Bedienung der Webanwendung möglichst wenig eingeschränkt werden. Falls Grenzwerte für elementare Funktionen der Webanwendung zu eng bemessen sind, können Angreifer dies auf Webanwendungs-Ebene für Denial-of-Service-Angriffe missbrauchen. Werden beispielsweise Benutzerkonten nach einer festgelegten Anzahl an erfolglosen Anmeldeversuchen für ein gewisses Zeitintervall gesperrt, können gezielte Falscheingaben zu einer längerfristigen Sperrung vieler Benutzerkonten führen. Demzufolge können sich legitime Benutzer in diesem Zeitraum nicht mehr an der Webanwendung anmelden.

Darüber hinaus ist die Effizienz automatisierter Angriffe in der Regel stark abhängig vom Detailgrad der Informationen in den Rückantworten der Webanwendung (siehe *APP.3.1.M13 Restriktive Herausgabe sicherheitsrelevanter Informationen*).

Folgende Beispiele zeigen mögliche Schutzmechanismen auf:

* Eine künstliche Verzögerung zwischen der Eingabe der Zugangsdaten bei der Benutzer-Authentisierung und der Meldung über einen fehlgeschlagenen Anmeldeversuch kann Brute-Force-Angriffe aufgrund des erhöhten Zeitbedarfs erschweren. Die Wirksamkeit dieser Methode kann durch ein progressives Ansteigen der Verzögerung nach jedem gescheiterten Versuch erhöht werden.
* Werden Eingaben zurückgewiesen, sollten Informationen über die Ursache generisch verfasst sein. Einem Angreifer darf es beispielsweise nicht möglich sein, aufgrund von Meldungen, wie "Passwort ungültig" anstelle von "Zugangsdaten ungültig", auf ein gültiges Benutzerkonto zu schließen (siehe auch APP.3.1.M16 *Fehlerbehandlung*).
* Angriffsversuche sind häufig gekennzeichnet durch vielfache Fehlversuche bei der Durchführung einer Aktion. Daher sollte in diesem Fall die Sitzung beendet werden. Anschließend sollte eine Neuanmeldung erforderlich sein.
* Automatisierte Angriffe lassen sich abwehren, indem die IP-Adresse bei Verdacht auf einen Angriff temporär gesperrt wird. Es sollte hierbei bedacht werden, dass durch diese Empfehlung eventuell Unbeteiligte ebenfalls von der Sperrung betroffen sind (z. B. wenn mehrere Benutzer denselben Proxy verwenden).
* Häufig werden sogenannte CAPTCHAs (Completely Automated Public Turing Test To Tell Computers and Humans Apart) zur Unterscheidung automatisierter und manueller Zugriffe eingesetzt. Hierbei müssen vom Benutzer der Webanwendung Aufgaben gelöst werden (z. B. die Zeichen in einem Bild müssen erkannt und abgetippt oder Rätselfragen beantwortet werden), was für ein Computerprogramm nicht ohne Weiteres möglich ist. Abhängig von der verwendeten Technik und Aufgabenstellung ist die Webanwendung dadurch eventuell nur eingeschränkt für Menschen mit Behinderung nutzbar. So sollte z. B. alternativ zum Einblenden der Aufgabe diese auch akustisch zur Verfügung gestellt werden, um Menschen mit Sehbehinderung die Nutzung der Webanwendung zu ermöglichen. Es ist zu beachten, dass der Einsatz von CAPTCHAs aus Gründen der Diskriminierung in vielen Ländern gesetzlich geregelt oder verboten ist. In Deutschland ist die Bundesverwaltung verpflichtet, ihre öffentlich zugänglichen Internet- und Intranet-Angebote nach der Barrierefreie-Informationstechnik-Verordnung (BITV) zu gestalten.
### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Webanwendungen".

#### APP.3.1.M8 Systemarchitektur einer Webanwendung

Webanwendungen verwenden im Allgemeinen mehrere IT-Systemkomponenten, z. B. Webserver, Web-Applikationsserver und Hintergrundsysteme. Als Grundlage für den sicheren Betrieb einer Webanwendung muss eine geeignete Systemarchitektur gewählt werden.

Beim Entwurf der Systemarchitektur der Webanwendung und der Vernetzung der beteiligten IT-Systeme sollten die folgenden Punkte berücksichtigt werden.

**Sicherer Entwurf der Logik **

Mit Webanwendungen lassen sich komplexe Geschäftsprozesse abbilden, die über das bloße Anzeigen von einzelnen Webseiten hinausgehen. Beim technischen Entwurf dieser Prozesse muss darauf geachtet werden, dass die umgesetzte Anwendungslogik nicht missbräuchlich verwendet werden kann. So soll beispielsweise nicht aus einem vorgesehenen Prozess der Webanwendung ausgebrochen und somit der Ablauf des Prozesses von außen gesteuert werden können.

Die Anforderungen an die abgebildete Geschäftslogik sind exakt zu erfassen und korrekt umzusetzen, sodass ausschließlich beabsichtigte und vorgesehene Aktionen durchgeführt werden können. Ein abweichendes Verhalten muss zurückgewiesen werden. Sollen beispielsweise mittels einer Empfehlungsfunktion der Webanwendung ausschließlich Artikelempfehlungen verschickt werden, ist zu berücksichtigen, dass diese Funktion auch missbraucht werden kann, um Spam-E-Mails zu versenden. Wird in diesem Beispiel der Empfehlungstext fest vorgegeben, so können keine Spam-E-Mails mehr über diese Funktion versandt werden. Des Weiteren ist auch zu prüfen, ob Fehler in der Geschäftslogik durch zwei gleichzeitige Sessions (concurrent sessions) auftreten können (race conditions).

Bei der Konzeption der Webanwendung sollten daher alle Funktionen anhand von Anwendungsfällen (Use Cases) dokumentiert werden. Dabei sollte erfasst werden, für welche Zwecke die Funktionen verwendet werden sollen und wie eine missbräuchliche Nutzung vermieden werden kann.

Wird die Webanwendung aus irgendeinem Grund abgebrochen, so muss die Logik sicherstellen, dass die Webanwendung wieder in einen konsistenten Zustand kommt (roll back).

Interaktive Funktionen in Web-Angeboten können auch durch aktive Inhalte umgesetzt werden, die auf dem Client-System ausgeführt werden (z. B. per JavaScript). Oft ist es aber auch möglich, diese Funktionen mit dynamischen oder statischen Inhalten bereitzustellen. Da die Nutzung von aktiven Inhalten aus Sicherheitsgründen auf den Client-Systemen häufig deaktiviert ist, wird empfohlen, die Webanwendung möglichst ohne aktive Inhalte zu konzeptionieren und die Anwendungslogik rein serverseitig zu realisieren.

Interaktive Funktionen in Webanwendungen können auf unterschiedliche Weise realisiert werden: Server-seitig oder Client-seitig. Da der Client nicht unter der Kontrolle der Webanwendung steht, kann nicht ausgeschlossen werden, dass dieser missbräuchlich benutzt wird. Gerade aktive Inhalte wie JavaScript oder ActiveX wurden und werden immer wieder ausgenutzt, Webanwendungen und die von ihnen verwalteten Informationen anzugreifen. Aus Sicherheitsüberlegungen empfiehlt es sich deshalb, aktive Inhalte Server-seitig umzusetzen oder, wo dies möglich ist, auf sie zu verzichten.

Sollen aktive Inhalte genutzt werden, sind folgende Punkte zu beachten:

* Es sollte sichergestellt sein, dass die Webanwendung auch dann verwendet werden kann, wenn die Ausführung aktiver Inhalte im Browser deaktiviert ist.
* Für aktive Inhalte sollte möglichst nachvollziehbar sein, aus welcher Quelle sie stammen, damit eine wirksame Prüfung im Client vorgenommen werden kann. Dies kann beispielsweise durch die Signatur von ActiveX-Komponenten erreicht werden.
* Ist es bei der Verwendung von Ajax unvermeidlich, XML-Daten zu serialisieren und dynamisch zu erzeugen, sollte auf Frameworks zurückgegriffen werden.
* Wird JavaScript verwendet, sollte auf den Funktionsaufruf *eval() *verzichtet werden.
* Benutzt die Webanwendung JSON für den Datenaustausch, so sind ausschließlich Objekte als Top-Level-Elemente zu verwenden.
Beispiele:

* Eine Webanwendung authentisiert die Benutzer in mehreren, aufeinanderfolgenden Schritten. Die Benutzer müssen im ersten Schritt Benutzername und Passwort und im zweiten Schritt ein Authentisierungstoken verwenden. Dabei sollte der erste Schritt nicht übersprungen werden können, damit sichergestellt ist, dass alle Authentisierungsmerkmale eingegeben werden. Im letzten Schritt für die endgültige Authentisierung müssen dann erneut alle Authentisierungsmerkmale überprüft werden.
* Bereits in der Konzeptionsphase einer Banking-Anwendung muss bedacht werden, dass ein Benutzer auch negative Beträge in ein Überweisungsformular eintragen kann. Die Webanwendung muss dabei sicherstellen, dass hierdurch nicht die Logik des Überweisungsformulars umgekehrt und dass keine unvorgesehene Gutschrift ausgelöst wird.
**Trennung nach Server-Rollen**

Die Serverdienste der Webanwendung (z. B. Webserver, Applikationsserver, Datenbankserver) sollten jeweils auf separaten IT-Systemen betrieben werden. Kann bei diesem Ansatz eine Schwachstelle im System einer exponierten Komponente (z. B. im Webserver) ausgenutzt werden, so sind die auf anderen Systemkomponenten (z. B. der Datenbank) gespeicherten Daten hiervon nicht direkt betroffen.

Eine Trennung der Server-Rollen kann auch durch eine Servervirtualisierung umgesetzt werden. Wird eine Servervirtualisierung gebraucht, so ist bei der Umsetzung der Baustein SYS.1.5 *Server-Virtualisierung* zu berücksichtigen.

**Eingeschränkte Konten für Serverprozesse der Systemkomponenten**

Es sollten jeweils eigene Konten für die unterschiedlichen Serverprozesse der Systemkomponenten verwendet werden (z. B. ein eigener Systembenutzer für den Webserverprozess). Dabei sind die Rechte dieser Dienstekonten auf Betriebssystemebene soweit einzuschränken, dass nur auf die erforderlichen Ressourcen und Dateien des Betriebssystems zugegriffen werden kann. Auf diese Weise verfügt ein Angreifer auch nach einer erfolgreichen Kompromittierung eines Server-Prozesses nur über eingeschränkte Rechte, sodass der Zugriff auf Betriebssystemebene erschwert wird. 

**Mehrschichtige Netzarchitektur**

Die IT-Systemkomponenten der Webanwendung sollten im Sicherheitsgateway in demilitarisierten Zonen (DMZ) entsprechend des Schutzbedarfs entkoppelt werden.

Die Netzarchitektur sollte einen mehrschichtigen Ansatz verfolgen (Multi-Tier-Architektur). Dabei sollten mindestens die folgenden Sicherheitszonen berücksichtigt werden:

* Webschicht  
 Diese Schicht grenzt an das nicht vertrauenswürdige Netz (z. B. Internet) und stellt die exponierte Schicht mit direkten Zugriffen durch Benutzer dar. Paketfilter zwischen angrenzenden Netzen (z. B. Anwendungsschicht und Internet) sollten den Datenverkehr filtern, sodass kein direkter Zugriff aus dem nicht vertrauenswürdigen Netz über die Netzgrenzen der Webschicht hinaus möglich ist. In dieser Schicht sollten Systeme wie der Webserver platziert werden, die eine exponierte Stellung einnehmen und z. B. den direkten Zugriff durch Benutzer erfordern.
* Anwendungsschicht  
 Die Anwendungsschicht sollte zum einen an die Webschicht und zum anderen an die Datenschicht angrenzen. Der Netzverkehr zu den angrenzenden Netzen sollte durch Paketfilter gefiltert werden, sodass kein direkter Zugriff zwischen den angrenzenden Netzen möglich ist. In diesem Netzsegment sollten Systeme und Server mit der Anwendungslogik (z. B. der Applikationsserver mit der Webanwendung) platziert sein. Die Systeme greifen auf Daten aus der angrenzenden Datenschicht zu (z. B. Datenbanken), bereiten diese auf und stellen sie Systemen in der Webschicht (z. B. dem Webserver) zur Verfügung.
* Datenschicht  
 Die Datenschicht ist die vertrauenswürdigste Zone der mehrschichtigen Architektur. Paketfilter zwischen den angrenzenden Netzen sollten den Datenverkehr reglementieren. In dieser Schicht sollten die Hintergrundsysteme der Webanwendung wie z. B. Datenbanken, Verzeichnisdienst und Legacy-Systeme aufgestellt sein. Der Zugriff auf diese Systeme sollte ausschließlich von angrenzenden Netzen aus möglich sein (z. B. Anwendungsschicht). Die Datenschicht ist als separate Zone umzusetzen und sollte nicht in andere Zonen (z. B. Intranet) integriert werden.
Es sollte aus den oben genannten Zonen nicht auf Systeme im Intranet zugegriffen werden können. Falls z. B. für die Authentisierung an der Webanwendung ein Verzeichnisdienst eingesetzt wird, sollte hierfür möglichst eine eigene Domäne auf dedizierter Hardware verwendet werden.

Eine Filterung des Datenverkehrs sollte durch getrennte Filterkomponenten erfolgen (z. B. Paketfilter). Bei hohem Schutzbedarf sollten die Filterkomponenten durch Systeme mit Filterfunktionen auf höheren Protokollebenen (z. B. Application Level Gateway) ersetzt oder ergänzt werden. Das Application Level Gateway sollte dabei in einer eigenen Sicherheitszone integriert werden, die noch vor den Systemen der Webschicht die Anfragen der Benutzer entgegennimmt.

**Dokumentation der Architektur**

Das Verständnis der Software-Architektur einer Webanwendung ist notwendig, um diese effizient und fehlerfrei zu warten, zu entwickeln und zu erweitern. Bei der Dokumentation von Webanwendungen sind einige Besonderheiten zu berücksichtigen.

Die Dokumentation muss alle Bestandteile berücksichtigen. Dabei sollten mindestens folgende Punkte durch die spezifische Dokumentation abgedeckt werden:

* Alle Abhängigkeiten (zum Beispiel zu Frameworks, Bibliotheken, Betriebssystemen, Hardware) und Schnittstellen (zum Beispiel zu Hintergrundsystemen) sollten dokumentiert werden.
* Für den Betrieb notwendige Komponenten, die nicht Bestandteil der Webanwendung sind, müssen als solche gekennzeichnet werden, zum Beispiel Hintergrundsysteme wie eine Datenbank.
* Aus der Dokumentation muss hervorgehen, welche Komponenten Sicherheitsmechanismen umsetzen. Im Folgenden sind die Sicherheitsfunktionen von Webanwendungen aufgeführt, die mindestens berücksichtigt werden sollten: 

 
	+ Benutzermanagement,
	+ Rollen- und Berechtigungskonzept,
	+ Authentisierung,
	+ Autorisierung,
	+ Session-Management,
	+ Protokollierung und
	+ Transportsicherheit.
	  

 
* Die Dokumentation muss beschreiben, wie die Webanwendung in eine bestehende Netzinfrastruktur integriert wird. Hierbei ist die Anforderung APP.3.1.M8 *Systemarchitektur einer Webanwendung* zu beachten.
* Die eingesetzten kryptografischen Funktionen und Verfahren müssen dokumentiert sein, siehe Baustein CON.1 *Kryptokonzept*.
Die Dokumentation sollte während des Projektverlaufs aktualisiert und angepasst werden, sodass sie schon während der Entwicklungstätigkeit genutzt werden kann und Entscheidungsfindungen dokumentiert sind.

#### APP.3.1.M9 Beschaffung, Entwicklung und Erweiterung von Webanwendungen [Tester, Leiter Entwicklung, Beschaffer, Entwickler]

Wenn Institutionen Webanwendungen verwenden möchten, können sie sich diese ganz oder in Teilen auf dem Markt einkaufen. Um ein geeignetes Produkt zu finden, müssen geeignete Kriterien definiert werden. Institutionen können aber auch eine Webanwendung selbst entwickeln oder erweitern. Auch dafür müssen Regeln festgelegt und eingehalten werden (siehe Abschnitt Entwicklung und Erweiterung). 

**Erstellung eines Anforderungskatalogs für Standardsoftware**

Um eine Aufgabe zu lösen, die mit einer Webanwendung bearbeitet wird, bietet der Markt meist eine Vielzahl gleichartiger Standardsoftwareprodukte an. In ihrer Grundfunktionalität vergleichbar, unterscheiden sie sich jedoch in Kriterien wie Anschaffungs- und Betriebskosten, Zusatzfunktionalitäten, Kompatibilität, Administration, Ergonomie und Informationssicherheit.

Um eine geeignete Webanwendung auswählen zu können, muss daher zunächst ein Anforderungskatalog erstellt werden (siehe hierzu Baustein CON.5 Standardsoftware). Der Anforderungskatalog sollte unter anderem zu den folgenden Punkten Aussagen enthalten:

* Funktionale Anforderungen
* IT-Einsatzumgebung
* Kompatibilitäts- und Interoperabilitätsanforderungen
* Performanceanforderungen 
* Zuverlässigkeitsanforderungen
* Konformität zu Standards
* Anforderungen an die Benutzerfreundlichkeit
Die für das Produkt erforderlichen Sicherheitseigenschaften sollten ebenfalls im Anforderungskatalog aufgeführt werden. Typische Sicherheitsfunktionen sind beispielsweise

* Identifizierung und Authentisierung
* Zugriffskontrolle
* Protokollierung und Protokollauswertung
* Datensicherung
* Verschlüsselung
* Funktionen zur Wahrung der Datenintegrität
Um verschiedene Webanwendungen vom Markt im Sinne einer Nutzwertanalyse vergleichen zu können, sollte eine Bewertungsskala entwickelt werden, in der geeignete Kriterien vorhanden sind, wie die Erfüllung der einzelnen Anforderungen gewertet wird. Dazu ist es erforderlich, vorab die Bedeutung der einzelnen Anforderungen für die angestrebte IT-gestützte Aufgabenerfüllung quantitativ oder qualitativ zu bewerten.

**Entwicklung und Erweiterung**

Die folgenden Punkte sollten bei der Entwicklung und Erweiterung von Webanwendungen beachtet werden.

Es sollte nach einem geeigneten Vorgehensmodell (z. B. V-Modell XT, Wasserfallmodell, Spiralmodell) entwickelt werden. Dabei hat eine Anwendung vor der Inbetriebnahme alle Entwicklungsphasen des Vorgehensmodells zu durchlaufen. Das verwendete Vorgehensmodell sollte mindestens die folgenden oder vergleichbare Phasen abdecken.

**Anforderungsanalyse**

Unternehmenssicherheitsrichtlinien und unternehmensspezifische Vorgaben sollten in der Anforderungsanalyse berücksichtigt und den Entwicklungsteams zur Verfügung gestellt werden (z. B. Erfüllung von Industrie-Standards wie PCI DSS oder Vorgaben zur Barrierefreiheit). Hierzu zählen z. B. auch Vorgaben und Anforderungen an die Verwendung kryptografischer Algorithmen und sicherer Programmierrichtlinien (siehe auch Abschnitt Umsetzung von Programmierrichtlinien).

In dieser Phase sollten alle von der Webanwendung zu verarbeitenden Daten identifiziert und nach dem Schutzbedarf klassifiziert werden. Es müssen adäquate Schutzmechanismen der Anwendung festgelegt werden, welche die Daten gemäß ihrem Schutzbedarf schützen.

**Konzeption und Design**

Bei der Konzeption sollten die Architektur und der Aufbau der Anwendung festgelegt und dokumentiert werden. Hierbei sollten Entwicklungstechniken (z. B. Programmiersprachen, Frameworks) ausgewählt werden. Auch das Wissen und der Erfahrungsschatz der Entwickler ist aus Kosten- und Sicherheitsgründen zu berücksichtigen.

Die Architektur sollte vorsehen, dass Komponenten (z. B. zur Autorisierung, Authentisierung) vorzugsweise in Modulen umgesetzt werden, die sich wiederverwenden lassen. Durch die zentrale Verfügbarkeit und Nutzung von Modulen können Redundanzen vermieden und die Pflege erleichtert werden. 

Bei Webanwendung sollten die zentralen Sicherheitsmechanismen nach Möglichkeit mindestens serverseitig umgesetzt werden.

Es sollte darauf geachtet werden, dass Sicherheitsanforderungen vollständig durch Sicherheitsmechanismen erfüllt und zur Erstellung von Testfällen festgehalten werden.

Getroffene Entscheidungen sollten dokumentiert werden, sodass später eine effiziente Weiterentwicklung der Anwendung durch ausreichende Dokumentation gewährleistet ist. 

**Entwicklung**

Bei der Umsetzung der Anwendung sollten Programmierrichtlinien (siehe auch Abschnitt Umsetzung von Programmierrichtlinien) für die sichere Entwicklung der Komponenten eingehalten werden.

Es sollte darauf geachtet werden, dass die Dokumentation während der Entwicklungstätigkeit fortgeführt wird (z. B. durch Kommentare im Quelltext und Werkzeuge zur Generierung der Dokumentation). Somit ist der Quelltext zu einem späteren Zeitpunkt auch für Dritte nachvollziehbar.

Zum Schutz vor dem Verlust bereits entwickelter und verworfener Lösungen sowie zu Dokumentationszwecken sollte die Historie der Änderungen festgehalten werden (z. B. durch ein Revisionssystem).

**Tests**

Testfälle sollten nicht nur die Geschäftsfunktionen, sondern ebenfalls die Sicherheitsfunktionalität berücksichtigen. Dazu zählen z. B. Sicherheitskomponenten wie Autorisierungs-, Authentisierungs- und Filterkomponenten. Nach Möglichkeit sollten Penetrationstests und (für hohen Schutzbedarf) auch Source-Code-Analysen durchgeführt werden, um die umgesetzten Sicherheitsmechanismen zu kontrollieren (APP.3.1.M21 *Durchführung von Penetrationstests*).

Bevor eine Anwendung betrieben wird, sollte nicht nur die Funktionstüchtigkeit, sondern auch ein möglicher Missbrauch der angebotenen Funktionalität geprüft werden. Dies kann durch Penetrationstests erreicht werden. Damit nach dem Vier-Augen-Prinzip getestet wird, sollten die Tests nicht von den Personen durchgeführt werden, die zuvor an der Konzeption oder der Entwicklung der Anwendung beteiligt waren. 

Bei den Tests ist darauf zu achten, dass diese nur mit Testdaten und nicht mit Live-Daten bzw. Kundendaten durchgeführt werden.

Bei Webanwendungen sollten die Webseiten auf Konformität zu dem verwendeten Standard (z. B. HTML-Standard) getestet werden. Dadurch können unvorhergesehene Seiteneffekte aufgrund einer Fehlinterpretation seitens der Browser vermieden werden. Eine Überprüfung mit verschiedenen Browsern kann hier sehr hilfreich sein.

Bei der Planung und Durchführung der Tests sollte die Anforderung APP.3.1.M10 *Software-Abnahme- und Freigabe-Verfahren* berücksichtigt werden.

**Integration und Softwareverteilung (Deployment)**

Vor der produktiven Inbetriebnahme sind die Webanwendungen und notwendige Hintergrundsysteme sicher zu konfigurieren. Hierbei sollte die Anbindung möglicher Hintergrundsysteme (z. B. Identitätsspeicher, Datenbanken) an die Anwendung berücksichtigt werden. Vor der Inbetriebnahme der Anwendung ist ebenfalls sicherzustellen, dass der Transportkanal geschützt ist.

Schützenswerte Daten der Webanwendung sind häufig in Hintergrundsystemen hinterlegt. Daher sollte das Sicherheitsniveau der Anwendung und möglicher Hintergrundsysteme einheitlich sein. Der Zugriff auf die Hintergrundsysteme sollte Benutzern lediglich über die definierten Schnittstellen der Anwendung möglich sein.

Darüber hinaus sollte sichergestellt werden, dass die Daten bei der Verteilung der Anwendung nicht durch Dritte manipuliert werden können.

**Wartung **

Es muss ein Prozess zur Pflege der Anwendung definiert werden, der auch die regelmäßige Prüfung der Sicherheit der Anwendung auf Schwachstellen bzw. verfügbare Patches berücksichtigt.

Wird die Anwendung angepasst oder erweitert, muss darauf geachtet werden, dass dabei die Sicherheitsmechanismen nicht beeinträchtigt werden. Zusätzlich sollte durch Tests in einer gesonderten Testumgebung erneut überprüft werden, ob die Sicherheitsmechanismen noch korrekt funktionieren.

**Umsetzung von Programmierrichtlinien**

Eine Programmierrichtlinie hilft, einen einheitlichen Programmierstil zu definieren und ein einheitliches Sicherheitsniveau zu etablieren (z. B. durch die Verwendung von Sicherheitsbibliotheken). Die Qualität und Verständlichkeit des Quelltexts kann hierdurch verbessert und nachvollziehbarer werden. In der Folge können Fehler und Schwachstellen einfacher gefunden und eine spätere Erweiterung der Anwendung kosteneffektiv umgesetzt werden.

Programmierrichtlinien sollten nicht nur bei der Entwicklung im eigenen Haus, sondern auch beim Outsourcing der Entwicklungstätigkeit umgesetzt werden.

**Zukunftssichere Entwicklung von Sicherheitsmechanismen**

Wenn Sicherheitsmechanismen entworfen und entwickelt werden, sollten hierbei auch zukünftige Entwicklungen von Angriffstechniken als auch Standards (z. B. neuer HTML-Standard) berücksichtigt werden. So sollte beispielsweise eine Filterkomponente, die als schädlich klassifizierte <script>-Tags filtert, ebenso unbekannte Tags filtern. Zum Zeitpunkt der Entwicklung noch unbekannte Tags können eventuell zukünftig verwendet werden (z. B. mit der Einführung eines neuen HTML-Standards), um Sicherheitsmechanismen der Webanwendung zu umgehen.

**Produktspezifische Sicherheitsfunktionalität**

Falls eine Webanwendung ausschließlich mit einem spezifischen Browser genutzt wird, so sollte der Einsatz von produktspezifischen Sicherheitsfunktionen des Browsers berücksichtigt werden.

**Outsourcing der Anwendungsentwicklung**

Im Fall von Outsourcing muss sichergestellt werden, dass das beauftragte Unternehmen die nötigen Sicherheitsanforderungen bei der Entwicklung der Anwendung erfüllt. Dies kann beispielsweise durch die Vorgabe eines Vorgehensmodells oder durch Programmierrichtlinien erreicht werden.

Wird für die Entwicklung einer Anwendung mit hohem Schutzbedarf ein Dienstleister beauftragt, sollte der Quelltext (z. B. das Projektarchiv) unter der administrativen Kontrolle des Auftraggebers stehen. Dabei sollte der Auftraggeber jederzeit auf den Quelltext der Anwendung zugreifen und Änderungen am Quelltext nachvollziehen können.

**Festlegung der Entwicklungsumgebung**

Die Produktiv-, Test- und Entwicklungsumgebungen sind auf getrennten Systemen zu betreiben. In den Umgebungen sollten unterschiedliche Zugangsdaten gewählt werden. Testkonten sollten hierbei, soweit möglich, keine privilegierten Rechte erhalten. Grundsätzlich dürfen sich erfolgreiche Angriffe auf die Entwicklungs- oder Testumgebung nicht auf die Produktivumgebung auswirken.

#### APP.3.1.M10 Abnahme und Freigabe von Webanwendungen [Leiter IT]

Im Zuge eines Software-Abnahme-Verfahrens wird überprüft, ob die betrachtete Software, zum Beispiel eine Webanwendung, die erforderliche Funktionalität zuverlässig bereitstellt und ob sie darüber hinaus keine unerwünschten Nebeneffekte hat. Mit der anschließenden Freigabe der Software durch die fachlich zuständige Stelle wird die Erlaubnis erteilt, die Software zu benutzen. Gleichzeitig übernimmt diese Stelle damit auch die Verantwortung für das IT-Verfahren, dass durch die Software realisiert wird.

Bei der Software-Abnahme wird sinnvollerweise zwischen Software unterschieden, die selbst oder im Auftrag entwickelt wurde, und Standardsoftware, die nur für den speziellen Einsatzzweck angepasst wird.

**Abnahme von selbst- oder im Auftrag entwickelter Software**

Bevor der Auftrag zur Software-Entwicklung intern oder extern vergeben wird, muss die Anforderungsdefinition für die Software erstellt sein, aus der dann das Grob- und Feinkonzept für die Realisierung entwickelt wird. Anhand dieser Dokumente erstellt die fachlich zuständige Stelle einen Abnahmeplan.

Üblicherweise werden hierzu Testfälle und die erwarteten Ergebnisse für die Software erarbeitet. Anhand dieser Testfälle wird die Software getestet und der Abgleich zwischen berechnetem und erwartetem Ergebnis wird als Indiz für die Korrektheit der Software benutzt.

Zur Entwicklung der Testfälle und zur Durchführung der Tests ist folgendes zu beachten:

* die Testfälle werden von der fachlich zuständigen Stelle entwickelt,
* für Testfälle werden keine Daten des Wirkbetriebs benutzt,
* Testdaten, insbesondere wenn dafür Wirkdaten kopiert werden, dürfen keine vertraulichen Informationen beinhalten und personenbezogene Daten sind zu anonymisieren oder zu simulieren,
* der Test darf sich nicht auf den laufenden Betrieb auswirken. Nach Möglichkeit sollte ein logisch oder physisch isolierter Testrechner benutzt werden.
Eine Abnahme ist zu verweigern, wenn:

* schwerwiegende Fehler in der Software festgestellt werden,
* Testfälle auftreten, in denen die erwarteten Ergebnisse nicht mit den berechneten übereinstimmen, 
* Benutzerhandbücher oder Bedienungsanleitungen nicht vorhanden oder von nicht ausreichender Qualität sind und
* die Software, unter anderem der Quellcode und die Abläufe, nicht oder nicht ausreichend dokumentiert ist.
Die Ergebnisse der Abnahme sind schriftlich festzuhalten. Die Dokumentation des Abnahmeergebnisses sollte umfassen:

* Bezeichnung und Versionsnummer der Software und falls erforderlich des IT-Verfahrens,
* Beschreibung der Testumgebung,
* Testfälle und Testergebnisse und
* Abnahmeerklärung.
**Abnahme von Standardsoftware**

Wird Standardsoftware beschafft, so sollte auch diese abgenommen und freigegeben werden. In der Abnahme sollte überprüft werden, ob

* die Software frei von Computer-Viren ist,
* die Software kompatibel zu den anderen eingesetzten Produkten ist, 
* die Software in der angestrebten Betriebsumgebung lauffähig ist und welche Parameter zu setzen sind,
* die Software komplett einschließlich der erforderlichen Dokumentation ausgeliefert wurde und
* die geforderte Funktionalität erfüllt wird.
**Freigabe-Verfahren**

Wurde die Software abgenommen, muss sie danach für die Nutzung freigegeben werden. Dazu ist zunächst festzulegen, wer berechtigt ist, Software freizugeben. Die Freigabe der Software ist schriftlich festzulegen und geeignet zu hinterlegen.

Die Freigabeerklärung sollte umfassen:

* Bezeichnung und Versionsnummer der Software und falls erforderlich des IT-Verfahrens,
* Bestätigung, dass die Abnahme ordnungsgemäß vorgenommen wurde,
* Einschränkungen für die Nutzung (Parametereinstellung, Benutzerkreis ...),
* Freigabedatum, ab wann die Software eingesetzt werden darf und
* die eigentliche Freigabeerklärung.
Falls IT-technisch möglich, muss verhindert werden, dass Software nach der Freigabe unbemerkt verändert oder manipuliert werden kann, beispielsweise durch geeignete Verfahren zum Integritätsschutz. Andernfalls müssen geeignete organisatorische Regelungen festgelegt werden, um Änderungen an der Software zu verhindern bzw. zeitnah festzustellen.

Auch nach intensiven Abnahmetests kann es vorkommen, dass im laufenden Einsatz Fehler in der Software festgestellt werden. Für diesen Fall ist festzulegen, wie in einem solchen Fehlerfall verfahren werden soll (Ansprechpartner, Fehlerbeseitigungsablauf, Beteiligung der fachlich zuständigen Stelle, Wiederholung der Abnahme und Freigabe, Versionskontrolle).

Weiterführende Erklärungen sind im Baustein CON.5 *Standardsoftware *zu finden*.*

#### APP.3.1.M11 Sichere Anbindung von Hintergrundsystemen

Webanwendungen verwenden häufig Hintergrundsysteme, zum Beispiel für die Datenhaltung in einer Datenbank oder für die Benutzerverwaltung durch Verzeichnisdienste. Die Daten sind auch bei der Übermittlung und Speicherung in Hintergrundsystemen ausreichend zu schützen. Dazu müssen die Hintergrundsysteme sicher an die Webanwendung angebunden sein.

Typische Hintergrundsysteme von Webanwendungen sind: Datenbanken, Verzeichnisdienste, Middleware, Web-Services und Legacy-Systeme.

Zur sicheren Anbindung von Hintergrundsystemen sollten folgende Punkte beachtet werden:

**Platzierung von und Zugriff auf die Hintergrundsysteme**

Die Benutzer der Webanwendung sollten nicht direkt auf die Hintergrundsysteme zugreifen können, da so eventuell Schutzmaßnahmen umgangen werden. Stattdessen sollten sie ausschließlich über vordefinierte Schnittstellen und Funktionen der Webanwendung darauf zugreifen dürfen. 

Darüber hinaus sollte die Verbindung zu den Hintergrundsystemen zusätzlich geschützt werden. Hierzu sollten sich die Systeme vor der Datenübertragung authentisieren und die übertragenen Daten verschlüsseln, sodass sie nicht unbemerkt mitgelesen oder geändert werden können (zum Beispiel mittels SSL/TLS).

Werden die beteiligten IT-Systeme über unsichere Kanäle angebunden, so sollte in jedem Fall ein kryptografisch abgesicherter Tunnel mit entsprechender Verschlüsselung und Authentisierung verwendet werden.

Zugriffe auf Hintergrundsysteme sollten mit minimalen Rechten erfolgen. Hierfür sollten Dienstekonten auf dem jeweiligen Hintergrundsystem eingerichtet werden.

Wird für den Zugriff auf ein Hintergrundsystem ein einziges Dienstekonto benutzt, werden alle Anfragen im Sicherheitskontext dieses Dienstekontos bearbeitet. Dies gilt dann sowohl für Zugriffe von Benutzern mit eingeschränkten Zugriffsberechtigungen als auch für die Zugriffe administrativer Benutzer. Um dies zu verhindern, sollten mehrere Dienstekonten mit unterschiedlichen Zugriffsrechten für ein Hintergrundsystem verwendet werden.

Bei einer geeigneten Systemumgebung können die Benutzerkonten an das Hintergrundsystem weitergeleitet werden, beispielsweise wenn ein Verzeichnisdienst verwendet wird, mit dem sowohl die Webanwendung als auch das Hintergrundsystem die Benutzer verwalten. Auf diese Weise können die Privilegien auf die notwendigen Rechte des jeweils an der Webanwendung angemeldeten Benutzers limitiert werden.

Es ist darauf zu achten, dass für unauthentisierte Zugriffe auf die Webanwendung ein eigenes Dienstekonto im Verzeichnisdienst mit eingeschränkten Berechtigungen verwendet wird.

**Enterprise Service Bus**

Im Kontext sogenannter serviceorientierter Architekturen (SOA) werden Webanwendungen häufig über einen Enterprise Service Bus (ESB) als zentrale Kommunikationsinfrastruktur an Hintergrundsysteme angebunden. Dadurch wird erreicht, dass für jede Anwendung jeweils nur die Schnittstelle zum ESB definiert und realisiert werden muss, und nicht viele separate Schnittstellen zu anderen Anwendungen und Diensten. In einem eigenen Verzeichnis (*Repository*) speichert der ESB Metainformationen über die angeschlossenen Dienste. 

Zusätzlich kann der ESB auch zentrale Sicherheitsfunktionen realisieren, um die angeschlossenen Anwendungen weiter zu schützen. Solche Sicherheitsfunktionen können beispielsweise Replay-Attacken erkennen und abwehren oder XML-Daten auf potenziell schädliche Inhalte prüfen, aber auch den Nachrichtenaustausch zentral und revisionssicher protokollieren.

Beim Einsatz eines ESB muss sichergestellt werden, dass sich alle Dienste gegenüber dem ESB authentisieren, bevor ihnen ein Zugriff erlaubt wird. Dies gilt auch für Zugriffe auf das ESB-Repository. Der ESB muss so in die Netzarchitektur integriert werden, dass ein Zugriff nur von den Servern der angeschlossenen Anwendungen und Dienste möglich ist und ein Zugriff von außen auf den ESB ausgeschlossen wird. Dazu sollte der ESB ein eigenes logisches Netzsegment erhalten. Der ESB muss eine eigene Berechtigungsprüfung durchführen, um zu prüfen, ob ein Zugriff auf den angefragten Dienst durch den anfragenden Dienst beziehungsweise die anfragende Anwendung zulässig ist. Dabei muss insbesondere sicher ausgeschlossen werden, dass Anwendungen oder Dienste mit Außenkontakt auf interne Dienste zugreifen, die dafür nicht vorgesehen sind. Solche Anwendungen dürfen auch nicht über das ESB-Repository Kenntnis von internen Diensten und ihren Schnittstellen erlangen. Sofern die serviceorientierte Architektur mehrere Sicherheitsdomänen umspannt, zum Beispiel eine DMZ mit extern aufrufbaren Services und ein internes Netz mit Backend-Systemen, so muss auch der ESB in entsprechende Sicherheitsdomänen mit kontrollierten Übergängen aufgeteilt werden, oder es müssen mehrere ESB für die einzelnen Sicherheitszonen realisiert werden.

Sofern der ESB nicht ausschließlich lokal in einem geschützten RZ-Netz kommuniziert, muss die Kommunikation zwischen ESB und den angeschlossenen Anwendungen geeignet gesichert werden (Authentisierung und Verschlüsselung).

Durch die Bündelung der Kommunikation vieler Anwendungen und Dienste kommt der Verfügbarkeit des ESB eine besondere Bedeutung zu. Dies ist bei der Realisierung und beim Betrieb des ESB entsprechend durch Redundanzen und eine geeignete Überwachung des Dienstes zu berücksichtigen.

#### APP.3.1.M12 Sichere Konfiguration von Webanwendungen [Entwickler]

Ist eine Webanwendung unzureichend konfiguriert, so kann ein Angreifer möglicherweise bestehende Sicherheitsmechanismen überwinden. Folgende Punkte sollten daher bei der Konfiguration der Webanwendung berücksichtigt werden:

**Deaktivierung nicht benötigter HTTP-Methoden**

Auf eine Webanwendung kann gemäß HTTP-Standard mit unterschiedlichen HTTP-Methoden (z. B. *GET, POST, PUT, DELETE* oder *TRACE*) zugegriffen werden. Üblicherweise benötigt eine Webanwendung jedoch nur eine sehr eingeschränkte Menge dieser HTTP-Methoden (z. B. *GET* und* POST*).

Darüber hinaus kann eine Webanwendung in Abhängigkeit der verwendeten HTTP-Methode unterschiedlich auf einen Request reagieren. Wird beispielsweise die Eingabedatenfilterung nur bei einem GET- oder POST-Request durchgeführt, so könnte diese Sicherheitsfunktion durch den Aufruf einer nicht vorgesehenen HTTP-Methode umgangen werden.

Einige HTTP-Methoden (z. B. *PUT*) bieten Zugriff auf sicherheitskritische Funktionalität (z. B. Hochladen beliebiger Dateien) und ermöglichen auf diese Weise Restriktionen der Webanwendung zu umgehen (z. B. die Dateitypenprüfung bei einer Upload-Funktion).

Deshalb sollten nicht benötigte HTTP-Methoden deaktiviert und von der Webanwendung nicht bearbeitet werden. Dies gilt auch für fiktive HTTP-Methoden, die nicht im entsprechenden Standard RFC 2616 definiert werden. Auch wenn die HTTP-Methoden bereits in der Konfiguration des Webservers deaktiviert wurden, sollte auch die Webanwendung nicht benötigte HTTP-Requests nicht bearbeiten.

**Zeichenkodierungskonfiguration**

Die übermittelten Daten zwischen dem Client des Benutzers und der Webanwendung können in verschiedenen Kodierungen vorliegen. Abhängig von der erwarteten Kodierung werden die Daten von Clients, von der Webanwendung oder von den Hintergrundsystemen unterschiedlich interpretiert. Damit Clients Daten an die Webanwendung in der gewünschten Kodierung senden, sollte die Webanwendung bei der Auslieferung von Webseiten in den Header-Feldern der HTTP-Response das Zeichenkodierungsschema (z. B. UTF-8) mit angeben.

Falls die Webanwendung international verwendet wird, sollte darauf geachtet werden, dass alle internationalen Zeichensätze auf allen logischen Ebenen der Webanwendung und von den angebundenen Hintergrundsystemen unterstützt werden.

**Festlegung von Grenzwerten**

Einige Schutzmechanismen sehen den Einsatz von Grenzwerten vor (siehe z. B. APP.3.1.M7 *Schutz vor unerlaubter automatisierter Nutzung von Webanwendungen*). Wird ein Grenzwert überschritten, erfolgt häufig die zeitweise Sperrung einer betroffenen Funktion oder Ressource. So können wiederholt fehlgeschlagene Anmeldeversuche zur Folge haben, dass das Benutzerkonto gesperrt wird (z. B. zur Abwehr von Brute-Force-Angriffen).

Solche Maßnahmen können jedoch die Bedienung der Webanwendung beeinflussen und somit ebenfalls unbeteiligte Benutzer betreffen. Diese Benutzer können sich beispielsweise nicht mehr an der Webanwendung anmelden, falls ihr Benutzerkonto gesperrt wurde.

Diese Auswirkungen sollten daher auch bei der Festlegung von Grenzwerten berücksichtigt werden.

**Restriktive Dateisystemberechtigungen**

Webanwendungen bieten Benutzern häufig direkt oder indirekt Zugriff auf das darunterliegende Dateisystem (z. B. über abrufbare Dateien oder eine Upload-Funktion). Damit ein Angreifer nicht unbefugt schützenswerte Dateien lesen oder manipulieren kann, sollten diese zusätzlich zu den Zugriffsbeschränkungen auf Webanwendungsebene durch restriktive Dateisystemberechtigungen geschützt werden. Der Server, auf dem die Webanwendung läuft, muss mit eingeschränkten Rechten gestartet werden und nicht als Administrator (root).

**Administration einer Webanwendung**

Die Webanwendung sollte vorrangig über ein von der Anwendung entkoppeltes System administriert werden. Im Fall einer E-Commerce-Anwendung kann beispielsweise die Artikelpflege über ein getrenntes System mit Zugriff auf die Datenbank der Webanwendung erfolgen. Das System sollte idealerweise allein für diesen Zweck bestimmt und nicht direkt mit der Webanwendung verbunden sein. Dementsprechend sollte die Webanwendung die Artikeldaten ausschließlich von der Datenbank abrufen.

Häufig bieten Webanwendungen zur Administration eine Weboberfläche auf demselben Server an. Diese Funktion sollte gemieden und stattdessen sollte die Webanwendung über ein separates System administriert werden. Falls die Administration auf demselben Server erforderlich ist, sollte die Administrationsoberfläche ausschließlich aus dem Administrationsnetz heraus erreichbar und der Zugriff durch gewöhnliche Benutzer der Webanwendung nicht möglich sein. Möglichkeiten zur Administration der Webanwendung, die nicht genutzt werden (z. B. Konsole), sollten deaktiviert sein.

#### APP.3.1.M13 Restriktive Herausgabe sicherheitsrelevanter Informationen [Entwickler]

Webseiten und Rückantworten von Webanwendungen können sicherheitsrelevante Informationen beinhalten, mit deren Hilfe Angreifer Sicherheitsmechanismen umgehen und Schwachstellen ausnutzen können. Daher dürfen keine sicherheitsrelevanten Informationen angezeigt werden, die nicht zwingend für den Betrieb und die Nutzung der Webanwendung notwendig sind.

Die folgenden Beispiele verdeutlichen, welche Informationen sicherheitsrelevante Hinweise enthalten können und wie verhindert werden kann, dass diese offengelegt werden. 

**Keine sicherheitsrelevanten Informationen in Fehlermeldungen**

Tritt bei der Bedienung der Webanwendung ein Fehler auf (zum Beispiel Zugriffsfehler), sollten dem Benutzer neutrale Fehlermeldungen übermittelt werden. Die Fehlermeldungen dürfen keine direkten Rückschlüsse auf eingesetzte Techniken, Sicherheitsmechanismen und Zustände der Webanwendung ermöglichen. Beispiele für Informationen, die nicht in Fehlermeldungen enthalten sein sollten:

* Stacktraces und Debugging-Informationen,
* Meldungen wie *Benutzername ungültig* oder *Passwort ungültig* (anstelle von allgemeinen Fehlermeldungen wie *Benutzername oder Passwort ungültig*),
* von Hintergrundsystemen weitergereichte Fehlermeldungen, zum Beispiel SQL-Fehlermeldungen einer Datenbank statt einer Meldung *Fehler bei der Überprüfung der Zugangsdaten*,
* Fehlercodes statt zum Beispiel der Meldung *Ein Fehler ist aufgetreten*.
Im Fall einer fehlgeschlagenen Authentisierung sollte beispielsweise unabhängig von der Gültigkeit des Benutzernamens stets eine allgemeingültige Meldung wie *Falsche oder ungültige Zugangsdaten* ausgegeben werden, damit ein Angreifer nicht auf die Existenz von Benutzerkonten rückschließen kann (user enumeration).

Grundsätzlich kann unterschiedlicher HTML-Code zur gleichen Ausgabe im Webbrowser führen. Beispielsweise werden zwei HTML-Seiten mit einer unterschiedlichen Anzahl von Leerzeichen im Browser gleich dargestellt, obwohl sie sich im HTML-Code unterscheiden. Es ist daher darauf zu achten, dass die Fehlermeldungen nicht nur in der Darstellung im Browser, sondern auch im HTML-Code identisch sind. Hiermit soll verhindert werden, dass ein Angreifer aufgrund eines veränderten HTML-Codes auf die Gültigkeit von Teil-Eingaben (zum Beispiel gültiger Benutzername bei falschem Passwort) schließen kann.

Weitere Informationen zur Fehlerbehandlung finden sich in APP.3.1.M16 *Fehlerbehandlung*.

**Verhinderung von "WS-Interface Probing"**

Wenn Web-Services-Description-Language-(WSDL)-Dateien generiert werden, ist darauf zu achten, dass die verwendeten Tools oder Frameworks keine zusätzlichen und womöglich sicherheitskritischen Informationen in die Dateien schreiben. Deswegen sind die Dateien, bevor sie veröffentlicht werden, zunächst entsprechend zu prüfen. Bei Bedarf müssen die Tools bzw. Frameworks dann so umkonfiguriert werden, dass sie keine sicherheitskritischen Informationen mehr in die WSDL-Dateien schreiben oder die Dateien müssen nachträglich bereinigt werden.

XML-Transportcontainer sollten generell keine Fehlermeldungen mit detaillierten Informationen an Benutzer (potenzielle Angreifer) weitergeben. Die Meldungen sollten so allgemein bzw. generisch gestaltet sein, dass sie keine Informationen über eingesetzte Anwendungen, Frameworks und Versionsnummern enthalten und auch keinen Rückschluss auf diese zulassen.

Sollen Dienste nur von bestimmten, dem Service-Provider bekannten Benutzern gesucht und aufgerufen werden können, bietet es sich an, die WSDL-Dateien bzw. deren Repositories mittels einer vorherigen Nutzerauthentisierung vor direktem und unberechtigtem Zugriff zu schützen.

**Vermeidung von sicherheitsrelevanten Kommentaren in ausgelieferten Webseiten**

Bei der Entwicklung von Webanwendungen werden möglicherweise Kommentare in den HTML-Code geschrieben. Diese Kommentare können sicherheitsrelevante Informationen (zum Beispiel To-do-Listen, Versionsnummern, Zugangsdaten oder uninterpretierter Quellcode) enthalten, die als HTML-Kommentare in der Webseite vom Benutzer leicht eingesehen werden können. Aus diesem Grund ist darauf zu achten, dass in den Kommentaren keine sicherheitsrelevanten Informationen enthalten sind. Idealerweise sollten in den ausgelieferten Webseiten oder Rückantworten einer produktiven Webanwendung überhaupt keine Kommentare verwendet werden.

**Eingeschränkter Zugriff auf Dokumentation**

Informationen in der Dokumentation einer Webanwendung können einem Angreifer auf potenzielle Schwachstellen (zum Beispiel Standardbenutzer nach der Installation) hinweisen. Sie können missbraucht werden, um Angriffe vorzubereiten. Daher sollte verzichtbare Dokumentation zur Webanwendung und den zugehörigen Komponenten (zum Beispiel Datenbank) gelöscht werden. Ist die Dokumentation online verfügbar, so sollte ausschließlich der entsprechende Adressatenkreis darauf zugreifen können. Beispielsweise sollte die Dokumentation zur Administration einer Webanwendung nicht aus dem Internet heraus erreichbar sein.

**Löschen nicht benötigter Dateien**

Im laufenden Betrieb einer Webanwendung fallen häufig Dateien an, die nicht für den produktiven Betrieb benötigt werden (zum Beispiel temporäre Dateien, oder Backup-Dateien). Diese Dateien können sicherheitskritische Informationen beinhalten (zum Beispiel Testergebnisse) oder Funktionen anbieten (zum Beispiel Testwerkzeuge zur Ermittlung von Versionsnummern der eingesetzten Bibliotheken), die für Angriffe auf die Webanwendung genutzt werden können.

Darüber hinaus ist zu beachten, dass insbesondere bei temporären Dateien oder Backup-Dateien häufig andere Dateiendungen (zum Beispiel *.bak-Dateien als Sicherheitskopien eines Editors) verwendet werden. Werden diese Dateien vom Webserver abgerufen, wäre es möglich, dass die Dateien aufgrund der unbekannten Dateiendung nicht mehr interpretiert werden und stattdessen der Quelltext der Webanwendung ausgeliefert wird.

Versionsverwaltungssysteme legen zumeist Dateien oder Ordnerstrukturen für die von ihnen verwalteten Objekte an (zum Beispiel Ordner wie *.svn* oder *.git*). Diese Dateien oder Ordner enthalten häufig detaillierte Informationen zu den verwalteten Projekten und ermöglichen unter Umständen einen kompletten Zugriff auf den Quellcode. Aus diesem Grund sollten Anwendungen oder Anwendungskomponenten grundsätzlich nicht über die Versionsverwaltung auf Produktivsysteme aufgespielt werden. Zumindest sollte der Zugriff auf von der Versionsverwaltungssoftware angelegte Dateien und Ordner blockiert werden.

Aus den genannten Gründen sind alle Dateien zu löschen, die für den produktiven Betrieb nicht benötigt werden. Darüber hinaus sollte regelmäßig kontrolliert werden, ob neue Dateien angefallen sind und ob diese gelöscht werden können. Ist dies nicht möglich, kann der Zugriff auf diese Dateien gesperrt werden.

**Sichere Erfassung durch externe Suchmaschinen**

Suchmaschinen setzen sogenannte Agenten (auch Robots oder Crawler genannt) ein, um neue oder geänderte Inhalte im Netz zu indizieren. Diese Agenten können durch die Datei *robots.txt* im Wurzelverzeichnis der Webanwendung instruiert werden, ausgewiesene Ressourcen (zum Beispiel Pfade) der Webanwendung zu ignorieren. Auf diese Weise können schützenswerte Informationen von der Indizierung in der Suchmaschine ausgenommen werden. Die vertraulichen Ressourcen (zum Beispiel Verzeichnis-Pfade) sollten in der Datei *robots.txt* unter der Direktive *Disallow* aufgeführt werden. So werden die Agenten veranlasst, die gelisteten Ressourcen nicht zu indizieren.

Damit die Einträge in der Datei *robots.txt* einem Angreifer keine Hinweise auf sicherheitskritische Ressourcen der Webanwendung geben, sollten alle zu schützenden Verzeichnisse nach Möglichkeit in einem gesonderten Verzeichnis der Webanwendung zusammengefasst werden. Ausschließlich dieses Verzeichnis sollte in die Datei *robots.txt* eingetragen werden, sodass diese keine internen Verzeichnisstrukturen mit sicherheitsrelevanten Informationen enthält.

**Schutz vor Directory-Traversal-Angriffen**

Ein Zugriff auf Ressourcen darf nur mit den dafür benötigten Rechten und nach einer vorausgegangenen Authentisierung erfolgen. Demzufolge sind geeignete Authentisierungsmechanismen zu implementieren sowie strikte Zugriffsregeln (Policies) zu definieren und umzusetzen. Zusätzlich kann ein Intrusion-Detection-System eingesetzt werden, das Directory-Traversal-Angriffe erkennt.

**Vermeidung von Produkt- und Versionsangaben**

Häufig enthalten Antworten und Ausgaben der einzelnen Komponenten der Webanwendung Angaben zu Produktnamen und Versionsnummern. Diese Informationen können zum Beispiel in HTTP-Headern oder in Kommentaren im HTML-Quelltext der ausgelieferten Webseiten enthalten sein. Auf der Grundlage dieser Angaben kann ein Angreifer gezielt nach bekannten Schwachstellen des Produkts suchen und über diese die Webanwendung angreifen. Daher sollten Angaben zu verwendeten Produkten und Versionen vermieden werden (zum Beispiel Applikationsframework, Webserver).

**Verzicht auf absolute Pfadangaben**

Absolute Pfadangaben ermöglichen oft Rückschlüsse auf die interne Struktur und den Aufbau der Webanwendung. So kann beispielsweise der Speicherort schützenswerter Informationen ermittelt werden. Daher sollten nach Möglichkeit keine absoluten Pfadangaben der Webanwendung veröffentlicht werden.

#### APP.3.1.M14 Schutz vertraulicher Daten [Entwickler]

Folgende Maßnahmen sollten zum Schutz vertraulicher Daten bei Webanwendungen getroffen werden. 

**Allgemeine Aspekte**

Werden vertrauliche Daten durch die Webanwendung verarbeitet, übertragen oder gespeichert (server- wie auch clientseitig), sollten sie durch kryptografische Verfahren geschützt werden. Auch falls die Webanwendung kompromittiert ist, sollten die eingesetzten kryptographischen Verfahren diese Daten weiterhin schützen.

Vertrauliche Daten einer Webanwendung sind z. B.:

* Zugangsdaten (z. B. Benutzer, Passwort),
* Authentisierungsdaten (z. B. Session-ID),
* kritische Daten, die von der Webanwendung verarbeitet werden (z. B. Zahlungsinformationen oder Gesundheitsdaten).
Kryptographische Verfahren können bei der Verarbeitung, Übertragung und Speicherung dieser Daten durch die Webanwendung und durch die Clients verwendet werden. Sie können dabei z. B. wie folgt eingesetzt werden:

* Verschlüsselung von Daten,
* sichere Speicherung von Zugangsdaten,
* Schutz des Transportkanals.
Es ist darauf zu achten, kryptographische Algorithmen für den jeweiligen Einsatzzweck auszuwählen, die dem Stand der Technik entsprechen und keine bekannten Schwachstellen aufweisen. Die kryptographischen Algorithmen sollten serverseitig umgesetzt sein.

Eine besondere Bedeutung bei der Kryptographie kommt den verwendeten Schlüsseln zu. Diese müssen je nach Einsatzgebiet über eine gewisse Mindestlänge verfügen und verschiedenen mathematischen Anforderungen (z. B. Komplexität) genügen. Zudem muss für einen entsprechend sicheren Transport beziehungsweise Austausch von Schlüsseln gesorgt werden. Gleiches gilt auch für deren Speicherung. Bei der Gestaltung einer Webanwendung sollten diese Punkte geregelt und in einem Kryptokonzept zusammengefasst werden (siehe CON.1 *Kryptokonzept*).

Für Webanwendungen mit hohem Schutzbedarf kann zusätzlich eine Absicherung der Nutzdaten erforderlich sein. Werden beispielsweise Sozialdaten mit hohen Anforderungen an die Vertraulichkeit von der Webanwendung verarbeitet, können diese Daten von der Webanwendung vor der Speicherung verschlüsselt werden. So ist sichergestellt, dass auch bei einem direkten Zugriff auf die Datenbank (z. B. durch Datenbankadministratoren) keine verwertbaren Daten ausgelesen werden können.

**Sicherer Umgang mit SSL/TLS**

Werden vertrauliche Daten übertragen, können sie durch einen sicheren Transportkanal vor unbefugter Kenntnisnahme oder Manipulation geschützt werden. Bevor vertrauliche Daten übertragen werden, sollte daher zu einer gesicherten Verbindung gewechselt werden. Auch nach der Anmeldung eines Benutzers sollten die übertragenen Daten weiterhin durch eine gesicherte Verbindung geschützt werden. Der Transportkanal wird hierzu üblicherweise durch den Einsatz von SSL/TLS abgesichert. Weitere Hinweise dazu finden sich im Baustein APP.3.2 *Webserver*. 

Darüber hinaus ist darauf zu achten, dass bei Fehlern während des SSL/TLS-Verbindungsaufbaus oder bei der Übertragung von Daten über einen verschlüsselten Kanal nicht zu einer unverschlüsselten Verbindung gewechselt wird. Stattdessen sollte der Verbindungsaufbau erneut erfolgen oder abgelehnt werden. Es muss verhindert werden, dass vertrauliche Daten über eine ungesicherte Verbindung übertragen werden (z. B. durch setzen des Secure-Flags für Cookies).

Beim Aufbau einer SSL/TLS-Verbindung wird der zu verwendende Verschlüsselungsmodus zwischen Client und Server ausgehandelt. Unter den verfügbaren Algorithmen befinden sich auch solche, die nicht mehr als sicher angesehen werden können. Insbesondere gibt es auch den sogenannten Null-Encryption-Modus, bei dem keine Verschlüsselung stattfindet. Bei der Konfiguration des Webservers für die Verwendung von SSL/TLS muss darauf geachtet werden, dass der Server keinen der schwachen Algorithmen und insbesondere nicht den Null-Encryption-Modus akzeptiert. Andernfalls könnte es dazu kommen, dass scheinbar eine sichere Verbindung aufgebaut wird (es wird https verwendet), die jedoch in Wirklichkeit zu schwach oder gar nicht verschlüsselt ist. Eine solche Situation könnte von einem Angreifer bewusst herbeigeführt werden, um Authentisierungsinformationen und andere Daten abzuhören. Daher sollte in der SSL/TLS-Konfiguration des Webservers die Verwendung des Null-Encryption-Modus und der schwachen Algorithmen abgeschaltet werden. 

**Erzwingen der HTTP-POST-Methode**

Bei der Bedienung einer Webanwendung werden üblicherweise Daten (z. B. Formulardaten oder die Session-ID) an die Webanwendung übermittelt. Diese Daten können als Parameter in der URL (GET-Methode) und im Rumpf des HTTP-Requests (POST-Methode) übertragen werden.

Bei der Verwendung der GET-Methode sind vertrauliche Daten wie Formulardaten in der URL sichtbar (z. B. im Browser-Verlauf) und können von zwischengelagerten Systemen protokolliert und gespeichert werden.

Daher sollten schützenswerte Daten ausschließlich über die POST-Methode übertragen werden. Hierbei ist zu berücksichtigen, dass Frameworks häufig die HTTP-Request-Methode abstrahieren. Eine falsche Konfiguration des Frameworks kann dazu führen, dass trotz erzwungener Eingrenzung auf die POST-Methode durch die Webanwendung weiterhin beide Methoden zulässig sind (z. B. über eine Weiterleitung eines HTTP-GET-Requests auf einen HTTP-POST-Request durch das Framework).

**Schutz clientseitig gespeicherter Daten**

Die zwischen dem Client und der Webanwendung ausgetauschten Daten können vom Client im lokalen Browsercache zwischengespeichert werden. Wenn der Browser die Daten über die Sitzungsdauer hinaus im Cache speichert, können diese von Personen mit Zugriff auf den Rechner des Benutzers und von Skripten und Browser-Plugins ohne zusätzliche Zugriffskontrolle aus dem Cache abgerufen werden.

Das clientseitige Zwischenspeichern ("Cachen") von vertraulichen Daten der Webanwendung kann durch folgende Direktiven in den HTTP-Headern der Webanwendung unterbunden werden:

* Cache-Control: *no-cache, no-store*
* Pragma: *no-cache*
* Expires: *-1*
Da der Webbrowser üblicherweise nicht unter der Kontrolle des Betreibers der Webanwendung steht, kann somit nicht vollständig ausgeschlossen werden, dass Daten trotzdem zwischengespeichert werden. Daher kann es für Webanwendungen mit hohem Schutzbedarf zusätzlich erforderlich sein, dass der Benutzer den Browsercache während der Bedienung der Webanwendung deaktiviert oder ihn löscht, sobald er seine Tätigkeiten an der Webanwendung beendet hat. In diesem Fall kann dem Benutzer beispielsweise nach erfolgter Abmeldung ein Hinweis angezeigt werden, dass der Browsercache gelöscht werden soll. Dies betrifft insbesondere Webanwendungen, die von öffentlichen IT-Systemen aus genutzt werden. Alternativ kann der Benutzer auf die Verwendung des Private Modes des Browsers hingewiesen werden, bei dem keine Daten über die Sitzung zwischengespeichert werden.

Häufig werden bei der Bedienung einer Webanwendung Daten in Cookies auf dem Client gespeichert. Bei jedem Zugriff auf die Webanwendung werden diese Cookies transparent für den Benutzer an die Webanwendung übermittelt. Dabei kann es sich auch um schützenswerte Daten wie die Session-ID handeln. Der Zugriff auf Cookies mit vertraulichen Daten sollte daher so weit wie möglich eingegrenzt werden. Wenn Cookies durch die Webanwendung erstellt werden, sollten folgende Cookie-Flags gesetzt sein:

* Domain  
 Das Cookie-Flag sollte nicht gesetzt werden, denn dann werden per Default nur Anfragen der Domain beantwortet, die das Cookie gesetzt hat. Sollte es notwendig sein, dies auch anderen (Sub-)Domains zu ermöglichen, dann sollte die Domäne so weit wie möglich eingeschränkt werden, ohne die Funktionalität der Webanwendung einzuschränken (z. B. *webapp.domain.tld* anstatt *domain.tld*).
* Path  
 Das Path-Attribut beschränkt die Gültigkeit des Cookies auf einen festgelegten Pfad der Webanwendung. Auch das Path-Attribut sollte so weit wie möglich eingeschränkt werden, ohne die Funktionalität der Webanwendung einzuschränken (z. B. */webapp/* anstelle von */*).
* Secure  
 Ist die Direktive Secure gesetzt, so wird das Cookie ausschließlich über verschlüsselte Kommunikationskanäle übertragen, wie z. B. über SSL/TLS.
* HttpOnly  
 Diese Direktive verhindert, dass clientseitige Skripte auf das Cookie zugreifen (z. B. JavaScript). Es ist zu beachten, dass dieses Attribut nicht von allen Browsern unterstützt wird.
Das folgende Beispiel zeigt die Anweisung, mit der ein Cookie unter Verwendung genannter Direktiven erstellt wird:

*Set-Cookie: SESSIONID=sl342kdfjslaal39skdj; path=/webapp; secure; HttpOnly*

Bei der Authentisierung des Benutzers gegenüber einer Webanwendung wird gewöhnlich ein HTML-Formular verwendet, in das der Benutzername und das Passwort eingegeben werden. Wenn der Benutzer sein Passwort in das Passwortfeld eintippt, sollte es nicht im Klartext wiedergegeben, sondern durch sogenannte Wildcards ersetzt werden (z. B. Sterne oder Punkte). Hierfür muss in der Formulardefinition der Passwort-Feld-Typ ausgewählt werden (*type="password"*).

Darüber hinaus kann der Webbrowser angewiesen werden, vertrauliche Formulardaten (z. B. den Benutzernamen und das Passwort) nicht zwischenzuspeichern und beim nächsten Aufruf des Formulars als Auswahl vorschlagen. Die Option *autocomplete="Off"* sollte hierfür bei der Definition des Formulars im Formularkopf gesetzt werden.

Während der Sitzung eines Benutzers an einer Webanwendung müssen in der Regel benutzerspezifische Daten gespeichert werden (z. B. die Artikel im Warenkorb). Diese Daten können dabei nicht nur serverseitig, sondern auch clientseitig in einem Cookie oder im Web-Storage des Browsers gespeichert werden. Grundsätzlich sollte vermieden werden, vertrauliche Daten an den Client zu übertragen oder auf dem Client zu speichern, da die Webanwendung keinen Einfluss auf den Schutz von clientseitig hinterlegten Daten hat. So können vom Browser auf dem Client umgesetzte Sicherheitsmechanismen zum Schutz der Daten häufig umgangen werden (z. B. durch direkten Zugriff auf das Dateisystem durch lokale Benutzer oder durch Cross-Site-Scripting). Stattdessen sollten vertrauliche Daten grundsätzlich serverseitig gespeichert werden und ausschließlich das Identifikationsmerkmal des Benutzers (z. B. die Session-ID) clientseitig hinterlegt sein.

Falls es sich nicht vermeiden lässt, die Sitzungsdaten clientseitig zu speichern, sollten diese Daten verschlüsselt und vor der Verarbeitung durch die Webanwendung auf Integrität geprüft werden. Damit wird sichergestellt, dass die Daten während der Übertragung nicht unbefugt eingesehen oder unbemerkt manipuliert werden können.

Darüber hinaus sollten die Daten vorzugsweise nur über den Zeitraum der Sitzung und nicht persistent gespeichert werden. Beim Web-Storage-Mechanismus sollte daher das sessionStorage-Objekt vor dem localStorage-Objekt bevorzugt werden.

**Schutz serverseitig hinterlegter Daten**

Sollen sich Benutzer an der Webanwendung anmelden können, müssen Zugangsdaten auf der Webanwendung gespeichert werden. Damit auch nach einer möglichen Kompromittierung der Webanwendung durch einen Angreifer die Zugangsdaten geschützt sind, dürfen sie nicht im Klartext gespeichert werden. Stattdessen sollten sie mithilfe von zeitgemäßen kryptografischen Algorithmen als* salted Hashes* hinterlegt werden, bei denen eine zufällige Zeichenfolge an den Klartext angehängt wird. Hierbei sollte für jedes Passwort ein unterschiedlicher, zufälliger Salt verwendet werden.

Darüber hinaus sollten die Zugangsdaten serverseitig auf einem vertrauenswürdigen IT-System (z. B. auf dem der Webanwendung) und in einem geschützten Bereich (z. B. außerhalb des Web-Root-Verzeichnisses oder in separaten Datenbanktabellen) hinterlegt sein. Die Zugangsdaten sollen nicht im Quelltext der Webanwendung (Hardcoded Passwords) gespeichert werden.

Darüber hinaus sollte ausschließlich die Webanwendung mit Schreibrechten auf die Zugangsdaten zugreifen können. Die Zugangsdaten sollten nur durch den Benutzer und über die vorgesehenen Schnittstellen und Funktionen der Webanwendung geändert werden können, sodass es Benutzern nicht möglich ist, Zugangsdaten unbefugt z. B. über den direkten Zugriff auf das Dateisystem zu lesen, zu ändern oder zu löschen.

Ruft ein Benutzer eine Webseite von der Webanwendung auf, so wird die Seite in der Regel von der Anwendung zur Laufzeit erstellt. Die aufgerufene Datei enthält Code, der von der Webanwendung vor der Auslieferung interpretiert wird und eine Webseite zurückliefert. Diese Webseite wird an den Benutzer übermittelt.

Üblicherweise werden anhand der Datei-Endung diese Dateitypen einem Interpreter oder Parser zugeordnet. Ändert sich die Datei-Endung, werden diese möglicherweise an den Benutzer übertragen, ohne vorher interpretiert zu werden. Werden derartige Dateien abgerufen, erhält der Benutzer Einsicht in die Programmlogik und in vertrauliche Informationen, die eventuell im Code gespeichert sind. Dies kann beliebige Dateien betreffen, deren Datei-Endung nicht einem Interpreter oder Parser zugeordnet ist. Beispiele für anfällige Dateien sind:

* temporäre Dateien (z. B. *temp.tmp*),
* Backup Daten (z. B. *backup.bak*),
* Konfigurationsdateien (z. B. *config.conf*),
* einzubindende Dateien (z. B. *include.inc*).
Die Dateien können vertrauliche Informationen wie Zugangsdaten enthalten, die bei unzureichender Zugriffsbeschränkung abgerufen werden können.

Daher sollten Dateien, die nicht für die Interpretation und den direkten Abruf durch den Benutzer vorgesehen sind, von der Webanwendung nicht ausgeliefert werden. Zusätzlich sollten die Dateisystemberechtigungen auf diese Dateien restriktiv gesetzt sein. Nicht mehr benötigte Dateien sollten zeitnah gelöscht werden (siehe auch APP.3.1.M12 *Sichere Konfiguration von Webanwendungen*, Absatz Löschen nicht benötigter Dateien).

**Speicherung von Konfigurationsdateien außerhalb von Web-Root**

Konfigurationsdateien der Webanwendung enthalten häufig schützenswerte Informationen, wie z. B. Zugangsdaten. Daher sollten die Benutzer der Webanwendung nicht auf die Konfigurationsdateien zugreifen können.

Aus diesem Grund sollten Konfigurationsdateien ausschließlich außerhalb des Webserver-Root-Verzeichnisses gespeichert werden. Außerhalb dieses Verzeichnisses werden in der Regel keine Daten von der Webanwendung ausgeliefert.

Grundsätzlich müssen Konfigurationsdaten außerhalb des Quelltextes in separaten Konfigurationsdateien gespeichert werden. Konfigurationseinstellungen, die vertrauliche Daten beinhalten, sollten zudem verschlüsselt werden.

#### APP.3.1.M15 Verifikation essentieller Änderungen

Sollen wichtige Einträge geändert werden, wie beispielsweise Passwörter und Konfigurationen, sollte die Eingabe durch ein Passwort erneut verifiziert werden. Die Benutzer sollten über Änderungen mittels Kommunikationswege außerhalb der Web-Anwendung informiert werden, beispielsweise per E-Mail.

#### APP.3.1.M16 Umfassende Ein- und Ausgabevalidierung [Entwickler]

Durch eine zuverlässige und gründliche Filterung der Ein- und Ausgabedaten von Webanwendungen mittels einer Validierungskomponente kann ein wirksamer Schutz vor gängigen Angriffen erreicht werden. Hierbei sollten sowohl die Eingabedaten von Benutzern an die Webanwendung als auch die Ausgabedaten der Webanwendung an die Clients oder an nachgelagerte Systeme, wie zum Beispiel Datenbanken, gefiltert und transformiert (output encoding) werden. Dadurch wird sichergestellt, dass nur erwartete und keine schadhaften Daten verarbeitet oder ausgegeben werden.

Ist es für einzelne Funktionen notwendig, den Datenfilter weniger restriktiv zu setzen, muss dies explizit beim Zugriff auf die Daten definiert und dokumentiert werden. Zusätzlich ist es möglich, kontextsensitive Filter in der Geschäftslogik der Anwendung oder in den Hintergrundsystemen zu nutzen.

Für eine sichere Verarbeitung der Daten sollten folgende Punkte bei der Umsetzung und der Konfiguration der Validierungskomponente berücksichtigt werden:

**Identifizierung der Daten**

Damit die Ein- und Ausgabedaten umfassend validiert werden können, müssen zunächst alle zu verarbeitenden Datenstrukturen (zum Beispiel E-Mail-Adresse) und die darin zulässigen Werte identifiziert werden. Für jede Datenstruktur sollte eine entsprechende Validierungsroutine umgesetzt werden. Neben der Datenstruktur sollte auch die Art und Weise der Datenverarbeitung erfasst werden, zum Beispiel Weiterleitung an einen Interpreter, Rückgabe an den Client, Speicherung in einer Datenbank.

**Berücksichtigung aller Daten und Datenformate**

Die Validierungskomponente sollte alle zu verarbeitenden Datenformate und verwendeten Interpreter berücksichtigen. Typische Datenformate bei Webanwendungen sind zum Beispiel personenbezogene Daten (Name, Telefonnummer, Postleitzahl), Bilder, PDF-Dateien und formatierte Texte. Typische Interpreter für Daten, die von Webanwendungen verarbeitet oder ausgegeben werden, sind zum Beispiel HTML-Renderer, SQL-, XML-, JSON-, LDAP-Interpreter und das Betriebssystem.

Daten können durch unterschiedliche Techniken auf ihre Gültigkeit geprüft werden. So kann die Validierungskomponente den Wertebereich der Eingaben überprüfen oder es können beispielsweise reguläre Ausdrücke verwendet werden, um erlaubte Zeichen und die Länge der erwarteten Daten zu validieren. Die Gültigkeit von XML-Daten kann unter anderem mithilfe des entsprechenden XML-Schemas überprüft werden. Darüber hinaus stellen Frameworks und Bibliotheken für gängige Datenformate entsprechende Validierungsfunktionen bereit.

Die folgenden Zeichen werden gewöhnlich von in Webanwendungen eingesetzten Programmen interpretiert und können daher von potenziellen Angreifern benutzt werden, um Schadcode einzuschleusen. Aus diesem Grund sollten sie bei der Filterung berücksichtigt werden:

Nullwert, Zeilenvorschub, Wagenrücklauf, Hochkomma, Komma, Schrägstriche, Leerzeichen, Tabulator-Zeichen, größer als und kleiner als, XML- und HTML-Tags. (Die Aufzählung ist nicht vollständig.)

Zudem können die Interpreter-Zeichensätze (zum Beispiel SQL-Syntax) bei unterschiedlichen Produkten variieren. Beispiele für kritische Zeichen werden im Abschnitt *Potenziell gefährliche Zeichen für Interpreter* in *Hilfsmittel zum Baustein Webanwendungen* [GSSID] aufgeführt.

Neben den eigentlichen Nutzdaten (zum Beispiel Formular-Parameter in GET- oder POST-Variablen) sind auch Daten anderer Herkunft (Sekundärdaten) zu validieren. Dazu zählen beispielsweise:

* Namen von Form-Variablen (Sie können ebenso wie der Wert der Form-Variablen beliebig manipuliert werden),
* HTTP-Header-Felder (Header-Felder in HTTP-Requests und -Responses sollten ausschließlich ASCII-Zeichen enthalten und zum Beispiel keine Zeilenvorschubzeichen wie *\r\n*),
* Session-IDs (zum Beispiel aus Cookies).
Automatisierte Aufrufe durch den Client zum Beispiel durch Ajax- beziehungsweise Flash-Skripte oder JSON-Requests sind ebenfalls zu prüfen.

Bei den Hintergrundsystemen ist eine (falls erforderlich erneute) Validierung der Daten vorzunehmen. Dies gilt auch dann, wenn Daten beispielsweise nach einem erfolgten Schreibvorgang in die Datenbank wieder ausgelesen werden, da die Daten auch in der Datenbank zwischenzeitlich geändert worden sein können.

Schädlicher Code kann aber auch über einen Weg übermittelt werden, der nicht von der Webanwendung kontrolliert werden kann (zum Beispiel FTP, NFS). Kann ein Angreifer über diese Dienste Dateien ändern oder erzeugen, die von der Webanwendung integriert werden, so kann er Schadcode über diesen Umweg einbetten. Bei dem sogenannten Cross-Channel-Scripting wird auf diese Weise JavaScript-Code eingefügt, der ähnlich wie bei persistentem Cross-Site-Scripting vom Browser ausgeführt wird. Daher sollten unabhängig von der Quelle immer alle Daten vor der Ausgabe an die Benutzer oder der Weiterverarbeitung durch die Anwendung validiert werden.

**Serverseitige Validierung**

Üblicherweise greifen die Benutzer mit generischen Clients (zum Beispiel Webbrowser) auf die Webanwendung zu. Diese Clients befinden sich nicht im Sicherheitskontext der Webanwendung, sondern stehen unter der Kontrolle der Benutzer. Die Datenvalidierung ist daher als serverseitiger Sicherheitsmechanismus auf einem vertrauenswürdigen IT-System umzusetzen.

Werden Daten zusätzlich durch Code von der Webanwendung clientseitig verarbeitet (zum Beispiel JavaScript-Code), so sollten diese Daten auch auf dem Client validiert werden. Die ausgelieferten Skripte der Webanwendung sollten hierbei die entsprechenden Validierungsroutinen mitliefern. Werden die Daten im nachgelagerten Verarbeitungsprozess an den Server gesendet, so ist zu beachten, dass die clientseitige Prüfung die serverseitige Validierung nicht ersetzen kann.

**Validierungsansatz**

Bei der Datenvalidierung wird zwischen dem White-List- und dem Black-List-Ansatz unterschieden.

Bei einem White-List-Ansatz werden ausschließlich solche Daten zugelassen, die in der Liste enthalten sind. Dabei werden, ausgehend von einer möglichst kleinen Zeichenmenge, Regeln erstellt, die Daten in einem festgelegten Zeichenraum zulassen und Daten zurückweisen, die abweichende Zeichen enthalten. Hierbei sollten komplexe Regeln durch die sequenzielle Verwendung einfacher Regeln abgebildet werden.

Dagegen werden bei einem Black-List-Ansatz solche Daten als unzulässig eingestuft und abgewiesen, die in der Liste enthalten sind. Alle Daten, die nicht explizit verboten sind, werden bei diesem Ansatz akzeptiert.

Bei dem Black-List-Ansatz besteht jedoch die Gefahr, dass nicht alle Variationen unzulässiger Daten berücksichtigt und somit erkannt werden. Daher sollte der White-List-Ansatz dem Black-List-Ansatz vorgezogen werden.

**Kanonisierung vor der Validierung**

Daten können in verschiedenen Kodierungen (zum Beispiel UTF-8, ISO 8859-1) und Notationen (zum Beispiel bei UTF-8 ist *"." = "2E" = "C0 AE"*) vorliegen. Abhängig vom angewendeten Kodierungsschema kann der gleiche Wert demnach unterschiedlich interpretiert werden. Werden die Daten ohne Berücksichtigung der Kodierung und der Notation validiert, so werden eventuell schädliche Daten nicht erkannt und gefiltert. Daher sollten alle Daten vor der Validierung in eine einheitliche, normalisierte Form überführt werden. Dieser Vorgang wird als Kanonisierung der Daten bezeichnet. Die so dargestellten Daten werden dann weiterverarbeitet. Wird AJAX verwendet, sollte zudem mittels der Eigenschaft *textContent* anstatt von *innerHTML* nachgeladen werden, da *textContent *automatisch eine Enkodierung vornimmt.

Darüber hinaus sollte die Webanwendung das Kodierungsschema explizit setzen, wenn sie Daten ausliefert (zum Beispiel über den Content-Type-Header: *charset=ISO-8859-1*). 

**Kontextsensitive Maskierung der Daten**

Falls potenziell schädliche Daten von einer Webanwendung verarbeitet werden müssen (zum Beispiel Zeichen mit einer Bedeutung für verwendete Interpreter) und somit eine Filterung nicht durchgeführt werden kann, müssen diese Daten maskiert und so in eine andere Darstellungsform überführt werden. In dieser maskierten Form werden die Daten nicht mehr als ausführbarer Code interpretiert. Da die Maskierung Interpreter-spezifisch ist, müssen alle verwendeten Interpreter berücksichtigt werden (zum Beispiel SQL, LDAP). Demnach muss kontextsensitiv für das erwartete Ein- und Ausgabeformat und die Interpretersprache maskiert werden. Aufgrund der Komplexität und der spezifischen Anforderungen unterschiedlicher Interpretersprachen wird empfohlen, für die Maskierung spezialisierte Bibliotheken einzusetzen.

Prinzipiell sollten alle Zeichen maskiert werden, die als unsicher für den beabsichtigten Interpreter eingestuft werden. Dazu zählen zum Beispiel:

* unerwartetes JavaScript und HTML zur Auslieferung an den Client (zum Beispiel den Webbrowser),
* unerlaubt eingefügte SQL-Statements an die Datenbank (zum Beispiel aus Eingaben in Formularfeldern),
* Befehle an das Betriebssystem (zum Beispiel in manipulierten HTTP-Variablen).
Maskiert wird, indem die betroffenen Daten beziehungsweise Metazeichen der jeweiligen Interpretersprache in sogenannte Zeichenreferenzen überführt werden. Das folgende Beispiel zeigt ausgewählte HTML-Zeichen mit den entsprechenden Zeichenreferenzen (engl. HTML-Entities):

* *&* => *&amp; *
* *<* => *&lt;*
* *>* => *&gt;*
* *"* => *&quot;*
* *'* => *&#39;*
Hier ist darauf zu achten, dass *&*-Zeichen im ersten Durchlauf ersetzt werden und dass keine Mehrfach-Maskierung erfolgt, da dieses Zeichen in anderen Zeichenreferenzen als Metazeichen wiederverwendet wird.

**Verwendung eines eigenen Markups zur Filterung von HTML-Tags**

Falls die Webanwendung HTML-Formatierungstags in Benutzereingaben erfordert (zum Beispiel zur Formatierung von Benutzer-Beiträgen), sollten erlaubte HTML-Tags von problematischen Tags unterschieden und gefiltert werden (siehe auch Abschnitt Kontextsensitive Maskierung der Daten).

Bei diesem Ansatz besteht das hohe Risiko, problematische Tags (beispielsweise *<script>*) zu übersehen. Auch scheinbar harmlose Tags lassen sich teilweise über Attribute wie *onMouseOver* zur Ausführung von Code missbrauchen. Daher sollte der alternative Ansatz, für das Markup des Benutzers eigene Markup-Tags zu definieren (zum Beispiel BBCode), vorgezogen werden. Diese Markup-Tags werden dann von der Anwendung in die zugehörigen HTML-Tags übersetzt. Herkömmliche Tags beziehungsweise problematische Zeichen werden nach wie vor gefiltert.

Ein mögliches Verfahren, wenn ein einfaches Markup zugelassen werden soll, ist die Verwendung von *{* und *}* statt *<* und *>*. Fett würde dann als *{F}**Dies ist fett**{/F}* geschrieben und ein Bild könnte auf diese Weise platziert werden: *{img src=/images/img.gif width=1 height=1 img}*.

Hierbei darf die Umwandlung in HTML nicht einfach geschweifte Klammern durch spitze Klammern ersetzen, sondern muss jedes Tag als Ganzes ansehen: 

* *{img* nach *<img*,
* *img}* nach *>*,
* *src=Datei* nach *src="Datei"* (wobei Datei zusätzlich zu filtern ist).
Wenn HTML-Tags zugelassen sind, ist grundsätzlich darauf zu achten, dass mindestens die folgenden Tags nicht erlaubt sind:

* applet
* base
* iframe
* link
* object
* script
* style
Mithilfe dieser Tags können beliebige Inhalte in die Webseite eingefügt werden. Diese dürfen daher nicht genutzt werden können.

**Abwehr von Code-Injections in SOAP-Nachrichten**

Allgemein sollten nie Eingaben ohne vorherige Prüfung weitergegeben werden. Um Injection-Angriffe zu vermeiden, ist es notwendig, Eingabeparameter aus der Schnittstellenbeschreibung (WSDL-Datei) heraus auf schädlichen Code zu filtern und zum Beispiel über eine Whitelist nur systemkonforme Strings zuzulassen. Empfohlen wird außerdem, Strings als Eingabetyp möglichst komplett zu vermeiden und zudem Integer-Werte auf deren Länge zu überprüfen.

**Behandlung von Fehleingaben (Sanitizing)**

Anstatt Daten aufgrund eines unerwarteten Datenformats oder Zeichens abzulehnen, können Fehleingaben korrigiert und automatisch transformiert werden (engl. sanitize). Dadurch soll eine benutzerfreundliche Eingabe der Daten in unterschiedlichen Schreibweisen ermöglicht werden. Für eine Weiterverarbeitung lassen sich die Daten von unerwarteten Zeichen säubern (zum Beispiel die Telefonnummer *(0049)-201-12345678* kann in das nur aus Zahlen bestehende Format *004920112345678* überführt werden).

Eine Säuberung kann darin bestehen, Zeichen zu löschen, zu ersetzen oder zu maskieren (siehe auch Abschnitt Kontextsensitive Maskierung der Daten).

Beim Sanitizing besteht die Gefahr, dass Änderungen an den Daten zu einer neuen Komplexität, neuen Angriffsvektoren oder einer Missinterpretation führen. Daher sollte Sanitizing möglichst vermieden und nur in Fällen angewendet werden, in denen ein Missbrauch des Sanitizing ausgeschlossen werden kann.

Falls die Webanwendung fehlerhafte Daten erkannt hat, sollten Fehler, die auf eine bewusste Manipulation hindeuten (zum Beispiel eine veränderte Session-ID) nicht automatisch korrigiert, sondern abgelehnt werden. Darüber hinaus sollten Eingabedaten, die mit bestimmungsgemäßer Browser- beziehungsweise Client-Bedienung nicht eintreten können, grundsätzlich abgelehnt werden. Dazu zählen zum Beispiel:

* zusätzliche oder fehlende Formular-Parameter,
* Session-Cookies mit unerwarteten Zeichen oder ungültiger Länge,
* unerwartete Werte bei der Übertragung von Formular-Parametern aus vordefinierten HIDDEN-, SELECT- oder CHECKBOX-Feldern,
* abweichender oder unerwünschter Übertragungsweg der Parameter (zum Beispiel GET, POST, Cookie).
Bei einer Säuberung der Daten sollte die geschachtelte Eingabe von Angriffsvektoren berücksichtigt werden. Problematisch ist zum Beispiel der auf den ersten Blick vernünftig erscheinende Filter *s/<script>//g;* (hier in Perl RegEx-Syntax geschrieben), um <script>-Tags im Eingabestrom zu löschen. Dieser kann jedoch mit einer geschachtelten Eingabe (zum Beispiel *<sc<script>ript>*) umgangen werden. Es ist daher rekursiv zu filtern. Im Zweifelsfall sind die Eingabedaten abzulehnen.

Grundsätzlich sollte bei einer Ablehnung der Daten die angeforderte Aktion ebenfalls abgebrochen und eine neutrale Fehlermeldung ausgegeben werden (siehe auch APP.3.1.M13* Restriktive Herausgabe sicherheitsrelevanter Informationen*). Bei Webanwendungen mit hohem Schutzbedarf sollte zusätzlich die Sitzung abgebrochen werden.

#### APP.3.1.M17 Fehlerbehandlung [Entwickler]

Tritt während des Betriebs einer Webanwendung ein Fehler auf, sollte dieser so behandelt werden, so dass ein konsistenter Zustand der Webanwendung gewährleistet ist und der Schutz der Daten aufrechterhalten wird. Eine Webanwendung ist in einem inkonsistenten Zustand, wenn sie aufgrund eines Fehlers in einen unerwarteten Zustand überführt wird und dadurch Daten unkontrolliert verarbeitet werden (zum Beispiel keine Fehlermeldung bei erfolgloser Speicherung von Daten).

Der konsistente Zustand einer Webanwendung kann unter anderem durch folgende Ereignisse gefährdet werden: 

* die Anwendung stürzt ab,
* eine Transaktion wird auf Anwendungsebene unvollständig durchgeführt,
* eine Aktion wird trotz eines Fehlers durchgeführt (zum Beispiel bei unvollständigen Prüfungen durch Sicherheitskomponenten),
* Dienste werden verhindert (Denial-of-Service),
* Rechte werden ausgeweitet (privilege escalation),
* Schadcode wird ausgeführt (code execution).
Folgende Punkte sollten bei der Fehlerbehandlung berücksichtigt werden:

* **Vermeidung vertraulicher Informationen in Fehlermeldungen:** Die Webanwendung muss dem Benutzer im Falle eines Fehlers neutrale, angepasste Fehlerseiten ausgeben, die keine vertraulichen Informationen beinhalten. Siehe hierzu auch *APP.3.1.*M13* Restriktive Herausgabe sicherheitsrelevanter Informationen*.
* **Protokollierung der Fehler:** Um aufgetretene Fehler vollständig nachvollziehen zu können, müssen diese als Ereignis gemäß APP.3.1.M5 *Protokollierung sicherheitsrelevanter Ereignisse von Webanwendungen* protokolliert werden.
* **Abbruch des Vorgangs nach Auftreten eines Fehlers:** Treten Fehler im Zusammenhang mit Sicherheitskomponenten der Webanwendung auf (zum Beispiel während der Autorisierung oder Authentisierung), muss die veranlasste Aktion abgebrochen und der Zugriff auf die angeforderte Ressource oder Funktion abgewiesen werden. Es muss gewährleistet sein, dass durch provozierte Fehler keine Sicherheitsmechanismen umgangen werden können. Für Webanwendungen mit einem hohen Schutzbedarf sollte zusätzlich in Betracht gezogen werden, eine bestehende Sitzung zwangsweise abzubrechen (siehe auch APP.3.1.M3 *Sicheres Session-Management*).
* **Freigabe von reservierten Ressourcen:** Im laufenden Betrieb belegen Webanwendungen Ressourcen wie zum Beispiel Netz- oder Datei-Streams, um auf Hintergrundsysteme, zwischengespeicherte Zustände oder sonstige Daten zuzugreifen. Solange die Webanwendung auf diese Ressourcen zugreift, sind diese in der Regel für deren exklusiven Zugriff reserviert und können von anderen Prozessen nicht verwendet werden. Tritt ein Fehler auf, sollten zuvor reservierte Ressourcen (zum Beispiel ein Datei-Handle auf eine temporäre Datei) im Rahmen der Fehlerbehandlung freigegeben werden. Darüber hinaus sind zwischengespeicherte Daten bei der Fehlerbehandlung zu löschen.
* **Unmittelbare Behandlung von Fehlern:** Interne Fehler sollten von der Webanwendung selbst behandelt werden. Die Weiterleitung eines unbehandelten Fehlers an andere Komponenten (zum Beispiel Applikationsserver oder nachgelagerte Web-Services) kann zu einem Verlust von Informationen führen, die zur Behandlung des Fehlers notwendig sind (zum Beispiel zur Freigabe von gebundenen Ressourcen). Daher sollten unbehandelte Fehler nicht weitergeleitet werden.
* **Vermeidung einer zu hohen Fehlertoleranz:** Sind Ursachen von Fehlerzuständen nicht vollständig geklärt, sollte der Fehler nicht etwa mit Rücksicht auf die Bedienungsfreundlichkeit toleriert werden. Im Zweifelsfall ist die Aktion abzubrechen. Bei schwerwiegenden Fehlern sollte immer abgebrochen werden.
Das Ziel sind robuste und fehlertolerante Webanwendungen, die bestimmungsgemäße Bedienung durch den Benutzer von offensichtlichen Missbrauchsversuchen und schwerwiegenden Fehlern unterscheiden und dann angemessen reagieren können.

#### APP.3.1.M18 Kontrolle der Protokolldateien

Die Protokollierung sicherheitsrelevanter Ereignisse ist als Sicherheitsmaßnahme nur wirksam, wenn die protokollierten Daten in regelmäßigen Abständen durch einen Revisor ausgewertet werden. Ist es personell oder technisch nicht möglich, die Rolle eines unabhängigen Revisors für Protokolldateien zu etablieren, kann ihre Auswertung auch durch den Administrator erfolgen. Für diesen Fall ist zu beachten, dass damit die Tätigkeiten des Administrators nur schwer kontrollierbar sind. Das Ergebnis der Auswertung sollte daher dem Sicherheitsbeauftragten, dem IT-Verantwortlichen oder einem anderen besonders zu bestimmenden Mitarbeiter vorgelegt werden.

Die regelmäßige Kontrolle dient darüber hinaus auch dem Zweck, durch die anschließende Löschung der Protokolldaten ein übermäßiges Anwachsen der Protokolldateien zu verhindern. Je nach Art der Protokolldaten kann es sinnvoll sein, diese auf externen Datenträgern zu archivieren.

Da Protokolldateien in den meisten Fällen personenbezogene Daten beinhalten, ist sicherzustellen, dass diese Daten nur zum Zweck der Datenschutzkontrolle, der Datensicherung oder zur Sicherstellung eines ordnungsgemäßen Betriebes verwendet werden (siehe § 14 Abs. 4 BDSG und Abschnitt *Datenschutzaspekte bei der Protokollierung*). Der Umfang der Protokollierung und die Kriterien für deren Auswertung sollte dokumentiert und innerhalb der Organisation abgestimmt werden.

Aus verschiedenen gesetzlichen Regelungen können sich einerseits Mindestaufbewahrungsfristen, aber andererseits auch Höchstaufbewahrungsfristen für Protokolldaten ergeben. So kann durch datenschutzrechtliche Regelungen eine Löschung erforderlich sein (siehe dazu auch Abschnitt *Datenschutzaspekte bei der Protokollierung*).

Für bestimmte Protokolldaten gelten aber unter Umständen gesetzliche Mindestaufbewahrungsfristen, z. B. wenn sie Aufschluss über betriebswirtschaftliche Vorgänge geben. Diese Fristen müssen auf jeden Fall eingehalten werden. Bevor Protokolldaten gelöscht werden, ist daher sorgfältig zu prüfen, ob entsprechende Rechtsvorschriften zu beachten sind und welche Aufbewahrungsfristen sich daraus ergeben. Hierbei sollte die Rechtsabteilung beteiligt werden.

Die nachfolgenden Auswertungskriterien dienen als Beispiele, die Hinweise auf eventuelle Sicherheitslücken, Manipulationsversuche und Unregelmäßigkeiten erkennen lassen:

* Liegen die Zeiten des An- und Abmeldens außerhalb der Arbeitszeit (Hinweis auf Manipulationsversuche)?
* Häufen sich fehlerhafte Anmeldeversuche (Hinweis auf den Versuch, Passwörter zu erraten)?
* Häufen sich unzulässige Zugriffsversuche (Hinweis auf Versuche zur Manipulation)?
* Gibt es auffällig große Zeitintervalle, in denen keine Protokolldaten aufgezeichnet wurden (Hinweis auf eventuell gelöschte Protokollsätze)?
* Ist der Umfang der protokollierten Daten zu groß (eine umfangreiche Protokolldatei erschwert es, Unregelmäßigkeiten zu finden)?
* Gibt es auffällig große Zeitintervalle, in denen anscheinend kein Benutzerwechsel stattgefunden hat (Hinweis darauf, dass Benutzer sich nicht konsequent nach Arbeitsende abmelden)?
* Gibt es auffallend lange Verbindungszeiten in öffentliche Netze hinein?
* Wurde in einzelnen Netzsegmenten oder im gesamten Netz eine auffällig hohe Netzlast oder eine Unterbrechung des Netzbetriebes festgestellt (Hinweis auf Versuche, die Dienste des Netzes zu verhindern bzw. zu beeinträchtigen oder auf eine ungeeignete Konzeption bzw. Konfiguration des Netzes)?
Bei der Auswertung der Protokolldateien sollte besonderes Augenmerk auf alle Zugriffe gelegt werden, die unter Administratorkennungen durchgeführt wurden.

Wenn regelmäßig umfangreiche Protokolldateien auszuwerten sind, sollte hierfür ein Werkzeug benutzt werden. Dieses Werkzeug sollte wählbare Auswertungskriterien zulassen und besonders kritische Einträge (z. B. mehrfacher fehlerhafter Anmeldeversuch) hervorheben.

**Datenschutzaspekte bei der Protokollierung**

Unter Protokollierung beim Betrieb von IT-Systemen ist im datenschutzrechtlichen Sinn die Erstellung von manuellen oder automatisierten Aufzeichnungen zu verstehen, aus denen sich die Fragen beantworten lassen: "Wer hat wann mit welchen Mitteln was veranlasst bzw. worauf zugegriffen?" Außerdem müssen sich Systemzustände ableiten lassen: "Wer hatte von wann bis wann welche Zugriffsrechte?"

Art und Umfang von Protokollierungen hängen vom allgemeinen Datenschutzrecht und auch von bereichsspezifischen Regelungen ab.

Die Protokollierung der Administrationsaktivitäten entspricht einer Systemüberwachung, während die Protokollierung der Benutzeraktivitäten im wesentlichen der Verfahrensüberwachung dient. Dementsprechend finden sich die Anforderungen an die Art und den Umfang der systemorientierten Protokollierung überwiegend im allgemeinen Datenschutzrecht, während die verfahrensorientierte Protokollierung oft durch bereichsspezifische Regelungen definiert wird. Beispiele für verfahrensorientierte Protokollierung sind Meldegesetze, Polizeigesetze, Verfassungsschutzgesetze.

**Mindestanforderungen an die Protokollierung**

Bei der Administration von Webanwendungen sind die folgenden Aktivitäten vollständig zu protokollieren:

* **Systemgenerierung und Modifikation von Systemparametern**  
 Da auf dieser Ebene in der Regel keine systemgesteuerten Protokolle erzeugt werden, bedarf es entsprechender detaillierter manueller Aufzeichnungen, die mit der Systemdokumentation korrespondieren sollten.
* **Einrichten von Benutzern**  
 Wem von wann bis wann durch wen das Recht eingeräumt worden ist, die betreffende Webanwendung zu benutzen, ist vollständig zu protokollieren. Für diese Protokolle sollten längerfristige Aufbewahrungszeiträume vorgesehen werden, da sie Grundlage praktisch jeder Revisionsmaßnahme sind.
* **Erstellung von Rechteprofilen**  
 Im Rahmen der Protokollierung der Benutzerverwaltung kommt es insbesondere auch darauf an aufzuzeichnen, wer die Anweisung zur Einrichtung bestimmter Benutzerrechte erteilt hat.
* **Einspielen und Änderung von Anwendungssoftware**  
 Die Protokolle repräsentieren das Ergebnis der Programm- und Verfahrensfreigaben.
* **Änderungen an der Dateiorganisation**  
 Im Hinblick auf die vielfältigen Manipulationsmöglichkeiten, die sich bereits bei Benutzung der "Standard-Dateiverwaltungssysteme" ergeben, kommt einer vollständigen Protokollierung eine besondere Bedeutung zu (siehe z. B. Datenbankmanagement).
* **Durchführung von Datensicherungsmaßnahmen**  
 Da derartige Maßnahmen (Backup, Restore) mit der Anfertigung von Kopien bzw. dem Überschreiben von Datenbeständen verbunden sind und häufig in "Ausnahmesituationen" durchgeführt werden, besteht eine erhöhte Notwendigkeit zur Protokollierung.
* **Sonstiger Aufruf von Administrations-Tools**  
 Die Benutzung aller Administrations-Tools ist zu protokollieren, um feststellen zu können, ob Unbefugte sich Systemadministrator-Rechte erschlichen haben.
* **Versuche unbefugten Einloggens und Überschreitung von Befugnissen**  
 Der vollständigen Protokollierung aller Auffälligkeiten beim Einloggen und der Benutzung von Komponenten kommt eine zentrale Bedeutung zu. Benutzer in diesem Sinne ist auch der Systemadministrator.
Werden personenbezogene Daten verarbeitet, sind abhängig vom Schutzbedarf der Verfahren bzw. Daten folgende Benutzeraktivitäten vollständig bzw. selektiv zu protokollieren:

* **Eingabe von Daten**  
 Auch wenn Befugnisüberschreitungen anderweitig protokolliert werden, sollte eine vollständige Protokollierung von Dateneingaben als Regelfall angesehen werden.
* **Datenübermittlungen**  
 Nur soweit nicht gesetzlich eine vollständige Protokollierung vorgeschrieben ist, kann eine selektive Protokollierung als ausreichend angesehen werden.
* **Benutzung von automatisierten Abrufverfahren**  
 In der Regel dürfte eine vollständige Protokollierung der Abrufe und der Gründe der Abrufe (Vorgang, Aktenzeichen etc.) erforderlich sein, um unbefugte Kenntnisnahme im Rahmen der grundsätzlich eingeräumten Zugriffsrechte aufdecken zu können.
* **Löschung von Daten**  
 Werden Daten gelöscht, ist dies zu protokollieren.
* **Aufruf von Programmen**  
 Dies kann erforderlich sein bei besonders schützenswerten Webanwendungen, die z. B. nur zu bestimmten Zeiten oder Anlässen benutzt werden dürfen. Deshalb ist in diesen Fällen eine vollständige Protokollierung angezeigt. Die Protokollierung dient auch der Entlastung der befugten Benutzer (Nachweis des ausschließlich befugten Aufrufs der Programme).
**Zweckbindung bei der Nutzung von Protokolldaten**

Protokolldaten unterliegen aufgrund der nahezu übereinstimmenden Regelungen im Datenschutzrecht des Bundes und der Länder einer besonderen engen Zweckbindung. Sie dürfen nur zu den Zwecken genutzt werden, die Anlass für ihre Speicherung waren. Dies sind in der Regel die in einem Sicherheitskonzept festgelegten allgemeinen Kontrollen, die in den meisten Datenschutzgesetzen geforderte Überwachung der ordnungsgemäßen Anwendung der Datenverarbeitungsprogramme, mit denen personenbezogene Daten verarbeitet werden, und die Kontrollen durch interne oder externe Datenschutzbeauftragte. Nur in Ausnahmefällen lassen die bereichsspezifischen Regelungen die Nutzung dieser Daten für andere Zwecke, z. B. zur Strafverfolgung, zu.

**Aufbewahrungsdauer**

Soweit nicht bereichsspezifische Regelungen etwas anderes vorsehen, richtet sich die Aufbewahrungsdauer der Protokolle nach den allgemeinen Löschungsregeln der Datenschutzgesetze. Protokolldaten sind unverzüglich zu löschen, wenn sie zur Erreichung des Zwecks nicht mehr erforderlich sind. Gibt es keinen zwingenden Grund für das weitere Vorhalten von Protokolldateien, besteht eine Löschungspflicht.

Als Anhaltspunkte können dienen:

* die Wahrscheinlichkeit, dass Unregelmäßigkeiten (noch) offenbar werden können und
* die Möglichkeit, die Gründe von Unregelmäßigkeiten anhand der Protokolle und anderer Unterlagen aufdecken zu können.
Erfahrungsgemäß sollte eine Frist von einem Jahr nicht überschritten werden.

Soweit Protokolle zum Zwecke gezielter Kontrollen angefertigt werden, kommen kürzere Speicherungsfristen in Betracht. In der Regel reicht eine Aufbewahrung bis zur tatsächlichen Kontrolle aus. Auch hier sind die bereichsspezifischen Vorschriften zu beachten.

**Technische und organisatorische Rahmenbedingungen**

Wie effektiv die Protokollierung und ihre Auswertung im Rahmen von Kontrollen ist, hängt entscheidend von den technischen und organisatorischen Rahmenbedingungen ab. Deshalb sind folgende Aspekte zu berücksichtigen:

* Es sollte ein Konzept erstellt werden, das den Zweck der Protokolle und deren Kontrollen sowie Schutzmechanismen für die Rechte der Mitarbeiter und der sonstigen betroffenen Personen klar definiert (siehe auch OPS.1.1.6 *Protokollierung*).
* Die Zwangsläufigkeit und damit die Vollständigkeit der Protokolle muss ebenso gewährleistet werden wie die Manipulationssicherheit der Einträge in Protokolldateien.
* Entsprechend der Zweckbindung der Datenbestände müssen wirksame Zugriffsbeschränkungen realisiert werden.
* Die Protokolle müssen so gestaltet sein, dass sie effektiv überprüft werden können. Dazu gehört auch eine IT-Unterstützung der Auswertung.
* Die Auswertungsmöglichkeiten sollten vorab abgestimmt und festgelegt sein.
* Kontrollen sollten so zeitnah durchgeführt werden, dass bei aufgedeckten Verstößen noch Schäden abgewendet sowie Konsequenzen gezogen werden können. Kontrollen müssen rechtzeitig vor dem Ablauf von Löschungsfristen von Protokolldateien stattfinden.
* Kontrollen sollten nach dem Vier-Augen-Prinzip erfolgen.
* Die Mitarbeiter sollten darüber informiert sein, dass Kontrollen durchgeführt werden, falls erforderlich auch unangekündigt.
* Für Routinekontrollen sollten automatisierte Verfahren (z. B. *watch dogs*) verwendet werden.
* Personal- bzw. Betriebsräte sollten bei der Erarbeitung des Protokollierungskonzeptes und bei der Festlegung der Auswertungsmöglichkeiten der Protokolle beteiligt werden.
#### APP.3.1.M19 Schutz vor SQL-Injection

Um SQL-Injections zu verhindern oder zumindest zu erschweren, sind eine Reihe von Maßnahmen zu ergreifen. Diese erstrecken sich über alle Komponenten einer Anwendung, von der Applikation selbst über den Server bis hin zum Datenbank-Managementsystem (DBMS).

**Maßnahmen bei der Programmierung von Applikationen**

Eine der wichtigsten Maßnahmen, um SQL-Injection zu vermeiden, ist die sorgfältige Überprüfung und Filterung von Eingaben und Parametern durch die Webanwendung. Überprüft werden sollte, ob die übergebenen Daten dem erwarteten Datentyp entsprechen. Wird z. B. ein numerischer Parameter erwartet, kann dieser in PHP (PHP: Hypertext Preprocessor) mit der Funktion *is\_numeric()* überprüft werden. Die Filterung hingegen muss dafür sorgen, dass Sonderzeichen wie das Quote-Zeichen ('), das Semikolon (;) und doppelte Bindestriche (--) ignoriert werden.

Sicherer ist es, Stored Procedures beziehungsweise Prepared SQL-Statements einzusetzen. Diese werden von vielen Datenbank-Managementsystemen (DBMS) angeboten und sind ursprünglich dazu gedacht, häufiger auftretende Abfragen zu optimieren. Der Vorteil dieser parametrisierten Statements ist, dass Parameter nicht mehr direkt in ein SQL-Statement eingebunden werden. Vielmehr werden diese getrennt vom SQL-Statement separat an die Datenbank übergeben. Das DBMS führt dann selbst Statement und Parameter zusammen, wobei die oben genannten Sonderzeichen **automatisch** maskiert werden.

Um potenziellen Angreifern keine Anhaltspunkte für Angriffe zu liefern, sollte besonderes Augenmerk darauf gelegt werden, dass Applikationen möglichst keine Fehlermeldungen nach außen ausgeben, die Rückschlüsse auf das verwendete System oder auf die Struktur der dahinterliegenden Datenbank zulassen. 

**Serverseitige Maßnahmen**

Die wichtigste Sicherheitsmaßname auf dem Server ist, das Betriebssystem zu härten. Um so wenig Angriffspunkte wie möglich zu bieten, werden dafür zum Beispiel folgende Maßnahmen ergriffen:

* nicht benötigte Dienste deaktivieren,
* nicht benötigte Benutzerkonten löschen,
* relevante Patches einspielen und
* alle für die Funktion des Servers unnötigen Bestandteile löschen.
Darüber hinaus sollte der Einsatz eines Application-Level-Gateways (ALG) erwogen werden. ALGs können auf Applikationsebene die Daten überwachen, die zwischen Webbrowser und Anwendung ausgetauscht werden, und verhindern, dass schädliche Daten den Server erreichen.

Eine weitere zusätzliche Sicherheitsmaßnahme stellt der Einsatz von Intrusion-Detection-Systemen (IDS) und Intrusion-Prevention-Systemen (IPS) dar. IDS analysieren den über ein Netz übertragenen Datenverkehr und erkennen potenziell gefährliche Daten. Die dazu eingesetzten Analysetechniken unterteilen sich in Misuse und Anomaly Detection. Die Misuse Detection versucht, bereits bekannte Angriffsmuster zu erkennen. Die Anomaly Detection verfolgt den Ansatz, die zulässigen Verhaltensmuster zu lernen und Abweichungen davon als Angriff zu identifizieren. Während ein IDS in der Lage ist, Angriffe zu erkennen und Warnungen auszugeben, ist ein IPS in der Lage, entsprechende Reaktionen auszuführen. Die Reaktion kann beispielsweise darin bestehen, die Verbindung zu blockieren, Daten zu verwerfen oder zu ändern.

Bei erhöhten Sicherheitsanforderungen sollte geprüft werden, ob der Einsatz von IDS beziehungsweise IPS zweckmäßig ist.

**Datenbankseitige Maßnahmen**

Ebenso wie das Betriebssystem sollte auch die Datenbank gehärtet werden. Im Falle der Datenbank bedeutet dies z. B.: 

* nicht benötigte Stored Procedures zu entfernen,
* nicht benötigte Dienste zu deaktivieren, 
* nicht benötigte Benutzerkonten und Default Accounts zu löschen und
* relevante Patches einzuspielen.
In diesem Zusammenhang sollte auch ein speziell für den Datenbankzugriff vorgesehener Account angelegt werden, der mit möglichst eingeschränkten Zugriffsrechten auskommen sollte. 

Darüber hinaus sollten vertrauliche Daten, wie z. B. Passwörter, in der Datenbank soweit möglich nur verschlüsselt gespeichert werden.

Von vielen Herstellern werden mittlerweile sogenannte Schwachstellen-Scanner angeboten, die sowohl Applikationen als auch Datenbanken auf Sicherheitslücken, wie beispielsweise mögliche SQL-Injections, überprüfen können. 

**Beispiel für prinzipielles Vorgehen zur Erstellung von sicherem Code bei Verwendung von PHP und MySQL:**

In PHP verhindert die Funktion *mysql\_real\_escape\_sting(),* dass Sonderzeichen an eine MySQL-Datenbank übergeben werden. Die Funktion maskiert die in dem übergebenen String enthaltenen Sonderzeichen wie z. B. Quotes und verhindert so SQL-Injections. 

Anstatt der folgenden Syntax: 

* $query = "SELECT * FROM users   
 WHERE username=   
 '" . $\_POST['username'] . "'   
 AND password=   
 '" . $\_POST['password'] . "'"; 
sollte also diese Syntax verwendet werden: 

* $query = "SELECT * FROM users   
 WHERE username=   
 '" . mysql\_real\_escape\_string($\_POST['username']) . "'   
 AND password=   
 '" . mysql\_real\_escape\_string($\_POST['password']) . "'"; 
**Beispiel für sicheren Code bei Verwendung von ASP mit ADO und SQL-Server:**

Ein prepared-Statement für das obige Beispiel sieht in diesem Fall folgendermaßen aus:

* $query = "SELECT * FROM users WHERE username=?   
 AND password=?"   
 Set cmd = Server.CreateObject("ADODB.Command")   
 cmd.CommandText = query   
 cmd.CommandType = adCmdText   
 Set param = cmd.CreateParameter("",adVarChar, adParamInput,   
 nMaxUsernameLength, strUsername)   
 cmd.Parameters.Append   
 Set param = cmd.CreateParameter("",adVarChar, adParamInput,   
 nMaxUsernameLength, strPassword)   
 cmd.Parameters.Append   
 Set rs = cmd.Execute() 
Hierbei ist zu beachten, dass die oben aufgeführten Code-Beispiele nur den grundsätzlichen Ansatz zur Vermeidung von SQL-Injection veranschaulichen sollen.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.3.1.M20 Einsatz von Web Application Firewalls(CIA)

Für die Filterung von Daten auf höheren Protokollebenen kann auf Web Application Firewalls (WAF) zurückgegriffen werden. Da eine WAF das HTTP-Protokoll und die darüber übertragenen Daten analysiert, lassen sich Angriffsmuster auf Anwendungsebene bereits an der WAF filtern. Auf diese Weise werden Angriffsversuche frühzeitig erkannt und nicht mehr an die Webanwendung weitergeleitet.

Die Filterung an der WAF kann üblicherweise auf zwei Arten erfolgen.

* An eine Webanwendung gesendete Daten werden auf bekannte Angriffsmuster untersucht. Die Angriffsmuster werden vom Hersteller der WAF zur Verfügung gestellt und umfassen sowohl typische Zeichenketten, die bei allgemeinen Angriffen gegen Webanwendungen (z. B. SQL-Injection) verwendet werden, als auch spezifische Angriffsmuster, die Standard-Softwareprodukte betreffen. Damit bekannte Angriffe zuverlässig erkannt werden, müssen die Angriffssignaturen ähnlich wie bei einem Virenscanner regelmäßig aktualisiert werden.
* Wird keine Standardsoftware eingesetzt oder soll ein zusätzlicher Schutz erreicht werden, können für WAF üblicherweise auch eigene Filterregeln erstellt werden. Dabei wird beispielsweise definiert, welche Eingabedaten für die Webanwendung zugelassen werden. Diese Methode erfordert einen hohen Konfigurationsaufwand und eine genaue Kenntnis der von der Webanwendung verarbeiteten Daten.
#### APP.3.1.M21 Verhinderung von Clickjacking [Entwickler](CI)

Um Clickjacking-Angriffe zu vermeiden, sollten folgende Gegenmaßnahmen umgesetzt werden:

* Eingebetteter Code (z. B. JavaScript) in den Webseiten sollte auf dem Client prüfen und sicherstellen, dass die Inhalte der Webanwendung auf der obersten Ebene des Browser-Fensters eingeblendet werden. Dies soll bewirken, dass keine anderen Ebenen über dem ursprünglichen Inhalt der Webseite gelagert werden können. Ist dies nicht möglich, so sollte die Anzeige der Webanwendung unterbunden werden (siehe Skript zur Vermeidung von Clickjacking in Hilfsmittel zum Baustein Webanwendung [GSSID]).
* Bei der Auslieferung der Webseiten durch die Webanwendung sollte zusätzlich in den HTTP-Response-Headern die Direktive *X-FRAME-OPTIONS* gesetzt sein. *X-FRAME-OPTIONS DENY* verhindert, dass Inhalte der Webseite in einem Frame angezeigt werden. Alternativ kann diese Einschränkung auf Seiten begrenzt werden, die nicht von derselben Domäne stammen (*X-FRAME-OPTIONS SAMEORIGIN*).
#### APP.3.1.M22 Durchführung von Penetrationstests(CIA)

Penetrationstests sind erprobte und geeignete Vorgehensweisen, um die aktuelle Sicherheit von IT-Systemen und IT-Anwendungen festzustellen. 

Das BSI setzt hierbei zwei Testmethoden ein, IS-Penetrationstests sowie IS-Webchecks. Der IS-Penetrationstest ist die Vorgehensweise zur Untersuchung des aktuellen Sicherheitsniveaus von IT-Systemen und Netzen. Mittels eines IS-Webchecks wird das aktuelle Sicherheitsniveau des Internetauftritts beziehungsweise von Web-Services einer Institution ermittelt.

Penetrationstests dienen dazu, die Erfolgsaussichten eines vorsätzlichen Angriffs auf einen Informationsverbund, ein einzelnes IT-System oder eine Internetpräsenz abzuschätzen und daraus notwendige ergänzende Sicherheitsmaßnahmen abzuleiten beziehungsweise zu prüfen, ob die bereits umgesetzten Sicherheitsmaßnahmen wirksam sind. Für sicherheitskritische Netze und Systeme sollten regelmäßig Penetrationstests erfolgen.

Im Detail werden dabei die installierten Anwendungen (Webanwendung, Mailserver, Web-Service) beziehungsweise die zugrunde liegenden Trägersysteme (Betriebssystem, Datenbank etc.) überprüft.

Typische Ansatzpunkte für einen Penetrationstest sind:

* Netzkoppelelemente (Router, Switches, Gateways),
* Sicherheitsgateway (Paketfilter, Intrusion-Detection-System, Virenscanner),
* Server (Datenbankserver, Webserver, Fileserver, Speichersysteme),
* Telekommunikationsanlagen,
* Webanwendungen (zum Beispiel Internetauftritt, Vorgangsbearbeitung, Webshop),
* Web-Services (zum Beispiel REST-Interface, SOAP-API, SOA),
* Clients,
* drahtlose Netze (zum Beispiel WLAN, Bluetooth) und
* Infrastruktureinrichtungen (Zutrittskontrollmechanismen).
Üblicherweise werden Penetrationstests in Blackbox-Tests und Whitebox-Tests unterteilt. Bei einem Blackbox-Test stehen dabei den Penetrationstestern lediglich die Adressinformationen des Zieles zur Verfügung, weitere Informationen werden ihnen nicht mitgeteilt. Mittels der Vorgehensweise "Blackbox-Test" soll damit der Angriff eines typischen Außentäters mit unvollständigen Kenntnissen über das Zielsystem simuliert werden. Dagegen verfügen die Penetrationstester bei einem Whitebox-Test über umfangreiche, für sie hilfreiche Informationen über die zu testenden Systeme. Dazu gehören beispielsweise Informationen über IP-Adressen, das interne Netz, die eingesetzte Soft- und Hardware. Diese Angaben werden ihnen zuvor vom Auftraggeber mitgeteilt.

Es ist jedoch fraglich, ob die Unterscheidung zwischen den Vorgehensweisen "Blackbox-Test" und "Whitebox-Test" heute noch sinnvoll ist. Beispielsweise besteht bei einem Blackbox-Test aufgrund nicht vorliegender Informationen ein höheres, durchaus vermeidbares Risiko, einen unbeabsichtigten Schaden zu verursachen. Weiterhin könnten Schwachstellen aufgrund nicht mitgeteilter Informationen übersehen werden.

Zudem besteht die Gefahr, dass im Rahmen eines Blackbox-Tests der Angriff eines informierten Innentäters nicht berücksichtigt wird. 

Den Penetrationstestern sollten daher heutzutage alle für die Testdurchführung notwendigen Informationen über die zu testenden Systeme zur Verfügung gestellt werden, um eventuell mit dem Test verbundene Risiken minimieren zu können und eine möglichst vollständige Schwachstellensuche zu ermöglichen.

Die Klassifizierung von Penetrationstests in eine weitestgehend automatisierte Schwachstellensuche ("Vulnerability Scan") sowie eine in großen Teilen manuelle Sicherheitsrevision erscheint daher nach heutigem Kenntnisstand praxisnäher und erfolgsorientierter.

**Personelle und fachliche Anforderungen an einen Dienstleister für Penetrationstests**

Penetrationstests sind anspruchsvolle und diffizile Aufgaben, die sich auch auf den laufenden IT-Betrieb auswirken können. Daher sollte hierfür nur hinreichend qualifiziertes und zuverlässiges Personal mit themenübergreifenden Kenntnissen auf folgenden Gebieten eingesetzt werden:

* Administration von Betriebssystemen und Anwendungen
* Netzwerkprotokolle und Auswertung von Netzwerkverkehr
* Sicherheitsprodukte (zum Beispiel Sicherheitsgateways, Intrusion-Detection-Systeme)
* Programmiersprachen
* Schwachstellenscanner
* Audit- und Administrationssoftware
Werden externe Dienstleister mit der Durchführung von Penetrationstests beauftragt, so sollte darauf geachtet werden, dass ein qualifizierter und vertrauenswürdiger Dienstleister ausgewählt wird, der entsprechend qualifizierte und zuverlässige Mitarbeiter bereitstellen kann. 

Weiterhin sollten Anbieter von Penetrationstests dem Auftraggeber eine strukturierte Methodik zu deren Durchführung vorstellen können, auf deren Basis die jeweilige individuelle Vorgehensweise ausgearbeitet werden kann.

**Strukturierung und Vorgehensweise für einen Penetrationstest**

In einer Vorbereitungsphase müssen zunächst zwischen dem Auftraggeber und dem Auftragnehmer die Ziele sowie der Umfang des Penetrationstests so genau wie möglich festgelegt werden. Der Penetrationstester sollte hierbei dem Auftraggeber eine strukturierte Vorgehensweise, welche zwischen den Parteien abzustimmen ist, vorstellen.

Während des Abstimmungsprozesses sollte beachtet werden, dass unter Umständen Dritte über den geplanten Penetrationstest informiert beziehungsweise daran beteiligt werden müssen. 

In der Regel müssen beispielsweise die Personalvertretung und der Datenschutzbeauftragte, häufig auch Externe, wie der Internet-Service-Provider oder der Webhoster, in das Vorhaben einbezogen werden.

Zwischen dem Auftraggeber und dem Dienstleister sollten bestimmte Voraussetzungen bereits im Vorfeld vereinbart werden. Hierzu zählen insbesondere:

* Vereinbarungen über die Verschwiegenheitspflichten
* Vereinbarungen über den Einsatz von Hard- und Software
* Vereinbarungen über die zu testenden IT-Systeme und IT-Anwendungen
* Festlegung von erlaubten und unerlaubten Aktivitäten der Penetrationstester, um Schäden möglichst zu vermeiden
* Vereinbarungen über den Umgang mit Datenträgern vor, während und nach Abschluss des Penetrationstests, da die Datenträger zum Beispiel schützenswerte Informationen über die Testergebnisse enthalten können
* Festlegungen über den Ort der Durchführung sowie zur Auswertung und Berichterstellung für den Penetrationstest
* Festlegung eines Terminplans einschließlich Wartungsfenster für die Durchführung der Tests
* Detaillierte Vereinbarungen über den Zugang zum Internet beziehungsweise den Anschluss von Testsystemen an das Internet während der Durchführung und der Auswertung von Penetrationstests
* Vereinbarungen über Zuständigkeiten und die Erreichbarkeit von Ansprechpartnern sowie zur Notfallvorsorge
In der sich anschließenden Informationsphase sammeln die Penetrationstester möglichst viele Informationen über das zu testende Objekt. Zur Vorbereitung der Tests werden die gewonnenen Informationen anschließend hinsichtlich potenzieller Schwachstellen ausgewertet.

In der eigentlichen Testphase eines Penetrationstests sollten nach Möglichkeit die Testverfahren vermieden werden, welche ein destruktives Ergebnis für die untersuchten IT-Systeme oder IT-Anwendungen zur Folge haben könnten.

So zielen beispielsweise DoS-Angriffe (Denial of Service) darauf ab, den Zugriff auf einzelne Dienste, Systeme oder Netzsegmente zu unterbinden. Die Feststellung, ob derartige Attacken möglich sind, kann jedoch oftmals im Vorfeld durch eine Systemanalyse geklärt werden, sodass solche Angriffe während eines Penetrationstests überflüssig werden.

Sollen dennoch DoS-Angriffe oder ähnliche destruktive Angriffe im Rahmen eines Penetrationstests durchgeführt werden, sollte dies außerhalb der produktiven Nutzungszeiten des Systems erfolgen. Eventuell kann ein derartiger Angriff auch anhand eines Testsystems simuliert werden. Diese Vorgehensweisen sollten ausdrücklich vereinbart werden.

Erst danach werden aktive Eindringversuche unternommen. Dabei müssen die vereinbarten Wartungsfenster und der Terminplan strikt eingehalten werden. Wenn Änderungen am zeitlichen Ablauf erforderlich sind, muss dies auf jeden Fall mit dem Auftraggeber abgestimmt werden.

Anderenfalls besteht die erhöhte Gefahr, dass auf der Seite des Auftraggebers bestimmte Aktivitäten der Penetrationstester mit echten Angriffen verwechselt werden. Empfehlenswert ist die vollständige Aufzeichnung und Dokumentation des Penetrationstests.

Um möglichst aussagekräftige Ergebnisse zu erhalten, sollte darauf geachtet werden, dass die Penetrationstests unmittelbar an dem zu testenden IT-System sowie unter Umgehung von vorgeschalteten Komponenten wie zum Beispiel Paketfilter, Web Application Firewall durchgeführt werden. Liegen besondere Gründe vor, den Test mit aktiven vorgeschalteten Sicherheitskomponenten durchzuführen, so ist zu beachten, dass dabei eventuell Sicherheitsprobleme in der Anwendung selbst unentdeckt bleiben, weil die vorgelagerten Komponenten die Angriffsversuche im Penetrationstest abfangen. Solche unentdeckten Schwachstellen bilden jedoch ein relevantes Risiko, denn häufig können mit einem abgewandelten Angriff die Schutzsysteme ausgehebelt und die Schwachstellen ausgenutzt werden.

**Typische Angriffstechniken**

Netz- und Portscanning: Netz- und Portscanning werden genutzt, um die in einem Netz aktiven IT-Systeme aufzufinden und die dort angebotenen Dienste (Ports) zu identifizieren.

Seitens der IT-Administration werden solche Abfragen dazu genutzt, den aktuellen Status der eingesetzten IT-Systeme abzufragen. Allerdings kann ein Angreifer unter Umständen mit Hilfe dieser Informationen vorhandene Schwachstellen auf den einzelnen IT-Systemen identifizieren und basierend auf diesen Informationen einen Angriff durchführen.

* Ausnutzung mangelhafter Eingabeüberprüfung: Als Eingabeüberprüfung wird das Verfahren bezeichnet, mit dem die Benutzereingaben (Daten), die einer Anwendung zur weiteren Bearbeitung übergeben werden, vorher gefiltert, bereinigt oder zurückgewiesen werden.Diese Filterung soll verhindern, dass der Anwendung schädlicher Code übergeben werden kann, dessen Verarbeitung zu einem Fehlverhalten führt wie zum Beispiel der Offenlegung vertraulicher Informationen.
* Angriffsmethoden, mit denen ein derartiges Fehlverhalten hervorgerufen werden kann, sind zum Beispiel *Cross-Site Scripting (XSS), Cross-Site Request Forgery (XSRF), Injection, OS Injection, Fuzzing*.
* Teilweise lassen sich auch Schwachstellen der verwendeten Protokolle und sonstigen Techniken ausnutzen, um Schaden zu bewirken, zum Beispiel mittels Angriffen auf veraltete SSL/TLS-Versionen.
* Denial-of-Service-Angriffe (DoS): Diese Angriffe zielen darauf ab, einen oder mehrere der zur Verfügung gestellten Dienste außer Betrieb zu setzen. Dies kann unter anderem mittels einer durch vermehrte Anfragen gesteigerten Last, durch ein massiv erhöhtes Datenaufkommen (zum Beispiel E-Mails), aber auch durch gezieltes Ausnutzen möglicher Softwarefehler durchgeführt werden. Ein bekanntes Beispiel für einen DoS-Angriff ist der *Ping of Death*.
* Information Gathering: Als *Information Gathering* wird die Sammlung aller Informationen bezeichnet, welche im weiteren für einen Angriff nützlich sein könnten. Beispiele für solche Informationen sind etwa das verwendete Nummerierungsschema für Verzeichnisse oder Server oder auch Erkenntnisse über Web-Service-Schnittstellen, die durch WSDL-Scanning gewonnen werden.
* Social Engineering: Als *Social Engineering* werden beispielsweise fingierte Anrufe oder sonstige Kontaktaufnahmen mit Personen bezeichnet, die das betrachtete IT-System bedienen. Das Ziel ist meist, dadurch vertrauliche Informationen, wie zum Beispiel Passwörter, zu erhalten.
* Passwort-Attacken: Hierbei wird die Sicherheit beziehungsweise Stärke von Passwörtern mittels sogenannter Wörterbuchangriffe, Brute-Force-Attacken oder durch Entschlüsselungsversuche getestet.
* Ausnutzen von Software-Schwachstellen: Bei diesen Angriffen wird beispielsweise getestet, ob die installierte Software anfällig für bestimmte Exploits ist, fehlerhaft konfiguriert ist, Schwachstellen aufweist oder veraltet ist. Häufig wird auch untersucht, ob etwa bekannte Schwachstellen der Standardinstallation des jeweiligen Produkts im vorliegenden Fall ausgenutzt werden können.
* Kryptografische Angriffe: Hierbei werden beispielsweise die Stärke und die Implementierung der eingesetzten Verschlüsselungsmechanismen und -protokolle sowie der Schlüsselverwaltung untersucht.
* Infrastruktur-Untersuchungen: Im Rahmen von Infrastruktur-Untersuchungen werden unter anderem bauliche Sicherungsmaßnahmen, Zutritts- und Schließeinrichtungen, aber auch die Entsorgung von Material durchleuchtet. Eine Variante hiervon ist das sogenannte *Dumpster Diving*, hierbei suchen Angreifer nützliche Unterlagen oder Datenträger im Abfall (zum Beispiel Papierkörbe, Abfallcontainer).
In der Auswertungs- und Berichtsphase werden die Ergebnisse gesammelt, ausgewertet und in Form eines Berichts zusammengestellt. Alle während des Penetrationstests gewonnenen Informationen sind hierbei entsprechend gesichert aufzubewahren. Der Auftraggeber sollte den Auftragnehmer im Vorfeld dazu verpflichten, alle Aufzeichnungen über den Penetrationstest vollumfänglich an den Auftraggeber zu übergeben beziehungsweise zu vernichten.

Der Bericht muss die gefundenen Schwachstellen auflisten und auch Maßnahmenempfehlungen enthalten, wie mit den entdeckten Schwachstellen umgegangen werden sollte. Empfehlenswert ist hierbei zudem die Erstellung eines Umsetzungsplans für die in dem Bericht aufgeführten Maßnahmenempfehlungen einschließlich einer Priorisierung. Für das Management sollte der Abschlussbericht außerdem eine Zusammenfassung enthalten, in der die wesentlichen Prüfungsergebnisse und ein Überblick über die empfohlene weitere Vorgehensweise dargestellt sind. Der Abschlussbericht muss dem ISB und den verantwortlichen Führungskräften vorgelegt werden.

Begleitend zu allen Phasen eines Penetrationstests ist eine gemeinsame Dokumentation der einzelnen Vereinbarungen und Ergebnisse durch den Auftraggeber und den Auftragnehmer empfehlenswert.

#### APP.3.1.M23 Verhinderung von Cross-Site Request Forgery [Entwickler](CI)

Bei einem Cross-Site-Request-Forgery-(CSRF)-Angriff wird einem Benutzer ein Befehl für eine Webanwendung (z. B. in Form eines Links in einem Gästebuch) von einem Angreifer übermittelt. Folgt er diesem Link, wird der Befehl an die Webanwendung gesendet und im Kontext dieses Benutzers ausgeführt. Ist der Benutzer an der Webanwendung angemeldet, so wird seine Vertrauensstellung gegenüber der Webanwendung ausgenutzt und der Befehl mit den Rechten des Benutzers ausgeführt.

Um derartige Angriffe zu erschweren, sollte die Webanwendung Sicherheitsmechanismen unterstützen, die es ermöglichen, beabsichtigte Seitenaufrufe des Benutzers von unbeabsichtigt weitergeleiteten Befehlen Dritter zu unterscheiden. Mit den folgenden Sicherheitsmaßnahmen soll verhindert werden, dass kritische Aktionen durch CSRF-Angriffe unbeabsichtigt ausgeführt werden.

**Verwendung eines zusätzlichen Tokens**

Bei einem CSRF-Angriff muss ein gültiger HTTP-Request nachgestellt und an das Opfer übermittelt werden. Ein solcher HTTP-Request kann z. B. durch eine URL auf die Webanwendung abgebildet werden (z. B. *http://webapp.tld/addUser?name=benutzer*). Hierfür muss der Angreifer die benötigten Request-Parameter, wie z. B. GET- und POST-Variablen, für den Aufruf kennen. Diese Parameter sind im Allgemeinen leicht zu ermitteln.

Als Schutz gegen einen CSRF-Angriff kann ein geheimes Token eingeführt werden, das ein Angreifer nur schwer erraten kann. Bei jedem Seitenaufruf der Webanwendung wird dieses Token als Parameter in URLs oder als verstecktes Element (Hidden-Field) in Formularen mit übertragen (Double Submit Cookies). Die Webanwendung prüft bei jedem Client-Request, ob das übertragene Token mit dem zur Sitzung hinterlegten Wert übereinstimmt. Im Fehlerfall wird der angeforderte Aufruf abgelehnt. Ohne Kenntnis dieses Tokens kann ein Angreifer keinen gültigen HTTP-Request nachstellen.

Obwohl die Session-ID vertraulich ist und daher als Token zum Schutz gegen CSRF-Angriffe eingesetzt werden könnte, sollte vorzugsweise ein separates Token erzeugt werden. Für das Token sollten dabei ähnliche Anforderungen gelten, die auch an die Session-ID gestellt werden.

Wird ein CSRF-Schutz implementiert, so wird empfohlen die Funktion aus bereits verwendeten Frameworks einzusetzen, falls diese eine entsprechende Implementierungen anbieten.

Bei Webanwendungen mit hohem Schutzbedarf sollte in Betracht gezogen werden, das Token für jeden Request derart zu erzeugen, dass bei jedem Aufruf der Webanwendung ein neues Token an den Client gesendet wird, das dann im darauffolgenden Request verwendet werden muss.

Bevor kritische Aktionen ausgeführt werden (z. B. zustandsändernde Anfragen wie eine Änderung des Passworts), sollte der Benutzer erneut von der Webanwendung authentisiert werden. Hierdurch können diese Funktionen nicht unbemerkt ausgeführt werden, sondern es ist eine Interaktion mit dem Benutzer erforderlich. Webanwendungen mit hohem Schutzbedarf sollten ein Authentisierungsverfahren mit mehreren Authentisierungsfaktoren (z. B. TAN, Chipkarte) verwenden.

Alternativ kann der Benutzer beim Aufruf von kritischen Aktionen auf eine Seite umgeleitet werden, die eine Benutzerinteraktion erfordert, bevor die Aktion ausgeführt wird (z. B. die Eingabe einer zufälligen Zeichenkette). Erst nachdem der Benutzer die Interaktion ausgeführt hat (z. B. richtige Zeichenkette eingegeben), wird er weitergeleitet und die ursprüngliche Anfrage bearbeitet. Anstelle der Zeichenkette können auch andere Mechanismen eingesetzt werden, die eine Benutzerinteraktion verlangen (z. B. CAPTCHAs oder Rätselfragen, siehe auch APP.3.1.M23 *Verhinderung der Blockade von Ressourcen (DoS) bei Webanwendungen*).

Das Referrer-Feld im HTTP-Request (die URL der Webseite, von der der Benutzer zur aktuellen Seite gekommen ist) kann als ein weiteres Sicherheitsmerkmal genutzt werden. Ein Request eines Benutzers der Webanwendung ist häufig nur dann gültig, wenn das Referrer-Feld eine URL der eigenen Webanwendung enthält. So kann davon ausgegangen werden, dass der Request durch den Klick auf einen Link der Webanwendung erzeugt wurde.

Dabei ist zu berücksichtigen, dass das Referrer-Feld deaktiviert oder gefiltert werden kann (z. B. aus Gründen des Datenschutzes) und die Maßnahme daher nicht für alle Webanwendungen umgesetzt werden kann.

**Umgehung von Schutzmechanismen**

Sicherheitsmechanismen zum Schutz vor CSRF-Angriffen, die auf das Referrer-Feld oder zusätzliche Token (siehe Abschnitt *Verwendung eines zusätzlichen Tokens*) basieren, können durch Cross-Site-Scripting-Angriffe umgangen werden. Die korrekte Filterung von Benutzerdaten (siehe APP.3.1.M15 *Umfassende Ein- und Ausgabevalidierung*) ist daher entscheidend für die Wirksamkeit der Sicherheitsmaßnahmen zum Schutz vor CSRF-Angriffen.

#### APP.3.1.M24 Verhinderung der Blockade von Ressourcen [Entwickler](A)

Webanwendungen bieten häufig ressourcenintensive Funktionen an, die zum Beispiel komplexe Datenbankabfragen oder Datenübermittlungen auslösen. Werden diese rechenintensiven Operationen bewusst gehäuft aufgerufen oder die Webanwendungen mit Anfragen überflutet, können hierdurch Ressourcen zu stark belegt und der Betrieb bis zur Unerreichbarkeit eingeschränkt werden. Dieses Vorgehen wird als Denial-of-Service-(DoS)-Angriff bezeichnet.

DoS-Angriffe beruhen in den meisten Fällen ebenso wie Brute-Force- und Enumeration-Angriffe auf Automation (siehe APP.3.1.M7 *Schutz vor unerlaubter automatisierter Nutzung von Webanwendungen*). Daher sollten zur Vorbeugung gegen DoS-Angriffe ähnliche Schutzmechanismen umgesetzt werden. Dazu zählen beispielsweise folgende Maßnahmen:

* Grenzwerte festlegen (zum Beispiel die vorübergehende Blockierung einer Ressource oder des Benutzerkontos nach wiederholten Fehlzugriffen),
* die Zeitspanne zwischen Anfrage und Verarbeitung durch die Webanwendung künstlich verzögern (zum Beispiel bei wiederholt erfolgloser Anmeldung),
* die aufrufende IP-Adresse bei Verdacht auf einen Angriff temporär sperren,
* CAPTCHAs verwenden,
* Eingaben bei Eingabefeldern verifizieren, bevor rechenintensive Operationen angestoßen werden,
* XML-Filtermechanismen und XML-Validitätsprüfungen einsetzen.
Zusätzlich geben die folgenden Beispiele Hinweise auf spezifische Schutzmaßnahmen, um Denial-of-Service-Angriffe bei Webanwendungen zu erschweren:

* Ressourcenintensive Operationen sind besonders anfällig für DoS-Angriffe. Daher kann die Ressourcennutzung pro Benutzer auf ein Maximum eingeschränkt werden. Darüber hinaus können bestimmte Operationen nur angemeldeten Benutzern zugänglich gemacht werden (zum Beispiel komplexe Datenbankaufrufe).
* Pro Benutzer sollte nur eine Anfrage zur gleichen Zeit bearbeitet werden. Mehrere Anfragen desselben Benutzers sollten sequenziell bearbeitet werden.
* Die Last durch DoS-Anfragen kann teilweise durch Zwischenspeichern ("cachen") der Webseitenaufrufe deutlich verringert werden. Somit wird die angeforderte, rechenintensive Operation nicht bei jedem Aufruf ausgeführt, sondern lediglich das zwischengespeicherte Resultat zurückgegeben. Stark ressourcenintensive Anfragen können auch in lastarmen Zeiten vorberechnet werden (Voraggregation).
* Die Architektur und die Flusskontrolle der Webanwendung sollten darauf ausgelegt sein, rechenintensive Operationen zu vermeiden (zum Beispiel bei der Erstellung von Session-IDs oder anderen kryptografischen Mechanismen sollten ressourcenintensive Operationen gemieden werden). Zur Erkennung rechenintensiver Operationen können Lasttests durchgeführt werden.
* Ein Überlauf von Speicherplatz, zum Beispiel im Rahmen der Protokollierung, kann dazu führen, dass keine Schreibzugriffe mehr auf den Datenträger möglich sind. Werden Speichervorgänge von der Webanwendung durchgeführt, kann dies den Betrieb gefährden. Daher sollte der Zugriff auf Datenspeicher begrenzt und die Kapazität der Datenspeicher regelmäßig geprüft werden. Ebenso sollte auch der Verbrauch von Arbeitsspeicher (RAM) pro Thread begrenzt werden.
* SOAP-Nachrichten müssen gemäß dem entsprechenden XML-Schema validiert werden. Ist die Validierung nicht erfolgreich, da sie zum Beispiel eine undefinierte Zahl an Elementen enthält, darf die SOAP-Nachricht nicht weiter verarbeitet werden, da dies ansonsten zu Problemen bei der Verarbeitung durch den XML-Parser führen kann.
* Ebenso sollten Webanwendungen vor SOAP-Flooding-Attacken geschützt werden. Diese sind vergleichbar mit herkömmlichen Flooding-Angriffen (z. B. SYN-Flooding) und können deswegen auch mit ähnlichen Schutzmaßnahmen bekämpft werden. So lassen sich mit einem Intrusion-Detection-System wiederholt gesendete Nachrichten erkennen und direkt blockieren, z. B. durch Anwendung von Heuristiken.
Bei Web-Anwendungen, bei denen aufgrund ihrer Natur mit gezielten, zum Beispiel politisch motivierten DoS-Angriffen aus dem Internet zu rechnen ist, kann auch die Zusammenarbeit mit einem Dienstleister sinnvoll sein, der sich auf die Abwehr von DoS-Angriffen spezialisiert hat. Solche Dienstleister leiten den IP-Verkehr im Angriffsfall über eigene Systeme, die Zugriffe filtern und/oder die Zielsysteme durch andere Maßnahmen, wie zum Beispiel Zwischenspeicher (Caching), entlasten. Dabei ist im Vorfeld abzuwägen, ob durch die Umleitung der Datenströme über die Systeme Dritter zusätzliche Gefährdungen oder Anforderungen entstehen. Eine beliebte Angriffsmethode für zwischengespeicherte Webseiten ist beispielsweise, dass der Angreifer nicht vorhandene Unterseiten aufruft. Wenn dies der Dienstleister nicht abfängt und die Anfrage nach der vermeintlich neuen Unterseite an die ursprüngliche Seite weiterleitet, kommt es zu einem unbeabsichtigten DoS-Angriff des Dienstleisters. Solchen neuen Angriffsvektoren muss bei der Auswahl des Anti-DoS-Dienstleisters begegnet werden.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Web-Tracking bezeichnet die Auswertung von Nutzerdaten, z. B. zur Verfolgung der Aktivitäten von Benutzern eines Webauftritts. Auf Grundlage dieser Auswertungen kann beispielsweise auf den Benutzer zugeschnittene Werbung eingeblendet oder die Popularität von Beiträgen anhand von Statistiken gemessen und daraufhin der Webauftritt optimiert werden. Hierfür können personenbezogene Informationen, wie der Standort des Benutzers, der Status einer Transaktion (z. B. Geschäftsabschluss bei einer Einkaufsplattform) und eine Abrufstatistik über Webseiten, protokolliert und herangezogen werden.

Werden externe Dienstleister beauftragt diese Nutzerdaten auszuwerten, ist zu beachten, dass diese Dienstleister möglicherweise die Nutzerdaten mit den Daten anderer Kunden und Webanwendungen korrelieren können. Auf dieser Basis können anwendungsübergreifend detaillierte Benutzerprofile erstellt werden.

Mögliche Techniken zur Sammlung von Nutzerdaten sind z. B.

* (persistente) Cookies,
Web-Bugs (ein Pixel große Bildelemente),

* Browser-Fingerabdrücke (z. B. durch Attribute, wie installierte Zusatzprogramme, Bildschirm-Auflösung, Zeitzone, User-Agent, HTTP-Header),
* Protokollierung der IP-Adresse.
Die Techniken können darüber hinaus kombiniert werden, um Benutzer zuverlässiger zu identifizieren.

Falls Nutzerdaten, insbesondere personenbezogene Daten, ausgewertet werden sollen, müssen die rechtlichen Grundlagen geprüft werden.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Webanwendungen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [BSICC] Gemeinsamen Kriterien für die Prüfung und Bewertung der Sicherheit von Informationstechnik (Common Criteria)

  

 BSI, (zuletzt abgerufen am 05.10.2017)  
 <https://www.bsi.bund.de/DE/Themen/ZertifizierungundAnerkennung/Produktzertifizierung/ZertifizierungnachCC/ITSicherheitskriterien/CommonCriteria/cc.html>

 
* #### [GSKHM] Hilfsmittel zur Nutzung der IT-Grundschutz-Kataloge

  

 BSI, (zuletzt abgerufen am 05.10.2017)  
 [https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine\_node.html](https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKataloge/Hilfsmittel/Bausteine/bausteine_node.html)

 
* #### [OWASP] Open Web Application Security Project

  

 OWASP, (zuletzt abgerufen am 28.09.2017)  
 <https://www.owasp.org>

 
* #### [TR21022] BSI Technische Richtlinie, Kryptografische Verfahren

  

 Verwendung von Transport Layer Security (TLS), Bundesamt für Sicherheit in der Informationstechnik (BSI), 2017  
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
