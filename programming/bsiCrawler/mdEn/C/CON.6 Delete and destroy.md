1 description
--------------

### 1.1 Introduction

To ensure that information does not fall into the wrong hands, a regulated procedure is required to completely and reliably erase or destroy data and data carriers. Protective information stored on analog and digital media must be considered.

If not or insufficiently deleted data carriers are passed on, sold or discarded, inadvertently valuable information can be passed on and considerable damage can occur. Therefore, every institution must have a procedure for secure deletion and destruction.

### 1.2 Objective

This module describes how to safely delete and destroy information in institutions and how to create a corresponding concept for it.

### 1.3 Delimitation

The module only contains the general procedural, technical and organizational requirements for deletion and destruction. Individual building blocks of the layers CON (concepts and procedures), security management (ISMS), ORP (organization and personnel), OPS (operation), DER (detection and reaction), IND (industrial IT), APP (applications), SYS (IT) Systems), NETs (networks and communication) and INFs (infrastructure) can define supplementary and more specific requirements for deletion and destruction. In particular, the building blocks OPS.1.1.6 * Data backup *, OPS 1.2.2 * Archiving, * OPS.1.2.3 * Information and data medium exchange and * OPS.1.2.7 * Sales / Disposal of IT * must be taken into account in addition, because these topics are directly related to the deletion and annihilation.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the area of ​​deletion and destruction:

### 2 1 Lacking or insufficiently documented regulations on deletion and destruction

If there are no documented processes and procedures for deleting and destroying information and media, or if they are not being applied correctly, sensitive information can not really be safely destroyed and fall into the wrong hands. This risk is particularly high for discarded data carriers and IT systems, since information may remain on them due to insufficient regulations. These data could be read or stolen by unauthorized third parties. If this includes existential information, the entire institution would be endangered.

### 2 2 Confidentiality loss due to remaining information on data carriers

In the case of electronic data transmission or data carrier forwarding, it happens again and again that also information is passed on which the institution should not leave.

For most file systems, files that the user deletes are not really destroyed. Only the references to the file are deleted from the management information of the file system and the blocks belonging to the file are marked as free. However, the actual content of the blocks on the disk is retained and can be reconstructed using appropriate tools. This allows attackers to gain access to the file. B. if such data carriers are passed on to third parties or disposed of inappropriately. For example, confidential information could be leaked out.

### 2 3 Unstructured data management
Due to inadequate specifications, as well as lack of training of the employees, information can be stored cluttered on used data carriers. This can lead to the fact that information can not be completely deleted, because no one knows more, what is stored in which files. Also, attackers may be able to access information unnoticed if many copies of a file exist and they exist in different directories with different protection functions. Copies are often not just stored in different directories of a volume. It is much more critical if several copies are stored on different data carriers and it is no longer clear where, what was filed and when. This problem is compounded when disks are procured remotely and are not controlled. Unstructured data management jeopardizes both the availability (working with the data) and the integrity and confidentiality.

### 2 4 Confidentiality loss through paging and temporary files

Swap files or paging partitions may contain sensitive data, such as: Passwords or cryptographic keys. However, the paging files and thus also the information contained therein are not protected because they z. B. can be read when the hard drive is removed and installed in another IT system.

In addition, during operation of many applications, files are generated that are not required for productive operation (eg browser history). These files may also contain security-related information. If paging or temporary files are not securely deleted, unauthorized access to sensitive information, passwords, and keys can be used to gain access to other IT systems and data, to gain competitive advantage in the marketplace, or to deliberately spy on user behavior.

### 2 5 Unsuitable disposal of data media and documents

If media or documents are not properly disposed of, it may be possible to extract information that should not be in the hands of third parties. Thus, attackers z. B. stealing media from inadequately secured disposal facilities. Even if commissioned disposal service providers are insufficiently controlled, confidentiality can not be sufficiently ensured.

3 requirements
---------------

The following are specific requirements for the Delete and Destroy area. Basically, the ISB is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic Requirements

The following requirements MUST be implemented as a priority:

#### CON.6.A1 Regulation of the procedure for the deletion and destruction of information [Head of IT, Head of Organization]

The institution MUST regulate the deletion and destruction of information. Depending on the organizational unit, it is necessary to regulate which information and resources may be deleted and disposed of under which conditions. Likewise, it must be determined in which spatial areas disposal and destruction facilities should be set up.
In addition, it is necessary to determine in the planning phase who is responsible for the deletion and destruction of information and resources and which interfaces exist between the organizational units. Likewise, the flow of information must be regulated internally and between the institution's officers and possible outsourcing service providers.

#### CON.6.A2 Proper disposal of equipment and information worthy of protection [Staff, Head of IT, Head of Building Services]

All sensitive information and equipment MUST be safely disposed of. For this purpose, secured and appropriate disposal facilities MUST be available on the premises of the institution. It MUST also be taken into account that information and resources may first be collected and then disposed of later. Such a central collection point MUST be protected against unauthorized access.

If external service providers are commissioned, the disposal process MUST be sufficiently secure and traceable. The companies responsible for the disposal SHOULD regularly be checked to see whether the disposal process still corresponds to the target state.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of extinguishing and destruction. They SHOULD be implemented in principle.

#### CON.6.A3 Erasing the media before and after the exchange [specialist responsible]

Before distributing previously used media or reusing it, all data on it should be securely deleted. For this purpose, suitable procedures SHOULD be available to the employees (see CON.6.A4 * Selection of suitable procedures for the deletion or destruction of data carriers *).

#### CON.6.A4 Selection of appropriate methods for deleting or destroying data carriers [Head of IT, Head of Organization]

For erasure and destruction, appropriate procedures should be selected. For example, there should always be suitable devices and tools for various types of data carriers with which the responsible employee can delete or destroy the stored information. It SHOULD be regularly checked whether the chosen procedures still correspond to the state of the art and are still sufficiently safe for the institution. The selected procedures SHOULD be known to all employees.

#### CON.6.A5 Regulated decommissioning of IT systems and data carriers [IT operation, employees, responsible persons, IT managers]

It SHOULD be regulated and documented how IT systems and data carriers are to be decommissioned. It should be ensured that all information stored on an IT system or data carrier is safely erased prior to disposal. When screening out, apart from "classic" IT systems, all IT systems that contain persistent storage elements SHOULD also be taken into account.

#### CON.6.A6 Instruction of all employees in the methods for the deletion or destruction of information [Head IT]

All employees SHOULD be briefed on the methods and procedures for deleting and destroying information. In doing so, the requirements of the module * ORP.3 Sensitization and Training * SHOULD be followed.

#### CON.6.A7 Elimination of residual information [IT operations, employees]

When distributing media and files, make sure that they do not contain any so-called residual information. For this, a process in the institution SHOULD be established and documented. In order for the employees to implement it sufficiently, they SHOULD be informed about the dangers of residual and additional information in files. It SHOULD be checked randomly whether the remaining information contained in files is actually deleted.
#### CON.6.A8 Policy on the Deletion and Destruction of Information [Staff, Head of IT, Data Protection Officer]

The regulations of the institution for * * deletion and destruction SHOULD be documented in a guideline. The guideline SHOULD be known to all relevant responsible persons and employees of the institution and form the basis for their work and actions. The content of the guideline SHOULD include all used data media, applications, IT systems and other resources and information that are affected by deletion and destruction. It SHOULD regularly and randomly check if the employees comply with the policy. The guideline SHOULD be updated regularly.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### CON.6.A9 Selection of appropriate methods for deleting or destroying data carriers with increased protection requirements [Head of IT, Head of Organization] (CIA)

For extinguishing and destroying, methods should be selected that meet the increased protection requirements of information and equipment.

#### CON.6.A10 Procurement of appropriate equipment for deletion or destruction of data [Head of Organization, Head of IT, Procurement Unit] (CIA)

Before acquiring equipment for deleting or destroying data SHOULD create a requirement documentation to compare the tools available on the market.

#### CON.6.A11 Destruction of data media by external service providers [Head of Organization, Data Protection Officer] (CIA)

On the premises of the institution, all data carriers to be destroyed SHOULD be stored securely against unauthorized access until they have been picked up by the external service provider. The removal SHOULD also be protected according to the protection requirement. The institution SHOULD have the disposal process checked regularly by trained persons.

In addition, the general requirements for service providers and their employees described in OPS.2.1 * Outsourcing Usage * SHOULD be implemented.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area of ​​"Deletion and destruction" can be found in the following publications, among others:

* #### [27001A8.3] ISO / IEC 27001: 2013 - Annex A.8.3 Media handling

  

 ISO, Information technology- Security techniques- Information security management system- Requirements, in particular Annex A, A.8.3 Media handling, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [DIN663991] DIN 66399-1: 2012-10 Office and data technology Part 1

  

 Part 1: Fundamentals and Terms, 2012

 
* #### [DIN663992] DIN 66399-2: 2012-10 Office and data technology Part 2

  

 Part 2: Requirements for Destruction Machines, 2012

 
* #### [DIN663993] DIN SPEC 66399-3: 2013-02 - Office and data carrier technology Part 3

  

 Part 3: Data Destruction Process, 2013

 
* #### [SP80088] NIST Special Publication 800-88 Revision 1

  

 NIST, Guidelines for Media Sanitation, 12.2014
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "Delete and Destroy".

* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.31 Incorrect use or administration of devices and systems
* G 0.44 Unauthorized intrusion into premises
The cross reference tables can be found in the download area due to their size.
