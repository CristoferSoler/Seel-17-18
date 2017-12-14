1 Beschreibung
--------------

### 1.1 Einleitung

Benutzer oder auch IT-Komponenten, die auf die Ressourcen einer Institution zugreifen, müssen zweifelsfrei identifiziert und authentisiert werden. Die Verwaltung der dafür notwendigen Informationen wird als Identitätsmanagement bezeichnet.

Beim Berechtigungsmanagement geht es darum, ob und wie Benutzer oder IT-Komponenten auf Informationen oder Dienste zugreifen und diese benutzen dürfen, ihnen also basierend auf dem Benutzerprofil Zutritt, Zugang oder Zugriff zu gewähren oder zu verweigern ist. Berechtigungsmanagement bezeichnet die Prozesse, die für Zuweisung, Entzug und Kontrolle der Rechte erforderlich sind.

Die Übergänge zwischen beiden Begriffen sind fließend, daher wird in diesem Baustein der Begriff Identitäts- und Berechtigungsmanagement (englisch Identity and Access Management, IAM) benutzt.

### 1.2 Zielsetzung

Ziel des Bausteins ist es, dass Benutzer oder auch IT-Komponenten ausschließlich auf die IT-Ressourcen und Informationen zugreifen können, die sie für ihre Arbeit benötigen und für die sie autorisiert sind, und unautorisierten Benutzern oder IT-Komponenten den Zugriff zu verwehren. Dazu werden Anforderungen formuliert, mit denen Institutionen ein sicheres Identitäts- und Berechtigungsmanagement aufbauen sollten.

### 1.3 Abgrenzung

In diesem Baustein werden grundsätzliche Anforderungen für den Aufbau eines Identitäts- und Berechtigungsmanagement beschrieben.

Anforderungen, die Komponenten eines Identitäts- und Berechtigungsmanagement betreffen wie Betriebssysteme oder Verzeichnisdienste, sind in den entsprechenden Bausteinen zu finden (z.B. SYS.1.3 Unix-Server, SYS.1.2.2 Windows Server 2012, APP.2.1 Allgemeiner Verzeichnisdienst, APP.2.2 Active Directory).

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich*** ***Identitäts- und Berechtigungsmanagement von besonderer Bedeutung:

### 2 1 Fehlende oder unzureichende Prozesse beim Identitäts- und Berechtigungsmanagement

Wenn beim Identitäts- und Berechtigungsmanagement Prozesse unzureichend definiert sind oder nicht befolgt werden, erhält der zuständige Administrator möglicherweise keine Informationen über personelle Veränderungen. Das kann dazu führen, dass beispielsweise ein Benutzerkonto eines ausgeschiedenen Mitarbeiters nicht gelöscht wird. Er kann somit weiterhin auf schützenswerte Informationen oder auch Cloud-Anwendungen zugreifen.

Auch ist es möglich, dass Mitarbeiter, die in eine neue Abteilung versetzt wurden, ihre alten Berechtigungen behalten und dadurch mit der Zeit umfangreiche Gesamt-Berechtigungen ansammeln. 

### 2 2 Fehlende zentrale Deaktivierungsmöglichkeit von Benutzerzugängen

In Institutionen haben Mitarbeiter oft Benutzerzugänge zu diversen IT-Systemen wie Produktiv-, Test-, Qualitätssicherungs- oder Projekt-Systeme. Diese befinden sich meist in unterschiedlichen Verantwortungsbereichen und werden von unterschiedlichen Administratoren verwaltet. Das führt dazu, dass nicht auf allen IT-Systemen eine gleiche und eindeutige Benutzerkennung verwendet wird und es meist auch keine zentrale Übersicht über die Benutzerzugänge auf den einzelnen IT-Systemen gibt. In einem solchen Szenario ist es nicht möglich, bei einem Angriff oder einem Passwortdiebstahl umgehend alle Benutzerzugänge eines Mitarbeiters zu deaktivieren. Auch können bei dem Ausscheiden eines Mitarbeiters aus der Institution nicht umgehend alle Zugänge gesperrt werden.

### 2 3 Ungeeignete Verwaltung von Zutritts-, Zugangs- und Zugriffsrechten

Wenn die Vergabe von Zutritts-, Zugangs- und Zugriffsrechten schlecht geregelt ist, führt das schnell zu gravierenden Sicherheitslücken, z. B. durch Wildwuchs in der Rechtevergabe. Bei der Einführung von Identitätsmanagement-Systemen oder Revisionen stellt sich häufig heraus, dass verschiedene Personen in unterschiedlichsten Organisationseinheiten für die Vergabe von Berechtigungen zuständig sind. Dies führt schnell dazu, dass Benutzer Berechtigungen auf Zuruf erhalten oder umgekehrt nur über unnötig komplizierte Wege an diese kommen. Dadurch können einerseits fehlende Berechtigungen die tägliche Arbeit behindern, andererseits können so Berechtigungen ohne Erfordernis vergeben werden und so ein Sicherheitsrisiko darstellen.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Identitäts- und Berechtigungsmanagement aufgeführt. Grundsätzlich ist der ISB für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### ORP.4.A1 Regelung für die Einrichtung von Benutzern und Benutzergruppen [Administrator, Leiter IT]

Es MUSS geregelt werden, wie Benutzer und Benutzergruppen einzurichten sind. Alle Benutzer und Benutzergruppen DÜRFEN NUR über separate administrative Rollen eingerichtet werden.

#### ORP.4.A2 Regelung für Einrichtung, Änderung und Entzug von Berechtigungen [Administrator, Leiter IT]

Benutzerkennungen und Berechtigungen DÜRFEN NUR aufgrund des tatsächlichen Bedarfs vergeben werden. Bei personellen Veränderungen MÜSSEN die nicht mehr benötigten Benutzerkennungen und Berechtigungen entfernt werden. Beantragen Mitarbeiter Berechtigungen, die über den Standard hinausgehen, DÜRFEN diese NUR nach zusätzlicher Begründung vergeben werden. Alle Berechtigungen MÜSSEN über separate administrative Rollen eingerichtet werden.

#### ORP.4.A3 Dokumentation der zugelassenen Benutzer und Rechteprofile [Administrator, Leiter IT]

Es MUSS eine Dokumentation der zugelassenen Benutzer, angelegten Benutzergruppen und Rechteprofile erfolgen. Die Dokumentation der zugelassenen Benutzer, angelegten Benutzergruppen und Rechteprofile MUSS regelmäßig auf Aktualität überprüft werden. Die Dokumentation MUSS vor unberechtigtem Zugriff geschützt werden. Sofern sie in elektronischer Form erfolgt, SOLLTE sie in das Datensicherungsverfahren einbezogen werden.

#### ORP.4.A4 Aufgabenverteilung und Funktionstrennung [Leiter IT]

Es MÜSSEN die für den IT-Einsatz relevanten Aufgaben und Funktionen definiert werden. Auch MUSS festgelegt werden, welche Aufgaben und Funktionen nicht miteinander vereinbar sind. Diese Trennungen MÜSSEN umgesetzt werden. Sie SOLLTEN dokumentiert werden.

#### ORP.4.A5 Vergabe von Zutrittsberechtigungen [Leiter IT]

Es MUSS festgelegt werden, welche Zutrittsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben werden. Werden Zutrittsmittel wie Chipkarten verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden. Die Zutrittsberechtigten SOLLTEN auf den korrekten Umgang mit den Zutrittsmitteln geschult werden. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.

#### ORP.4.A6 Vergabe von Zugangsberechtigungen [Leiter IT]

Es MUSS festgelegt werden, welche Zugangsberechtigungen an welche Personen im Rahmen ihrer Funktion vergeben bzw. entzogen werden. Werden Zugangsmittel wie Chipkarten verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden. Die Zugangsberechtigten SOLLTEN auf den korrekten Umgang mit den Zugangsmitteln geschult werden. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.

#### ORP.4.A7 Vergabe von Zugriffsrechten [Leiter IT]

Es MUSS festgelegt werden, welche Zugriffsrechte an welche Personen im Rahmen ihrer Funktion vergeben bzw. entzogen werden. Werden Zugangsmittel wie Chipkarten verwendet, so MUSS die Ausgabe bzw. der Entzug dokumentiert werden. Die Zugriffsrechte SOLLTEN auf den korrekten Umgang mit den Zugangsmitteln geschult werden. Bei längeren Abwesenheiten SOLLTEN berechtigte Personen vorübergehend gesperrt werden.

#### ORP.4.A8 Regelung des Passwortgebrauchs [Benutzer, Leiter IT]

Die Institution MUSS den Passwortgebrauch verbindlich regeln. Dabei MUSS festgelegt werden, dass nur Passwörter mit ausreichender Länge und Komplexität verwendet werden. Die Passwörter SOLLTEN in angemessenen Zeitabständen geändert werden. Die Passwörter MÜSSEN sofort gewechselt, sobald sie unautorisierten Personen bekannt geworden sind oder der Verdacht darauf besteht. Passwörter MÜSSEN geheim gehalten werden. Standardpasswörter MÜSSEN durch ausreichend starke Passwörter ersetzt und vordefinierte Logins geändert werden. Es SOLLTE überprüft werden, dass die mögliche Passwortlänge auch im vollen Umfang von dem IT-System geprüft wird. Bei erfolglosen Anmeldeversuchen SOLLTE das System keinen Hinweis darauf geben, ob Passwort oder Benutzerkennung falsch sind.

#### ORP.4.A9 Identifikation und Authentisierung [Leiter IT]

Der Zugang zu allen IT-Systemen und Diensten MUSS durch eine angemessene Identifikation und Authentisierung der zugreifenden Benutzer, Dienste oder IT-Systeme abgesichert sein. Vorkonfigurierte Zugangsmittel MÜSSEN vor dem produktiven Einsatz geändert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Identitäts- und Berechtigungsmanagement. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### ORP.4.A10 Schutz von Benutzerkonten mit weitreichenden Berechtigungen [Leiter IT]

Benutzerkonten mit weitreichenden Berechtigungen SOLLTEN mit mindestens zwei Authentisierungsmerkmalen geschützt werden.

#### ORP.4.A11 Zurücksetzen von Passwörtern [Leiter IT]

Für das Zurücksetzen von Passwörtern SOLLTE ein angemessenes sicheres Verfahren definiert und umgesetzt werden. Die Support-Mitarbeiter, die Passwörter zurücksetzen können, SOLLTEN entsprechend geschult werden. Bei höherem Schutzbedarf des Passwortes SOLLTE eine Strategie definiert werden, falls der Support-Mitarbeiter aufgrund fehlender sicherer Möglichkeiten der Übermittlung des Passwortes die Verantwortung nicht übernehmen kann.

#### ORP.4.A12 Entwicklung eines Authentisierungskonzeptes für IT-Systeme und Anwendungen [Leiter IT]

Es SOLLTE ein Authentisierungskonzept erstellt werden. Darin SOLLTE für jedes IT-System und jede Anwendung definiert werden, welche Funktions- und Sicherheitsanforderungen an die Authentisierung gestellt werden. Authentisierungsinformationen SOLLTEN kryptografisch sicher geschützt übertragen und gespeichert werden.

#### ORP.4.A13 Geeignete Auswahl von Authentisierungsmechanismen [Leiter IT]

Es SOLLTEN dem Schutzbedarf angemessene Identifikations- und Authentisierungsmechanismen verwendet werden. Authentisierungsdaten SOLLTEN durch das IT-System bzw. IT-Anwendungen bei der Verarbeitung jederzeit gegen Ausspähung, Veränderung und Zerstörung geschützt werden.

#### ORP.4.A14 Kontrolle der Wirksamkeit der Benutzertrennung am IT-System [Administrator]

In angemessenen Zeitabständen SOLLTE überprüft werden, ob die Benutzer von IT-Systemen sich regelmäßig nach Aufgabenerfüllung abmelden und nicht mehrere Benutzer unter der gleichen Kennung arbeiten.

#### ORP.4.A15 Vorgehensweise und Konzeption der Prozesse beim Identitäts- und Berechtigungsmanagement [Leiter IT]

Für das Identitäts- und Berechtigungsmanagement SOLLTEN folgenden Prozesse definiert und umgesetzt werden:

* Richtlinien verwalten, 
* Identitätsprofile verwalten,
* Benutzerkennungen verwalten
* Berechtigungsprofile verwalten,
* Rollen verwalten.
#### ORP.4.A16 Richtlinien für die Zugriffs- und Zugangskontrolle [Administrator]

Es SOLLTE eine Richtlinie für die Zugriffs- und Zugangskontrolle von IT-Systemen, IT-Komponenten und Netzen erstellt werden. Es SOLLTEN Standard-Rechteprofile benutzt werden, die den Funktionen und Aufgaben der Mitarbeiter entsprechen. Für jedes IT-System und jede IT-Anwendung SOLLTE eine schriftliche Zugriffsregelung existieren. Außerdem SOLLTEN alle eingerichteten Benutzer und vergebenen Rechte dokumentiert sein. Es SOLLTE geregelt sein, dass Benutzer nur auf IT-Systeme und Dienste zugreifen können, wenn sie vorher angemessen identifiziert und authentisiert wurden.

#### ORP.4.A17 Geeignete Auswahl von Identitäts- und Berechtigungsmanagement-Systemen [Leiter IT]

Beim Einsatz eines Identitäts- und Berechtigungsmanagement-System SOLLTE es für die Institution und deren jeweilige Geschäftsprozesse, Organisationsstrukturen und Abläufe sowie deren Schutzbedarf passen. Das Identitäts- und Berechtigungsmanagement-System SOLLTE die in der Institution vorhandenen Vorgaben zum Umgang mit Identitäten und Berechtigungen abbilden können. Das ausgewählte Identitäts- und Berechtigungsmanagement-System SOLLTE den Grundsatz der Funktionstrennung realisieren können. Das Identitäts- und Berechtigungsmanagement-System SOLLTE angemessen vor Angriffen geschützt werden.

#### ORP.4.A18 Einsatz eines zentralen Authentifizierungsdienstes [Leiter IT]

Um ein zentrales Identitäts- und Berechtigungsmanagement aufzubauen, SOLLTE ein zentraler netzbasierter Authentisierungsdienst eingesetzt werden. Der Einsatz eines zentralen netzbasierten Authentisierungsdienstes SOLLTE sorgfältig geplant werden. Dazu SOLLTEN die Sicherheitsanforderungen dokumentiert werden, die für die Auswahl eines solchen Dienstes relevant sind.

#### ORP.4.A19 Einweisung aller Mitarbeiter in den Umgang mit Authentisierungsverfahren und -mechanismen [Benutzer, Leiter IT]

Alle Mitarbeiter SOLLTEN in den korrekten Umgang mit den Authentisierungsverfahren eingewiesen werden. Es SOLLTE verständliche Richtlinien für den Umgang mit Authentisierungsverfahren geben. Die Mitarbeiter SOLLTEN über relevante Regelungen informiert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### ORP.4.A20 Notfallvorsorge für das Identitäts- und Berechtigungsmanagement-System [Leiter IT](CIA)

Es SOLLTE geprüft werden, inwieweit ein ausgefallenes Identitäts- und Berechtigungsmanagement-System sicherheitskritisch für die Geschäftsprozesse ist. Für Notfälle SOLLTE ein Berechtigungskonzept vorhanden sein und es SOLLTEN Notfallberechtigungen existieren.

#### ORP.4.A21 Mehr-Faktor-Authentisierung [Leiter IT](C)

Bei höherem Schutzbedarf SOLLTE eine sichere Zwei- oder Mehr-Faktor-Authentisierung, z. B. mit kryptographischen Zertifikaten, Chipkarten oder Token, zur Authentisierung verwendet werden. 

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Identitäts- und Berechtigungsmanagement" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [29146] ISO/IEC 29146:2016

  

 Information technology - Security techniques - A framework for access management, 06.2016

 
* #### [ISFTS14] The Standard of Good Practice - Area TS1.4 Identiy and Access Management

  

 ISF, insbesondere Area TS1.4 Identiy and Access Management, Juni 2016

 
* #### [NIST80053A] NIST Special Publication 800-53A

  

 Assessing Security and Privacy Controls in Federal Information Systems, insebsondere Bereiche AC und IA, 12.2014

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Identitäts- und Berechtigungsmanagement" von Bedeutung.

* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.44 Unbefugtes Eindringen in Räumlichkeiten
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

