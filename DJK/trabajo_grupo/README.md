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

- **Amazon Web Services (AWS) EC2**: AWS ofrece una amplia gama de instancias EC2 que permiten un control total sobre la configuración de los servidores, la red y el almacenamiento. Además, AWS Auto Scaling puede ayudar a manejar picos de tráfico de manera eficiente.

<br>

- **Google Cloud Platform (GCP) Compute Engine**: GCP proporciona máquinas virtuales altamente personalizables y escalables. Con herramientas como Google Kubernetes Engine (GKE), puedes gestionar contenedores de manera eficiente, lo que es ideal para aplicaciones que necesitan escalar rápidamente.

<br>

- **Microsoft Azure Virtual Machines**: Azure ofrece una infraestructura de alto rendimiento con opciones de escalabilidad automática. Además, Azure proporciona un control detallado sobre la configuración de los servidores y la red, lo que puede ayudar a optimizar costos.

<br>

- **DigitalOcean Droplets**: Si buscas una opción más económica pero aún potente, DigitalOcean ofrece Droplets que son fáciles de configurar y escalar. También proporcionan un control total sobre la configuración del servidor.

<br>

- **IBM Cloud**: IBM Cloud ofrece infraestructura como servicio (IaaS) con un alto grado de personalización y control. Es ideal para aplicaciones que requieren un rendimiento constante y la capacidad de escalar rápidamente.

<br> 

## Analisis economico de los servicios

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

