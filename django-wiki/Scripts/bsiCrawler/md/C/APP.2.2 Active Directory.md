1 Beschreibung
--------------

### 1.1 Einleitung

Active Directory Services (oft als AD oder ADS abgekürzt) ist ein von Microsoft entwickelter Verzeichnisdienst, der mit dem Betriebssystem Windows 2000 Server erstmalig eingeführt wurde. Ausgehend von den Active Directory-Funktionen des Betriebssystems Microsoft Windows 2000 Server wurden dem Active Directory-Dienst mit jedem Release der Windows-Server-Familie weiteren Schlüsselfunktionen hinzugefügt.

Active Directory wird hauptsächlich in IT-Netzen mit überwiegend Microsoft-Komponenten eingesetzt. Active Directory speichert Informationen über Objekte innerhalb eines IT-Netzes, z. B. über Benutzer oder Computer, und erleichtert es Anwendern und Administratoren, diese Informationen bereitzustellen, zu organisieren, zu nutzen und zu überwachen. Als ein objektbasierter Verzeichnisdienst ermöglicht Active Directory die Verwaltung von Objekten und deren Beziehung untereinander, die die eigentliche Netzumgebung ausmachen. Active Directory stellt zentrale Steuerungs- und Kontrollmöglichkeiten des jeweiligen Netzes bereit. Der Einsatz eines solchen Verzeichnisdienstes bietet sich vor allem dort an, wo z. B. die Anzahl der im Netz eingesetzten Clients eine dezentrale Verwaltung erschwert. Ohne einen Verzeichnisdienst könnte die Zuverlässigkeit lokal vorzunehmender Einstellungen, wie z. B. Umsetzung der Vorgaben aus Sicherheitsrichtlinien, aufgrund des hohen personellen Aufwandes nicht mehr gewährleistet werden. Verwaltungsaufgaben innerhalb des Netzes wie z. B. Passwortänderungen, Kontenerstellung und Zugriffsrechte können durch den Einsatz eines Verzeichnisdienstes effizienter durchgeführt werden.

### 1.2 Zielsetzung

Dieser Baustein hat die Absicherung von Active Directory im Regelbetrieb einer Institution (Behörde oder Unternehmen) zum Ziel, die ADS zur Verwaltung ihrer Infrastruktur von Windows-Systemen (Client und Server) einsetzt.

### 1.3 Abgrenzung

In diesem Baustein werden die für Active Directory spezifischen Gefährdungen und Maßnahmen betrachtet. Allgemeine Sicherheitsempfehlungen zu Verzeichnisdiensten finden sich im Baustein APP.2.1 Allgemeiner Verzeichnisdienst. Die dort beschriebenen allgemeinen Maßnahmen werden im vorliegenden Baustein konkretisiert und ergänzt. Dieser Baustein wiederholt nicht die Anforderungen der Absicherung der Betriebssysteme der Server und Clients, die für den Betrieb und die Verwaltung des AD genutzt werden (z. B. SYS.1.2.2 Windows Server 2012 oder SYS.2.2.3 Client unter Windows 10) sowie der zugrundeliegenden Netzinfrastruktur. Auch Prozesse wie Datensicherung und Patchmanagement werden nur insofern behandelt, wie im Bereich AD Besonderheiten zu beachten sind.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Active Directory von besonderer Bedeutung:

### 2 1 Unzureichende Planung der Sicherheitsgrenzen

Eine AD-Instanz erzeugt einen Wald (Forest) als Container auf höchster Ebene für alle Domänen dieser Instanz. Ein Wald kann einen oder mehrere Domänen-Containerobjekte enthalten, die über eine gemeinsame logische Struktur, einen Global Catalog, ein Schema und automatische transitive Vertrauensbeziehungen verfügen. Der Wald stellt also die Sicherheitsgrenze dar, innerhalb derer Informationen standardmäßig im AD weitergegeben werden, nicht ein einzelner Baum. Wird diese Grenzen nicht bewusst und strukturiert geplant, kann es dazu kommen, dass Informationen ungewollt abfließen und das Sicherheitskonzept der Institution versagt. Daher kann es notwendig sein, weitere Forests aufzubauen, wenn für Teile der Infrastruktur unterschiedliche Sicherheitsanforderungen gelten. Dies bedeutet jedoch zusätzliche Komplexität in Einrichtung und Verwaltung.

### 2 2 Zu viele oder zu laxe Vertrauensbeziehungen

Werden die Vertrauensbeziehungen zwischen Wäldern und Domänen nicht regelmäßig daraufhin evaluiert, ob sie weiterhin benötigt und gerechtfertigt sind, ob sie den korrekten Typ haben (d. h. vor allem, ob eine zweiseitige Vertrauensbeziehung wirklich notwendig ist) und ob die Sicherheitskontrollen zu ihrer Gewährleistung ausreichend sind, können Probleme mit Berechtigungen auftreten und Informationen abfließen. Insbesondere wenn die standardmäßig aktive SID-(Security Identifier-)Filterung deaktiviert wird, können komplexe, schwer zu durchschauende Schwachstellen auftreten. Gleiches gilt für den Verzicht auf Selective Authentication bei Vertrauensbeziehungen zwischen Forests.

### 2 3 Fehlende Sicherheitsfunktionen durch ältere Betriebssysteme und Domain Functional Level

Jede neue Generation des Betriebssystems Windows Server bringt zusätzliche Sicherheitsfunktionen und -erweiterungen auch in Bezug auf AD mit. Außerdem werden in der Regel die Standardeinstellungen mit jedem neuen Release immer sicherer gesetzt. Einige davon sind verwendbar, sobald das neue System installiert ist, andere erst dann, wenn das Domänen-/Wald-Functional-Level angehoben wurde. Der Einsatz älterer Betriebssysteme als (primärer) Domänencontroller bzw. veralteter Domain Functional Level verhindert also die Nutzung zeitgemäßer Sicherheitsfunktionen und erhöht die Gefahr unsicherer Standardeinstellungen. Eine unsicher konfigurierte Domäne gefährdet die darin verarbeiteten Informationen und erleichtert Angriffe durch Dritte.

### 2 4 Betrieb weiterer Rollen und Dienste auf Domänencontrollern

Jeder weitere auf einem Domänencontroller betriebene Dienst, außer dem AD selbst sowie weniger dafür unbedingt benötigter Hilfsdienste wie etwa DNS, erhöht die Angriffsfläche dieser zentralen Infrastrukturkomponenten durch mögliche zusätzliche Schwachstellen und Fehlkonfigurationen. Diese können bewusst oder unbewusst missbraucht werden, um z. B. Informationen unberechtigt zu kopieren oder zu verändern.

### 2 5 Missbrauch der Gruppe der Domänenadministratoren

Das AD selbst sollte nur von einer sehr kleinen Zahl von Administratoren verwaltet werden. Häufig werden jedoch sehr viel mehr Konten als DA (Domänenadministrator) geführt. Diese haben volle administrative Rechte auf allen Domänencontrollern, Workstations, Gruppenrichtlinien etc. Dies eröffnet Angreifern unnötig viel Spielraum, wenn einer dieser Accounts übernommen werden kann. Häufig enthält die Gruppe der DA Dienstkonten und andere Gruppen, die nicht direkt mit der Verwaltung des AD selbst zu tun haben.

### 2 6 Unzureichende Überwachung und Dokumentation von delegierten Rechten

Wenn die Bildung unternehmensspezifischer Gruppen und die Delegation von Rechten an diese nicht systematisch geplant und umgesetzt wird, kann die Delegation außer Kontrolle geraten und viel mehr Zugriff einräumen als vorgesehen, was durch Dritte missbraucht werden kann. Ohne regelmäßige Auditierung der Gruppen und ihrer Zugriffsrechte drohen diese Rechte mit der Zeit auszuufern. Auch die Nutzung von Standardgruppen und Delegation derer Rechte an eigene Gruppen (etwa durch Delegation von "Account Operators" an Helpdesk-Mitarbeiter) gewähren in der Regel mehr Rechte als tatsächlich benötigt.

### 2 7 Unsichere Authentisierung

Sogenannte "Legacy" (also historische) Authentisierungsmechanismen im Bereich AD wie LM (LAN Manager) und NTLM (NT LAN Manager) v1 gelten heute als unsicher und können von Angreifern unter bestimmten Bedingungen leicht umgangen werden. Dadurch kann ein Angreifer Rechte erhalten und missbrauchen, ohne Benutzerpasswörter zu kennen, zu erraten oder anderweitig zu brechen und so die Domäne oder Teile von dieser kompromittieren.

### 2 8 Anmeldung von AD-Administratoren an Systemen niedriger Vertrauensstufen

Es muss davon ausgegangen werden, dass Schadcode auf verschiedene Systeme wie etwa normale Workstations oder Server gelangt. Ein Angreifer, der hierüber Zugriff erhält, wird nach weiteren Credentials suchen, die er missbrauchen kann. Melden sich privilegierte Accounts an allen möglichen IT-Systemen an, so erhält der Angreifer eine Vielzahl von Chancen, die Credentials abzugreifen und sich zusätzliche Berechtigungen zu verschaffen, insbesondere wenn die Credentials dort gecached werden.

### 2 9 Fehlende Überwachung der Mitgliedschaft in privilegierten Gruppen

In den meisten Institutionen wächst die Anzahl der Konten mit administrativen Rechten stetig an und wird selten oder nie bereinigt. Dies verletzt das Prinzip der minimalen Rechte (Least Privilege) und führt dazu, dass Angreifer immer mehr Möglichkeiten haben, sich zusätzliche Berechtigungen zu verschaffen und zu missbrauchen.

### 2 10 Zu mächtige oder schwach gesicherte Dienstkonten

Anbieter von Anwendungssoftware setzen manchmal DA-Rechte für Dienstkonten voraus, um das Testen und Ausbringen ihrer Produkte zu vereinfachen, obwohl für den Betrieb deutlich weniger Rechte notwendig wären. Die zusätzlichen Rechte des Dienstkontos können von Angreifern missbraucht werden, um sich in der Domäne weiterzubewegen. Da die Credentials eines Dienstes, der im Kontext eines Dienstkontos ausgeführt wird, im geschützten Speicher des LSASS vorgehalten werden, kann der Angreifer diese dort extrahieren. So kann ein einzelner schwach gesicherter Serviceaccount zur Kompromittierung der gesamten Domäne führen.

Insbesondere gilt dies, wenn das Dienstkonto mit einem schwachen Passwort gesichert ist. Denn ein Angreifer kann beim Einsatz von Kerberos-Authentisierung ohne weiteres ein TGS-(Ticket Granting Service)-Ticket anfordern, in welchem das Passwort des Dienstaccounts verarbeitet ist, und letzteres offline per Brute-Force brechen.

### 2 11 Nutzung desselben lokalen Administratorpassworts auf mehreren Systemen

Lokale Konten können sich auf einem System anmelden, auch wenn es nicht mit der Domäne verbunden ist. Werden dieselben Credentials auf mehreren Systemen verwendet, kann der Administrator sich auf den anderen Systemen ebenfalls anmelden. Damit steigt die Gefahr, dass ein Angreifer auf einem der Systeme Domänencredentials mit höheren Rechten findet und diese missbrauchen kann, um die Domäne zu kompromittieren.

### 2 12 Fehlende Entfernung nicht mehr verwendeter Konten aus dem AD

Angreifer können nicht mehr verwendete Accounts, die im AD aber noch vorhanden sind, bevorzugt für Angriffe zu nutzen versuchen, da ein Missbrauch mangels Eigentümer möglicherweise länger nicht bemerkt wird.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz von Active Directory aufgeführt. Grundsätzlich ist der IT-Betrieb für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt. Der ISB ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### APP.2.2.A1 Planung des Active Directory [Fachverantwortliche]

Es MUSS ein geeignetes, möglichst hohes Domain Functional Level gewählt. Die Begründung SOLLTE geeignet dokumentiert werden. Ein bedarfsgerechtes Active Directory-Berechtigungskonzept MUSS entworfen werden. Administrative Delegationen MÜSSEN mit restriktiven und bedarfsgerechten Berechtigungen ausgestattet sein. Die geplante Active Directory-Struktur einschließlich etwaiger Schema-Änderungen SOLLTE nachvollziehbar dokumentiert sein.

#### APP.2.2.A2 Planung der Active Directory-Administration [Fachverantwortliche]

Es MUSS ein rollenbasiertes Berechtigungskonzept erstellt werden. Alle administrativen Aufgabenbereiche und Berechtigungen SOLLTEN geeignet dokumentiert sein.

In großen Domänen MUSS eine Aufteilung der administrativen Benutzer bezüglich Diensteverwaltung und Datenverwaltung des Active Directory existieren. Zusätzlich MÜSSEN hier die administrativen Aufgaben im Active Directory nach einem Delegationsmodell überschneidungsfrei verteilt sein.

#### APP.2.2.A3 Planung der Gruppenrichtlinien unter Windows

Es MUSS ein Konzept zur Einrichtung von Gruppenrichtlinien vorliegen. Mehrfachüberdeckungen MÜSSEN beim Gruppenrichtlinienkonzept möglichst vermieden werden. Durch die Dokumentation des Gruppenrichtlinienkonzepts MÜSSEN Ausnahmeregelungen erkannt werden können. Alle Gruppenrichtlinienobjekte MÜSSEN durch restriktive Zugriffsrechte geschützt sein. Für die Parameter in allen Gruppenrichtlinienobjekten MÜSSEN sichere Vorgaben festgelegt sein.

#### APP.2.2.A4 Schulung zur Active Directory-Verwaltung

Die Administratoren MÜSSEN mit allen Sicherheitsmechanismen und -aspekten von Active Directory in ihrem Tätigkeitsbereich vertraut sein. Sie SOLLTEN für die Arbeit mit Active Directory vor der Einrichtung sowie regelmäßig geschult sein.

#### APP.2.2.A5 Härtung des Active Directory

Built-in-Accounts MÜSSEN mit komplexen Passwörtern versehen werden und ausschließlich als Notfallkonten dienen. Privilegierte Accounts MÜSSEN Mitglieder der Gruppe Protected Users sein. Für Dienstkonten MÜSSEN (Group) Managed Service Accounts verwendet werden.

Für alle Domänen-Controller MÜSSEN restriktive Zugriffsrechte auf Betriebssystemebene vergeben sein. Der Active Directory-Restore-Modus MUSS durch ein geeignetes Passwort geschützt sein. Arbeiten in diesem Modus SOLLTEN nur unter Einhaltung des Vier-Augen-Prinzips erfolgen.

Es SOLLTE regelmäßig ein Abbild des Domänencontrollers erstellt werden. Die Berechtigungen für die Gruppe "Jeder" MUSS beschränkt werden. Die Domänencontroller MUSS gegen unautorisierte Neustarts geschützt sein.

Die Richtlinien für Domänen und Domänencontroller MÜSSEN sichere Einstellungen für Kennworte, Kontensperrung, Kerberos-Authentisierung, Benutzerrechte und Überwachung umfassen. Eine ausreichende Größe für das Sicherheitsprotokoll des Domänen-Controllers MUSS eingestellt sein. Bei externen Vertrauensstellungen zu anderen Domänen MÜSSEN Autorisierungsdaten der Benutzer gefiltert und anonymisiert werden.

#### APP.2.2.A6 Aufrechterhaltung der Betriebssicherheit von Active Directory

Alle Vertrauensbeziehungen im AD MÜSSEN regelmäßig evaluiert werden.

Die Dienste-Administratoren auf dem Domänencontroller DÜRFEN nur die notwendigen Rechte besitzen. Diese Rechte MÜSSEN in regelmäßigen Abständen überprüft werden. Die Gruppe der Domänenadministratoren MUSS leer oder möglichst klein sein. Nicht mehr verwendete Konten MÜSSEN im AD deaktiviert oder gelöscht werden.

Alle notwendigen Parameter des Active Directory SOLLTEN als Basisinformationen aktuell und nachvollziehbar festgehalten werden.

#### APP.2.2.A7 Umsetzung sicherer Verwaltungsmethoden für Active Directory [Fachverantwortliche]

Administratorkonten DÜRFEN NICHT für die gewöhnliche tägliche Arbeit verwendet werden. Serveradministrator-Konten DÜRFEN NICHT auf Workstations verwendet werden. Domänenadministrator-Konten DÜRFEN NICHT auf Workstations oder Servern genutzt werden.

Jeder Account MUSS sich eindeutig einem Mitarbeiter zuordnen lassen.

Die Anzahl der Dienste-Administratoren und der Datenadministratoren des Active Directory MUSS auf das notwendige Minimum vertrauenswürdiger Personen reduziert sein. Ihre Konten MÜSSEN angemessen abgesichert sein.

Das Standardkonto "Administrator" SOLLTE umbenannt und ein unprivilegiertes Konto mit dem Namen "Administrator" SOLLTE erstellt sein. Alltägliche, nichtadministrative Aufgaben MÜSSEN mit unprivilegierten Benutzerkonten durchgeführt werden.

Es MUSS sichergestellt sein, dass die Verwaltung von Dienste-Administratorkonten ausschließlich von Mitgliedern der Dienste-Administratorgruppe erfolgt. Die Gruppe "Kontenoperatoren" SOLLTE leer sein.

Administratoren SOLLTEN der Gruppe "Schema-Admins" nur temporär für den Zeitraum der Schema-Änderungen zugewiesen werden. Für die Gruppen "Organisations-Admins" und "Domänen-Admins" zur Administration der Stammdomäne SOLLTE ein Vier-Augen-Prinzip etabliert sein.

Die Arbeitsplätze zur Administration des Active Directory MÜSSEN ausreichend abgesichert sein. Bei Remoteadministration der Domänen-Controller MUSS der Datenverkehr geeignet verschlüsselt sein.

Es MUSS sichergestellt sein, dass die Gruppen "Administratoren" bzw. "Domänenadministratoren" Besitzer des Domänenstammobjektes der jeweiligen Domäne sind.

Der Einsatz von domänenlokalen Gruppen für die Steuerung der Leseberechtigung für Objektattribute SOLLTE vermieden werden.

Der Papierkorb des AD SOLLTE aktiviert werden.

In großen Institutionen SOLLTE mit einer Enterprise Identity Management-Lösung sichergestellt werden, dass die Rechte aller Anwender definierten Vorgaben entsprechen.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Active Directory. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### APP.2.2.A8 Konfiguration des sicheren Kanals unter Windows

Der Sichere Kanal unter Windows SOLLTE entsprechend den Sicherheitsanforderungen und den lokalen Gegebenheiten konfiguriert sein. Dabei SOLLTEN alle relevanten Gruppenrichtlinienparameter berücksichtigt werden.

#### APP.2.2.A9 Schutz der Authentisierung beim Einsatz von Active Directory

In der Umgebung des Active Directory SOLLTE konsequent das Authentisierungsprotokoll Kerberos eingesetzt werden. Wenn aus Kompatibilitätsgründen übergangsweise NTLMv2 eingesetzt wird, SOLLTE die Migration auf Kerberos geplant und terminiert werden. Die LM-Authentisierung SOLLTE deaktiviert sein. Der SMB-Datenverkehr SOLLTE signiert sein. Anonyme Zugriffe auf Domänencontroller SOLLTEN unterbunden sein.

#### APP.2.2.A10 Sicherer Einsatz von DNS für Active Directory

Es SOLLTEN integrierte DNS-Zonen bzw. die sichere dynamische Aktualisierung der DNS-Daten verwendet werden, um DNS-Clientabfragen durch unautorisierte Systeme zu vermeiden. Der Zugriff auf die Konfigurationsdaten des DNS-Servers SOLLTE nur von administrativen Konten erlaubt sein. Der DNS-Cache auf den DNS-Servern SOLLTE vor unberechtigten Änderungen geschützt sein. Der Zugriff auf den DNS-Dienst der Domänen-Controller SOLLTE auf das notwendige Maß beschränkt sein. Die Netzaktivitäten in Bezug auf DNS-Anfragen SOLLTEN überwacht werden. Der Zugriff auf die DNS-Daten im Active Directory SOLLTE mittels ACLs auf Administratoren beschränkt sein.

Sekundäre DNS-Zonen SOLLTEN vermieden werden. Zumindest SOLLTE die Zonen-Datei vor unbefugtem Zugriff geschützt werden.

Wird IPsec eingesetzt, um die DNS-Kommunikation abzusichern, SOLLTE ein ausreichender Datendurchsatz im Netz gewährleistet sein.

#### APP.2.2.A11 Überwachung der Active Directory-Infrastruktur

Die Active Directory-Infrastruktur SOLLTE anhand der systemeigenen Ereignisse überwacht und protokolliert werden. Die Ergebnisse der Sicherheitsüberwachung des Active Directory SOLLTEN regelmäßig ausgewertet werden. Verfügbarkeit und Systemressourcen der Domänen-Controller SOLLTEN überwacht werden. Änderungen auf Domänen-Ebene und an der Gesamtstruktur des Active Directory SOLLTEN überwacht, protokolliert und ausgewertet werden.

#### APP.2.2.A12 Datensicherung für Domänen-Controller

Es SOLLTE eine Datensicherungs- und Wiederherstellungsrichtlinie für Domänen-Controller existieren. Die eingesetzte Sicherungssoftware SOLLTE explizit vom Hersteller für die Datensicherung von Domänen-Controllern freigegeben sein. Für die Domänen-Controller SOLLTE ein separates Datensicherungskonto mit Dienste-Administratorenrechten eingerichtet sein. Die Anzahl der Mitglieder der Gruppe "Sicherungs-Operatoren" SOLLTE auf das notwendige Maß begrenzt sein. Der Zugriff auf das AdminSDHolder-Objekt SOLLTE zum Schutz der Berechtigungen besonders geschützt sein.

Die Daten der Domänen-Controller SOLLTEN in regelmäßigen Abständen gesichert werden. Dabei SOLLTE ein Verfahren eingesetzt werden, das veraltete Objekte weitgehend vermeidet.

Die Sicherungsmedien SOLLTEN an einem geeigneten Standort aufbewahrt werden. Der korrekte Ablauf und das Wiedereinspielen von Datensicherungen der Domänen-Controller SOLLTEN in regelmäßigen Abständen überprüft werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### APP.2.2.A13 Zwei-Faktor-Authentifizierung(CIA)

Privilegierte Konten im Bereich des AD SOLLTEN mittels Zwei-Faktor-Authentifizierung geschützt werden.

#### APP.2.2.A14 Dedizierte privilegierte Administrationssysteme(CIA)

Die Administration des Active Directory SOLLTE auf dedizierte Administrationssysteme eingeschränkt werden. Diese SOLLTEN durch die eingeschränkte Aufgabenstellung besonders stark gehärtet sein.

#### APP.2.2.A15 Trennung von Administrations- und Produktionsumgebung(CIA)

Besonders kritische Systeme, wie Domaincontroller und Systeme zur Administration der Domain, SOLLTEN in einen eigenen Forest ausgegliedert werden, der einen einseitigen Trust in Richtung des Produktions-Forests besitzt.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Active Directory" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [ADRL] AD Reading Library

  

 Mit weiterführender Literatur des AD Security Blogs, (zuletzt abgerufen am 28.09.2017)  
 [https://adsecurity.org/page\_id=41 ](https://adsecurity.org/page_id=41)

 
* #### [ADSB] Active Directory Security Blog

  

 Sean Metcalf, (zuletzt abgerufen am 28.09.2017)  
 [https://adsecurity.org ](https://adsecurity.org)

 
* #### [ADSR] Liste von Security Resourcen

  

 AD Security Blog (zuletzt abgerufen am 28.09.2017)  
 [https://adsecurity.org/page\_id=399](https://adsecurity.org/page_id=399) 

 
* #### [ESAE] Enhanced Security Administrative Environment

  

 Microsoft TechNet (zuletzt abgerufen am 28.09.2017)   
 <https://docs.microsoft.com/de-de/windows-server/identity/securing-privileged-access/securing-privileged-access>

 
* #### [PAW] Privileged Access Workstations

  

 Microsoft TechNet, 04.2016  
 [http://download.microsoft.com/download/9/3/9/9392A4D2-D530-4344-8447-4A7CF1C01AEE/Privileged%20Access%20Workstation\_Datasheet.pdf](http://download.microsoft.com/download/9/3/9/9392A4D2-D530-4344-8447-4A7CF1C01AEE/Privileged%20Access%20Workstation_Datasheet.pdf)

 
* #### [TN283324] Einstiegspunkt Active Directory für Windwos Server 2012 (R2)

  

 Microsoft TechNet, (zuletzt abgerufen am 28.09.2017)  
 [https://technet.microsoft.com/en-us/library/dn283324.aspx ](https://technet.microsoft.com/en-us/library/dn283324.aspx)

 
* #### [TN378801] Einstiegspunkt Active Directory für Windows Server 2008 R2

  

 Microsoft TechNet, 05.2009   
 <https://technet.microsoft.com/en-us/library/dd378801.aspx>

 
* #### [TNAD] Einstiegspunkt für Active Directoy für Windows Server aktuell

  

 Microsoft TechNet  
 https://technet.microsoft.com/en-us/windows-server-docs/identity/ad-ds/active-directory-domain-services

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Active Directory" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
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
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.36 Identitätsdiebstahl
* G 0.37 Abstreiten von Handlungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.42 Social Engineering
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

