1 description
--------------

### 1.1 Introduction

Businesses and governments are storing more and more data and at the same time relying more and more on it. Data is then lost, eg. B. by defective hardware or malware, can cause serious damage. However, regular data backups minimize such effects. A data backup should ensure that redundant data can be used to resume IT operations at short notice if parts of the operational data are lost.

### 1.2 Life cycle

** planning and conception **

In order to set up an effective data backup, possible influencing factors must first be identified (see CON.3.M1 * Survey of influencing factors of the data backup *) and then an appropriate procedure established (see CON.3.M2 * Specification of the procedure for data backup *). Based on this, the responsible persons must develop a minimum data security concept (see CON.3.M4 * Creation of a minimum data protection concept *) and a data backup concept (see CON.3.M6 * Development of a data protection concept *).

**Procurement**

Backups are usually done using backup programs. However, not all programs are suitable for each institution. Therefore, the backup software must be carefully selected (see CON.3.M7 * Obtaining a suitable backup system *).

**Implementation**

All employees must be informed about the data backups and should know which tasks they themselves have to fulfill (see CON.3.M10 * Data backup obligation *). Likewise, a backup copy of the software used should be created (see CON.3.M11 * Backup copy of the software used *).

All data backups are suitable for documentation (see CON.3.M6 * Development of a data protection concept *).

**Business**

The steps and procedures specified in the data protection concept must be carried out regularly (see CON.3.M5 * Regular data backup *).

Backups usually contain a lot of sensitive information about the institution. Therefore it must be ensured that the backup volumes are kept protected (see CON.3.M12 * Suitable storage of backup volumes *).

** Emergency Preparedness **

Backups must also work in an emergency, d. H. the backed-up data must be easy and fast to restore. To ensure this, regular tests must be performed (see CON.3.A8 * Functional Tests and Recoverability Check *).

2 measures
-----------

In the following, specific implementation notes are listed in the "Data backup concept" section.

### 2.1 Basic measures

The following measures should be implemented as a priority:

#### CON.3.M1 Survey of influencing factors of data backup [IT-Betrieb, Fachverantwortliche]

For each IT system, possibly even for individual IT applications of particular importance, the following influencing factors must be determined. For this, the system administrators and the persons responsible for the individual IT applications can be interviewed. The results are comprehensible to document. In detail must be determined:

* Specification of the data to be backed up: The data stock of the IT system (the IT application) required for the specialized tasks should be determined. These include the application and operating software, the system data (eg, initialization files, macro definitions, configuration data, phrases, password files, access rights files), the application data itself, and log data (e.g., login log, security breach logs, data transfer logs).
* Availability requirements of the IT applications to the data: For the data specified in the first step, the availability requirements must now be specified. A proven measure of this is the indication of the maximum tolerable downtime. It indicates the period of time over which the specialist task can be continued without this data, without having to resort to backup data.
* Reconstruction of the data without data backup: To develop an economical data protection concept (see CON.3.M6 Development of a data protection concept), it is necessary to know if and with which effort destroyed data can be reconstructed if a data backup is not available is. It should be examined from which sources the data can be reconstructed and how long that would take. Examples include the file situation, printouts, surveys and surveys.
* Data volume: For the selection of the storage medium, a decisive factor is the stored and secured data volume.
* Volume of change: To determine the frequency of backup and the adequate backup procedure, it is important to know how much data changes over a given period of time. It is necessary to provide information as to whether existing files are changed in content or whether new files are being created.
* Change dates of the data: There are IT applications in which data changes only occur on certain dates, such as the payroll accounting run at the end of the month. In such cases, data backup immediately after such an appointment makes sense. Therefore, for the data to be backed up, it should be indicated whether they change daily, weekly or on specific dates.
* Deadlines: For the data, it must be clarified whether certain deadlines must be met. These may be retention periods or deletion periods in connection with personal data. These deadlines are to be considered in the data backup.
* Confidentiality of the data: The confidentiality requirement of a file is transferred to the backup copy during a data backup.
* Data integrity requirements: For data backups it must be ensured that the data has been stored with integrity and is not changed during the retention period. This is all the more important the higher the need for integrity of the user data. Therefore, the data backups should indicate how high the integrity requirement is.
* Knowledge and skills of IT users: Deciding who is responsible for data backup, the IT user himself, or dedicated staff or system administrators is what determines the knowledge and skills of IT users and what tools they have can be made available. If the time required to perform a backup for IT users is too high, this should be stated.
#### CON.3.M2 Definition of the procedure for the data backup [IT-Betrieb, Fachverantwortliche]

How a backup is to be performed is determined mainly by the influencing factors collected in CON.3.M1 * Survey of factors influencing data backup *. For each IT system and for each data type, the procedure of data backup must be defined. If necessary, even a distinction must be made for individual IT applications of the respective IT system.

The following points should be considered when establishing a data protection policy:

* Type of data backup,
* Frequency and time of data backup,
* Number of generations,
* Procedure and storage medium,
* Responsibility for data backup,
* Repository,
* Requirements for the backup archive,
* Transport modalities and
* Storage modality.
The following table shows the dependencies between the mentioned points and the influencing factors (see CON.3.M1 * Survey of influencing factors of the data backup *) and then explains:

Table: Data backup

** Type of backup **

The following types of backup exist:

* Full data backup: Full backup saves all files to be backed up to an additional disk at a given time. It is not taken into account whether the files have changed since the last backup or not. Therefore, a full data backup requires a lot of memory. The advantage is that the data is completely available for the backup time and the restoration of files is easy and fast, since only the affected files from the last full data backup must be extracted. If full data backups are rarely carried out, extensive post-modification within a file can result in a high re-entry effort.
* Incremental data backup: With incremental data backup, unlike full data backup, only the files that have changed since the last data backup (full data backup or incremental backup) are backed up. This saves storage space and shortens the time required for data backup. The incremental data backup is always based on a full data backup. At periodic intervals full data backups are generated, in the time between one or more incremental backups are completed. During the restoration, the last full data backup is taken as a basis, which is supplemented by the files changed in the meantime from the incremental backups.
* Differential backup: differential backup backs up files that have changed since the last full backup. A differential backup needs more space than an incremental one, but files can be restored more easily and quickly. For the restoration of the data, the last full data backup as well as the most recent differential, not like the incremental one, where under certain circumstances several data backups must be read in succession.
* Mirroring: Mirroring the data permanently creates an exact copy of the data in another directory or media. This is usually done transparently to the user, for example through a RAID system. Mirroring alone does not replace backup because inconsistencies, file errors, or deletions of files immediately affect the mirrored version. For example, if the original datasets are encrypted by ransomware, this directly affects the mirrored copy.
A special form of the mentioned data security strategies is the image data backup. Here, not the individual files of a disk stack are backed up, but the physical sectors of the disk. It is a full backup that can be restored very quickly to a similar hard drive.

Another form is Hierarchical Storage Management (HSM). This is primarily about using existing storage as economically as possible. Depending on the frequency with which they are accessed, files are kept on fast online storage (hard drives), swapped out to nearline storage (automatic data carrier systems), or archived to offline storage devices (magnetic tapes). At the same time, these HSM systems also offer automatic data backup routines combined from incremental data backup and full data backup.
A redundant data storage offer RAID systems (Redundant Array of Inexpensive Disks). The RAID concept describes the connection of several hard disks under the command of a so-called array controller. There are several RAID levels, of which RAID level 1 describes data mirroring. However, RAID systems do not replace data backup! They do not help with theft or fire, so the data stored on RAID systems must also be backed up to additional media and these media must also be stored in other fire sections.

In order to decide which data protection strategy should be used, the following influencing factors (see CON.3.M1 * Survey of Factors Affecting Data Backup *) have to be taken into account in order to find a suitable and at the same time economic form:

* Availability requirements: If the availability requirements are very high, data mirroring should be considered. If the availability requirements are high, a full data backup should be performed instead of an incremental data backup.
* Volume of data and volume of change: If the volume of change is close to the volume of data (for example, when using a database), the space saving of the incremental data backup is reduced so much that a full backup can be considered. However, if the volume of change is significantly smaller than the volume of data, the incremental backup saves space.
* Change dates of the data: The change dates of the data may have a small influence on the data backup strategy. If there are times when application-specific complete data must be saved (eg according to weekly, monthly or annual accounts), only a full backup is considered at these times.
* Knowledge of IT users: A data mirroring requires appropriate knowledge of the system administrator, but requires no knowledge from the user. A full data backup can also be performed by an IT user with little knowledge of the system. In contrast, incremental data protection requires more system knowledge and experience in dealing with data backups.
** Frequency and dates of data backup **

If a data loss occurs, all data is lost until the last backup. The more up-to-date the last data backup, the less data loss the institution has to cope with. At the same time, it must be noted that the time of data backup can not only be selected periodically (eg daily, weekly, weekdays), but also event-dependent data backups (eg after x transactions, after execution of a specific program, after system changes) may be necessary can.

When selecting the frequency and time of the data backup, the following influencing factors (see CON.3.M1 * Survey of the influencing factors of the data backup *) must be observed:

Availability requirements, recovery effort without data backup and change volume: The time interval of the data backups should be selected so that the restoration and re-acquisition time (reconstruction effort of the changed data for which no data backup exists) of the data changed during this period (change volume) is smaller than the maximum tolerable downtime is.
* Change dates of the data: If there are times when the data change on a large scale (eg program run for salary payment or software version change) or where the complete dataset must be available, then it is advisable to carry out a full data backup immediately afterwards , In addition to the periodic ones, the event-dependent data backup times must be defined.
** number of generations **
On the one hand, data backups are repeated at short intervals in order to have a copy of an up-to-date dataset available, on the other hand, the data backup must ensure that stored data is kept as long as possible. A full data backup is called generation. The number of generations to keep and the time gap between generations should be set. These requirements can be explained by the following examples:

* If a file is intentionally or unintentionally deleted, this file is no longer available in all subsequent backups. If it turns out that this deleted file is still needed, an older data backup must be used for the restoration, which was created before the deletion. If such a generation is no longer available, then the file must be recaptured.
* If a loss of integrity occurs in a file, eg. As by malware, it is likely that this is not noticed directly, but only offset in time. To restore the integrity of the file, you need to resort to a generation that was created before the loss of integrity.
* It can not be ruled out that a data backup was created incorrectly or incompletely. That is why it is often helpful to use another generation.
In order to be able to maintain these advantages of the generation principle, however, a boundary condition must be adhered to: the time interval between the generations must not be less than a minimum. Example: In an automated data backup process, repeated crashes of the backup run occur. This would successively overwrite all generations. This can be prevented by checking the minimum age before overwriting a generation and only overwriting it when that age is exceeded.

A generational principle can be characterized by two variables: the minimum age of the oldest generation and the number of available generations. Where:

* the higher the minimum age of the oldest generation, the greater the likelihood that a file with integrity loss (a deleted file, which is subsequently recognized as necessary) is still a precursor version,
* The larger the number of available generations, the more current the requested legacy version.
The number of generations, however, is directly related to the cost of data backup because there must be sufficient volumes of data. Since a separate data medium should be used for each generation, the number of generations must be limited to an economically reasonable level.

The following influences result for the selection of the parameters of the generation principle (see CON.3.M1 * Survey of the influencing factors of the data backup *):

* Data availability requirements and data integrity requirements: The higher the availability or integrity requirements of the data, the more generations it will take to minimize the recovery time in the event of integrity loss.
* If the loss of a file or an integrity violation may not be noticed until very late, additional quarterly or yearly backup records are recommended.
* Recovery effort without data backup: If the data is extensive, but can also be reconstructed without data backup, then this can be taken into account as another pseudo-generation.
* Data volume: The higher the data volume, the more space is needed and the higher the cost of a generation. A high volume of data can therefore limit the number of generations for economic reasons.
* Volume of Change: The higher the volume of change, the shorter the inter-generational interval should be to have as timely a version of the file as possible and to minimize the recovery effort.
** Procedure and storage medium **

Now that you have determined the type of backup, the frequency, and the generation principle, you should now select the procedure and the appropriate storage medium.

To minimize the volume of data on the storage medium, data compression algorithms can be applied. In some cases, the volume of data can be greatly reduced. However, it is important to ensure that the chosen parameters and algorithms are documented and retained for the restoration of the data (decompression).

There are two parameters for the ** procedure ** that must be specified: the degree of automation and the centralization (storage location).

For the degree of automation, a distinction must be made between manual and automatic:

* Manual data backup means that the data backup is triggered manually. It may be advantageous that the performer can individually customize the date of the backup to the workflow. Disadvantage is that the backup depends on the motivation and discipline of the employee. Due to illness or other reasons for absence, data backups may be canceled.
* Automatic backups are initiated programmatically on specific dates. It is advantageous that the backup is performed reliably, provided that the schedule is complete and up to date. The disadvantage may be that the schedule must be adapted to current changes or important changes are not immediately secured.
With regard to centralization, centralized and decentralized data backups can be distinguished:

* Central data backups are characterized by the fact that the storage location and the data backup are carried out on the central IT system. This procedure has the advantage that only one employee has to be intensively trained and the users are relieved of this work. A further advantage is that more cost-effective storage media can be used by the higher central data volume. The disadvantage is that possibly confidential data could be transferred and viewed by unauthorized persons.
* Decentralized data backups are performed by the users themselves, without having to transfer the data to a central IT system. It is advantageous that the user retains control of the data and the backup volumes, especially if they are confidential data. The disadvantage is that consistent data protection depends on the reliability of the user and that decentralized solutions demand time from the users.
After deciding whether the data backup is performed manually or automatically, centrally or remotely, the appropriate data medium or the appropriate storage medium for data backup must now be found. The following parameters can be considered for this:

* Volume Request Time: How long may it take for a backup volume to be available for recovery? Robot systems can do that within minutes, outsourced tapes may need to be transported and laid down consuming.
* Access time, transfer rate: how long a data backup takes and how fast data can be restored depends on the medium access time of the data carrier and on the transfer rate. Hard disks allow access to certain files in the millisecond range, a magnetic tape must first be spooled to the appropriate place and in the case of cloud storage, the transfer rate depends directly on the Internet connection.
* Storage capacity: The storage medium must have sufficient storage capacity. In the process, future data volumes must also be scheduled.
* Costs: The costs of the data backup must be in reasonable proportion to the security purpose. In this case, the lifetime of the disk is to be considered.
The following influencing factors (see CON.3.M1 * Survey of influencing factors of the data backup *) must be observed:

* Availability Requirements: The higher the availability requirements, the faster the media must be accessed as the storage medium of the backup, and the faster the required data must be re-recordable from the media.
* It must be ensured that the storage media can be used for recovery even if one of the readers fails. The compatibility and function of a replacement device must be ensured.
* Data and change volume: As data volumes increase, inexpensive storage media are often used.
* Deadlines: If deletion periods must be adhered to (eg for personal data), the selected storage medium must enable the deletion. Storage media that are not or only with great effort erasable (eg WORM), should be avoided in this case.
* Confidentiality requirements and integrity requirements of the data: If the confidentiality or integrity requirement of the data to be protected is high, this protection requirement is also transferred to the data carriers used for data backup. If encryption of the data backup is not possible, consideration can be given to the selection of data carriers which, due to their compact design, can be stored in data cabinets or vaults.
* Knowledge of IT users: The knowledge and data-processing capabilities of IT users determine whether or not to choose a policy in which the user himself or herself manually acts for data backup, whether other trained individuals perform data backup remotely, or if an automated one Data backup is more practical.
** Responsibility for data backup **

There are three groups of people responsible for deciding who is responsible for data protection: First, it may be the user himself (typically for decentralized and non-networked IT systems), the system administrator or an administrator specially trained for data protection. If the data backup is not carried out by the user, those responsible must be obliged to maintain secrecy regarding the data content. Maybe the data should also be encrypted.

In addition, the decision makers must be named, which can cause a recovery. It remains to be clarified who has the right to access data carriers, especially if they are outsourced to backup archives. It must be ensured that only authorized persons gain access. Finally, it must be defined who is authorized to carry out a restoration of the entire database or selected individual files.

In determining responsibility, particular attention must be paid to the confidentiality, integrity of the data and the trustworthiness of the responsible employees. It must be ensured that the responsible person is reachable and a representative is named and trained.

As influencing factor (see CON.3.M1 * Survey of influencing factors of the data backup *) please note:

* Knowledge of IT users: The knowledge and data processing-specific capabilities of IT users determine whether data backup should be carried out independently for each IT user. If the knowledge of IT users is insufficient, the responsibility must be transferred to the system administrator or a specially trained person.
** ** repository
As a general rule, backup media and original data media should be kept in different fire compartments (see CON.3.M12 * Suitable storage of backup media *). However, the further away the storage media, the longer the transport routes and thus the transport times can be, and the longer the recovery takes. As influencing factors (see CON.3.M1 * Survey of influencing factors of the data backup *), therefore, consider:

* Availability requirements: The higher the availability requirements, the faster the volumes of the backup must be available. If the data carriers are outsourced externally, it is to be considered in the case of very high availability requirements that copies of the data backup should also be available in the immediate vicinity.
* Confidentiality and integrity of the data: the higher this requirement is, the better it must be possible to prevent manipulation of the data carriers. The necessary access control can be achieved through appropriate infrastructural and organizational measures.
* Data volume: With increasing data volume, the security of the repository is increasingly important.
** Requirements for the backup archive **

Data backups have at least as high protection requirements with regard to confidentiality and integrity as the backed-up data itself. When storing data in a central back-up archive, correspondingly effective security measures are necessary, eg, security measures. B. an access control.

In addition, it must be ensured by organizational and personnel measures (disk management) that the fast and targeted access to required data carriers is possible. For this, the block OPS.1.2.2 * Archiving * must be observed.

The following influencing factors (see CON.3.M1 * Survey of influencing factors of the data backup *) must be observed:

* Availability requirements: The higher the availability requirements, the faster targeted access to required volumes must be possible. If manual inventory management does not meet availability requirements, automated access procedures can be used.
* Data volume: The data volume ultimately determines the type and number of storage media or the size of the online storage. For a correspondingly large volume of data, sufficient storage capacity must be provided in the data medium archive.
* Deadlines: If deletion deadlines are met, the organization of the backup archive must ensure that the data is deleted at the specified times. The process must be documented.
* Confidentiality and integrity of the data: the higher this need is, the more carefully it must be prevented that it can be manipulated on the data carriers. The necessary access control can be achieved through appropriate infrastructural and organizational measures.
** transport modalities **

During a data backup, data is transported. Be it that they are transmitted over a network or a line, whether it is that data carriers are transported to the data medium archive. The following should be noted:

* Availability requirements: The higher the availability requirements, the faster the data must be available for recovery. This must be taken into account when selecting the data transmission medium or when selecting the data carrier transport path.
* Data volume: If the data is transferred over a network for restoration, the transmission capacity of the network must be taken into account. It must be ensured that the data volume can be transferred within the required time (availability requirement).
* Change dates of the data: If data backups are carried out over a network (especially on selected dates), a capacity bottleneck can arise due to the volume of data to be transferred. Therefore, at the time of data backup, ensure sufficient data transfer capacity.
* Confidentiality and integrity of the data: the higher this requirement is, the more carefully it must be prevented that the data is intercepted, unauthorized copied or manipulated during transport. Finally, in the case of data transmissions, encryption or cryptographic protection against tampering must be considered. In the case of physical transport, secure containers and ways are to be used and, if necessary, also the benefits and costs of encryption must be weighed.
** ** Aufbewahrungsmodalität

As part of the data protection concept (see CON.3.M6 * Development of a data protection concept *), it should be considered whether storage or deletion periods must be adhered to for certain data.

* Deadlines: If retention periods are to be adhered to, the data should be archived (see OPS.1.2.2 Archiving). If deletion deadlines have to be met, the organizational procedure must be defined and the technical prerequisites must be created so that the data can be deleted at the given times.
#### CON.3.M3 Determination of legal factors influencing data backup

For the data backup a number of legal factors have to be considered, eg. B. Privacy laws. There are various legal requirements for the storage of certain information. Failure to comply with this may result in civil or criminal penalties. Therefore the responsible persons should inform themselves, which legal requirements are to be considered.

This results in requirements that must be taken into account in the data protection concept.

#### CON.3.M4 Creation of a minimal data backup concept

For an institution, it must be determined which minimum requirements for data backup must be adhered to. It serves as the basis for a data protection concept and generally applies to all IT systems and especially to new IT systems for which no data protection concept has yet been developed.

A minimal data backup concept can look like this:

* Software: It is all once purchased or self-created software to secure by a full backup.
* System data: All system data must be backed up at least once a month with one generation.
* Application data: All application data must be backed up at least once a week using full backup in the three-generation principle.
* Log data: All log data must be backed up at least once a month using full backup in the three-generation principle.
* Implementation: Used hardware and software, parameters used, procedure of data backup or recovery.
#### CON.3.M5 Regular data backup [IT operation]

After the preparatory work and the basic concept, regular backups must be carried out with the chosen procedure.

At least the data that can not be derived from other information must be backed up regularly. Documentations, program and program description must be provided.

It is recommended to create a data protection concept (see CON.3.M6 * Development of a data protection concept *).

Depending on the amount and importance of the data being re-stored and the possible damage caused by loss of this data, the following must be specified:

* Time interval examples: daily, weekly, monthly
* Timing examples: at night, on Fridays in the evening
* Number of generations to keep. Example: Daily full backup will keep the last seven backups, as well as Friday evening backups for the past two months.
* Scope of data to backup The easiest way is to specify partitions or directories that will be considered during regular backup. A suitable differentiation can increase the clarity and save effort and costs. Example: self-created files and individual configuration files
* Storage media (depending on the amount of data) Examples: DVDs, USB storage or hard drives
* Previous deletion of the media before reuse (eg for hard disks)
* Responsibility for implementation (administrator, user)
* Responsibility for monitoring the backup, especially in the case of automatic execution (error messages, remaining space on the storage media)
* Documentation of the created backups (date, type of execution of the backup as well as selected parameters, labeling of the data carriers)
Due to the great effort, full backups can usually be done at most once a day. The data created since the last backup can not be restored. Therefore, and to reduce costs, differential or incremental backups should be regularly performed between the full backups. Notes on the different types of backups can be found in CON.3.M2 * Setting the Backup Method *.

A differential or incremental backup can be more frequent, for example immediately after important files have been created or several times a day. Compatibility with ongoing operations must be ensured.

For software used, it must be decided separately whether it has to be recorded by the regular data backup. This depends, for example, on the cost of reinstalling and applying patches and updates. It may be sufficient to make backup copies of the original data media (see CON.3.M11 * Backup copy of the software used *).

All users should be informed about the data protection regulations (see CON.3.M10 * Data backup obligation *).

If only the server disks are backed up in networked computers, it must be ensured that the data to be backed up is regularly transferred by the users or automatically there. For major changes to IT systems or in the information network, the data backup process must be adapted accordingly.

Confidential data should be encrypted as far as possible before the backup, whereby it must be ensured that a decryption must be possible even after a longer period of time (see CON.3.M13 * Use of cryptographic procedures for data backup *).

The printout of data on paper is not an appropriate way of securing data.

### 2.2 Standard measures

Together with the basic measures, the following measures correspond to the state of the art in the field of "data backup concept".

#### CON.3.M6 Development of a data protection concept [Head of IT, specialist responsible]

The data protection procedure is determined by a large number of influencing factors: the IT system, the data volume, the frequency of the data change and the availability requirements are some of these factors. In the data protection concept, it is important to find a solution that takes these factors into account and at the same time is economically justifiable from a cost point of view.
The technical possibilities to carry out data backups are manifold. However, the selection is always determined by the factors mentioned. For this reason, it is first of all necessary to determine the influencing variables of the IT systems and the IT applications realized with them and document them comprehensibly (see CON.3.M1 * Survey of influencing factors of the data backup) *. Subsequently, the appropriate procedure must be developed and documented (see CON.3.M2 * Definition of the procedure for data backup *). Finally, the implementation must be arranged by the institution's management. The data protection concept must also provide for regular functional tests for data backup (see CON.3.M9 * Functional tests and check of recoverability *)

The results should be updatable and extensible in a data protection concept. A possible structure of a data protection concept is shown by way of example in the following table of contents:

** Contents Backup Concept **

**1. definitions **

* Application data, system data, software, log data
* Full backup, incremental backup
** 2nd Hazardous situation ** (** for motivation **)

* Dependence of the institution on the data
* Typical threats such as untrained users, shared databases, computer viruses, hackers, power failure, hard drive errors
* Institution-relevant causes of damage
* Damage in-house
** 3rd Influencing factors per IT system **

* Specification of the data to be backed up
* Availability requirements of the IT applications to the data
* Reconstruction of data without backup
* Data volume
* Change volume
* Change dates of the data
* Deadlines
* Confidentiality of the data
* Integrity requirements of the data
* Knowledge and data processing capabilities of IT users
** 4th Backup plan per IT system **

** 4.1 Specifications per data type ** and ** 4.2 Definition of the procedure for the data ** restoration

* Type of backup
* Frequency and timing of data backup
* Number of generations
* Backup medium
* Responsibility for data protection
* Repository of backup volumes
* Requirements for the backup archive
* Transport modalities
* Recovery times with existing backup
* Boundary conditions for the backup archive
 

 
+ Contract design (for external archives)
+ Refresh cycles of data backup
+ Inventory
+ Delete backups
+ Destruction of unusable data carriers
+ Provision of workable readers


 
5. Minimum data protection concept

6. Obligation of the employees for data backup

7. Sporadic Restoration Exercises

Individual points of this data protection concept are described in the measures CON.3.M1 * Determination of the factors influencing the data backup *, CON.3.M2 * Definition of the procedure for the data backup *, CON.3.M8 * Functional tests and check of the recoverability * and CON. 3.M10 * Obligation of the employees for data backup * detailed.

#### CON.3.M7 Procurement of a suitable data protection system [Head of IT, IT operation]

When purchasing a backup system, attention should be paid not only to its performance, but also to its usability and, in particular, its tolerance for user errors.

The backup software should meet the following requirements:

* The backup software should be able to detect an incorrect or corrupted media in the backup drive.
* It should work well with existing hardware.
* It should be possible to have backups done automatically at pre-selectable times or at adjustable intervals without the need for manual intervention (other than the need to provide backup media).
* It should be possible to automatically inform one or more selected users about the backup result and any error messages via e-mail or similar mechanisms. The execution of data backups including the backup result and possible error messages should be saved in a log file.
* The backup software should support backing up the backup media by password or even better by encryption. Furthermore, it should be able to store the saved data in compressed form.
* By specifying appropriate include and exclude lists for the file and directory selection, it should be possible to specify exactly which data should be saved and which should not. It should be possible to combine these lists into backup profiles, save them and reuse them for later backup runs.
* It should be possible to select the data to be backed up depending on the creation date or its last modification.
* The backup software should be able to generate logical and physical full copies as well as incremental copies (differential backups).
* The data to be backed up should also be stored on network drives or in online data stores.
* The backup software should be able to perform an automatic comparison of the backed up data with the original after the backup, and perform an appropriate comparison between the reconstructed data and the contents of the backup media after the data recovery.
* When restoring files, it should be possible to choose whether to restore the files to the original location or to another disk or directory. It should also be possible to control the behavior of the software in case a file with the same name already exists at the destination. You should be able to choose whether this file is always, never or only in the case that it is older than the file to be reconstructed, is overwritten, or that in this case an explicit request is made.
If the data protection can be password protected with the program used, this option should be used. The password must then be stored securely.

Most operating systems include backup programs. However, not all fulfill the demands on products for professional and comfortable data backups. However, if no other products are available, the system related programs should be used.

#### CON.3.M8 Function Tests and Recoverability Check [IT Operations]

If a dataset can not be restored, this can have many causes. There may be technical defects, incorrect parameters or simply obsolete media. Even if rules are not adhered to or the volumes are not properly managed, this can lead to irreparable errors.

In order to prevent this and to detect errors early on, it must be regularly checked whether the backed-up data can be reproduced easily and in a reasonable amount of time. If defects or other problems occur, they must be repaired as soon as possible.

Likewise, those responsible should regularly test whether the backup works as desired. If possible, the programs should be set so that in case of a failure (eg full backup medium) the responsible employee is automatically informed.

Furthermore, after a patch or update for the backup program, it must be checked whether the software is still working properly and z. B. no setting parameters were overwritten.

#### CON.3.M9 Prerequisites for online data backup [Head of IT, IT operation]
Creating a backup using an online storage service is typically initiated through a corresponding application on a user's client or on an institution's server. Also possible is z. For example, a hybrid model through an appliance: Here, the data is held locally on the appliance and additionally in an online storage service. In all cases, the data to be backed up over the Internet from a computer within the institution to a server of the online storage provider.

Depending on the provider, the handling of the transmitted data may vary. For example, many vendors support the storage and recovery of different versions of a file to be transferred. On the other hand, if the online storage provider does not offer versioning of files, the older file will be overwritten without any additional query and is thus no longer available for a restore. In this case, however, online storage does not meet the requirements for backup in the corporate or government environment. Institutions should therefore pay particular attention to the existing versioning of the data in order to prevent unwanted deletion of older versions of data.

As a general rule, the main focus should always be on the question of which protection requirements the secured data have, which legal obligations regarding the business-relevant data an institution is subject to and how it will be affected if data is lost or altered by unauthorized persons.

Many providers of online storage services are well aware that institutions place a high value on the availability of their data and keep their customers' data redundant. Institutions should make sure that the provider stores the data in different locations or in spatially separated data centers. If there are problems in one data center, the data will still be available in another data center.

Companies and authorities should not only value the secure storage of their data, but also question the implementation of the access options to the user accounts created. In corporate and governmental environments targeted attacks are conceivable, the intention of which is to block the user account and thus prevent access to the backup of the data. Such a denial-of-service attack usually uses different vulnerabilities, such as a combination of the automatic blocking of a user account in the event of failed login attempts and an unvalidated e-mail address. As a protective measure, the time-out principle can counteract such a targeted denial-of-service attack. The user account is not completely blocked, but only a renewed attempt to log in for a predetermined period prevented.

Not only are completeness and availability of their backed-up data of interest to institutions, but they place, among other things, to avoid legal consequences or a loss of image, also great value on their confidentiality and integrity. Institutions should therefore use encryption techniques to increase the level of security of transmission and data storage with external service providers.
Many providers of online storage solutions advertise the increased security through encryption. Here, however, must be analyzed in more detail how the encryption is implemented in practice. As a rule, only the actual transmission of the data is encrypted, for example via the establishment of an https connection (Hyper Text Transfer Protocol Secure). Before and after transport, however, the data is available in plain text in clear text. Some vendors provide their customers with additional encryption methods regardless of how the data is transported. However, the institution can often not rule out that an innate perpetrator, ie an employee of the online storage provider, procures the corresponding keys and thus can access the encrypted information, distort it or publish it. If an attacker gains access to the data by compromising the authentication, the provider's encryption is also ineffective.

If institutions see their data as particularly worthy of protection, they should encrypt it on their own systems and thus before the actual data transfer.

However, the need for a secure method of using online storage solutions, especially in the government or business environment, is increasingly being addressed by the market. In the meantime, a number of encryption solutions have been established, most of which have been specially tailored to work with online storage services. The programs already check during the installation whether a suitable folder of an online storage exists, and then create a corresponding subfolder in which the encrypted files are stored. Institutions using additional encryption software should be careful to choose a sufficiently strong password or other access protection for the application. In addition, a copy of the software solution used and the associated cryptographic keys should be stored in a secure location in order to be able to access the encrypted backups of the online storage in the event of a complete loss of data within the institution. For this purpose, the encryption software can be secured unencrypted with the online storage service, the key must of course be backed up differently. In this way, the institution is independent of whether the encryption software is still available after a longer period in a compatible version.

Institutions should also be satisfied that the recovery of stored data from online storage works properly and should also periodically test it (see CON.3.A8 * Functional Tests and Recoverability Check *).

#### CON.3.M10 Employee commitment to backup

All users should be informed about the data protection rules in order to be able to point out any shortcomings (for example, too short a time interval for their needs) or to make individual additions (for example, intermediate mirroring of important data on the own disk).

Also, informing users about how long the data is re-recordable is important. For example, if only two generations are kept with weekly full backup, depending on the time of the loss only two to three weeks left to rehome the data.
Employees who are tasked with creating backups should be informed and required to carefully follow the data protection concept or the minimum data protection concept. This is especially important where centrally performed backups do not apply, so z. B. in non-networked or mobile devices. Employees should be regularly reminded of the data backup and motivated to do so.

#### CON.3.M11 Backup copy of the software used [IT operation]

In case of problems with IT systems, it is often necessary to reinstall the operating systems and applications used in a timely manner. For this, all files required for installation must be available. Therefore, it is necessary to make copies and archive them in an appropriate location.

If the software is delivered on data carriers (eg DVDs or USB sticks), a backup copy should be made of the original data media or the original software for self-development, from which the software can be restored. The original data media and the backup copies must be kept separate from each other.

In particular, applications are often not delivered on data carriers, but only as separate installation files, as part of a package or software management or as source code packages. These installation sources should also be stored in a suitable location.

To install paid operating systems or applications, you often need to enter license numbers during installation. Therefore, it is necessary that in addition to the installation sources and the license numbers are appropriately stored. Unauthorized access to the installation media and license numbers must be excluded.

If the software has been translated from source code, the documentation should include all options used during translation (especially the options used to call any * configure * script). If the software was installed from a binary package, then all steps should be documented, with which the installation can be understood later.

Every change to a configuration file should be documented. It is recommended to use versioning. In addition, all configuration files must be backed up regularly.

#### CON.3.M12 Suitable storage of backup data carriers [IT operation]

Backup volumes are subject to special storage requirements:

* Access to these data media must be restricted to authorized persons.
* A sufficiently fast access must be guaranteed if necessary.
* The repository must also ensure the climatic conditions for longer-term storage of data media.
* In the event of an emergency, the backup media must be stored separately from the secure IT system, if possible in a different fire compartment.
### 2.3 Measures for increased protection requirements

The following are proposed measures that go beyond the state of the art level of protection and should be considered in case of increased protection needs. The letters in brackets indicate which basic values ​​are given priority protection by the measure (C = confidentiality, I = integrity, A = availability).

#### CON.3.M13 Use of cryptographic procedures in data protection [IT operation]

The confidentiality requirement of a file is transferred to the backup copy during a data backup. Therefore, with increased protection requirements, the backup should be encrypted.
For the backups, suitable encryption methods must be selected. The decisive feature of an encryption method is the quality of the algorithm as well as the key selection. Since the security suitability of encryption methods is limited by the technical development of hardware and software as well as advances in cryptography, they must be regularly updated according to the state of the art.

It must also be ensured that the keys are managed appropriately.

Further notes on cryptographic methods can be found in the module CON.1 * Crypto Concept *.

3 Further information
------------------------------

### 3.1 Worth knowing

Supplementary information is listed here that is not included in the measures, but nevertheless worthy of note. Currently there is no corresponding information for this module. The IT-Grundschutz hotline is happy to receive useful information at grundschutz@bsi.bund.de.

### 3.2 Literature

Additional information on hazards and security measures in the area of ​​"data protection concept" can be found in the following publications, among others:

* #### [27001] ISO / IEC 27001: 2013

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BKBU] Guide Backup / Recovery / Disaster Recovery

  

 Bitkom, 2016
 <Https://www.bitkom.org/noindex/Publikationen/2017/Leitfaden/170125-LF-Backup-Recovery.pdf>

 
* #### [ISF] The Standard of Good Practice

  

 Information Security Forum (ISF), 06.2016

 
* #### [NIST80053] Security and Privacy Controls for Federal Information Systems and Organizations

  

 Special Publication 800-53, Revision 4, NIST, 04.2013 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>
