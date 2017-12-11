1 Beschreibung
--------------

### 1.1 Einleitung

In diesem Baustein wird der sichere Austausch von Informationen betrachtet, mit dem Fokus auf digitale und analoge Datenträger als Transportmedien, aber auch der Informationsaustausch bei persönlichen Treffen oder über IT-Netze. Auch bei einer breitbandigen Netzanbindung kann es sinnvoll oder notwendig sein, für den Informationsaustausch Datenträger zu übermitteln. Ein Grund kann sein, dass es keine oder keine hinreichend vertrauenswürdige Vernetzung zwischen den betroffenen IT-Systemen gibt. Datenträger können bei persönlichen Treffen oder auch per Versand ausgetauscht werden. 

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, den Informationsaustausch zwischen verschiedenen Kommunikationspartnern und IT-Systemen abzusichern. Insbesondere wird dargestellt, was beim Datenträgeraustausch zu beachten ist, um die transportierten Daten angemessen zu schützen.

### 1.3 Abgrenzung

Dieser Baustein ist immer dann anzuwenden, wenn ein Informationsaustausch mit Stellen außerhalb der eigenen Institution bzw. Liegenschaft erfolgt und dabei nicht das interne Netz verwendet wird. Er ist vor allem anzuwenden, wenn 

* neue Transportwege aufgebaut werden (neue Kommunikationspartner, neue Medien, neue Netze),
* der Informationsaustausch mit Hilfe von Datenträgern erfolgt. Hierbei sind neben der Übermittlung insbesondere auch die Speicherung und der Umgang mit den Datenträgern zu berücksichtigen. 
Die Absicherung von Netzverbindungen wird in anderen Bausteinen des IT-Grundschutz-Kompendiums behandelt. Auch die Weiterverarbeitung im Ziel-IT-System wird nicht betrachtet. In diesem Baustein stehen die grundsätzlichen Regelungen für einen sicheren Informationsaustausch im Vordergrund, vor allem bei der Nutzung von mobilen Datenträgern. Nicht betrachtet werden die Gründe, warum es keine oder keine hinreichend vertrauenswürdige Vernetzung zwischen den betroffenen IT-Systemen gibt. 

Daneben wird in diesem Baustein auch die Speicherung der Daten auf dem Sender- und Empfänger-System, soweit es in direktem Zusammenhang mit dem Datenträgeraustausch steht, sowie der Umgang mit den Datenträgern vor bzw. nach dem Transfer berücksichtigt. Dieser Baustein betrachtet mobile Datenträger wie z. B. Wechselplatten, optische Datenträger, USB-Sticks und -Festplatten und nicht zu vergessen Papierdokumente. 

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind für den Informations- und Datenträgeraustausch von besonderer Bedeutung:

### 2 1 Defekte Datenträger

Bei allen Arten von Datenträgern können Beschädigungen, Fehler oder Ausfälle auftreten. Zum Problem werden sie dann, wenn die auf den Datenträgern gespeicherten Informationen an keiner anderen Stelle gespeichert sind und sich nicht schnell und einfach rekonstruieren lassen. 

**Unzulässige Temperatur und Luftfeuchte **

Extreme Temperaturen und Feuchtigkeit können sich auf eine ordnungsgemäße Funktion von Datenträgern auswirken. Zu jeder Art von Datenträgern gibt es festgelegte Grenzwerte, innerhalb derer die ordnungsgemäße Funktion gewährleistet ist. Werden diese über- oder unterschritten, kann es zu Betriebsstörungen und zu Geräteausfällen kommen. Bei digitalen Speichermedien können zu große Temperaturschwankungen oder zu große Luftfeuchtigkeit zu Datenfehlern führen. 

**Unsachgemäß verpackte Datenträger**

Beim Transport oder Versand sind Datenträger besonderen Belastungen ausgesetzt. Bei Datenträgern können bereits geringfügige Verunreinigungen zu Datenfehlern führen. Festplatten können durch den "Headcrash" des Schreib-/Lesekopfes, Bänder oder Kassetten durch direkte mechanische Einwirkung zerstört werden. CD-ROM s oder DVDs können durch Verkratzen der Oberfläche unbrauchbar werden. 

**Datenverlust durch starke Magnetfelder** 

Typische Datenträger mit magnetisierbaren Speichermedien sind Wechselplatten, Kassetten und Bänder. Diese Datenträger sind empfindlich gegenüber magnetischer Störstrahlung, so dass die Nähe zu solchen Strahlungsquellen vermieden werden sollte.

### 2 2 Nicht fristgerecht verfügbare Datenträger

Beim Datenträgeraustausch ist es bei vielen Geschäftsprozessen von besonderer Bedeutung, dass diese fristgerecht ihren Empfänger erreichen bzw. dort zeitnah genutzt werden können. Auch kleine Fehler in der Kennzeichnung können dazu führen, dass ein Datenträger nicht in der erforderlichen Zeit sein Ziel erreicht. Wenn vor Ort die notwendigen Schnittstellen bzw. Betriebsmittel nicht vorhanden sind, kann ein Datenträger unter Umständen nicht ausgelesen werden. Die resultierenden Verzögerungen können zu erheblichen Schäden führen.

### 2 3 Ungeregelte Weitergabe von Informationen oder Datenträgern

Bei einer ungeregelten Weitergabe bzw. ungeordneter Zustellung von Informationen oder Datenträgern besteht die Gefahr, dass vertrauliche Informationen in unbefugte Hände gelangen oder das gewünschte Ziel nicht rechtzeitig erreichen.

### 2 4 Unzureichendes Schlüsselmanagement bei Verschlüsselung

Werden zum Schutz der Vertraulichkeit zu übermittelnder Daten Verschlüsselungssysteme eingesetzt, so kann aufgrund eines unzureichenden Schlüsselmanagements der gewünschte Schutz unterlaufen werden, beispielsweise wenn leicht zu erratende Schlüssel gewählt wurden oder wenn die zur Verschlüsselung bzw. Entschlüsselung eingesetzten kryptographischen Schlüssel den Kommunikationspartner nicht auf einem sicheren Weg erreichen. Einfachstes Negativbeispiel ist der Versand der verschlüsselten Informationen und des benutzten Schlüssels auf oder mit demselben Datenträger. In diesem Fall kann jeder, der in den Besitz des Datenträgers gelangt, die Informationen entschlüsseln, vorausgesetzt, dass das bei der Verschlüsselung eingesetzte Verfahren bekannt ist.

### 2 5 Verlust von Datenträgern beim Versand

Werden Datenträger in nicht sonderlich stabilen Behältnissen (Briefumschlägen oder sonstigen Verpackungen) versandt, besteht die Gefahr, dass die Datenträger bei Beschädigung der Verpackung verloren gehen. Auch besteht die Gefahr des Verlustes beim Empfänger, auf dem Postweg oder durch Unachtsamkeit eines Boten. Datenträger werden immer kleiner, so dass sie auch leichter beim Transport verloren gehen können. 

Wenn die Informationen auf den Datenträgern nicht verschlüsselt sind, können sie außerdem bei einem Verlust in die falschen Hände geraten.

### 2 6 Weitergabe falscher oder interner Informationen

Bei der Weitergabe von Informationen kommt es immer wieder vor, dass neben den gewünschten Informationen auch andere Informationen übermittelt werden. Dadurch geraten immer wieder vertrauliche oder nicht für die Veröffentlichung geeignete Informationen in die falschen Hände. So kommt es vor, dass Datenträger weitergegeben werden, ohne dass die vorher darauf gespeicherten Daten in geeigneter Weise gelöscht wurden. Ebenso kann es vorkommen, dass vertrauliche Unterlagen versehentlich an den falschen Empfänger versandt werden oder dass Briefe zusammen mit internen Kommentaren ausgedruckt und versandt werden.

### 2 7 Diebstahl, Manipulation oder Zerstörung von Datenträgern

Außentäter, aber auch Innentäter, können aus unterschiedlichen Beweggründen (Ausspähung, Rache, Böswilligkeit, Frust) heraus versuchen, Datenträger zu stehlen, zu manipulieren oder zu zerstören. Die Manipulationen reichen von der unerlaubten Einsichtnahme in schützenswerte Daten über inhaltliche Änderung von Daten bis hin zur Zerstörung von Datenträgern.

### 2 8 Schadprogramme in übertragenen Dateien oder auf Datenträgern

Wenn die Arbeitsumgebung unzureichend gegen Schadprogramme abgesichert ist, könnten sich auf Datenträger, die an Externe weitergegeben werden, Schadprogramme befinden. Dadurch könnten die gespeicherten Daten zerstört oder verfälscht werden, aber vor allem IT-Systeme auf Empfängerseite kompromittiert werden. Aber auch der Imageverlust und der finanzielle Schaden, der durch Schadprogramme entstehen kann, sind von großer Bedeutung.

### 2 9 Unberechtigtes Kopieren von Informationen oder der Datenträger

Werden Informationen oder Datenträger über einen unsicheren Transportweg ausgetauscht oder transportiert, besteht die Gefahr, dass die übermittelten Informationen bei der Beförderung durch Unbefugte kopiert werden. Ebenso könnten Angreifer versuchen, die Kommunikation über IT-Netze abzuhören.

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Schutz beim Informations- und Datenträgeraustausch aufgeführt. Grundsätzlich ist der Informationssicherheitsbeauftragte (ISB) für die Erfüllung der Anforderungen zuständig. Abweichungen hiervon werden in den entsprechenden Anforderungen gesondert erwähnt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### OPS.1.2.3.A1 Festlegung zulässiger Kommunikationspartner [Leiter Organisation]

In der Institution MUSS festgelegt werden, welche Kommunikationspartner welche Informationen erhalten und weitergeben dürfen. Dies MUSS für alle Einsatzzwecke in der Institution kommuniziert werden. Vor dem Austausch von Informationen MUSS geklärt werden, dass der Empfänger die notwendigen Berechtigungen für den Erhalt und die Weiterverarbeitung der Informationen besitzt. 

#### OPS.1.2.3.A2 Regelung des Informationsaustausches [Leiter Organisation]

Werden Informationen ausgetauscht, MUSS im Vorfeld geklärt werden, wie schutzbedürftig die relevanten Informationen sind, mit wem die Informationen ausgetauscht werden dürfen und wie sie dabei konkret zu schützen sind. Die Mitarbeiter MÜSSEN dazu ausreichend sensibilisiert werden. Die Empfänger MÜSSEN darauf hingewiesen werden, dass die übermittelten Daten nur zu dem Zweck benutzt werden dürfen, zu dem sie weitergegeben wurden.

#### OPS.1.2.3.A3 Unterweisung des Personals zum Informationsaustausch [Fachverantwortliche]

Das Personal MUSS darüber informiert werden, welche Rahmenbedingungen für den Informationsaustausch gelten. Es MUSS wissen, welche Informationen sie wann, wo und wie weitergeben dürfen.

#### OPS.1.2.3.A4 Schutz vor Schadsoftware [Benutzer]

Digitale Daten MÜSSEN sowohl vom Sender vor Versand als auch vom Empfänger auf Schadsoftware überprüft werden. Die eingesetzten Virenschutz-Programme müssen dem aktuellen Stand der Technik entsprechen.

#### OPS.1.2.3.A5 Verlustmeldung [Benutzer]

Es MUSS umgehend gemeldet werden, wenn ein Datenträger beim Datenträgeraustausch verloren oder gestohlen wird oder der Verdacht auf Manipulation besteht. Hierfür MUSS es in jeder Institution klare Meldewege und Ansprechpartner geben.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Informations- und Datenträgeraustausch. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### OPS.1.2.3.A6 Vereinbarungen zum Informationsaustausch mit Externen [Leiter Organisation]

Bei einem regelmäßigen Informationsaustausch mit externen Partnern SOLLTEN die Rahmenbedingungen hierfür formal vereinbart werden. 

#### OPS.1.2.3.A7 Regelung des Datenträgeraustausches [Leiter Organisation]

Der ordnungsgemäße Datenträgeraustausch SOLLTE geregelt werden. Es SOLLTE festgelegt werden, wie die Datenträger in der eigenen Institution, beim Transport und beim Empfänger zu schützen sind. Bei der Wahl der Versandart SOLLTE die Art der Datenträger und der Schutzbedarf der Informationen berücksichtigt werden. Außerdem SOLLTE festgelegt werden, wann und wie Datenträger physikalisch gelöscht werden.

#### OPS.1.2.3.A8 Physikalisches Löschen von Datenträgern vor und nach Verwendung [Benutzer]

Vor und nach einem Datenträgeraustausch SOLLTEN zuvor anderweitig verwendete Datenträger physikalisch gelöscht werden. Den Mitarbeitern SOLLTEN geeignete Programme zum physikalischen Löschen zur Verfügung gestellt werden.

#### OPS.1.2.3.A9 Beseitigung von Restinformationen in Dateien vor Weitergabe [Benutzer]

Die Benutzer SOLLTEN hinsichtlich der Gefahren von Rest- und Zusatzinformationen in Dateien informiert werden. Den Benutzern SOLLTE vermittelt werden, wie sie Rest- und Zusatzinformationen in Dateien vermeiden können. Restinformationen SOLLTEN entsprechend beseitigt werden. Vor der Weitergabe von Dateien SOLLTEN stichprobenhafte Überprüfungen der Dateien auf enthaltene Restinformationen durchgeführt werden.

#### OPS.1.2.3.A10 Abschluss von Vertraulichkeitsvereinbarungen [Leiter Organisation]

Mit Externen SOLLTEN Vertraulichkeitsvereinbarungen getroffen werden, bevor sie Zugang und Zugriff auf vertrauliche Informationen erhalten. Durch die verwendeten Vertraulichkeitsvereinbarungen SOLLTEN alle wichtigen Aspekte zum Schutz von vertraulichen Informationen berücksichtigt werden.

#### OPS.1.2.3.A11 Kompatibilitätsprüfung des Sender- und Empfängersystems [IT-Betrieb]

Vor einem Informationsaustausch SOLLTEN die eingesetzten Systeme und Produkte auf Sender- und Empfängerseite auf ihre Kompatibilität geprüft werden. 

#### OPS.1.2.3.A12 Angemessene Kennzeichnung der Datenträger beim Versand [Benutzer]

Bei der Kennzeichnung von Datenträgern SOLLTE sichergestellt werden, dass Absender und Empfänger unmittelbar zu identifizieren sind. Die Kennzeichnung der Datenträger bzw. deren Verpackung SOLLTE den Inhalt der Datenträger eindeutig für den Empfänger erkennbar machen. Die Kennzeichnung von Datenträgern mit schützenswerten Informationen SOLLTE KEINE Rückschlüsse auf Art und Inhalte der Informationen zulassen.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### OPS.1.2.3.A13 Verschlüsselung und digitale Signaturen [Benutzer](CI)

Vertrauliche Informationen SOLLTEN vor einem Informationsaustausch verschlüsselt werden. Informationen mit hohem Integritätsanspruch SOLLTEN digital signiert werden. Hierfür SOLLTEN geeignete Kryptoverfahren ausgewählt werden, die dem Schutzbedarf entsprechen und auf Sender- und Empfängerseite problemlos genutzt werden können.** **Für den Einsatz von kryptographischen Verfahren SOLLTE ein geeignetes Schlüsselmanagement etabliert werden. 

#### OPS.1.2.3.A14 Datenträgerverwaltung [Leiter Organisation, IT-Betrieb](CIA)

Bei höherem Schutzbedarf SOLLTE eine Datenträgerverwaltung eingerichtet werden, um den Zugriff auf Datenträger, deren Kennzeichnung und ordnungsgemäße Aufbewahrung zu regeln. Für alle Arten von Datenträgern SOLLTE der ordnungsgemäße Umgang inklusive Aufbewahrung, Weitergabe, Transport und Löschung geregelt sein. Es SOLLTE ein Bestandsverzeichnis erstellt werden. Die Datenträger SOLLTEN gemäß den Herstellerangaben sachgerecht behandelt werden. 

#### OPS.1.2.3.A15 Sichere Versandart und Verpackung [Poststelle, Benutzer](C)

Sofern Informationen einem erhöhten Schutzbedarf unterliegen, SOLLTE geprüft werden, wie diese bei einem Datenträgeraustausch angemessen geschützt werden können. Es SOLLTEN sichere Versandverpackungen für Datenträger verwendet werden, die Manipulationen durch Veränderungen an der Verpackung erkennen lassen. Der Versender SOLLTE die Poststelle auf notwendige Versand- und Verpackungsarten hinweisen. Grundsätzlich SOLLTEN die Daten verschlüsselt werden.

#### OPS.1.2.3.A16 Sichere Aufbewahrung der Datenträger vor und nach Versand [Benutzer, Poststelle](CIA)

Beschriebene Datenträger SOLLTEN so aufbewahrt werden, dass nur berechtigte Benutzer darauf zugreifen können. Alle beteiligten Mitarbeiter SOLLTEN auf eine sachgerechte und sichere Aufbewahrung und Handhabung der Datenträger hingewiesen werden.

#### OPS.1.2.3.A17 Verifizieren von Datenträgern vor Versand [Benutzer](CI)

Vor dem Versenden von Datenträgern SOLLTE überprüft werden, 

* ob die gewünschten Informationen vollständig enthalten sind und 
* ob keine zusätzlichen Informationen enthalten sind, die nicht weitergegeben werden sollen. 
#### OPS.1.2.3.A18 Sicherungskopie der übermittelten Daten [Benutzer](A)

Sind die zu übertragenden Daten nur zum Zweck der Datenübertragung erstellt bzw. zusammengestellt worden und nicht auf einem weiteren Medium gespeichert, SOLLTE eine Sicherungskopie dieser Daten vorgehalten werden. Bei Verlust oder Beschädigung der Daten auf dem Transportweg kann der Versand mit geringfügigem Aufwand erneut erfolgen.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Informations- und Datenträgeraustausch" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001] ISO/IEC 27001:2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [NIST800150] Guide to Cyber Threat Information Sharing

  

 Special Publication 800-150, National Institute of Standards and Technology (NIST), 10.2016  
 <http://dx.doi.org/10.6028/NIST.SP.800-150>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Informations- und Datenträgeraustausch" von Bedeutung.

* G 0.2 Ungünstige klimatische Bedingungen
* G 0.4 Verschmutzung, Staub, Korrosion
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.16 Diebstahl von Geräten, Datenträgern oder Dokumenten
* G 0.17 Verlust von Geräten, Datenträgern oder Dokumenten
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.22 Manipulation von Informationen
* G 0.24 Zerstörung von Geräten oder Datenträgern
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.38 Missbrauch personenbezogener Daten
* G 0.39 Schadprogramme
* G 0.42 Social Engineering
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

