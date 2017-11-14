from model.models import ResponsibleInit, ResponsibleImpl, Role, Countermeasure, Checking
Role.objects.create(name="Administrator",description="The administrator can do almost everything :)")
Role.objects.create(name="User",description="The user cannot do a lot of things :)")
Countermeasure.objects.create(id="M 1.1",name="Compliance with relevant standards and regulations",description="There are guidelines, standards or regulations for almost all areas of technology. These may have been issued by standardization organizations, industry associations, user groups or government institutions, eg. B. DIN (German Institute for Standardization), ISO (International Standards Organization), VDE (Association of Electrical Engineering, Electronics and Information Technology), VDMA (German Engineering Federation), VdS (Association of Property Insurers). These rules help ensure that technical equipment provides a sufficient level of protection for users and safety during operation. When planning and constructing buildings, during their operation and conversion, and when installing technical building equipment (eg internal supply networks such as telephone or data networks) and when purchasing and operating equipment, it is essential to comply with the relevant standards and regulations. The observance of standards is not a safety measure per se. It means that minimum requirements are met and the current state of the art and knowledge is respected.")
Checking.objects.create(description="Are all relevant standards and regulations taken into account in the planning, construction and reconstruction of buildings and the installation of technical equipment?",countermeasure=Countermeasure.objects.get(id="M 1.1"))