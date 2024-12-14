# Actividad: "Elección Estratégica del Modelo de Servicio en la Nube"

Esta tarea corresponde con la actividad del bloque 3 de la asignatura ETS y DJK.

Para más detalles de la tarea consultar el siguiente enlace: [Tarea](https://www3.gobiernodecanarias.org/medusa/eforma/campus/mod/assign/view.php?id=7823247)

## Integrantes del grupo

| Grupo | Integrante 1 | Integrante 2 |url repositorio|
| ----- | ------------ | --------------- |--------|
|     0 | Antonio [@toninavhd](https://github.com/toninavhd)| Leonardo [@Leopoldo777x](https://github.com/Leopoldo777x)|[Repositorio](https://github.com/toninavhd/1-DAW_pt2/tree/main/DJK/trabajo_grupo)|

### Supuesto a analizar:

**Problema A:**

Una startup tecnológica necesita alojar una **aplicación de alto rendimiento** que debe **escalar rápidamente durante eventos de tráfico elevado**. Además, requiere un **control total sobre la configuración de los servidores**, la red y el almacenamiento, con el objetivo de hilar fino en el hardware para **ahorrar costes**.

 - **Recomendación aportada:**

En este caso recomendariamos al cliente **IaaS (Infraestructura como Servicio)** ya que este modelo de computación en la nube que proporcionaría los recursos de TI ( *Tecnologías de la informacion*) virtualizados a través de Internet. En lugar de comprar y mantener servidores físicos, almacenamiento y redes por lo que esta opción **reduciría los costes iniciales** ofreciendo un servcio de calidad. 

A continuación hablaremos en mas detalle de las ventajas de este modelo.

### Ventajas de IaaS para una startup tecnológica

- **Escalabilidad:** Una de las principales ventajas del modelo ***IaaS*** es la *escalabilidad* esto significa que la empresa podrá ajustar los recursos y capacidad necesaria a demanda, esto supone una gran ventaja para empresas con un **trafico elevado**. El escalado puede ser de **dos tipos:**
<br>
  - **Escalado vertical**(hardware).
     Es cuando se debe de añadir más máquinas o servidores al sistema para que la carga esté mas distribuida.
  - **Escalado horizontal**(distribucion de sistema).
     Mejorar los recursos de una máquina o servidor existente, como aumentar la RAM o CPU.
<br>

- **Costos Reducidos:** Como se comentaba a manera introductoria en el apartado anterior, al **pagar solo por los recursos utilizados**, las startups como la de este caso pueden evitar los altos costos iniciales de la infraestructura necesaria para las exigentes necesidades de la misma y **reducir en gastos operativos**.
<br>

- **Control Total:** Ofrece un control completo sobre la configuración de los servidores, la red y el almacenamiento, permitiendo optimizar el rendimiento segun la demanda y los costos.
<br>

- **Flexibilidad:** Las empresas pueden elegir y configurar los recursos según sus necesidades y la demanda de el momento por lo que facilita la personalización y la adaptación a cambios rápidos.
<br>

- **Rapidez de Implementación:** Permite desplegar y gestionar aplicaciones rápidamente, acelerando el tiempo de llegada al mercado.

## Ejemplos de servicios Iaas

Hay varios servicios Iaas, a continuación, hablaremos en profundidad de tres de ellos y mencionaremos algunos mas mostrando sus características de forma mas resumida:

#### Amazon Web Services (AWS) EC2

- AWS ofrece una amplia gama de instancias EC2 que permiten un control total sobre la configuración de los servidores, la red y el almacenamiento. Además, AWS Auto Scaling puede ayudar a manejar picos de tráfico de manera eficiente. ***AWS*** fue lanzada oficalmente en 2006 por la compañía Amazon.
 **AWS** ofrece más de 200 servicios que abarcan una amplia gama de tecnologías, incluyendo computación, almacenamiento, bases de datos, análisis, redes, aprendizaje automático, inteligencia artificial, Internet de las Cosas (IoT) y seguridad. Dentro de sus **principales servicios esta**:

1. **Computación**:
   - **Amazon EC2 (Elastic Compute Cloud):** Ofrece capacidad de computación escalable en la nube, permitiendo a los usuarios lanzar y gestionar instancias de servidores virtuales. **Recomendamos este servicio para nuestra empresa.**
   - **AWS Lambda**: Ejecuta código sin necesidad de aprovisionar o gestionar servidores, ideal para aplicaciones sin servidor.

2. **Almacenamiento**:
   - **Amazon S3 (Simple Storage Service):** Proporciona almacenamiento de objetos escalable y duradero, utilizado para almacenar y recuperar cualquier cantidad de datos en cualquier momento.
   - **Amazon EBS (Elastic Block Store):** Ofrece almacenamiento en bloque persistente para instancias EC2.

3. **Bases de Datos**:
   - **Amazon RDS (Relational Database Service):** Facilita la configuración, operación y escalado de bases de datos relacionales en la nube.
   - **Amazon DynamoDB**: Una base de datos NoSQL completamente gestionada que proporciona rendimiento rápido y predecible con escalabilidad automática.

4. **Redes y Entrega de Contenido:**
   - **Amazon VPC (Virtual Private Cloud):** Permite aprovisionar una sección aislada de la nube de AWS para lanzar recursos en una red virtual definida.
   - **Amazon CloudFront**: Un servicio de red de entrega de contenido (CDN) que distribuye datos, videos, aplicaciones y APIs a usuarios globalmente con baja latencia y altas velocidades de transferencia.

5. **Seguridad, Identidad y Cumplimiento:**
   - **AWS IAM (Identity and Access Management)**: Gestiona el acceso a los servicios y recursos de AWS de manera segura.
   - **AWS Shield**: Proporciona protección contra ataques DDoS para las aplicaciones alojadas en AWS.
<br>

#### Microsoft Azure Virtual Machines:

- Azure ofrece una infraestructura de alto rendimiento con opciones de escalabilidad automática. Además, Azure proporciona un control detallado sobre la configuración de los servidores y la red, lo que puede ayudar a optimizar costos.
  Algunas de sus **principales características son:**

1. **Compatibilidad con Múltiples Sistemas Operativos:**
   - Azure Virtual Machines soporta una variedad de sistemas operativos, incluyendo Windows, Linux y otros sistemas operativos personalizados.

2. **Escalabilidad y Flexibilidad:**
   - Permite escalar automáticamente hasta miles de máquinas virtuales según la demanda o las programaciones definidas con Virtual Machine Scale Sets.
   - Ofrece opciones de escalado horizontal y vertical para adaptarse a las necesidades cambiantes de las aplicaciones.

3. **Rendimiento y Alta Disponibilidad:**
   - Mejora el rendimiento de la red y el almacenamiento con el hardware personalizado de Azure Boost y el diseño optimizado del hipervisor.
   - Garantiza una alta disponibilidad con un Acuerdo de Nivel de Servicio (SLA) del 99.99%.

4. **Seguridad y Cumplimiento:**
   - Proporciona seguridad integrada con Azure Security Center y Azure Defender.
   - Cumple con una amplia gama de certificaciones de cumplimiento y normativas de seguridad.

5. **Copia de Seguridad y Recuperación:**
   - Ofrece soluciones de copia de seguridad y recuperación ante desastres rápidas y confiables con Azure Backup y Azure Site Recovery.

6. **Optimización de Costos:**
   - Permite optimizar los costos mediante reservas de Azure, Azure Spot Virtual Machines y la Ventaja Híbrida de Azure.
   - Proporciona herramientas como Microsoft Cost Management para gestionar y optimizar el gasto en la nube.

   Además ***Microsoft Azure*** también puede utilizarse para:

- **Desarrollo y Pruebas**: Crear entornos de desarrollo y pruebas rápidamente sin necesidad de invertir en hardware físico.
- **Aplicaciones Empresariales**: Ejecutar aplicaciones empresariales críticas, como bases de datos, ERP y CRM, en un entorno seguro y escalable.
- **Computación de Alto Rendimiento**: Utilizar máquinas virtuales optimizadas para HPC para ejecutar cargas de trabajo intensivas en computación, como simulaciones científicas y análisis de datos.

#### IBM Cloud:
- IBM Cloud es una plataforma de computación en la nube ofrecida por IBM, diseñada para proporcionar una amplia gama de servicios y soluciones en la nube. Esta plataforma está preparada para la inteligencia artificial (IA), es segura y está diseñada para entornos híbridos.

Alguna de sus **características mas importantes** son:

1. **Computación y Servidores**:
   - **IBM Cloud Virtual Servers**: Proporciona servidores virtuales escalables y flexibles para diversas cargas de trabajo.
   - **IBM Bare Metal Servers**: Ofrece servidores físicos dedicados para un rendimiento máximo y control total.

2. **Almacenamiento**:
   - **IBM Cloud Object Storage**: Ofrece almacenamiento de objetos escalable y duradero para grandes volúmenes de datos.
   - **IBM Block Storage**: Proporciona almacenamiento en bloque de alto rendimiento para aplicaciones críticas.

3. **Bases de Datos**:
   - **IBM Db2 on Cloud**: Una base de datos SQL completamente gestionada que ofrece alta disponibilidad y escalabilidad.
   - **IBM Cloudant**: Una base de datos NoSQL distribuida y completamente gestionada para aplicaciones web y móviles.

4. **IA y Machine Learning**:
   - **IBM Watson**: Ofrece una suite de herramientas de IA y machine learning para desarrollar e implementar modelos de IA.
   - **IBM Watson Studio**: Proporciona un entorno colaborativo para científicos de datos, desarrolladores y analistas.

5. **Seguridad y Cumplimiento**:
   - **IBM Cloud Security**: Proporciona soluciones de seguridad integradas para proteger datos y aplicaciones en la nube.
   - **IBM Key Protect**: Ofrece gestión de claves de cifrado para proteger datos sensibles.

Sus principales ventajas son:

- **Resiliencia**: IBM Cloud está diseñado para ofrecer alta disponibilidad y recuperación ante desastres, asegurando que las aplicaciones y los datos estén siempre accesibles.
- **Seguridad**: Proporciona un entorno seguro con múltiples capas de protección y cumplimiento de normativas.
- **Escalabilidad**: Permite escalar recursos de manera flexible para adaptarse a las necesidades cambiantes del negocio.
- **Innovación**: Ofrece acceso a tecnologías avanzadas, incluyendo IA y machine learning, para impulsar la innovación empresarial.
 
<br>

#### Otras plataformas IaaS:
Hay muchas mas plataformas que ofrecen este tipo de servicio, las siguientes nos parecen dignas de mención dada su popularidad:

- **DigitalOcean Droplets**: Si buscas una opción más económica pero aún potente, DigitalOcean ofrece Droplets que son fáciles de configurar y escalar. También proporcionan un control total sobre la configuración del servidor. El sitema de Droplets es novedoso de facil uso e intuitivo por lo que nos pareció conveniente nombrarlo.

<br>

- **Google Cloud Platform (GCP) Compute Engine**: GCP proporciona máquinas virtuales altamente personalizables y escalables. Con herramientas como Google Kubernetes Engine (GKE), puedes gestionar contenedores de manera eficiente, lo que es ideal para aplicaciones que necesitan escalar rápidamente.


## Analisis económico de los servicios

- **Amazon Web Services (AWS)**: esta empresa ofrece un sistema de pago por uso para la mayoría de sus servicios.

  Para esta empresa, escogiendo el servicio **EC2**, con una **instancia dedicada** para poder mantener un control sobre la configuración del servidor, y no compartir recursos con otros clientes, suponiendo unos picos elevados de **8 horas la mitad de días de la semana**, con una infraestructura de:

  - **8 vCPUs**.
  - **16 GiB de memoria**.
  - **Rendimiento de red de hasta 10 Gigabit**.

  Escogiendo una opción de pago **bajo demanda** para maximizar la flexibilidad, daría un costo mensual de:

  - **$0.34 dólares la hora**.
  - **$189 dólares mensuales**, lo cual sería aproximadamente unos **180 euros**.

 <br>

- **Microsoft Azure Virtual Machines**: Para esta empresa, suponiendo un servidor similar al del supuesto anterior, con las siguientes características:

  - **8 vCPUs**.
  - **16 GiB de memoria**.
  - **Rendimiento de transferencia de hasta 10 Gbps**.

  En un modelo de **pago por uso**, el costo mensual estimado sería de:

  - **270€ mensuales**, el cual puede variar según la **región de despliegue** y el **tipo de soporte**.

 <br>

- **IBM Cloud (Servidor Dedicado)**: Para IBM Cloud, suponiendo un servidor dedicado con las siguientes características:

  - **8 vCPUs**.
  - **16 GiB de memoria**.
  - **Rendimiento de transferencia de hasta 1 Gbps**.
  - **Ubicado en Europa Occidental**.

  El costo mensual estimado sería un estimado de:

  - **320€ mensuales**.

